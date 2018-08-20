/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.object;


import java.io.Serializable;

import javax.persistence.Column;
import javax.persistence.Embeddable;

@SuppressWarnings("serial")
public class VOOBKeyDTO  implements Serializable {
	private int ruleId;    

	private int xPathId;

	private String operator;

	public int getRuleId() {
		return ruleId;
	}

	public void setRuleId(int ruleId) {
		this.ruleId = ruleId;
	}

	public int getxPathId() {
		return xPathId;
	}

	public void setxPathId(int xPathId) {
		this.xPathId = xPathId;
	}

	public String getOperator() {
		return operator;
	}

	public void setOperator(String operator) {
		this.operator = operator;
	}

	public VOOBKeyDTO(int ruleId, int xPathId, String operator) {
		this.ruleId = ruleId;
		this.xPathId = xPathId;
		this.operator = operator;
	}
	
	public VOOBKeyDTO() {
	    
	}
}
