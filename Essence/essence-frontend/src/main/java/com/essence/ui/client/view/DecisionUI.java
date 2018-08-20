/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.view;

import java.util.Date;
import java.util.List;

import com.essence.ui.client.GreetingService;
import com.essence.ui.client.GreetingServiceAsync;
import com.essence.ui.client.object.DecisionDTO;
import com.essence.ui.client.object.DecisionStatusTypeDTO;
import com.essence.ui.client.object.DecisionTypeDTO;
import com.essence.ui.custom.AsyncCallbackAdapter;
import com.essence.ui.custom.HTMLFormatUtil;
import com.essence.ui.custom.MyClickableCellTextDecision;
import com.essence.ui.shared.StringUtil;
import com.google.gwt.cell.client.ButtonCell;
import com.google.gwt.cell.client.FieldUpdater;
import com.google.gwt.core.client.GWT;
import com.google.gwt.event.dom.client.ClickEvent;
import com.google.gwt.event.dom.client.ClickHandler;
import com.google.gwt.user.cellview.client.CellTable;
import com.google.gwt.user.cellview.client.Column;
import com.google.gwt.user.cellview.client.SimplePager;
import com.google.gwt.user.cellview.client.TextColumn;
import com.google.gwt.user.cellview.client.SimplePager.TextLocation;
import com.google.gwt.user.client.Window;
import com.google.gwt.user.client.rpc.AsyncCallback;
import com.google.gwt.user.client.ui.Button;
import com.google.gwt.user.client.ui.DialogBox;
import com.google.gwt.user.client.ui.DockLayoutPanel;
import com.google.gwt.user.client.ui.FlexTable;
import com.google.gwt.user.client.ui.HorizontalPanel;
import com.google.gwt.user.client.ui.Label;
import com.google.gwt.user.client.ui.ListBox;
import com.google.gwt.user.client.ui.ScrollPanel;
import com.google.gwt.user.client.ui.VerticalPanel;
import com.google.gwt.view.client.ListDataProvider;
import com.google.gwt.view.client.SingleSelectionModel;

@SuppressWarnings("unused")
public class DecisionUI {
	// The message displayed to the user when the server cannot be reached or
	// returns an error.
	private static final String SERVER_ERROR = "An error occurred while "
			+ "attempting to contact the server. Please check your network "
			+ "connection and try again.";

	// Create a remote service proxy to talk to the server-side Greeting
	// service.
	private final GreetingServiceAsync greetingService = GWT
			.create(GreetingService.class);
	private final ListDataProvider<DecisionDTO> dataProvider = new ListDataProvider<DecisionDTO>();

	public void updateDataProvider () {
		greetingService.getDecisions(new AsyncCallbackAdapter<List<DecisionDTO>>() {
			/*
			public void onFailure(Throwable caught) {
				//nothing
			}
			*/
			// Called by onFailure if the session is still valid
			public void doFailureAction() {
				//nothing				
			}

			public void onSuccess(List<DecisionDTO> result) {
				dataProvider.setList(result);
			}
		});
	}

