package org.autonlab.anomalydetection;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.ListIterator;

import java.net.URI;

import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;

import org.json.simple.JSONObject;
import org.json.simple.JSONArray;
import org.json.simple.JSONValue;

import org.javatuples.*;
import com.savarese.spatial.*;

import org.joda.time.*;

public class DataIOWriteAnomaly {

    Client client;
    HashMap<Integer, String> causes;
    HashMap<Integer, String> states;

    public DataIOWriteAnomaly()
    {
	client = Client.create();
	causes = null;
	states = null;
    }

    public void closeConnection()
    {
	client.destroy();
    }

    public String writeFakeAnomalies() 
    {
	String output = new String();
	int numToCreate = 15;

	for (int predictionValue = 0; predictionValue < 4; predictionValue++) {
	    for (int i = 0; i < numToCreate; i++) {
		Long testStart = new Long(1399912491L);
		Long testEnd = new Long(1399912451L);
		Long trainStart = new Long(1399830841L);
		Long trainEnd = new Long(1399917252L);
		Integer sourceType = AnomalyDetectionConfiguration.ANOMALY_FILTER_TYPE_IP_ADDRESS;
		String sourceValue = "10.90.94.9";
		Integer targetType = AnomalyDetectionConfiguration.ANOMALY_FILTER_TYPE_IP_ADDRESS;
		String algorithm ="svm_chi_squared_1.0";
		Double score = new Double(100.0);
		Integer[] patternIndex = { };
		String[] trainingTargetValue = {  "10.80.1.148", "10.90.94.9"};
		Double[] trainingMinCount = { 0.0, 320.0 + (predictionValue * 20)};
		Double[] trainingMaxCount = { 0.0, 320.0 + (predictionValue * 20)};
		Double[] trainingMeanCount = { 0.0,  320.0 + (predictionValue * 20)};
		Double[] trainingStandardDeviation = { 0.0, 0.0 };
		String[] anomalyValue = { "10.80.1.148", "10.90.94.9"};
		Integer[] anomalyCount = { 0, 320 + (predictionValue * 20)};
		Integer[] predictedCauses = { (1 + predictionValue) };
		Integer[] predictedStates = { (1 + predictionValue) };
		String[] predictedScoreString = { "High" };

		output += writeAnomaly(testStart, testEnd, trainStart, trainEnd,
				       sourceType, sourceValue, targetType,
				       algorithm,  score,  patternIndex,
				       trainingTargetValue, trainingMinCount,
				       trainingMaxCount,  trainingMeanCount,
				       trainingStandardDeviation,  anomalyValue,
				       anomalyCount,  predictedCauses,
				       predictedStates, predictedScoreString);
	    }
	    String causeString = null;
	    String stateString = null;
	    DataIOWriteAnomaly dataConn = new DataIOWriteAnomaly();
	    causeString = dataConn.getCause(1 + predictionValue);
	    stateString = dataConn.getStates(2);
	    dataConn.closeConnection();
	    dataConn = null;
	    output += "Sent " + numToCreate + " anomalies with data [0, " + (320 + (predictionValue * 20)) + "] and cause, status " + causeString + ", " + stateString + "\n";
	}
	return output;
    }

