/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.shared;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

import com.essence.model.SeverityType;

public class StringUtil {

	static public void main(String[] args) {
		String msgType="myOperationResponse";
		System.out.println(msgType.substring(0, msgType.length()-8));
		//testDateParsing();
	}

	@SuppressWarnings("unused")
    private static void testDateParsing() {
		/*
		DatatypeConverter dtc;
		SimpleDateFormat df  = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ssz");
		SimpleDateFormat df1 = new SimpleDateFormat("yyyy-MM-dd");
		SimpleDateFormat df2 = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss");
		*/
		/*
		Date d1 = df1.parse("2014-07-12");
		System.out.println("d1=" + d1.toString());
		Date d2 = df1.parse("2014-07-12Z");
		System.out.println("d2=" + d2.toString());
		Date d3 = df1.parse("2014-07-12+05:00");
		System.out.println("d3=" + d3.toString());
		Date d4 = df1.parse("2014-07-12-05:00");
		System.out.println("d4=" + d4.toString());
		Date d5 = df2.parse("2014-07-12T12:11:59");
		System.out.println("d5=" + d5.toString());
		Date d6 = df2.parse("2014-07-12T12:11:59Z");
		System.out.println("d6=" + d6.toString());
		Date d7 = df2.parse("2014-07-12T12:11:59+05:00");
		System.out.println("d7=" + d7.toString());
		Date d8 = df2.parse("2014-07-12T12:11:59-05:00");
		System.out.println("d8=" + d8.toString());
		Date d9 = df.parse("2014-07-12T12:11:59+05:00");
		System.out.println("d9=" + d9.toString());
		Date d10 = df.parse("2014-07-12T12:11:59-05:00");
		System.out.println("d10=" + d10.toString());
		*/
		/*
		Calendar c = DatatypeConverter.parseDateTime("2014-07-12");
		System.out.println("1=" + c.getTime());
c = DatatypeConverter.parseDateTime("2014-07-12Z");
		System.out.println("2=" + c.getTime());
c = DatatypeConverter.parseDateTime("2014-07-12+05:00");
		System.out.println("3="+c.getTime());
		c = DatatypeConverter.parseDateTime("2014-07-12-05:00");
		System.out.println("4="+c.getTime());
		c = DatatypeConverter.parseDateTime("2014-07-12T12:11:59");
		System.out.println("5="+c.getTime());
		c = DatatypeConverter.parseDateTime("2014-07-12T12:11:59Z");
		System.out.println("6="+c.getTime());
		c = DatatypeConverter.parseDateTime("2014-07-12T12:11:59+05:00");
		System.out.println("7="+c.getTime());
		c = DatatypeConverter.parseDateTime("2014-07-12T12:11:59-05:00");
		System.out.println("8="+c.getTime());		
		*/
		/*
		 * date	Defines a date value YYYY-MM-DD{Z, +hh:00, -hh:00}
dateTime	Defines a date and time value YYYY-MM-DDThh:mm:ss{Z, +hh:00, -hh:00}
duration	Defines a time interval	PnYnMnDTnHnMnS
		 */
	}
	
	@SuppressWarnings("unused")
    private static void test() {
		String detailXpathValue = "1345|/Envelope/Body/test/fieldname";
		String[] xpathValueComponnets = detailXpathValue.split("\\|");
		Integer xpathId = StringUtil.textToInteger(xpathValueComponnets[0]);
		System.out.println("xpathValueComponnets length="+xpathValueComponnets.length+" xpathId="+xpathId);
	}
	
	@SuppressWarnings("unused")
    private static void testEnum() {
		System.out.println("High = " + SeverityType.valueOf("HIGH"));
		//System.out.println("null = " + SeverityType.valueOf(null)); // Exception in thread "main" java.lang.NullPointerException: Name is null
		//System.out.println("invalid = " + SeverityType.valueOf("invalid")); // Exception in thread "main" java.lang.IllegalArgumentException: No enum const class com.essence.ui.client.SeverityType.invalid
		
		SeverityType t = null;
		try {
			t = SeverityType.valueOf("invalid");			
		} catch (Exception ex) {
			System.out.println(ex.getMessage());
		}
		System.out.println("t = " + t);		
	}
	
	@SuppressWarnings("unused")
    private static void testEmptyList() {
		List<String> l1 = null, l2 = new ArrayList<String>();
		/*
		System.out.println("Print null list");
		for (String s : l1) // Exception in thread "main" java.lang.NullPointerException
			System.out.println("s=" + s);
			*/
		System.out.println("Print empty list");
		for (String s : l2)
			System.out.println("s=" + s);
	}
	
	/*
	static public String millisTimeToDateString(Long t) {
		if (t == null)
			return "";
		return DateFormat.getDateTimeInstance(DateFormat.SHORT, DateFormat.LONG).format(new Date(t));
	}
	*/
	
	public static final String FIELD_NAME_SEPARATOR = "  -  ";
	
	static public String reverseXpath(String xpath) {
		if (xpath == null || xpath.isEmpty())
			return xpath;
		
		String[] parts = xpath.split("/");
		StringBuffer sb = new StringBuffer();
		for (int i = parts.length-1; i>=0; i--) {
			if (parts[i].isEmpty())
				continue;

			sb.append(parts[i]);
			
			if ((parts.length > 1) && (i == parts.length - 1))
				sb.append(FIELD_NAME_SEPARATOR);
			else if (i > 0 && !parts[i-1].isEmpty())
				sb.append("-");
		}
		return sb.toString();
	}

	public static String getElementNameFromXpath(String xpath) {
		if (xpath == null || xpath.isEmpty())
			return null;
		int idx = xpath.lastIndexOf("/");
		return xpath.substring(idx+1);
	}
	
	/**
	 * Check to see if a String contains non-empty value
	 * 
	 * @param s
	 * @return
	 */
	static public boolean stringHasValue(String s) {
		if (s == null || s.isEmpty())
			return false;
		
		return true;
	}
	
	/**
	 * Remove the name space from a node name, for example, tns:nodeName1 will return nodeName1
	 * @param nodeName
	 * @return
	 */
	static public String removeNamespace(String nodeName) {
		if (nodeName != null && nodeName.indexOf(":")>-1)
			return nodeName.substring(nodeName.indexOf(":")+1);
		else
			return nodeName;
	}
	
	static public Integer textToInteger(String text) {
		if (text == null || text.isEmpty())
			return null;
		try {
			return Integer.valueOf(text);
		} catch (NumberFormatException ex) {
			return null;
		}
	}

	static public Double textToDouble(String text) {
		if (text == null || text.isEmpty())
			return null;
		try {
			return Double.valueOf(text);
		} catch (NumberFormatException ex) {
			return null;
		}
	}

	static public Long textToLong(String text) {
		if (text == null || text.isEmpty())
			return null;
		try {
			return Long.valueOf(text);
		} catch (NumberFormatException ex) {
			return null;
		}
	}
	
	static public String combineEndpointCodes (Set<String> cds) {
		if (cds == null || cds.isEmpty())
			return null;
		
		StringBuffer sb = new StringBuffer();
		boolean isFirst = true;
		for (String cd: cds) {
			if (isFirst) {
				isFirst = false;
			} else
				sb.append(", ");

			sb.append(cd);
		}
		
		return sb.toString();
	}

	static public String combineVersion(String key, String version) {
		if (key == null || version == null)
			return key;
		return key+"-"+version;
	}
	

}
