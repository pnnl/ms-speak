/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;

/**
 * Created by BWintemberg on 8/11/2015.
 */
public class NewAnomalyNormalEntry {
    private short sequenceNumber;

    private String targetValue;

    private
    double minCount;

    private
    double maxCount;

    private
    double meanCount;

    private
    double standardDeviation;

    public short getSequenceNumber() {
        return sequenceNumber;
    }

    public void setSequenceNumber(short value) {
        sequenceNumber = value;
    }

    public String getTargetValue() {
        return targetValue;
    }

    public void setTargetValue(String targetValue) {
        this.targetValue = targetValue;
    }

    public double getMinCount() {
        return minCount;
    }

    public void setMinCount(double minCount) {
        this.minCount = minCount;
    }

    public double getMaxCount() {
        return maxCount;
    }

    public void setMaxCount(double maxCount) {
        this.maxCount = maxCount;
    }

    public double getMeanCount() {
        return meanCount;
    }

    public void setMeanCount(double meanCount) {
        this.meanCount = meanCount;
    }

    public double getStandardDeviation() {
        return standardDeviation;
    }

    public void setStandardDeviation(double standardDeviation) {
        this.standardDeviation = standardDeviation;
    }
}
