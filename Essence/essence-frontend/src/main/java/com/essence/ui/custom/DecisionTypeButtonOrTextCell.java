/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.custom;

import com.essence.ui.client.object.DecisionTypeDTO;
import com.google.gwt.cell.client.AbstractCell;
import com.google.gwt.cell.client.ButtonCell;
import com.google.gwt.cell.client.TextCell;
import com.google.gwt.safehtml.shared.SafeHtml;
import com.google.gwt.safehtml.shared.SafeHtmlBuilder;

public class DecisionTypeButtonOrTextCell<T> extends AbstractCell<T> {
    ButtonCell buttonCell = new ButtonCell();
    TextCell textCell = new TextCell();

	@Override
	public void render(Context arg0, Object arg1, SafeHtmlBuilder arg2) {
		// TODO Auto-generated method stub
        if (arg1 != null && arg1.equals(DecisionTypeDTO.MANUAL_ACTION.toString())) {
        	buttonCell.render(arg0, (SafeHtml)arg1, arg2);
        } else {
            textCell.render(arg0,(SafeHtml) arg1, arg2);
        }		
	}

	public ButtonCell getButtonCell() {
		return buttonCell;
	}

	public void setButtonCell(ButtonCell buttonCell) {
		this.buttonCell = buttonCell;
	}

	public TextCell getTextCell() {
		return textCell;
	}

	public void setTextCell(TextCell textCell) {
		this.textCell = textCell;
	}
}
