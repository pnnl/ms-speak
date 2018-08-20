/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.object;

// if changing this, please also add to hashmap in com.essence.services.DetectionRuleTypeResource
public enum DetectionRuleTypeDTO {
	VALUE_OUT_OF_BOUND,
	MS_EP_CONNECTIVITY,
	WRONG_MSG_TO_MS_EP,
	ERR_MSG_FROM_MS_EP,
	WRONG_MSG_FORMAT,
	DENIAL_OF_SERVICE,
	NW_SEGMENTATION,
	NEW_HOST,
	ANOMALY;
	
	static public DetectionRuleTypeDTO textToValue(String s) {
		if (s==null || s.isEmpty())
			return null;
		try {
			return DetectionRuleTypeDTO.valueOf(s);
		} catch (Exception ex) {
			return null;
		}
	}
}