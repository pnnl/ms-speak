package org.autonlab.anomalydetection;

import com.savarese.spatial.*;

import java.util.*;

import libsvm.*;

import org.apache.commons.collections.map.*;
import org.javatuples.*; //Tuples, Pair

/**
 * We use a chi-squared kernel. k(x,y) = 1- (sum[1->n, (xi-yi)^2 / .5(xi+yi)])
 * or an RBF kernel. k(x,y) = exp(-gamma*sum[1->n, (xi-yi)^2])
 * See http://crsouza.blogspot.com/2010/03/kernel-functions-for-machine-learning.html
 */
// MultiValueMap is not thread safe
// also, NU_START_POW_LOW is modified
public class SVMCalc {
     // cache of processed models. This is shared across concurrent accesses so we need to protect it with a lock
    static volatile HashMap<Integer, HashMap<GenericPoint<String>, HashMap<GenericPoint<String>, svm_model>>> _svmModelsCache = new HashMap();

    public static svm_model generateModel(ArrayList<Pair<Integer, GenericPoint<Integer>>> histograms, double targetCrossTrainAccuracy, ArrayList<Pair<Integer, GenericPoint<Integer>>> histogramsAnomaly, double targetAnomalyAccuracy) {
	return generateModelMain(histograms, null, targetCrossTrainAccuracy, histogramsAnomaly, targetAnomalyAccuracy, svm_parameter.ONE_CLASS);
    }

    public static svm_model generateModelOneVsAll(ArrayList<Pair<Integer, GenericPoint<Integer>>> histogramsClass1, ArrayList<Pair<Integer, GenericPoint<Integer>>> histogramsClass2, double targetCrossTrainAccuracy) {
	return generateModelMain(histogramsClass1, histogramsClass2, targetCrossTrainAccuracy, null, 0.0, svm_parameter.NU_SVC);
    }

