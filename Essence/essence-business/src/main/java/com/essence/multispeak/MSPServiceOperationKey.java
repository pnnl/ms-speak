/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.multispeak;

import java.io.Serializable;

import javax.persistence.Column;
import javax.persistence.Embeddable;

@SuppressWarnings("serial")
@Embeddable
public class MSPServiceOperationKey implements Serializable {
	static public final String SUPPORTED_VERSION_3 = "v3ac"; // version 3 build ac
	static public final String SUPPORTED_VERSION_5 = "v503"; // version 5.03
	
	@Column(name = "service_name", nullable = false)    
	private String serviceName;    
	
	@Column(name = "op_name", nullable = false)    
	private String operationName;

	@Column(name = "version", nullable = false)    
	private String version;

	public String getServiceName() {
		return serviceName;
	}

	public void setServiceName(String eerviceName) {
		this.serviceName = eerviceName;
	}

	public String getOperationName() {
		return operationName;
	}

	public void setOperationName(String operationName) {
		this.operationName = operationName;
	}

	public String getVersion() {
		return version;
	}

	public void setVersion(String version) {
		this.version = version;
	}
	
}
