/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;

import javax.persistence.*;
import java.io.Serializable;

/**
 * Created by BWintemberg on 11/2/2015.
 */
@SuppressWarnings("serial")
@Entity
@Table(name = "setting")
public class Setting implements Serializable {
    @Id
    @Column(name = "name")
    private String name;

    @Column(name = "value")
    private String value;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
}
