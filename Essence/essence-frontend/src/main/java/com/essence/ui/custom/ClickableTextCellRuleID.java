/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.custom;

import com.google.gwt.cell.client.ClickableTextCell;
import com.google.gwt.safehtml.shared.SafeHtml;
import com.google.gwt.safehtml.shared.SafeHtmlBuilder;

public class ClickableTextCellRuleID extends ClickableTextCell {
	String style;
	
	public ClickableTextCellRuleID() {
		super();
		style = "myClickableCellTestStyle";
	}
	@Override
    protected void render(Context context, SafeHtml value, SafeHtmlBuilder sb) {
     if (!value.asString().equals("none")) {
    	  sb.appendHtmlConstant("<div class=\""+style+"\">");
          sb.append(value);
          sb.appendHtmlConstant("</div>");
      }
     else
    	 sb.append(value);
    }

}
