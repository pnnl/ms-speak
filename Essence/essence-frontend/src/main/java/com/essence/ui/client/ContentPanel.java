/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client;

import java.util.ArrayList;

import com.google.gwt.user.client.ui.DeckLayoutPanel;
import com.google.gwt.user.client.ui.Widget;


public class ContentPanel extends DeckLayoutPanel {
    public ContentPanel(ArrayList<Widget> contentWidgets) {
        for (Widget panel : contentWidgets) {
          System.out.println("Adding to content panel: " + panel);
          add(panel);
        }
        //showWidget(0);
        setAnimationDuration(800);
        setAnimationVertical(true);
      }
}
