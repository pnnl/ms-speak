/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;

import com.essence.model.Cause;
import com.essence.util.DateAdapter;

import javax.xml.bind.annotation.adapters.XmlJavaTypeAdapter;
import java.util.Date;
import java.util.List;

/**
 * Created by BWintemberg on 8/11/2015.
 */
public class AnomalyResult {
    private long alertId;

    @XmlJavaTypeAdapter(DateAdapter.class)
    private Date detectionTimeWindowStart;

    @XmlJavaTypeAdapter(DateAdapter.class)
    private Date detectionTimeWindowEnd;

    @XmlJavaTypeAdapter(DateAdapter.class)
    private Date trainingTimeWindowStart;

    @XmlJavaTypeAdapter(DateAdapter.class)
    private Date trainingTimeWindowEnd;

    private String sourceValue;

    private int targetType;

    private String algorithm;

    private double score;

    private List<Integer> patternIndex;

    private List<NewAnomalyAnomalyEntry> anomalyEntries;

    private Cause userCause;

    private AnomalyState userState;

    public Date getDetectionTimeWindowStart() {
        return detectionTimeWindowStart;
    }

    public void setDetectionTimeWindowStart(Date detectionTimeWindowStart) {
        this.detectionTimeWindowStart = detectionTimeWindowStart;
    }

    public Date getDetectionTimeWindowEnd() {
        return detectionTimeWindowEnd;
    }

    public void setDetectionTimeWindowEnd(Date detectionTimeWindowEnd) {
        this.detectionTimeWindowEnd = detectionTimeWindowEnd;
    }

    public Date getTrainingTimeWindowStart() {
        return trainingTimeWindowStart;
    }

    public void setTrainingTimeWindowStart(Date trainingTimeWindowStart) {
        this.trainingTimeWindowStart = trainingTimeWindowStart;
    }

    public Date getTrainingTimeWindowEnd() {
        return trainingTimeWindowEnd;
    }

    public void setTrainingTimeWindowEnd(Date trainingTimeWindowEnd) {
        this.trainingTimeWindowEnd = trainingTimeWindowEnd;
    }

    public String getSourceValue() {
        return sourceValue;
    }

    public void setSourceValue(String sourceValue) {
        this.sourceValue = sourceValue;
    }

    public int getTargetType() {
        return targetType;
    }

    public void setTargetType(int targetType) {
        this.targetType = targetType;
    }

    public String getAlgorithm() {
        return algorithm;
    }

    public void setAlgorithm(String algorithm) {
        this.algorithm = algorithm;
    }

    public List<Integer> getPatternIndex() {
        return patternIndex;
    }

    public void setPatternIndex(List<Integer> patternIndex) {
        this.patternIndex = patternIndex;
    }

    public List<NewAnomalyAnomalyEntry> getAnomalyEntries() {
        return anomalyEntries;
    }

    public void setAnomalyEntries(List<NewAnomalyAnomalyEntry> anomalyEntries) {
        this.anomalyEntries = anomalyEntries;
    }

    public Cause getUserCause() {
        return userCause;
    }

    public void setUserCause(Cause cause) {
        this.userCause = cause;
    }

    public AnomalyState getUserState() {
        return userState;
    }

    public void setUserState(AnomalyState state) {
        this.userState = state;
    }

    public double getScore() {
        return score;
    }

    public void setScore(double score) {
        this.score = score;
    }

    public long getAlertId() {
        return alertId;
    }

    public void setAlertId(long alertId) {
        this.alertId = alertId;
    }
}
