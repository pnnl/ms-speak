/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;


import javax.persistence.*;
import java.io.Serializable;
import java.util.List;
/* TO-DO deleted state and retrieve active vs. deleted */

@SuppressWarnings("serial")
@Entity
@Table(name = "detection_rule")
public class DetectionRule implements Serializable {
	@Id @GeneratedValue
	@Column(name = "rule_id")
	private int	   id;

	@Column(name = "organization_id")
	private int	   organizationId = -1;

	@Column(name = "rule_type")
	private String ruleType; // type of detection rule in categorization

	@Column(name = "src_endpoint_type")
	private String srcEndpointType; // MultiSpeak endpoint type, can be "ANY"
	
	@Column(name = "dst_endpoint_type")
	private String dstEndpointType; // MultiSpeak endpoint type, can be "ANY"
	
	@Column(name = "version")
	private String version; // MultiSpeak version for the endpoint

	@Column(name = "action_type")
	private String actionType; 		// Allowed or Disallowed
	
	@Column(name = "src_ip_addr")
	private String srcIPAddress; 	// of packet / message, can be "ANY"
	
	@Column(name = "dst_ip_addr")
	private String dstIPAddress; 	// of packet / message, can be "ANY"
	
	@Column(name = "num_dos_pkts")
	private Integer numberOfPacketsForDoS;	// how many packets within the specific period to be considered DoS
	
	@Column(name = "time_win_seconds")
	private	Long timeWindowInSeconds;	// number of seconds for the detection time window
	
	@Column(name = "priority")
	private Integer priority;	// priority default to 99999
	
	@Column(name = "voob_title")
	private String voobTitle; 	

	transient List<ValueOutOfBoundDetail> voobDetails = null;
	transient String policyDescription = null;
	
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	
	public String getSrcEndpointType() {
		return srcEndpointType;
	}
	public void setSrcEndpointType(String srcEndpointType) {
		this.srcEndpointType = srcEndpointType;
	}
	public String getDstEndpointType() {
		return dstEndpointType;
	}
	public void setDstEndpointType(String dstEndpointType) {
		this.dstEndpointType = dstEndpointType;
	}
	public String getActionType() {
		return actionType;
	}
	public void setActionType(String actionType) {
		this.actionType = actionType;
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
	
	public String getRuleType() {
		return ruleType;
	}
	public void setRuleType(DetectionRuleType ruleType) {
		this.ruleType = ruleType.toString();
	}
	public void setRuleType(String ruleType) {
		this.ruleType = ruleType;
	}
	public Integer getPriority() {
		return priority;
	}
	public void setPriority(Integer priority) {
		this.priority = priority;
	}
	public List<ValueOutOfBoundDetail> getVoobDetails() {
		return voobDetails;
	}
	public void setVoobDetails(List<ValueOutOfBoundDetail> voobDetails) {
		this.voobDetails = voobDetails;
	}
	/*
	 * return the index of the element that contains a more accurate message name, not just the header's "ALL"
	 */
	public int getNonHeaderIndexOfVooBDetails() {
		int msgIdx = 0;
		if (voobDetails != null) {
    		for (msgIdx=0; msgIdx<voobDetails.size(); msgIdx++) {
    			if (!voobDetails.get(msgIdx).getEndpointCode().equals(Xpath.HEADER_SERVICE_CD))
    				break;
    		}
    		if (msgIdx >= voobDetails.size())
    			msgIdx = 0; // header only rule
		}

		return msgIdx;
	}
	
	public String getVoobTitle() {
		return voobTitle;
	}
	public void setVoobTitle(String voobTitle) {
		this.voobTitle = voobTitle;
	}
	public String getVersion() {
		return version;
	}
	public void setVersion(String version) {
		this.version = version;
	}
	public int getOrganizationId() {
		return organizationId;
	}
	public void setOrganizationId(int organizationId) {
		this.organizationId = organizationId;
	}
	public String getPolicyDescription() {
		return policyDescription;
	}
	public void setPolicyDescription(String policyDescription) {
		this.policyDescription = policyDescription;
	}
	public void print() {
		StringBuffer sb = new StringBuffer();
		sb.append("id="+id+"\truleType="+this.ruleType+"\tMSP version="+this.version+"\tsrcEndpointType="+this.srcEndpointType+"\tdstEndpointType="+this.dstEndpointType+"\tactionType="+this.actionType+"\tpriority="+priority);
		sb.append("\tsrcIPAddress="+this.srcIPAddress+"\tdstIPAddress="+this.dstIPAddress+"\tnumberOfPacketsForDoS="+this.numberOfPacketsForDoS+"\ttimeWindowInSeconds="+this.timeWindowInSeconds);
		if (voobDetails != null && !voobDetails.isEmpty())
			for (ValueOutOfBoundDetail d : voobDetails)
				sb.append("\t" + d.getDisplayDetails());
		System.out.println(sb.toString());
	}

	public DetectionRule(int organizationId, String ruleType, String srcEndpointType, String dstEndpointType, String version, String actionType, String srcIPAddress, String dstIPAddress, Integer numberOfPacketsForDoS, Long timeWindowInSeconds, Integer priority, String voobTitle, List<ValueOutOfBoundDetail> voobDetails, String policyDescription) {
		this.organizationId = organizationId;
		this.ruleType = ruleType;
		this.srcEndpointType = srcEndpointType;
		this.dstEndpointType = dstEndpointType;
		this.version = version;
		this.actionType = actionType;
		this.srcIPAddress = srcIPAddress;
		this.dstIPAddress = dstIPAddress;
		this.numberOfPacketsForDoS = numberOfPacketsForDoS;
		this.timeWindowInSeconds = timeWindowInSeconds;
		this.priority = priority;
		this.voobTitle = voobTitle;
		this.voobDetails = voobDetails;
		this.policyDescription = policyDescription;
	}

	public DetectionRule() {
	}
}
