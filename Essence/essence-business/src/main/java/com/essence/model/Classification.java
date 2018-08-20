/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;

import javax.persistence.*;
import java.io.Serializable;

@SuppressWarnings("serial")
@Entity
@Table(name = "classification")
public class Classification implements Serializable {

    @Id  @GeneratedValue
    @Column(name = "id")
    private Long id;

    @Column(name = "classification")
    private String classification;
    
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getClassification() {
        return classification;
    }

    public void setClassification(String classification) {
        this.classification = classification;
    }

    public Classification(String classification) {
        this.classification = classification;
    }

    public Classification() {
    }
}
