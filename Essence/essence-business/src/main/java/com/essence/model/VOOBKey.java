/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;


import javax.persistence.Column;
import javax.persistence.Embeddable;
import java.io.Serializable;

@SuppressWarnings("serial")
@Embeddable
public class VOOBKey implements Serializable {
	@Column(name = "rule_id", nullable = false)    
	private int ruleId;    
	
	@Column(name = "xpath_id", nullable = false)    
	private int xPathId;
	
	@Column(name = "operator", nullable = false)    
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

	public VOOBKey(int ruleId, int xPathId, String operator) {
		this.ruleId = ruleId;
		this.xPathId = xPathId;
		this.operator = operator;
	}

	public VOOBKey() {
	}
}
