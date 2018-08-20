package org.autonlab.anomalydetection;

import com.datastax.driver.core.*; //cassandra
import com.savarese.spatial.*;
import java.util.*;
import org.joda.time.*;
import org.javatuples.*;
import java.text.DateFormat;

public class DataIOCassandraDB implements DataIO {
    private Session _session = null;
    private String _keyspace;
    private String _hostname;
    private String _table;
    private ArrayList<String> _categoryFieldsList;
    private ArrayList<String> _valueFieldsList;
    private Cluster _cluster;

    public DataIOCassandraDB(String hostname, String keyspace, String table) {
	_cluster = Cluster.builder().addContactPoint(hostname).build();
	_session = _cluster.connect();

	_keyspace = keyspace;
	_hostname = hostname;
	_table = table;
	if (_table == null) {
	    _table = "packet_twong";
	}

	_categoryFieldsList = new ArrayList<String>();
	_categoryFieldsList.add("source_addr");
	_categoryFieldsList.add("text_values.endpoint");

	_valueFieldsList = new ArrayList<String>();
	_valueFieldsList.add("time_stamp"); // timestamp must be first
	_valueFieldsList.add("text_values.messagetype");
	_valueFieldsList.add("dest_addr");
    }

    /*
     * @param categoryFieldsCSV a CSV of DB column names to categorize the histograms by
     */
    public void setCategoryFields(String categoryFieldsCSV) {
	String[] sParts = categoryFieldsCSV.split(",");
	Arrays.sort(sParts);
	_categoryFieldsList = new ArrayList<String>();

	for (int ii = 0; ii < sParts.length; ii++) {
	    _categoryFieldsList.add(sParts[ii]);
	}
    }

    /*
     * @param valueFieldsCSV a CSV of DB column names to generate histograms on
     */
    public void setValueFields(String valueFieldsCSV) {
	String[] sParts = valueFieldsCSV.split(",");
	Arrays.sort(sParts);
	_valueFieldsList = new ArrayList<String>();

	_valueFieldsList.add("time_stamp");

	for (int ii = 0; ii < sParts.length; ii++) {
	    _valueFieldsList.add(sParts[ii]);
	}
    }

    public String packetStats(int minutesBack) {
	DateTime startTime = null;
	String statementExtra = new String();
	Date highestDate = null;
	Date lowestDate = null;

	if (minutesBack > 0) {
	    startTime = DateTime.now(DateTimeZone.UTC).minusMinutes(minutesBack);
	    statementExtra += " WHERE time_stamp > '" + startTime + "' ALLOW FILTERING";
	}

	String selectStatement = "SELECT time_stamp FROM " + _keyspace + "." + _table + statementExtra;
	ResultSet results = _session.execute(selectStatement);
	int rowCount = 0;
	for (Row row: results) {
	    if (highestDate == null) {
		highestDate = row.getDate("time_stamp");
	    }
	    else if (row.getDate("time_stamp").after(highestDate)) {
		highestDate = row.getDate("time_stamp");
	    }
	    if (lowestDate == null) {
		lowestDate = row.getDate("time_stamp");
	    }
	    else if (row.getDate("time_stamp").before(lowestDate)) {
		lowestDate = row.getDate("time_stamp");
	    }
	    rowCount++;
	    if ((rowCount % 1000) == 0) {
		System.out.println("Read in " + rowCount + " rows");
	    }
	}

	long diff = (highestDate.getTime() - lowestDate.getTime()) / 1000;
	String output = new String();
	Double rate = new Double(new Double(rowCount)/new Double(diff));
	int sample = (int)(400/rate);
	int slide = (int)(400/rate/6);
	output += rowCount + " packets in " + diff + " seconds (" + rate + "/sec).\n<br>";
	output += "To get about 400 packets in a window, try a window width of " + sample + " seconds\n<br>";
	output += "and a slide width of 1/6 that, or " + slide + " seconds\n\n<br><br>";
	output += "<a href=setSampleWindowSecs/" + sample + ">Set sample window to " + sample + " seconds</a>\n<br><br>";
	output += "<a href=setSlideWindowSecs/" + slide + ">Set slide window to " + slide + " seconds</a>\n<br><br>";
	return output;
    }

