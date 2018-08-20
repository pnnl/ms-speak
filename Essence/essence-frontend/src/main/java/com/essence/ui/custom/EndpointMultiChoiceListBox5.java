/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.custom;

import java.util.LinkedList;
import java.util.List;

import com.google.gwt.user.client.ui.ListBox;

public class EndpointMultiChoiceListBox5 extends ListBox {
	public EndpointMultiChoiceListBox5() {
		super();
		for (int i=0; i<EndpointListBoxV5.EndpointTypesListItems.length; i++) {
			this.addItem(EndpointListBoxV5.EndpointTypesListItems[i][1], EndpointListBoxV5.EndpointTypesListItems[i][0]);
		}
		this.setMultipleSelect(true);
	}

	public List<String> getSelectedItems() {
	    List<String> selectedItems = new LinkedList<String>();
	    for (int i = 0; i < getItemCount(); i++) {
	        if (isItemSelected(i)) {
	            selectedItems.add(this.getValue(i));
	        }
	    }
	    return selectedItems;
	}
	
	public void setSelected(String endpointList) { // take in a comma separated list of endpoint codes
		if (endpointList == null || endpointList.isEmpty())
			return;
		
		String[] endpoints = endpointList.split(",");
		for (int i=0; i<endpoints.length; i++)
			for (int j=0; j<EndpointListBoxV5.EndpointTypesListItems.length; j++) {
				if (endpoints[i].equalsIgnoreCase(EndpointListBoxV5.EndpointTypesListItems[j][0]))
					this.setItemSelected(j, true);
		}	
	}
}
