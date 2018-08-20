package org.autonlab.anomalydetection;

import com.savarese.spatial.*;

import java.util.*;

import org.apache.commons.collections.map.*;
import org.javatuples.*;


public class HistogramStore {
    //               ID                value                          category              scaling                 time       histogram
    private HashMap<Integer, HashMap<GenericPoint<String>, HashMap<GenericPoint<String>, Pair<Double, ArrayList<Pair<Integer, GenericPoint<Integer>>>>>>> allHistogramsMap;
    private HashMap<GenericPoint<String>, HashMap<GenericPoint<String>, HashMap<Pair<Integer, Integer>, Integer>>> allHistogramsMapKeyRemap;

    private int nextHistogramMapID;

    public HistogramStore() {
	 allHistogramsMap = new HashMap();
	 allHistogramsMapKeyRemap = new HashMap();
	 nextHistogramMapID = 0;
    }

    public Set<Integer> getIDList() {
	return allHistogramsMap.keySet();
    }

    public Boolean isIDValid(Integer id) {
	if (allHistogramsMap.get(id) == null) { 
	    return false;
	}
	return true;
    }

    public Boolean isValueValid(Integer id, GenericPoint<String> valueName) {
	if (allHistogramsMap.get(id).get(valueName) == null) {
	    return false;
	}
	return true;
    }

    public Boolean isCategoryValid(Integer id, GenericPoint<String> valueName, GenericPoint<String> categoryName) {
	if (allHistogramsMap.get(id).get(valueName).get(categoryName) == null) {
	    return false;
	}
	return true;
    }

    public Integer getNextID() {
	return nextHistogramMapID;
    }

    public Set<GenericPoint<String>> getValueList(Integer id) {
	return allHistogramsMap.get(id).keySet();
    }

    public Set<GenericPoint<String>> getCategoryList(Integer id, GenericPoint<String> valueName) {
	return allHistogramsMap.get(id).get(valueName).keySet();
    }

    public ArrayList<Pair<Integer, GenericPoint<Integer>>> getHistograms(Integer id, GenericPoint<String> valueName, GenericPoint<String> categoryPoint) {
	return allHistogramsMap.get(id).get(valueName).get(categoryPoint).getValue1();
    }

    public Double getScalingFactor(Integer id, GenericPoint<String> valueName, GenericPoint<String> categoryPoint) {
	return allHistogramsMap.get(id).get(valueName).get(categoryPoint).getValue0();
    }

    public void setScalingFactor(Integer id, GenericPoint<String> valueName, GenericPoint<String> categoryPoint, Double scalingFactor) {
	allHistogramsMap.get(id).get(valueName).put(categoryPoint, allHistogramsMap.get(id).get(valueName).get(categoryPoint).setAt0(scalingFactor));
    }

    public Integer getHistogramsDataCount(Integer id, GenericPoint<String> valueName, GenericPoint<String> categoryPoint) {
	return getHistograms(id, valueName, categoryPoint).size();
    }
	
    public Integer putHistogramSet(HashMap<GenericPoint<String>, HashMap<GenericPoint<String>, Pair<Double, ArrayList<Pair<Integer, GenericPoint<Integer>>>>>> putData) {
	Integer id = nextHistogramMapID;
	allHistogramsMap.put(id, putData);
	nextHistogramMapID++;
	return id;
    }

