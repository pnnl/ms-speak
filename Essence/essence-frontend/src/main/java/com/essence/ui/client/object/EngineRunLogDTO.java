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
public class EngineRunLogDTO implements Serializable {
	private int id;

	private	Long runTime;

	private Long cutoffTime; 

	private String description;
	
	public int getId() {
		return id;
	}
	
// removed setId method, should not be called since id
// is auto-incremented in the database and should not 
// be changed by the user.
	
	public Long getRunTime() {
		return runTime;
	}
	
	public void setRunTime(Long runtime) {
		this.runTime = runtime;
	}
	
	public Long getCutoffTime() {
		return cutoffTime;
	}
	
	public void setCutoffTime(Long cutofftime) {
		this.cutoffTime = cutofftime;
	}
	
	public String getDescription() {
		return description;
	}
	
	public void setDescription(String description) {
		this.description = description;
	}

	public void print() {
		StringBuffer sb = new StringBuffer();
		sb.append("id= "+this.id+"\truntime= "+this.runTime+"\tCutoffTime= "+this.cutoffTime+"\tdescription= "+this.description);
		System.out.println(sb.toString());
	}

	public EngineRunLogDTO(int id, Long runTime, Long cutoffTime, String description) {
		this.id = id;
		this.runTime = runTime;
		this.cutoffTime = cutoffTime;
		this.description = description;
	}

	public EngineRunLogDTO() {
	}
}
