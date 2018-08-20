package org.autonlab.anomalydetection;

import java.util.*;
import org.javatuples.*;
import com.savarese.spatial.*;

/**
 * This class is not thread safe
 */
public class HistoTuple {
    /*
     * There are few unique strings so to save memory we map the string
     * to an Integer and store with each record instead
     * The mappings are first categorized by the type of value
     */
    static volatile HashMap<GenericPoint<String>, HashMap<String, Integer>> _valueMap = new HashMap();

    /*
     * we use the volatile keyword for the above static values because each REST daemon call
     * starts a new thread 
     */

    double _timeStamp;
    int _msgIndex; // This HistoTuple's message type as an index into the _valueMap mapping

    // if this HistoTuple is in the current sliding window or not
    // we need this so we don't remove it if it was never in it in the first place
    boolean _wasCounted; 

    public static void resetMap () {
	_valueMap = new HashMap();
    }

    /**
     * Make a new histoTuple
     *
     * @param timeStamp the time from epoch
     * @param value the message type
     * @param valueType type of value
     */
    public HistoTuple(double timeStamp, String value, GenericPoint<String> valueType) {
	// the timestamp could be stored as an int to save memory
	_timeStamp = timeStamp;
	_msgIndex = -1;
	_wasCounted = false; 

	if (!_valueMap.containsKey(valueType)) {
	    _valueMap.put(valueType, new HashMap());
	}
	if (_valueMap.get(valueType).containsKey(value)) {
	    _msgIndex = _valueMap.get(valueType).get(value).intValue();
	}
	else {
	    _valueMap.get(valueType).put(value, _valueMap.get(valueType).size());
	    _msgIndex = _valueMap.get(valueType).size() - 1; // -1 because _valueMap.size() increased in the previous line
	}

    }

     /**
     * set whether or not this tuple is counted in the sliding window
     *
     * @param val set whether or not this HistoTuple is counted in the current sliding window
     */
    private void setWasCounted(boolean val) {
	_wasCounted = val;
    }

    /**
     * @return timestamp associated with this HistoTuple
     */
    public double getTimeStamp() {
	return _timeStamp;
    }

    /**
     * @return message type ID for this HistoTuple
     */
    public int getMsgType() {
	return _msgIndex;
    }

    /**
     * @return whether or not this tuple is counted in the sliding window
     */
    private boolean getWasCounted() {
	return _wasCounted;
    }

    /**
     * @return the number of unique value seen
     */
    public static int getDimensions(GenericPoint<String> valueType) {
	int size = _valueMap.get(valueType).size();
	return size;
    }

    /**
     * @return all of the dimensions in <dim> <dim name> format
     */
    public static String getDimensionNames() {
	String output = new String();

	for (GenericPoint<String> valueType : _valueMap.keySet()) {
	    for (String keyVal : _valueMap.get(valueType).keySet()) {
		output += valueType + " : " +  _valueMap.get(valueType).get(keyVal) + " " + keyVal + "\n";
	    }
	}

	return output;
    }

    public static String[] getDimensionNamesArray() {
	String[] ret = null;
	// making a bad assumption here that there is only one valuetype
	for (GenericPoint<String> valueType : _valueMap.keySet()) {
	    ret = new String[_valueMap.get(valueType).size()];
	    for (String keyVal : _valueMap.get(valueType).keySet()) {
		ret[_valueMap.get(valueType).get(keyVal)] = keyVal;
	    }
	}

	return ret;
    }

