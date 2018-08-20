package org.autonlab.anomalydetection;

import com.savarese.spatial.*;
import java.util.*;
import java.util.concurrent.locks.*;
import libsvm.*;
import org.javatuples.*; //Tuples, Pair

public class SVMKernel implements Runnable {
    // Setting this to 1 could make things really slow
    // but it's useful to disable occasionally to see if
    // it produces similar results
    // Note that there is randomness in cross-validation
    // so it might not produce identical results every time
    static final int DISABLE_CACHE = 0;

    int _threadCount = 0;
    Thread[] _threadArray = null;
    int _svm_type;
    int _svm_type_precomputed_kernel_type;
    int _rowSize;

    // These are used by all related threads. Volatile variables are modified by threads
    ArrayList<Pair<Integer, GenericPoint<Integer>>> _histogramsA = null;
    ArrayList<Pair<Integer, GenericPoint<Integer>>> _histogramsB = null;
    volatile svm_node _retNode[][] = null;
    volatile Lock _retNodeLock = null;

    // cache a GenericPoint histogram to its pre-computed kernel as an Integer index into _retNode
    // The cost of the lookup is small compared to not having to compute the kernel. The number of
    // dimensions in a histogram for a lookup is small compared to the _histogramsB.size() kernel
    // computations required for a row
    volatile HashMap<GenericPoint<Integer>, Integer> _retNodeRowCache = null;

    /**
     * Convert an ArrayList of histograms into a matrix of svm_nodes that can be passed into the svm library
     * This is done in parallel. This library can also be instantiated multiple times in parallel
     *
     * From the libsvm documentation:
     * "Assume there are L training instances x1, ..., xL and. 
     * Let K(x, y) be the kernel
     * value of two instances x and y. The input formats are:
     *
     * New training instance for xi:
     *
     * <label> 0:i 1:K(xi,x1) ... L:K(xi,xL)"
     *
     * the L training instances are represented by histogramsB and the new instances are histogramsA.
     * In the calculation, the size of A will determine the number of rows and the size of B determines the number of columns
     *
     * @param histogramsA The ArrayList of histograms that we're applying the kernel to (the test set)
     * @param histogramsB The ArrayList of histograms for the training set (same as histogramsA when training, different when histogramsA is the test set)
     * @param threadCount The number of threads to use to perform the computation
     * @param svm_type The type of SVM to use. This is a value from the svm_parameter namespace
     * @param svm_type_precomputed_kernel_type If svm_type is svm_parameter.PRECOMPUTED, define our custom implemented type here, otherwise value is ignored
     * @param threadCount if svm_type is svm_parameter.PRECOMPUTED, use this many threads to apply kernel. Otherwise ignore value
     */
    public SVMKernel(ArrayList<Pair<Integer, GenericPoint<Integer>>> histogramsA, ArrayList<Pair<Integer, GenericPoint<Integer>>> histogramsB, int svm_type, int svm_type_precomputed_kernel_type, int threadCount) {
	_threadCount = threadCount;
	_threadArray = new Thread[_threadCount];
	_histogramsA = histogramsA;
	_histogramsB = histogramsB;
	_retNode = new svm_node[histogramsA.size()][];
	_svm_type = svm_type;
	_svm_type_precomputed_kernel_type = svm_type_precomputed_kernel_type;
	
	// the PRECOMPUTED format requires an initial node per row that looks like (0:index)
	if (_svm_type == svm_parameter.PRECOMPUTED) {
	    _rowSize = _histogramsB.size() + 1;
	}
	else {
	    _rowSize = _histogramsB.get(0).getValue1().getDimensions();
	}

	_retNodeRowCache = new HashMap();

	/* 
	 * for non-precomputed kernels, we're just copying the data
	 * without processing it so don't incur the overhead of
	 * spawning too many threads. To simplify the code we will
	 * spawn one thread rather than special casing it and doing
	 * the work here
	 */
	if (_svm_type != svm_parameter.PRECOMPUTED) {
	    _threadCount = 1;
	}

	for (svm_node[] svmNodeArr : _retNode) {
	    svmNodeArr = null;
	}
	_retNodeLock = new ReentrantLock();

	for (int i = 0; i < _threadCount; i++) {
	    _threadArray[i] = new Thread(new SVMKernel(_retNodeLock, _retNode, _svm_type, _svm_type_precomputed_kernel_type, _histogramsA, _histogramsB, _rowSize, _retNodeRowCache));
	    _threadArray[i].start();
	}   
    }

    public SVMKernel(Lock retNodeLock, svm_node[][] retNode, int svm_type, int svm_type_precomputed_kernel_type, ArrayList<Pair<Integer, GenericPoint<Integer>>> histogramsA, ArrayList<Pair<Integer, GenericPoint<Integer>>> histogramsB, int rowSize, HashMap<GenericPoint<Integer>, Integer> rowCache) {
	_retNodeLock = retNodeLock;
	_retNode = retNode;
	_histogramsA = histogramsA;
	_histogramsB = histogramsB;
	_svm_type = svm_type;
	_svm_type_precomputed_kernel_type = svm_type_precomputed_kernel_type;
	_rowSize = rowSize;
	_retNodeRowCache = rowCache;
    }

