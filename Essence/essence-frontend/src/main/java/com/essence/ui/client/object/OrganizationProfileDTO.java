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
public class OrganizationProfileDTO  implements Serializable {
	@Id @GeneratedValue
	@Column(name = "id")
	private int	   id;

	private String description; 

	// 1- yes/true, 0 - no/false
	private boolean enabled;

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public boolean isEnabled() {
		return enabled;
	}

	public void setEnabled(boolean enabled) {
		this.enabled = enabled;
	} 		
	
	public void print() {
		StringBuffer sb = new StringBuffer();
		sb.append("id="+id+"\tdescription="+this.description+"\tenabled="+this.enabled);
		System.out.println(sb.toString());
	}

	public OrganizationProfileDTO(String description, boolean enabled) {
		this.description = description;
		this.enabled = enabled;
	}

	public OrganizationProfileDTO() {
	}
}
