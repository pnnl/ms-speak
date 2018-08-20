/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.view;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Map;

import com.essence.ui.client.GreetingService;
import com.essence.ui.client.GreetingServiceAsync;
import com.essence.ui.client.object.AnalyzerResultDTO;
import com.essence.ui.client.object.AnalyzerResultStatusTypeDTO;
import com.essence.ui.client.object.DetectionRuleDTO;
import com.essence.ui.client.object.DetectionRuleTypeDTO;
import com.essence.ui.client.object.SeverityTypeDTO;
import com.essence.ui.client.object.ValueOutOfBoundDetailDTO;
import com.essence.ui.custom.AsyncCallbackAdapter;
import com.essence.ui.custom.ClickableTextCellRuleID;
import com.essence.ui.custom.HTMLFormatUtil;
import com.essence.ui.custom.MyClickableCellText;
import com.essence.ui.custom.WrapCsvString;
import com.essence.ui.custom.WrapString;
import com.essence.ui.custom.WrappedCsvStringColumn;
import com.essence.ui.custom.WrappedStringColumn;
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
import com.google.gwt.user.client.ui.DecoratorPanel;
import com.google.gwt.user.client.ui.DialogBox;
import com.google.gwt.user.client.ui.DockLayoutPanel;
import com.google.gwt.user.client.ui.FlexTable;
import com.google.gwt.user.client.ui.HorizontalPanel;
import com.google.gwt.user.client.ui.Label;
import com.google.gwt.user.client.ui.ListBox;
import com.google.gwt.user.client.ui.ScrollPanel;
import com.google.gwt.user.client.ui.TextBox;
import com.google.gwt.user.client.ui.VerticalPanel;
import com.google.gwt.user.client.ui.HTMLTable.RowFormatter;
import com.google.gwt.view.client.ListDataProvider;
import com.google.gwt.view.client.SingleSelectionModel;

@SuppressWarnings("unused")
public class AnalyzerAndReportUI {
	// The message displayed to the user when the server cannot be reached or
	// returns an error.
	private static final String SERVER_ERROR = "An error occurred while "
			+ "attempting to contact the server. Please check your network "
			+ "connection and try again.";

	// Create a remote service proxy to talk to the server-side Greeting
	// service.
	private final GreetingServiceAsync greetingService = GWT
			.create(GreetingService.class);
	private final ListDataProvider<AnalyzerResultDTO> dataProvider = new ListDataProvider<AnalyzerResultDTO>();
	
	public void updateDataProvider() {
//		greetingService.getAnalyzerResults(new AsyncCallbackAdapter<List<AnalyzerResultDTO>>() {
//
//			// Called by onFailure if the session is still valid
//			public void doFailureAction() {
//				// nothing
//			}
//
//			public void onSuccess(List<AnalyzerResultDTO> result) {
//				dataProvider.setList(result);
//			}
//		});
	}
	
	private void setupAnalyzeResultDisplayPanel(CellTable<AnalyzerResultDTO> table,
												final ListDataProvider<AnalyzerResultDTO> dataProvider) {
		final ClickableTextCellRuleID clickableIDcell = new ClickableTextCellRuleID();

		Column<AnalyzerResultDTO,String> ruleIDColumn = new Column<AnalyzerResultDTO,String>(clickableIDcell) {
			@Override
			public String getValue (AnalyzerResultDTO dr) {
				if (dr.getRefRuleId() == null)
					  return "none";
				else
					  return dr.getRefRuleId().toString();
			}
		};
		table.addColumn(ruleIDColumn, "Ref Rule ID");
		table.addColumnStyleName(2, "ar_number_column_style");
		ruleIDColumn.setFieldUpdater(new FieldUpdater<AnalyzerResultDTO,String> () {
			public void update(int index, AnalyzerResultDTO ar, String value) {
				showRuleDetailDialog(ar);
			}
		});
	}

