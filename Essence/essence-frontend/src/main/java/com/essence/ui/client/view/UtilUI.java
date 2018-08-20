/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.view;

import com.essence.ui.client.EssenceFrontEnd;
import com.essence.ui.client.GreetingService;
import com.essence.ui.client.GreetingServiceAsync;
import com.essence.ui.custom.AsyncCallbackAdapter;
import com.essence.ui.custom.HTMLFormatUtil;
import com.google.gwt.core.client.GWT;
import com.google.gwt.event.dom.client.ClickEvent;
import com.google.gwt.event.dom.client.ClickHandler;
import com.google.gwt.user.client.rpc.AsyncCallback;
import com.google.gwt.user.client.ui.*;

public class UtilUI {
    private static final String SERVER_ERROR = "An error occurred while "
            + "attempting to contact the server. Please check your network "
            + "connection and try again.";
    
    private final GreetingServiceAsync greetingService = GWT
            .create(GreetingService.class);
    
    private void setupControlPanel(FlexTable grid, final Label errorLabelControl) {
        //FlexTable grid = new FlexTable();
        grid.getElement().setId("utilGrid");

        Button runButton = new Button("Delete Engine Run Log");
        runButton.addClickHandler(new ClickHandler() {
            public void onClick(ClickEvent event) {
                errorLabelControl.setText("");
                
                greetingService.deleteAllEngineRunLogs(
                        new AsyncCallbackAdapter<Integer>() {
                            /*
                            public void onFailure(Throwable caught) {
                                errorLabelControl.setText(SERVER_ERROR);
                            }
                            */
                            
                            // Called by onFailure if the session is still valid
                            public void doFailureAction() {
                                errorLabelControl.setText(SERVER_ERROR);
                            }

                            public void onSuccess(Integer result) {
                                errorLabelControl.setText(result + " Engine Run Log rows deleted.");
                            }
                        });
            }
        });
        grid.setWidget(0, 0, runButton);
        //controlPanel.add(runButton);
        
        Button displayAllResultButton = new Button("Delete All Alerts");
        displayAllResultButton.addClickHandler(new ClickHandler() {
            public void onClick(ClickEvent event) {
                errorLabelControl.setText("");
                
                greetingService.deleteAllAlerts(new AsyncCallbackAdapter<Integer>() {
                    /*
                    public void onFailure(Throwable caught) {
                        errorLabelControl.setText(SERVER_ERROR);
                    }
                    */
                    
                    // Called by onFailure if the session is still valid
                    public void doFailureAction() {
                        errorLabelControl.setText(SERVER_ERROR);
                    }

                    public void onSuccess(Integer result) {
                        errorLabelControl.setText(result + " Alert rows deleted.");
                    }
                });
            }
        });
        grid.setWidget(1, 0, displayAllResultButton);
        //controlPanel.add(HTMLFormatUtil.getPaddingLabel());
        //controlPanel.add(displayAllResultButton);

        Label urlLabel = new Label("Graph URL");
        final TextBox url = new TextBox();
        greetingService.getSetting("iframeURL", new AsyncCallback<String>() {
            
            @Override
            public void onSuccess(String result) {
                url.setText(result);
            }
            
            @Override
            public void onFailure(Throwable caught) {
                // TODO Auto-generated method stub
                
            }
        });
        Button urlButton = new Button("Update URL");
        urlButton.addClickHandler(new ClickHandler() {
            @Override
            public void onClick(ClickEvent clickEvent) {
                EssenceFrontEnd.setGraphFrameURL(url.getText());
                greetingService.updateSetting("iframeURL", url.getText(), new AsyncCallbackAdapter<String>() {
                    @Override
                    public void doFailureAction() {

                    }

                    @Override
                    public void onSuccess(String s) {
                    }
                });
            }
        });
        grid.setWidget(2, 0, urlLabel);
        grid.setWidget(2, 1, url);
        grid.setWidget(2, 2, urlButton);

        //controlPanel.add(grid);
    }
    
    public void setupUtilPanels(DockLayoutPanel dPanel) {
        VerticalPanel vPanel = new VerticalPanel();
        final Label errorLabelControl = new Label();
        //HorizontalPanel controlPanel = new HorizontalPanel();
        //controlPanel.addStyleName("essencePanel");
        //controlPanel.setSpacing(10);
        FlexTable grid = new FlexTable();
        setupControlPanel(grid, errorLabelControl);
        vPanel.add(grid);   
        
        vPanel.add(errorLabelControl);
        dPanel.add(vPanel);
    }   
}
