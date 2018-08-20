/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.view;

import java.util.List;

import com.essence.ui.client.GreetingService;
import com.essence.ui.client.GreetingServiceAsync;
import com.essence.ui.client.object.ActionDTO;
import com.essence.ui.client.object.DetectionRuleDTO;
import com.essence.ui.client.object.DetectionRuleTypeDTO;
import com.essence.ui.custom.AsyncCallbackAdapter;
import com.essence.ui.custom.HTMLFormatUtil;
import com.essence.ui.shared.StringUtil;
import com.google.gwt.core.client.GWT;
import com.google.gwt.event.dom.client.ClickEvent;
import com.google.gwt.event.dom.client.ClickHandler;
import com.google.gwt.user.cellview.client.CellTable;
import com.google.gwt.user.cellview.client.SimplePager;
import com.google.gwt.user.cellview.client.TextColumn;
import com.google.gwt.user.cellview.client.SimplePager.TextLocation;
import com.google.gwt.user.client.Window;
import com.google.gwt.user.client.rpc.AsyncCallback;
import com.google.gwt.user.client.ui.Button;
import com.google.gwt.user.client.ui.DockLayoutPanel;
import com.google.gwt.user.client.ui.FlexTable;
import com.google.gwt.user.client.ui.HorizontalPanel;
import com.google.gwt.user.client.ui.Label;
import com.google.gwt.user.client.ui.ScrollPanel;
import com.google.gwt.user.client.ui.TextBox;
import com.google.gwt.user.client.ui.VerticalPanel;
import com.google.gwt.view.client.ListDataProvider;
import com.google.gwt.view.client.SingleSelectionModel;

@SuppressWarnings("unused")
public class ActionUI {
	// The message displayed to the user when the server cannot be reached or
	// returns an error.
	private static final String SERVER_ERROR = "An error occurred while "
			+ "attempting to contact the server. Please check your network "
			+ "connection and try again.";

	// Create a remote service proxy to talk to the server-side Greeting
	// service.
	private final GreetingServiceAsync greetingService = GWT
			.create(GreetingService.class);
	private final ListDataProvider<ActionDTO> dataProvider = new ListDataProvider<ActionDTO>();
	private String NAME = "";
	
	public void updateDataProvider() {
		greetingService.getActions(new AsyncCallbackAdapter<List<ActionDTO>>() {
			/*
			public void onFailure(Throwable caught) {
				//nothing
			}
			*/
			
			// Called by onFailure if the session is still valid
			public void doFailureAction() {
			}

			public void onSuccess(List<ActionDTO> result) {
				dataProvider.setList(result);
			}
		});
		
		greetingService.getName(new AsyncCallbackAdapter<String>() {
			/*
			public void onFailure(Throwable caught) {
				//
			}
			*/
			
			// Called by onFailure if the session is still valid
			public void doFailureAction() {
			}

			public void onSuccess(String result) {
				if (StringUtil.stringHasValue(result))
					NAME = result;
				else
					NAME = "No Name";
			}
		});

	}
	private void setupActionDisplayPanel(CellTable<ActionDTO> table, final ListDataProvider<ActionDTO> dataProvider) {
		TextColumn<ActionDTO> idColumn = new TextColumn<ActionDTO>() {
			@Override
			public String getValue(ActionDTO r) {
				return r.getId() + "";
			}
		};
		idColumn.setSortable(true);
		table.addColumn(idColumn, "Action ID");
		table.addColumnStyleName(0, "ar_number_column_style");
				
		TextColumn<ActionDTO> decisionIdColumn = new TextColumn<ActionDTO>() {
			@Override
			public String getValue(ActionDTO r) {
				return r.getDecisionId()+"";
			}
		};
		decisionIdColumn.setSortable(true);
		table.addColumn(decisionIdColumn, "Ref Decision ID");
		table.addColumnStyleName(1, "ar_number_column_style");
		
		TextColumn<ActionDTO> decisionTypeColumn = new TextColumn<ActionDTO>() {
			@Override
			public String getValue(ActionDTO r) {
				return r.getDecision().getDecisionType();
			}
		};
		decisionTypeColumn.setSortable(true);
		table.addColumn(decisionTypeColumn, "Decision Type");
		table.addColumnStyleName(2, "ar_narrow_column_style");

		TextColumn<ActionDTO> detailColumn = new TextColumn<ActionDTO>() {
			@Override
			public String getValue(ActionDTO r) {
				return r.getDetail();
			}
		};
		detailColumn.setSortable(true);
		table.addColumn(detailColumn, "Detail");
		table.addColumnStyleName(3, "ar_wide_column_style");

		TextColumn<ActionDTO> tsColumn = new TextColumn<ActionDTO>() {
			@Override
			public String getValue(ActionDTO r) {
				return r.getTimestamp().toString();
			}
		};
		tsColumn.setSortable(true);
		table.addColumn(tsColumn, "Timestamp");
		table.addColumnStyleName(4, "ar_narrow_column_style");
		
		table.setWidth("100%", true);		
	}
	
