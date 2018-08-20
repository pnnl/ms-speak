/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.view;

import java.util.List;
import java.util.Objects;

import com.essence.ui.client.GreetingService;
import com.essence.ui.client.GreetingServiceAsync;
import com.essence.ui.client.object.*;
import com.essence.ui.custom.AsyncCallbackAdapter;
import com.essence.ui.custom.HTMLFormatUtil;
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
import com.google.gwt.user.client.ui.Button;
import com.google.gwt.user.client.ui.DialogBox;
import com.google.gwt.user.client.ui.DockLayoutPanel;
import com.google.gwt.user.client.ui.FlexTable;
import com.google.gwt.user.client.ui.HorizontalPanel;
import com.google.gwt.user.client.ui.Label;
import com.google.gwt.user.client.ui.ListBox;
import com.google.gwt.user.client.ui.ScrollPanel;
import com.google.gwt.user.client.ui.TextBox;
import com.google.gwt.user.client.ui.VerticalPanel;
import com.google.gwt.view.client.ListDataProvider;
import com.google.gwt.view.client.SingleSelectionModel;

public class DecisionRuleUI {
	// The message displayed to the user when the server cannot be reached or
	// returns an error.
	private static final String SERVER_ERROR = "An error occurred while "
			+ "attempting to contact the server. Please check your network "
			+ "connection and try again.";

	// Create a remote service proxy to talk to the server-side Greeting
	// service.
	private final GreetingServiceAsync greetingService = GWT
			.create(GreetingService.class);
	private final ListDataProvider<DecisionRuleDTO> dataProvider = new ListDataProvider<>();
	private void setupDecisionRuleDisplayPanel(CellTable<DecisionRuleDTO> table, final Label errorLabelDisplay) {
		TextColumn<DecisionRuleDTO> idColumn = new TextColumn<DecisionRuleDTO>() {
			@Override
			public String getValue(DecisionRuleDTO r) {
				return r.getId() + "";
			}
		};
		idColumn.setSortable(true);
		table.addColumn(idColumn, "Rule ID");
		table.addColumnStyleName(0, "ar_number_column_style");

		TextColumn<DecisionRuleDTO> typeColumn = new TextColumn<DecisionRuleDTO>() {
			@Override
			public String getValue(DecisionRuleDTO r) {
				return r.getDetectionRuleType();
			}
		};
		table.addColumn(typeColumn, "Violated Rule Type");
		table.addColumnStyleName(1, "rule_type_column_style");

		TextColumn<DecisionRuleDTO> refRuleIdColumn = new TextColumn<DecisionRuleDTO>() {
			@Override
			public String getValue(DecisionRuleDTO r) {
				if (r.getDetectionRuleRef() != null)
					return r.getDetectionRuleRef()+"";
				else
					return "";
			}
		};
		table.addColumn(refRuleIdColumn, "Ref Violated Rule ID");
		table.addColumnStyleName(2, "ar_number_column_style");

		TextColumn<DecisionRuleDTO> severityColumn = new TextColumn<DecisionRuleDTO>() {
			@Override
			public String getValue(DecisionRuleDTO r) {
				return r.getSeverityType();
			}
		};
		table.addColumn(severityColumn, "Severity");
		table.addColumnStyleName(3, "ar_time_column_style");

        TextColumn<DecisionRuleDTO> causeColumn = new TextColumn<DecisionRuleDTO>() {
            @Override
            public String getValue(DecisionRuleDTO r) {
                return r.getCause() != null ? r.getCause().getCause() : "";
            }
        };
        table.addColumn(causeColumn, "Cause");
        table.addColumnStyleName(4, "ar_time_column_style");

        TextColumn<DecisionRuleDTO> stateColumn = new TextColumn<DecisionRuleDTO>() {
            @Override
            public String getValue(DecisionRuleDTO r) {
                return r.getState() != null ? r.getState().getState() : "";
            }
        };
        table.addColumn(stateColumn, "State");
        table.addColumnStyleName(5, "ar_time_column_style");

		TextColumn<DecisionRuleDTO> decisionColumn = new TextColumn<DecisionRuleDTO>() {
			@Override
			public String getValue(DecisionRuleDTO r) {
				return r.getDecisionType();
			}
		};
		table.addColumn(decisionColumn, "Decision Type");
		table.addColumnStyleName(6, "ar_wide_column_style");
		
		/*
		TextColumn<DecisionRuleDTO> priorityColumn = new TextColumn<DecisionRuleDTO>() {
			@Override
			public String getValue(DecisionRuleDTO r) {
				return r.getPriority()+"";
			}
		};
		table.addColumn(priorityColumn, "Priority");
		table.addColumnStyleName(5, "ar_number_column_style");
		*/
		ButtonCell buttonCell = new ButtonCell();
		Column<DecisionRuleDTO, String> buttonColumn = new Column<DecisionRuleDTO, String>(buttonCell) {
		  @Override
		  public String getValue(DecisionRuleDTO dr) {
		    // The value to display in the button.
		    return "Delete";
		  }
		};
		table.addColumn(buttonColumn, "Operation");
		buttonColumn.setFieldUpdater(new FieldUpdater<DecisionRuleDTO, String>() {
			  public void update(int index, DecisionRuleDTO dr, String value) {
			    // Value is the button value.  Object is the row object.
			   // Window.alert("You clicked: " + value + " and index = " + index + " id = " + dr.getId());
	            if (dr != null) {
	                dataProvider.getList().remove(dr);
					greetingService.removeDecisionRule(dr,
							new AsyncCallbackAdapter<String>() {
		    					// Called by onFailure if the session is still valid
		    					public void doFailureAction() {
									errorLabelDisplay.setText(SERVER_ERROR);
		    					}

								public void onSuccess(String result) {
									//no-op
								}
							});
	            }
			  }
			});
		
		table.setWidth("100%", true);		
	}
	