	private void showRuleDetailDialog(final AnalyzerResultDTO ar ) {
		greetingService.getDetectionRuleByID(ar.getRefRuleId(), new AsyncCallbackAdapter<DetectionRuleDTO>() {
			public void onSuccess(final DetectionRuleDTO dr) {
				
				final DialogBox dialogBox = new DialogBox();
				dialogBox.setText("Detection Rule Details");
				dialogBox.setAnimationEnabled(true);
				
				final FlexTable grid = new FlexTable();
				grid.setStyleName("flex_table_style");
				final VerticalPanel dialogPanel = new VerticalPanel();
				dialogPanel.addStyleName("essencePanel");
				dialogPanel.setSpacing(6);
				
				final Button closeButton = new Button("Close");
				closeButton.addStyleName("sendButton");
				closeButton.addClickHandler(new ClickHandler() {
					public void onClick(ClickEvent event) {
						dialogBox.hide();
					}
				});
				
				int i = 0;
				Label idLabel = new Label("Rule ID");
				Label id = new Label(dr.getId() + "");
				grid.getFlexCellFormatter().setColSpan(i, 1, 4);
				grid.setWidget(i, 0, idLabel);
				grid.setWidget(i, 1, id);
				i++;
				
				Label ruleType = new Label("Detection Rule Type");
				Label rule = new Label(dr.getRuleType());
				grid.getFlexCellFormatter().setColSpan(i, 1, 4);
				grid.setWidget(i, 0, ruleType);
				grid.setWidget(i, 1, rule);
				i++;
				final int currentRowNumber = i;
				
				if (dr.getRuleType().equals(DetectionRuleTypeDTO.VALUE_OUT_OF_BOUND.toString())) {
						//Window.alert("getting VOOB details for " + dr.getId());
						List<Integer> ruleIds = new ArrayList<>();
						ruleIds.add(dr.getId());
						greetingService.getValueOutOfBoundRuleDetails(ruleIds, new AsyncCallbackAdapter<Map<Integer,
								List<ValueOutOfBoundDetailDTO>>>() {
									public void doFailureAction() {
									}

									public void onSuccess(Map<Integer, List<ValueOutOfBoundDetailDTO>> detailMap) {
										List<ValueOutOfBoundDetailDTO> details = detailMap.get(dr.getId());
										dr.setVoobDetails(details);

										Label protocolLabel = new Label("Protocol");
										protocolLabel.setStyleName("xpath_instructions_style");
										Label protocolValueLabel = new Label("MultiSpeak " + dr.getVersion()); 
										int row = currentRowNumber;
										grid.getFlexCellFormatter().setColSpan(row, 1, 4);
										grid.setWidget(row, 0, protocolLabel);
										grid.setWidget(row, 1, protocolValueLabel);
										row++;

										if (details != null && !details.isEmpty()) {
											int msgIdx = dr.getNonHeaderIndexOfVooBDetails();
											
											Label epLabel = new Label("Endpoint Code");
											epLabel.setStyleName("xpath_instructions_style");
											Label endpointType = new Label();
											endpointType.setText(details.get(msgIdx).getEndpointCode());
											grid.getFlexCellFormatter().setColSpan(row, 1, 4);
											grid.setWidget(row, 0, epLabel);
											grid.setWidget(row, 1, endpointType);
											row++;

											grid.getFlexCellFormatter().setColSpan(row, 1, 4);
											Label msgNameLabel = new Label("Message Name");
											msgNameLabel.setStyleName("xpath_instructions_style");
											grid.setWidget(row, 0, msgNameLabel);
											grid.setWidget(row, 1, new Label(details.get(msgIdx).getMessageName()));
											row++;
											
											grid.getFlexCellFormatter().setColSpan(row, 1, 4);
											Label ruleTitleLabel = new Label("Rule Title");
											ruleTitleLabel.setStyleName("xpath_instructions_style");
											grid.setWidget(row, 0, ruleTitleLabel);
											grid.setWidget(row, 1, new Label(dr.getVoobTitle()));
											row++;
											
											int xPathCount = 1;
											for (ValueOutOfBoundDetailDTO d : details) {
												
												grid.getFlexCellFormatter().setColSpan(row, 3, 2);
												Label xpathLabel = new Label("Xpath-Condition-"+ xPathCount);
												xpathLabel.setStyleName("xpath_instructions_style");

												grid.setWidget(row, 0, xpathLabel);
												grid.setWidget(row, 1, new Label(d.getFieldName()));
												grid.setWidget(row, 2, new Label(d.getKey().getOperator()));
												grid.setWidget(row, 3, new Label(d.getTargetValue()));
												row++;
												grid.getFlexCellFormatter().setColSpan(row, 1, 4);
												Label xpath = new Label(d.getXpath().replace("/", " /"));
												xpath.setStyleName("xpath_label_width");
												grid.setWidget(row, 1, xpath);

												xPathCount++;
												row++;
											}		
										}
										grid.getFlexCellFormatter().setColSpan(row, 0, 5);
										grid.setWidget(row, 0, closeButton);
										
										dialogPanel.add(grid);
										dialogBox.setWidget(dialogPanel);
										int left = Window.getClientWidth() / 3;
										int top = Window.getClientHeight() / 5;
										dialogBox.setPopupPosition(left, top);
										dialogBox.show();

									}
							});

				} else {
					Label versionLabel = new Label("MultiSpeak Version");
					Label version = new Label(dr.getVersion());
					grid.getFlexCellFormatter().setColSpan(i, 1, 4);
					grid.setWidget(i, 0, versionLabel);
					grid.setWidget(i, 1, version);
					i++;
	
					Label sourceEPType = new Label("Source EP Type");
					Label epType = new Label(dr.getSrcEndpointType());
					grid.getFlexCellFormatter().setColSpan(i, 1, 4);
					grid.setWidget(i, 0, sourceEPType);
					grid.setWidget(i, 1, epType);
					i++;
					
					Label destEPType = new Label("Dest EP Type");
					Label destType = new Label(dr.getDstEndpointType());
					grid.getFlexCellFormatter().setColSpan(i, 1, 4);
					grid.setWidget(i, 0, destEPType);
					grid.setWidget(i, 1, destType);
					i++;
					
					Label sourceIPLabel = new Label("Source IP");
					Label sourceIP = new Label(dr.getSrcIPAddress());
					grid.getFlexCellFormatter().setColSpan(i, 1, 4);
					grid.setWidget(i, 0, sourceIPLabel);
					grid.setWidget(i, 1, sourceIP);
					i++;
					
					Label destIPLabel = new Label("Dest IP");
					Label destIP = new Label(dr.getSrcIPAddress());
					grid.getFlexCellFormatter().setColSpan(i, 1, 4);
					grid.setWidget(i, 0, destIPLabel);
					grid.setWidget(i, 1, destIP);
					i++;
					
					if(dr.getRuleType().equals("DENIAL_OF_SERVICE")) {
						Label DOSPacketLabel = new Label("DOS Packets");
						Label dosPacket = new Label(dr.getSrcIPAddress());
						grid.getFlexCellFormatter().setColSpan(i, 1, 4);
						grid.setWidget(i, 0, DOSPacketLabel);
						grid.setWidget(i, 1, dosPacket);
						i++;
						
						Label DOSWindowLabel = new Label("DOS Window");
						Label DOSWindow = new Label(dr.getSrcIPAddress());
						grid.getFlexCellFormatter().setColSpan(i, 1, 4);
						grid.setWidget(i, 0, DOSWindowLabel);
						grid.setWidget(i, 1, DOSWindow);
						i++;
					}
					Label actionLabel = new Label("Action Type");
					Label action = new Label(dr.getActionType());
					grid.getFlexCellFormatter().setColSpan(i, 1, 4);
					grid.setWidget(i, 0, actionLabel);
					grid.setWidget(i, 1, action);
					i++;

					grid.getFlexCellFormatter().setColSpan(i, 0, 5);
					grid.setWidget(i, 0, closeButton);
					
					dialogPanel.add(grid);
					dialogBox.setWidget(dialogPanel);
					int left = Window.getClientWidth() / 3;
					int top = Window.getClientHeight() / 5;
					dialogBox.setPopupPosition(left, top);
					dialogBox.show();

				}
				
			}
			
			// Called by onFailure if the session is still valid
			public void doFailureAction() {
				final DialogBox dialogBox = new DialogBox();
				dialogBox.setText("Error");
				final Button closeButton = new Button("Close");
				closeButton.addStyleName("sendButton");
				closeButton.addClickHandler(new ClickHandler() {
					public void onClick(ClickEvent event) {
						dialogBox.hide();
					}
				});
			}
		});
	}
	
