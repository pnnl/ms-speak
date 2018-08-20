/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;

import javax.persistence.*;
import java.io.Serializable;

@SuppressWarnings("serial")
@Entity
@Table(name = "cause")
public class Cause implements Serializable {
    @Id  @GeneratedValue
    @Column(name = "id")
    private Long id;

    @Column(name = "cause")
    private String cause;
    
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getCause() {
        return cause;
    }

    public void setCause(String cause) {
        this.cause = cause;
    }

    public Cause(String cause) {
        this.cause = cause;
    }

    public Cause() {
    }
}
