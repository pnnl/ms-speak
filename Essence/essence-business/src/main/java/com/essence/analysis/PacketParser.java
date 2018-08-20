/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.analysis;

public class PacketParser {
	static public Integer extractMultiSpeakFieldValue(Packet p) {
		Integer value = null;
		String content = Packet.ba2string(p.getContent());
		if (content == null)
			return null;
		
		int start = content.indexOf("<ver:meterNo>");
		int end = content.indexOf("</ver:meterNo>");
		if (start > -1 && end > -1) {
			String mnStr = content.substring(start+13, end);
			try {
				value = Integer.valueOf(mnStr);
			} catch (NumberFormatException ex){
				//
			}
			
			return value;
		}
		
		return null;
	}
}
