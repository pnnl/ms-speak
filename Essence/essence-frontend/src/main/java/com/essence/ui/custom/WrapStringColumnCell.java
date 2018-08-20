/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.custom;

import com.google.gwt.cell.client.AbstractCell;
import com.google.gwt.cell.client.Cell;
import com.google.gwt.cell.client.ValueUpdater;
import com.google.gwt.dom.client.Element;
import com.google.gwt.dom.client.NativeEvent;
import com.google.gwt.safehtml.shared.SafeHtmlBuilder;

public class WrapStringColumnCell extends AbstractCell<WrapString> implements Cell<WrapString>{
    String longString;

    /**
     * Add this constructor, if you want click event for this column.
     */
    public WrapStringColumnCell() {
        super("click", "keydown");      
    }

    /**
     * This method provides style for your wrap data
     * 
     */
    public void render(Cell.Context context, WrapString value, SafeHtmlBuilder sb) {
    	String longString = value.getLongString();
    	@SuppressWarnings("unused")
        String row1Content = longString;
    	@SuppressWarnings("unused")
        String row2Content = null;
    	int LINE_SIZE = 60;
        sb.appendHtmlConstant("<div><table width='100%'>");
        while (longString != null && !longString.isEmpty()) {
        	if (longString.length() <= LINE_SIZE) {
    	        sb.appendHtmlConstant("<tr><td><div>"+longString+"</div></td></tr>");
        		break;
        	} else {
	    	    sb.appendHtmlConstant("<tr><td><div>"+longString.subSequence(0, LINE_SIZE)+"</div></td></tr>");
	    	    longString = longString.substring(LINE_SIZE);
        	}
        }
        sb.appendHtmlConstant("</table></div>");
    }

    /**
     * This method update cell value on click event.
     * 
     */
    public void onBrowserEvent(Cell.Context context, Element parent, WrapString value, NativeEvent event,  ValueUpdater<WrapString> valueUpdater) {
        super.onBrowserEvent(context, parent, value, event, valueUpdater);
        setValue(context, parent, value); 
        valueUpdater.update(value);
    }
}

