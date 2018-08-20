/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.custom;

import com.google.gwt.core.client.GWT;
import com.google.gwt.user.client.Window;
import com.google.gwt.user.client.rpc.AsyncCallback;
import com.google.gwt.user.client.rpc.InvocationException;

public abstract class AsyncCallbackAdapter<T> implements AsyncCallback<T> {
	
	abstract public void doFailureAction();
	
    public void onFailure(Throwable caught) {

        if (caught instanceof InvocationException) {
            InvocationException ie = (InvocationException) caught;
            if(ie.getMessage().contains("j_spring_security_check"))
            {
//                Window.alert("Session is timed out. Please login again");
                Window.open(GWT.getHostPageBaseURL() + "login.html", "_self", null);
                return;
            }
        } 
        
      //Do other error handling here
        doFailureAction();
    }
}