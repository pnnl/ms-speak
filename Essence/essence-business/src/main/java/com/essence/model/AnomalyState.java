/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;

import javax.persistence.*;
import java.io.Serializable;

/**
 * Created by BWintemberg on 8/10/2015.
 */
@SuppressWarnings("serial")
@Entity
@Table(name="anomaly_state")
public class AnomalyState implements Serializable {
    @Id
    @GeneratedValue
    @Column(name = "id")
    private Long id;

    @Column(name = "name")
    private String state;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getState() {
        return state;
    }

    public void setState(String value) {
        this.state = value;
    }
}
