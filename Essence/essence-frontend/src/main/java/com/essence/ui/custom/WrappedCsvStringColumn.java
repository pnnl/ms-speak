/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.custom;

import com.google.gwt.user.cellview.client.Column;

public abstract class WrappedCsvStringColumn<T> extends Column<T, WrapCsvString> {

    public WrappedCsvStringColumn() {
        super(new WrapCsvStringColumnCell());
    }

    /**      
     * Return the passed-in object. 
     * @param object The value to get
     */    
    @Override
   public WrapCsvString getValue(T object) {   
       return null;         
   }    
}