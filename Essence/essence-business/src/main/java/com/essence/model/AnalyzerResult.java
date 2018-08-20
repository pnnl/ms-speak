/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;

import org.hibernate.annotations.Fetch;
import org.hibernate.annotations.FetchMode;

import javax.persistence.*;
import javax.xml.bind.annotation.XmlTransient;
import java.io.Serializable;
import java.sql.Timestamp;

@SuppressWarnings("serial")
@Entity
@Table(name = "analyzer_result")
public class AnalyzerResult implements Serializable {
	@Id  @GeneratedValue
	@Column(name = "id")
	private Long	   id;

    @OneToOne()
    @JoinColumn(name="alertid")
	@Fetch(FetchMode.JOIN)
    @XmlTransient
    private Alert alert;

	@Column(name = "time_stamp", nullable = false)
	private Timestamp timeStamp;

	@Column(name = "run_time")
	private	Long runTime;

	@Column(name = "detector_type")
	private String detectorType; // type of detection in categorization

	@Column(name = "src_ip_addr")
	private String srcIPAddress; 	// of packet / message, can be "ANY"
	
	@Column(name = "dst_ip_addr")
	private String dstIPAddress; 	// of packet / message, can be "ANY"
	
	@Column(name = "num_dos_pkts")
	private Integer numberOfPacketsForDoS;	// how many packets within the specific period to be considered DoS
	
	@Column(name = "time_win_seconds")
	private	Long timeWindowInSeconds;	// number of seconds for the detection time window
	
	@Column(name = "ref_rule_id")
	private Integer refRuleId;
	
	public void setAlert(Alert alert){
	    this.alert = alert;
	}
	
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

	public AnalyzerResult(Long runTime, String detectorType, String srcIPAddress, String dstIPAddress, Integer numberOfPacketsForDoS, Long timeWindowInSeconds, Integer refRuleId) {
		this.runTime = runTime;
		this.detectorType = detectorType;
		this.srcIPAddress = srcIPAddress;
		this.dstIPAddress = dstIPAddress;
		this.numberOfPacketsForDoS = numberOfPacketsForDoS;
		this.timeWindowInSeconds = timeWindowInSeconds;
		this.refRuleId = refRuleId;
	}

	public AnalyzerResult() {
	}
}
