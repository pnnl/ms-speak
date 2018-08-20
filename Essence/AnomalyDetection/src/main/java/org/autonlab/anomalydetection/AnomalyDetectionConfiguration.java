package org.autonlab.anomalydetection;

import libsvm.*;

public class AnomalyDetectionConfiguration {

    // number of CPU threads to use when doing parallel computation
    static int NUM_THREADS = 2;

    // The width of time in which we count datapoints - can be changed via REST call
    static int SAMPLE_WINDOW_SECS = 1800;
    // The number of seconds that we slide the SAMPLE_WINDOW_SECS for the next datapoint - can be changed via REST call
    static int SLIDE_WINDOW_SECS = 300;

    // 0 = off, >0 = on
    static int SVM_ENABLE_SUPERVISED_LEARNING = 1;
    static double SVM_UNSUPERVISED_THRESHOLD = 1.0;

    static final int CALC_TYPE_KDTREE = 0;
    static final int CALC_TYPE_SVM = 1;
    static final int CALC_TYPE_SVM_RANDOM = 2;
    static final String[] CALC_TYPE_NAMES = {"KDTree", "SVM", "SVMRandom"}; // the index into this array's names should line up with the CALC_TYPE_<type> ints

    static int CALC_TYPE_TO_USE = CALC_TYPE_KDTREE;

    static final int NU_START_POW_HIGH = -1;
    static int NU_START_POW_LOW = -5;
    static final int[] NU_BASE_LIST = {1, 3};
    static final int NU_EXPAND_INCREMENT = 3; // if we pick a nu that is the highest or lowest in the test range, we expand the range in that direction and check again
    // It runs out we can't expand in the _HIGH direction because libsvm requires nu to be < 1 (and also >= 0)

    static final int SVM_CACHE_SIZE = 28000;
    static final double SVM_EPS = .001; // README says "eps is the stopping criterion. (we usually use 0.00001 in nu-SVC, 0.001 in others)"
    static final double SVM_GAMMA = 0.02; // For the RBF Kernel, we need the additional gamma = 1/(2*variance) factor. Variance = 5.0
    static final int SVM_D = 10000;//Number of random Fourier features 
    static final boolean RFF_SINE = true; //parameter determining whether to use cos+unif or cos+sine.

    static final int SVM_PRECOMPUTED_KERNEL_TYPE_NONE = 0;
    static final int SVM_PRECOMPUTED_KERNEL_TYPE_CHI_SQUARED = 1;
    static final int SVM_PRECOMPUTED_KERNEL_TYPE_LINEAR = 2;
    static final int SVM_PRECOMPUTED_KERNEL_TYPE_RBF = 3;

    static final int SVM_TYPE_PRECOMPUTED_KERNEL_TYPE = SVM_PRECOMPUTED_KERNEL_TYPE_CHI_SQUARED;
    //static final int SVM_TYPE_PRECOMPUTED_KERNEL_TYPE = SVM_PRECOMPUTED_KERNEL_TYPE_LINEAR;

    static final int SVM_RANDOM_KERNEL_TYPE = svm_parameter.LINEAR;
    static final int SVM_KERNEL_TYPE = svm_parameter.PRECOMPUTED;
    //static final int SVM_KERNEL_TYPE = svm_parameter.RBF;
    //static final int SVM_KERNEL_TYPE = svm_parameter.LINEAR;

    public static String printCalcTypeNameLinksHTML(String prefix) {
	String output = "<br><br>Set new calc type:<ul>\n";
	for (String oneName : CALC_TYPE_NAMES) {
	    output += "<li><a href='" + prefix + oneName + "'>" + oneName + "</a></li>\n";
	}
	output += "</ul>\n";
	return output;
    }

    static String ANOMALY_REST_URL_PREFIX = "http://54.210.142.233/essence-services";

    static final int ANOMALY_FILTER_TYPE_IP_ADDRESS = 1;
    static final int ANOMALY_FILTER_TYPE_MESSAGE_TYPE = 2;
}
