/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.object;

import com.essence.model.AnomalyPrediction;

import java.io.Serializable;
import java.util.Date;
import java.util.Set;

@SuppressWarnings("serial")
public class AnomalyDTO implements Serializable {
    private Long id;
    
    private Date detectionTimeWindowStart;
    
    private Date detectionTimeWindowEnd;
    
    private Date trainingTimeWindowStart;
    
    private Date trainingTimeWindowEnd;
    
    private int sourceType;
    
    private String sourceValue;
    
    private int targetType;
    
    private double score;
    
    private String algorithm;

    //private int patternIndex;
    private Set<Integer> patternIndex;

    private Set<AnomalyNormalEntryDTO> normalEntries;

    private Set<AnomalyAnomalyEntryDTO> anomalyEntries;

    private Set<AnomalyPredictionDTO> predictions;

//    private Set<CauseDTO> predictedCauses;
//
//    private Set<AnomalyStateDTO> predictedStates;

    public AnomalyDTO(Long id, Date detectionTimeWindowStart, Date detectionTimeWindowEnd, Date trainingTimeWindowStart,
                      Date trainingTimeWindowEnd, int sourceType, String sourceValue, int targetType, double score,
                      String algorithm, Set<Integer> patternIndex, Set<AnomalyNormalEntryDTO> normalEntries,
                      Set<AnomalyAnomalyEntryDTO> anomalyEntries, Set<AnomalyPredictionDTO> predictions) {
        this.id = id;
        this.detectionTimeWindowStart = detectionTimeWindowStart;
        this.detectionTimeWindowEnd = detectionTimeWindowEnd;
        this.trainingTimeWindowStart = trainingTimeWindowStart;
        this.trainingTimeWindowEnd = trainingTimeWindowEnd;
        this.sourceType = sourceType;
        this.sourceValue = sourceValue;
        this.targetType = targetType;
        this.score = score;
        this.algorithm = algorithm;
        this.patternIndex = patternIndex;
        this.normalEntries = normalEntries;
        this.anomalyEntries = anomalyEntries;
        this.predictions = predictions;
    }

    public AnomalyDTO() {
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

//    @XmlTransient
//    public Alert getAlert() {
//        return alert;
//    }

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

    public double getScore() {
        return score;
    }

    public void setScore(double score) {
        this.score = score;
    }

    public String getAlgorithm() {
        return algorithm;
    }

    public void setAlgorithm(String algorithm) {
        this.algorithm = algorithm;
    }

//    public Cause getPredictedCause() {
//        return predictedCause;
//    }
//
//    public void setPredictedCause(Cause predictedCause) {
//        this.predictedCause = predictedCause;
//    }

    public Set<Integer> getPatternIndex() {
        return patternIndex;
    }

    public void setPatternIndex(Set<Integer> patternIndex) {
        this.patternIndex = patternIndex;
    }

    public Set<AnomalyNormalEntryDTO> getNormalEntries() {
        return normalEntries;
    }

    public void setNormalEntries(Set<AnomalyNormalEntryDTO> normalEntries) {
        this.normalEntries = normalEntries;
    }

    public Set<AnomalyAnomalyEntryDTO> getAnomalyEntries() {
        return anomalyEntries;
    }

    public void setAnomalyEntries(Set<AnomalyAnomalyEntryDTO> anomalyEntries) {
        this.anomalyEntries = anomalyEntries;
    }

    public Set<AnomalyPredictionDTO> getPredictions() {
        return predictions;
    }

    public void setPredictions(Set<AnomalyPredictionDTO> predictions) {
        this.predictions = predictions;
    }
}