	private void setupDetectorPanel(HorizontalPanel detectorPanel, final Label errorLabelActivateDetector, 
			final ListDataProvider<AnalyzerResultDTO> dataProvider) {
		// DoS detector panel
		Label detectorTypeLabel = new Label("Filter Type");

		final ListBox detectorType = new ListBox();
		detectorType.setName("Detector Type");
		detectorType.setTitle("Detector Type Title");
		detectorType.addItem("VALUE_OUT_OF_BOUND", "VALUE_OUT_OF_BOUND");
		detectorType.addItem("MS_EP_CONNECTIVITY", "MS_EP_CONNECTIVITY");
		detectorType.addItem("WRONG_MSG_TO_MS_EP", "WRONG_MSG_TO_MS_EP");
		//detectorType.addItem("ERR_MSG_FROM_MS_EP", "ERR_MSG_FROM_MS_EP");
		//detectorType.addItem("WRONG_MSG_FORMAT", "WRONG_MSG_FORMAT");
		detectorType.addItem("DENIAL_OF_SERVICE", "DENIAL_OF_SERVICE");
		//detectorType.addItem("NW_SEGMENTATION", "NW_SEGMENTATION");
		//detectorType.addItem("NEW_HOST", "NEW_HOST");
		detectorType.setWidth("220");
	    detectorPanel.add(HTMLFormatUtil.getPaddingLabel());
		detectorPanel.add(detectorTypeLabel);
		detectorPanel.add(detectorType);

		// Result display button
	    Button displayDetectorResultButton = new Button("Show Detector Findings");
//	    displayDetectorResultButton.addClickHandler(new ClickHandler() {
//	    	public void onClick(ClickEvent event) {
//	    		greetingService.getAnalyzerResultsByType(
//	    				DetectionRuleTypeDTO.valueOf(detectorType.getValue(detectorType.getSelectedIndex())),
//	    				new AsyncCallbackAdapter<List<AnalyzerResultDTO>>() {
//	    					// Called by onFailure if the session is still valid
//	    					public void doFailureAction() {
//	    						errorLabelActivateDetector.setText(SERVER_ERROR);
//	    					}
//
//	    					public void onSuccess(List<AnalyzerResultDTO> result) {
//	    						dataProvider.setList(result);
//	    					}
//	    				});
//	        }
//	    });
	    detectorPanel.add(HTMLFormatUtil.getPaddingLabel());
	    detectorPanel.add(displayDetectorResultButton);

		// Result display button
	    Button displayAllResultButton = new Button("Show All Findings");
//	    displayAllResultButton.addClickHandler(new ClickHandler() {
//	    	public void onClick(ClickEvent event) {
//	    		greetingService.getAnalyzerResults(new AsyncCallbackAdapter<List<AnalyzerResultDTO>>() {
//					// Called by onFailure if the session is still valid
//					public void doFailureAction() {
//						errorLabelActivateDetector.setText(SERVER_ERROR);
//					}
//
//	    			public void onSuccess(List<AnalyzerResultDTO> result) {
//	    				dataProvider.setList(result);
//	    			}
//	    		});
//	        }
//	    });
	    detectorPanel.add(HTMLFormatUtil.getPaddingLabel());
	    detectorPanel.add(displayAllResultButton);
	}
	
