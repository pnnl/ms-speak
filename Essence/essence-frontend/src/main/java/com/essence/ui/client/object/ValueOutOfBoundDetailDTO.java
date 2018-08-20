/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.object;

import java.io.Serializable;

import javax.persistence.Column;
import javax.persistence.EmbeddedId;
import javax.persistence.Entity;
import javax.persistence.Table;

import com.essence.multispeak.MSPServiceOperationKey;

@SuppressWarnings("serial")
public class ValueOutOfBoundDetailDTO  implements Serializable {
	protected VOOBKeyDTO key;

	private String targetValue; 

	// Field name in the formal of Version:ServiceCode:MessageName:FieldName, mainly for displaying purpose
	private String qualifiedFieldName; 

	private String xpath; 

	transient XpathDTO xpathObject = null;
	
	public VOOBKeyDTO getKey() {
		return key;
	}

	public void setKey(VOOBKeyDTO key) {
		this.key = key;
	}

	private String getQualifiedFieldName4Display() {
		if (qualifiedFieldName == null || qualifiedFieldName.isEmpty())
			return "";
		String[] parts = qualifiedFieldName.split(":");
		if (parts != null && parts.length > 3) {
			if (parts[0].equals(MSPServiceOperationKey.SUPPORTED_VERSION_5))
				return parts[1]+"(v5):"+parts[2]+": "+parts[3];
			else
				return parts[1]+"(v3):"+parts[2]+": "+parts[3];
		}
		else
			return qualifiedFieldName;
	}
	
	public String getDisplayDetails() {
		return getQualifiedFieldName4Display() + key.getOperator()+ targetValue;
	}
	
	public void print() {
		System.out.println("ruleId="+key.getRuleId()+"\txPathId="+key.getxPathId()+"\tdetails="+getDisplayDetails());
	}

	public String getTargetValue() {
		return targetValue;
	}

	public void setTargetValue(String targetValue) {
		this.targetValue = targetValue;
	}

	public String getQualifiedFieldName() {
		return qualifiedFieldName;
	}

	public void setQualifiedFieldName(String qualifiedFieldName) {
		this.qualifiedFieldName = qualifiedFieldName;
	}

	public String getVersion() {
		if (qualifiedFieldName == null || qualifiedFieldName.isEmpty())
			return "";
		
		String[] parts = qualifiedFieldName.split(":");
		if (parts != null && parts.length > 3)
			return parts[0];
		return qualifiedFieldName;
	}

	public String getEndpointCode() {
		if (qualifiedFieldName == null || qualifiedFieldName.isEmpty())
			return "";
/*
		int idx = qualifiedFieldName.indexOf(":");
		if (idx > -1)
			return qualifiedFieldName.substring(0, idx);
		else
			return qualifiedFieldName;
			*/
		
		String[] parts = qualifiedFieldName.split(":");
		if (parts != null && parts.length > 3)
			return parts[1];
		return qualifiedFieldName;
	}
	
	public String getMessageName() {
		if (qualifiedFieldName == null || qualifiedFieldName.isEmpty())
			return "";
		String[] parts = qualifiedFieldName.split(":");
		if (parts != null && parts.length > 3)
			return parts[2];
		return qualifiedFieldName;
	}
	
	public String getFieldName() {
		if (qualifiedFieldName == null || qualifiedFieldName.isEmpty())
			return "";
		String[] parts = qualifiedFieldName.split(":");
		if (parts != null && parts.length > 3)
			return parts[3];
		return qualifiedFieldName;
	}

	public String getXpath() {
		return xpath;
	}

	public void setXpath(String xpath) {
		this.xpath = xpath;
	}

	public XpathDTO getXpathObject() {
		return xpathObject;
	}

	public void setXpathObject(XpathDTO xpathObject) {
		this.xpathObject = xpathObject;
	}

    public ValueOutOfBoundDetailDTO(VOOBKeyDTO key, String targetValue, String qualifiedFieldName, String xpath, XpathDTO xpathObject) {
        this.key = key;
        this.targetValue = targetValue;
        this.qualifiedFieldName = qualifiedFieldName;
        this.xpath = xpath;
        this.xpathObject = xpathObject;
    }
    
    public ValueOutOfBoundDetailDTO() {
        
    }
}
