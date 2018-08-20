/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.action;

public class AttachmentPoint {
	String 	switchDPID;
	int		port;
	String	errorStatus;
	
	public String getSwitchDPID() {
		return switchDPID;
	}

	public void setSwitchDPID(String switchDPID) {
		this.switchDPID = switchDPID;
	}

	public int getPort() {
		return port;
	}

	public void setPort(int port) {
		this.port = port;
	}

	public String getErrorStatus() {
		return errorStatus;
	}

	public void setErrorStatus(String errorStatus) {
		this.errorStatus = errorStatus;
	}

	public String toString() {
		return "switchDPID="+switchDPID+" port="+port+" errorStatus="+errorStatus;
	}
}
