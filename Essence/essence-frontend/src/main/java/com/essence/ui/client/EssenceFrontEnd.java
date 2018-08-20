/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client;

import java.util.ArrayList;

import com.essence.ui.client.object.EndpointConfigurationDTO;
import com.essence.ui.client.object.EndpointConfigurationKeyDTO;
import com.essence.ui.client.object.GraphMessage;
import com.essence.ui.client.view.ActionUI;
import com.essence.ui.client.view.AlertUI;
import com.essence.ui.client.view.DecisionRuleUI;
import com.essence.ui.client.view.DecisionUI;
import com.essence.ui.client.view.DetectionRuleUI;
import com.essence.ui.client.view.EndpointConfigurationUI;
import com.essence.ui.client.view.UtilUI;
import com.essence.ui.custom.AsyncCallbackAdapter;
import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.core.client.GWT;
import com.google.gwt.dom.client.Document;
import com.google.gwt.dom.client.Style.Unit;
import com.google.gwt.event.dom.client.ClickEvent;
import com.google.gwt.event.dom.client.ClickHandler;
import com.google.gwt.event.logical.shared.SelectionEvent;
import com.google.gwt.event.logical.shared.SelectionHandler;
import com.google.gwt.safehtml.shared.SafeHtml;
import com.google.gwt.safehtml.shared.SafeHtmlBuilder;
import com.google.gwt.user.client.ui.*;

/**
 * Entry point classes define <code>onModuleLoad()</code>.
 */
public class EssenceFrontEnd implements EntryPoint {
    private final GreetingServiceAsync greetingService = GWT
            .create(GreetingService.class);
    private DeckLayoutPanel contentPanel;
    private final EndpointConfigurationUI endpointConfigurationUI = new EndpointConfigurationUI();
    private final AlertUI alertUI = new AlertUI();
    private static Frame graphFrame = new Frame();
    
    public EssenceFrontEnd() {
    }

    /**
     * This is the entry point method.
     */
    public void onModuleLoad() {
        createDashboard();
    }
    
    private void createDashboard(){
        // Add left panel
        DockLayoutPanel dockPanel = new DockLayoutPanel(Unit.PX);
        createMenu(dockPanel);
        createLeftPanelButtons(dockPanel);

        final SplitLayoutPanel mainPanel = new SplitLayoutPanel();

        // Add header
        mainPanel.addNorth(makeHeader(), 40);

        // Add navigation
        mainPanel.addWest(dockPanel, 130);
        
        // Add content
        mainPanel.add(contentPanel);

        setupListener();
        
        RootLayoutPanel.get().add(mainPanel);
        
        setBrowserWindowTitle("ESSENCE");
    }

