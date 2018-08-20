/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.analysis;

import javax.persistence.Column;
import javax.persistence.Embeddable;

import java.sql.Timestamp;
import java.io.Serializable;

@SuppressWarnings("serial")
@Embeddable
public class PacketPK implements Serializable 
{    
	@Column(name = "source_addr", nullable = false)    
	private String sourceAddress;    
	
	@Column(name = "dest_addr", nullable = false)    
	private String destAddress;
	
	@Column(name = "time_stamp", nullable = false)    
	private Timestamp timeStamp;
	
	public String getSourceAddress()
	{
		return sourceAddress;
	}
	
	public void setSourceAddress(String sourceAddress)
	{
		this.sourceAddress = sourceAddress;
	}
	
	public String getDestAddress()
	{
		return destAddress;
	}
	
	public void setDestAddress(String destAddress)
	{
		this.destAddress = destAddress;
	}
	
	public Timestamp getTimeStamp()
	{
		return timeStamp;
	}
	
	public void setTimeStamp(Timestamp timeStamp)
	{
		this.timeStamp = timeStamp;
	}
}