package org.autonlab.anomalydetection;

import com.datastax.driver.core.*;
import com.savarese.spatial.*;

import java.util.*; 

import java.util.concurrent.locks.*;

import javax.ws.rs.*;
import javax.ws.rs.core.*;

import org.apache.commons.collections.map.*;
import org.javatuples.*;
import org.apache.commons.math3.distribution.UniformRealDistribution;
import org.apache.commons.math3.distribution.UniformIntegerDistribution;

import org.joda.time.*;

@Path("/")
public class DaemonService {
    static HistogramStore histogramData = new HistogramStore();

    static ReentrantReadWriteLock allHistogramsMapLock = new ReentrantReadWriteLock();

    /**
     * Get the histogram's number of dimensions and their names. This is so that calls to /evaluate can be constructed properly
     *
     * @return the number of dimensions in the histogram, -1 if there's no matching IP, 0 if there's no data for that IP then a list of <index> <name> pairs, one per line
     */
    @GET
    @Path("/getdimensions")
    @Produces(MediaType.TEXT_PLAIN)
    public Response getDimensions() {
	String output = new String("-1");
	output = "";

	allHistogramsMapLock.readLock().lock();

	output += "" + HistoTuple.getDimensionNames();

	allHistogramsMapLock.readLock().unlock();

	return Response.status(200).entity(output).build();
    }


    @GET
    @Path("/getDatasetKeys")
    @Produces(MediaType.TEXT_HTML)
    public Response getDatasetKeys() throws InterruptedException {
	String output = new String();

	allHistogramsMapLock.readLock().lock();

	for (Integer id : histogramData.getIDList()) {
	    output += "ID " + id + "<ul>";
	    for (GenericPoint<String> valueName : histogramData.getValueList(id)) {
		for (GenericPoint<String> categoryFields : histogramData.getCategoryList(id, valueName)) {
		    output += "<li>";
		    for (int ii = 0; ii < categoryFields.getDimensions(); ii++) {
			output += categoryFields.getCoord(ii);
			if (ii != categoryFields.getDimensions() - 1) {
			    output += "(" + valueName + ",";
			}
		    }
		    output += "</li>";
		}
	    }
	    output += "</ul>";
	}

	allHistogramsMapLock.readLock().unlock();

	return Response.status(200).entity(output).build();
    }

    /* minor bug here that if id does not exist, doesn't unlock */
    @GET
    @Path("/getHistograms")
    @Produces(MediaType.TEXT_PLAIN)
    public Response getHistograms(@QueryParam("id") Integer id,
				  @QueryParam("categoryCSV") String category,
				  @QueryParam("valueCSV") String value) throws InterruptedException {

	GenericPoint<String> categoryPoint = getPointFromCSV(category);
	GenericPoint<String> valuePoint = getPointFromCSV(value);

	allHistogramsMapLock.readLock().lock();

	StringBuilder output = new StringBuilder();
	int newID = histogramData.recalculateByCategory(id, categoryPoint, valuePoint, output);
	if (newID != id) {
	    output.append("Didn't find the data at id " + id + " but found it at id " + newID);
	    id = newID;
	}

	Double[][] stats = histogramData.getHistogramStats(id, valuePoint, categoryPoint);
	output.append("min: " + Arrays.asList(stats[0]) + "\n");
	output.append("max: " + Arrays.asList(stats[1]) + "\n");
	output.append("mean: " + Arrays.asList(stats[2]) + "\n");
	output.append("stddev: " + Arrays.asList(stats[3]) + "\n");

	ArrayList<Pair<Integer, GenericPoint<Integer>>> histograms = histogramData.getHistograms(id, valuePoint, categoryPoint);
	output.append("Number of histograms: " + histograms.size() + " \n");
	for (Pair<Integer, GenericPoint<Integer>> tempPair : histograms) {
	    output.append(tempPair.getValue0() + " : " + tempPair.getValue1().toString() + "\n");
	}

	allHistogramsMapLock.readLock().unlock();

	return Response.status(200).entity(output.toString()).build();
    }

    /**
     * create a dataset of a single histogram with the histogram values passed in by caller
     * for debugging and testing
     *
     * @param catagoryCSV for data i.e., source_addr;10.90.94.9 
     * @param valueCSV i.e., dest_addr
     * @param valuedataCSV i.e., [100,  200]
     */
    @GET
    @Path("/testhist")
    @Produces(MediaType.TEXT_PLAIN)
	public Response testWriteHist(@QueryParam("categoryCSV") String categoryCSV,
				      @QueryParam("valueCSV") String valueCSV,
				      @QueryParam("valueDataCSV") String valueDataCSV) {
	HashMap<GenericPoint<String>, HashMap<GenericPoint<String>, Pair<Double, ArrayList<Pair<Integer, GenericPoint<Integer>>>>>> newData = new HashMap();

	GenericPoint<String> categoryPoint = getPointFromCSV(categoryCSV);
	GenericPoint<String> valuePoint = getPointFromCSV(valueCSV);
	GenericPoint<Integer> valueDataPoint = getPointFromCSVInt(valueDataCSV);

	newData.put(valuePoint, new HashMap<GenericPoint<String>, Pair<Double, ArrayList<Pair<Integer, GenericPoint<Integer>>>>>());
	ArrayList<Pair<Integer, GenericPoint<Integer>>> data = new ArrayList<Pair<Integer, GenericPoint<Integer>>>();

	DateTime startTime = new DateTime();
	Integer startTimeSec = (int)((startTime.getMillis())/1000);
	Pair<Integer, GenericPoint<Integer>> temp = new Pair<Integer, GenericPoint<Integer>>(startTimeSec, valueDataPoint);

	data.add(temp);

	newData.get(valuePoint).put(categoryPoint, new Pair<Double, ArrayList<Pair<Integer, GenericPoint<Integer>>>>(-1.0,data));
	
	allHistogramsMapLock.writeLock().lock();
	Integer newID = histogramData.putHistogramSet(newData);
	allHistogramsMapLock.writeLock().unlock();
	return Response.status(200).entity("ID "+ newID).build();
    }

    /**
     *
     * @param ageMins The number of minutes into the past from the current time to include data. Everything else is excluded
     *                 NOTE: as of this writing we're hard coding the current time to be 2014-05-12T13:54:12.000-04:00 since
     *                       that is the most recent time of our test data and we're not using live data
     */
    @GET
    @Path("/getdb")
    @Produces(MediaType.TEXT_PLAIN)
    public Response getDbCall(@QueryParam("hostname") String hostname,
			  @QueryParam("categoryCSV") String categoryCSV,
			  @QueryParam("value") String valueCSV,
			  @QueryParam("ageMins") Integer ageMins,
			  @QueryParam("keySpace") String keySpace,
			  @QueryParam("table") String table,
			  @QueryParam("useNow") Integer useNow) throws InterruptedException {

	allHistogramsMapLock.writeLock().lock();

	StringBuilder output = getDb(hostname, categoryCSV, valueCSV, ageMins, keySpace, table, 0, useNow);

	allHistogramsMapLock.writeLock().unlock();
	return Response.status(200).entity(output.toString()).build();
    }