    /*
     * The first dimension is an array one for each value in the histogram
     * For each of these there are 4 values the min, max, mean, and stddev for those values in the dataset
     */
    public Double[][] getHistogramStats(Integer id, GenericPoint<String> valueName, GenericPoint<String> categoryPoint) {
	ArrayList<Pair<Integer, GenericPoint<Integer>>> data = getHistograms(id, valueName, categoryPoint);
	if (data == null || data.size() == 0) {
	    return null;
	}

	Double[][] ret = null;

	int dimensions = data.get(0).getValue1().getDimensions();
	ret = new Double[4][dimensions];
	Double dataPointCount = new Double(data.size());
	for (int i = 0; i < dimensions; i++) {
	    ret[0][i] = Double.MAX_VALUE; // store min
	    ret[1][i] = Double.MIN_VALUE; // store max
	    ret[2][i] = 0.0; // store mean
	    ret[3][i] = 0.0; // store stddev
	}

	for (Pair<Integer, GenericPoint<Integer>> oneData : data) {
	    for (int i = 0; i < dimensions; i++) {
		Integer val = oneData.getValue1().getCoord(i);
		if (val > ret[1][i]) {
		    ret[1][i] = new Double(val);
		}
		if (val < ret[0][i]) {
		    ret[0][i] = new Double(val);
		}
		ret[2][i] += new Double(val);
	    }
	}
	for (int i = 0; i < dimensions; i++) {
	    ret[2][i] /= dataPointCount;
	}

	for (Pair<Integer, GenericPoint<Integer>> oneData : data) {
	    for (int i = 0; i < dimensions; i++) {
		Integer val = oneData.getValue1().getCoord(i);
		ret[3][i] += new Double(Math.pow(val-ret[2][i], 2));
	    }
	}
	for (int i = 0; i < dimensions; i++) {
	    ret[3][i] /= dataPointCount;
	    ret[3][i] = Math.sqrt(ret[3][i]);
	}

	return ret;
    }

    public Boolean deleteHistogramSet(Integer id) {
	if (!allHistogramsMap.containsKey(id)) {
	    return false;
	}
	allHistogramsMap.remove(id);
	return true;
    }
	
    /**
     * The calling function must hold the semaphore(?? not sure yet)
     *
     * Return the data ID for this category and value. If the category does not exist but is a subset of existing categories, we generate
     * a new data ID and copy the relevant data into it and return that ID
     *
     * @param id The data index ID returned when the data was read in
     * @param categoryPoint category
     * @param valuePoint histogram values
     * @param output function will add text to this if it makes a new mapping
     *
     * @return the ID that contains the data with indexes valueCSV and categoryCSV (which may be different from the input id) or -1 if none
     */
    public Integer recalculateByCategory(Integer id, GenericPoint<String> categoryPoint, GenericPoint<String> valuePoint, StringBuilder output) {

	// If the data we want is already there
	if (allHistogramsMap.get(id) == null) {
	    throw new RuntimeException("Error: id " + id + " not found");
	}
	if (allHistogramsMap.get(id).get(valuePoint) == null) {
	    throw new RuntimeException("Error: value key '" + valuePoint + "' not found");
	}
	if (allHistogramsMap.get(id).get(valuePoint).get(categoryPoint) != null) {
	    return id;
	}

	Pair<Integer, Integer> startAndEnd = getStartAndEndTime(id);
	if (allHistogramsMapKeyRemap.get(valuePoint) != null &&
	    allHistogramsMapKeyRemap.get(valuePoint).get(categoryPoint) != null &&
	    startAndEnd != null &&
	    allHistogramsMapKeyRemap.get(valuePoint).get(categoryPoint).get(startAndEnd) != null) {
	    return allHistogramsMapKeyRemap.get(valuePoint).get(categoryPoint).get(startAndEnd);
	}

	allHistogramsMap.put(nextHistogramMapID, new HashMap<GenericPoint<String>, HashMap<GenericPoint<String>, Pair<Double, ArrayList<Pair<Integer, GenericPoint<Integer>>>>>>());
	allHistogramsMap.get(nextHistogramMapID).put(valuePoint, new HashMap<GenericPoint<String>, Pair<Double, ArrayList<Pair<Integer, GenericPoint<Integer>>>>>());
	allHistogramsMap.get(nextHistogramMapID).get(valuePoint).put(categoryPoint, new Pair<Double, ArrayList<Pair<Integer, GenericPoint<Integer>>>>(0.0, new ArrayList()));

	int subsetsFound = 0;
	// the histograms are in an arraylist so it's hard to add them together. Sum them in a hashmap then convert it to an arraymap
	TreeMap<Integer, GenericPoint<Integer>> newDataSum = new TreeMap(); //use TreeMap not HashMap so we get keys back in sorted orders
	for (GenericPoint<String> oneKey : allHistogramsMap.get(id).get(valuePoint).keySet()) {
	    if (isPointSubset(categoryPoint, oneKey)) {
		System.out.println("counting " + categoryPoint.toString() + " as subset as " + oneKey.toString() + "\n");
		subsetsFound++;
		for (Pair<Integer, GenericPoint<Integer>> oneHist : allHistogramsMap.get(id).get(valuePoint).get(oneKey).getValue1()) {

		    GenericPoint<Integer> sumData = newDataSum.get(oneHist.getValue0());
		    if (sumData == null) {
			sumData = new GenericPoint<Integer>(oneHist.getValue1().getDimensions());
		    }
		    int copyIndex = 0;
		    for (copyIndex = 0; copyIndex < oneHist.getValue1().getDimensions(); copyIndex++) {
			if (sumData.getCoord(copyIndex) == null) {
			    sumData.setCoord(copyIndex, oneHist.getValue1().getCoord(copyIndex));
			}
			else {
			    sumData.setCoord(copyIndex, sumData.getCoord(copyIndex) + oneHist.getValue1().getCoord(copyIndex));
			}
		    }
		    newDataSum.put(oneHist.getValue0(), sumData);
		}
	    }
	}

	// convert the newdataSum TreeMap to an ArrayList
	for (Integer timeSec : newDataSum.keySet()) {
	    allHistogramsMap.get(nextHistogramMapID).get(valuePoint).get(categoryPoint).getValue1().add(new Pair<Integer, GenericPoint<Integer>>(timeSec, newDataSum.get(timeSec)));
	}

	int newID = -1;
	if (subsetsFound > 0) {
	    newID = nextHistogramMapID;
	    nextHistogramMapID++;
	    output.append("Did not find appropriate data at ID " + id + " but was able to create it from existing data and put it in id " + newID + "\n");

	    if (allHistogramsMapKeyRemap.get(valuePoint) == null) {
		allHistogramsMapKeyRemap.put(valuePoint, new HashMap<GenericPoint<String>, HashMap<Pair<Integer, Integer>, Integer>>());
	    }
	    if (allHistogramsMapKeyRemap.get(valuePoint).get(categoryPoint) == null) {
		allHistogramsMapKeyRemap.get(valuePoint).put(categoryPoint, new HashMap<Pair<Integer, Integer>, Integer>());
	    }
	    startAndEnd = getStartAndEndTime(newID);
	    allHistogramsMapKeyRemap.get(valuePoint).get(categoryPoint).put(startAndEnd, newID);
	}

	return newID;
    }