    String dateString = null;
    /* histogram value names -> category names -> histograms */
    public HashMap<GenericPoint<String>, HashMap<GenericPoint<String>, ArrayList<HistoTuple>>> getData(int minutesBack, int ignoreMinRecent, int useNow) {
	HashMap<GenericPoint<String>, HashMap<GenericPoint<String>, ArrayList<HistoTuple>>> trainMap = new HashMap();
	Date highestDate = null;

	// this is a dumb way of doing this: We want the most recent timestamp in the database
	// but we can't query it from Cassandra. We loop through every record and find the highest
	DateTime endTime = null;
	DateTime startTime = null;
	if ((minutesBack > 0 || ignoreMinRecent > 0) && useNow ==0) {
	    String selectStatement = "SELECT time_stamp FROM " + _keyspace + "." + _table;
	    ResultSet results = _session.execute(selectStatement);
	    int rowCount = 0;
	    for (Row row: results) {
		if (highestDate == null) {
		    highestDate = row.getDate("time_stamp");
		}
		else if (row.getDate("time_stamp").after(highestDate)) {
		    highestDate = row.getDate("time_stamp");
		}
		rowCount++;
		if ((rowCount % 1000) == 0) {
		    System.out.println("Read in " + rowCount + " rows");
		}
	    }
	    if (highestDate != null) {
		endTime = new DateTime(highestDate.getTime(), DateTimeZone.UTC);
		if (minutesBack > 0) {
		    startTime = endTime.minusMinutes(minutesBack);
		}
		if (ignoreMinRecent > 0) {
		    endTime = endTime.minusMinutes(ignoreMinRecent);
		}
	    }

	    // This happens if the database is empty
	    //if (endTime == null || startTime == null) {
		//return null;
		//}
	}
	if ((minutesBack > 0 || ignoreMinRecent > 0) && useNow > 0) {
	    endTime = DateTime.now(DateTimeZone.UTC);
	    if (minutesBack > 0) {
		startTime = endTime.minusMinutes(minutesBack);
	    }
	    if (ignoreMinRecent > 0) {
		endTime = endTime.minusMinutes(ignoreMinRecent);
	    }
	}


	int getTextValues = 0;

	// build a SELECT statement that pulls out all of the database columns that we want
	String selectStatement = "SELECT ";
	HashMap<String, Integer> fieldsSeen = new HashMap();
	// get the column names for our data's keys
	for (String oneField : _categoryFieldsList) {
	    int oneFieldEnd = oneField.indexOf(".");
	    if (oneFieldEnd == -1) {
		oneFieldEnd = oneField.length();
	    }
	    else {
		getTextValues = 1;
	    }
	    String oneFieldName = oneField.substring(0, oneFieldEnd);

	    // XML fields are all stored as a hash inside one DB column so we want to be sure not to request duplicate column names
	    if (!fieldsSeen.containsKey(oneFieldName)) {
		selectStatement += oneFieldName + ",";
		fieldsSeen.put(oneFieldName, 1);
	    }
	}
	// get the column names for our data's histogram values
	for (String oneField : _valueFieldsList) {
	    int oneFieldEnd = oneField.indexOf(".");
	    if (oneFieldEnd == -1) {
		oneFieldEnd = oneField.length();
	    }
	    else {
		getTextValues = 1;
	    }
	    String oneFieldName = oneField.substring(0, oneFieldEnd);

	    // XML fields are all stored as a hash inside one DB column so we want to be sure not to request duplicate column names
	    if (!fieldsSeen.containsKey(oneFieldName)) {
		selectStatement += oneFieldName + ",";
		fieldsSeen.put(oneFieldName, 1);
	    }
	}

	selectStatement = selectStatement.substring(0, selectStatement.length() - 1); // drop the trailing comma from above
	selectStatement += " FROM " + _keyspace + "." + _table;
	if (startTime != null || endTime != null) {
	    selectStatement += " WHERE ";

	}
	if (startTime != null) {
	    selectStatement += " time_stamp > '" + startTime + "' ";
	}
	if (endTime != null) {
	    if (startTime != null) {
		selectStatement += " AND ";
	    }
	    selectStatement += " time_stamp < '" + endTime + "' ";
	}


	if (startTime != null || endTime != null) {
	    selectStatement += " ALLOW FILTERING";
	}
	System.out.println("Statement is " + selectStatement);
	ResultSet results = _session.execute(selectStatement);

	// get the data we want out of what the database returned
	// some of the db columns are hashses of more values, so we have to be smart about pulling those out too 
	int rowCount = 0;
	int categoryFieldsListSize = _categoryFieldsList.size();//cache these outside of the loops to save recalculation
	int valueFieldsListSize = _valueFieldsList.size() - 1; // -1 because  we don't want to count time_stamp

	HashMap< GenericPoint<String>, Double> highestDateSeen = new HashMap();

	for (Row row: results) {
	    GenericPoint<String> category = new GenericPoint<String>(categoryFieldsListSize);
	    Map<String, String> fieldMap = new HashMap(); // initializing this isn't needed but Java complains
	    if (getTextValues == 1) {
		fieldMap = row.getMap("text_values", String.class, String.class);
	    }

	    // build the category here. We have to do this inside the loop because the category
	    // contains the name's value that we see in the record
	    int ii = 0;
	    for (String oneField : _categoryFieldsList) {
		String categoryString = oneField + ";";
		if (oneField.equals("time_stamp")) {
		    categoryString += (row.getDate("time_stamp").getTime() / 1000);
		}
		else if (oneField.matches("^text_values.*$")) {
		    if (getTextValues == 0) {
			throw new RuntimeException("didn't retrieve text_values from DB but need it");
		    }
		    int oneFieldStart = oneField.indexOf(".");
		    if (oneFieldStart == -1) {
			throw new RuntimeException("did not find a period in field " + oneField);
		    }
		    String oneFieldTrailing = oneField.substring(oneFieldStart + 1, oneField.length());
		    categoryString += (fieldMap.get(oneFieldTrailing));
		}
		else {
		    String fieldValue = row.getString(oneField);
		    categoryString += (fieldValue == null ? "" : fieldValue);
		}
		category.setCoord(ii, categoryString);
		ii++;
	    }

	    if (!_valueFieldsList.get(0).equals("time_stamp")) {
		throw new RuntimeException("First value field was not time_stamp");
	    }
	    double dateSecs = (row.getDate("time_stamp").getTime() / 1000);
	    String value = "";
	    GenericPoint<String> valueNamePoint = new GenericPoint<String>(valueFieldsListSize);
	    ii = 0;
	    for (String valueName : _valueFieldsList) {
		if (valueName.equals("time_stamp")) {
		    continue;
		}
		valueNamePoint.setCoord(ii, valueName);
		if (valueName.matches("^text_values.*$")) {
		    if (getTextValues == 0) {
			throw new RuntimeException("didn't retrieve text_values from DB but need it");
		    }
		    int oneFieldStart = valueName.indexOf(".");
		    if (oneFieldStart == -1) {
			throw new RuntimeException("did not find a period in field " + valueName);
		    }
		    String oneFieldTrailing = valueName.substring(oneFieldStart + 1, valueName.length());
		    value += fieldMap.get(oneFieldTrailing) + ",";
		}
		else {
		    value += row.getString(valueName) + ",";
		}
		if (value == null) {
		    throw new RuntimeException("Failed to get value for column " + valueName);
		}
		// When we get to the point where we can customize the values we save, we might need to overwrite this cached value
		ii++;
	    }

	    value = value.substring(0, value.length() - 1); // to drop the trailing comma appended above

	    if (!trainMap.containsKey(valueNamePoint)) {
		trainMap.put(valueNamePoint, new HashMap<GenericPoint<String>, ArrayList<HistoTuple>>());
	    }
	    if (!trainMap.get(valueNamePoint).containsKey(category)) {
		trainMap.get(valueNamePoint).put(category, new ArrayList<HistoTuple>());
	    }
	    HistoTuple newTuple = new HistoTuple(dateSecs, value, valueNamePoint);

	    if (!highestDateSeen.containsKey(category)) {
		highestDateSeen.put(category,new Double(-1));
	    }

	    // we have to sort the data here because Cassandra won't do it for us
	    if (dateSecs > highestDateSeen.get(category)) {
		//System.out.println(dateSecs + ">"+highestDateSeen);
		highestDateSeen.put(category, dateSecs);
		trainMap.get(valueNamePoint).get(category).add(newTuple);
	    }
	    else {
		for (int sort_i = 0; sort_i < trainMap.get(valueNamePoint).get(category).size(); sort_i++) {
		    //System.out.println(trainMap.get(valueNamePoint).get(category).get(sort_i)._timeStamp +" vs "+dateSecs);
		    if (trainMap.get(valueNamePoint).get(category).get(sort_i)._timeStamp >= dateSecs) {
			trainMap.get(valueNamePoint).get(category).add(sort_i, newTuple);
			break;
		    }
		}
	    }

	    rowCount++;
	    if ((rowCount % 1000) == 0) {
		System.out.println("Read in " + rowCount + " rows");
	    }

	}
	results = null;

	if (trainMap.size() == 0) {
	    return null;
	}

	return trainMap;
    }

    public void putData(String categoryCSV, int dateSecs, String messageType) {
    // from group meeting, we're going to write to a different db not the cassandra one so we won't reimplement this in a dynamic category friendly way 
    // until we know more details
    //	_session.execute("INSERT INTO " + _keyspace + ".packet (time_stamp, source_addr, text_values, dest_addr) VALUES (" + dateSecs + ",'" + ipAddress + "',{'messagetype' : '" + messageType + "', 'endpoint' : '" + appName + "'}, '" + _counter + "')");
    //_counter++;
    }

    public void close() {
	_session.close();
	_cluster.close();
	_session = null;
    }
}