    public StringBuilder getDb(String hostname, String categoryCSV, String valueCSV, Integer ageMins, String keySpace, String table, Integer ignoreRecentMin, Integer useNow) {
	StringBuilder output = new StringBuilder("");

	DataIOCassandraDB dbHandle = new DataIOCassandraDB(hostname, keySpace, table);

	if (categoryCSV != null) {
	    dbHandle.setCategoryFields(categoryCSV);
	}
	if (valueCSV != null) {
	    dbHandle.setValueFields(valueCSV);
	}
	if (ageMins == null) {
	    ageMins = 0;
	}
	if (ignoreRecentMin == null) {
	    ignoreRecentMin = 0;
	}
	if (useNow == null) {
	    useNow = 0;
	}
	HashMap<GenericPoint<String>, HashMap<GenericPoint<String>, ArrayList<HistoTuple>>> data = dbHandle.getData(ageMins, ignoreRecentMin, useNow);

	if (data != null) {
	    
	    Integer new_id = histogramData.putHistogramSet(HistoTuple.mergeWindows(data, AnomalyDetectionConfiguration.SAMPLE_WINDOW_SECS, AnomalyDetectionConfiguration.SLIDE_WINDOW_SECS));
	    output.append("Dataset ID: " + new_id + "\n");
	    for (GenericPoint<String> valueName : histogramData.getValueList(new_id)) {
		for (GenericPoint<String> category : histogramData.getCategoryList(new_id, valueName)) {
		    output.append("Category: " + category.toString() + ", Value: " + valueName);
		    output.append(" (datapoints: " + histogramData.getHistogramsDataCount(new_id, valueName, category) + ")\n");
		}
	    }
	}
	else {
	    output.append("No data returned");
	}
	dbHandle.close();

	return output;
    }

    @GET
    @Path("/getfakedata")
    @Produces(MediaType.TEXT_PLAIN)
    public Response getFakeData() throws InterruptedException {
	GenericPoint<String> valueType = new GenericPoint(1);
	valueType.setCoord(0, "messagetype");

	allHistogramsMapLock.writeLock().lock();

	StringBuilder output = new StringBuilder("");

	HashMap<GenericPoint<String>, Pair<Double, ArrayList<Pair<Integer, GenericPoint<Integer>>>>> fakeData = new HashMap();

	// generate a sparse-ish lower half of a matrix. This will be our training data
	ArrayList<Pair<Integer, GenericPoint<Integer>>> lowerHalf = new ArrayList();
	int fakeTime = 1;
	for (int i = 10; i < 50; i += 10) {
	    for (int j = 10; j <= (50-i); j += 10) {
		GenericPoint<Integer> fakePoint = new GenericPoint(i, j);
		output.append(fakePoint.toString() + "\n");
		Pair<Integer, GenericPoint<Integer>> fakePair = new Pair(fakeTime, fakePoint);
		lowerHalf.add(fakePair);
		fakeTime++;
	    }
	}
	GenericPoint<String> category = new GenericPoint(2);
	category.setCoord(0, "1.1.1.1");
	category.setCoord(1, "myapp");
	fakeData.put(category, new Pair<Double, ArrayList<Pair<Integer, GenericPoint<Integer>>>>(0.0, lowerHalf));
	output.append("Category: 1.1.1.1, myapp (" + lowerHalf.size() + ")\n");

	// generate a dense full matrix. This will be test data used to run against the lower half matrix
	ArrayList<Pair<Integer, GenericPoint<Integer>>> fullMatrix = new ArrayList();
	for (int i = 10; i < 100; i += 10) {
	    for (int j = 10; j < 100; j += 10) {
		GenericPoint<Integer> fakePoint = new GenericPoint(i, j);
		Pair<Integer, GenericPoint<Integer>> fakePair = new Pair(fakeTime, fakePoint);
		fullMatrix.add(fakePair);
		fakeTime++;
	    }
	}
	GenericPoint<String> category2 = new GenericPoint(2);
	category2.setCoord(0, "5.5.5.5");
	category2.setCoord(1, "otherthing");
	fakeData.put(category2, new Pair<Double, ArrayList<Pair<Integer, GenericPoint<Integer>>>>(0.0, fullMatrix));
	output.append("Category: 5.5.5.5, otherthing (" + fullMatrix.size() + ")\n");

	// generate some fake HistoTuples. these are unused but the code would crash without them
	HistoTuple foo = new HistoTuple(1, "fake1", valueType);
	HistoTuple foo2 = new HistoTuple(2, "fake2", valueType);

	HashMap<GenericPoint<String>, HashMap<GenericPoint<String>, Pair<Double, ArrayList<Pair<Integer, GenericPoint<Integer>>>>>> fakeDataFinal = new HashMap();
	fakeDataFinal.put(valueType, fakeData);
	output.append("Dataset ID: " + histogramData.putHistogramSet(fakeDataFinal) + "\n");

	allHistogramsMapLock.writeLock().unlock();

	return Response.status(200).entity(output.toString()).build();
    }

    /**
     * Delete the mapping for one ID -> newMap
     *
     * @return "ok" on success, something else on error
     */
    @GET
    @Path("/deleteone/{id}")
    @Produces(MediaType.TEXT_PLAIN)
    public Response deleteOne(@PathParam("id") Integer id) throws InterruptedException {

	allHistogramsMapLock.writeLock().lock();

	String output = "ok";
	if (!histogramData.deleteHistogramSet(id)) {
	    output = "No data matching id " + id;
	}

	SVMCalc.removeModelFromCache(id);

	allHistogramsMapLock.writeLock().unlock();

	return Response.status(200).entity(output).build();
    }	    

    /**
     * Delete all mappingings for ID -> newMap
     *
     * @return "ok" and the number if elements removed
     */
    @GET
    @Path("/deleteall")
    @Produces(MediaType.TEXT_PLAIN)
    public Response deleteAllCall() throws InterruptedException {
	String output = "ok";

	allHistogramsMapLock.writeLock().lock();

	deleteAll();

	allHistogramsMapLock.writeLock().unlock();

	return Response.status(200).entity(output).build();
    }

    public void deleteAll() {
	histogramData = new HistogramStore();
    }
	
