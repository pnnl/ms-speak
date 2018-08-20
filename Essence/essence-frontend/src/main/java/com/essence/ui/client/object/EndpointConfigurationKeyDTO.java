/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.object;

import java.io.Serializable;

import javax.persistence.Column;
import javax.persistence.Embeddable;

@SuppressWarnings("serial")
public class EndpointConfigurationKeyDTO implements Serializable {
	@Column(name = "host_ip_addr")
	private String	   hostIPAddress;
	
	@Column(name = "organization_id")
	private int	   organizationId = -1;

	public String getHostIPAddress() {
		return hostIPAddress;
	}

	public void setHostIPAddress(String hostIPAddress) {
		this.hostIPAddress = hostIPAddress;
	}

	public int getOrganizationId() {
		return organizationId;
	}

	public void setOrganizationId(int organizationId) {
		this.organizationId = organizationId;
	}

	public EndpointConfigurationKeyDTO(String hostIPAddress, int organizationId) {
		this.hostIPAddress = hostIPAddress;
		this.organizationId = organizationId;
	}

	public EndpointConfigurationKeyDTO() {
	}
}