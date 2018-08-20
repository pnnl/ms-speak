/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association
Copyright (C) 2014-2016, Cigital, Inc
*/
package com.essence.services.dtos;

import com.essence.model.AnalyzerResultStatusType;

import java.util.Date;

public class AlertDTO {
    private Long id;

    private Integer alertTypeId;

    private Date creationTime;

    private String description; 	// details of the result

    private String status; 	// OPEN, PROCESSED, ARCHIVED

    private int	organizationId = -1;

    private AnomalyDTO anomaly;

    private AnalyzerResultDTO analyzerResult;

    private String severity;

    public AlertDTO(Long id, Integer alertTypeId, Date creationTime, String description, String status,
                    int organizationId, AnomalyDTO anomaly, AnalyzerResultDTO analyzerResult, String severity) {
        this.id = id;
        this.alertTypeId = alertTypeId;
        this.creationTime = creationTime;
        this.description = description;
        this.status = status;
        this.organizationId = organizationId;
        this.anomaly = anomaly;
        this.analyzerResult = analyzerResult;
        this.severity = severity;
    }

    public AlertDTO() {
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(AnalyzerResultStatusType type) {
        if (type != null)
            this.status = type.toString();
    }

    public int getOrganizationId() {
        return organizationId;
    }

    public void setOrganizationId(int organizationId) {
        this.organizationId = organizationId;
    }

    public AnomalyDTO getAnomaly() {
        return anomaly;
    }

    public void setAnomaly(AnomalyDTO anomaly) {
        this.anomaly = anomaly;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public Integer getAlertTypeId() {
        return alertTypeId;
    }

    public void setAlertTypeId(Integer alertTypeId) {
        this.alertTypeId = alertTypeId;
    }

    public Date getCreationTime() {
        return creationTime;
    }

    public void setCreationTime(Date creationTime) {
        this.creationTime = creationTime;
    }

    public AnalyzerResultDTO getAnalyzerResult() {
        return analyzerResult;
    }

    public void setAnalyzerResult(AnalyzerResultDTO analyzerResult) {
        this.analyzerResult = analyzerResult;
    }

    public String getSeverity() {
        return severity;
    }

    public void setSeverity(String severity) {
        this.severity = severity;
    }
}