    @GET
    @Path("/test")
    @Produces(MediaType.TEXT_PLAIN)
    public Response getData(@QueryParam("trainID") Integer trainID,
			    @QueryParam("trainCategoryCSV") String trainCategory,
			    @QueryParam("trainValue") String trainValue,
			    @QueryParam("testID") Integer testID,
			    @QueryParam("testCategoryCSV") String testCategory,
			    @QueryParam("testValue") String testValue,
			    @QueryParam("anomalyTrainID") Integer anomalyTrainID,
			    @QueryParam("anomalyTrainCategoryCSV") String anomalyTrainCategory,
			    @QueryParam("anomalyTrainValue") String anomalyTrainValue,
			    @QueryParam("autoReload") Integer autoReloadSec) throws InterruptedException {

	int calcTypeToUse;

	allHistogramsMapLock.writeLock().lock();
	calcTypeToUse = AnomalyDetectionConfiguration.CALC_TYPE_TO_USE;

	if (calcTypeToUse == AnomalyDetectionConfiguration.CALC_TYPE_KDTREE) {
	    StringBuilder output = getDataKDTree(trainID, trainCategory, trainValue, testID, testCategory, testValue);
	    allHistogramsMapLock.writeLock().unlock();
	    return Response.status(200).entity(output.toString()).build();
	}
	else if (calcTypeToUse == AnomalyDetectionConfiguration.CALC_TYPE_SVM) {
	    StringBuilder output = getDataSVM(trainID, trainCategory, trainValue, testID, testCategory, testValue, anomalyTrainID, anomalyTrainCategory, anomalyTrainValue, autoReloadSec);
	    allHistogramsMapLock.writeLock().unlock();
	    return Response.status(200).entity(output.toString()).build();
	}
	else {
	    throw new RuntimeException("unknown calculation type");
	}
    }

    @GET
    @Path("/testKDTree")
    @Produces(MediaType.TEXT_PLAIN)
    public Response getDataKDTreeCall(@QueryParam("trainID") Integer trainID,
				  @QueryParam("trainCategoryCSV") String trainCategory,
				  @QueryParam("trainValue") String trainValue,
				  @QueryParam("testID") Integer testID,
				  @QueryParam("testCategoryCSV") String testCategory,
				  @QueryParam("testValue") String testValue) throws InterruptedException {
	allHistogramsMapLock.writeLock().lock();

	StringBuilder output = getDataKDTree(trainID, trainCategory, trainValue, testID, testCategory, testValue);

	allHistogramsMapLock.writeLock().unlock();

	return Response.status(200).entity(output.toString()).build();
    }

    public StringBuilder getDataKDTree(Integer trainID,
				       String trainCategory,
				       String trainValue,
				       Integer testID,
				       String testCategory,
				       String testValue) {

	StringBuilder output = new StringBuilder("Calculation method: KDTree\n");

	int error = 0;
	if (trainID == null) {
	    System.out.println("train ID not set");
	    error++;
	}

	if (testID == null) {
	    System.out.println("test ID not set");
	    error++;
	}

	if (trainCategory == null) {
	    System.out.println("train Category not set");
	    error++;
	}

	if (testCategory == null) {
	    System.out.println("test Category not set");
	    error++;
	}

	if (trainValue == null) {
	    System.out.println("train Value not set");
	    error++;
	}

	if (testValue == null) {
	    System.out.println("test Value not set");
	    error++;
	}

	if (error > 0) {
	    throw new RuntimeException("error in inputs");
	}

	GenericPoint<String> trainCategoryPoint = getPointFromCSV(trainCategory);
	GenericPoint<String> trainValuePoint =  getPointFromCSV(trainValue);
	GenericPoint<String> testCategoryPoint = getPointFromCSV(testCategory);
	GenericPoint<String> testValuePoint = getPointFromCSV(testValue);

	output.append(KDTreeCalc.runOneTestKDTree(histogramData, trainID, trainCategoryPoint, trainValuePoint, testID, testCategoryPoint, testValuePoint, null));

	return output;
    }

    /**
     * Simply convert a CSV of strings into a GenericPoint where each dimension was one of the CSV strings
     *
     * Relative to the rest of the code, this is not an expensive operation but when possible we call
     * this outside of the allHistogramsMapSemaphore
     *
     * @param csv
     * @return GenericPoint
     */
    public GenericPoint<String> getPointFromCSV(String csv) {
	String[] sParts = csv.split(",");
	Arrays.sort(sParts);
	GenericPoint<String> point = new GenericPoint(sParts.length);

	for (int ii = 0; ii < sParts.length; ii++) {
	    point.setCoord(ii, sParts[ii]);
	}

	return point;
    }
    public GenericPoint<Integer> getPointFromCSVInt(String csv) {
	String[] sParts = csv.split(",");
	// note: no sort here like with the String version of this because
	// we're directly storing the input not translating them to another format
	GenericPoint<Integer> point = new GenericPoint(sParts.length);

	for (int ii = 0; ii < sParts.length; ii++) {
	    System.out.println("coord " + ii + " val " + Integer.parseInt(sParts[ii]));
	    point.setCoord(ii, Integer.parseInt(sParts[ii]));
	}

	return point;
    }

    @GET
    @Path("/setAnomalyServer")
    @Produces(MediaType.TEXT_HTML)
    public Response setAnomalyServer(@QueryParam("hostname") String hostname) throws InterruptedException {
	if (hostname != null) {
	    AnomalyDetectionConfiguration.ANOMALY_REST_URL_PREFIX = "http://" + hostname + "/essence-services";
	}
	return Response.status(200).entity("ok").build();
    }

    @GET
    @Path("/purgeSupervisedCache")
    @Produces(MediaType.TEXT_HTML)
    public Response demo() {
	allHistogramsMapLock.writeLock().lock();
	AnomalyPrediction.purgeCache();
	allHistogramsMapLock.writeLock().unlock();
	return Response.status(200).entity("ok").build();
    }


