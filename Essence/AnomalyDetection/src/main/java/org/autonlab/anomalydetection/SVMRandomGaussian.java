package org.autonlab.anomalydetection;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

import libsvm.svm_node;

import org.javatuples.Pair; //Tuples, Pair
import org.apache.commons.math3.distribution.MultivariateNormalDistribution;
import org.apache.commons.math3.distribution.UniformRealDistribution;

import com.savarese.spatial.GenericPoint;


/**
 * @author sibiv
 * 
 * This class is for creating random Gaussian Fourier Features to approximate the RBF Kernel.
 * Given a list of histograms, this returns a list of svm_nodes which have been randomly created.
 * Eventually, a linear SVM will be used given these features. 
 *
 */
public class SVMRandomGaussian implements Runnable {
	// Setting this to 1 could make things really slow
	// but it's useful to disable occasionally to see if
	// it produces similar results
	// Note that there is randomness in cross-validation
	// so it might not produce identical results every time
	static final int DISABLE_CACHE = 0;

	int _threadCount = 0;
	Thread[] _threadArray = null;

	// These are used by all related threads. Volatile variables are modified by threads
	ArrayList<Pair<Integer, GenericPoint<Integer>>> _histograms = null;
	// ArrayList<Pair<Double, GenericPoint<Integer>>> _histograms2 = null; // 

	int _n = 0; // The length of histogram element
	int _D = 0; // The number of random features 
	boolean _sine = true; // if true, use cos+sine instead of cos+unif 
	volatile svm_node _retNode[][] = null;
	volatile Lock _retNodeLock = null;
	
	GaussianRandomFeatures _gff;

	// cache a GenericPoint histogram to its pre-computed feature map as an Integer index into _retNode
	// We want to ensure that each histogram gets mapped to the same feature vector -- I think.
	volatile HashMap<GenericPoint<Integer>, Integer> _retNodeRowCache = null;

	/**
	 * Convert an ArrayList of histograms into a matrix of svm_nodes that can be passed into the svm library
	 * This is done in parallel. This library can also be instantiated multiple times in parallel
	 *
	 * @param histograms The ArrayList of histograms that we're 
	 * @param threadCount The number of threads to use to perform the computation
	 * @param D The number of random fourier features
	 * @param sigmak A measure of the bandwidth of the RBF kernel; gammak = 1/(2*sigmak^2)
	 * @param 
	 * @param threadCount if svm_type is svm_parameter.PRECOMPUTED, use this many threads to apply kernel. Otherwise ignore value
	 */
	public SVMRandomGaussian(ArrayList<Pair<Integer, GenericPoint<Integer>>> histograms, int D, 
							 double gammak, boolean sine, int threadCount) {
		_threadCount = threadCount;
		_threadArray = new Thread[_threadCount];
		_histograms = histograms;
		_D = D;
		_sine = sine;
		_n = _histograms.get(0).getValue1().getDimensions();
		_retNode = new svm_node[histograms.size()][];
		_retNodeRowCache = new HashMap<GenericPoint<Integer>,Integer>();
		
		_gff = new GaussianRandomFeatures(_D, _n, gammak, sine);
		if (_sine) _D *= 2;
		
		for (svm_node[] svmNodeArr : _retNode)
			svmNodeArr = null;

		_retNodeLock = new ReentrantLock();

		for (int i = 0; i < _threadCount; i++) {
			_threadArray[i] = new Thread(new SVMRandomGaussian(_retNodeLock, _retNode, _histograms, _retNodeRowCache, _D, _n, _gff));
			_threadArray[i].start();
		}   
	}

	public SVMRandomGaussian(ArrayList<Pair<Integer, GenericPoint<Integer>>> histograms, int D, 
							 GaussianRandomFeatures gff, int threadCount) {
		_threadCount = threadCount;
		_threadArray = new Thread[_threadCount];
		_histograms = histograms;
		_D = D;
		_n = _histograms.get(0).getValue1().getDimensions();
		_retNode = new svm_node[histograms.size()][];
		_retNodeRowCache = new HashMap<GenericPoint<Integer>,Integer>();
		_gff = gff;

		for (svm_node[] svmNodeArr : _retNode)
			svmNodeArr = null;

		_retNodeLock = new ReentrantLock();

		for (int i = 0; i < _threadCount; i++) {
			_threadArray[i] = new Thread(new SVMRandomGaussian(_retNodeLock, _retNode, _histograms, _retNodeRowCache, _D, _n, _gff));
			_threadArray[i].start();
		}   
	}


	public SVMRandomGaussian(Lock retNodeLock, svm_node[][] retNode, ArrayList<Pair<Integer, 
								   GenericPoint<Integer>>> histograms, HashMap<GenericPoint<Integer>, Integer> rowCache,
								   int D, int n, GaussianRandomFeatures  gff) {
		_retNodeLock = retNodeLock;
		_retNode = retNode;
		_histograms = histograms;
		_retNodeRowCache = rowCache;
		_D = D;
		_n = n;
		_gff = gff;
	}

	/**
	 * ??? otherwise we simply reformat the data to D+1xN so that libsvm can handle it
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
		while (index < _histograms.size()) {
			GenericPoint<Integer> oneHist = null;
			// look for the first unprocessed output row or decide that we're done
			_retNodeLock.lock();
			while (index < _histograms.size() && _retNode[index] != null)
				index++;
			
			if (index < _histograms.size() && _retNode[index] == null) {
				oneHist = _histograms.get(index).getValue1();

				Integer cacheIndex = _retNodeRowCache.get(oneHist);
				if (cacheIndex != null) {
					cache_hit++;
					// We've already computed this feature vector before
					_retNode[index] = _retNode[cacheIndex].clone();  

					_retNodeLock.unlock();
					continue;
				}

			}
			_retNodeLock.unlock();

			if (index >= _histograms.size())
				break;
			
			_retNode[index] = _gff.computeGaussianFourierFeatures_SVM(oneHist);

			index++;
		}

		System.out.println("Cache stats: hit: " + cache_hit + " work: " + cache_work);
	}

	// So that other Randomized SVMs can use the same features.
	public GaussianRandomFeatures getRandomFeatures () {
		return _gff;
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


}