    private static svm_model generateModelMain(ArrayList<Pair<Integer, GenericPoint<Integer>>> histogramsClass1, ArrayList<Pair<Integer, GenericPoint<Integer>>> histogramsClass2, double targetCrossTrainAccuracy, ArrayList<Pair<Integer, GenericPoint<Integer>>> histogramsAnomaly, double targetAnomalyAccuracy, Integer classifierType) {
	TreeMap<Double, Double> nuValues = new TreeMap();
	System.out.println("YYY -------------------------");
	// generate a list of nu values to try (we can add to this later)
	for (double testNU : AnomalyDetectionConfiguration.NU_BASE_LIST) {
	    for (int testPow = AnomalyDetectionConfiguration.NU_START_POW_LOW; testPow <= AnomalyDetectionConfiguration.NU_START_POW_HIGH; testPow++) {
		nuValues.put(testNU * Math.pow(10, testPow), -1.0); // negative indicates that we still need to calculate it
	    }
	}

	// fill in the svm_problem with the histogram data points
	int histSize = histogramsClass1.size();
	if (histogramsClass2 != null) {
	    histSize += histogramsClass2.size();
	}
	svm_problem svmProblem = new svm_problem();
	svmProblem.l = histSize;
	svmProblem.y = new double[histSize];
	Arrays.fill(svmProblem.y, 1.0); // all of our training data is non-anomalous
	if (histogramsClass2 != null) {
	    for (int i = histogramsClass1.size(); i < histSize; i++) {
		svmProblem.y[i] = 2.0;
	    }
	}

	ArrayList<Pair<Integer, GenericPoint<Integer>>> histogramsCombined = null;

	if (histogramsClass2 == null) {
	    histogramsCombined = histogramsClass1;
	}
	else {
	    histogramsCombined = new ArrayList();
	    histogramsCombined.addAll(histogramsClass1);
	    histogramsCombined.addAll(histogramsClass2);
	}
	svmProblem.x =  (new SVMKernel(histogramsCombined, histogramsCombined, AnomalyDetectionConfiguration.SVM_KERNEL_TYPE, AnomalyDetectionConfiguration.SVM_TYPE_PRECOMPUTED_KERNEL_TYPE, AnomalyDetectionConfiguration.NUM_THREADS)).getData();

	svm_problem svmProblemAnomaly = null;
	if (histogramsAnomaly != null) {
	    svmProblemAnomaly = new svm_problem();
	    svmProblemAnomaly.l = histogramsAnomaly.size();
	    svmProblemAnomaly.y = new double[histogramsAnomaly.size()];
	    Arrays.fill(svmProblemAnomaly.y, -1.0); // set all of this data to anomalous
	    svmProblemAnomaly.x =  (new SVMKernel(histogramsAnomaly, histogramsCombined, AnomalyDetectionConfiguration.SVM_KERNEL_TYPE, AnomalyDetectionConfiguration.SVM_TYPE_PRECOMPUTED_KERNEL_TYPE, AnomalyDetectionConfiguration.NUM_THREADS)).getData();
	}

	svm_parameter svmParameter = new svm_parameter();
	svmParameter.svm_type = classifierType;
	svmParameter.kernel_type = AnomalyDetectionConfiguration.SVM_KERNEL_TYPE;
	svmParameter.cache_size = AnomalyDetectionConfiguration.SVM_CACHE_SIZE;
	svmParameter.eps = AnomalyDetectionConfiguration.SVM_EPS;
	svmParameter.gamma = AnomalyDetectionConfiguration.SVM_GAMMA;
	// the library uses kfold
	svmParameter.nu = allCrossValidate(svmProblem, svmParameter, nuValues, targetCrossTrainAccuracy, histogramsAnomaly, svmProblemAnomaly, targetAnomalyAccuracy);
	if (svmParameter.nu == -1) {
	    throw new RuntimeException("nu was not set");
	}
	System.out.println("YYY picked a nu of " + svmParameter.nu);

	// I don't know what limits we should set for expanding but I just don't want to get stuck in an infinite loop
	// or somehow have so small a nu that it stops being relevant
	int expandTimes = 0;
	while (svmParameter.nu == nuValues.firstKey() && expandTimes < 5) {
	    System.out.println("YYY expanding");
	    for (double testNU : AnomalyDetectionConfiguration.NU_BASE_LIST) {
		for (int testPow = AnomalyDetectionConfiguration.NU_START_POW_LOW; testPow > AnomalyDetectionConfiguration.NU_START_POW_LOW - AnomalyDetectionConfiguration.NU_EXPAND_INCREMENT; testPow--) {
		    nuValues.put(testNU * Math.pow(10, testPow), -1.0); // negative indicates that we still need to calculate it
		}
	    }

	    // The previous nu could still be the best option. We set this to -1 so allCrossValidate reconsiders it
	    // It is a hack because it causes us to re-do the work of calculating it. If this becomes a performance
	    // problem we can do something smarter
	    nuValues.put(svmParameter.nu, -1.0);

	    AnomalyDetectionConfiguration.NU_START_POW_LOW -= AnomalyDetectionConfiguration.NU_EXPAND_INCREMENT;
	    svmParameter.nu = allCrossValidate(svmProblem, svmParameter, nuValues, targetCrossTrainAccuracy, histogramsAnomaly, svmProblemAnomaly, 0.9);
	    expandTimes++;
	}

	System.out.println("YYY selected nu of " + svmParameter.nu);
	return svm.svm_train(svmProblem, svmParameter);
    }

