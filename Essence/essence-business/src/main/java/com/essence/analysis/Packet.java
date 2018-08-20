/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.analysis;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.EmbeddedId;
import javax.persistence.PersistenceContext;
import javax.persistence.Table;

import com.essence.multispeak.MSPServiceOperationKey;

import java.io.Serializable;
import java.io.UnsupportedEncodingException;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

@SuppressWarnings("serial")
@Entity
@Table(name = "packet", schema = "demo@cassandra_pu")
@PersistenceContext(unitName="cassandra_pu") 
public class Packet implements Serializable
{    
	static public final String MESSAGE_TYPE_KEY = "messagetype"; // e.g. setDisconnectedStatus
	static public final String ENDPOINT_NAME_KEY = "endpoint"; // e.g. MR_Server
	static public final String MSP_VERSION_KEY = "mspVersion"; // e.g.
	// lookup key for MSP version, e.g. V5 or V3,  Version_3.0, V5.0
															// xmlns:ver="http://www.multispeak.org/Version_3.0"
															// xmlns:res="http://www.multispeak.org/V5.0/ws/response"
	@EmbeddedId    
	protected PacketPK packetPK;
	
	@Column(name="protocol")    
	private String protocol;        
	
	@Column(name="content")    
	private byte[] content;        

	@Column(name="voltage")    
	private Integer voltage;        

	@Column(name="numeric_values")    
	private Map<String, Float> numericValues;        
	
	@Column(name="text_values")    
	private Map<String, String> textValues;        

	public Map<String, Float> getNumericValues() {
		return numericValues;
	}

	public void setNumericValues(Map<String, Float> numericValues) {
		this.numericValues = numericValues;
	}

	public Map<String, String> getTextValues() {
		return textValues;
	}

	public void setTextValues(Map<String, String> textValues) {
		this.textValues = textValues;
	}

	public Integer getVoltage() {
		return voltage;
	}

	public void setVoltage(Integer voltage) {
		this.voltage = voltage;
	}

	public Packet() {}    
	
	public Packet(PacketPK key, String protocol, byte[] content)    
	{    	
		this.packetPK = key;
		this.protocol = protocol;
		this.content = content;
	}

	public PacketPK getPacketPK() 
	{		
		return packetPK;	
	}

	public void setPacketPK(PacketPK key) 
	{		
		this.packetPK = key;	
	}	
	
	public String getProtocol() 
	{		
		return protocol;	
	}	
	
	public void setProtocol(String protocol) 
	{		
		this.protocol = protocol;	
	}	
	
	public byte[] getContent() 
	{		
		return content;	
	}	
	
	public void setContent(byte[] content) 
	{		
		this.content = content;	
	}	
	
	public String getMspVersion() {
		if (getTextValues() == null || getTextValues().isEmpty())
			return null;
		
		String version = getTextValues().get(MSP_VERSION_KEY);
		if (version == null)
			return null;
		
		if (version.contains("V5") || version.contains("v5") || version.contains("5"))
			return MSPServiceOperationKey.SUPPORTED_VERSION_5;
		
		if (version.contains("Version_3") || version.contains("V3") || version.contains("v3") || version.contains("3"))
			return MSPServiceOperationKey.SUPPORTED_VERSION_3;
		
		return null;
	}
	
	public void print() {
		System.out.print("\tSource = " + getPacketPK().getSourceAddress());
		System.out.print("\tDestination = " + getPacketPK().getDestAddress());
		System.out.print("\tTimestamp = " + getPacketPK().getTimeStamp());
		System.out.print("\tProtocol = " + getProtocol());
		System.out.print("\tVoltage = " + this.getVoltage());
		System.out.println("\tcontent = " + ba2string(getContent()));
		printNumericValues(getNumericValues());
		printTextValues(getTextValues());
		System.out.println("\tMultiSpeak field value = " + PacketParser.extractMultiSpeakFieldValue(this));		
	}

	public void printNoContent() {
		System.out.print("\tSource = " + getPacketPK().getSourceAddress());
		System.out.print("\tDestination = " + getPacketPK().getDestAddress());
		System.out.print("\tTimestamp = " + getPacketPK().getTimeStamp());
		System.out.print("\tProtocol = " + getProtocol());
		System.out.println("\tVoltage = " + this.getVoltage());
		//System.out.println("\tcontent = " + ba2string(getContent()));
		printNumericValues(getNumericValues());
		printTextValues(getTextValues());
		System.out.println("\tMultiSpeak field value = " + PacketParser.extractMultiSpeakFieldValue(this));		
	}
	
	public static String ba2string(byte[] ba) {
		String s = ba.toString()+": ";
		try {
			String s1 = new String(ba, "UTF-8");
			return s+s1;
		} catch (UnsupportedEncodingException ex) {
			ex.printStackTrace();
			return s;
		}
	}
	
	static void printNumericValues(Map<String, Float> nvs) {
		StringBuffer sb = new StringBuffer(200);
		sb.append("{");
		if (nvs != null && !nvs.isEmpty()) {
			Set<String> keySet = nvs.keySet();
			Iterator<String> it = keySet.iterator();
			boolean isNotFirst = false;
			while (it.hasNext()){
				if (isNotFirst) {
					sb.append(",");
				}
				isNotFirst = true;
				String key = it.next();
				sb.append("'");
				sb.append(key);
				sb.append("'");
				sb.append(":");
				Object o = nvs.get(key);
				sb.append(o.toString());
			}
		}
		sb.append("}");
		System.out.println(sb.toString());
	}

	static void printTextValues(Map<String, String> nvs) {
		StringBuffer sb = new StringBuffer(200);
		sb.append("{");
		if (nvs != null && !nvs.isEmpty()) {
			Set<String> keySet = nvs.keySet();
			Iterator<String> it = keySet.iterator();
			boolean isNotFirst = false;
			while (it.hasNext()){
				if (isNotFirst) {
					sb.append(",");
				}
				isNotFirst = true;
				String key = it.next();
				sb.append("'");
				sb.append(key);
				sb.append("'");
				sb.append(":");
				String o = nvs.get(key);
				sb.append("'");
				sb.append(o.toString());
				sb.append("'");
			}
		}
		sb.append("}");
		System.out.println(sb.toString());
	}

}