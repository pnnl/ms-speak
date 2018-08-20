/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;

import com.essence.model.Decision;

import java.io.Serializable;
import java.sql.Timestamp;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToOne;
import javax.persistence.Table;

@SuppressWarnings("serial")
@Entity
@Table(name = "action")
public class Action implements Serializable {
	@Id @GeneratedValue
	@Column(name = "id")
	private int	   id;
	
	@Column(name = "detail") // content for notification, or decisionType for manual action ref DecisionRuleTyp
	private String detail; 
	
	@Column(name = "decision_id", insertable=false, updatable=false)	// decision rule id
	private Integer decisionId;
	
	@Column(name = "timestamp") // if decision impact source host
	private Timestamp timestamp;

    @OneToOne(fetch=FetchType.EAGER)
    @JoinColumn(name="decision_id")
    private Decision decision;
    
	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getDetail() {
		return detail;
	}

	public void setDetail(String detail) {
		this.detail = detail;
	}

	public Decision getDecision() {
		return decision;
	}

	public void setDecision(Decision decision) {
		this.decision = decision;
		this.decisionId = decision.getId();
	}

	public Integer getDecisionId() {
		return decisionId;
	}

	public void setDecisionId(Integer decisionId) {
		this.decisionId = decisionId;
	}

	public Timestamp getTimestamp() {
		return timestamp;
	}

	public void setTimestamp(Timestamp timestamp) {
		this.timestamp = timestamp;
	} 

	public void print() {
		StringBuffer sb = new StringBuffer();
		sb.append("id="+this.id+"\tdecisionId="+this.decision.getId()+"\tdecisionType="+this.decision.getDecisionType()+"\tdetail="+this.detail+"\ttimestamp="+this.timestamp);
		System.out.println(sb.toString());
	}
}