	private void setupControlPanel(HorizontalPanel controlPanel, final Label errorLabelActivateDetector, final ListDataProvider<DecisionRuleDTO> dataProvider) {
		// Filter based on violation type panel
		Label detectorTypeLabel = new Label("Violation Type");

		final ListBox detectorType = new ListBox();
		detectorType.setName("Detector Type ");
		detectorType.setTitle("Detector Type Title");
		detectorType.addItem("N/A", "N/A");
		detectorType.addItem("MS_EP_CONNECTIVITY", "MS_EP_CONNECTIVITY");
		//detectorType.addItem("WRONG_MSG_TO_MS_EP", "WRONG_MSG_TO_MS_EP");
		//detectorType.addItem("ERR_MSG_FROM_MS_EP", "ERR_MSG_FROM_MS_EP");
		//detectorType.addItem("WRONG_MSG_FORMAT", "WRONG_MSG_FORMAT");
		detectorType.addItem("DENIAL_OF_SERVICE", "DENIAL_OF_SERVICE");
		//detectorType.addItem("NW_SEGMENTATION", "NW_SEGMENTATION");
		//detectorType.addItem("NEW_HOST", "NEW_HOST");
		detectorType.addItem("CAUSE/STATE", "CAUSE/STATE");
		detectorType.setWidth("220");
		controlPanel.add(detectorTypeLabel);
		controlPanel.add(detectorType);

		// Add decision rule button
	    final Button addDecisionRuleButton = new Button("Add Decision Rule for Violation Type");
	    addDecisionRuleButton.addClickHandler(new ClickHandler() {
	    	public void onClick(ClickEvent event) {
				String type = detectorType.getValue(detectorType.getSelectedIndex());
				showCreateDecisionRuleDialog(type, addDecisionRuleButton, dataProvider);
	        }
	    });
	    controlPanel.add(HTMLFormatUtil.getPaddingLabel());
	    controlPanel.add(addDecisionRuleButton);

		// Result display button
	    Button displayDecisionRulesByTypetButton = new Button("Show Decision Rules for Violation Type");
	    displayDecisionRulesByTypetButton.addClickHandler(new ClickHandler() {
	    	public void onClick(ClickEvent event) {
				String type = detectorType.getValue(detectorType.getSelectedIndex());
				DetectionRuleTypeDTO drType = DetectionRuleTypeDTO.textToValue(type);
	    		if (drType != null )
	    			greetingService.getDecisionRulesByViolationType(DetectionRuleTypeDTO.valueOf(detectorType.getValue(detectorType.getSelectedIndex())), 
	    				new AsyncCallbackAdapter<List<DecisionRuleDTO>>() {
	    					// Called by onFailure if the session is still valid
	    					public void doFailureAction() {
	    						errorLabelActivateDetector.setText(SERVER_ERROR);
	    					}

	    					public void onSuccess(List<DecisionRuleDTO> result) {
	    						dataProvider.setList(result);
	    					}
	    				});
	    		else
		    		greetingService.getDecisionRules(new AsyncCallbackAdapter<List<DecisionRuleDTO>>() {
    					// Called by onFailure if the session is still valid
    					public void doFailureAction() {
    						errorLabelActivateDetector.setText(SERVER_ERROR);
    					}

		    			public void onSuccess(List<DecisionRuleDTO> result) {
		    				dataProvider.setList(result);
		    			}
		    		});
	        }
	    });
	    controlPanel.add(HTMLFormatUtil.getPaddingLabel());
	    controlPanel.add(displayDecisionRulesByTypetButton);

		// Result display button
	    Button displayAllDecisionRuleButton = new Button("Show All Decision Rules");
	    displayAllDecisionRuleButton.addClickHandler(new ClickHandler() {
	    	public void onClick(ClickEvent event) {
	    		greetingService.getDecisionRules(new AsyncCallbackAdapter<List<DecisionRuleDTO>>() {
					// Called by onFailure if the session is still valid
					public void doFailureAction() {
						errorLabelActivateDetector.setText(SERVER_ERROR);
					}

	    			public void onSuccess(List<DecisionRuleDTO> result) {
	    				dataProvider.setList(result);
	    			}
	    		});
	        }
	    });
	    controlPanel.add(HTMLFormatUtil.getPaddingLabel());
	    controlPanel.add(displayAllDecisionRuleButton);	    
	}
	