    /**
     * This code works for any number of dimensions
     * This code assumes that the input file is ordered by time
     *
     * Every data subset within a given ID will have the same time ranges even if some of the windows will have all zeros
     */
    public static HashMap<GenericPoint<String>, HashMap<GenericPoint<String>, Pair<Double, ArrayList<Pair<Integer, GenericPoint<Integer>>>>>> mergeWindows(HashMap<GenericPoint<String>, HashMap<GenericPoint<String>, ArrayList<HistoTuple>>> listMap, int windowSecs, int slideSecs) {
	// The code will probably work if this restriction is removed. It was written to handle this case.
	if (slideSecs > windowSecs) {
	    throw new RuntimeException("slideSecs is higher than windowSecs. This is not permitted as it might skip training data");
	}

	HashMap<GenericPoint<String>, HashMap<GenericPoint<String>, Pair<Double, ArrayList<Pair<Integer, GenericPoint<Integer>>>>>> ret = new HashMap();


	for (GenericPoint<String> valueName : listMap.keySet()) {

	    if (!ret.containsKey(valueName)) {
		System.out.println("XYZ new value name " +valueName.toString());
		ret.put(valueName, new HashMap<GenericPoint<String>, Pair<Double, ArrayList<Pair<Integer, GenericPoint<Integer>>>>>());
	    }

	    double startTime = Double.MAX_VALUE;
	    double endTime = 0;
	    for (GenericPoint<String> mapKey : listMap.get(valueName).keySet()) {
		ArrayList<HistoTuple> list = listMap.get(valueName).get(mapKey);
		for (HistoTuple oneTuple : list) {
		    if (oneTuple._timeStamp < startTime) {
			startTime = oneTuple._timeStamp;
		    }
		    if (oneTuple._timeStamp > endTime) {
			endTime = oneTuple._timeStamp;
		    }
		}
	    }

	    //look at each category's value. mapKey is source_addr;10.0.0.1, etc
	    for (GenericPoint<String> mapKey : listMap.get(valueName).keySet()) {
		ArrayList<HistoTuple> list = listMap.get(valueName).get(mapKey);

		// the highest index that has not yet been processed
		int headIndex = 0;
		HistoTuple headTuple = null;
		// the lowest index that has been processed already
		int tailIndex = 0;
		HistoTuple tailTuple = null;
		// the beginning of the current window
		int currentSecs = (int)startTime;

		// this check also allows us to safely do list.get(0) later on
		if (list.size() == 0) {
		    throw new RuntimeException("Got no tuples from arraylist");
		}

		ArrayList<Pair<Integer, GenericPoint<Integer>>> data = new ArrayList<Pair<Integer, GenericPoint<Integer>>>();
		int[] histogram = new int[HistoTuple.getDimensions(valueName)];

		headTuple = list.get(0);
		tailTuple = list.get(0);

		int windowCount = 0;
		int addCount = 0;
		slidingWindow:
		// headTuple points to the newest tuple within the sliding window
		// tailTuple the oldest
		//while (currentSecs < endTime) {
		//once a window runs off the edge we want to stop immediately so we don't get a window that's only partially filled
		while (currentSecs + windowSecs <= endTime) {
		    addCount = 0;
		    // System.out.print("Window is " + currentSecs + " to " + (currentSecs+windowSecs) + ". Histogram: ");
		    // add to the histogram tuples that have entered the window
		    while (headTuple != null && headTuple.getTimeStamp() < (currentSecs + windowSecs)) {

			// incase the sliding window skips values
			if (headTuple.getTimeStamp() >= currentSecs) {
			    //System.out.println(headTuple.getTimeStamp() + " compared to " + currentSecs);
			    addCount++;
			    histogram[headTuple.getMsgType()]++;
			    headTuple.setWasCounted(true);
			    //		    System.out.println("Added" + headTuple.getTimeStamp() + " " + headTuple.getMsgType());
			}

			headIndex++;
			if (headIndex < list.size()) {
			    headTuple = list.get(headIndex);
			}
			else {
			    System.out.println("head is done " + tailIndex);
			    headTuple = null;
			    //break slidingWindow;
			}
		    }

		    // remove from the histogram tuples that have fallen out of the window
		    while (tailTuple != null && tailTuple.getTimeStamp() < currentSecs) {
			if (tailTuple.getWasCounted() == true) {
			    histogram[tailTuple.getMsgType()]--;
			    tailTuple.setWasCounted(false);
			    //   System.out.println("removed");
			}
		    
			tailIndex++;
			if (tailIndex < list.size()) {
			    tailTuple = list.get(tailIndex);
			}
			else {
			    System.out.println("Tail is done " + tailIndex);
			    tailTuple = null;
			    //break slidingWindow;
			}
		    }

		    if (tailIndex > headIndex) {
			throw new RuntimeException("tailIndex (" + tailIndex + ") is higher than headIndex (" + headIndex + ")");
		    }

		    GenericPoint<Integer> myPoint = new GenericPoint<Integer>(HistoTuple.getDimensions(valueName));
		    for (int i = 0; i < HistoTuple.getDimensions(valueName); i++) {
			//System.out.print(histogram[i] + " ");
			myPoint.setCoord(i, histogram[i]);
		    }

		    Pair<Integer, GenericPoint<Integer>> temp = new Pair<Integer, GenericPoint<Integer>>(currentSecs, myPoint);
		    data.add(temp);
		    //System.out.println("");
		    // Slide the window forward for the next iteration
		    currentSecs += slideSecs;
		    windowCount++;
		    // System.out.println("slide");
		}

		int remainderCount = 0;
		for (int i = 0; i < HistoTuple.getDimensions(valueName); i++) {
		    remainderCount += histogram[i];
		}
		if (remainderCount > 0) {
		    System.out.println("Warning: the final " + addCount + " rows did not fill a full window period and that histogram was dropped:");
		    for (int i = 0; i < HistoTuple.getDimensions(valueName); i++) {
			System.out.print(histogram[i] + " ");
		    }
		    System.out.println("");
		}
		System.out.println("XYZ data " +valueName.toString() + " and " + mapKey.toString());
		ret.get(valueName).put(mapKey, new Pair<Double, ArrayList<Pair<Integer, GenericPoint<Integer>>>>(-1.0,data));
	    }
	}

	return ret;
    }

