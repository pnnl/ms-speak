package org.autonlab.anomalydetection;

import com.savarese.spatial.*;
import java.util.*;
import org.apache.commons.collections.map.*;
import org.javatuples.*;

public class KDTreeCalc {
   /**
     * Convert the training data from a hash of (<GenericPoint> -> HistoTuple<date, message type>) to (<GenericPoint> -> KDTree)
     *
     * @param trainHashMap The HashMap to be converted to a mapping to KDTree
     * @param output this function will append the list all seen combinations of <GenericPoint>
     * @return HashMap of <GenericPoint>  to KDTree
     * 
     */
    public static HashMap<GenericPoint<String>,KDTree<Integer, GenericPoint<Integer>, java.lang.Integer>> makeKDTree(GenericPoint<String> valueType, HashMap<GenericPoint<String>, Pair<Double, ArrayList<Pair<Integer, GenericPoint<Integer>>>>> trainHashMap, StringBuilder output) {
	HashMap<GenericPoint<String>, KDTree<Integer, GenericPoint<Integer>, java.lang.Integer>> newMap = new HashMap();

	for (GenericPoint<String> keyAddr : trainHashMap.keySet()) {
	    if (output != null) {
		output.append(keyAddr.toString());
	    }
	    newMap.put(keyAddr, GetKDTree(valueType, trainHashMap.get(keyAddr).getValue1()));
	}
	
	return newMap;
    }

    public static KDTree<Integer, GenericPoint<Integer>, java.lang.Integer> GetKDTree(GenericPoint<String> valueType, ArrayList<Pair<Integer, GenericPoint<Integer>>> histograms) {
	KDTree<Integer, GenericPoint<Integer>, java.lang.Integer> treeKD = new KDTree<Integer, GenericPoint<Integer>, java.lang.Integer>(HistoTuple.getDimensions(valueType));

	for (Pair<Integer, GenericPoint<Integer>> dataPair : histograms) {
	    treeKD.put(dataPair.getValue1(), dataPair.getValue0());
	}
	return treeKD;
    }

   /**
    * @param histogramData Object containing the histograms
    * @param trainID ID of the model to use to train on
    * @param trainKey Key index for the training set histograms
    * @param testID ID of the model to use to test on
    * @param testKey Key index for the test set histograms
    * @param results If not null, every result will be recorded here as score->timestamp. We use a MultiValueMap so duplicate scores will still be recorded
    */
    public static String runOneTestKDTree(HistogramStore histogramData, Integer trainID, GenericPoint<String> trainKey, GenericPoint<String> trainValue, Integer testID, GenericPoint<String> testKey, GenericPoint<String> testValue, MultiValueMap results) {
	NearestNeighbors<Integer, GenericPoint<Integer>, java.lang.Integer> neighbor = new NearestNeighbors<Integer, GenericPoint<Integer>, java.lang.Integer>();

	String output = new String();

	HistoTuple.upgradeWindowsDimensions(trainValue, histogramData.getHistograms(trainID, trainValue, trainKey), histogramData.getHistograms(testID, testValue, testKey), null);

	KDTree<Integer, GenericPoint<Integer>, java.lang.Integer> trainTree = KDTreeCalc.GetKDTree(trainValue, histogramData.getHistograms(trainID, trainValue, trainKey));

	// The GenericPoints are often duplicated so we could add a cache here but I'm not sure if performace would improve by that much. KDTrees are already log time
	for (Pair<Integer, GenericPoint<Integer>> tempPair : histogramData.getHistograms(testID, testValue, testKey)) {
	    Integer histogramTime = (Integer)tempPair.getValue(0);
	    GenericPoint<Integer> histogramValue = (GenericPoint<Integer>)tempPair.getValue(1);

	    NearestNeighbors.Entry<Integer, GenericPoint<Integer>, java.lang.Integer>[] vals = neighbor.get(trainTree, histogramValue, 1, false);

	    if (results != null) {
		results.put(vals[0].getDistance(), histogramTime);
	    }
	    output += "time " + histogramTime + " distance for " + histogramValue.toString() + " is " + vals[0].getDistance() + "\n";
	}

	return output;
    }
}