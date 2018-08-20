/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.alert;

import java.io.Serializable;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.NamedNativeQuery;
import javax.persistence.Transient;

@SuppressWarnings("serial")
@Entity
@NamedNativeQuery(name = "alertCountQuery", 
resultClass = AlertCount.class,
query = "{call GetAlertCountByIP}")
public class AlertCount implements Serializable {
    private Long count;
    
    @Id
    @Column(name = "ip")
    private String ipAddress;
    
    @Transient
    private int severity;

    public Long getCount() {
        return count;
    }

    public void setCount(Long count) {
        this.count = count;
    }

    public String getIpAddress() {
        return ipAddress;
    }

    public void setIpAddress(String ipAddress) {
        this.ipAddress = ipAddress;
    }

    public int getSeverity() {
        return severity;
    }

    public void setSeverity(int severity) {
        this.severity = severity;
    }
}