    public static boolean upgradeWindowsDimensions(GenericPoint<String> valueType, ArrayList<Pair<Integer, GenericPoint<Integer>>> histogramA, ArrayList<Pair<Integer, GenericPoint<Integer>>> histogramB, ArrayList<Pair<Integer, GenericPoint<Integer>>> histogramC) {
	boolean retA = false;
	boolean retB = false;
	boolean retC = false;

	retA = upgradeWindowsDimensionsOne(valueType, histogramA);
	retB = upgradeWindowsDimensionsOne(valueType, histogramB);
	if (histogramC != null) {
	    retC = upgradeWindowsDimensionsOne(valueType, histogramC);
	}

	if (retA == true || retB == true || retC == true) {
	    return true;
	}
	return false;
    }


    /**
     * When a HistoTuple is made, it is set with the current number of dimensions. Later, the number of dimensions may
     * change and a new HistoTuple will have a greater number of dimensions. To run tests between two HistoTuples 
     * they must have the same dimensions, and this function upgrades an old HistoTuple to the current number of dimensions.
     */
    private static boolean upgradeWindowsDimensionsOne(GenericPoint<String> valueType, ArrayList<Pair<Integer, GenericPoint<Integer>>> histogram) {

	if (histogram.size() == 0) {
	    return false;
	}

	if (histogram.get(0).getValue1().getDimensions() == _valueMap.get(valueType).size()) {
	    return false;
	}
	for (int ii = 0; ii < histogram.size(); ii++) {
	    GenericPoint oldPoint = histogram.get(ii).getValue1();
	    GenericPoint newPoint = new GenericPoint(_valueMap.get(valueType).size());
	    for (int jj = 0; jj < _valueMap.get(valueType).size(); jj++) {
		if (jj < oldPoint.getDimensions()) {
		    newPoint.setCoord(jj, oldPoint.getCoord(jj));
		}
		else {
		    newPoint.setCoord(jj, 0);
		}
	    }

	    Pair<Integer, GenericPoint<Integer>> histogramTemp = new Pair(histogram.get(ii).getValue0(), newPoint);
	    histogram.set(ii, histogramTemp);
	}
	return true;
    }

}