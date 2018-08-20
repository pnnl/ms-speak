/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.custom;

import com.google.gwt.cell.client.ClickableTextCell;
import com.google.gwt.safehtml.shared.SafeHtml;
import com.google.gwt.safehtml.shared.SafeHtmlBuilder;

public class VOOBDetailClickableCellText  extends ClickableTextCell {
	String style;
	
	public VOOBDetailClickableCellText() {
		super();
		style = "myClickableCellTestStyle";
	}
	@Override
    protected void render(Context context, SafeHtml value, SafeHtmlBuilder sb) {
      // Make the details clickable for VOOB rule
      if (value != null && !value.asString().isEmpty()) {
    	  sb.appendHtmlConstant("<div class=\""+style+"\">");
          sb.append(value);
          sb.appendHtmlConstant("</div>");
      }
    }

   public void addStyleName(String style) {
       this.style = style; 
   }

}