    @GET
    @Path("/demo")
    @Produces(MediaType.TEXT_HTML)
    public Response demo(@QueryParam("hostname") String hostname,
			  @QueryParam("categoryCSV") String categoryCSV,
			  @QueryParam("valueCSV") String valueCSV,
			  @QueryParam("ageMins") Integer ageMins,
           		  @QueryParam("refreshSec") Integer refreshSec,
 			  @QueryParam("keySpace") String keySpace,
			  @QueryParam("recentMin") Integer recentMin,
			  @QueryParam("demoFilter") String demoFilter,
 			  @QueryParam("table") String table,
			  @QueryParam("useNow") Integer useNow) throws InterruptedException {
	//assume we use demo mode at a live site with live data
	if (useNow == null) {
	    useNow = 1;
	}

	allHistogramsMapLock.writeLock().lock();

	if (hostname != null) {
	    AnomalyDetectionConfiguration.ANOMALY_REST_URL_PREFIX = "http://" + hostname + "/essence-services";
	}

	deleteAll(); //invalidate the existing data

	/* 
	 * There is a bug that I haven't tracked down.
	 * If we run this demo first on an empty database, then stream to it, somehow
	 * this breaks the SVM library. I surmised that it was related to this HistoTuple
	 * getting out of sync when the database was empty and then now growing correctly
	 * when there was data. So, this fixes the problem but I don't understand the
	 * reason it was broken in the first place.
	 */
	HistoTuple.resetMap();

	// number of windows we want to split at
	if (recentMin == null) {
	    recentMin = 10;
	}


	//this will go into ID 0 and be the training data
	getDb(hostname, categoryCSV, valueCSV, ageMins, keySpace, table, recentMin, useNow);

	//this will go into ID 1 and be the test data
	getDb(hostname, categoryCSV, valueCSV, recentMin, keySpace, table, 0, useNow);

	GenericPoint<String> oneCategoryPointSource = null;
	GenericPoint<String> oneCategoryPointDest = null;
	if (histogramData.isIDValid(0) && histogramData.isIDValid(1)) {
	    for (GenericPoint<String> oneValuePoint: histogramData.getValueList(0)) {
		for (GenericPoint<String> oneCategoryPoint : histogramData.getCategoryList(0, oneValuePoint)) {
		    System.out.println(oneCategoryPoint.toString() + "ABC");
		    if (oneCategoryPointSource == null) {
			oneCategoryPointSource = oneCategoryPoint;
			continue;
		    }
		    if (oneCategoryPointDest == null) {
			oneCategoryPointDest = oneCategoryPoint;
		    }

		    // To always trigger anomalies, use wildly unrelated data for training and test data. In this example, the training set is the source IP and the 
		    // test set is the destination IP
		    //StringBuilder output = getDataSVM(0, oneCategoryPointSource.getCoord(0), valueCSV, 1, oneCategoryPointDest.getCoord(0), valueCSV, null, null, null, refreshSec);

		    String newFilter = demoFilter;
		    if (newFilter == null) {
			newFilter = oneCategoryPointSource.getCoord(0);
		    }
		    StringBuilder output = getDataSVM(0, newFilter, valueCSV, 1, newFilter, valueCSV, null, null, null, refreshSec);

		    allHistogramsMapLock.writeLock().unlock();
		    return Response.status(200).entity(output.toString()).build();
		}
	    }
	}

	allHistogramsMapLock.writeLock().unlock();

	// There is no data yet so reload the page every 2 seconds
	StringBuilder output = new StringBuilder("<html>");
	output.append("<head><meta http-equiv='refresh' content='" + refreshSec + "'></head>");
	output.append("<body><pre>No data yet\n");
	return Response.status(200).entity(output.toString()).build();
    }

    @GET
    @Path("/testSVM")
    @Produces(MediaType.TEXT_HTML)
    public Response getDataSVMCall(@QueryParam("trainID") Integer trainID,
			       @QueryParam("trainCategoryCSV") String trainCategory,
			       @QueryParam("trainValue") String trainValue,
			       @QueryParam("testID") Integer testID,
			       @QueryParam("testCategoryCSV") String testCategory,
			       @QueryParam("testValue") String testValue,
			       @QueryParam("anomalyTrainID") Integer anomalyTrainID,
			       @QueryParam("anomalyTrainCategoryCSV") String anomalyTrainCategory,
			       @QueryParam("anomalyTrainValue") String anomalyTrainValue,
			       @QueryParam("autoReloadSec") Integer autoReloadSec) throws InterruptedException {

	allHistogramsMapLock.writeLock().lock();

	StringBuilder output = getDataSVM(trainID, trainCategory, trainValue, testID, testCategory, testValue, anomalyTrainID, anomalyTrainCategory, anomalyTrainValue, autoReloadSec);

	allHistogramsMapLock.writeLock().unlock();

	return Response.status(200).entity(output.toString()).build();
    }

    public StringBuilder getDataSVM(Integer trainID,
				    String trainCategory,
				    String trainValue,
				    Integer testID,
				    String testCategory,
				    String testValue,
				    Integer anomalyTrainID,
				    String anomalyTrainCategory,
				    String anomalyTrainValue,
				    Integer autoReloadSec) {

	StringBuilder output = new StringBuilder("<html>");
	if (autoReloadSec != null && autoReloadSec > 0) {
	    output.append("<head><meta http-equiv='refresh' content='" + autoReloadSec + "'></head>");
	}
	output.append("<body><pre>Calculation method: SVM\n");

	GenericPoint<String> trainCategoryPoint = getPointFromCSV(trainCategory);
	GenericPoint<String> trainValuePoint = getPointFromCSV(trainValue);
	GenericPoint<String> testCategoryPoint = getPointFromCSV(testCategory);
	GenericPoint<String> testValuePoint = getPointFromCSV(testValue);

	GenericPoint<String> anomalyTrainCategoryPoint = null;
	GenericPoint<String> anomalyTrainValuePoint = null;
	if (anomalyTrainCategory != null) {
	    anomalyTrainCategoryPoint = getPointFromCSV(anomalyTrainCategory);
	    anomalyTrainValuePoint = getPointFromCSV(anomalyTrainValue);
	}

	/* if the data we want isn't stored, perhaps we can calculate it from other existing data */
	int newTrainID = histogramData.recalculateByCategory(trainID, trainCategoryPoint, trainValuePoint, output);
	if (newTrainID == -1) {
	    output.append("ERROR: trainCategoryCSV (" + trainCategory + ") was not found and could not be calculated from existing data\n");
	    return output;
	}
	else if (newTrainID != trainID) {
	    output.append("NOTE: trainCategoryCSV (" + trainCategory + ") was not found at id " + trainID + " but found it at ID " + newTrainID + "\n");
	    trainID = newTrainID;
	}
	int newTestID = histogramData.recalculateByCategory(testID, testCategoryPoint, testValuePoint, output);
	if (newTestID == -1) {
	    output.append("ERROR: testCategoryCSV  (" + testCategory + ") was not found and could not be calculated from existing data\n");
	    return output;
	}
	else if (newTestID != testID) {
	    output.append("NOTE: testCategoryCSV  (" + testCategory + ") was not found at id " + testID + " but found it at ID " + newTestID + "\n");
	    testID = newTestID;
	}
	if (anomalyTrainID != null) {
	    int newAnomalyTrainID = histogramData.recalculateByCategory(anomalyTrainID, anomalyTrainCategoryPoint, anomalyTrainValuePoint, output);
	    if (newAnomalyTrainID == -1) {
		output.append("ERROR: anomalyTrainCategoryCSV (" + anomalyTrainCategory + ") was not found and could not be calculated from existing data\n");
		return output;
	    }
	    else if (newAnomalyTrainID != anomalyTrainID) {
		output.append("NOTE: anomalyTrainCategoryCSV (" + anomalyTrainCategory + ") was not found at id " + anomalyTrainID + " but found it at ID " + newAnomalyTrainID + "\n");
		anomalyTrainID = newAnomalyTrainID;
	    }
	}

	MultiValueMap resultsHash = new MultiValueMap();
	//	try {
	    StringBuilder ret = null;
	    ret = SVMCalc.runOneTestSVM(histogramData, trainID, trainCategoryPoint, trainValuePoint, testID, testCategoryPoint, testValuePoint, anomalyTrainID, anomalyTrainCategoryPoint, anomalyTrainValuePoint, resultsHash);
	    output.append(ret.toString());
	    /*
	}
	catch (Exception ex) {
	    System.out.println("Caught excpetion. Data changing");
	}
	    */

	List<Double> resultsHashList = new ArrayList<Double>(resultsHash.keySet());
	Collections.sort(resultsHashList); // ascending order
	Collections.reverse(resultsHashList); //descending order
	int ii = 0;
	
	Double score = 0.0;
	if (resultsHashList.size() > 0) {
	    score = resultsHashList.get(0);
	}

	Pair<Integer, Integer> trainTime = histogramData.getStartAndEndTime(trainID);
	Pair<Integer, Integer> anomalyTrainTime = null;
	if (anomalyTrainID != null) {
	    anomalyTrainTime = histogramData.getStartAndEndTime(anomalyTrainID);
	}
	Pair<Integer, Integer> testTime = histogramData.getStartAndEndTime(testID);

	/*
	for (Pair<Integer, GenericPoint<Integer>> onePoint : ((Collection<Pair<Integer, GenericPoint<Integer>>>)resultsHash.getCollection(score))) {
	    Integer timestamp = onePoint.getValue0();
	    output.append("\n====== Highest Anomaly Info =====\n"); //right now we just say the highest scoring point is anomaly just to make sure we can print the info
	    output.append("Anomaly " + score + " at time " + timestamp + "( " + ((Collection<Integer>)resultsHash.getCollection(score)).size() + " with this score)\n");
	    output.append(" * anomaly datapoint: " + onePoint.getValue1() + "\n");
	    System.out.println(trainTime.getValue0());
	    output.append(" * Training data: " + trainID + "," + trainCategoryPoint.toString() + "," + trainValuePoint.toString() + " time range: " + trainTime.getValue0() + " to " + trainTime.getValue1() + "\n"); 
	    if (anomalyTrainID != null) {
		output.append(" * Anomaly training data: " + anomalyTrainID + "," + anomalyTrainCategoryPoint.toString() + "," + anomalyTrainValuePoint.toString() + " time range: " + anomalyTrainTime.getValue0() + " to " + anomalyTrainTime.getValue1() + "\n");
	    }
	    output.append(" * Testing data: " + testID + "," + testCategoryPoint.toString() + "," + testValuePoint.toString() + " time range: " + testTime.getValue0() + " to " + testTime.getValue1() + "\n");
	    output.append("<a href=http://10.21.1.24:8080/AnomalyDetection/rest/getHistograms?id=" + trainID + "&categoryCSV=" + trainCategory + "&valueCSV=" + trainValue + ">link to training dataset</a>\n");
	    if (anomalyTrainID != null) {
		output.append("<a href=http://10.21.1.24:8080/AnomalyDetection/rest/getHistograms?id=" + anomalyTrainID + "&categoryCSV=" + anomalyTrainCategory + "&valueCSV=" + anomalyTrainValue + ">link to anomaly training dataset</a>\n");
	    }
	    output.append("<a href=http://10.21.1.24:8080/AnomalyDetection/rest/getHistograms?id=" + testID + "&categoryCSV=" + testCategory + "&valueCSV=" + testValue + ">link to testing dataset</a>\n");
	    break;
	}
	*/
	return output;
    }