	private void setupControlPanel(HorizontalPanel controlPanel, final Label errorLabelControl, 
			final ListDataProvider<ActionDTO> dataProvider) {
	    Button displayAllResultButton = new Button("Refresh Actions");
	    displayAllResultButton.addClickHandler(new ClickHandler() {
	    	public void onClick(ClickEvent event) {
	    		greetingService.getActions(new AsyncCallbackAdapter<List<ActionDTO>>() {
	    			/*
	    			public void onFailure(Throwable caught) {
	    				errorLabelControl.setText(SERVER_ERROR);
	    			}
	    			*/
					
					// Called by onFailure if the session is still valid
					public void doFailureAction() {
						errorLabelControl.setText(SERVER_ERROR);
					}

	    			public void onSuccess(List<ActionDTO> result) {
	    				dataProvider.setList(result);
	    			}
	    		});
	        }
	    });
	    controlPanel.add(HTMLFormatUtil.getPaddingLabel());
	    controlPanel.add(displayAllResultButton);
	    
//	    final String turnFirewallOffText = "Turn Off SDN Controller";
//	    final String turnFirewallOnText = "Turn On SDN Controller";
//	    final Button turnOffFirewallButton = new Button(turnFirewallOffText);
//	    turnOffFirewallButton.addClickHandler(new ClickHandler() {
//	    	public void onClick(ClickEvent event) {
//	    		if (turnOffFirewallButton.getText().equals(turnFirewallOffText)) { // currently on
//		    		greetingService.setFirewall(false, new AsyncCallbackAdapter<String>() { // turn it off
//		    			/*
//		    			public void onFailure(Throwable caught) {
//		    				errorLabelControl.setText(SERVER_ERROR);
//		    			}
//		    			*/
//
//    					// Called by onFailure if the session is still valid
//    					public void doFailureAction() {
//    						errorLabelControl.setText(SERVER_ERROR);
//    					}
//
//		    			public void onSuccess(String result) {
//		    				turnOffFirewallButton.setText(turnFirewallOnText);
//		    			}
//		    		});
//	    		} else { // currently off
//		    		greetingService.setFirewall(true, new AsyncCallbackAdapter<String>() { // turn it on
//		    			/*
//		    			public void onFailure(Throwable caught) {
//		    				errorLabelControl.setText(SERVER_ERROR);
//		    			}
//    					*/
//
//    					// Called by onFailure if the session is still valid
//    					public void doFailureAction() {
//    						errorLabelControl.setText(SERVER_ERROR);
//    					}
//
//		    			public void onSuccess(String result) {
//		    				turnOffFirewallButton.setText(turnFirewallOffText);
//		    			}
//		    		});
//	    		}
//	    	}
//	    });
//
//	    // This detection may not working well with multiple users doing the same thing
//	    greetingService.isFirewallOn(new AsyncCallbackAdapter<Boolean>() {
//	    	/*
//	    			public void onFailure(Throwable caught) {
//	    				errorLabelControl.setText(SERVER_ERROR);
//	    			}
//	    			*/
//
//					// Called by onFailure if the session is still valid
//					public void doFailureAction() {
//						errorLabelControl.setText(SERVER_ERROR);
//					}
//
//	    			public void onSuccess(Boolean result) {
//	    				if (result) // currently on
//	    					turnOffFirewallButton.setText(turnFirewallOffText);
//	    				else // currently off
//	    					turnOffFirewallButton.setText(turnFirewallOnText);
//	    			}
//	    		});
//	    controlPanel.add(HTMLFormatUtil.getPaddingLabel());
//	    controlPanel.add(turnOffFirewallButton);
	}
	
