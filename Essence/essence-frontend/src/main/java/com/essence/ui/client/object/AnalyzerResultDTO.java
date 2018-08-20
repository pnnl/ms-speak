/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.object;

import com.essence.model.Alert;

import java.io.Serializable;
import java.sql.Timestamp;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToOne;
import javax.persistence.Table;
import javax.xml.bind.annotation.XmlTransient;

@SuppressWarnings("serial")
public class AnalyzerResultDTO implements Serializable {
	public AnalyzerResultDTO(Long id, Long runTime, String detectorType, String srcIPAddress, String dstIPAddress,
							 Integer numberOfPacketsForDoS, Long timeWindowInSeconds, Integer refRuleId, Timestamp timestamp) {
		this.id = id;
		this.runTime = runTime;
		this.detectorType = detectorType;
		this.srcIPAddress = srcIPAddress;
		this.dstIPAddress = dstIPAddress;
		this.numberOfPacketsForDoS = numberOfPacketsForDoS;
		this.timeWindowInSeconds = timeWindowInSeconds;
		this.refRuleId = refRuleId;
		this.timeStamp = timestamp;
	}

	public AnalyzerResultDTO() {
	}

	private Long	   id;

	private Timestamp timeStamp;

	private	Long runTime;

	private String detectorType; // type of detection in categorization

	private String srcIPAddress; 	// of packet / message, can be "ANY"

	private String dstIPAddress; 	// of packet / message, can be "ANY"

	private Integer numberOfPacketsForDoS;	// how many packets within the specific period to be considered DoS

	private	Long timeWindowInSeconds;	// number of seconds for the detection time window

	private Integer refRuleId;
	
	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public Timestamp getTimeStamp() {
		return timeStamp;
	}

	public void setTimeStamp(Timestamp timeStamp) {
		this.timeStamp = timeStamp;
	}

	public Long getRunTime() {
		return runTime;
	}

	public void setRunTime(Long runTime) {
		this.runTime = runTime;
	}

	public String getDetectorType() {
		return detectorType;
	}

	public void setDetectorType(String detectorType) {
		this.detectorType = detectorType;
	}

	public String getSrcIPAddress() {
		return srcIPAddress;
	}

	public void setSrcIPAddress(String srcIPAddress) {
		this.srcIPAddress = srcIPAddress;
	}

	public String getDstIPAddress() {
		return dstIPAddress;
	}

	public void setDstIPAddress(String dstIPAddress) {
		this.dstIPAddress = dstIPAddress;
	}

	public Integer getNumberOfPacketsForDoS() {
		return numberOfPacketsForDoS;
	}

	public void setNumberOfPacketsForDoS(Integer numberOfPacketsForDoS) {
		this.numberOfPacketsForDoS = numberOfPacketsForDoS;
	}

	public Long getTimeWindowInSeconds() {
		return timeWindowInSeconds;
	}

	public void setTimeWindowInSeconds(Long timeWindowInSeconds) {
		this.timeWindowInSeconds = timeWindowInSeconds;
	}

	public Integer getRefRuleId() {
		return refRuleId;
	}

	public void setRefRuleId(Integer refRuleId) {
		this.refRuleId = refRuleId;
	}

    public void print() {
		StringBuffer sb = new StringBuffer();
//		sb.append("id="+this.id+"\tdetectorType="+this.detectorType+"\trefRuleId="+this.refRuleId+"\truntime=");
//		sb.append(this.runTime+"\tdescription="+this.description+"\tsrcIPAddress="+this.srcIPAddress+"\tdstIPAddress=");
//		sb.append(this.dstIPAddress+"\tnumberOfPacketsForDoS="+this.numberOfPacketsForDoS+"\ttimeWindowInSeconds=");
//		sb.append(this.timeWindowInSeconds+"\tseverity="+this.severity + "\tstatus="+this.status + "\tpolicyId=");
//		sb.append(this.organizationId);
		System.out.println(sb.toString());
	}
}