	public void updateDataProvider() {
		greetingService.getDecisionRules(new AsyncCallbackAdapter<List<DecisionRuleDTO>>() {
			// Called by onFailure if the session is still valid
			public void doFailureAction() {
				//nothing
			}

			public void onSuccess(List<DecisionRuleDTO> result) {
				dataProvider.setList(result);
			}
		});
	}
	
	private void showCreateDecisionRuleDialog(final String type, final Button buttonToEnable,
			final ListDataProvider<DecisionRuleDTO> dataProvider) {
        final boolean isDetectionRuleType = !Objects.equals(type, "CAUSE/STATE");

		// Create the dialog box
		final DialogBox dialogBox = new DialogBox();
		dialogBox.setText("Create Decision Rule for Violation Type " + type);
		dialogBox.setAnimationEnabled(true);

		VerticalPanel dialogPanel = new VerticalPanel();
		dialogPanel.addStyleName("essencePanel");
		dialogPanel.setSpacing(4);

		FlexTable grid = new FlexTable();

		final Button addButton = new Button("Create");
		// We can add style names to widgets
		addButton.addStyleName("sendButton");

		final Button cancelButton = new Button("Cancel");
		cancelButton.addStyleName("sendButton");
		cancelButton.addClickHandler(new ClickHandler() {
			public void onClick(ClickEvent event) {
				dialogBox.hide();
				buttonToEnable.setEnabled(true);
				buttonToEnable.setFocus(true);
			}
		});

		final Label errorLabelAdd = new Label();

		Label detectionTypePromptLabel = new Label("Violation Type");
		Label detectionTypeValueLabel = new Label(type);
		detectionTypePromptLabel.setWidth("220");
		grid.setWidget(0, 0, detectionTypePromptLabel);
		grid.setWidget(0, 1, detectionTypeValueLabel);

		final TextBox detectionRuleRef = new TextBox();
		final ListBox severity = new ListBox();
		final ListBox cause = new ListBox();
		final ListBox state = new ListBox();

		if (isDetectionRuleType) {
			Label detectionRuleRefLabel = new Label("Violation Rule Ref ID");
			detectionRuleRef.setWidth("220");
			grid.setWidget(1, 0, detectionRuleRefLabel);
			grid.setWidget(1, 1, detectionRuleRef);

			Label severityLabel = new Label("Severity");
			severity.addItem("N/A", "N/A");
			severity.addItem("HIGH", "HIGH");
			severity.addItem("MEDIUM", "MEDIUM");
			severity.addItem("LOW", "LOW");
			severity.addItem("INFORMATIONAL", "INFORMATIONAL");
			severity.setWidth("220");
			grid.setWidget(2, 0, severityLabel);
			grid.setWidget(2, 1, severity);
		}
		else if (Objects.equals(type, "CAUSE/STATE")) {
            cause.addItem("", "");
            state.addItem("", "");

			greetingService.getCauses(new AsyncCallbackAdapter<List<CauseDTO>>() {
				@Override
				public void doFailureAction() {

				}

				@Override
				public void onSuccess(List<CauseDTO> causeDTOs) {
					for (CauseDTO c : causeDTOs) {
						cause.addItem(c.getCause(), c.getId().toString());
					}
				}
			});

			greetingService.getAnomalyStates(new AsyncCallbackAdapter<List<AnomalyStateDTO>>() {
				@Override
				public void doFailureAction() {

				}

				@Override
				public void onSuccess(List<AnomalyStateDTO> anomalyStateDTOs) {
					for (AnomalyStateDTO s : anomalyStateDTOs) {
						state.addItem(s.getState(), s.getId().toString());
					}
				}
			});

			Label causeLabel = new Label("Cause");
			cause.setWidth("220");
			grid.setWidget(1, 0, causeLabel);
			grid.setWidget(1, 1, cause);

			Label stateLabel = new Label("State");
			cause.setWidth("220");
			grid.setWidget(2, 0, stateLabel);
			grid.setWidget(2, 1, state);
		}

		Label decisionLabel = new Label("Decision Type");
		final ListBox decision = new ListBox();
		decision.addItem("IGNORE", "IGNORE");
		decision.addItem("BLOCK_SOURCE", "BLOCK_SOURCE");
		decision.addItem("BLOCK_DESTINATION", "BLOCK_DESTINATION");
		decision.addItem("BLOCK_BETWEEN_PAIR", "BLOCK_BETWEEN_PAIR");
		//decision.addItem("ASSIGN_SEVERITY", "ASSIGN_SEVERITY");
		decision.addItem("MANUAL_ACTION", "MANUAL_ACTION");
		decision.addItem("ALERT_ONLY", "ALERT_ONLY");
		//decision.addItem("AUTO_SUPPRESS", "AUTO_SUPPRESS");
		decision.setWidth("220");
		grid.setWidget(3, 0, decisionLabel);
		grid.setWidget(3, 1, decision);
/*
		Label priorityLabel = new Label("Priority");
		final TextBox priority = new TextBox();
		detectionRuleRef.setWidth("220");
		grid.setWidget(4, 0, priorityLabel);
		grid.setWidget(4, 1, priority);
*/
		grid.setWidget(4, 0, addButton);
		grid.setWidget(4, 1, cancelButton);
		grid.getFlexCellFormatter().setColSpan(5, 1, 2);
		grid.setWidget(5, 0, errorLabelAdd);

		// Create a handler for the addButton
		class AddButtonHandler implements ClickHandler {

			// Fired when the user clicks on the sendButton.
			public void onClick(ClickEvent event) {
				addRule();
			}

			/**
			 * Send the rule data to the server to be added to the database and
			 * wait for a response.
			 */
			private void addRule() {
				errorLabelAdd.setText("");
				DecisionRuleDTO rule = new DecisionRuleDTO();
                if (isDetectionRuleType) {
                    if (DetectionRuleTypeDTO.textToValue(type) != null)
                        rule.setDetectionRuleType(DetectionRuleTypeDTO.textToValue(type));
                    if (StringUtil.textToInteger(detectionRuleRef.getText()) != null) {
                        rule.setDetectionRuleRef(StringUtil.textToInteger(detectionRuleRef.getText()));
                    }
                    rule.setSeverityType(SeverityTypeDTO.textToValue(severity.getValue(severity.getSelectedIndex())));
                }
				else if (Objects.equals(type, "CAUSE/STATE")) {
                    if (cause.getSelectedIndex() > 0) {
                        CauseDTO causeDTO = new CauseDTO();
                        causeDTO.setId(Long.parseLong(cause.getValue(cause.getSelectedIndex())));
                        rule.setCause(causeDTO);
                    }

                    if (state.getSelectedIndex() > 0) {
                        AnomalyStateDTO stateDTO = new AnomalyStateDTO();
                        stateDTO.setId(Long.parseLong(state.getValue(state.getSelectedIndex())));
                        rule.setState(stateDTO);
                    }
				}
				rule.setDecisionType(DecisionTypeDTO.textToValue(decision.getValue(decision.getSelectedIndex())));

				// Then, we send the input to the server.
				greetingService.addDecisionRule(rule,
						new AsyncCallbackAdapter<String>() {
							// Called by onFailure if the session is still valid
							public void doFailureAction() {
								dialogBox.setText("Remote Procedure Call - Failure");
								errorLabelAdd.addStyleName("serverResponseLabelError");
								errorLabelAdd.setText(SERVER_ERROR);
								dialogBox.center();
								buttonToEnable.setFocus(true);
								dialogBox.hide();
							}

							public void onSuccess(String result) {
								greetingService.getDecisionRules(new AsyncCallbackAdapter<List<DecisionRuleDTO>>() {
											// Called by onFailure if the session is still valid
											public void doFailureAction() {
												errorLabelAdd.setText(SERVER_ERROR);
											}

											public void onSuccess(
													List<DecisionRuleDTO> result) {
												dataProvider.setList(result);
												dataProvider.refresh();
											}

										});
								buttonToEnable.setEnabled(true);
								dialogBox.setText("Remote Procedure Call");
								dialogBox.center();
								buttonToEnable.setFocus(true);
								dialogBox.hide();
							}
						});
			}
		}

		// Add a handler to send the name to the server
		AddButtonHandler handler = new AddButtonHandler();
		addButton.addClickHandler(handler);
		buttonToEnable.setEnabled(false);
		dialogPanel.add(grid);
		dialogBox.setWidget(dialogPanel);
		int left = Window.getClientWidth() / 3;
		int top = Window.getClientHeight() / 5;
		dialogBox.setPopupPosition(left, top);
		dialogBox.show();
	}

