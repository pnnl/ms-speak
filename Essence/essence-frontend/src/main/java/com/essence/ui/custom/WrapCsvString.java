/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.custom;

import com.google.gwt.user.client.ui.Composite;

public class WrapCsvString extends Composite {    
    String commaDelimitedString;

    public WrapCsvString(String commaDelimitedString) {
    	this.commaDelimitedString = commaDelimitedString;
    }

	public String getCommaDelimitedString() {
		return commaDelimitedString;
	}

	public void setCommaDelimitedString(String commaDelimitedString) {
		this.commaDelimitedString = commaDelimitedString;
	}   
}