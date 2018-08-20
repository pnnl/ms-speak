package org.autonlab.anomalydetection;

import org.apache.commons.math3.distribution.MultivariateNormalDistribution;
import org.apache.commons.math3.distribution.UniformRealDistribution;
import com.savarese.spatial.GenericPoint;
import libsvm.svm_node;

public class GaussianRandomFeatures {

	int _D;
	int _n;

	// Mean and covariance of Gaussian distribution
	double[] _mu;
	double[][] _cov;
	double _gammak;
	MultivariateNormalDistribution _mnd;
	// Our w vectors in order to generate the random features 
	double[][] _ws; 
	
	// Uniform distribution
	double _lb;
	double _ub;
	UniformRealDistribution _urd;
	// Our w vectors in order to generate the random features
	double[] _bs;
	
	boolean _sine;

	public GaussianRandomFeatures(int D, int n, double gammak, boolean sine) {
		_D = D;
		_n = n;
		_gammak = gammak;
		_sine = sine;
		
		// Initialize mnd
		// The value for the variances are taken from: http://www.eecs.berkeley.edu/~brecht/papers/07.rah.rec.nips.pdf
		_cov = new double[_n][_n];
		_mu = new double[_n];
		for(int i = 0; i < _n; i++) {
			_mu[i] = 0;
			for(int j = 0; j < _n; j++)
				_cov[i][j] = (i == j) ? 2*_gammak : 0;
		}
		_mnd = new MultivariateNormalDistribution(_mu, _cov);
		_ws = new double[_D][];
		for (int i = 0; i < _D; i ++)
			_ws[i] = _mnd.sample();
		
		// Initialize urd
		_lb = 0;
		_ub = 2*Math.PI;
		_urd = new UniformRealDistribution (_lb, _ub);
		_bs = new double[_D];
		for (int i = 0; i < _D; i ++)
			_bs[i] = _urd.sample();
	}
	
	/**
	 * Generate the random Fourier features to approximate the Gaussian Kernel
	 * For approximating with low-dim features: http://www.eecs.berkeley.edu/~brecht/papers/07.rah.rec.nips.pdf
	 *
	 * Assuming the Gaussian kernel has gamma=1.
	 *
	 * @param hist the histogram
	 * 
	 * @return the feature array f = sqrt(2/D)*[cos(w_1 T x + b_1) ... cos(w_D T x + b_D)]  
	 */
	// TODO: Make them into matrix operations perhaps. This could make them faster.
	public double[] computeGaussianFourierFeatures(GenericPoint<Integer> hist) {

		if (_sine) {
			double[] f = new double[2*_D];
			
			for (int i = 0; i < _D; i++) {
				double[] w = _ws[i];
	
				double t = 0.0;	// t = wTx	
				for (int j = 0; j < _n; j++)
					t += hist.getCoord(j)*w[j];
				
				f[i] = Math.cos(t)*Math.sqrt(1.0/_D);
				f[_D+i] = Math.sin(t)*Math.sqrt(1.0/_D);
			}
			return f;
		} else {
			double[] f = new double[_D];
			
			for (int i = 0; i < _D; i++) {
				double[] w = _ws[i];
				double b = _bs[i];
	
				double t = 0.0;	// t = wTx	
				for (int j = 0; j < _n; j++)
					t += hist.getCoord(j)*w[j];
				
				f[i] = Math.cos(t + b)*Math.sqrt(2.0/_D);
			}
			return f;
		}
	}

	public double[] computeGaussianFourierFeatures(double[] hist) {

		if (_sine) {
			double[] f = new double[2*_D];
			
			for (int i = 0; i < _D; i++) {
				double[] w = _ws[i];
	
				double t = 0.0;	// t = wTx	
				for (int j = 0; j < _n; j++)
					t += hist[j]*w[j];
				
				f[i] = Math.cos(t)*Math.sqrt(1.0/_D);
				f[_D+i] = Math.sin(t)*Math.sqrt(1.0/_D);
			}
			return f;
		} else {
			double[] f = new double[_D];
			
			for (int i = 0; i < _D; i++) {
				double[] w = _ws[i];
				double b = _bs[i];
	
				double t = 0.0;	// t = wTx	
				for (int j = 0; j < _n; j++)
					t += hist[j]*w[j];
				
				f[i] = Math.cos(t + b)*Math.sqrt(2.0/_D);
			}
			return f;
		}
	}
	