	public void setupDecisionRulePanel(ScrollPanel analyzerPanel, DockLayoutPanel dPanel) {
		

		final Label errorLabelDisplay = new Label();

		// Create a CellTable.
		final CellTable<DecisionRuleDTO> table = new CellTable<>();
		setupDecisionRuleDisplayPanel(table, errorLabelDisplay);

		SimplePager.Resources pagerResources = GWT.create(SimplePager.Resources.class);
		SimplePager pager = new SimplePager(TextLocation.CENTER, pagerResources, false, 10, true);
		pager.setDisplay(table);
		dataProvider.addDataDisplay(table);

		final SingleSelectionModel<DecisionRuleDTO> selectionModel = new SingleSelectionModel<>();
	    table.setSelectionModel(selectionModel);

		greetingService.getDecisionRules(new AsyncCallbackAdapter<List<DecisionRuleDTO>>() {
			// Called by onFailure if the session is still valid
			public void doFailureAction() {
				errorLabelDisplay.setText(SERVER_ERROR);
			}

			public void onSuccess(List<DecisionRuleDTO> result) {
				dataProvider.setList(result);
			}
		});

		VerticalPanel displayPanel = new VerticalPanel();
		displayPanel.add(pager);
		displayPanel.add(table);
		displayPanel.add(errorLabelDisplay);
		displayPanel.setHorizontalAlignment(VerticalPanel.ALIGN_RIGHT);
		analyzerPanel.add(displayPanel);
		
		VerticalPanel vPanel = new VerticalPanel();
		final Label errorLabelActivateDetector = new Label();
		HorizontalPanel addRuleAndFilterPanel = new HorizontalPanel();
		addRuleAndFilterPanel.addStyleName("essencePanel");
		addRuleAndFilterPanel.setSpacing(10);
		setupControlPanel(addRuleAndFilterPanel, errorLabelActivateDetector, dataProvider);
		vPanel.add(addRuleAndFilterPanel);	
	    
		vPanel.add(errorLabelActivateDetector);
		dPanel.addNorth(vPanel, 10);
	}
}
