package org.autonlab.anomalydetection;

import libsvm.*;

public class QuietPrint implements svm_print_interface{
	
	// Just to quiet down printing.
	public void print (String s) {}

}
