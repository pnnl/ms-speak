/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.object;

import java.io.Serializable;

@SuppressWarnings("serial")
public class AnomalyPredictionDTO implements Serializable {
    private Long id;

    private AnomalyStateDTO state;

    private CauseDTO cause;

    private String score;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public AnomalyStateDTO getState() {
        return state;
    }

    public void setState(AnomalyStateDTO state) {
        this.state = state;
    }

    public CauseDTO getCause() {
        return cause;
    }

    public void setCause(CauseDTO cause) {
        this.cause = cause;
    }

    public String getScore() {
        return score;
    }

    public void setScore(String score) {
        this.score = score;
    }

    public AnomalyPredictionDTO() {
    }

    public AnomalyPredictionDTO(Long id, AnomalyStateDTO state, CauseDTO cause, String score) {
        this.id = id;
        this.state = state;
        this.cause = cause;
        this.score = score;
    }
}
