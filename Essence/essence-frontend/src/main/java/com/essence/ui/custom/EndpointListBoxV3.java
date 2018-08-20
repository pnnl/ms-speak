/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.custom;

import com.essence.ui.client.object.EndpointConfigurationDTO;
import com.google.gwt.user.client.ui.ListBox;

public class EndpointListBoxV3 extends ListBox {
	/*
	static public String[][] EndpointTypesListItems = {
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
	*/

	static public String[][] EndpointTypesListItems = EndpointConfigurationDTO.EndpointTypesListItems3;
	
	public EndpointListBoxV3() {
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