    @GET
    @Path("/testSVMRandom")
    @Produces(MediaType.TEXT_HTML)
    public Response getDataSVMRandom(@QueryParam("trainID") Integer trainID,
				     @QueryParam("trainCategoryCSV") String trainCategory,
				     @QueryParam("trainValue") String trainValue,
				     @QueryParam("testID") Integer testID,
				     @QueryParam("testCategoryCSV") String testCategory,
				     @QueryParam("testValue") String testValue,
				     @QueryParam("anomalyTrainID") Integer anomalyTrainID,
				     @QueryParam("anomalyTrainCategoryCSV") String anomalyTrainCategory,
				     @QueryParam("anomalyTrainValue") String anomalyTrainValue,
				     @QueryParam("autoReloadSec") Integer autoReloadSec) throws InterruptedException {

	StringBuilder output = new StringBuilder("<html>");
	if (autoReloadSec != null && autoReloadSec > 0) {
	    output.append("<head><meta http-equiv='refresh' content='" + autoReloadSec + "'></head>");
	}
	output.append("<body><pre>Calculation method: SVM\n");

	GenericPoint<String> trainCategoryPoint = getPointFromCSV(trainCategory);
	GenericPoint<String> trainValuePoint = getPointFromCSV(trainValue);
	GenericPoint<String> testCategoryPoint = getPointFromCSV(testCategory);
	GenericPoint<String> testValuePoint = getPointFromCSV(testValue);

	GenericPoint<String> anomalyTrainCategoryPoint = null;
	GenericPoint<String> anomalyTrainValuePoint = null;
	if (anomalyTrainCategory != null) {
	    anomalyTrainCategoryPoint = getPointFromCSV(anomalyTrainCategory);
	    anomalyTrainValuePoint = getPointFromCSV(anomalyTrainValue);
	}

	allHistogramsMapLock.writeLock().lock();

	int newTrainID = histogramData.recalculateByCategory(trainID, trainCategoryPoint, trainValuePoint, output);
	if (newTrainID == -1) {
	    output.append("ERROR: trainCategoryCSV (" + trainCategory + ") was not found and could not be calculated from existing data\n");
	    return Response.status(200).entity(output.toString()).build();
	}
	else if (newTrainID != trainID) {
	    output.append("NOTE: trainCategoryCSV (" + trainCategory + ") was not found at id " + trainID + " but found it at ID " + newTrainID + "\n");
	    trainID = newTrainID;
	}
	int newTestID = histogramData.recalculateByCategory(testID, testCategoryPoint, testValuePoint, output);
	if (newTestID == -1) {
	    output.append("ERROR: testCategoryCSV  (" + testCategory + ") was not found and could not be calculated from existing data\n");
	    return Response.status(200).entity(output.toString()).build();
	}
	else if (newTestID != testID) {
	    output.append("NOTE: testCategoryCSV  (" + testCategory + ") was not found at id " + testID + " but found it at ID " + newTestID + "\n");
	    testID = newTestID;
	}
	if (anomalyTrainID != null) {
	    int newAnomalyTrainID = histogramData.recalculateByCategory(anomalyTrainID, anomalyTrainCategoryPoint, anomalyTrainValuePoint, output);
	    if (newAnomalyTrainID == -1) {
		output.append("ERROR: anomalyTrainCategoryCSV (" + anomalyTrainCategory + ") was not found and could not be calculated from existing data\n");
		return Response.status(200).entity(output.toString()).build();
	    }
	    else if (newAnomalyTrainID != anomalyTrainID) {
		output.append("NOTE: anomalyTrainCategoryCSV (" + anomalyTrainCategory + ") was not found at id " + anomalyTrainID + " but found it at ID " + newAnomalyTrainID + "\n");
		anomalyTrainID = newAnomalyTrainID;
	    }
	}
	System.out.println("ZZZ " + trainID + " : " + testID + " : " + anomalyTrainID + "\n");
	MultiValueMap resultsHash = new MultiValueMap();
	output.append(SVMRandomCalc.runOneTestSVM(histogramData, trainID, trainCategoryPoint, trainValuePoint, testID, testCategoryPoint, testValuePoint, anomalyTrainID, anomalyTrainCategoryPoint, anomalyTrainValuePoint, resultsHash, AnomalyDetectionConfiguration.SVM_D));

	List<Double> resultsHashList = new ArrayList<Double>(resultsHash.keySet());
	Collections.sort(resultsHashList); // ascending order
	Collections.reverse(resultsHashList); //descending order
	int ii = 0;
	Double score = resultsHashList.get(0);

	Pair<Integer, Integer> trainTime = histogramData.getStartAndEndTime(trainID);
	Pair<Integer, Integer> anomalyTrainTime = null;
	if (anomalyTrainID != null) {
	    anomalyTrainTime = histogramData.getStartAndEndTime(anomalyTrainID);
	}
	Pair<Integer, Integer> testTime = histogramData.getStartAndEndTime(testID);


	for (Pair<Integer, GenericPoint<Integer>> onePoint : ((Collection<Pair<Integer, GenericPoint<Integer>>>)resultsHash.getCollection(score))) {
	    Integer timestamp = onePoint.getValue0();
	    output.append("\n====== Anomaly Detected Info =====\n"); //right now we just say the highest scoring point is anomaly just to make sure we can print the info
	    output.append("Anomaly " + score + " at time " + timestamp + "( " + ((Collection<Integer>)resultsHash.getCollection(score)).size() + " with this score)\n");
	    output.append(" * anomaly datapoint: " + onePoint.getValue1() + "\n");
	    output.append(" * Training data: " + trainID + "," + trainCategoryPoint.toString() + "," + trainValuePoint.toString() + " time range: " + trainTime.getValue0() + " to " + trainTime.getValue1() + "\n"); 
	    if (anomalyTrainID != null) {
		output.append(" * Anomaly training data: " + anomalyTrainID + "," + anomalyTrainCategoryPoint.toString() + "," + anomalyTrainValuePoint.toString() + " time range: " + anomalyTrainTime.getValue0() + " to " + anomalyTrainTime.getValue1() + "\n"); 
	    }
	    output.append(" * Testing data: " + testID + "," + testCategoryPoint.toString() + "," + testValuePoint.toString() + " time range: " + testTime.getValue0() + " to " + testTime.getValue1() + "\n");
	    output.append("<a href=http://10.21.1.24:8080/AnomalyDetection/rest/getHistograms?id=" + trainID + "&categoryCSV=" + trainCategory + "&valueCSV=" + trainValue + ">link to training dataset</a>\n");
	    if (anomalyTrainID != null) {
		output.append("<a href=http://10.21.1.24:8080/AnomalyDetection/rest/getHistograms?id=" + anomalyTrainID + "&categoryCSV=" + anomalyTrainCategory + "&valueCSV=" + anomalyTrainValue + ">link to anomaly training dataset</a>\n");
	    }
	    output.append("<a href=http://10.21.1.24:8080/AnomalyDetection/rest/getHistograms?id=" + testID + "&categoryCSV=" + testCategory + "&valueCSV=" + testValue + ">link to testing dataset</a>\n");
	    break;
	}

	allHistogramsMapLock.writeLock().unlock();

	return Response.status(200).entity(output.toString()).build();
    }