    /**
     * write an anomaly to the database
     *
     * @param testStart seconds from epoch timestamp of test data start
     * @param testEnd seconds from epoch timestamp of test data end
     * @param trainStart seconds from epoch timestamp of training data start
     * @param trainEnd seconds from epoch timestamp of training data end
     * @param sourceType see AnomalyDetectionConfiguration.ANOMALY_FILTER_TYPE_ for values
     * @param sourceValue the string representation of the histogram value
     * @param targetType see AnomalyDetectionConfiguration.ANOMALY_FILTER_TYPE_ for values
     * @param algorithm string for how this anomaly was generated
     * @param score score that triggered this anomaly
     * @param patternIndex results from pattern detection (if any). See documentation
     * @param trainingTargetValue strings representing each histogram column in the training data
     * @param trainingMinCount array of lowest counts seen in the training data
     * @param trainingMaxCount array of highest counts seen in the training data
     * @param trainingMeanCount array of average counts seen in the training data
     * @param trainingStandardDeviation array of stddev seen in the training data
     * @param anomalyValue probably the same as trainingTargetValue
     * @param anomalyCount array of counts in the anomaly histogram
     * @param predictedCauses causes from the supervised learning component (if any)
     * @param predictedStates states from the supervised learning component (if any)
     */
    public String writeAnomaly(Long testStart, Long testEnd, Long trainStart, Long trainEnd,
			       Integer sourceType, String sourceValue, Integer targetType,
			       String algorithm, Double score, Integer[] patternIndex,
			       String[] trainingTargetValue, Double[] trainingMinCount,
			       Double[] trainingMaxCount, Double[] trainingMeanCount,
			       Double[] trainingStandardDeviation, String[] anomalyValue,
			       Integer[] anomalyCount, Integer[] predictedCauses,
			       Integer[] predictedStates, String[] predictedScoreString) {

	JSONObject obj = new JSONObject();
	DateTime testStartDateTime = new DateTime(testStart * 1000);
	obj.put("detectionTimeWindowStart", testStartDateTime.toString("EEE, dd MMM yyyy HH:mm:ss Z"));
	DateTime testEndDateTime = new DateTime(testEnd * 1000);
	obj.put("detectionTimeWindowEnd", testEndDateTime.toString("EEE, dd MMM yyyy HH:mm:ss Z"));
	DateTime trainingStartDateTime = new DateTime(trainStart * 1000);
	obj.put("trainingTimeWindowStart", trainingStartDateTime.toString("EEE, dd MMM yyyy HH:mm:ss Z"));
	DateTime trainingEndDateTime = new DateTime(trainEnd * 1000);
	obj.put("trainingTimeWindowEnd", trainingEndDateTime.toString("EEE, dd MMM yyyy HH:mm:ss Z"));
	obj.put("sourceType", sourceType);
	// 10.90.94.9 or 10.80.1.148
	obj.put("sourceValue", sourceValue);
	obj.put("targetType", targetType);
	obj.put("algorithm", algorithm);
	obj.put("score", score);


	//obj.put("patternIndex", patternIndex);
	JSONArray patternArray = new JSONArray();
	if (patternIndex != null) {
	    for (Integer onePattern : patternIndex) {
		patternArray.add(onePattern);
	    }
	}
	obj.put("patternIndex",patternArray);


	JSONArray normalEntriesArray = new JSONArray();
	if (trainingTargetValue != null) {
	    for (int i = 0; i < trainingTargetValue.length; i++) {
		JSONObject normalEntries = new JSONObject();
		normalEntries.put("sequenceNumber", new Integer(i));
		normalEntries.put("targetValue", trainingTargetValue[i]);
		normalEntries.put("minCount", trainingMinCount[i].intValue());
		normalEntries.put("maxCount", trainingMaxCount[i].intValue());
		normalEntries.put("meanCount", trainingMeanCount[i]);
		normalEntries.put("standardDeviation", trainingStandardDeviation[i]);
		normalEntriesArray.add(normalEntries);
	    }
	}
	obj.put("normalEntries", normalEntriesArray);

	JSONArray anomalyEntriesArray = new JSONArray();
	if (anomalyValue != null) {
	    for (int i = 0; i < anomalyValue.length; i++) {
		JSONObject anomalyEntries = new JSONObject();
		anomalyEntries.put("sequenceNumber",new Integer(i));
		anomalyEntries.put("targetValue", anomalyValue[i]);
		anomalyEntries.put("count", anomalyCount[i]);
		anomalyEntriesArray.add(anomalyEntries);
	    }
	}
	obj.put("anomalyEntries", anomalyEntriesArray);
	/*
	JSONArray predictedCausesArray = new JSONArray();
	if (predictedCauses != null) {
	    for (Integer oneCause : predictedCauses) {
		JSONObject predictedCausesEntry = new JSONObject();
		predictedCausesEntry.put("id", new Integer(oneCause));
		predictedCausesArray.add(predictedCausesEntry);
	    }
	}
	obj.put("predictedCauses",predictedCausesArray);

	JSONArray predictedStatesArray = new JSONArray();
	if (predictedStates != null) {
	    for (Integer oneState : predictedStates) {
		JSONObject predictedStatesEntry = new JSONObject();
		predictedStatesEntry.put("id", oneState);
		predictedStatesArray.add(predictedStatesEntry);
	    }
	}
	obj.put("predictedStates",predictedStatesArray);
	*/
	if (predictedCauses != null && predictedStates != null && predictedScoreString != null) {
	    JSONArray predictionsArray = new JSONArray();
	    for (int i = 0; i < predictedCauses.length; i++) {
		JSONObject predictionsEntry = new JSONObject();


		JSONObject predictedCauseEntry = new JSONObject();
		predictedCauseEntry.put("id", new Integer(predictedCauses[i]));
		predictionsEntry.put("cause", predictedCauseEntry);

		predictionsEntry.put("score", predictedScoreString[i]);

		JSONObject predictedStateEntry = new JSONObject();
		predictedStateEntry.put("id", new Integer(predictedStates[i]));
		predictionsEntry.put("state", predictedStateEntry);

		predictionsArray.add(predictionsEntry);
	    }
	    obj.put("predictions",predictionsArray);
	}

	String output = new String();
	//output += obj.toString();
	output += "\n";

	WebResource webResource = client.resource(AnomalyDetectionConfiguration.ANOMALY_REST_URL_PREFIX + "/anomaly");
	ClientResponse response = webResource.type("application/json").post(ClientResponse.class, obj.toString());
	String writeRes = response.getEntity(String.class);
	if (!writeRes.equals("A new anomaly and alert have been created")) {
	    output += "\nUnexpected response from writing anomaly: " + writeRes + "\n\n\n";
	}

	return output;
    }

