/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.analysis;

import java.sql.Timestamp;

public class TimestampUtil {
	static public String getTimestampString(long timeInMillis) {
		Timestamp ts = new Timestamp(timeInMillis);
		String tsStr = ts.toString().substring(0,19)+"-0" + ts.getTimezoneOffset()/60 + "00";
		/*
		System.out.println("toGMTString = " + ts.toGMTString());
		System.out.println("toLocaleString = " + ts.toLocaleString());
		System.out.println("toString = " + ts.toString());
		System.out.println("timezoneOffSet = " + ts.getTimezoneOffset());
		System.out.println("returned string = " + tsStr);	
		*/	
		return tsStr;
	}
}