	private void setupDecisionDisplayPanel(CellTable<DecisionDTO> table, final ListDataProvider<DecisionDTO> dataProvider) {
		TextColumn<DecisionDTO> idColumn = new TextColumn<DecisionDTO>() {
			@Override
			public String getValue(DecisionDTO r) {
				return r.getId() + "";
			}
		};
		idColumn.setSortable(true);
		table.addColumn(idColumn, "Decision ID");
		table.addColumnStyleName(0, "ar_number_column_style");
				
		TextColumn<DecisionDTO> typeColumn = new TextColumn<DecisionDTO>() {
			@Override
			public String getValue(DecisionDTO r) {
				return r.getDecisionType();
			}
		};
		typeColumn.setSortable(true);
		table.addColumn(typeColumn, "Decision Type");
		table.addColumnStyleName(1, "rule_type_column_style");

		TextColumn<DecisionDTO> refIssueIdColumn = new TextColumn<DecisionDTO>() {
			@Override
			public String getValue(DecisionDTO r) {
				return r.getIssueId()+"";
			}
		};
		refIssueIdColumn.setSortable(true);
		table.addColumn(refIssueIdColumn, "Ref Issue ID");
		table.addColumnStyleName(2, "ar_number_column_style");

		TextColumn<DecisionDTO> refRuleIdColumn = new TextColumn<DecisionDTO>() {
			@Override
			public String getValue(DecisionDTO r) {
				return r.getDecisionRuleId() != null ? r.getDecisionRuleId()+"" : "";
			}
		};
		refRuleIdColumn.setSortable(true);
		table.addColumn(refRuleIdColumn, "Ref Decision Rule ID");
		table.addColumnStyleName(3, "ar_number_column_style");

		TextColumn<DecisionDTO> srcIPColumn = new TextColumn<DecisionDTO>() {
			@Override
			public String getValue(DecisionDTO r) {
				return r.getSourceIPAddress();
			}
		};
		srcIPColumn.setSortable(true);
		table.addColumn(srcIPColumn, "Source IP");
		table.addColumnStyleName(4, "ar_narrow_column_style");

		TextColumn<DecisionDTO> dstIPColumn = new TextColumn<DecisionDTO>() {
			@Override
			public String getValue(DecisionDTO r) {
				return r.getDestinationIPAddress();
			}
		};
		dstIPColumn.setSortable(true);
		table.addColumn(dstIPColumn, "Destination IP");
		table.addColumnStyleName(5, "ar_narrow_column_style");

		TextColumn<DecisionDTO> memoColumn = new TextColumn<DecisionDTO>() {
			@Override
			public String getValue(DecisionDTO r) {
				return r.getMemo();
			}
		};
		memoColumn.setSortable(true);
		table.addColumn(memoColumn, "Memo / Action Type");
		table.addColumnStyleName(6, "ar_wide_column_style");

		final MyClickableCellTextDecision clickableCell = new MyClickableCellTextDecision();
		Column<DecisionDTO,String> severityColumn = new Column<DecisionDTO,String>(clickableCell) {
			@Override
			public String getValue (DecisionDTO d) {
				if (d.getDecisionType().equals(DecisionTypeDTO.MANUAL_ACTION.toString()) && 
						  d.getStatus().equals(DecisionStatusTypeDTO.OPEN.toString())) // && !StringUtil.stringHasValue(d.getMemo()))
					  return "Select Action";
				  else
					  return "N/A";
			}
		};
		table.addColumn(severityColumn, "Manual Action");
		table.addColumnStyleName(7, "ar_narrow_column_style");
		severityColumn.setFieldUpdater(new FieldUpdater<DecisionDTO, String>() {
			 public void update(int index, DecisionDTO d, String value) {
		            if (d != null && value != null && !value.equals("N/A")) {
						showChooseActionDialog(dataProvider, d);
		            }
			  }
		});
		
		
		TextColumn<DecisionDTO> statusColumn = new TextColumn<DecisionDTO>() {
			@Override
			public String getValue(DecisionDTO r) {
				return r.getStatus();
			}
		};
		table.addColumn(statusColumn, "Status");
		table.addColumnStyleName(8, "ar_narrow_column_style");
		
		table.setWidth("100%", true);		
	}
	
	private void setupControlPanel(HorizontalPanel controlPanel, final Label errorLabelControl, 
			final ListDataProvider<DecisionDTO> dataProvider) {
		Label decisionTypeLabel = new Label("Filter Type");

		final ListBox decisionType = new ListBox();
		decisionType.addItem("IGNORE", "IGNORE");
		decisionType.addItem("BLOCK_SOURCE", "BLOCK_SOURCE");
		decisionType.addItem("BLOCK_DESTINATION", "BLOCK_DESTINATION");
		decisionType.addItem("BLOCK_BETWEEN_PAIR", "BLOCK_BETWEEN_PAIR");
		decisionType.addItem("MANUAL_ACTION", "MANUAL_ACTION");
		decisionType.addItem("ALERT_ONLY", "ALERT_ONLY");
		decisionType.setWidth("220");
		controlPanel.add(HTMLFormatUtil.getPaddingLabel());
		controlPanel.add(decisionTypeLabel);
		controlPanel.add(decisionType);

		// Result display button
	    Button displayDecisionByTypeButton = new Button("Show Decisions By Type");
	    displayDecisionByTypeButton.addClickHandler(new ClickHandler() {
	    	public void onClick(ClickEvent event) {
	    		greetingService.getDecisionsByType(
	    				DecisionTypeDTO.valueOf(decisionType.getValue(decisionType.getSelectedIndex())), 
	    				new AsyncCallbackAdapter<List<DecisionDTO>>() {
	    					/*
	    					public void onFailure(Throwable caught) {
	    						errorLabelControl.setText(SERVER_ERROR);
	    					}
	    					*/
	    					// Called by onFailure if the session is still valid
	    					public void doFailureAction() {
	    						errorLabelControl.setText(SERVER_ERROR);
	    					}

	    					public void onSuccess(List<DecisionDTO> result) {
	    						dataProvider.setList(result);
	    					}
	    				});
	        }
	    });
	    controlPanel.add(HTMLFormatUtil.getPaddingLabel());
	    controlPanel.add(displayDecisionByTypeButton);

		// Result display button
	    Button displayAllDecisionsButton = new Button("Show All Decisions");
	    displayAllDecisionsButton.addClickHandler(new ClickHandler() {
	    	public void onClick(ClickEvent event) {
	    		greetingService.getDecisions(new AsyncCallbackAdapter<List<DecisionDTO>>() {
	    			/*
	    			public void onFailure(Throwable caught) {
	    				errorLabelControl.setText(SERVER_ERROR);
	    			}
	    			*/
					// Called by onFailure if the session is still valid
					public void doFailureAction() {
						errorLabelControl.setText(SERVER_ERROR);
					}

	    			public void onSuccess(List<DecisionDTO> result) {
	    				dataProvider.setList(result);
	    			}
	    		});
	        }
	    });
	    controlPanel.add(HTMLFormatUtil.getPaddingLabel());
	    controlPanel.add(displayAllDecisionsButton);
	}
	