    /**
     * Set a new value for the size of the window to use when calculating histograms
     * WARNING: if the value is different from the current value, this function will
     *  delete all existing data from the system
     *
     * @param new value in seconds
     */
    @GET
    @Path("/setSampleWindowSecs/{newVal}")
    @Produces(MediaType.TEXT_PLAIN)
    public Response setSampleWindowSecs(@PathParam("newVal") int newValue) throws InterruptedException {

	allHistogramsMapLock.writeLock().lock();

	if (newValue != AnomalyDetectionConfiguration.SAMPLE_WINDOW_SECS) {
	    deleteAll(); //invalidate the existing data
	}
	AnomalyDetectionConfiguration.SAMPLE_WINDOW_SECS = newValue;

	allHistogramsMapLock.writeLock().unlock();

	return Response.status(200).entity("Changes enacted. All data deleted.").build();
    }

    @GET
    @Path("/getSampleWindowSecs")
    @Produces(MediaType.TEXT_PLAIN)
    public Response getSampleWindowSecs() throws InterruptedException {

	allHistogramsMapLock.writeLock().lock();

	String output = "" + AnomalyDetectionConfiguration.SAMPLE_WINDOW_SECS;

	allHistogramsMapLock.writeLock().unlock();

	return Response.status(200).entity(output).build();
    }

    /**
     * Set a new value for how far to slide the window when calculating histograms
     * WARNING: if the value is different from the current value, this function will
     *  delete all existing data from the system
     *
     * @param new value in seconds
     */
    @GET
    @Path("/setSlideWindowSecs/{newVal}")
    @Produces(MediaType.TEXT_PLAIN)
    public Response setSlideWindowSecs(@PathParam("newVal") int newValue) throws InterruptedException {

	allHistogramsMapLock.writeLock().lock();

	if (newValue != AnomalyDetectionConfiguration.SAMPLE_WINDOW_SECS) {
	    deleteAll(); //invalidate the existing data
	}
	AnomalyDetectionConfiguration.SLIDE_WINDOW_SECS = newValue;

	allHistogramsMapLock.writeLock().unlock();

	return Response.status(200).entity("Change enacted. All data deleted.").build();
    }

    @GET
    @Path("/getSlideWindowSecs")
    @Produces(MediaType.TEXT_PLAIN)
    public Response getSlideWindowSecs() throws InterruptedException {

	allHistogramsMapLock.writeLock().lock();

	String output = "" + AnomalyDetectionConfiguration.SLIDE_WINDOW_SECS;

	allHistogramsMapLock.writeLock().unlock();

	return Response.status(200).entity(output).build();
    }

    @GET
    @Path("/setCalcType/{newVal}")
    @Produces(MediaType.TEXT_HTML)
    public Response setCalcType(@PathParam("newVal") String newValue) throws InterruptedException {

	allHistogramsMapLock.writeLock().lock();

	String output = "Ok. Calc type set to " + newValue;
	int newIndex = Arrays.asList(AnomalyDetectionConfiguration.CALC_TYPE_NAMES).indexOf(newValue);
	if (newIndex >= 0) {
	    AnomalyDetectionConfiguration.CALC_TYPE_TO_USE = newIndex;
	}
	else {
	    output = "Invalid type<br>\n";
	}
	output += AnomalyDetectionConfiguration.printCalcTypeNameLinksHTML("");

	allHistogramsMapLock.writeLock().unlock();

	return Response.status(200).entity(output).build();
    }

