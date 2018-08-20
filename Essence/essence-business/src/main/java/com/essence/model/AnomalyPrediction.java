/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;

import javax.persistence.*;
import java.io.Serializable;

/**
 * Created by BWintemberg on 11/17/2015.    1q
 */
@SuppressWarnings("serial")
@Entity
@Table(name = "anomaly_prediction")
public class AnomalyPrediction implements Serializable {
    @Id
    @GeneratedValue
    @Column(name = "id")
    private Long id;

    @ManyToOne
    @JoinColumn(name="anomalyid", nullable=false)//, insertable=false, updatable=false)
    private Anomaly anomaly;

    @ManyToOne
    @JoinColumn(name="stateid", nullable=false)//, insertable=false, updatable=false)
    private AnomalyState state;

    @ManyToOne
    @JoinColumn(name="causeid", nullable=false)//, insertable=false, updatable=false)
    private Cause cause;

    @Column(name = "score")
    private String score;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public AnomalyState getState() {
        return state;
    }

    public void setState(AnomalyState state) {
        this.state = state;
    }

    public Cause getCause() {
        return cause;
    }

    public void setCause(Cause cause) {
        this.cause = cause;
    }

    public String getScore() {
        return score;
    }

    public void setScore(String score) {
        this.score = score;
    }

    public void setAnomaly(Anomaly anomaly) {
        this.anomaly = anomaly;
    }
}