    /**
     * For all entries in the nuValues TreeMap, if the value is negative, calculate the cross-validation accuracy
     * for nu equal to the TreeMap's key. Save the accuracy as the value in the TreeMap. If the value is not negative
     * we assume the accuracy has been previously calculated and we skip it. This allows us to expand the range of 
     * nu values we try if we decide to try additional values
     *
     * @param svmProblem precomputed svm_problem with the training data
     * @param svmParameter preset svm_parameter with the configuration parameters all set except for nu
     * @param nuValues a TreeMap of nu -> cross-validation accuracy
     * @param targetCrossTrainAccuracy The targetCrossTrainAccuracy accuracy. This function will return a nu that returns the closest accuracy to this or -1 if nuValues required no work
     *
     * @return a nu that generates the accuracy closest (absolute value) to the targetCrossTrainAccuracy parameter
     */
    private static double allCrossValidate(svm_problem svmProblem, svm_parameter svmParameter, TreeMap<Double, Double> nuValues, double targetCrossTrainAccuracy, ArrayList<Pair<Integer, GenericPoint<Integer>>> histogramsAnomaly, svm_problem svmProblemAnomaly, double targetAnomalyAccuracy) {
	double closestNUAccuracyDiff = Integer.MAX_VALUE;
	double closestNU = -1;

	for (Double nu : nuValues.keySet()) {
	    // if the value for this nu is non-negative, it means we've already calculated the accuracy so we can skip it
	    if (nuValues.get(nu) >= 0.0) {
		continue;
	    }
	    svmParameter.nu = nu;

	    String error_msg = svm.svm_check_parameter(svmProblem, svmParameter);
	    if (error_msg != null) {
		System.out.println("ERROR from parameter check " + error_msg);
	    }

	    double[] crossValidationResults = new double[svmProblem.l];
	    svm.svm_cross_validation(svmProblem, svmParameter, 4, crossValidationResults);

	    int total_correct = 0;
	    for (int i = 0; i < svmProblem.l; i++) {
			if (crossValidationResults[i] == svmProblem.y[i]) {
			    total_correct++;
			}
	    }

	    int totalCorrectAnomaly = -1;
	    if (histogramsAnomaly != null) {
			svm_model trainModel = svm.svm_train(svmProblem, svmParameter);
			totalCorrectAnomaly = 0;
			int index = 0;
			for (Pair<Integer, GenericPoint<Integer>> onePoint : histogramsAnomaly) {
			    double[] values = new double[1];
			    svm.svm_predict_values(trainModel, svmProblemAnomaly.x[index], values);
			    double prediction = values[0];
	
			    // this code returns a lower score for more anomalous so we flip it to match kdtree
			    prediction *= -1;
			    if (prediction >= 0) {
			    	totalCorrectAnomaly++;
			    }
			    index++;
			}
	    }

	    double accuracy = (1.0 * total_correct)/(1.0 * svmProblem.l);
	    System.out.print("YYY Cross Validation Accuracy = " + accuracy + " for nu " + nu + "\n");  

	    double accuracyAnomaly = -1;
	    if (totalCorrectAnomaly != -1) {
			accuracyAnomaly = (1.0 * totalCorrectAnomaly) / (1.0 * svmProblemAnomaly.l);
			System.out.print("YYY Cross Validation Accuracy for Anomaly = " + accuracyAnomaly + " for nu " + nu + "\n");  
	    }

	    // these two cases can eventually be collapsed into one case but I'm not sure where this nu calculation via anomaly will go in the fugure
	    // so I'm leaving it separate for now
	    if (totalCorrectAnomaly == -1) {
		// If our current best nu is at the edge of the range and the current nu is just as good but not on the edge, use it instead
		if ((closestNU == nuValues.lastKey() || closestNU == nuValues.firstKey()) &&
		    Math.abs(Math.abs(accuracy-targetCrossTrainAccuracy) - closestNUAccuracyDiff) < .000001 && nu != nuValues.lastKey() && nu != nuValues.firstKey()) {
		    closestNUAccuracyDiff = Math.abs(accuracy - targetCrossTrainAccuracy);
		    closestNU = nu;
		    System.out.println("YYY this is better because it is not on the range edge");
		}
		else if (Math.abs(accuracy - targetCrossTrainAccuracy) < closestNUAccuracyDiff) {
		    closestNUAccuracyDiff = Math.abs(accuracy - targetCrossTrainAccuracy);
		    closestNU = nu;
		    System.out.println("YYY this is closer to " + targetCrossTrainAccuracy + " with diff " + closestNUAccuracyDiff);
		}
		nuValues.put(nu, accuracy);
	    }
	    else {
		// If our current best nu is at the edge of the range and the current nu is just as good but not on the edge, use it instead
		if ((closestNU == nuValues.lastKey() || closestNU == nuValues.firstKey()) &&
		    Math.abs(Math.abs(accuracy-targetCrossTrainAccuracy) + Math.abs(accuracyAnomaly-targetAnomalyAccuracy) - closestNUAccuracyDiff) < .000001 && nu != nuValues.lastKey() && nu != nuValues.firstKey()) {
		    closestNUAccuracyDiff = Math.abs(accuracy - targetCrossTrainAccuracy) + Math.abs(accuracyAnomaly-targetAnomalyAccuracy);
		    closestNU = nu;
		    System.out.println("YYY this is better because it is not on the range edge");
		}
		else if (Math.abs(accuracy - targetCrossTrainAccuracy)  + Math.abs(accuracyAnomaly-targetAnomalyAccuracy) < closestNUAccuracyDiff) {
		    closestNUAccuracyDiff = Math.abs(accuracy - targetCrossTrainAccuracy) + Math.abs(accuracyAnomaly-targetAnomalyAccuracy);
		    closestNU = nu;
		    System.out.println("YYY this is closer to " + targetCrossTrainAccuracy + " with diff " + closestNUAccuracyDiff);
		}
		nuValues.put(nu, accuracy * accuracyAnomaly / 2);
	    }
	}

	return closestNU;
    }

