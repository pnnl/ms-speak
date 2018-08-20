/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.action;

import java.util.List;

public class Device {
	String		entityClass;
	List<String>	mac;
	List<String>	ipv4;
	List<String>	vlan;
	List<AttachmentPoint>	attachmentPoint;		
	long		lastSeen;
	
	public String getEntityClass() {
		return entityClass;
	}

	public void setEntityClass(String entityClass) {
		this.entityClass = entityClass;
	}

	public List<String> getMac() {
		return mac;
	}

	public void setMac(List<String> mac) {
		this.mac = mac;
	}

	public List<String> getIpv4() {
		return ipv4;
	}

	public void setIpv4(List<String> ipv4) {
		this.ipv4 = ipv4;
	}

	public List<String> getVlan() {
		return vlan;
	}

	public void setVlan(List<String> vlan) {
		this.vlan = vlan;
	}

	public List<AttachmentPoint> getAttachmentPoint() {
		return attachmentPoint;
	}

	public void setAttachmentPoint(List<AttachmentPoint> attachmentPoint) {
		this.attachmentPoint = attachmentPoint;
	}

	public long getLastSeen() {
		return lastSeen;
	}

	public void setLastSeen(long lastSeen) {
		this.lastSeen = lastSeen;
	}

	public void print() {
		System.out.print("entityClass="+entityClass+"\tmac"+listToString(mac)+"\tipv4"+listToString(ipv4)+"\tvlan"+listToString(vlan)+"\tlastSeen"+lastSeen);
		if (attachmentPoint == null || attachmentPoint.isEmpty())
			System.out.println("\tattachmentPoint[]");
		else {
			System.out.print("\tattachmentPoint[");
			System.out.print(attachmentPoint.get(0).toString());
			for (int i=1; i<attachmentPoint.size(); i++)
				System.out.print("; "+attachmentPoint.get(i).toString());
			System.out.println("]");
		}		
	}
	
	public String listToString(List<String> l) {
		if (l == null || l.isEmpty())
			return "[]";
		StringBuilder sb = new StringBuilder();
		sb.append("[");
		sb.append(l.get(0));
		for (int i=1; i<l.size(); i++)
			sb.append(", " + l.get(i));
		sb.append("]");
		return sb.toString();
	}
}
