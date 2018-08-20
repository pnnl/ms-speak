/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.object;

import java.io.Serializable;

/**
 * Created by BWintemberg on 8/10/2015.
 */
@SuppressWarnings("serial")
public class AnomalyAnomalyEntryDTO implements Serializable {
    private long id;

    private short sequenceNumber;

    private String targetValue;

    private int count;

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

    public String getTargetValue() { return targetValue; }

    public void setTargetValue(String targetValue) {
        this.targetValue = targetValue;
    }

    public int getCount() { return count; }

    public void setCount(int count) { this.count = count; }

    public AnomalyAnomalyEntryDTO() {
    }

    public AnomalyAnomalyEntryDTO(long id, short sequenceNumber, String targetValue, int count) {
        this.id = id;
        this.sequenceNumber = sequenceNumber;
        this.targetValue = targetValue;
        this.count = count;
    }
}
