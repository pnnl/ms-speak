/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.cmu;

public class NewAnomalyEntry {
    private String targetValue;
    private int count;
    
    public String getTargetValue() {
        return targetValue;
    }
    public void setTargetValue(String targetValue) {
        this.targetValue = targetValue;
    }
    public int getCount() {
        return count;
    }
    public void setCount(int count) {
        this.count = count;
    }
}
