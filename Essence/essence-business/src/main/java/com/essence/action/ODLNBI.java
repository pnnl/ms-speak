/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.action;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import com.essence.action.util.Prop;

public class ODLNBI {

	String postUrl = "/restconf/config/opendaylight-inventory:nodes";
	String getSwitchURL = "/restconf/operational/opendaylight-inventory:nodes";
	String getHostURL = "/restconf/operational/opendaylight-inventory:nodes/node";

	String restTableFlowURL = "/restconf/config/opendaylight-inventory:nodes/node";

	Prop prop = new Prop();
	String controllerURL = prop.getControllerUrl();

	/*	public static void main(String[] z)
	{
		System.out.println("I Rule!!");
		ODLNBI odlNbi = new ODLNBI();

		odlNbi.applyRule("0.0.0.0", "0", "10.0.0.2", "32", "ipv4", "drop");
	}
	 */
	public Map<String, String> getSwitchHostIPMapping()
	{
		String switchURL = controllerURL + getSwitchURL;
		String hostURL = controllerURL + getHostURL;
		String switchesString = getRestCall(switchURL);
		Nodes nodeInfo = new Nodes();
		ArrayList<String> switchList = nodeInfo.getSwitches(switchesString);
		String hostString;
		Map<String, String> ipSwitchMap = new HashMap<String, String>();
		for(int i=0;i<switchList.size();i++)
		{
			System.out.println("Switch is : " + switchList.get(i));
			hostString = getRestCall(hostURL + "/" + switchList.get(i));
			System.out.println("Host String = " + hostString);
			ArrayList<String> ipArraylist = nodeInfo.getIPAddressAndMACMapping(hostString);
			for(int j=0;j<ipArraylist.size();j++)
			{
				ipSwitchMap.put(ipArraylist.get(j), switchList.get(i));
			}
		}
		return ipSwitchMap;
	}

	public String applyPairBlockRule(String sourceIPAddress, String sourceIPAddressPrefix, String destinationIPAddress, String destinationIPADrressPrefix, String ipProto, String rule)
	{
		Map<String, String> ipSwitchMap = getSwitchHostIPMapping();

		String tableFlowURL = controllerURL + restTableFlowURL +  "/" + ipSwitchMap.get(sourceIPAddress) + "/table/0/flow/1";
		System.out.println("tableFlowURL = " + tableFlowURL);
		String result1 = "", result2 = "";
		if(rule.equalsIgnoreCase("DENY") | rule.equalsIgnoreCase("DROP"))
		{
			String payload =new XMLString().getBlockSourceAndDestinationIPAddressXMLObject(sourceIPAddress, sourceIPAddressPrefix, destinationIPAddress, destinationIPADrressPrefix, ipProto, "0", "1");
			result1 = putRestCall(tableFlowURL, payload);
		}

		tableFlowURL = controllerURL + restTableFlowURL +  "/" + ipSwitchMap.get(destinationIPAddress) + "/table/0/flow/1";
		System.out.println("tableFlowURL = " + tableFlowURL);
		if(rule.equalsIgnoreCase("DENY") | rule.equalsIgnoreCase("DROP"))
		{
			String payload =new XMLString().getBlockSourceAndDestinationIPAddressXMLObject(sourceIPAddress, sourceIPAddressPrefix, destinationIPAddress, destinationIPADrressPrefix, ipProto, "0", "1");
			result2 = putRestCall(tableFlowURL, payload);
		}
		if(result1.equalsIgnoreCase(result2) && !result1.equalsIgnoreCase(""))
			return result1;
		return "failed!!";
	}

	public String applySourceBlockRule(String sourceIPAddress, String sourceIPAddressPrefix, String destinationIPAddress, String destinationIPADrressPrefix, String ipProto, String rule)
	{
		Map<String, String> ipSwitchMap = getSwitchHostIPMapping();

		String tableFlowURL = controllerURL + restTableFlowURL +  "/" + ipSwitchMap.get(sourceIPAddress) + "/table/0/flow/1";
		System.out.println("tableFlowURL = " + tableFlowURL);
		if(rule.equalsIgnoreCase("DENY") | rule.equalsIgnoreCase("DROP"))
		{
			String payload =new XMLString().getBlockSourceAndDestinationIPAddressXMLObject(sourceIPAddress, sourceIPAddressPrefix, destinationIPAddress, destinationIPADrressPrefix, ipProto, "0", "1");
			return putRestCall(tableFlowURL, payload);
		}
		return "failed!!";
	}

