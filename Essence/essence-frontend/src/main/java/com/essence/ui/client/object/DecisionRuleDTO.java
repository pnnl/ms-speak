/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.object;

import java.io.Serializable;

@SuppressWarnings("serial")
public class DecisionRuleDTO implements Serializable {
	private int	   id;
	
	// decision based on detection rule category, ref DetectionRuleType
	private String detectionRuleType; 
	
	// decision based on detection rule itself
	private Integer detectionRuleRef; 
	
	// severity based decision, ref SeverityType
	private String severityType;
	
	private String decisionType; // type of decision rule in categorization, ref DecisionRuleType

	private AnomalyStateDTO state;

	private CauseDTO cause;

	private Integer priority;	// priority default to 99999

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getDetectionRuleType() {
		return detectionRuleType;
	}

	public void setDetectionRuleType(DetectionRuleTypeDTO detectionRuleType) {
		if (detectionRuleType != null)
			this.detectionRuleType = detectionRuleType.toString();
	}

	public Integer getDetectionRuleRef() {
		return detectionRuleRef;
	}

	public void setDetectionRuleRef(Integer detectionRuleRef) {
		this.detectionRuleRef = detectionRuleRef;
	}

	public String getSeverityType() {
		return severityType;
	}

	public void setSeverityType(SeverityTypeDTO severityType) {
		if(severityType != null)
			this.severityType = severityType.toString();
	}

	public String getDecisionType() {
		return decisionType;
	}

	public void setDecisionType(DecisionTypeDTO decisionType) {
		if (decisionType != null)
			this.decisionType = decisionType.toString();
	}

	public Integer getPriority() {
		return priority;
	}

	public void setPriority(Integer priority) {
		this.priority = priority;
	}

	public AnomalyStateDTO getState() {
		return state;
	}

	public void setState(AnomalyStateDTO state) {
		this.state = state;
	}

	public CauseDTO getCause() {
		return cause;
	}

	public void setCause(CauseDTO cause) {
		this.cause = cause;
	}

	public void print() {
		StringBuffer sb = new StringBuffer();
		sb.append("id="+id+"\tdetectionRuleType="+this.detectionRuleType+"\tdetectionRuleRef="+this.detectionRuleRef+
                "\tseverityType="+this.severityType+"\tdecisionType="+this.decisionType+"\tpriority="+priority);
		System.out.println(sb.toString());
	}

	public DecisionRuleDTO(int id, String detectionRuleType, Integer detectionRuleRef, String severityType,
						   String decisionType, CauseDTO cause, AnomalyStateDTO state, Integer priority) {
		this.id = id;
	    this.detectionRuleType = detectionRuleType;
		this.detectionRuleRef = detectionRuleRef;
		this.severityType = severityType;
		this.decisionType = decisionType;
		this.cause = cause;
		this.state = state;
		this.priority = priority;
	}

	public DecisionRuleDTO() {
	}
}