    public String getAnomaliesTest()
    {
	Long testStart = 1399912491000L;
	Long testEnd = 1399912451000L;
	Long trainStart = 1399830841000L;
	Long trainEnd = 1399917252000L;
	String sourceValue = "10.90.94.9";
	Integer targetType = 1;
	String algorithm = "svm_chi_squared_1.0";
	Integer userState = -1;
	Integer userCause = -1;

	HashMap<Pair<Integer, Integer>, ArrayList<Pair<Integer, GenericPoint<Integer>>>> anomalies;
	anomalies = getAnomalies(testStart, testEnd, trainStart, trainEnd, sourceValue, targetType, algorithm, userState, userCause);

	String output = new String();
	for (Pair<Integer, Integer> bar : anomalies.keySet()) {
	    output += bar.getValue0() + ", " + bar.getValue1() + "\n";
	    for (Pair<Integer, GenericPoint<Integer>> oneData : anomalies.get(bar)) {
		output += "[";
		for (int i = 0; i < oneData.getValue1().getDimensions(); i++) {
		    output += oneData.getValue1().getCoord(i) + ",";
		}
		output += "]\n";
	    }
	}

	return output;
    }

    public HashMap<Pair<Integer, Integer>, ArrayList<Pair<Integer, GenericPoint<Integer>>>> getAnomalies(
			Long testStart, Long testEnd, Long trainStart, Long trainEnd,
			String sourceValue, Integer targetType, String algorithm,
			Integer userState, Integer userCause)
    {
	String ret = new String();
	String arg = new String();

	if (testStart > 0) {
	    arg += "&detectionTimeWindowStart=" + testStart;
	}
	if (testEnd > 0) {
	    arg += "&detectionTimeWindowEnd=" + testEnd;
	}
	if (trainStart > 0) {
	    arg += "&trainingTimeWindowStart=" + trainStart;
	}
	if (trainEnd > 0) {
	    arg += "&trainingTimeWindowEnd=" + trainEnd;
	}
	if (sourceValue.length() > 0) {
	    arg += "&sourceValue=" + sourceValue;
	}
	if (targetType > 0) {
	    arg += "&targetType=" + targetType;
	}
	if (algorithm.length() > 0) {
	    arg += "&algorithm=" + algorithm;
	}
	
	if (userCause != null && userCause > 0) {
	    arg += "&userCause=" + userCause;
	}

	if (userState != null && userState > 0) {
	    arg += "&userState=" + userState;
	}
	System.out.println("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX " +arg + "\n");
	WebResource webResource = client.resource(AnomalyDetectionConfiguration.ANOMALY_REST_URL_PREFIX + "/anomaly/query/?" + arg);
	ret = webResource.accept("application/json").get(String.class);

	JSONArray retArray = new JSONArray();
	retArray = (JSONArray)JSONValue.parse(ret);

	//	String testState = "[{\"id\":1,\"state\":\"1\"}]";
	//Object retObj = JSONValue.parse(testState);
	//JSONArray retArray = (JSONArray)retObj;


	HashMap<Pair<Integer, Integer>, ArrayList<Pair<Integer, GenericPoint<Integer>>>> anomalyData = new HashMap();

	for (int i = 0; i < retArray.size(); i++) {
	    Object oneObj = retArray.get(i);
	    JSONObject oneJObj = (JSONObject)oneObj;

	    JSONObject oneCause = (JSONObject)oneJObj.get("userCause");
	    Integer cause = -1;
	    if (oneCause != null) {
		Object oneCauseID = oneCause.get("id");
		if (oneCauseID != null) {
		    cause = Integer.parseInt(oneCauseID.toString());
		}
		else {
		    System.out.println(ret + "\n\n");
		}
	    }

	    JSONObject oneState = (JSONObject)oneJObj.get("userState");
	    Integer state = -1;
	    if (oneState != null) {
		Object oneStateID = oneState.get("id");
		if (oneStateID != null) {
		    state = Integer.parseInt(oneStateID.toString());
		}
		else {
		    System.out.println(ret + "\n\n");
		}
	    }

	    Pair<Integer, Integer> key = new Pair(cause, state);
	    if (!anomalyData.containsKey(key)) {
		anomalyData.put(key, new ArrayList());
	    }

	    JSONArray anomalyEntries =(JSONArray)oneJObj.get("anomalyEntries");
	    GenericPoint<Integer> point = new GenericPoint(anomalyEntries.size());
	    for (int j = 0; j < anomalyEntries.size(); j++) {
		JSONObject oneAnomaly = (JSONObject)anomalyEntries.get(j);
		Integer count = Integer.parseInt(oneAnomaly.get("count").toString());
		Integer sequenceNumber = Integer.parseInt(oneAnomaly.get("sequenceNumber").toString());
		point.setCoord(sequenceNumber, count);
	    }
	    // Using timestamps of 0 for now. Not sure if it matters yet
	    anomalyData.get(key).add(new Pair(0, point));
	}
	return anomalyData;
    }

