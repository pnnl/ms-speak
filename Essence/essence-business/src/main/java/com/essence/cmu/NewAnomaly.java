/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.cmu;

import java.io.Serializable;
import java.util.Date;
import java.util.List;

@SuppressWarnings("serial")
public class NewAnomaly implements Serializable {
    private int sourceType;
    private String sourceValue;
    private int targetType;
    private Date detectionTimeWindowStart;
    private Date detectionTimeWindowEnd;
    private Date trainingTimeWindowStart;
    private Date trainingTimeWindowEnd;
    private String patternIndex;
    private float score;
    private String algorithm;
    private String annotationCause;
    
    // Vector of training data
    private String targetValue;
    private float MinCount;
    private float MaxCount;
    private float MeanCount;
    private float StandardDeviation;
    
    private List<NewAnomalyEntry> anomalyEntries;

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

    public String getPatternIndex() {
        return patternIndex;
    }

    public void setPatternIndex(String patternIndex) {
        this.patternIndex = patternIndex;
    }

    public float getScore() {
        return score;
    }

    public void setScore(float score) {
        this.score = score;
    }

    public String getAlgorithm() {
        return algorithm;
    }

    public void setAlgorithm(String algorithm) {
        this.algorithm = algorithm;
    }

    public String getAnnotationCause() {
        return annotationCause;
    }

    public void setAnnotationCause(String annotationCause) {
        this.annotationCause = annotationCause;
    }

    public String getTargetValue() {
        return targetValue;
    }

    public void setTargetValue(String targetValue) {
        this.targetValue = targetValue;
    }

    public float getMinCount() {
        return MinCount;
    }

    public void setMinCount(float minCount) {
        MinCount = minCount;
    }

    public float getMaxCount() {
        return MaxCount;
    }

    public void setMaxCount(float maxCount) {
        MaxCount = maxCount;
    }

    public float getMeanCount() {
        return MeanCount;
    }

    public void setMeanCount(float meanCount) {
        MeanCount = meanCount;
    }

    public float getStandardDeviation() {
        return StandardDeviation;
    }

    public void setStandardDeviation(float standardDeviation) {
        StandardDeviation = standardDeviation;
    }

    public List<NewAnomalyEntry> getAnomalyEntries() {
        return anomalyEntries;
    }

    public void setAnomalyEntries(List<NewAnomalyEntry> anomalyEntries) {
        this.anomalyEntries = anomalyEntries;
    }
}
