/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.object;

import java.io.Serializable;

/**
 * Created by BWintemberg on 8/10/2015.
 */
@SuppressWarnings("serial")
public class AnomalyNormalEntryDTO implements Serializable {
    private long id;

    private short sequenceNumber;

    private
    String targetValue;

    private
    double minCount;

    private
    double maxCount;

    private
    double meanCount;

    private
    double standardDeviation;

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

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

    public AnomalyNormalEntryDTO() {
    }

    public AnomalyNormalEntryDTO(long id, short sequenceNumber, String targetValue, double minCount, double maxCount,
                                 double meanCount, double standardDeviation) {
        this.id = id;
        this.sequenceNumber = sequenceNumber;
        this.targetValue = targetValue;
        this.minCount = minCount;
        this.maxCount = maxCount;
        this.meanCount = meanCount;
        this.standardDeviation = standardDeviation;
    }
}