    /**
     * Get the times for the first and last histograms for a given ID. All data within one ID has the same time windows
     *
     * @param id
     */
    public Pair<Integer, Integer> getStartAndEndTime(Integer id) {
	if (allHistogramsMap.get(id) == null) {
	    return null;
	}
	System.out.println("looking for id " + id);
	for (GenericPoint<String> category : allHistogramsMap.get(id).keySet()) {
	    for (GenericPoint<String> key : allHistogramsMap.get(id).get(category).keySet()) {
		System.out.println("ONE");
		int size = allHistogramsMap.get(id).get(category).get(key).getValue1().size();
		if (size == 0) {
		    continue;
		}
		System.out.println("size " + size);

		Integer firstTime = allHistogramsMap.get(id).get(category).get(key).getValue1().get(0).getValue0();
		Integer lastTime = allHistogramsMap.get(id).get(category).get(key).getValue1().get(size - 1).getValue0();
		Pair<Integer, Integer> ret = new Pair(firstTime, lastTime);
		return ret;
	    }
	}
	return null;
    }

    /**
     * Compare the string names in a GenericPoint. This is for the category names only and
     * not the histogram values
     * The caller must hold the semaphore
     *
     * @param testPoint the point that may be a subset
     * @param bigPoint the point that may be a superset
     *
     * @return true if every coord in testPoint also exists in bigPoint, false otherwise
     */
    public Boolean isPointSubset(GenericPoint<String> testPoint, GenericPoint<String> bigPoint) {

	if (bigPoint.getDimensions() <  testPoint.getDimensions()) {
	    return false;
	}

	int bigPointCoord = 0;
	int testPointCoord = 0;

	while (bigPointCoord < bigPoint.getDimensions() && testPointCoord < testPoint.getDimensions()) {
	    if (testPoint.getCoord(testPointCoord).equals(bigPoint.getCoord(bigPointCoord))) {
		bigPointCoord++;
		testPointCoord++;
	    }
	    else {
		bigPointCoord++;
	    }
	}
	if (testPointCoord == testPoint.getDimensions()) {
	    return true;
	}

	return false;
    }
}