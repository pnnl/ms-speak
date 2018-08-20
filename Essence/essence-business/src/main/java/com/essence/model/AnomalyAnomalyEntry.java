/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;

import javax.persistence.*;

import com.essence.model.Anomaly;

import java.io.Serializable;

/**
 * Created by BWintemberg on 8/10/2015.
 */
@SuppressWarnings("serial")
@Entity
@Table(name="anomaly_anomalyentry")
public class AnomalyAnomalyEntry implements Serializable {
    @Id
    @GeneratedValue
    private long id;

    @ManyToOne
    @JoinColumn(name="anomalyid", nullable=false)//, insertable=false, updatable=false)
    private Anomaly anomaly;

    @Column(name = "sequence_number")
    private short sequenceNumber;

    @Column(name = "target_value")
    private String targetValue;

    //@Column(name = "feature_value")
    @Transient
    private String featureValue;

    private int count;

    public AnomalyAnomalyEntry() {
    }

//    public AnomalyAnomalyEntry(long id, short sequenceNumber, String targetValue, int count) {
//        this.id = id;
//            this.sequenceNumber = sequenceNumber;
//        this.targetValue = targetValue;
//        this.count = count;
//    }

    public AnomalyAnomalyEntry(long id, short sequenceNumber, String featureValue, int count) {
        this.id = id;
        this.sequenceNumber = sequenceNumber;
        this.featureValue = featureValue;
        this.count = count;
    }

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

    public String getFeatureValue() {
        return featureValue;
    }

    public void setFeatureValue(String featureValue) {
        this.featureValue = featureValue;
    }

    public void setAnomaly(Anomaly anomaly) {
        this.anomaly = anomaly;
    }
}
