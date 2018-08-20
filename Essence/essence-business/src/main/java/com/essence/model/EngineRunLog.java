/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;


import javax.persistence.*;
import java.io.Serializable;

@SuppressWarnings("serial")
@Entity
@Table(name = "engine_run_log")
public class EngineRunLog implements Serializable {
	@Id  @GeneratedValue
	@Column(name = "id")
	private int id;

	@Column(name = "run_time")
	private	Long runTime;

	@Column(name = "cutoff_time")
	private Long cutoffTime; 

	@Column(name = "description")
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

	public EngineRunLog(Long runTime, Long cutoffTime, String description) {
		this.runTime = runTime;
		this.cutoffTime = cutoffTime;
		this.description = description;
	}

	public EngineRunLog() {
	}
}
