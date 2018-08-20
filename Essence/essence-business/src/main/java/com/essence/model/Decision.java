/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;

import com.essence.model.Alert;

import java.io.Serializable;
import java.util.Date;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.OneToOne;
import javax.persistence.Table;

@SuppressWarnings("serial")
@Entity
@Table(name = "decision")
public class Decision  implements Serializable {
	@Id @GeneratedValue
	@Column(name = "id")
	private int	   id;
	
	@Column(name = "decision_type")
	private String decisionType; // type of decision rule in categorization, ref DecisionRuleType

	@Column(name = "src_ip_addr") // if decision impact source host
	private String sourceIPAddress; 
	
	@Column(name = "dst_ip_addr") // if decision impact destination host
	private String destinationIPAddress; 
	
	@Column(name = "memo") // content for notification, or decisionType for manual action ref DecisionRuleTyp
	private String memo; 

	@Column(name = "issue_id", insertable=false, updatable=false) // alert id
	private Long issueId; 
	
	@Column(name = "decision_rule_ref")	// decision rule id
	private Integer decisionRuleId;
	
	@Column(name = "status")	// ref DecisionStatusType
	private String status;
	
	@ManyToOne()
	@JoinColumn(name = "causeid")
	private Cause cause;

    @ManyToOne(cascade=CascadeType.ALL)
    @JoinColumn(name = "classificationid")
	private Classification classification;
	
	@Column(name = "decision_time")
	private Date decisionTime;
	
	@Column(name = "username")
	private String username;

	@ManyToOne()
	@JoinColumn(name = "stateid")
	private AnomalyState anomalyState;

    @OneToOne(fetch=FetchType.EAGER)
    @JoinColumn(name="issue_id")
    private Alert issue;

	public Decision(int id, String decisionType, String sourceIPAddress, String destinationIPAddress, String memo,
					Long issueId, Integer decisionRuleId, String status, Cause cause,
					Classification classification, Date decisionTime, String username, AnomalyState anomalyState,
					Alert issue) {
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

	public Decision() {
	}
	//private AnalyzerResult issue;

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

	public Alert getIssue() {
		return issue;
	}

	public void setIssue(Alert issue) {
		this.issueId = issue.getId();
		this.issue = issue;
	}

    public Cause getCause() {
        return cause;
    }

    public void setCause(Cause cause) {
        this.cause = cause;
    }

    public Classification getClassification() {
        return classification;
    }

    public void setClassification(Classification classification) {
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

	public AnomalyState getAnomalyState() {
		return anomalyState;
	}

	public void setAnomalyState(AnomalyState anomalyState) {
		this.anomalyState = anomalyState;
	}
}
