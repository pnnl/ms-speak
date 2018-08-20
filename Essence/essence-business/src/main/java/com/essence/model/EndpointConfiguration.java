/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;

import javax.persistence.Column;
import javax.persistence.EmbeddedId;
import javax.persistence.Entity;
import javax.persistence.Table;
import java.io.Serializable;
import java.util.Comparator;
import java.util.List;

@SuppressWarnings("serial")
@Entity
@Table(name = "endpoint_config")
public class EndpointConfiguration implements Serializable, Comparable<EndpointConfiguration> {
	static public String[][] EndpointTypesListItems3 = {
		{"N/A", "N/A"},
		{"CB", "CB - Customer Billing Database"},
		{"CD", "CD - Connect/Disconnect/Power Limitation"},
		{"CH", "CH - Call Handling"},
		{"CRM", "CRM - Customer Relationship Management"},
		{"DAC", "DAC - Distribution Automation Control"},
		{"DAD", "DAD - Distribution Automation Data"},
		{"DGV", "DGV - Dynamic GIS Viewer"},
		{"EA", "EA - Engineering Analysis"},
		{"EDR", "EDR - End Device Receiving"},
		{"EDT", "EDT - End Device Testing"},
		{"FA", "FA - Finance and Accounting"},
		{"GIS", "GIS - Geographic Information System"},
		{"LM", "LM - Load Management"},
		{"LP", "LP - Load Profile"},
		{"MDM", "MDM - Meter Data Management"},
		{"MR", "MR - Meter Reading "},
		{"OA", "OA - Outage Analysis"},
		{"OD", "OD - Outage Detection"},
		{"PP", "PP - Payment Processing"},
		{"PPM", "PPM - Pre-Paid Metering"},
		{"SCADA", "SCADA - Supervisory Control and Data Acquisition"},
		{"SGV", "SGV - Static GIS Viewer"},
		{"Staking", "Staking - Automated Staking"},
	};
	
	static public String[][] EndpointTypesListItems5 = {
		{"N/A", "N/A"},
		{"AM", "AM - Asset management"},
		{"ASM", "ASM - Assembly"},
		{"AVL", "AVL - Automatic Vehicle Locationt"},
		{"CB", "CB - Customer Billing"},
		{"CD", "CD - Connect Disconnect"},
		{"CH", "CH - Call Handling"},
		{"CP", "CP - Commissioning and Provisioning"},
		{"DA", "DA - Distribution Automation"},
		{"DER", "DER - Distributed Energy Resources"},
		{"DGN", "DGN - Design"},
		{"DM", "DM - Demand Management"},
		{"DR", "DR - Demand Response"},
		{"EA", "EA - Engineering Analysis"},
		{"EDTR", "EDTR -  End Device Testing and Receiving "},
		{"FA", "FA - Finance & Accounting"},
		{"GIS", "GIS - Geographic Information System"},
		{"INV", "INV - Material Inventory"},
		{"LOC", "LOC - One Call Locate"},
		{"MDM", "MDM - Meter Data Management"},
		{"MM", "MM - Message Management"},
		{"MOD", "MOD - Power System Model"},
		{"MR", "MR - Meter Reading "},
		{"NOT", "NOT - Notification Services"},
		{"OA", "OA - Outage Analysis"},
		{"OD", "OD - Outage Detection"},
		{"PAN", "PAN - PAN Communications"},
		{"PG", "PG - Payment Gateway"},
		{"PP", "PP - Payment Processing"},
		{"PPM", "PPM - Pre-Paid Metering"},
		{"PUB", "PUB - Publisher (Subscription Management)"},
		{"RM", "RM - Resource Management"},
		{"SCADA", "SCADA - Supervisory Control & Data Acquisition"},
		{"SA", "SA - Scheduling & Assignment"},
		{"SWO", "SWO - Switching Orders"},
		{"WEA", "WEA - Weather Data"},
		{"WG", "WG - Work Generator"},
		{"WO", "WO - Work Owner"},
		{"WP", "WP - Work Performer"},
		{"WR", "WR - Work Requester"},
		{"WV", "WV - Work Viewer"}
	};