    @GET
    @Path("/getCalcType")
    @Produces(MediaType.TEXT_HTML)
    public Response getCalcType() throws InterruptedException {

	allHistogramsMapLock.writeLock().lock();

	String output = "Calc type is " + AnomalyDetectionConfiguration.CALC_TYPE_NAMES[AnomalyDetectionConfiguration.CALC_TYPE_TO_USE];
	output += "<br>" + AnomalyDetectionConfiguration.printCalcTypeNameLinksHTML("setCalcType/");

	allHistogramsMapLock.writeLock().unlock();

	return Response.status(200).entity(output).build();
    }

    
    @GET
    @Path("/setNumThreads/{newVal}")
    @Produces(MediaType.TEXT_HTML)
    public Response setNumThreads(@PathParam("newVal") Integer newValue) throws InterruptedException {
	String output = "Number of threads was " + AnomalyDetectionConfiguration.NUM_THREADS + " and is now " + newValue;

	allHistogramsMapLock.writeLock().lock();
	if (AnomalyDetectionConfiguration.NUM_THREADS == newValue) {
	    output = "Number of threads is already " + newValue + ". No change";
	}
	else {
	    AnomalyDetectionConfiguration.NUM_THREADS = newValue;
	}
	allHistogramsMapLock.writeLock().unlock();

	return Response.status(200).entity(output).build();
    }

    @GET
    @Path("/setEnableSupervisedLearning/{newVal}")
    @Produces(MediaType.TEXT_HTML)
    public Response setEnableSupervisedLearning(@PathParam("newVal") Integer newValue) throws InterruptedException {
	String output = "Enable Supervised Learning was " + AnomalyDetectionConfiguration.SVM_ENABLE_SUPERVISED_LEARNING + " and is now " + newValue;

	allHistogramsMapLock.writeLock().lock();
	if (AnomalyDetectionConfiguration.SVM_ENABLE_SUPERVISED_LEARNING == newValue) {
	    output = "Value is already " + newValue + ". No change";
	}
	else {
	    AnomalyDetectionConfiguration.SVM_ENABLE_SUPERVISED_LEARNING = newValue;
	}
	allHistogramsMapLock.writeLock().unlock();

	return Response.status(200).entity(output).build();
    }

    @GET
    @Path("/setUnsupervisedThreshold/{newVal}")
    @Produces(MediaType.TEXT_HTML)
    public Response setUnsupervisedThreshold(@PathParam("newVal") Double newValue) throws InterruptedException {
	String output = "Unsupervised threshold was " + AnomalyDetectionConfiguration.SVM_UNSUPERVISED_THRESHOLD + " and is now " + newValue;

	allHistogramsMapLock.writeLock().lock();
	if (AnomalyDetectionConfiguration.SVM_UNSUPERVISED_THRESHOLD == newValue) {
	    output = "Value is already " + newValue + ". No change";
	}
	else {
	    AnomalyDetectionConfiguration.SVM_UNSUPERVISED_THRESHOLD = newValue;
	}
	allHistogramsMapLock.writeLock().unlock();

	return Response.status(200).entity(output).build();
    }

// CUSTOM TESTS
	//_______________________________________________________________________//
	
