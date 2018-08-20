/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;

import org.hibernate.annotations.Fetch;
import org.hibernate.annotations.FetchMode;

import java.io.Serializable;
import java.util.Date;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.OneToOne;
import javax.persistence.Table;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;

@SuppressWarnings("serial")
@Entity
@Table(name = "alert")
public class Alert implements Serializable {
    @Id  @GeneratedValue
    @Column(name = "id")
    private Long id;
    
    @Column(name = "alert_type_id")
    private Integer alertTypeId;
    
    @Column(name = "creation_time", columnDefinition="DATETIME")
    @Temporal(TemporalType.TIMESTAMP)
    private Date creationTime;

    @Column(name = "description")
    private String description; 	// details of the result

    @Column(name = "status")
    private String status; 	// OPEN, PROCESSED, ARCHIVED

    @Column(name = "organization_id")
    private int	   organizationId = -1;

    @Column(name = "severity")
    private String severity;

    @OneToOne(mappedBy="alert", cascade=CascadeType.ALL, fetch=FetchType.LAZY)
    @Fetch(FetchMode.JOIN)
    private Anomaly anomaly;

    @OneToOne(mappedBy="alert", cascade=CascadeType.ALL, fetch=FetchType.LAZY)
    @Fetch(FetchMode.JOIN)
    private AnalyzerResult analyzerResult;

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

//    public void setSeverity(SeverityType type) {
//        if (type != null)
//            this.severity = type.toString();
//    }
//
//    public void setSeverity(String type) {
//        if (type == null)
//            return;
//
//        if (type.isEmpty() || type.equalsIgnoreCase("N/A")) { // clear the severity
//            this.severity = null;
//            return;
//        }
//
//        SeverityType s = null;
//        try {
//            s = SeverityType.valueOf(type);
//        } catch (Exception ex) {
//            // No op
//        }
//
//        if (s != null)
//            this.severity = type;
//    }

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

    public Anomaly getAnomaly() {
        return anomaly;
    }

    public void setAnomaly(Anomaly anomaly) {
        this.anomaly = anomaly;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public void print() {
        StringBuffer sb = new StringBuffer(); 
        //sb.append("id="+this.id+"\trelatedItemId="+this.relatedItemId+"\talertTypeId="+this.alertTypeId);
        sb.append("\tcreationTime="+this.creationTime+"\tdescription="+this.description);
        //sb.append("\tseverity="+this.severity + "\tstatus="+this.status + "\tpolicyId=" + this.organizationId);
        System.out.println(sb.toString());
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

    public AnalyzerResult getAnalyzerResult() {
        return analyzerResult;
    }

    public void setAnalyzerResult(AnalyzerResult analyzerResult) {
        this.analyzerResult = analyzerResult;
    }

    public String getSeverity() {
        return severity;
    }

    public void setSeverity(String severity) {
        this.severity = severity;
    }
    
//    public Alert(AlertDTO a) {
//        id = a.getId();
//        alertTypeId = a.getAlertTypeId();
//        analyzerResult = a.getAnalyzerResult();
//        anomaly = new Anomaly(a.getAnomaly(), this);
//        creationTime = a.getCreationTime();
//        description = a.getDescription();
//        organizationId = a.getOrganizationId();
//        status = a.getStatus();
//    }

    public Alert(Long id, Integer alertTypeId, Date creationTime, String description, String status, int organizationId,
                 Anomaly anomaly, AnalyzerResult analyzerResult, String severity) {
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

    public Alert() {
    }
}
