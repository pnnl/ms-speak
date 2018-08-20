/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.custom;

import com.google.gwt.user.cellview.client.Column;

public abstract class WrappedStringColumn<T> extends Column<T, WrapString> {

    public WrappedStringColumn() {
        super(new WrapStringColumnCell());
    }

    /**      
     * Return the passed-in object. 
     * @param object The value to get
     */    
    @Override
   public WrapString getValue(T object) {   
       return null;         
   }    
}