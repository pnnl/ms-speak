/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;

import java.io.Serializable;
import java.util.List;

@SuppressWarnings("serial")
public class DetectionRuleTypes implements Serializable {
    List<String> types;

    public List<String> getTypes() {
        return types;
    }

    public void setTypes(List<String> types) {
        this.types = types;
    }
}
