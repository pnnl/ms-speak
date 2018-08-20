/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.shared;

import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import com.essence.multispeak.MSPServiceOperationKey;

public class Validator {
    private static final String IPADDRESS_PATTERN = 
		"^([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\." +
		"([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\." +
		"([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\." +
		"([01]?\\d\\d?|2[0-4]\\d|25[0-5])$";
 
    private static Pattern ipaddressPattern = Pattern.compile(IPADDRESS_PATTERN);
 
   /**
    * Validate ip address with regular expression
    * @param ip ip address for validation
    * @return true valid ip address, false invalid ip address
    */
    public static boolean validateIPAddress(final String ip){		  
        Matcher matcher = ipaddressPattern.matcher(ip);
	    return matcher.matches();	    	    
    }
    
    public static boolean validateIPAddresses(final List<String> ips){
    	if (ips == null || ips.isEmpty())
    		return true;
    	
    	for (String ip: ips) {
    		Matcher matcher = ipaddressPattern.matcher(ip);
    		if (matcher.matches())
    			continue;
    		else
    			return false; // fail at the first one
    	}
    	
	    return true;	    	    
    }

    public static boolean validateMultiSpeakEndpointCode(final String cd) {
    	if (cd == null || cd.isEmpty() || cd.length() > 5)
    		return false;
    	return true;
    }

    public static boolean validateMultiSpeakVersion(final String version) {
    	if (version == null || version.isEmpty())
    		return false;
    	if (version.equals(MSPServiceOperationKey.SUPPORTED_VERSION_3) || version.equals(MSPServiceOperationKey.SUPPORTED_VERSION_5))
    		return true;
    	return false;
    }

    private static final String ALPHA_NUMERIC_PATTERN = "^[a-zA-Z0-9]*$";
 
    private static Pattern alphaNumericPattern = Pattern.compile(ALPHA_NUMERIC_PATTERN);
    public static boolean validateAlphaNumericOnly(String s) {
        Matcher matcher = alphaNumericPattern.matcher(s);
	    return matcher.matches();	    	    
    }

}