	public void setupActionPanels(ScrollPanel ActionPanel, DockLayoutPanel dPanel) {
		

		// Create a CellTable.
		final CellTable<ActionDTO> table = new CellTable<ActionDTO>();
		setupActionDisplayPanel(table, dataProvider);

		SimplePager.Resources pagerResources = GWT.create(SimplePager.Resources.class);
		SimplePager pager = new SimplePager(TextLocation.CENTER, pagerResources, false, 10, true);
		pager.setDisplay(table);
		dataProvider.addDataDisplay(table);

	    final SingleSelectionModel<ActionDTO> selectionModel = new SingleSelectionModel<ActionDTO>();
	    table.setSelectionModel(selectionModel);

		// Set the width of each column.
		// table.setColumnWidth(nameColumn, 35.0, Unit.PCT);
		final Label errorLabelDisplay = new Label();

		greetingService.getActions(new AsyncCallbackAdapter<List<ActionDTO>>() {
			/*
			public void onFailure(Throwable caught) {
				errorLabelDisplay.setText(SERVER_ERROR);
			}
			*/
			
			// Called by onFailure if the session is still valid
			public void doFailureAction() {
				errorLabelDisplay.setText(SERVER_ERROR);
			}

			public void onSuccess(List<ActionDTO> result) {
				dataProvider.setList(result);
			}
		});

		VerticalPanel displayPanel = new VerticalPanel();
		displayPanel.add(pager);
		displayPanel.add(table);
		displayPanel.add(errorLabelDisplay);
		displayPanel.setHorizontalAlignment(VerticalPanel.ALIGN_RIGHT);
		ActionPanel.add(displayPanel);

		VerticalPanel vPanel = new VerticalPanel();
		final Label errorLabelControl = new Label();
		HorizontalPanel controlPanel = new HorizontalPanel();
		controlPanel.addStyleName("essencePanel");
		controlPanel.setSpacing(10);
		setupControlPanel(controlPanel, errorLabelControl, dataProvider);
		vPanel.add(controlPanel);	
	    
		vPanel.add(errorLabelControl);
		dPanel.addNorth(vPanel, 10);
	}	
	
	// Experimental method to support one more tab and verify user input for roles
	// Currently NOT in use
	public void setupWhoPanels(ScrollPanel whoPanel) {
		
		VerticalPanel namePanel = new VerticalPanel();
		namePanel.addStyleName("essencePanel");
		namePanel.setSpacing(4);

		FlexTable grid = new FlexTable();

		final Button addButton = new Button("Submit Name");
		// We can add style names to widgets
		addButton.addStyleName("sendButton");

		final Label errorLabelAdd = new Label();

		Label nameLabel = new Label("My Name Is: ");
		final TextBox nameBox = new TextBox();
		nameBox.setWidth("220");
		grid.setWidget(0, 0, nameLabel);
		grid.setWidget(0, 1, nameBox);

		Label displayLabel = new Label("The Name Entered Is: ");
		final Label displayName = new Label(NAME);
		grid.setWidget(1, 0, displayLabel);
		grid.setWidget(1, 1, displayName);

		grid.getFlexCellFormatter().setColSpan(2, 1, 2);
		grid.setWidget(2, 0, addButton);
		grid.getFlexCellFormatter().setColSpan(3, 1, 2);
		grid.setWidget(3, 0, errorLabelAdd);

		// Create a handler for the addButton
		class AddButtonHandler implements ClickHandler {

			// Fired when the user clicks on the sendButton.
			public void onClick(ClickEvent event) {
				errorLabelAdd.setText("");

				String name = nameBox.getText();

				// Then, we send the input to the server.
				greetingService.addName(name, new AsyncCallbackAdapter<String>() {
					/*
							public void onFailure(Throwable caught) {
								errorLabelAdd.addStyleName("serverResponseLabelError");
								errorLabelAdd.setText(SERVER_ERROR);
							}
							*/
	    					
	    					// Called by onFailure if the session is still valid
	    					public void doFailureAction() {
								errorLabelAdd.addStyleName("serverResponseLabelError");
								errorLabelAdd.setText(SERVER_ERROR);
	    					}

							public void onSuccess(String result) {
								greetingService.getName(new AsyncCallbackAdapter<String>() {
									/*
											public void onFailure(Throwable caught) {
												errorLabelAdd.setText(SERVER_ERROR);
											}
											*/
											
					    					// Called by onFailure if the session is still valid
					    					public void doFailureAction() {
												errorLabelAdd.addStyleName("serverResponseLabelError");
												errorLabelAdd.setText(SERVER_ERROR);
					    					}

					    					public void onSuccess(String result) {
												if (StringUtil.stringHasValue(result))
													displayName.setText(result);
												else
													displayName.setText("No Name");
											}
										});
							}
						});
			}
		}

		// Add a handler to send the name to the server
		AddButtonHandler handler = new AddButtonHandler();
		addButton.addClickHandler(handler);
		namePanel.add(grid);
		whoPanel.add(namePanel);
	}	
}
