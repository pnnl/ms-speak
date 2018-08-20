/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.custom;

import java.util.LinkedList;
import java.util.List;

import com.essence.multispeak.MSPServiceOperationKey;
import com.google.gwt.user.client.ui.ListBox;

public class EndpointMultiChoiceListBox extends ListBox {
	String version = null;
	
	public EndpointMultiChoiceListBox() {
		super();
		this.setMultipleSelect(true);
	}
	
	public void setVersion(String version) {
		this.version = version;
		if (version != null && version.equals(MSPServiceOperationKey.SUPPORTED_VERSION_3)) {
			this.clear();
			for (int i=0; i<EndpointListBoxV3.EndpointTypesListItems.length; i++) {
				this.addItem(EndpointListBoxV3.EndpointTypesListItems[i][1], EndpointListBoxV3.EndpointTypesListItems[i][0]);
			}		
		} else if (version != null && version.equals(MSPServiceOperationKey.SUPPORTED_VERSION_5)) {
			this.clear();
			for (int i=0; i<EndpointListBoxV5.EndpointTypesListItems.length; i++) {
				this.addItem(EndpointListBoxV5.EndpointTypesListItems[i][1], EndpointListBoxV5.EndpointTypesListItems[i][0]);
			}
		}
	}
	
	public String getVersion() {
		return version;
	}

	public List<String> getSelectedItems() {
	    List<String> selectedItems = new LinkedList<String>();
	    for (int i = 0; i < getItemCount(); i++) {
	        if (isItemSelected(i) && !getValue(i).equals("N/A")) {
	            selectedItems.add(this.getValue(i));
	        }
	    }
	    return selectedItems;
	}
	
	public void setSelected(String endpointList) { // take in a comma separated list of endpoint codes
		if (endpointList == null || endpointList.isEmpty()) {
		    for (int i = 0; i < getItemCount(); i++) {
		        if (isItemSelected(i)) {
		            this.setItemSelected(i, false);
		        }
		    }			
			return;
		}
		
		String[] endpoints = endpointList.split(",");
		if (version != null && version.equals(MSPServiceOperationKey.SUPPORTED_VERSION_3)) {
			for (int i=0; i<endpoints.length; i++)
				for (int j=0; j<EndpointListBoxV3.EndpointTypesListItems.length; j++) {
					if (endpoints[i].equalsIgnoreCase(EndpointListBoxV3.EndpointTypesListItems[j][0]))
						this.setItemSelected(j, true);
			}	
		} else if (version != null && version.equals(MSPServiceOperationKey.SUPPORTED_VERSION_5)) {
			for (int i=0; i<endpoints.length; i++)
				for (int j=0; j<EndpointListBoxV5.EndpointTypesListItems.length; j++) {
					if (endpoints[i].equalsIgnoreCase(EndpointListBoxV5.EndpointTypesListItems[j][0]))
						this.setItemSelected(j, true);
			}	
		}
	}
}