	public void setupDecisionPanels(ScrollPanel decisionPanel, DockLayoutPanel dPanel) {
		// Create a CellTable.
		final CellTable<DecisionDTO> table = new CellTable<DecisionDTO>();
		setupDecisionDisplayPanel(table, dataProvider);

		SimplePager.Resources pagerResources = GWT.create(SimplePager.Resources.class);
		SimplePager pager = new SimplePager(TextLocation.CENTER, pagerResources, false, 10, true);
		pager.setDisplay(table);
		dataProvider.addDataDisplay(table);

	    final SingleSelectionModel<DecisionDTO> selectionModel = new SingleSelectionModel<DecisionDTO>();
	    table.setSelectionModel(selectionModel);

		// Set the width of each column.
		// table.setColumnWidth(nameColumn, 35.0, Unit.PCT);
		final Label errorLabelDisplay = new Label();

		greetingService.getDecisions(new AsyncCallbackAdapter<List<DecisionDTO>>() {
			/*
			public void onFailure(Throwable caught) {
				errorLabelDisplay.setText(SERVER_ERROR);
			}
			*/
			// Called by onFailure if the session is still valid
			public void doFailureAction() {
				errorLabelDisplay.setText(SERVER_ERROR);
			}

			public void onSuccess(List<DecisionDTO> result) {
				dataProvider.setList(result);
			}
		});

		VerticalPanel displayPanel = new VerticalPanel();
		displayPanel.add(pager);
		displayPanel.add(table);
		displayPanel.add(errorLabelDisplay);
		displayPanel.setHorizontalAlignment(VerticalPanel.ALIGN_RIGHT);
		decisionPanel.add(displayPanel);

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
	
	private void showChooseActionDialog(final ListDataProvider<DecisionDTO> dataProvider, final DecisionDTO d) {
		// Create the dialog box
		final DialogBox dialogBox = new DialogBox();
		dialogBox.setText("Choose Action for Maunal Action Decision");
		dialogBox.setAnimationEnabled(true);

		VerticalPanel dialogPanel = new VerticalPanel();
		dialogPanel.addStyleName("essencePanel");
		dialogPanel.setSpacing(6);

		FlexTable grid = new FlexTable();

		final Button saveButton = new Button("Save");
		// We can add style names to widgets
		saveButton.addStyleName("sendButton");

		final Button cancelButton = new Button("Cancel");
		cancelButton.addStyleName("sendButton");
		cancelButton.addClickHandler(new ClickHandler() {
			public void onClick(ClickEvent event) {
				dialogBox.hide();
			}
		});

		final Label errorLabelAdd = new Label();

		Label idLabel = new Label("Decision ID");
		Label id = new Label(d.getId()+"");
		grid.setWidget(0, 0, idLabel);
		grid.setWidget(0, 1, id);

		Label decisionTypeLabel = new Label("Decision Type");
		Label decisionType = new Label(d.getDecisionType());
		grid.setWidget(1, 0, decisionTypeLabel);
		grid.setWidget(1, 1, decisionType);

		Label refRuleIDLabel = new Label("Ref Rule ID");
		Label refRuleID = new Label(d.getDecisionRuleId()+"");
		grid.setWidget(2, 0, refRuleIDLabel);
		grid.setWidget(2, 1, refRuleID);

		Label issueIDLabel = new Label("Issue ID");
		Label issueID = new Label(d.getIssueId()+"");
		grid.setWidget(3, 0, issueIDLabel);
		grid.setWidget(3, 1, issueID);

		Label srcIPLabel = new Label("Source IP");
		Label srcIP = new Label(d.getSourceIPAddress());
		grid.setWidget(4, 0, srcIPLabel);
		grid.setWidget(4, 1, srcIP);

		Label dstIPLabel = new Label("Destination IP");
		Label dstIP = new Label(d.getDestinationIPAddress());
		grid.setWidget(5, 0, dstIPLabel);
		grid.setWidget(5, 1, dstIP);

		Label issueDetailLabel = new Label("Issue Detail");
		Label issueDetail = new Label(d.getIssue().getDescription());
		grid.setWidget(6, 0, issueDetailLabel);
		grid.setWidget(6, 1, issueDetail);

		Label statusLabel = new Label("Status");
		Label status = new Label(d.getStatus());
		grid.setWidget(7, 0, statusLabel);
		grid.setWidget(7, 1, status);

		Label actionTypeLabel = new Label("Action Type");
		final ListBox actionType = new ListBox();
		actionType.addItem("", "");
		actionType.addItem("IGNORE", "IGNORE");
		actionType.addItem("BLOCK_SOURCE", "BLOCK_SOURCE");
		actionType.addItem("BLOCK_DESTINATION", "BLOCK_DESTINATION");
		actionType.addItem("BLOCK_BETWEEN_PAIR", "BLOCK_BETWEEN_PAIR");
		actionType.addItem("ALERT_ONLY", "ALERT_ONLY");
		actionType.setWidth("220");
		actionType.setSelectedIndex(0);
		if (d.getMemo() != null && d.getMemo().equals("IGNORE"))
			actionType.setSelectedIndex(1);
		else if (d.getMemo() != null && d.getMemo().equals("BLOCK_SOURCE"))
			actionType.setSelectedIndex(2);
		else if (d.getMemo() != null && d.getMemo().equals("BLOCK_DESTINATION"))
			actionType.setSelectedIndex(3);
		else if (d.getMemo() != null && d.getMemo().equals("BLOCK_BETWEEN_PAIR"))
			actionType.setSelectedIndex(4);
		else if (d.getMemo() != null && d.getMemo().equals("ALERT_ONLY"))
			actionType.setSelectedIndex(5);
		grid.setWidget(8, 0, actionTypeLabel);
		grid.setWidget(8, 1, actionType);

		grid.setWidget(9, 0, saveButton);
		grid.setWidget(9, 1, cancelButton);

		grid.getFlexCellFormatter().setColSpan(10, 1, 2);
		grid.setWidget(10, 0, errorLabelAdd);

		// Create a handler for the addButton
		class SaveButtonHandler implements ClickHandler {

			// Fired when the user clicks on the sendButton.
			public void onClick(ClickEvent event) {
				saveActionType();
			}

			/**
			 * Send the rule data to the server to be added to the database and
			 * wait for a response.
			 */
			private void saveActionType() {
				errorLabelAdd.setText("");
				// TODO-First, we validate the input.
				DecisionTypeDTO decisionType = null;
				try {
					decisionType = DecisionTypeDTO.valueOf(actionType.getValue(actionType.getSelectedIndex()));			
				} catch (Exception ex) {
					//System.out.println(ex.getMessage());
				}

				// Then, we send the input to the server.
				greetingService.setActionTypeOnManualDecision(d, decisionType, 
						new AsyncCallbackAdapter<String>() {/*
							public void onFailure(Throwable caught) {
								dialogBox
										.setText("Remote Procedure Call - Failure");
								errorLabelAdd
										.addStyleName("serverResponseLabelError");
								errorLabelAdd.setText(SERVER_ERROR);
								dialogBox.center();
								dialogBox.hide();
							}
							*/
	    					// Called by onFailure if the session is still valid
	    					public void doFailureAction() {
								dialogBox.setText("Remote Procedure Call - Failure");
								errorLabelAdd.addStyleName("serverResponseLabelError");
								errorLabelAdd.setText(SERVER_ERROR);
								dialogBox.center();
								dialogBox.hide();
	    					}

							public void onSuccess(String result) {
								greetingService.getDecisions(new AsyncCallbackAdapter<List<DecisionDTO>>() {
									/*
											public void onFailure(
													Throwable caught) {
												errorLabelAdd
														.setText(SERVER_ERROR);
											}
											*/
					    					// Called by onFailure if the session is still valid
					    					public void doFailureAction() {
					    						errorLabelAdd.setText(SERVER_ERROR);
					    					}

											public void onSuccess(
													List<DecisionDTO> result) {
												dataProvider.setList(result);
												dataProvider.refresh();
											}

										});
								dialogBox.setText("Remote Procedure Call");
								dialogBox.center();
								dialogBox.hide();
							}
						});
			}
		}

		// Add a handler to send the name to the server
		SaveButtonHandler handler = new SaveButtonHandler();
		saveButton.addClickHandler(handler);
		dialogPanel.add(grid);
		dialogBox.setWidget(dialogPanel);
		int left = Window.getClientWidth() / 3;
		int top = Window.getClientHeight() / 5;
		dialogBox.setPopupPosition(left, top);
		dialogBox.show();
	}	
}
