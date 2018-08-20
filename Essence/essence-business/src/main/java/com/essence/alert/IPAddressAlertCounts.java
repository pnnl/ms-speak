/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.alert;

import java.io.Serializable;
import java.util.HashMap;

@SuppressWarnings("serial")
public class IPAddressAlertCounts implements Serializable {
    private HashMap<String, AlertCount> items;

    public HashMap<String, AlertCount> getItems() {
        return items;
    }

    public void setItems(HashMap<String, AlertCount> items) {
        this.items = items;
    }
}