	public String applyDestinationBlockRule(String sourceIPAddress, String sourceIPAddressPrefix, String destinationIPAddress, String destinationIPADrressPrefix, String ipProto, String rule)
	{
		Map<String, String> ipSwitchMap = getSwitchHostIPMapping();

		String tableFlowURL = controllerURL + restTableFlowURL +  "/" + ipSwitchMap.get(destinationIPAddress) + "/table/0/flow/1";
		System.out.println("tableFlowURL = " + tableFlowURL);
		if(rule.equalsIgnoreCase("DENY") | rule.equalsIgnoreCase("DROP"))
		{
			String payload =new XMLString().getBlockSourceAndDestinationIPAddressXMLObject(sourceIPAddress, sourceIPAddressPrefix, destinationIPAddress, destinationIPADrressPrefix, ipProto, "0", "1");
			return putRestCall(tableFlowURL, payload);
		}
		return "failed!!";
	}

	//address-tracker:addresses
	public String getRestCall(String url)
	{
		System.out.println(url);
		StringBuilder sb = new StringBuilder();

		URL obj;
		HttpURLConnection con;
		try {
			obj = new URL(url);
			con = (HttpURLConnection) obj.openConnection();
			con.setRequestMethod("GET");
			con.setRequestProperty("Accept", "application/json");
			con.setRequestProperty("Authorization", "Basic YWRtaW46YWRtaW4=");
			con.setDoOutput(true);

			int responseCode = con.getResponseCode();

			if (responseCode == HttpURLConnection.HTTP_OK) { // success
				BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));

				int cp;
				while ((cp = in.read()) != -1) {
					sb.append((char) cp);
				}
				in.close();
			} else {
				System.out.println("GET request not worked");
			}
		} catch (MalformedURLException e) {
			e.printStackTrace();
		}
		catch(IOException e){
			e.printStackTrace();
		}
		return sb.toString();
	}

	public String putRestCall(String url, String payload)
	{
		StringBuilder sb = new StringBuilder("PUT request not worked");

		URL obj;
		HttpURLConnection con;
		try {
			obj = new URL(url);
			con = (HttpURLConnection) obj.openConnection();
			con.setRequestMethod("PUT");
			con.setRequestProperty("Content-Type", "application/xml");
			con.setRequestProperty("Accept", "application/json");
			con.setRequestProperty("Authorization", "Basic YWRtaW46YWRtaW4=");
			con.setDoOutput(true);

			DataOutputStream wr = new DataOutputStream(con.getOutputStream());
			wr.writeBytes(payload);
			wr.flush();
			wr.close();

			int responseCode = con.getResponseCode();

			if (responseCode == HttpURLConnection.HTTP_OK) { // success
				BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
				sb=new StringBuilder("");
				int cp;
				while ((cp = in.read()) != -1) {
					sb.append((char) cp);
				}
				in.close();
			} else {
				System.out.println("PUT request not worked");
			}
		} catch (MalformedURLException e) {
			e.printStackTrace();
		}
		catch(IOException e){
			e.printStackTrace();
		}
		return sb.toString();
	}

	public String deleteRestCall(String url)
	{
		StringBuilder sb = new StringBuilder("DELETE request not worked");

		URL obj;
		HttpURLConnection con;
		try {
			obj = new URL(url);
			con = (HttpURLConnection) obj.openConnection();
			con.setRequestMethod("DELETE");
			con.setRequestProperty("Accept", "application/json");
			con.setRequestProperty("Authorization", "Basic YWRtaW46YWRtaW4=");
			con.setDoOutput(true);

			int responseCode = con.getResponseCode();

			if (responseCode == HttpURLConnection.HTTP_OK) { // success
				BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
				sb = new StringBuilder("");
				int cp;
				while ((cp = in.read()) != -1) {
					sb.append((char) cp);
				}
				in.close();
			} else {
				System.out.println("DELETE request not worked");
			}
		} catch (MalformedURLException e) {
			e.printStackTrace();
		}
		catch(IOException e){
			e.printStackTrace();
		}
		return sb.toString();
	}
}