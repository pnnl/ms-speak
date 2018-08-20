/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.multispeak;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.EmbeddedId;
import javax.persistence.Table;

import java.io.Serializable;

@SuppressWarnings("serial")
@Entity
@Table(name = "msp_service_op")
public class MSPServiceOperation implements Serializable
{    
	@EmbeddedId    
	protected MSPServiceOperationKey servicePK;
	
	@Column(name="service_cd")    
	private String serviceCode;        
	
	@Column(name="input_msg")    
	private String inputMessageElement;        

	@Column(name="output_msg")    
	private String outputMessageElement;        

	@Column(name="soap_action")    
	private String soapAction;        

	@Column(name="soap_req_hdr_msg")    
	private String soapRequestHeaderMessage;        

	@Column(name="soap_req_hdr_part")    
	private String soapRequestHeaderPart;        
	
	@Column(name="soap_resp_hdr_msg")    
	private String soapResponseHeaderMessage;        

	@Column(name="soap_resp_hdr_part")    
	private String soapResponseHeaderPart;        

	public MSPServiceOperationKey getServicePK() {
		return servicePK;
	}

	public void setServicePK(MSPServiceOperationKey servicePK) {
		this.servicePK = servicePK;
	}

	public String getServiceCode() {
		return serviceCode;
	}

	public void setServiceCode(String serviceCode) {
		this.serviceCode = serviceCode;
	}

	public String getInputMessage() {
		return inputMessageElement;
	}

	public void setInputMessage(String inputMessage) {
		this.inputMessageElement = inputMessage;
	}

	public String getOutputMessage() {
		return outputMessageElement;
	}

	public void setOutputMessage(String outputMessage) {
		this.outputMessageElement = outputMessage;
	}

	public String getSoapAction() {
		return soapAction;
	}

	public void setSoapAction(String soapAction) {
		this.soapAction = soapAction;
	}

	public String getSoapRequestHeaderMessage() {
		return soapRequestHeaderMessage;
	}

	public void setSoapRequestHeaderMessage(String soapRequestHeaderMessage) {
		this.soapRequestHeaderMessage = soapRequestHeaderMessage;
	}

	public String getInputMessageElement() {
		return inputMessageElement;
	}

	public void setInputMessageElement(String inputMessageElement) {
		this.inputMessageElement = inputMessageElement;
	}

	public String getOutputMessageElement() {
		return outputMessageElement;
	}

	public void setOutputMessageElement(String outputMessageElement) {
		this.outputMessageElement = outputMessageElement;
	}

	public String getSoapRequestHeaderPart() {
		return soapRequestHeaderPart;
	}

	public void setSoapRequestHeaderPart(String soapRequestHeaderPart) {
		this.soapRequestHeaderPart = soapRequestHeaderPart;
	}

	public String getSoapResponseHeaderMessage() {
		return soapResponseHeaderMessage;
	}

	public void setSoapResponseHeaderMessage(String soapResponseHeaderMessage) {
		this.soapResponseHeaderMessage = soapResponseHeaderMessage;
	}

	public String getSoapResponseHeaderPart() {
		return soapResponseHeaderPart;
	}

	public void setSoapResponseHeaderPart(String soapResponseHeaderPart) {
		this.soapResponseHeaderPart = soapResponseHeaderPart;
	}

	public void setServiceCodeFromName(String serviceName) {
		if (serviceName == null)
			return;
		
		int idx = serviceName.indexOf("_");
		if (idx > -1)
			this.serviceCode = serviceName.substring(0, idx);
		else
			this.serviceCode = serviceName;		
	}
	
	public void print() {
		System.out.print("\tServiceName = " + servicePK.getServiceName());
		System.out.print("\tVersion = " + servicePK.getVersion());
		System.out.print("\tOperationName = " + servicePK.getOperationName());
		System.out.print("\tserviceCode = " + serviceCode);
		System.out.print("\tinputMessageElement = " + inputMessageElement);
		System.out.print("\toutputMessageElement = " + outputMessageElement);
		System.out.print("\tsoapAction= " + soapAction);
		System.out.print("\tsoapRequestHeaderMessage = " + soapRequestHeaderMessage);		
		System.out.println("\tsoapRequestHeaderPart = " + soapRequestHeaderPart);		
		System.out.print("\tsoapResponseHeaderMessage = " + soapResponseHeaderMessage);		
		System.out.println("\tsoapResponseHeaderPart = " + soapResponseHeaderPart);		// what's used in the xml
	}	
}