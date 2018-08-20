/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.object;


import java.io.Serializable;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Table;

@SuppressWarnings("serial")
public class XpathDTO implements Serializable {
	static public final String HEADER_SERVICE_CD = "ALL";
	static public final String REQUEST_HEADER_MESSAGE_NAME = "MultiSpeakRequestMsgHeader";
	static public final String RESPONSE_HEADER_MESSAGE_NAME = "MultiSpeakResponseMsgHeader";
	static public final String HEADER_SIGNATURE_PATH = "/Envelope/Header/";
	static public final String REQUEST_HEADER_SIGNATURE_PATH = "/Envelope/Header/MultiSpeakRequestMsgHeader/";
	static public final String RESPONSE_HEADER_SIGNATURE_PATH = "/Envelope/Header/MultiSpeakResponseMsgHeader/";
	static public final String BODY_SIGNATURE_PATH = "/Envelope/Body/";
	
	static public final String REQ_RESP_HEADER_MESSAGE_NAME_V3 = "MultiSpeakMsgHeader";
	static public final String REQ_RESP_HEADER_SIGNATURE_PATH_V3 = "/Envelope/Header/MultiSpeakMsgHeader/";
	
	@Id @GeneratedValue
	@Column(name = "id")
	private int	   id;	
	
	@Column(name="service_cd")    
	private String serviceCode; 
	
	@Column(name="version")    
	private String version; 

	@Column(name="msg_name")    
	private String messageName; 
	
	@Column(name="xpath")    
	private String xpath; 

	@Column(name="field_name")    
	private String fieldName; 
	
	@Column(name="is_array")    
	private Boolean isArray;

	@Column(name="value_type")    
	private String valueType; // ref ValueType.java
	
	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getServiceCode() {
		return serviceCode;
	}

	public void setServiceCode(String serviceCode) {
		this.serviceCode = serviceCode;
	}

	public String getMessageName() {
		return messageName;
	}

	public void setMessageName(String messageName) {
		this.messageName = messageName;
	}

	public String getXpath() {
		return xpath;
	}

	public void setXpath(String xpath) {
		this.xpath = xpath;
	}

	public String getFieldName() {
		return fieldName;
	}

	public void setFieldName(String fieldName) {
		this.fieldName = fieldName;
	}

	public Boolean getIsArray() {
		return isArray;
	}

	public void setIsArray(Boolean isArray) {
		this.isArray = isArray;
	}
	
	public String getValueType() {
		return valueType;
	}

	public void setValueType(String valueType) {
		this.valueType = valueType;
	}

	public String getVersion() {
		return version;
	}

	public void setVersion(String version) {
		this.version = version;
	}

	public void print() {
		StringBuffer sb = new StringBuffer();
		sb.append("id="+this.id+"\tserviceCD="+this.serviceCode+"\tversion="+this.version+"\tmsgName="+this.messageName+"\tfieldName="+this.fieldName+"\txpath="+this.xpath+"\tisArray=" + this.isArray);
		System.out.println(sb.toString());
	}

	public XpathDTO(int id, String serviceCode, String version, String messageName, String xpath, String fieldName,
					Boolean isArray, String valueType) {
		this.id = id;
		this.serviceCode = serviceCode;
		this.version = version;
		this.messageName = messageName;
		this.xpath = xpath;
		this.fieldName = fieldName;
		this.isArray = isArray;
		this.valueType = valueType;
	}

	public XpathDTO() {
	}
}
