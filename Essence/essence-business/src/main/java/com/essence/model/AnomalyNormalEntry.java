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
@Table(name="anomaly_normalentry")
public class AnomalyNormalEntry implements Serializable {
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

    @Column(name = "min_count")
    private
    double minCount;

    @Column(name = "max_count")
    private
    double maxCount;

    @Column(name = "mean_count")
    private
    double meanCount;

    @Column(name = "standard_deviation")
    private
    double standardDeviation;

    public AnomalyNormalEntry() {
    }

//    public AnomalyNormalEntry(long id, short sequenceNumber, String targetValue, double minCount,
//                              double maxCount, double meanCount, double standardDeviation) {
//        this.id = id;
//        this.sequenceNumber = sequenceNumber;
//        this.targetValue = targetValue;
//        this.minCount = minCount;
//        this.maxCount = maxCount;
//        this.meanCount = meanCount;
//        this.standardDeviation = standardDeviation;
//    }

    public AnomalyNormalEntry(long id, short sequenceNumber, String featureValue, double minCount,
                              double maxCount, double meanCount, double standardDeviation) {
        this.id = id;
        this.sequenceNumber = sequenceNumber;
        this.targetValue = targetValue;
        this.minCount = minCount;
        this.maxCount = maxCount;
        this.meanCount = meanCount;
        this.standardDeviation = standardDeviation;
        this.featureValue = featureValue;
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
