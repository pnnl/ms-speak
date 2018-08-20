/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;


import com.essence.model.DecisionType;

import javax.persistence.*;
import java.io.Serializable;

@SuppressWarnings("serial")
@Entity
@Table(name = "decision_rule")
public class DecisionRule implements Serializable {
	@Id @GeneratedValue
	@Column(name = "rule_id")
	private int	   id;
	
	@Column(name = "detection_rule_type") // decision based on detection rule category, ref DetectionRuleType
	private String detectionRuleType; 
	
	@Column(name = "detection_rule_ref") // decision based on detection rule itself
	private Integer detectionRuleRef; 
	
	@Column(name = "severity_type")	// severity based decision, ref SeverityType
	private String severityType; 		
	
	@Column(name = "decision_type")
	private String decisionType; // type of decision rule in categorization, ref DecisionRuleType

	@ManyToOne
	@JoinColumn(name="stateid")//, insertable=false, updatable=false)
	private AnomalyState state;

	@ManyToOne
	@JoinColumn(name="causeid")//, insertable=false, updatable=false)
	private Cause cause;

	@Column(name = "priority")
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

	public void setDetectionRuleType(DetectionRuleType detectionRuleType) {
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

	public void setSeverityType(SeverityType severityType) {
		if(severityType != null)
			this.severityType = severityType.toString();
	}

	public String getDecisionType() {
		return decisionType;
	}

	public void setDecisionType(DecisionType decisionType) {
		if (decisionType != null)
			this.decisionType = decisionType.toString();
	}

	public Integer getPriority() {
		return priority;
	}

	public void setPriority(Integer priority) {
		this.priority = priority;
	}

	public AnomalyState getState() {
		return state;
	}

	public void setState(AnomalyState state) {
		this.state = state;
	}

	public Cause getCause() {
		return cause;
	}

	public void setCause(Cause cause) {
		this.cause = cause;
	}
	public void print() {
		StringBuffer sb = new StringBuffer();
		sb.append("id="+id+"\tdetectionRuleType="+this.detectionRuleType+"\tdetectionRuleRef="+this.detectionRuleRef+"\tseverityType="+this.severityType+"\tdecisionType="+this.decisionType+"\tpriority="+priority);
		System.out.println(sb.toString());
	}

	public DecisionRule(String detectionRuleType, Integer detectionRuleRef, String severityType, String decisionType,
						Cause cause, AnomalyState state, Integer priority) {
		this.detectionRuleType = detectionRuleType;
		this.detectionRuleRef = detectionRuleRef;
		this.severityType = severityType;
		this.decisionType = decisionType;
		this.cause = cause;
		this.state = state;
		this.priority = priority;
	}

	public DecisionRule() {
	}
}
