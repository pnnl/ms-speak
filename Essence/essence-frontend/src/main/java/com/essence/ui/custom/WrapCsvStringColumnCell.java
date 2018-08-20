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

public class WrapCsvStringColumnCell extends AbstractCell<WrapCsvString> implements Cell<WrapCsvString>{
	    String csvString;

	    /**
	     * Add this constructor, if you want click event for this column.
	     */
	    public WrapCsvStringColumnCell() {
	        super("click", "keydown");      
	    }

	    /**
	     * This method provides style for your wrap data
	     * 
	     */
	    @Override
	    public void render(Context context, WrapCsvString value, SafeHtmlBuilder sb) {
	    	String csvString = value.getCommaDelimitedString();
	        @SuppressWarnings("unused")
            String row1Content = csvString;
	        @SuppressWarnings("unused")
	    	String row2Content = null;
/*
	    	String[] tokens = csvString.split(",");
	    	if (tokens.length >= 20) { // split
	    		int row1Size = tokens.length - tokens.length/2;
	    		StringBuffer row1 = new StringBuffer();
	    		row1.append(tokens[0]);
	    		int i = 1;
	    		for (; i<row1Size; i++)
	    			row1.append(",").append(tokens[i]);
	    		StringBuffer row2 = new StringBuffer();
	    		row2.append(tokens[i]);
	    		row1Content = row1.toString();
	    		
	    		i++;
	    		for (;i<tokens.length;i++)
	    			row2.append(",").append(tokens[i]);	  
	    		row2Content = row2.toString();
	    	}
	    	*/
	    	int LINE_SIZE = 60;
	        sb.appendHtmlConstant("<div><table width='100%'>");
	        while (csvString != null && !csvString.isEmpty()) {
	        	if (csvString.length() <= LINE_SIZE) {
	    	        sb.appendHtmlConstant("<tr><td><div>"+csvString+"</div></td></tr>");
	        		break;
	        	} else {
	        		int splitPoint = csvString.substring(LINE_SIZE).indexOf(",");
	        		if (splitPoint == -1) { // got the final one
		    	        sb.appendHtmlConstant("<tr><td><div>"+csvString+"</div></td></tr>");
		        		break;	        			
	        		} else {
		    	        sb.appendHtmlConstant("<tr><td><div>"+csvString.subSequence(0, LINE_SIZE+splitPoint)+"</div></td></tr>");
		    	        csvString = csvString.substring(LINE_SIZE+splitPoint+1);
	        		}
	        	}
	        }
	        /*
	        sb.appendHtmlConstant("<tr><td><div>"+row1Content+"</div></td></tr>");
	        if (row2Content != null)
	        	sb.appendHtmlConstant("<tr><td><div>"+row2Content+"</div></td></tr>");
	        	*/
	        sb.appendHtmlConstant("</table></div>");
	    }

	    /**
	     * This method update cell value on click event.
	     * 
	     */
	    public void onBrowserEvent(Context context, Element parent, WrapCsvString value, NativeEvent event,  ValueUpdater<WrapCsvString> valueUpdater) {
	        super.onBrowserEvent(context, parent, value, event, valueUpdater);
	        setValue(context, parent, value); 
	        valueUpdater.update(value);
	    }
}
