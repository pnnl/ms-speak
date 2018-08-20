/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;

import com.essence.model.AnomalyState;
import com.essence.model.Cause;
import com.essence.util.DateAdapter;

import javax.xml.bind.annotation.adapters.XmlJavaTypeAdapter;
import java.util.Date;
import java.util.List;

/**
 * Created by BWintemberg on 8/11/2015.
 */
public class NewAnomaly {
    @XmlJavaTypeAdapter(DateAdapter.class)
    private Date detectionTimeWindowStart;

    @XmlJavaTypeAdapter(DateAdapter.class)
    private Date detectionTimeWindowEnd;

    @XmlJavaTypeAdapter(DateAdapter.class)
    private Date trainingTimeWindowStart;

    @XmlJavaTypeAdapter(DateAdapter.class)
    private Date trainingTimeWindowEnd;

    private int sourceType;

    private String sourceValue;

    private int targetType;

    private String algorithm;

    private double score;

    private List<Integer> patternIndex;
    private List<NewAnomalyNormalEntry> normalEntries;

    private List<NewAnomalyAnomalyEntry> anomalyEntries;

//    private List<Cause> predictedCauses;
//
//    private List<AnomalyState> predictedStates;

    private List<AnomalyPrediction> predictions;

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

    public int getSourceType() {
        return sourceType;
    }

    public void setSourceType(int sourceType) {
        this.sourceType = sourceType;
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

    public List<NewAnomalyNormalEntry> getNormalEntries() {
        return normalEntries;
    }

    public void setNormalEntries(List<NewAnomalyNormalEntry> normalEntries) {
        this.normalEntries = normalEntries;
    }

    public List<NewAnomalyAnomalyEntry> getAnomalyEntries() {
        return anomalyEntries;
    }

    public void setAnomalyEntries(List<NewAnomalyAnomalyEntry> anomalyEntries) {
        this.anomalyEntries = anomalyEntries;
    }

    public List<AnomalyPrediction> getPredictions() {
        return predictions;
    }

    public void setPredictions(List<AnomalyPrediction> predictions) {
        this.predictions = predictions;
    }

    public double getScore() {
        return score;
    }

    public void setScore(double score) {
        this.score = score;
    }
}