    /**
     * @param histogramData Object containing the histograms
     * @param trainID ID of the model to use to train on
     * @param trainKey Key index for the training set histograms
     * @param testID ID of the model to use to test on
     * @param testKey Key index for the test set histograms
     * @param anomalyID ID for a dataset that we will consider as all anomalies when training or null
     * @param results If not null, every result will be recorded here as score->timestamp. We use a MultiValueMap so duplicate scores will still be recorded
     *
     * @return some text that can be displayed to the user
     */
    public static StringBuilder runOneTestSVM(HistogramStore histogramData, Integer trainID, GenericPoint<String> trainKey, GenericPoint<String> trainValue, Integer testID, GenericPoint<String> testKey, GenericPoint<String> testValue, Integer anomalyID, GenericPoint<String> anomalyKey, GenericPoint<String> anomalyValue, MultiValueMap results) {

	StringBuilder output = new StringBuilder();

    	svm_model svmModel = null;

	if (histogramData.isIDValid(trainID) == false) {
	    output.append("Error: trainID " + trainID + " not found");
	    return output;
	}
	if (histogramData.isValueValid(trainID, trainValue) == false) {
	    output.append("Error: trainValue " + trainValue + " not found");
	    return output;
	}
	if (histogramData.isCategoryValid(trainID, trainValue, trainKey) == false) {
	    output.append("Error: trainIP, trainApp pair of " + trainKey.toString() + " for trainID " + trainID + " not found");
	    return output;
	}
	if (histogramData.isIDValid(testID) == false) {
	    output.append("Error: testID " + testID + " not found");
	    return output;
	}
	if (histogramData.isValueValid(testID, testValue) == false) {
	    output.append("Error: testValue " + testValue + " not found");
	    return output;
	}
	if (histogramData.isCategoryValid(testID, testValue, testKey) == false) {
	    output.append("Error: testKey of " + testKey.toString() + " for testID " + testID + " not found");
	    return output;
	}
	if (anomalyID != null) {
	    if (histogramData.isIDValid(anomalyID) == false) {
		output.append("Error: anomalyID " + anomalyID + " not found");
		return output;
	    }
	    if (histogramData.isValueValid(anomalyID, anomalyValue) == false) {
		output.append("Error: anomalyValue " + anomalyValue + " not found");
		return output;
	    }
	    if (histogramData.isCategoryValid(anomalyID, anomalyValue, anomalyKey) == false) {
		output.append("Error: anomalyKey of " + anomalyKey.toString() + " for anomalyID " + anomalyID + " not found");
		return output;
	    }
	}

	ArrayList<Pair<Integer, GenericPoint<Integer>>> anomalyHistogram = null;
	if (anomalyID != null) {
	    anomalyHistogram = histogramData.getHistograms(anomalyID, anomalyValue, anomalyKey);
	}
	boolean changed = HistoTuple.upgradeWindowsDimensions(trainValue, histogramData.getHistograms(trainID, trainValue, trainKey), histogramData.getHistograms(testID, testValue, testKey), anomalyHistogram);


	if (changed) {
	    _svmModelsCache.remove(trainID);
	    _svmModelsCache.remove(testID);
	}

	if (_svmModelsCache.get(trainID) == null ||
	    _svmModelsCache.get(trainID).get(trainValue) == null ||
	    _svmModelsCache.get(trainID).get(trainValue).get(trainKey) == null) {

	    ArrayList<Pair<Integer, GenericPoint<Integer>>> anomalyData = null;
	    if (anomalyID != null) {
		anomalyData = histogramData.getHistograms(anomalyID, anomalyValue, anomalyKey);
	    }
	    svmModel = SVMCalc.generateModel(histogramData.getHistograms(trainID, trainValue, trainKey), .9, anomalyData, .9);

	    if (_svmModelsCache.get(trainID) == null) {
		_svmModelsCache.put(trainID, new HashMap<GenericPoint<String>, HashMap<GenericPoint<String>, svm_model>>());
	    }
	    if (_svmModelsCache.get(trainID).get(trainValue) == null) {
		_svmModelsCache.get(trainID).put(trainValue, new HashMap<GenericPoint<String>, svm_model>());
	    }
	    if (_svmModelsCache.get(trainID).get(trainValue).get(trainKey) == null) {
		_svmModelsCache.get(trainID).get(trainValue).put(trainKey, svmModel);
	    }
	}
	else {
	    svmModel = _svmModelsCache.get(trainID).get(trainValue).get(trainKey);
	    System.out.println("SVM Model cache hit");

	}

	// test the training set against itself to get a scaling factor
	double anomalyScale = histogramData.getScalingFactor(trainID, trainValue, trainKey);
	if (anomalyScale <= 1e-3) {
	    SVMKernel svmKernel = new SVMKernel(histogramData.getHistograms(trainID, trainValue, trainKey), histogramData.getHistograms(trainID, trainValue, trainKey), AnomalyDetectionConfiguration.SVM_KERNEL_TYPE, AnomalyDetectionConfiguration.SVM_TYPE_PRECOMPUTED_KERNEL_TYPE, AnomalyDetectionConfiguration.NUM_THREADS);
	    svm_node[][] bar = svmKernel.getData();

	    int index = 0;
	    anomalyScale = 0.0;
	    /* loop through the histograms to generate the predictions */
	    for (Pair<Integer, GenericPoint<Integer>> onePoint : histogramData.getHistograms(trainID, trainValue, trainKey)) {
		double[] values = new double[1];

		svm.svm_predict_values(svmModel, bar[index], values);
		double prediction = values[0];

		// this code returns a lower score for more anomalous so we flip it to match kdtree
		prediction *= -1;
		//		System.out.println("prediction is " + prediction);
		if (anomalyScale < prediction) {
		    anomalyScale = prediction;
		}
		index++;
	    }

	    // this can happen if the data is very simliar or there isn't a lot of it. If we do nothing all of the results end up as "Infinity"
	    if (anomalyScale <= 1e-3) {
	    	System.out.println("Calculated scaling factor of " + anomalyScale + " too small. Changing to 1.0.");
	    	anomalyScale = 1.0;
	    }

	    // the documentation for Pair doesn't say this but for some reason setAt0 doesn't overwrite the value, it returns a copy of the Pair with the new value
	    histogramData.setScalingFactor(trainID, trainValue, trainKey, anomalyScale);
	    System.out.println("Calculated scaling factor of " + anomalyScale);
	}
	else {
	    System.out.println("Using cached scaling factor of " + anomalyScale);
	}

	// If we're running many instances of similar test data against the same training data
	// we might want to implement a cache that's per-training set and save it externally
	// rather than the current scheme of only caching within an instance of SVMKernel
	SVMKernel svmKernel = new SVMKernel(histogramData.getHistograms(testID, testValue, testKey), histogramData.getHistograms(trainID, trainValue, trainKey), AnomalyDetectionConfiguration.SVM_KERNEL_TYPE, AnomalyDetectionConfiguration.SVM_TYPE_PRECOMPUTED_KERNEL_TYPE, AnomalyDetectionConfiguration.NUM_THREADS);
	svm_node[][] bar = svmKernel.getData();

	String anomalyString = "";
	if (testKey.getDimensions() > 0) {
	    anomalyString = testKey.getCoord(0).split(";")[1];
	    // this is of the form type;value and we just want the value
	    
	}

	Double[][] training_stats = null;
	Pair<Integer, Integer> train_times = histogramData.getStartAndEndTime(trainID);
	Pair<Integer, Integer> test_times = histogramData.getStartAndEndTime(testID);
	int index = 0;
	/* loop through the histograms to generate the predictions */
	for (Pair<Integer, GenericPoint<Integer>> onePoint : histogramData.getHistograms(testID, testValue, testKey)) {
	    double[] values = new double[1];

	    double d = svm.svm_predict_values(svmModel, bar[index], values);
	    double prediction = values[0];

	    // this code returns a lower score for more anomalous so we flip it to match kdtree
	    prediction *= -1;

	    prediction /= anomalyScale;


	    output.append(index + ": Anomaly score: " + prediction + " for data " + onePoint.getValue1().toString() + "\n");

	    if (results != null) {
		results.put(prediction, onePoint);
	    }
	    if (prediction > AnomalyDetectionConfiguration.SVM_UNSUPERVISED_THRESHOLD && AnomalyDetectionConfiguration.SVM_ENABLE_SUPERVISED_LEARNING == 0) {
		output.append("This seems suspicious, but Supervised Learning code disabled via config\n");
	    }
	    else if (prediction > AnomalyDetectionConfiguration.SVM_UNSUPERVISED_THRESHOLD) {
		output.append("This seems suspicious, so predicting the cause of this anomaly\n");

		ArrayList[] ret = AnomalyPrediction.predictAnomalyType(onePoint, null, output);
		
		DataIOWriteAnomaly writeAnomaly = new DataIOWriteAnomaly();
		int dim = onePoint.getValue1().getDimensions();
		Integer[] onePointToArray = new Integer[dim];
		for (int i = 0; i < dim; i++) {
		    onePointToArray[i] = onePoint.getValue1().getCoord(i);
		}

		Integer[] predictedStates = null;
		Integer[] predictedCauses = null;
		String[] predictedScore = null;

		ArrayList<Integer> predStateRet = ret[0];
		if (predStateRet.size() > 0) {
		    predictedStates = predStateRet.toArray(new Integer[predStateRet.size()]);
		}
		ArrayList<Integer> predCauseRet = ret[1];
		if (predCauseRet.size() > 0) {
		    predictedCauses = predCauseRet.toArray(new Integer[predCauseRet.size()]);
		}
		ArrayList<String> predScoreRet = ret[2];
		if (predScoreRet.size() > 0) {
		    predictedScore = predScoreRet.toArray(new String[predScoreRet.size()]);
		}

		ArrayList<Integer> pattern = new ArrayList<Integer>();
		// if we failed to make a prediction about the cause and status, try matching a pattern 
		
		if (training_stats == null) {
		    training_stats = histogramData.getHistogramStats(trainID, trainValue, trainKey);
		}
		if (predStateRet.size() == 0 && predCauseRet.size() == 0) {
		    pattern = AnomalyPrediction.patternAnomalyType(onePoint, training_stats[2], training_stats[3]);
		    output.append("pattern is " + pattern.toString());
		    
		}
		Integer[] pattern_arr = null;
		if (pattern.size() > 0) {
		    pattern_arr = pattern.toArray(new Integer[pattern.size()]);
		}

		String[] dimensionArray = HistoTuple.getDimensionNamesArray();
		output.append(writeAnomaly.writeAnomaly(new Long(test_times.getValue0()), new Long(test_times.getValue1()),
							new Long(train_times.getValue0()), new Long(train_times.getValue1()),
							1,anomalyString, 1, 
							"svm_chi_squared_1.0", prediction, pattern_arr,
							dimensionArray, training_stats[0],
							training_stats[1], training_stats[2],
							training_stats[3], HistoTuple.getDimensionNamesArray(),
							onePointToArray, predictedCauses,
							predictedStates, predictedScore));
		if (predictedCauses == null || predictedStates == null) {
		    output.append("\nNo predicted cause was made. This happens when there is not yet enough user feedback.\n\n");
		}
		
	    }
	    index++;
	}

	return output;
    }

    public static void removeModelFromCache(int id) {
	_svmModelsCache.remove(id);
    }
}
