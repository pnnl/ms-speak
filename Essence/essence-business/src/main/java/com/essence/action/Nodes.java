/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.action;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class Nodes{
	public ArrayList<String> getSwitches(String string)
	{
		JSONObject json;
		JSONArray nodeArray;
		ArrayList<String> switches = new ArrayList<String>();
		try {
			json = new JSONObject(string);
			nodeArray = json.getJSONObject("nodes").getJSONArray("node");
			for(int i=0;i<nodeArray.length();i++)
			{
				switches.add(nodeArray.getJSONObject(i).get("id").toString());
			}
		} catch (JSONException e) {
			e.printStackTrace();
		}
		return switches;
	}

	public ArrayList<String> getIPAddressAndMACMapping(String string)
	{
		JSONObject json;
		JSONArray nodeArray, nodeConnectorArray;
		Map<String, String> ipMacMap = new HashMap<String, String>();
		ArrayList<String> ipArray = new ArrayList<String>();
		try {
			json = new JSONObject(string);
			nodeArray = json.getJSONArray("node");
			for(int i=0;i<nodeArray.length();i++) {
				nodeConnectorArray = nodeArray.getJSONObject(i).getJSONArray("node-connector");
				for(int j=0;j<nodeConnectorArray.length();j++) {
					try {
						String addressMap = nodeConnectorArray.getJSONObject(j).get("address-tracker:addresses").toString();
						String ip = new JSONObject(addressMap.substring(1, addressMap.length()-1)).get("ip").toString();
						String mac = new JSONObject(addressMap.substring(1,addressMap.length()-1)).get("mac").toString();					
						ipArray.add(ip);
						ipMacMap.put(ip, mac);
					} catch(Exception e) {
						continue;
					}
				}
			}
		} catch (JSONException e) {
			e.printStackTrace();
		}
		return ipArray;
	}
}