    /**
     * If we selected svm_parameter.PRECOMPUTED, we apply the kernel and reformat the data so it is N+1xN
     * otherwise we simply reformat the data to D+1xN so that libsvm can handle it
     * (D = number of dimensions of each histogram, N = number of histograms)
     */
    public void run() {
	int index = 0;
	int cache_hit = 0;
	int cache_work = 0;
	/* 
	 * _retNode contains the processed data so we synchronize on
	 *  that.  The rows of _retNode represent the processed output
	 *  of the _histograms at the same index. Any row that is null
	 *  has yet to be processed
	 */
	while (index < _histogramsA.size()) {
	    GenericPoint<Integer> oneHist = null;

	    // look for the first unprocessed output row or decide that we're done
	    _retNodeLock.lock();
	    while (index < _histogramsA.size() && _retNode[index] != null) {
		index++;
	    }
	    if (index < _histogramsA.size() && _retNode[index] == null) {
		oneHist = _histogramsA.get(index).getValue1();
		if (_svm_type == svm_parameter.PRECOMPUTED) {
		    Integer cacheIndex = _retNodeRowCache.get(oneHist);
		    if (cacheIndex != null) {
			cache_hit++;
			_retNode[index] = _retNode[cacheIndex].clone();

			// modify the first column since it is row-specific
			_retNode[index][0].index = 0;
			_retNode[index][0].value = index + 1; // +1 because these start at 1 instead of 0	

			_retNodeLock.unlock();
			continue;
		    }
		    else {
			_retNode[index] = new svm_node[_rowSize];
		    }
		}
		else {
		    _retNode[index] = new svm_node[_rowSize];
		}
	    }
	    // even though we haven't done the work we can unlock here. Once we set _retNode[index] to something
	    // other than null, no other threads will try to use that 
	    _retNodeLock.unlock();

	    if (index >= _histogramsA.size()) {
		break;
	    }

	    if (_svm_type == svm_parameter.PRECOMPUTED) {
		// the PRECOMPUTED format requires an initial node per row that looks like (0:index)
		 _retNode[index][0] = new svm_node();
		 _retNode[index][0].index = 0;
		 _retNode[index][0].value = index + 1; // +1 because these start at 1 instead of 0
		 for (int j = 0; j < _histogramsB.size(); j++) {
		     _retNode[index][j+1] = new svm_node();
		     _retNode[index][j+1].index = j+1;
		     if (_svm_type_precomputed_kernel_type == AnomalyDetectionConfiguration.SVM_PRECOMPUTED_KERNEL_TYPE_CHI_SQUARED) {
			 _retNode[index][j+1].value = this.chiSquaredKernel(oneHist, _histogramsB.get(j).getValue1());
		     }
		     else if (_svm_type_precomputed_kernel_type == AnomalyDetectionConfiguration.SVM_PRECOMPUTED_KERNEL_TYPE_LINEAR) {
			 _retNode[index][j+1].value = this.linearKernel(oneHist, _histogramsB.get(j).getValue1());
		     }
		     else {
			 throw new RuntimeException("SVM Kernel type '" + _svm_type_precomputed_kernel_type + "' not defined!");
		     }
		 }

		 if (DISABLE_CACHE == 0) {
		     _retNodeLock.lock();
		     // check if the cache contains this key since a different thread could have put it in there
		     if (!_retNodeRowCache.containsKey(oneHist)) {
			 _retNodeRowCache.put(oneHist, index);
		     }
		     _retNodeLock.unlock();
		 }

		 cache_work++;
	    }
	    else {
		for (int j = 0; j < oneHist.getDimensions(); j++) {
		    _retNode[index][j] = new svm_node();
		    _retNode[index][j].index = j+1;
		    _retNode[index][j].value = oneHist.getCoord(j);
		}
	    }

	    index++;
	}

	if (_svm_type == svm_parameter.PRECOMPUTED) {
	    System.out.println("Cache stats: hit: " + cache_hit + " work: " + cache_work);
	}
    }

    /**
     * Wait for all threads to finish then return the data
     *
     * @return the svm_node matrix representing the kernel-processed histograms
     */
    public svm_node[][] getData() {
	int i;
	for (i = 0; i < _threadCount; i++) {
	    try {
		_threadArray[i].join();
	    } catch (InterruptedException e) {
		e.printStackTrace();
	    }
	}

	return _retNode;
    }

    /**
     * Calculate the kernel between two histograms histX and histY
     * See Chi-Square Kernel here: http://crsouza.blogspot.com/2010/03/kernel-functions-for-machine-learning.html
     *
     * @param histX the first histogram
     * @param histY the second histogram
     *
     * @return the kernel value of two histograms x and y
     */
    public double chiSquaredKernel(GenericPoint<Integer> histX, GenericPoint<Integer> histY) {
	double res = 0.0;

	for (int i = 0; i < histX.getDimensions(); i++) {
	    // if histX.getCoord(i) and histY.getCoord(i)) are both zero, we get zero in the denominator so we just skip that one
	    if ((histX.getCoord(i) + histY.getCoord(i)) != 0.0) {
		res += Math.pow(histX.getCoord(i) - histY.getCoord(i), 2) / (.5 * (histX.getCoord(i) + histY.getCoord(i)));
	    }
	}
	res = 1.0 - res;
	return res;
    }

    /**
     * Calculate the kernel between two histograms histX and histY
     * See linear Kernel here: http://crsouza.blogspot.com/2010/03/kernel-functions-for-machine-learning.html
     *
     * This is implemented for debugging purposes since the svmlib already has a LINEAR option
     *
     * @param histX the first histogram
     * @param histY the second histogram
     *
     * @return the kernel value of two histograms x and y
     */
    public double linearKernel(GenericPoint<Integer> histX, GenericPoint<Integer> histY) {
	double res = 0.0;

	for (int i = 0; i < histX.getDimensions(); i++) {
	    res += histX.getCoord(i) * histY.getCoord(i);
	}
	return res;
    }
}
