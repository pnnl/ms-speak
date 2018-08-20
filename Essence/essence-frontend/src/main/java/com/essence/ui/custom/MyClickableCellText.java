/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.custom;

import com.google.gwt.cell.client.ClickableTextCell;
import com.google.gwt.safehtml.shared.SafeHtml;
import com.google.gwt.safehtml.shared.SafeHtmlBuilder;

public class MyClickableCellText extends ClickableTextCell {
	String style;
	
	public MyClickableCellText() {
		super();
		style = "myClickableCellTestStyle";
	}
	@Override
    protected void render(Context context, SafeHtml value, SafeHtmlBuilder sb) {
      if (value != null && !value.asString().equals("assign")) {
          sb.append(value);
      }
      // if the value is assign, then we need to make the cell clickable with underline
      // otherwise, not.
      if (value.asString().equals("assign")) {
    	  sb.appendHtmlConstant("<div class=\""+style+"\">");
          sb.append(value);
          sb.appendHtmlConstant("</div>");
      }
    }

   public void addStyleName(String style) {
       this.style = style; 
   }
}
