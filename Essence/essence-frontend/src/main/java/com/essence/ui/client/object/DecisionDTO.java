/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.object;

import java.io.Serializable;
import java.util.Date;

import com.essence.model.AnomalyState;
import com.essence.model.Cause;
import com.essence.model.Classification;

@SuppressWarnings("serial")
public class DecisionDTO implements Serializable {
	private int	   id;

	private String decisionType; // type of decision rule in categorization, ref DecisionRuleType

	private String sourceIPAddress; 

	private String destinationIPAddress; 

	private String memo; 

	private Long issueId; 

	private Integer decisionRuleId;

	private String status;

	private CauseDTO cause;

	private ClassificationDTO classification;

	private Date decisionTime;

	private String username;

	private AnomalyStateDTO anomalyState;

    private AlertDTO issue;

	public DecisionDTO(int id, String decisionType, String sourceIPAddress, String destinationIPAddress, String memo,
					   Long issueId, Integer decisionRuleId, String status, CauseDTO cause,
					   ClassificationDTO classification, Date decisionTime, String username, AnomalyStateDTO anomalyState,
					   AlertDTO issue) {
		this.id = id;
		this.decisionType = decisionType;
		this.sourceIPAddress = sourceIPAddress;
		this.destinationIPAddress = destinationIPAddress;
		this.memo = memo;
		this.issueId = issueId;
		this.decisionRuleId = decisionRuleId;
		this.status = status;
		this.cause = cause;
		this.classification = classification;
		this.decisionTime = decisionTime;
		this.username = username;
		this.anomalyState = anomalyState;
		this.issue = issue;
	}

	public DecisionDTO() {
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getDecisionType() {
		return decisionType;
	}

	public void setDecisionType(String decisionType) {
		this.decisionType = decisionType;
	}

	public String getSourceIPAddress() {
		return sourceIPAddress;
	}

	public void setSourceIPAddress(String sourceIPAddress) {
		this.sourceIPAddress = sourceIPAddress;
	}

	public String getDestinationIPAddress() {
		return destinationIPAddress;
	}

	public void setDestinationIPAddress(String destinationIPAddress) {
		this.destinationIPAddress = destinationIPAddress;
	}

	public String getMemo() {
		return memo;
	}

	public void setMemo(String memo) {
		this.memo = memo;
	}

	public Long getIssueId() {
		return issueId;
	}

	public void setIssueId(Long issueId) {
		this.issueId = issueId;
	}

	public Integer getDecisionRuleId() {
		return decisionRuleId;
	}

	public void setDecisionRuleId(Integer decisionRuleId) {
		this.decisionRuleId = decisionRuleId;
	} 		

	public String getStatus() {
		return status;
	}

	public void setStatus(String status) {
		this.status = status;
	}

	public AlertDTO getIssue() {
		return issue;
	}

	public void setIssue(AlertDTO issue) {
		this.issueId = issue.getId();
		this.issue = issue;
	}

    public CauseDTO getCause() {
        return cause;
    }

    public void setCause(CauseDTO cause) {
        this.cause = cause;
    }

    public ClassificationDTO getClassification() {
        return classification;
    }

    public void setClassification(ClassificationDTO classification) {
        this.classification = classification;
    }

    public Date getDecisionTime() {
        return decisionTime;
    }

    public void setDecisionTime(Date decisionTime) {
        this.decisionTime = decisionTime;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void print() {
		StringBuffer sb = new StringBuffer();
		sb.append("id="+this.id+"\tdecisionType="+this.decisionType+"\tsourceIP="+this.sourceIPAddress+"\tdestIP="+this.destinationIPAddress+"\trefIssueId=" + this.issueId + "\trefRuleId=" + this.decisionRuleId + "\tmemo="+this.memo);
		System.out.println(sb.toString());
	}

	public AnomalyStateDTO getAnomalyState() {
		return anomalyState;
	}

	public void setAnomalyState(AnomalyStateDTO anomalyState) {
		this.anomalyState = anomalyState;
	}
}
