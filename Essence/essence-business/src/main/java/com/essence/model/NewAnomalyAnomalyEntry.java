/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;

/**
 * Created by BWintemberg on 8/11/2015.
 */
public class NewAnomalyAnomalyEntry {
    private short sequenceNumber;

    private String targetValue;

    private int count;

    public short getSequenceNumber() {
        return sequenceNumber;
    }

    public void setSequenceNumber(short value) {
        sequenceNumber = value;
    }

    public String getTargetValue() { return targetValue; }

    public void setTargetValue(String targetValue) {
        this.targetValue = targetValue;
    }

    public int getCount() { return count; }

    public void setCount(int count) { this.count = count; }
}