	public void setupAnalyzerAndReportPanel2(ScrollPanel analyzerPanel, DockLayoutPanel dPanel) {
		// Create a CellTable.
		final CellTable<AnalyzerResultDTO> table = new CellTable<AnalyzerResultDTO>();
		setupAnalyzeResultDisplayPanel(table, dataProvider);

		SimplePager.Resources pagerResources = GWT.create(SimplePager.Resources.class);
		SimplePager pager = new SimplePager(TextLocation.CENTER, pagerResources, false, 10, true);
		pager.setDisplay(table);
		dataProvider.addDataDisplay(table);

		// Set the width of each column.
		// table.setColumnWidth(nameColumn, 35.0, Unit.PCT);
		final Label errorLabelDisplay = new Label();

		VerticalPanel displayPanel = new VerticalPanel();
		displayPanel.add(pager);
		displayPanel.add(table);
		displayPanel.add(errorLabelDisplay);
		displayPanel.setHorizontalAlignment(VerticalPanel.ALIGN_RIGHT);
		analyzerPanel.add(displayPanel);

		// DoS detector panel
		// Any detector error message
		VerticalPanel vPanel = new VerticalPanel();
		final Label errorLabelActivateDetector = new Label();

		HorizontalPanel detectorPanel = new HorizontalPanel();
		detectorPanel.addStyleName("essencePanel");
		detectorPanel.setSpacing(10);
		setupDetectorPanel(detectorPanel, errorLabelActivateDetector, dataProvider);
		vPanel.add(detectorPanel);	
	    
		vPanel.add(errorLabelActivateDetector);
		dPanel.addNorth(vPanel, 10);
	}
}
