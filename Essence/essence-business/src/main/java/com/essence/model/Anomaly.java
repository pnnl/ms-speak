/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;

import java.io.Serializable;
import java.util.Date;
import java.util.Set;

import javax.persistence.*;
import javax.xml.bind.annotation.XmlTransient;

@SuppressWarnings("serial")
@Entity
@Table(name = "anomaly")
public class Anomaly implements Serializable {
    @Id  @GeneratedValue
    @Column(name = "id")
    private Long id;
    
    @OneToOne()
    @JoinColumn(name="AlertId")
    @XmlTransient
    private Alert alert;
    
    @Column(name = "DetectionTimeWindowStart")
    private Date detectionTimeWindowStart;
    
    @Column(name = "DetectionTimeWindowEnd")
    private Date detectionTimeWindowEnd;
    
    @Column(name = "TrainingTimeWindowStart")
    private Date trainingTimeWindowStart;
    
    @Column(name = "TrainingTimeWindowEnd")
    private Date trainingTimeWindowEnd;
    
    @Column(name = "SourceType")
    private int sourceType;
    
    @Column(name = "SourceValue")
    private String sourceValue;
    
    @Column(name = "TargetType")
    private int targetType;
    
    @Column(name = "Score")
    private double score;
    
    @Column(name = "Algorithm")
    private String algorithm;

    @OneToMany(cascade=CascadeType.ALL, mappedBy = "anomaly", fetch=FetchType.LAZY)
    private Set<AnomalyNormalEntry> normalEntries;

    @OneToMany(cascade=CascadeType.ALL, mappedBy = "anomaly", fetch=FetchType.LAZY)
    private Set<AnomalyAnomalyEntry> anomalyEntries;

    @OneToMany(cascade=CascadeType.ALL, mappedBy = "anomaly", fetch=FetchType.LAZY)
    private Set<AnomalyPrediction> predictions;

    @ElementCollection(fetch=FetchType.LAZY)
    @CollectionTable(name="anomaly_patternindex", joinColumns=@JoinColumn(name="anomalyId"))
    @Column(name="patternIndex")
    private Set<Integer> patternIndex;

    //@ElementCollection(fetch=FetchType.LAZY)
    //@CollectionTable(name="anomaly_filtertypes", joinColumns=@JoinColumn(name="anomalyId"))
    //@Column(name="filterType")
    @Transient
    private Set<String> filterTypes;

    //@ElementCollection(fetch=FetchType.LAZY)
    //@CollectionTable(name="anomaly_filters", joinColumns=@JoinColumn(name="anomalyId"))
    //@Column(name="filter")
    @Transient
    private Set<String> filters;

    //@ElementCollection(fetch=FetchType.LAZY)
    //@CollectionTable(name="anomaly_featureTypes", joinColumns=@JoinColumn(name="anomalyId"))
    //@Column(name="featureType")
    @Transient
    private Set<String> featureTypes;

    public Set<String> getFilterTypes() {
        return filterTypes;
    }

    public void setFilterTypes(Set<String> filterTypes) {
        this.filterTypes = filterTypes;
    }

    public Set<String> getFilters() {
        return filters;
    }

    public void setFilters(Set<String> filters) {
        this.filters = filters;
    }

    public Set<String> getFeatureTypes() {
        return featureTypes;
    }

    public void setFeatureTypes(Set<String> featureTypes) {
        this.featureTypes = featureTypes;
    }

    public Anomaly(Date detectionTimeWindowStart, Date detectionTimeWindowEnd,
                   Date trainingTimeWindowStart, Date trainingTimeWindowEnd, int sourceType, String sourceValue,
                   int targetType, double score, String algorithm, Set<AnomalyNormalEntry> normalEntries,
                   Set<AnomalyAnomalyEntry> anomalyEntries, Set<AnomalyPrediction> predictions,
                   Set<Integer> patternIndex) {
        this.detectionTimeWindowStart = detectionTimeWindowStart;
        this.detectionTimeWindowEnd = detectionTimeWindowEnd;
        this.trainingTimeWindowStart = trainingTimeWindowStart;
        this.trainingTimeWindowEnd = trainingTimeWindowEnd;
        this.sourceType = sourceType;
        this.sourceValue = sourceValue;
        this.targetType = targetType;
        this.score = score;
        this.algorithm = algorithm;
        this.normalEntries = normalEntries;
        this.anomalyEntries = anomalyEntries;
        this.patternIndex = patternIndex;
        this.predictions = predictions;
    }

    public Anomaly(Alert alert, Date detectionTimeWindowStart, Date detectionTimeWindowEnd,
                   Date trainingTimeWindowStart, Date trainingTimeWindowEnd, double score, String algorithm,
                   Set<AnomalyNormalEntry> normalEntries, Set<AnomalyAnomalyEntry> anomalyEntries,
                   Set<AnomalyPrediction> predictions, Set<Integer> patternIndex, Set<String> filterTypes,
                   Set<String> filters, Set<String> featureTypes) {
        this.alert = alert;
        this.detectionTimeWindowStart = detectionTimeWindowStart;
        this.detectionTimeWindowEnd = detectionTimeWindowEnd;
        this.trainingTimeWindowStart = trainingTimeWindowStart;
        this.trainingTimeWindowEnd = trainingTimeWindowEnd;
        this.score = score;
        this.algorithm = algorithm;
        this.normalEntries = normalEntries;
        this.anomalyEntries = anomalyEntries;
        this.predictions = predictions;
        this.patternIndex = patternIndex;
        this.filterTypes = filterTypes;
        this.filters = filters;
        this.featureTypes = featureTypes;
    }

    public Anomaly() {
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    @XmlTransient
    public void setAlert(Alert alert) {
        this.alert = alert;
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

    public int getSourceType() {
        return sourceType;
    }

    public void setSourceType(int sourceType) {
        this.sourceType = sourceType;
    }

    public String getSourceValue() {
        return sourceValue;
    }

    public String getSourceIPAddress() {
        // TODO: modify when changing to filters

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

    public Set<Integer> getPatternIndex() {
        return patternIndex;
    }

    public void setPatternIndex(Set<Integer> patternIndex) {
        this.patternIndex = patternIndex;
    }

    public Set<AnomalyNormalEntry> getNormalEntries() {
        return normalEntries;
    }

    public void setNormalEntries(Set<AnomalyNormalEntry> normalEntries) {
        this.normalEntries = normalEntries;
    }

    public Set<AnomalyAnomalyEntry> getAnomalyEntries() {
        return anomalyEntries;
    }

    public void setAnomalyEntries(Set<AnomalyAnomalyEntry> anomalyEntries) {
        this.anomalyEntries = anomalyEntries;
    }

    public Set<AnomalyPrediction> getPredictions() {
        return predictions;
    }

    public void setPredictions(Set<AnomalyPrediction> predictions) {
        this.predictions = predictions;
    }
}
