/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.alert;

import java.io.Serializable;

@SuppressWarnings("serial")
public class AnomalyCause implements Serializable {
    private long anomalyId;
    private long causeId;
    private String cause;
    
    public long getAnomalyId() {
        return anomalyId;
    }
    public void setAnomalyId(long anomalyId) {
        this.anomalyId = anomalyId;
    }
    public long getCauseId() {
        return causeId;
    }
    public void setCauseId(long causeId) {
        this.causeId = causeId;
    }
    public String getCause() {
        return cause;
    }
    public void setCause(String cause) {
        this.cause = cause;
    }
}