    private void createMenu(DockLayoutPanel dockPanel) {
        final int GRAPH_FRAME_INDEX = 0;

        Tree tree = new Tree();
        tree.addSelectionHandler(new SelectionHandler<TreeItem>() {
            public void onSelection(SelectionEvent<TreeItem> event) {
                EssenceTreeItem item = (EssenceTreeItem) event.getSelectedItem();
                int index = item.getSubPanelIndex();
                contentPanel.showWidget(index);

                if(index == GRAPH_FRAME_INDEX && (graphFrame.getUrl() == null || graphFrame.getUrl().isEmpty())) {
                    greetingService.getSetting("iframeURL", new AsyncCallbackAdapter<String>() {
                        @Override
                        public void doFailureAction() {

                        }

                        @Override
                        public void onSuccess(String setting) {
                            if (setting != null) {
                                graphFrame.setUrl(setting);
                            }
                        }
                    });
                }
            }
        });

        ArrayList<Widget> contentWidgets = new ArrayList<>(8);

        // Network graph
        FlowPanel flowPanel = new FlowPanel();
        graphFrame.getElement().setId("graphFrame");
        flowPanel.add(graphFrame);
        contentWidgets.add(flowPanel);
        SafeHtmlBuilder builder = new SafeHtmlBuilder();
        builder.appendEscaped("Network Graph");
        EssenceTreeItem item = new EssenceTreeItem(builder.toSafeHtml(), GRAPH_FRAME_INDEX);
        tree.addItem(item);

        // Alerts
        final DockLayoutPanel dPanel2 = new DockLayoutPanel(Unit.PCT);
        SplitLayoutPanel alertPanel = new SplitLayoutPanel();
        alertUI.setupAlertPanel2(alertPanel);
        dPanel2.addNorth(alertPanel, 100);
        contentWidgets.add(dPanel2);
        builder = new SafeHtmlBuilder();
        builder.appendEscaped("Alerts");
        tree.addItem(new EssenceTreeItem(builder.toSafeHtml(), 1));

        // Decisions
        final DockLayoutPanel decisionDockPanel = new DockLayoutPanel(Unit.PCT);
        ScrollPanel decisionPanel = new ScrollPanel(); // parents need to be a layout panel, not VerticalPanel
        final DecisionUI decisionUI = new DecisionUI();
        decisionUI.setupDecisionPanels(decisionPanel, decisionDockPanel);
        decisionPanel.addStyleName("reportPanelScroll");
        decisionDockPanel.addNorth(decisionPanel, 100);
        contentWidgets.add(decisionDockPanel);
        builder = new SafeHtmlBuilder();
        builder.appendEscaped("Decisions");
        tree.addItem(new EssenceTreeItem(builder.toSafeHtml(), 2));

        // Actions
        final DockLayoutPanel actionDockPanel = new DockLayoutPanel(Unit.PCT);
        ScrollPanel actionPanel = new ScrollPanel(); // parents need to be a layout panel, not VerticalPanel
        final ActionUI actionUI = new ActionUI();
        actionUI.setupActionPanels(actionPanel, actionDockPanel);
        actionPanel.addStyleName("reportPanelScroll");
        actionDockPanel.addNorth(actionPanel, 100);
        contentWidgets.add(actionDockPanel);
        actionUI.updateDataProvider();
        builder = new SafeHtmlBuilder();
        builder.appendEscaped("Actions");
        tree.addItem(new EssenceTreeItem(builder.toSafeHtml(), 3));

        // Detection rules
        final DockLayoutPanel detectionPanel2 = new DockLayoutPanel(Unit.PCT);
        ScrollPanel detectionRulePanel2 = new ScrollPanel(); // parents need to be a layout panel, not VerticalPanel
        final DetectionRuleUI drUI = new DetectionRuleUI();
        drUI.setupDetectionRulePanel2(detectionRulePanel2, detectionPanel2);
        detectionRulePanel2.addStyleName("reportPanelScroll");
        detectionPanel2.addNorth(detectionRulePanel2, 100);
        contentWidgets.add(detectionPanel2);
        drUI.refreshRuleDisplay();
        builder = new SafeHtmlBuilder();
        builder.appendEscaped("Detection Rules");
        tree.addItem(new EssenceTreeItem(builder.toSafeHtml(), 4));

        // Decision rules
        final DockLayoutPanel decisionRulePanel = new DockLayoutPanel(Unit.PCT);
        ScrollPanel decisionRuleDisplayPanel = new ScrollPanel(); // parents need to be a layout panel, not VerticalPanel
        final DecisionRuleUI decisionRuleUI = new DecisionRuleUI();
        decisionRuleUI.setupDecisionRulePanel(decisionRuleDisplayPanel, decisionRulePanel);
        decisionRuleDisplayPanel.addStyleName("reportPanelScroll");
        decisionRulePanel.addNorth(decisionRuleDisplayPanel, 100);
        contentWidgets.add(decisionRulePanel);
        decisionRuleUI.updateDataProvider();
        builder = new SafeHtmlBuilder();
        builder.appendEscaped("Decision Rules");
        tree.addItem(new EssenceTreeItem(builder.toSafeHtml(), 5));

        // Endpoints
        final DockLayoutPanel endpointConfigdPanel = new DockLayoutPanel(Unit.PCT);
        ScrollPanel endpointConfigPanel = new ScrollPanel();
        //final EndpointConfigurationUI ecUI = new EndpointConfigurationUI();
        endpointConfigurationUI.setupEndpointConfigPanel(endpointConfigPanel, endpointConfigdPanel);
        endpointConfigPanel.addStyleName("reportPanelScroll");
        endpointConfigdPanel.add(endpointConfigPanel);
        contentWidgets.add(endpointConfigdPanel);
        endpointConfigurationUI.updateDataProvider();
        builder = new SafeHtmlBuilder();
        builder.appendEscaped("Endpoints");
        tree.addItem(new EssenceTreeItem(builder.toSafeHtml(), 6));

        // Add admin panel
        DockLayoutPanel utilDockPanel = new DockLayoutPanel(Unit.PCT);
        UtilUI utilUI = new UtilUI();
        utilUI.setupUtilPanels(utilDockPanel);
        contentWidgets.add(utilDockPanel);
        builder = new SafeHtmlBuilder();
        builder.appendEscaped("Admin");
        tree.addItem(new EssenceTreeItem(builder.toSafeHtml(), 7));

        contentPanel = new ContentPanel(contentWidgets);

        dockPanel.addNorth(tree, 200);
    }

