/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.object;

import java.io.Serializable;

@SuppressWarnings("serial")
public class MultiSpeakEndPointConnectivityRule implements Serializable {
	private DetectionRuleDTO genericDetectionRule;
	
	static public MultiSpeakEndPointConnectivityRule convert(DetectionRuleDTO rule) {
		MultiSpeakEndPointConnectivityRule r = new MultiSpeakEndPointConnectivityRule();
		r.genericDetectionRule = rule;
		r.genericDetectionRule.setRuleType(DetectionRuleTypeDTO.MS_EP_CONNECTIVITY);
		return r;
	}
	
	public MultiSpeakEndPointConnectivityRule() {
		genericDetectionRule = new DetectionRuleDTO();
		genericDetectionRule.setRuleType(DetectionRuleTypeDTO.MS_EP_CONNECTIVITY);
	}
	
	public DetectionRuleDTO getDetectionRule() {
		return genericDetectionRule;
	}
	
	public int getId() {
		return genericDetectionRule.getId();
	}
	public void setId(int id) {
		genericDetectionRule.setId(id);
	}

	public String getVersion() {
		return genericDetectionRule.getVersion();
	}
	public void setVersion(String version) {
		genericDetectionRule.setVersion(version);
	}

	public String getSrcEndpointType() {
		return genericDetectionRule.getSrcEndpointType();
	}
	public void setSrcEndpointType(String srcEndpointType) {
		genericDetectionRule.setSrcEndpointType(srcEndpointType);
	}
	public String getDstEndpointType() {
		return genericDetectionRule.getDstEndpointType();
	}
	public void setDstEndpointType(String dstEndpointType) {
		genericDetectionRule.setDstEndpointType(dstEndpointType);
	}
	public String getActionType() {
		return genericDetectionRule.getActionType();
	}
	public void setActionType(String actionType) {
		genericDetectionRule.setActionType(actionType);
	}
	
	public String getRuleType() {
		return genericDetectionRule.getRuleType();
	}
	public Integer getPriority() {
		return genericDetectionRule.getPriority();
	}
	public void setPriority(Integer priority) {
		genericDetectionRule.setPriority(priority);
	}
	public void print() {
		genericDetectionRule.print();
	}

	public void setOrganizationId(int id) {
		genericDetectionRule.setOrganizationId(id);
	}
	
	public int getOrganizationId() {
		return genericDetectionRule.getOrganizationId();
		
	}
}