	public svm_node[] computeGaussianFourierFeatures_SVM(GenericPoint<Integer> hist) {

		if (_sine) {
			svm_node[] f = new svm_node[2*_D];
			
			for (int i = 0; i < _D; i++) {
				double[] w = _ws[i];
	
				double t = 0.0;	// t = wTx	
				for (int j = 0; j < _n; j++)
					t += hist.getCoord(j)*w[j];
				
				f[i] = new svm_node();
				f[i].index = i+1;
				f[i].value = Math.cos(t)*Math.sqrt(1.0/_D);
				
				f[_D+i] = new svm_node();
				f[_D+i].index = _D+i+1;
				f[_D+i].value = Math.sin(t)*Math.sqrt(1.0/_D);
			}
			return f;
		} else {
			svm_node[] f = new svm_node[_D];
			
			for (int i = 0; i < _D; i++) {
				double[] w = _ws[i];
				double b = _bs[i];
	
				double t = 0.0;	// t = wTx	
				for (int j = 0; j < _n; j++)
					t += hist.getCoord(j)*w[j];
				
				f[i] = new svm_node();
				f[i].index = i+1;
				f[i].value = Math.cos(t + b)*Math.sqrt(2.0/_D);
			}
			return f;
		}
	}

	public svm_node[] computeGaussianFourierFeatures_SVM(double[] hist) {

		if (_sine) {
			svm_node[] f = new svm_node[2*_D];
			
			for (int i = 0; i < _D; i++) {
				double[] w = _ws[i];
	
				double t = 0.0;	// t = wTx	
				for (int j = 0; j < _n; j++)
					t += hist[j]*w[j];
				
				f[i] = new svm_node();
				f[i].index = i+1;
				f[i].value = Math.cos(t)*Math.sqrt(1.0/_D);
				
				f[_D+i] = new svm_node();
				f[_D+i].index = _D+i+1;
				f[_D+i].value = Math.sin(t)*Math.sqrt(1.0/_D);
			}
			return f;
		} else {
			svm_node[] f = new svm_node[_D];
			
			for (int i = 0; i < _D; i++) {
				double[] w = _ws[i];
				double b = _bs[i];
	
				double t = 0.0;	// t = wTx	
				for (int j = 0; j < _n; j++)
					t += hist[j]*w[j];

				f[i] = new svm_node();
				f[i].index = i+1;
				f[i].value = Math.cos(t + b)*Math.sqrt(2.0/_D);
			}
			return f;
		}
	}
	
	/**
	 * Calculate the kernel between two histograms histX and histY
	 * See gaussian (RBF) Kernel here: http://crsouza.blogspot.com/2010/03/kernel-functions-for-machine-learning.html
	 *
	 * This is implemented for debugging purposes since the svmlib already has an RBF option
	 *
	 * @param histX the first histogram
	 * @param histY the second histogram
	 *
	 * @return the kernel value of two histograms x and y
	 */
	public double gaussianKernel(GenericPoint<Integer> histX, GenericPoint<Integer> histY) {
		double res = 0.0;

		for (int i = 0; i < histX.getDimensions(); i++) {
			res += Math.pow(histX.getCoord(i) - histY.getCoord(i), 2);
		}
		return Math.exp(-_gammak*res);
	}
	
	public double gaussianKernel(double[] histX, double[] histY) {
		double res = 0.0;

		for (int i = 0; i < histX.length; i++) {
			res += Math.pow(histX[i] - histY[i], 2);
		}
		return Math.exp(-_gammak*res);
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
	
	public double linearKernel(double[] histX, double[] histY) {
		double res = 0.0;

		for (int i = 0; i < histX.length; i++) {
			res += histX[i] * histY[i];
		}
		return res;
	}

}