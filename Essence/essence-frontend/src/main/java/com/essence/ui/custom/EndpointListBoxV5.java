/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.custom;

import com.essence.ui.client.object.EndpointConfigurationDTO;
import com.google.gwt.user.client.ui.ListBox;

public class EndpointListBoxV5 extends ListBox {
	/*
	static public String[][] EndpointTypesListItems = {
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
	*/

	static public String[][] EndpointTypesListItems = EndpointConfigurationDTO.EndpointTypesListItems5;

	public EndpointListBoxV5() {
		super();
		for (int i=0; i<EndpointTypesListItems.length; i++) {
			this.addItem(EndpointTypesListItems[i][1], EndpointTypesListItems[i][0]);
		}
	}
	
	static public void copyListItemsToListBox(ListBox lb) {
		if (lb == null)
			return;
		for (int i=0; i<EndpointTypesListItems.length; i++) {
			lb.addItem(EndpointTypesListItems[i][1], EndpointTypesListItems[i][0]);
		}		
	}	
}
