/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.custom;

import com.google.gwt.user.client.ui.Composite;

public class WrapString  extends Composite {    
    String longString;

    public WrapString(String s) {
    	this.longString = s;
    }

	public String getLongString() {
		return longString;
	}

	public void setLongString(String longString) {
		this.longString = longString;
	}
}
