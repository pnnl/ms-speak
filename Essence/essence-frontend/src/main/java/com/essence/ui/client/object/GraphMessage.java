/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.object;

import com.google.gwt.core.client.JavaScriptObject;

/**
 * Created by BWintemberg on 10/5/2015.
 */
public class GraphMessage extends JavaScriptObject {
    // Overlay types always have protected, zero-arg ctors
    protected GraphMessage() { }

    // Typically, methods on overlay types are JSNI
    public final native String getCall() /*-{ return this.Call; }-*/;
    public final native int getId() /*-{ return this.id;  }-*/;
    public final native String getIPAddress()  /*-{ return this.IPAddress;  }-*/;
    public final native String getVersion()  /*-{ return this.Version;  }-*/;
    public final native String getEndpointList()  /*-{ return this.EndpointList;  }-*/;
}