    private void createLeftPanelButtons(DockLayoutPanel dockPanel) {
        FlowPanel leftFlowPanel = new FlowPanel();

        final Button runDetectorButton = new Button("Run Analyzer Once");
        final Button runDetectorButtonN = new Button("Run Analyzer Continuously");
        final Button engineOn = new Button("Analyzer Running");
        runDetectorButton.addClickHandler(new ClickHandler() {
            public void onClick(ClickEvent event) {
                greetingService.runAnalyzer(false,
                        //DetectionRuleType.valueOf(detectorType.getValue(detectorType.getSelectedIndex())),
                        new AsyncCallbackAdapter<String>() {
                            // Called by onFailure if the session is still valid
                            public void doFailureAction() {
                                //errorLabelActivateDetector.setText(SERVER_ERROR);
                            }

                            public void onSuccess(String result) {
                            }
                        });
                engineOn.setVisible(false);
            }
        });
        runDetectorButton.addStyleName("leftPanelButton");
        leftFlowPanel.add(runDetectorButton);

        runDetectorButtonN.addClickHandler(new ClickHandler() {
            public void onClick(ClickEvent event) {
                greetingService.runAnalyzer(true,
                        //DetectionRuleType.valueOf(detectorType.getValue(detectorType.getSelectedIndex())),
                        new AsyncCallbackAdapter<String>() {
                            // Called by onFailure if the session is still valid
                            public void doFailureAction() {
                                //errorLabelActivateDetector.setText(SERVER_ERROR);
                            }

                            public void onSuccess(String result) {
                            }
                        });
                engineOn.setVisible(true);
            }
        });
        leftFlowPanel.add(runDetectorButtonN);
        runDetectorButtonN.addStyleName("leftPanelButton");

        engineOn.setStyleName("greenButton");
        engineOn.setVisible(false);
        leftFlowPanel.add(engineOn);

        Button decisionRunButton = new Button("Run Decision Engine");
        decisionRunButton.addClickHandler(new ClickHandler() {
            public void onClick(ClickEvent event) {
                greetingService.runDecisionEngine(
                        new AsyncCallbackAdapter<String>() {
                            /*
                            public void onFailure(Throwable caught) {
                                errorLabelControl.setText(SERVER_ERROR);
                            }
                            */
                            // Called by onFailure if the session is still valid
                            public void doFailureAction() {
                                //errorLabelControl.setText(SERVER_ERROR);
                            }


                            public void onSuccess(String result) {
                                // no-op
                            }
                        });
            }
        });
        decisionRunButton.addStyleName("leftPanelButton");
        leftFlowPanel.add(decisionRunButton);

        Button actionRunButton = new Button("Run Action Engine");
        actionRunButton.addClickHandler(new ClickHandler() {
            public void onClick(ClickEvent event) {
                greetingService.runActionEngine(
                        new AsyncCallbackAdapter<String>() {
	    					/*
	    					public void onFailure(Throwable caught) {
	    						errorLabelControl.setText(SERVER_ERROR);
	    					}
	    					*/

                            // Called by onFailure if the session is still valid
                            public void doFailureAction() {
                                //errorLabelControl.setText(SERVER_ERROR);
                            }

                            public void onSuccess(String result) {
                                // no-op
                            }
                        });
            }
        });
        actionRunButton.addStyleName("leftPanelButton");
        leftFlowPanel.add(actionRunButton);

        dockPanel.add(leftFlowPanel);
    }
	
	public void setBrowserWindowTitle (String newTitle) {
		if (Document.get() != null) {
			Document.get().setTitle (newTitle);
		}
	}

    public static String getGraphFrameURL() {
        return graphFrame.getUrl();
    }
    
    public static void setGraphFrameURL(String url) {
        graphFrame.setUrl(url);
    }

    public void handleMessage(GraphMessage msg) {
        if (msg.getCall() == "showAlertDisplay") {
            alertUI.showAlertDisplayDialogBox(msg.getId());
        }
        else if (msg.getCall() == "addHost") {
            endpointConfigurationUI.showAddHostDialog(null, msg.getIPAddress(), null);
        }
        else if (msg.getCall() == "addEndpointConfiguration") {
            EndpointConfigurationDTO d = new EndpointConfigurationDTO();
            d.setKey(new EndpointConfigurationKeyDTO());
            d.getKey().setHostIPAddress(msg.getIPAddress());
            d.setVersion(msg.getVersion());

            endpointConfigurationUI.showEditEndpointConfigurationDialog(null, d, null);
        }
        else if (msg.getCall() == "showEndpointConfiguration") {
            endpointConfigurationUI.showEndpointConfigurationInfoDialog(msg.getIPAddress());
        }
    }

    public native void setupListener() /*-{
        var frontend = this;
        function listener(event) {
            if(event.origin !== getGraphFrameURL()) return;
            frontend.@com.essence.ui.client.EssenceFrontEnd::handleMessage(Lcom/essence/ui/client/object/GraphMessage;)(event.data); // call function with the name
        }
        if ($wnd.addEventListener) {
            $wnd.addEventListener("message", listener, false);
        }else if ($wnd.attachEvent) {
            $wnd.attachEvent("onmessage", listener)
        } else {
            $wnd["onmessage"] = listener;
        }
    }-*/;

    private HTML makeHeader() {
        return new HTML("<h4>Essence Dashboard</h4>");
    }

    private class EssenceTreeItem extends TreeItem {
        private int subPanelIndex;

        public EssenceTreeItem(SafeHtml safeHtml, int subPanelIndex) {
            super(safeHtml);
            this.subPanelIndex = subPanelIndex;
        }

        public int getSubPanelIndex() {
            return subPanelIndex;
        }
    }
}