	static public boolean isValidEndpointCode3(String cd) {
		if (cd == null || cd.isEmpty())
			return false;
		
		for (int i=1; i<EndpointTypesListItems3.length; i++) {
			if (EndpointTypesListItems3[i][0].equalsIgnoreCase(cd))
				return true;
		}
		
		return false;		
	}

	static public boolean isValidEndpointCode5(String cd) {
		if (cd == null || cd.isEmpty())
			return false;
		
		for (int i=1; i<EndpointTypesListItems5.length; i++) {
			if (EndpointTypesListItems5[i][0].equalsIgnoreCase(cd))
				return true;
		}
		
		return false;		
	}

	@EmbeddedId    
	protected EndpointConfigurationKey key;

	// host name or mac address
	@Column(name = "host_name")
	private String hostName;

	@Column(name = "endpoint_types")
	private String endpointList; // comma delimited list of endpoint types

	@Column(name = "version")
	private String version;

	public String getHostName() {
		return hostName;
	}

	public void setHostName(String hostName) {
		this.hostName = hostName;
	}

	public String getEndpointList() {
		return endpointList;
	}

	public void setEndpointList(String endpointList) {
		this.endpointList = endpointList;
	}

	public String[] getEndpointCDs() {
		if (endpointList == null || endpointList.isEmpty())
			return null;

		return endpointList.split(",");
	}

	// convenient methods
	public String getEndpointListHTML() {
		if (endpointList == null)
			return null;
		return endpointList.replaceAll(",", "<br>");
	}

	public void setEndpointList(List<String> endpoints) {
		if (endpoints == null || endpoints.isEmpty())
			return;
		StringBuffer sb = new StringBuffer();

		sb.append(endpoints.get(0));
		for (int i=1; i<endpoints.size(); i++) {
			sb.append(",").append(endpoints.get(i));
		}
		this.setEndpointList(sb.toString());
	}

	public String getVersion() {
		return version;
	}

	public void setVersion(String version) {
		this.version = version;
	}

	public EndpointConfigurationKey getKey() {
		return key;
	}

	public void setKey(EndpointConfigurationKey key) {
		this.key = key;
	}

	public void print() {
		System.out.println("policyId = " + this.key.getOrganizationId() + "\thost_ip=" + this.key.getHostIPAddress() + "\thost_name=" + this.hostName + "\tEndpoints=" + this.endpointList);
	}
	
	public int compareTo(EndpointConfiguration o) {
        return Comparators.HOST_IP_ADDRESS.compare(this, o);
    }


    public static class Comparators {

        public static Comparator<EndpointConfiguration> HOST_IP_ADDRESS = new Comparator<EndpointConfiguration>() {
            public int compare(EndpointConfiguration o1, EndpointConfiguration o2) {
        		
        		if (o2 == null || o2.key.getHostIPAddress() == null || o2.key.getHostIPAddress().isEmpty())
        			return 1; 
        		
        		if (o1 == null || o1.key.getHostIPAddress() == null || o1.key.getHostIPAddress().isEmpty())
        			return -1; 
        		
        		String[] ipParts = o1.key.getHostIPAddress().split("\\.");
        		String[] ipParts2 = o2.key.getHostIPAddress().split("\\.");
        		
        		for (int i=0; i<ipParts.length; i++) {
        			if (!ipParts[i].equals(ipParts2[i]))
        				return Integer.valueOf(ipParts[i]) - Integer.valueOf(ipParts2[i]); // ascending order
        		}
        		
        		return 0;
            }
        };
    }

    public EndpointConfiguration(EndpointConfigurationKey key, String hostName, String endpointList, String version) {
        this.key = key;
        this.hostName = hostName;
        this.endpointList = endpointList;
        this.version = version;
    }

    public EndpointConfiguration() {
    }
}