    /* We should do some sort of caching here but we don't have a mechanism for invalidating the cache so for now we just retrieve the info every time */
    public String getCause(Integer lookupID)
    {
	//if (causes != null) {
	//return this.causes.get(lookupID);
	//}
	WebResource webResource = client.resource(AnomalyDetectionConfiguration.ANOMALY_REST_URL_PREFIX + "/anomaly/causes/");
	String ret = webResource.accept("application/json").get(String.class);
	JSONArray retArray = new JSONArray();
	retArray = (JSONArray)JSONValue.parse(ret);
	
	this.causes = new HashMap();

	for (int i = 0; i < retArray.size(); i++) {
	    Object oneObj = retArray.get(i);
	    JSONObject oneJObj = (JSONObject)oneObj;

	    
	    Integer id = Integer.parseInt(oneJObj.get("id").toString());
	    String cause = oneJObj.get("cause").toString();
	    this.causes.put(id, cause);
	}

	return this.causes.get(lookupID);
    }

    
    public String getStates(Integer lookupID)
    {
	//if (states != null) {
	//    return this.states.get(lookupID);
	//}
	WebResource webResource = client.resource(AnomalyDetectionConfiguration.ANOMALY_REST_URL_PREFIX + "/anomaly/states/");
	String ret = webResource.accept("application/json").get(String.class);
	JSONArray retArray = new JSONArray();
	retArray = (JSONArray)JSONValue.parse(ret);
	
	this.states = new HashMap();

	for (int i = 0; i < retArray.size(); i++) {
	    Object oneObj = retArray.get(i);
	    JSONObject oneJObj = (JSONObject)oneObj;

	    
	    Integer id = Integer.parseInt(oneJObj.get("id").toString());
	    String state = oneJObj.get("state").toString();
	    this.states.put(id, state);
	}

	return this.states.get(lookupID);
    }
}
