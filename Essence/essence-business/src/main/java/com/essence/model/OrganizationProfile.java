/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;


import javax.persistence.*;
import java.io.Serializable;

@SuppressWarnings("serial")
@Entity
@Table(name = "organization")
public class OrganizationProfile implements Serializable {
	@Id @GeneratedValue
	@Column(name = "id")
	private int	   id;
	
	/*
	@Column(name = "policy_type") // ref PolicyType
	private String policyType1; 
	*/
	@Column(name = "description") 
	private String description; 
	
	@Column(name = "enabled")	// 1- yes/true, 0 - no/false
	private boolean enabled;

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}
/*
	public String getPolicyType1() {
		return policyType1;
	}

	public void setPolicyType(String policyType) {
		this.policyType1 = policyType;
	}
*/
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

	public OrganizationProfile(String description, boolean enabled) {
		this.description = description;
		this.enabled = enabled;
	}

	public OrganizationProfile() {
	}
}
