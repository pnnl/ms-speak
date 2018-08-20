/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.object;

import java.io.Serializable;
import java.sql.Timestamp;

@SuppressWarnings("serial")
public class ActionDTO implements Serializable {
	private int	   id;

	private String detail; 

	private Integer decisionId;

	private Timestamp timestamp;

    private DecisionDTO decision;

	public ActionDTO(int id, String detail, Integer decisionId, Timestamp timestamp, DecisionDTO decision) {
		this.id = id;
		this.detail = detail;
		this.decisionId = decisionId;
		this.timestamp = timestamp;
		this.decision = decision;
	}

	public ActionDTO() {
	}

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

	public DecisionDTO getDecision() {
		return decision;
	}

	public void setDecision(DecisionDTO decision) {
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
