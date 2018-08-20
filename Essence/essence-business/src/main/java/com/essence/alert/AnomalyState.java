/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.alert;

public class AnomalyState {
    private long anomalyId;
    private long stateId;
    private String state;
    
    public long getAnomalyId() {
        return anomalyId;
    }
    public void setAnomalyId(long anomalyId) {
        this.anomalyId = anomalyId;
    }
    public long getStateId() {
        return stateId;
    }
    public void setStateId(long stateId) {
        this.stateId = stateId;
    }
    public String getState() {
        return state;
    }
    public void getState(String state) {
        this.state = state;
    }
}