package org.autonlab.anomalydetection;

import com.savarese.spatial.*;
import java.io.*;
import java.util.*;

public class DataIOFile implements DataIO {
    private BufferedReader br = null;

    public DataIOFile(String filename) {
	try {
	    br = new BufferedReader(new FileReader(filename));
	} catch (IOException e) {
	    e.printStackTrace();
	    throw new RuntimeException("Failed to import data");
	}
    }

    /**
     * Read a csv file and return a HashMap
     *
     */
    public HashMap<GenericPoint<String>, HashMap<GenericPoint<String>, ArrayList<HistoTuple>>> getData(int minutesBack, int ignoreRecentMins, int useNow) {
	GenericPoint<String> valueType = new GenericPoint(1);
	valueType.setCoord(0, "text_values.messagetype");
	HashMap<GenericPoint<String>, HashMap<GenericPoint<String>, ArrayList<HistoTuple>>> trainMap = new HashMap();
	trainMap.put(valueType, new HashMap<GenericPoint<String>, ArrayList<HistoTuple>>());

	int count = 0;

	try {
	    int i;
 	    String sCurrentLine;

	    System.out.print("Importing data");
	    while ((sCurrentLine = br.readLine()) != null) {
		String[] sParts;

		if (count % 1000 == 0) {
		    System.out.print(".");
		}

		// expecting a line of the form <ip address>,<timestamp from epoch>,<msg type string>,<Application name>
		// The final two arguments may not exist but the first two must
		sParts = sCurrentLine.split(",");
		String ipAddress = sParts[0];
		Double timeStamp = Double.parseDouble(sParts[1]);
		String messageType = "";
		String applicationName = "";
		if (sParts.length >= 3) {
		    messageType = sParts[2];
		}
		if (sParts.length >= 4) {
		    applicationName = sParts[3];
		}

		GenericPoint<String> category = new GenericPoint<String>(2);
		category.setCoord(0, ipAddress);
		category.setCoord(1, applicationName);

		if (!trainMap.get(valueType).containsKey(category)) {
		    trainMap.get(valueType).put(category, new ArrayList<HistoTuple>());
		}
		trainMap.get(valueType).get(category).add(new HistoTuple(timeStamp, messageType, valueType));

		count++;
	    }
	    System.out.println("");
	} catch (IOException e) {
	    e.printStackTrace();
	    throw new RuntimeException("Failed to import data");
	} finally {
	    try {
		if (br != null)br.close();
	    } catch (IOException ex) {
		ex.printStackTrace();
		throw new RuntimeException("Failed to import data");
	    }
	}

	return trainMap;
    }

    public void putData(String categoryCSV, int dateSecs, String messageType) {
	throw new RuntimeException("putData for files not implemented");
    }

    public void close() {
	throw new RuntimeException("close for files is not implemented");
    }
}