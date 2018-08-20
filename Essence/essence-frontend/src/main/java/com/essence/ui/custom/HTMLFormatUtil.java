/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.custom;

import com.google.gwt.user.client.ui.HTML;

public class HTMLFormatUtil {
	final static public String HTML_SPACE_FILLER_CONTENT = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp";
	static public HTML getPaddingLabel() {
		return	new HTML(HTML_SPACE_FILLER_CONTENT);
	}
	
}