    @GET
    @Path("/customTest")
    @Produces(MediaType.TEXT_PLAIN)
    public Response customTest(@QueryParam("n") Integer n, @QueryParam("size") Integer s, @QueryParam("rn") Integer rn) throws InterruptedException {//@QueryParam("id") Integer id,
	//@QueryParam("csvKey") String csvKey) {

	StringBuilder output = new StringBuilder("Custom Test\n\n");
		
//	output.append(getFakeData2(n,s,rn).getEntity());
	getFakeData2(n,s,rn);
	//		String filename="/usr0/home/sibiv/Research/Data/GRE.out";
	//		DataIOFile foo = new DataIOFile(filename);
	//		allHistogramsMap.put(nextHistogramMapID, HistoTuple.mergeWindows(foo.getData(), AnomalyDetectionConfiguration.SAMPLE_WINDOW_SECS, AnomalyDetectionConfiguration.SLIDE_WINDOW_SECS));
	//		System.out.println("Opened file.");

	int id = histogramData.getNextID()-1;
	String csvKeyA = "a";
	String csvValueA = "b";
	String csvKey1 = "a1";
	String csvValue1 = "b1";
	String csvKey2 = "a2";
	String csvValue2 = "b2";
		
	GenericPoint<String> trainKeyA = getPointFromCSV(csvKeyA);
	GenericPoint<String> trainValueA = getPointFromCSV(csvValueA);
	GenericPoint<String> trainKey = getPointFromCSV(csvKey1);
	GenericPoint<String> trainValue = getPointFromCSV(csvValue1);
	GenericPoint<String> testKey = getPointFromCSV(csvKey2);
	GenericPoint<String> testValue = getPointFromCSV(csvValue2);

	output.append("\n\nSVM RANDOM:\n");
	long startTime1 = System.nanoTime();
	output.append(SVMRandomCalc.runOneTestSVM(histogramData, id, trainKey, trainValue, id, testKey, testValue, id-1, trainKeyA, trainValueA, null, rn).toString());
	long endTime1 = System.nanoTime();
	double duration = (double)(endTime1 - startTime1)/1000000000;
	output.append("\n\nTime taken:\n" + (duration));
	output.append("\n\nSVM:\n");
	long startTime2 = System.nanoTime();
	output.append(SVMCalc.runOneTestSVM(histogramData, id, trainKey, trainValue, id, testKey, testValue, id-1, trainKeyA, trainValueA, null).toString());
	long endTime2 = System.nanoTime();
	duration = (double)(endTime2 - startTime2)/1000000000;
	output.append("\n\nTime taken:\n" + (duration));
		
	return Response.status(200).entity(output.toString()).build();
    }

	
    @GET
    @Path("/getfakedata2")
    @Produces(MediaType.TEXT_PLAIN)
    public Response getFakeData2(@QueryParam("n") Integer n, @QueryParam("size") Integer s, @QueryParam("rn") Integer rn) {
		
	//allHistogramsMap.clear();
		
	StringBuilder output = new StringBuilder("");

	
	UniformRealDistribution urd = new UniformRealDistribution (0.0, 1.0);
	UniformIntegerDistribution uid = new UniformIntegerDistribution(0,5);
		
	output.append("Anomaly data:\n\n");
	int hs = (int) s/2; // half size
	int qs = (int) s/2; // quarter size
		
	HashMap<GenericPoint<String> , HashMap<GenericPoint<String>, Pair<Double, ArrayList<Pair<Integer, GenericPoint<Integer>>>>>> anomalyData = new HashMap();
	ArrayList<Pair<Integer, GenericPoint<Integer>>> anomalyTraining = new ArrayList<Pair<Integer, GenericPoint<Integer>>>();
	int fakeTime = 1;
	for (int i = 0; i < n; i += 1) {
	    GenericPoint<Integer> fakePoint = new GenericPoint<Integer>(s);
	    for (int j = 0; j < s; j += 1) { // Randomly fill first quarter with 0s and 1s (anomalies)
		if (j < qs)
		    fakePoint.setCoord(j, uid.sample());
		else
		    fakePoint.setCoord(j, 0);

	    }
	    output.append(fakePoint.toString() + "\n");
	    Pair<Integer, GenericPoint<Integer>> fakePair = new Pair<Integer, GenericPoint<Integer>>(fakeTime, fakePoint);
	    anomalyTraining.add(fakePair);
	    fakeTime++;
	}
	GenericPoint<String> aKey = new GenericPoint<String>(1);
	aKey.setCoord(0, "a");
	GenericPoint<String> aValue = new GenericPoint<String>(1);
	aValue.setCoord(0, "b");
	anomalyData.put(aValue, new HashMap<GenericPoint<String>, Pair<Double, ArrayList<Pair<Integer, GenericPoint<Integer>>>>>());
	anomalyData.get(aValue).put(aKey, new Pair(0.0, anomalyTraining));
	output.append("Key: a, Value: b (" + anomalyTraining.size() + ")\n\n");
		
	Integer new_id = histogramData.putHistogramSet(anomalyData);
	output.append("Dataset ID: " + new_id + "\n");
	
	boolean useOnes = false;
	output.append("Train data:\n\n");
	HashMap<GenericPoint<String> ,HashMap<GenericPoint<String>, Pair<Double, ArrayList<Pair<Integer, GenericPoint<Integer>>>>>> fakeData = new HashMap();
	ArrayList<Pair<Integer, GenericPoint<Integer>>> training = new ArrayList<Pair<Integer, GenericPoint<Integer>>>();
		
	fakeTime = 1;
	for (int i = 0; i < n; i += 1) {
	    GenericPoint<Integer> fakePoint = new GenericPoint<Integer>(s);
	    for (int j = 0; j < s; j += 1) { // Randomly fill second half with 1s and 0s
		if (j < hs)
		    fakePoint.setCoord(j, 0);
		else
			fakePoint.setCoord(j, uid.sample());

	    }
	    output.append(fakePoint.toString() + "\n");
	    Pair<Integer, GenericPoint<Integer>> fakePair = new Pair<Integer, GenericPoint<Integer>>(fakeTime, fakePoint);
	    training.add(fakePair);
	    fakeTime++;
	}
	GenericPoint<String> key = new GenericPoint<String>(1);
	key.setCoord(0, "a1");
	GenericPoint<String> value = new GenericPoint<String>(1);
	value.setCoord(0, "b1");
	fakeData.put(value, new HashMap<GenericPoint<String>, Pair<Double, ArrayList<Pair<Integer, GenericPoint<Integer>>>>>());
	fakeData.get(value).put(key, new Pair(0.0, training));
	output.append("Key: a1, Value: b1 (" + training.size() + ")\n\n");

	output.append("Test data:\n\n");
	// generate a dense full matrix. This will be test data used to run against the lower half matrix
	int normal_n = (int) 3*n/4;
	fakeTime = 1;
	ArrayList<Pair<Integer, GenericPoint<Integer>>> testing = new ArrayList<Pair<Integer, GenericPoint<Integer>>>();
	for (int i = 0; i < n; i += 1) {
	    GenericPoint<Integer> fakePoint = new GenericPoint<Integer>(s);
	    if (i < normal_n) {
		for (int j = 0; j < s; j += 1) { // Randomly fill second half with 1s and 0s
			if (j < hs)
				fakePoint.setCoord(j, 0);
			else
				fakePoint.setCoord(j, uid.sample());
			}
	    } else {
		for (int j = 0; j < s; j += 1) { // Randomly fill first quarter with 0s and 1s (anomalies)
			if (j < qs)
				fakePoint.setCoord(j, uid.sample());
			else
				fakePoint.setCoord(j, 0);

		}
	    }
	    output.append(fakePoint.toString() + "\n");
	    Pair<Integer, GenericPoint<Integer>> fakePair = new Pair<Integer, GenericPoint<Integer>>(fakeTime, fakePoint);
	    testing.add(fakePair);
	    fakeTime++;
	}
	GenericPoint<String> key2 = new GenericPoint<String>(1);
	key2.setCoord(0, "a2");
	GenericPoint<String> value2 = new GenericPoint<String>(1);
	value2.setCoord(0, "b2");
	fakeData.put(value2, new HashMap<GenericPoint<String>, Pair<Double, ArrayList<Pair<Integer, GenericPoint<Integer>>>>>());
	fakeData.get(value2).put(key2, new Pair(0.0, testing));
	output.append("Key: a2, b2 (" + testing.size() + ")\n");
		
	// generate some fake HistoTuples. these are unused but the code would crash without themnew HistoTuple (k, String("fake" + k), value);
	HistoTuple foos[] = new HistoTuple[s];
	for (int k = 0; k < s; k++)
		foos[k] = new HistoTuple (k, "fake" + k, value);
	// // generate some fake HistoTuples. these are unused but the code would crash without them
	// HistoTuple foo = new HistoTuple(1, "fake1", valueType);
	// HistoTuple foo2 = new HistoTuple(2, "fake2", valueType);
	
	histogramData.putHistogramSet(fakeData);
		
	//output.append(allHistogramsMap.get(0).get(key2).get(0).toString());
	return Response.status(200).entity(output.toString()).build();
    }
	
    public double norm(double[] v) {
	double n = 0.0;
	for (int i = 0; i < v.length; i++)
	    n += v[i]*v[i];
	return Math.sqrt(n);
    }

    @GET
    @Path("/populateAnomalies")
    @Produces(MediaType.TEXT_PLAIN)
    public Response testFunction() {
	DataIOWriteAnomaly foo = new DataIOWriteAnomaly();
	return Response.status(200).entity(foo.writeFakeAnomalies()).build();
    }

    @GET
    @Path("/testFunction2")
    @Produces(MediaType.TEXT_PLAIN)
    public Response testFunction2() {
	DataIOWriteAnomaly foo = new DataIOWriteAnomaly();
	HashMap<Pair<Integer, Integer>, ArrayList<Pair<Integer, GenericPoint<Integer>>>> anomalies;
	String output = foo.getAnomaliesTest();

	return Response.status(200).entity(output).build();
    }

    @GET
    @Path("/packetStats")
    @Produces(MediaType.TEXT_HTML)
    public Response packetStats(@QueryParam("hostname") String hostname, 
				@QueryParam("keySpace") String keySpace, 
				@QueryParam("table") String table,
				@QueryParam("minutesBack") int minutesBack) {
	String output = new String();
	allHistogramsMapLock.writeLock().lock();


	DataIOCassandraDB dbHandle = new DataIOCassandraDB(hostname, keySpace, table);

	output = dbHandle.packetStats(minutesBack);
	dbHandle.close();

	allHistogramsMapLock.writeLock().unlock();

	return Response.status(200).entity(output).build();
    }
}
