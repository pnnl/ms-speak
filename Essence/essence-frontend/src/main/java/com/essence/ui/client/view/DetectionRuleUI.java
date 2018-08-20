/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.view;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import com.essence.multispeak.MSPServiceOperationKey;
import com.essence.ui.client.GreetingService;
import com.essence.ui.client.GreetingServiceAsync;
import com.essence.ui.client.object.DetectionRuleDTO;
import com.essence.ui.client.object.DetectionRuleTypeDTO;
import com.essence.ui.client.object.MultiSpeakEndPointConnectivityRule;
import com.essence.ui.client.object.VOOBKeyDTO;
import com.essence.ui.client.object.ValueOperatorTypeDTO;
import com.essence.ui.client.object.ValueOutOfBoundDetailDTO;
import com.essence.ui.client.object.XpathDTO;
import com.essence.ui.custom.EndpointListBoxV3;
import com.essence.ui.custom.EndpointListBoxV5;
import com.essence.ui.custom.VOOBDetailClickableCellText;
import com.essence.ui.shared.StringUtil;
import com.essence.ui.custom.AsyncCallbackAdapter;
import com.google.gwt.cell.client.ButtonCell;
import com.google.gwt.cell.client.FieldUpdater;
import com.google.gwt.core.client.GWT;
import com.google.gwt.event.dom.client.ChangeEvent;
import com.google.gwt.event.dom.client.ChangeHandler;
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
import com.google.gwt.user.client.ui.HTMLTable.RowFormatter;
import com.google.gwt.user.client.ui.HorizontalPanel;
import com.google.gwt.user.client.ui.Label;
import com.google.gwt.user.client.ui.ListBox;
import com.google.gwt.user.client.ui.ScrollPanel;
import com.google.gwt.user.client.ui.TextBox;
import com.google.gwt.user.client.ui.VerticalPanel;
import com.google.gwt.view.client.ListDataProvider;

public class DetectionRuleUI {

	// The message displayed to the user when the server cannot be reached or
	// returns an error.
	private static final String SERVER_ERROR = "An error occurred while "
			+ "attempting to contact the server. Please check your network "
			+ "connection and try again.";

	// Create a remote service proxy to talk to the server-side Greeting
	// service.
	private final GreetingServiceAsync greetingService = GWT.create(GreetingService.class);

	final ListDataProvider<DetectionRuleDTO> dataProvider = new ListDataProvider<DetectionRuleDTO>();

	public void refreshRuleDisplay() {	
		greetingService.getDetectionRules(new AsyncCallbackAdapter<List<DetectionRuleDTO>>() {
			// Called by onFailure if the session is still valid
			public void doFailureAction() {
			}

			public void onSuccess(final List<DetectionRuleDTO> result) {
				if (result == null || result.isEmpty()) {
					dataProvider.setList(result);
					dataProvider.refresh();
					return;
				}
					
				List<Integer> ruleIds = new ArrayList<Integer>();
				for (int i=0; i<result.size(); i++)
					if (result.get(i).getRuleType().equals(DetectionRuleTypeDTO.VALUE_OUT_OF_BOUND.toString()))
						ruleIds.add(result.get(i).getId());
				greetingService.getValueOutOfBoundRuleDetails(ruleIds, new AsyncCallbackAdapter<Map<Integer, List<ValueOutOfBoundDetailDTO>>>() {
					// Called by onFailure if the session is still valid
					public void doFailureAction() {
					}

					public void onSuccess(Map<Integer, List<ValueOutOfBoundDetailDTO>> result2) {
						for (int i=0; i<result.size(); i++)
							if (result.get(i).getRuleType().equals(DetectionRuleTypeDTO.VALUE_OUT_OF_BOUND.toString())) {
								result.get(i).setVoobDetails(result2.get(result.get(i).getId()));
							}
						
						dataProvider.setList(result);
						dataProvider.refresh();
					}
				});
			}
		});
	}
	
	public void setupDetectionRulePanel2(ScrollPanel detectionPanel, DockLayoutPanel dPanel){
		VerticalPanel displayPanel = new VerticalPanel();
		final Label errorLabelDisplay = new Label();
		final Label errorLabelAdd = new Label();

		// Create a CellTable.
		final CellTable<DetectionRuleDTO> table = new CellTable<DetectionRuleDTO>();
		TextColumn<DetectionRuleDTO> idColumn = new TextColumn<DetectionRuleDTO>() {
			@Override
			public String getValue(DetectionRuleDTO rule) {
				return rule.getId() + "";
			}
		};
		idColumn.setSortable(true);
		table.addColumn(idColumn, "Rule ID");

		TextColumn<DetectionRuleDTO> typeColumn = new TextColumn<DetectionRuleDTO>() {
			@Override
			public String getValue(DetectionRuleDTO rule) {
				return rule.getRuleType();
			}
		};
		typeColumn.setSortable(true);
		table.addColumn(typeColumn, "Rule Type");
		table.addColumnStyleName(1, "rule_type_column_style");
		//table.setColumnWidth(typeColumn, 65.0, Unit.PCT);

		TextColumn<DetectionRuleDTO> srcEPColumn = new TextColumn<DetectionRuleDTO>() {
			@Override
			public String getValue(DetectionRuleDTO rule) {
				if (rule.getVersion() != null && rule.getSrcEndpointType() != null)
					return rule.getSrcEndpointType() + "(" + rule.getVersion() + ")";
				return rule.getSrcEndpointType();
			}
		};
		srcEPColumn.setSortable(true);
		table.addColumn(srcEPColumn, "Source EP Type");
		table.addColumnStyleName(2, "rule_narrow_column_style");
		
		TextColumn<DetectionRuleDTO> dstEPColumn = new TextColumn<DetectionRuleDTO>() {
			@Override
			public String getValue(DetectionRuleDTO rule) {
				if (rule.getVersion() != null && rule.getDstEndpointType() != null)
					return rule.getDstEndpointType() + "(" + rule.getVersion() + ")";
				return rule.getDstEndpointType();
			}
		};
		dstEPColumn.setSortable(true);
		table.addColumn(dstEPColumn, "Destination EP Type");
		table.addColumnStyleName(3, "rule_narrow_column_style");

		TextColumn<DetectionRuleDTO> srcIPColumn = new TextColumn<DetectionRuleDTO>() {
			@Override
			public String getValue(DetectionRuleDTO rule) {
				return rule.getSrcIPAddress();
			}
		};
		srcIPColumn.setSortable(true);
		table.addColumn(srcIPColumn, "Source IP");
		table.addColumnStyleName(4, "rule_narrow_column_style");
		
		TextColumn<DetectionRuleDTO> dstIPColumn = new TextColumn<DetectionRuleDTO>() {
			@Override
			public String getValue(DetectionRuleDTO rule) {
				return rule.getDstIPAddress();
			}
		};
		dstIPColumn.setSortable(true);
		table.addColumn(dstIPColumn, "Destination IP");

		TextColumn<DetectionRuleDTO> dosColumn = new TextColumn<DetectionRuleDTO>() {
			@Override
			public String getValue(DetectionRuleDTO rule) {
				if (rule.getNumberOfPacketsForDoS() != null)
					return rule.getNumberOfPacketsForDoS()+" / " + rule.getTimeWindowInSeconds();
				else 
					return "";
			}
		};
		dosColumn.setSortable(true);
		table.addColumn(dosColumn, "DOS Packets / Window (Seconds)");
		
		final VOOBDetailClickableCellText clickableCell = new VOOBDetailClickableCellText();
		Column<DetectionRuleDTO,String> vobColumn = new Column<DetectionRuleDTO,String>(clickableCell) {
			
			@Override
			public String getValue (DetectionRuleDTO dr) {
				if (dr.getRuleType().equals(DetectionRuleTypeDTO.VALUE_OUT_OF_BOUND.toString())) {
					int idx = dr.getNonHeaderIndexOfVooBDetails();
					if (StringUtil.stringHasValue(dr.getVoobTitle())) {
						List<ValueOutOfBoundDetailDTO> details = dr.getVoobDetails();
						if (details != null && !details.isEmpty()) {
							return details.get(idx).getEndpointCode()  + "(" + details.get(idx).getVersion() + ")" + ":" + details.get(idx).getMessageName() + " - " + dr.getVoobTitle();
						} else
							return dr.getVoobTitle();
					}
					
					List<ValueOutOfBoundDetailDTO> details = dr.getVoobDetails();
					if (details == null || details.isEmpty())
						return "";
					
					StringBuffer sb = new StringBuffer();
					boolean isFirst = true;
					for (ValueOutOfBoundDetailDTO d : details) {
						if (isFirst)
							isFirst = false;
						else
							sb.append(" | ");
						sb.append(d.getDisplayDetails());
					}
					return sb.toString();
				} else
					return "";
			}
		};
		table.addColumn(vobColumn, "Value Out Of Bound");
		table.addColumnStyleName(7, "rule_wide_column_style");
		
		vobColumn.setFieldUpdater(new FieldUpdater<DetectionRuleDTO, String>() {
			public void update (int index, DetectionRuleDTO dr, String value) {
				if (dr != null && dr.getRuleType().equals(DetectionRuleTypeDTO.VALUE_OUT_OF_BOUND.toString())) {
					showVOOBRuleDialog(dr);
				}
			}
		});

		TextColumn<DetectionRuleDTO> actionColumn = new TextColumn<DetectionRuleDTO>() {
			@Override
			public String getValue(DetectionRuleDTO rule) {
				return rule.getActionType();
			}
		};
		actionColumn.setSortable(true);
		table.addColumn(actionColumn, "Action Type");
		
		ButtonCell buttonCell = new ButtonCell();
		Column<DetectionRuleDTO, String> buttonColumn = new Column<DetectionRuleDTO,String>(buttonCell){
			@Override
			public String getValue(DetectionRuleDTO dr) {
				return "Delete";
			}
		};
		table.addColumn(buttonColumn, "Operation");
		buttonColumn.setFieldUpdater(new FieldUpdater <DetectionRuleDTO, String>() {
			public void update(int index, DetectionRuleDTO dr, String value) {
				if (dr != null) {
					dataProvider.getList().remove(dr);
					greetingService.removeGeneralDetectionRule(dr,
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

		SimplePager.Resources pagerResources = GWT
				.create(SimplePager.Resources.class);
		SimplePager pager = new SimplePager(TextLocation.CENTER,
				pagerResources, false, 10, true);
		pager.setDisplay(table);
		
		dataProvider.addDataDisplay(table);

		refreshRuleDisplay();

		displayPanel.add(pager);
		displayPanel.add(table);
		displayPanel.add(errorLabelDisplay);
		displayPanel.setHorizontalAlignment(VerticalPanel.ALIGN_RIGHT);
		
		//HorizontalPanel hPanel = new HorizontalPanel();

		HorizontalPanel chooseTypePanel = new HorizontalPanel();
		chooseTypePanel.addStyleName("essencePanel");
		chooseTypePanel.setSpacing(10);

		Label ruleTypeLabel = new Label("Rule Type");
		final ListBox ruleType = new ListBox();
		ruleType.setName("Rule Type");
		ruleType.setTitle("Rule Type Title");
		ruleType.addItem("VALUE_OUT_OF_BOUND", "VALUE_OUT_OF_BOUND");
		ruleType.addItem("MS_EP_CONNECTIVITY", "MS_EP_CONNECTIVITY");
//		ruleType.addItem("WRONG_MSG_TO_MS_EP", "WRONG_MSG_TO_MS_EP");
//		ruleType.addItem("ERR_MSG_FROM_MS_EP", "ERR_MSG_FROM_MS_EP");
//		ruleType.addItem("WRONG_MSG_FORMAT", "WRONG_MSG_FORMAT");
		ruleType.addItem("DENIAL_OF_SERVICE", "DENIAL_OF_SERVICE");
//		ruleType.addItem("NW_SEGMENTATION", "NW_SEGMENTATION");
//		ruleType.addItem("NEW_HOST", "NEW_HOST");
		ruleType.setWidth("220");
		chooseTypePanel.add(ruleTypeLabel);
		chooseTypePanel.add(ruleType);

		/** new look **/
		final Button createButton = new Button("Create New Detection Rule");
		// We can add style names to widgets
		createButton.addStyleName("sendButton");
		createButton.addClickHandler(new ClickHandler() {
			public void onClick(ClickEvent event) {
				String type = ruleType.getValue(ruleType.getSelectedIndex());
				if (type != null && "MS_EP_CONNECTIVITY".equals(type))
					showCreateConnectivityRuleDialog(createButton, dataProvider);
				else if (type != null && "DENIAL_OF_SERVICE".equals(type)) {
					showCreateDoSRuleDialog(createButton, dataProvider);	
				} else if (type != null && "VALUE_OUT_OF_BOUND".equals(type)) {
						showCreateVOOBRuleDialog(createButton, dataProvider);					
				} else
					showCreateGeneralRuleDialog(type, createButton, dataProvider);
			}
		});
		chooseTypePanel.add(createButton);
		
		/*
	    final SingleSelectionModel<DetectionRuleDTO> selectionModel = new SingleSelectionModel<DetectionRuleDTO>();
	    table.setSelectionModel(selectionModel);
	    */
/*
	    Button deleteButton = new Button("Delete Selected Entry");
	    deleteButton.addClickHandler(new ClickHandler() {

	    	public void onClick(ClickEvent event) {
	    		DetectionRuleDTO selected = selectionModel.getSelectedObject();
	    		if (selected != null) {
	    			dataProvider.getList().remove(selected);
					greetingService.removeGeneralDetectionRule(selected,
							new AsyncCallbackAdapter<String>() {
								public void onFailure(Throwable caught) {
									errorLabelDisplay.setText(SERVER_ERROR);
								}

								public void onSuccess(String result) {
									//no-op
								}

							});
	    		}
	        }
	    });
		chooseTypePanel.add(HTMLFormatUtil.getPaddingLabel());
	    chooseTypePanel.add(deleteButton);
	    */
		
		//hPanel.add(chooseTypePanel);

		/*
		HorizontalPanel policyPanel = new HorizontalPanel();
		policyPanel.addStyleName("essencePanel");
		policyPanel.setSpacing(10);

		Label policyLabel = new Label("Choose a Policy to Activate");
				
		final ListBox policies = new ListBox();
		greetingService.getAllOrganizations(new AsyncCallbackAdapter<List<OrganizationProfile>>() {
			// Called by onFailure if the session is still valid
			public void doFailureAction() {
				errorLabelDisplay.addStyleName("serverResponseLabelError");
				errorLabelDisplay.setText(SERVER_ERROR);
			}

			public void onSuccess(List<OrganizationProfile> result) {
				if (result != null && !result.isEmpty()) {
					policies.clear();
					int idx = 0;
					for (OrganizationProfile p : result) {
						policies.insertItem(p.getDescription(), ""+p.getId(), idx);
						if (p.isEnabled()) {
							policies.setItemSelected(idx, true);
						}
						idx++;
					}
				}
			}
		});
		policies.setWidth("220");
		policies.addChangeHandler(new ChangeHandler() {
			public void onChange(ChangeEvent arg0) {
				int id = Integer.valueOf(policies.getValue(policies.getSelectedIndex()));
				greetingService.activateOrganization(id, new AsyncCallbackAdapter<String>() {
					public void doFailureAction() {
						errorLabelDisplay.addStyleName("serverResponseLabelError");
						errorLabelDisplay.setText(SERVER_ERROR);
					}

					public void onSuccess(String s) {
						greetingService.getDetectionRules(new AsyncCallbackAdapter<List<DetectionRuleDTO>>() {
	    					// Called by onFailure if the session is still valid
	    					public void doFailureAction() {
	    						errorLabelDisplay.addStyleName("serverResponseLabelError");
	    						errorLabelDisplay.setText(SERVER_ERROR);
	    					}

							public void onSuccess(final List<DetectionRuleDTO> result) {
								refreshRuleDisplay(result, dataProvider, errorLabelAdd);
							}

						});
					}

				});
			}
		});

		policyPanel.add(policyLabel);
		policyPanel.add(policies);
		hPanel.add(policyPanel);
*/
	    VerticalPanel vPanel = new VerticalPanel();
	    
		vPanel.add(chooseTypePanel);
		vPanel.add(errorLabelAdd);
		
		detectionPanel.add(displayPanel);
		
		dPanel.addNorth(vPanel, 10);
	}

	private void applyDataRowStyles(FlexTable grid) {
		RowFormatter rf = grid.getRowFormatter();

		for (int row = 0; row < grid.getRowCount(); ++row) {
			if ((row % 2) != 0) {
				rf.addStyleName(row, "FlexTable-OddRow");
			}
			else {
				rf.addStyleName(row, "FlexTable-EvenRow");
			}
		}
	}
	  
	private void showVOOBRuleDialog(final DetectionRuleDTO dr) {
		
		// Create the dialog box
		final DialogBox dialogBox = new DialogBox();
		dialogBox.setText("Value Out Of Bound Rule Details");
		dialogBox.setAnimationEnabled(true);

		VerticalPanel dialogPanel = new VerticalPanel();
		dialogPanel.addStyleName("essencePanel");
		dialogPanel.setSpacing(6);

		FlexTable grid = new FlexTable();
		grid.setStyleName("flex_table_style");

		final Button closeButton = new Button("Close");
		closeButton.addStyleName("sendButton");
		closeButton.addClickHandler(new ClickHandler() {
			public void onClick(ClickEvent event) {
				dialogBox.hide();
			}
		});

		Label idLabel = new Label("Rule ID");
		idLabel.setStyleName("xpath_instructions_style");
		Label id = new Label(dr.getId()+"");
		grid.getFlexCellFormatter().setColSpan(0, 1, 4);
		grid.setWidget(0, 0, idLabel);
		grid.setWidget(0, 1, id);

		Label ruleTypeLabel = new Label("Rule Type");
		ruleTypeLabel.setStyleName("xpath_instructions_style");
		Label ruleType = new Label(dr.getRuleType());
		grid.getFlexCellFormatter().setColSpan(1, 1, 4);
		grid.setWidget(1, 0, ruleTypeLabel);
		grid.setWidget(1, 1, ruleType);
		
		Label protocolLabel = new Label("Protocol");
		protocolLabel.setStyleName("xpath_instructions_style");
		//final TextBox protocolValue = new TextBox();
		Label protocolValueLabel = new Label("MultiSpeak " + dr.getVersion()); 
		grid.getFlexCellFormatter().setColSpan(2, 1, 4);
		grid.setWidget(2, 0, protocolLabel);
		grid.setWidget(2, 1, protocolValueLabel);

		List<ValueOutOfBoundDetailDTO> details = dr.getVoobDetails();
		int nextRowNumber = 3;
		if (details != null && !details.isEmpty()) {
			int msgIdx = dr.getNonHeaderIndexOfVooBDetails();
			
			Label epLabel = new Label("Endpoint Code");
			epLabel.setStyleName("xpath_instructions_style");
			Label endpointType = new Label();
			endpointType.setText(details.get(msgIdx).getEndpointCode());
			grid.getFlexCellFormatter().setColSpan(nextRowNumber, 1, 4);
			grid.setWidget(nextRowNumber, 0, epLabel);
			grid.setWidget(nextRowNumber, 1, endpointType);
			nextRowNumber++;
			
			grid.getFlexCellFormatter().setColSpan(nextRowNumber, 1, 4);
			Label msgNameLabel = new Label("Message Name");
			msgNameLabel.setStyleName("xpath_instructions_style");
			grid.setWidget(nextRowNumber, 0, msgNameLabel);
			grid.setWidget(nextRowNumber, 1, new Label(details.get(msgIdx).getMessageName()));
			nextRowNumber++;
			
			grid.getFlexCellFormatter().setColSpan(nextRowNumber, 1, 4);
			Label ruleTitleLabel = new Label("Rule Title");
			ruleTitleLabel.setStyleName("xpath_instructions_style");
			grid.setWidget(nextRowNumber, 0, ruleTitleLabel);
			grid.setWidget(nextRowNumber, 1, new Label(dr.getVoobTitle()));
			nextRowNumber++;
			
			int xPathCount = 1;
			for (ValueOutOfBoundDetailDTO d : details) {
				
				grid.getFlexCellFormatter().setColSpan(nextRowNumber, 3, 2);
				Label xpathLabel = new Label("Xpath-Condition-"+ xPathCount);
				xpathLabel.setStyleName("xpath_instructions_style");

				grid.setWidget(nextRowNumber, 0, xpathLabel);
				grid.setWidget(nextRowNumber, 1, new Label(d.getFieldName()));
				grid.setWidget(nextRowNumber, 2, new Label(d.getKey().getOperator()));
				grid.setWidget(nextRowNumber, 3, new Label(d.getTargetValue()));
				nextRowNumber++;
				grid.getFlexCellFormatter().setColSpan(nextRowNumber, 1, 4);
				Label xpath = new Label(d.getXpath().replace("/", " /"));
				xpath.setStyleName("xpath_label_width");
				grid.setWidget(nextRowNumber, 1, xpath);

				xPathCount++;
				nextRowNumber++;
			}		
		}
		
		grid.getFlexCellFormatter().setColSpan(nextRowNumber, 0, 5);
		grid.setWidget(nextRowNumber, 0, closeButton);
		
		applyDataRowStyles(grid);
		
		dialogPanel.add(grid);
		dialogBox.setWidget(dialogPanel);
		int left = Window.getClientWidth() / 20;
		int top = Window.getClientHeight() / 20;
		dialogBox.setPopupPosition(left, top);
		dialogBox.show();
	}	

	private void showCreateGeneralRuleDialog(final String type, final Button buttonToEnable,
			final ListDataProvider<DetectionRuleDTO> dataProvider) {
		// Create the dialog box
		final DialogBox dialogBox = new DialogBox();
		dialogBox.setText("Create General Detection Rule for Type " + type);
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
		final ListBox srcEPType = new ListBox(); 
		final ListBox dstEPType = new ListBox(); 
		
		Label mspVersionLabel = new Label("MultiSpeak Version");
		final ListBox mspVersion = new ListBox();
		mspVersion.addItem("N/A", "N/A");
		mspVersion.addItem(MSPServiceOperationKey.SUPPORTED_VERSION_5, MSPServiceOperationKey.SUPPORTED_VERSION_5);
		mspVersion.addItem(MSPServiceOperationKey.SUPPORTED_VERSION_3, MSPServiceOperationKey.SUPPORTED_VERSION_3);
		mspVersion.setWidth("220");
		mspVersion.addChangeHandler(new ChangeHandler() {
			public void onChange(ChangeEvent arg0) {
				String version = mspVersion.getValue(mspVersion.getSelectedIndex());
				if (version != null && version.equals(MSPServiceOperationKey.SUPPORTED_VERSION_5)) {
					srcEPType.clear();
					dstEPType.clear();
					EndpointListBoxV5.copyListItemsToListBox(srcEPType);
					EndpointListBoxV5.copyListItemsToListBox(dstEPType);
				} else if (version != null && version.equals(MSPServiceOperationKey.SUPPORTED_VERSION_3)) {
					srcEPType.clear();
					dstEPType.clear();
					EndpointListBoxV3.copyListItemsToListBox(srcEPType);
					EndpointListBoxV3.copyListItemsToListBox(dstEPType);
				} else {
					srcEPType.clear();
					dstEPType.clear();
				}
			}
		});

		grid.setWidget(0, 0, mspVersionLabel);
		grid.setWidget(0, 1, mspVersion);

		Label srcEPLabel = new Label("Source Endpoint Type");
		//final EndpointListBoxV5 srcEPType = new EndpointListBoxV5();
		//final TextBox srcEPType = new TextBox();
		srcEPType.setWidth("220");
		srcEPType.setName("Source Endpoint Type");
		srcEPType.setTitle("Source Endpoint Type Title");
		grid.setWidget(1, 0, srcEPLabel);
		grid.setWidget(1, 1, srcEPType);

		Label dstEPLabel = new Label("Destination Endpoint Type");
		//final EndpointListBoxV5 dstEPType = new EndpointListBoxV5();
		//final TextBox dstEPType = new TextBox();
		dstEPType.setWidth("220");
		dstEPType.setName("Destination Endpoint Type");
		dstEPType.setTitle("Source Endpoint Type Title");
		grid.setWidget(2, 0, dstEPLabel);
		grid.setWidget(2, 1, dstEPType);

		Label srcIPLabel = new Label("Source IP Address");
		final TextBox srcIPAddr = new TextBox();
		srcIPAddr.setWidth("220");
		srcIPAddr.setName("Source IP Address");
		srcIPAddr.setTitle("Source IP Address Title");
		grid.setWidget(3, 0, srcIPLabel);
		grid.setWidget(3, 1, srcIPAddr);

		Label dstIPLabel = new Label("Destination IP Address");
		final TextBox dstIPAddr = new TextBox();
		dstIPAddr.setWidth("220");
		dstIPAddr.setName("Destination IP Address");
		dstIPAddr.setTitle("Destination IP Address Title");
		grid.setWidget(4, 0, dstIPLabel);
		grid.setWidget(4, 1, dstIPAddr);

		Label dosLabel = new Label("Denial of Service (# of packets)");
		final TextBox dosNumPackets = new TextBox();
		dosNumPackets.setWidth("220");
		dosNumPackets.setName("DOS Number of Packets");
		dosNumPackets.setTitle("DOS Number of Packets Title");
		grid.setWidget(5, 0, dosLabel);
		grid.setWidget(5, 1, dosNumPackets);

		Label dosTWLabel = new Label("DOS Time Window (seconds)");
		final TextBox dosTW = new TextBox();
		dosTW.setWidth("220");
		dosTW.setName("DOS Time Window");
		dosTW.setTitle("DOS Time Window Title");
		grid.setWidget(6, 0, dosTWLabel);
		grid.setWidget(6, 1, dosTW);

		Label actionLabel = new Label("Action");
		final ListBox actionType = new ListBox();
		actionType.setName("Action Type");
		actionType.setTitle("Action Type Title");
		actionType.addItem("N/A", "N/A");
		actionType.addItem("Allowed", "Allowed");
		actionType.addItem("Disallowed", "Disallowed");
		actionType.setWidth("220");
		grid.setWidget(7, 0, actionLabel);
		grid.setWidget(7, 1, actionType);

		grid.setWidget(8, 0, addButton);
		grid.setWidget(8, 1, cancelButton);
		grid.getFlexCellFormatter().setColSpan(9, 1, 2);
		grid.setWidget(9, 0, errorLabelAdd);

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
				// TODO-First, we validate the input.

				DetectionRuleDTO rule = new DetectionRuleDTO();
				rule.setRuleType(type);
				if (actionType.getValue(actionType.getSelectedIndex()) != null && !actionType.getValue(actionType.getSelectedIndex()).equals("N/A"))
					rule.setActionType(actionType.getValue(actionType.getSelectedIndex()));
				rule.setVersion(mspVersion.getValue(mspVersion.getSelectedIndex()));
				if (dstEPType.getValue(dstEPType.getSelectedIndex()) != null && !dstEPType.getValue(dstEPType.getSelectedIndex()).equals("N/A"))
					rule.setDstEndpointType(dstEPType.getValue(dstEPType.getSelectedIndex()));
				if (srcEPType.getValue(srcEPType.getSelectedIndex()) != null && !srcEPType.getValue(srcEPType.getSelectedIndex()).equals("N/A"))
					rule.setSrcEndpointType(srcEPType.getValue(srcEPType.getSelectedIndex()));
				rule.setDstIPAddress(dstIPAddr.getText());
				rule.setNumberOfPacketsForDoS(StringUtil.textToInteger(dosNumPackets.getText()));
				rule.setSrcIPAddress(srcIPAddr.getText());
				rule.setTimeWindowInSeconds(StringUtil.textToLong(dosTW.getText()));

				// Then, we send the input to the server.
				greetingService.addGeneralDetectionRule(rule,
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
								refreshRuleDisplay();
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
	
	private void showCreateConnectivityRuleDialog(final Button buttonToEnable,
			final ListDataProvider<DetectionRuleDTO> dataProvider) {
		// Create the dialog box
		final DialogBox dialogBox = new DialogBox();
		dialogBox.setText("Create MultiSpeak Connectivity Rule");
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
		final ListBox srcEPType = new ListBox(); 
		final ListBox dstEPType = new ListBox(); 
		
		Label mspVersionLabel = new Label("MultiSpeak Version");
		final ListBox mspVersion = new ListBox();
		mspVersion.addItem("N/A", "N/A");
		mspVersion.addItem(MSPServiceOperationKey.SUPPORTED_VERSION_5, MSPServiceOperationKey.SUPPORTED_VERSION_5);
		mspVersion.addItem(MSPServiceOperationKey.SUPPORTED_VERSION_3, MSPServiceOperationKey.SUPPORTED_VERSION_3);
		mspVersion.setWidth("220");
		mspVersion.addChangeHandler(new ChangeHandler() {
			public void onChange(ChangeEvent arg0) {
				String version = mspVersion.getValue(mspVersion.getSelectedIndex());
				if (version != null && version.equals(MSPServiceOperationKey.SUPPORTED_VERSION_5)) {
					srcEPType.clear();
					dstEPType.clear();
					EndpointListBoxV5.copyListItemsToListBox(srcEPType);
					EndpointListBoxV5.copyListItemsToListBox(dstEPType);
				} else if (version != null && version.equals(MSPServiceOperationKey.SUPPORTED_VERSION_3)) {
					srcEPType.clear();
					dstEPType.clear();
					EndpointListBoxV3.copyListItemsToListBox(srcEPType);
					EndpointListBoxV3.copyListItemsToListBox(dstEPType);
				} else {
					srcEPType.clear();
					dstEPType.clear();
				}
			}
		});

		grid.setWidget(0, 0, mspVersionLabel);
		grid.setWidget(0, 1, mspVersion);

		Label srcEPLabel = new Label("Source Endpoint Type");
		srcEPType.setWidth("220");
		srcEPType.setName("Source Endpoint Type");
		srcEPType.setTitle("Source Endpoint Type Title");
		grid.setWidget(1, 0, srcEPLabel);
		grid.setWidget(1, 1, srcEPType);

		Label dstEPLabel = new Label("Destination Endpoint Type");
		dstEPType.setWidth("220");
		dstEPType.setName("Destination Endpoint Type");
		dstEPType.setTitle("Source Endpoint Type Title");
		grid.setWidget(2, 0, dstEPLabel);
		grid.setWidget(2, 1, dstEPType);

		Label actionLabel = new Label("Action");
		final ListBox actionType = new ListBox();
		actionType.setName("Action Type");
		actionType.setTitle("Action Type Title");
		actionType.addItem("Allowed", "Allowed");
		actionType.addItem("Disallowed", "Disallowed");
		actionType.setWidth("220");
		grid.setWidget(3, 0, actionLabel);
		grid.setWidget(3, 1, actionType);

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
				// TODO-First, we validate the input.

				String errorMsg = "";
				if (!StringUtil.stringHasValue(mspVersion.getValue(mspVersion.getSelectedIndex())) || mspVersion.getValue(mspVersion.getSelectedIndex()).equals("N/A"))
					errorMsg = errorMsg + "Invalid version value. ";
				if (!StringUtil.stringHasValue(srcEPType.getValue(srcEPType.getSelectedIndex())) || srcEPType.getValue(srcEPType.getSelectedIndex()).equals("N/A"))
					errorMsg = errorMsg + "Invalid source endpoint value. ";
				if (!StringUtil.stringHasValue(dstEPType.getValue(dstEPType.getSelectedIndex())) || dstEPType.getValue(dstEPType.getSelectedIndex()).equals("N/A"))
					errorMsg = errorMsg + "Invalid destination endpoint value. ";
				if (!StringUtil.stringHasValue(actionType.getValue(actionType.getSelectedIndex())))
					errorMsg = errorMsg + "Invalid action value. ";

				if (StringUtil.stringHasValue(errorMsg)) {
					errorLabelAdd.setText(errorMsg);
					return;
				}
				
				MultiSpeakEndPointConnectivityRule rule = new MultiSpeakEndPointConnectivityRule();
				rule.setActionType(actionType.getValue(actionType.getSelectedIndex()));
				rule.setDstEndpointType(dstEPType.getValue(dstEPType.getSelectedIndex()));
				rule.setSrcEndpointType(srcEPType.getValue(srcEPType.getSelectedIndex()));
				rule.setVersion(mspVersion.getValue(mspVersion.getSelectedIndex()));

				// Then, we send the input to the server.
				greetingService.addMSEndPointConnectivityRule(rule,
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
								refreshRuleDisplay();
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
	
	private void showCreateDoSRuleDialog(final Button buttonToEnable,
			final ListDataProvider<DetectionRuleDTO> dataProvider) {
		// Create the dialog box
		final DialogBox dialogBox = new DialogBox();
		dialogBox.setText("Create Denial of Service Rule");
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

		Label dosLabel = new Label("Denial of Service (# of packets)");
		final TextBox dosNumPackets = new TextBox();
		dosNumPackets.setWidth("220");
		dosNumPackets.setName("DOS Number of Packets");
		dosNumPackets.setTitle("DOS Number of Packets Title");
		grid.setWidget(0, 0, dosLabel);
		grid.setWidget(0, 1, dosNumPackets);

		Label dosTWLabel = new Label("DOS Time Window (seconds)");
		final TextBox dosTW = new TextBox();
		dosTW.setWidth("220");
		dosTW.setName("DOS Time Window");
		dosTW.setTitle("DOS Time Window Title");
		grid.setWidget(1, 0, dosTWLabel);
		grid.setWidget(1, 1, dosTW);

		grid.setWidget(2, 0, addButton);
		grid.setWidget(2, 1, cancelButton);
		grid.getFlexCellFormatter().setColSpan(3, 1, 2);
		grid.setWidget(3, 0, errorLabelAdd);

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
				// TODO-First, we validate the input.


				DetectionRuleDTO rule = new DetectionRuleDTO();
				rule.setRuleType(DetectionRuleTypeDTO.DENIAL_OF_SERVICE);
				rule.setNumberOfPacketsForDoS(StringUtil.textToInteger(dosNumPackets.getText()));
				rule.setTimeWindowInSeconds(StringUtil.textToLong(dosTW.getText()));

				// Then, we send the input to the server.
				greetingService.addGeneralDetectionRule(rule, new AsyncCallbackAdapter<String>() {
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
								refreshRuleDisplay();
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
	
	private void showCreateVOOBRuleDialog(final Button buttonToEnable,
			final ListDataProvider<DetectionRuleDTO> dataProvider) {
		// Create the dialog box
		final DialogBox dialogBox = new DialogBox();
		dialogBox.setText("Create Value Out Of Bound Rule");
		dialogBox.setAnimationEnabled(true);
		
		VerticalPanel dialogPanel = new VerticalPanel();
		dialogPanel.addStyleName("essencePanel");
		dialogPanel.setSpacing(4);
		
		FlexTable grid = new FlexTable();

		int nextRowNumber = 0;
		
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

		Label protocolLabel = new Label("Protocol");
		//final TextBox protocolValue = new TextBox();
//		Label protocolValueLabel = new Label("MultiSpeak"); // this can be changed to dropdown list of protocols in the future
		final ListBox endpointType = new ListBox();

		final ListBox msg4SelectedEndpoint = new ListBox();		
		final ListBox mspVersion = new ListBox();
		mspVersion.addItem("MultiSpeak v503", MSPServiceOperationKey.SUPPORTED_VERSION_5);
		mspVersion.addItem("MultiSpeak v3ac", MSPServiceOperationKey.SUPPORTED_VERSION_3);
		mspVersion.addChangeHandler(new ChangeHandler() {
			public void onChange(ChangeEvent arg0) {
				String version = mspVersion.getValue(mspVersion.getSelectedIndex());
				greetingService.getEndpointCodes(version, new AsyncCallbackAdapter<List<String>>() {
					// Called by onFailure if the session is still valid
					public void doFailureAction() {
						dialogBox.setText("Remote Procedure Call - Failure");
						errorLabelAdd.addStyleName("serverResponseLabelError");
						errorLabelAdd.setText(SERVER_ERROR);
						dialogBox.center();
						buttonToEnable.setFocus(true);
						dialogBox.hide();
					}

					public void onSuccess(List<String> result) {
						if (result != null) {
							endpointType.clear();
							for (String ep : result)
								endpointType.addItem(ep);
						}
					}
				});
			}
		});
		grid.getFlexCellFormatter().setColSpan(nextRowNumber, 1, 3);
		grid.setWidget(nextRowNumber, 0, protocolLabel);
		grid.setWidget(nextRowNumber, 1, mspVersion);
		nextRowNumber++;
		
		Label epLabel = new Label("Endpoint Code");
		endpointType.setName("Endpoint Type");
		endpointType.setTitle("Endpoint Type Title");
		greetingService.getEndpointCodes(mspVersion.getValue(mspVersion.getSelectedIndex()), new AsyncCallbackAdapter<List<String>>() {
			// Called by onFailure if the session is still valid
			public void doFailureAction() {
				dialogBox.setText("Remote Procedure Call - Failure");
				errorLabelAdd.addStyleName("serverResponseLabelError");
				errorLabelAdd.setText(SERVER_ERROR);
				dialogBox.center();
				buttonToEnable.setFocus(true);
				dialogBox.hide();
			}

			public void onSuccess(List<String> result) {
				if (result != null) {
					endpointType.clear();
					for (String ep : result)
						endpointType.addItem(ep);
				}
			}
		});
		endpointType.setVisibleItemCount(5);
		endpointType.addChangeHandler(new ChangeHandler() {
			public void onChange(ChangeEvent arg0) {
				String cd = endpointType.getValue(endpointType.getSelectedIndex());
				String version = mspVersion.getValue(mspVersion.getSelectedIndex());
				greetingService.getEndpointMessages(cd, version, new AsyncCallbackAdapter<List<String>>() {
					// Called by onFailure if the session is still valid
					public void doFailureAction() {
						dialogBox.setText("Remote Procedure Call - Failure");
						errorLabelAdd.addStyleName("serverResponseLabelError");
						errorLabelAdd.setText(SERVER_ERROR);
						dialogBox.center();
						buttonToEnable.setFocus(true);
						dialogBox.hide();
					}

					public void onSuccess(List<String> result) {
						msg4SelectedEndpoint.clear();
						for (String msg : result)
							msg4SelectedEndpoint.addItem(msg);
					}
				});				
			}
		});
		grid.getFlexCellFormatter().setColSpan(nextRowNumber, 1, 3);
		grid.setWidget(nextRowNumber, 0, epLabel);
		grid.setWidget(nextRowNumber, 1, endpointType);
		nextRowNumber++;

		final ListBox xpath4SelectedEndpointMsg1 = new ListBox();
		final ListBox xpath4SelectedEndpointMsg2 = new ListBox();
		final ListBox xpath4SelectedEndpointMsg3 = new ListBox();
		final ListBox xpath4SelectedEndpointMsg4 = new ListBox();
		xpath4SelectedEndpointMsg1.addStyleName("xpath_listbox_width");
		xpath4SelectedEndpointMsg2.addStyleName("xpath_listbox_width");
		xpath4SelectedEndpointMsg3.addStyleName("xpath_listbox_width");
		xpath4SelectedEndpointMsg4.addStyleName("xpath_listbox_width");
		
		final Label xpathLabel1 = new Label("Condition #1 (loading xpaths...)");
		final Label xpathLabel2 = new Label("Condition #2 (loading xpaths...)");
		final Label xpathLabel3 = new Label("Condition #3 (loading xpaths...)");
		final Label xpathLabel4 = new Label("Condition #4 (loading xpaths...)");

		Label epMsgLabel = new Label("Endpoint Messages");
		msg4SelectedEndpoint.setVisibleItemCount(5);
		msg4SelectedEndpoint.addChangeHandler(new ChangeHandler() {
			public void onChange(ChangeEvent arg0) {
				String cd = endpointType.getValue(endpointType.getSelectedIndex());
				String version = mspVersion.getValue(mspVersion.getSelectedIndex());
				final String msg = msg4SelectedEndpoint.getValue(msg4SelectedEndpoint.getSelectedIndex());
				
				greetingService.getHeaderXpaths(false, version, new AsyncCallbackAdapter<List<XpathDTO>>() {
					// Called by onFailure if the session is still valid
					public void doFailureAction() {
						dialogBox.setText("Remote Procedure Call - Failure");
						errorLabelAdd.addStyleName("serverResponseLabelError");
						errorLabelAdd.setText(SERVER_ERROR);
						dialogBox.center();
						buttonToEnable.setFocus(true);
						dialogBox.hide();
					}

					public void onSuccess(List<XpathDTO> result) {
						xpath4SelectedEndpointMsg1.clear();
						xpath4SelectedEndpointMsg2.clear();
						xpath4SelectedEndpointMsg3.clear();
						xpath4SelectedEndpointMsg4.clear();
						xpath4SelectedEndpointMsg1.addItem("Select an xpath", "");
						xpath4SelectedEndpointMsg2.addItem("Select an xpath", "");
						xpath4SelectedEndpointMsg3.addItem("Select an xpath", "");
						xpath4SelectedEndpointMsg4.addItem("Select an xpath", "");
						for (XpathDTO path : result) {
							xpath4SelectedEndpointMsg1.addItem("HEADER:" +
									StringUtil.reverseXpath(path.getXpath().substring(
											XpathDTO.HEADER_SIGNATURE_PATH.length()))
									+ ": " + path.getValueType(), path.getId() + "|" + path.getXpath());
							xpath4SelectedEndpointMsg2.addItem("HEADER:" +
									StringUtil.reverseXpath(path.getXpath().substring(
											XpathDTO.HEADER_SIGNATURE_PATH.length()))
									+ ": " + path.getValueType(), path.getId() + "|" + path.getXpath());
							//xpath4SelectedEndpointMsg2.addItem("HEADER:" + StringUtil.reverseXpath(path.getXpath().substring(Xpath.HEADER_SIGNATURE_PATH.length())), path.getId()+"|"+path.getXpath());
							//xpath4SelectedEndpointMsg3.addItem("HEADER:" + StringUtil.reverseXpath(path.getXpath().substring(Xpath.HEADER_SIGNATURE_PATH.length())), path.getId()+"|"+path.getXpath());
						}
					}
				});				

				greetingService.getXpathsByServiceCDMsgName(cd, version, msg, false, new AsyncCallbackAdapter<List<XpathDTO>>() {
					// Called by onFailure if the session is still valid
					public void doFailureAction() {
						dialogBox.setText("Remote Procedure Call - Failure");
						errorLabelAdd.addStyleName("serverResponseLabelError");
						errorLabelAdd.setText(SERVER_ERROR);
						dialogBox.center();
						buttonToEnable.setFocus(true);
						dialogBox.hide();
					}

					public void onSuccess(List<XpathDTO> result) {
						int chunkSize = result.size() / 2;
						int chunk1FirstIndex = 0;
						int chunk1LastIndex = chunkSize - 1;
						int chunk2FirstIndex = chunkSize;
						int chunk2LastIndex = result.size() - 1; // 2*chunkSize-1;

//						if (result.size() == 1) {
//							chunk1FirstIndex = 0;
//							chunk1LastIndex = 0;
//							chunk2LastIndex = -1;
//						}

						//int chunk3FirstIndex = 2*chunkSize;
						//int chunk3LastIndex = result.size()-1;

//						try {
							for (int i = chunk1FirstIndex; i <= chunk1LastIndex; i++) {
								xpath4SelectedEndpointMsg1.addItem(StringUtil.reverseXpath(
										result.get(i).getXpath().substring(
												XpathDTO.BODY_SIGNATURE_PATH.length() + msg.length() + 1)) + ": "
										+ result.get(i).getValueType(), result.get(i).getId() + "|" + result.get(i).getXpath());
								xpath4SelectedEndpointMsg2.addItem(StringUtil.reverseXpath(
										result.get(i).getXpath().substring(
												XpathDTO.BODY_SIGNATURE_PATH.length() + msg.length() + 1)) + ": "
										+ result.get(i).getValueType(), result.get(i).getId() + "|" + result.get(i).getXpath());
							}

							for (int i = chunk2FirstIndex; i <= chunk2LastIndex; i++) {
								xpath4SelectedEndpointMsg3.addItem(StringUtil.reverseXpath(result.get(i).getXpath().substring(XpathDTO.BODY_SIGNATURE_PATH.length() + msg.length() + 1)) + ": " + result.get(i).getValueType(), result.get(i).getId() + "|" + result.get(i).getXpath());
								xpath4SelectedEndpointMsg4.addItem(StringUtil.reverseXpath(result.get(i).getXpath().substring(XpathDTO.BODY_SIGNATURE_PATH.length() + msg.length() + 1)) + ": " + result.get(i).getValueType(), result.get(i).getId() + "|" + result.get(i).getXpath());
							}

							//for (int i=chunk3FirstIndex; i<=chunk3LastIndex; i++)
							//xpath4SelectedEndpointMsg3.addItem(StringUtil.reverseXpath(result.get(i).getXpath().substring(Xpath.BODY_SIGNATURE_PATH.length()+msg.length()+1))+": "+result.get(i).getValueType(), result.get(i).getId()+"|"+result.get(i).getXpath());

							xpathLabel1.setText("Condition #1 (Headers, " + result.get(chunk1FirstIndex).getFieldName().substring(0, 2) + "-" + result.get(chunk1LastIndex).getFieldName().substring(0, 2) + ")");
							xpathLabel2.setText("Condition #2 (Headers, " + result.get(chunk1FirstIndex).getFieldName().substring(0, 2) + "-" + result.get(chunk1LastIndex).getFieldName().substring(0, 2) + ")");
							xpathLabel3.setText("Condition #3 (" + result.get(chunk2FirstIndex).getFieldName().substring(0, 2) + "-" + result.get(chunk2LastIndex).getFieldName().substring(0, 2) + ")");
							xpathLabel4.setText("Condition #4 (" + result.get(chunk2FirstIndex).getFieldName().substring(0, 2) + "-" + result.get(chunk2LastIndex).getFieldName().substring(0, 2) + ")");
							//xpathLabel3.setText("Condition #3 (" + result.get(chunk3FirstIndex).getFieldName().substring(0, 2) + "-" + result.get(chunk3LastIndex).getFieldName().substring(0, 2) + ")");
//						} catch (Exception ex) {
//							dialogBox.setText(ex.getMessage());
//						}
					}
				});				
			}
		});
		grid.getFlexCellFormatter().setColSpan(nextRowNumber, 1, 3);
		grid.setWidget(nextRowNumber, 0, epMsgLabel);
		grid.setWidget(nextRowNumber, 1, msg4SelectedEndpoint);
		nextRowNumber++;

		final ListBox xpath1Operator = new ListBox();
		xpath1Operator.addItem("  "+ValueOperatorTypeDTO.LESS_THAN.valueToText(), ValueOperatorTypeDTO.LESS_THAN.valueToText());
		xpath1Operator.addItem("  "+ValueOperatorTypeDTO.LESS_THEN_EQUAL_TO.valueToText(), ValueOperatorTypeDTO.LESS_THEN_EQUAL_TO.valueToText());
		xpath1Operator.addItem("  "+ValueOperatorTypeDTO.EQUAL_TO.valueToText(), ValueOperatorTypeDTO.EQUAL_TO.valueToText());
		xpath1Operator.addItem("  "+ValueOperatorTypeDTO.GREATER_THAN_EQUAL_TO.valueToText(), ValueOperatorTypeDTO.GREATER_THAN_EQUAL_TO.valueToText());
		xpath1Operator.addItem("  "+ValueOperatorTypeDTO.GREATER_THAN.valueToText(), ValueOperatorTypeDTO.GREATER_THAN.valueToText());
		xpath1Operator.addItem("  "+ValueOperatorTypeDTO.NOT_EQUAL_TO.valueToText(), ValueOperatorTypeDTO.NOT_EQUAL_TO.valueToText());

		final ListBox xpath2Operator = new ListBox();
		xpath2Operator.addItem("  "+ValueOperatorTypeDTO.LESS_THAN.valueToText(), ValueOperatorTypeDTO.LESS_THAN.valueToText());
		xpath2Operator.addItem("  "+ValueOperatorTypeDTO.LESS_THEN_EQUAL_TO.valueToText(), ValueOperatorTypeDTO.LESS_THEN_EQUAL_TO.valueToText());
		xpath2Operator.addItem("  "+ValueOperatorTypeDTO.EQUAL_TO.valueToText(), ValueOperatorTypeDTO.EQUAL_TO.valueToText());
		xpath2Operator.addItem("  "+ValueOperatorTypeDTO.GREATER_THAN_EQUAL_TO.valueToText(), ValueOperatorTypeDTO.GREATER_THAN_EQUAL_TO.valueToText());
		xpath2Operator.addItem("  "+ValueOperatorTypeDTO.GREATER_THAN.valueToText(), ValueOperatorTypeDTO.GREATER_THAN.valueToText());
		xpath2Operator.addItem("  "+ValueOperatorTypeDTO.NOT_EQUAL_TO.valueToText(), ValueOperatorTypeDTO.NOT_EQUAL_TO.valueToText());

		final ListBox xpath3Operator = new ListBox();
		xpath3Operator.addItem("  "+ValueOperatorTypeDTO.LESS_THAN.valueToText(), ValueOperatorTypeDTO.LESS_THAN.valueToText());
		xpath3Operator.addItem("  "+ValueOperatorTypeDTO.LESS_THEN_EQUAL_TO.valueToText(), ValueOperatorTypeDTO.LESS_THEN_EQUAL_TO.valueToText());
		xpath3Operator.addItem("  "+ValueOperatorTypeDTO.EQUAL_TO.valueToText(), ValueOperatorTypeDTO.EQUAL_TO.valueToText());
		xpath3Operator.addItem("  "+ValueOperatorTypeDTO.GREATER_THAN_EQUAL_TO.valueToText(), ValueOperatorTypeDTO.GREATER_THAN_EQUAL_TO.valueToText());
		xpath3Operator.addItem("  "+ValueOperatorTypeDTO.GREATER_THAN.valueToText(), ValueOperatorTypeDTO.GREATER_THAN.valueToText());
		xpath3Operator.addItem("  "+ValueOperatorTypeDTO.NOT_EQUAL_TO.valueToText(), ValueOperatorTypeDTO.NOT_EQUAL_TO.valueToText());
		
		final ListBox xpath4Operator = new ListBox();
		xpath4Operator.addItem("  "+ValueOperatorTypeDTO.LESS_THAN.valueToText(), ValueOperatorTypeDTO.LESS_THAN.valueToText());
		xpath4Operator.addItem("  "+ValueOperatorTypeDTO.LESS_THEN_EQUAL_TO.valueToText(), ValueOperatorTypeDTO.LESS_THEN_EQUAL_TO.valueToText());
		xpath4Operator.addItem("  "+ValueOperatorTypeDTO.EQUAL_TO.valueToText(), ValueOperatorTypeDTO.EQUAL_TO.valueToText());
		xpath4Operator.addItem("  "+ValueOperatorTypeDTO.GREATER_THAN_EQUAL_TO.valueToText(), ValueOperatorTypeDTO.GREATER_THAN_EQUAL_TO.valueToText());
		xpath4Operator.addItem("  "+ValueOperatorTypeDTO.GREATER_THAN.valueToText(), ValueOperatorTypeDTO.GREATER_THAN.valueToText());
		xpath4Operator.addItem("  "+ValueOperatorTypeDTO.NOT_EQUAL_TO.valueToText(), ValueOperatorTypeDTO.NOT_EQUAL_TO.valueToText());

		final TextBox xpath1Value = new TextBox();
		final TextBox xpath2Value = new TextBox();
		final TextBox xpath3Value = new TextBox();
		final TextBox xpath4Value = new TextBox();
		xpath1Value.setWidth("100px");
		xpath2Value.setWidth("100px");
		xpath3Value.setWidth("100px");
		xpath4Value.setWidth("100px");

		grid.getFlexCellFormatter().setColSpan(nextRowNumber, 1, 3);
		Label voobTitleLabel = new Label("Rule Title*");
		final TextBox voobTitle = new TextBox();
		voobTitle.setWidth("400px");
		grid.setWidget(nextRowNumber, 0, voobTitleLabel);
		grid.setWidget(nextRowNumber, 1, voobTitle);
		nextRowNumber++;

		grid.getFlexCellFormatter().setColSpan(nextRowNumber, 1, 3);
		Label instructionLabel = new Label("Xpath conditions below are AND'ed together to define value out of bound.");
		instructionLabel.setStyleName("xpath_instructions_style");
		grid.setWidget(nextRowNumber, 1, instructionLabel);
		nextRowNumber++;

		//		grid.setWidget(nextRowNumber, 0, xpathLabel1);
		grid.setWidget(nextRowNumber, 1, new Label("Xpath"));
		grid.setWidget(nextRowNumber, 2, new Label("Operator"));
		grid.setWidget(nextRowNumber, 3, new Label("Value"));
		nextRowNumber++;

		grid.setWidget(nextRowNumber, 0, xpathLabel1);
		grid.setWidget(nextRowNumber, 1, xpath4SelectedEndpointMsg1);
		grid.setWidget(nextRowNumber, 2, xpath1Operator);
		grid.setWidget(nextRowNumber, 3, xpath1Value);
		nextRowNumber++;

		grid.setWidget(nextRowNumber, 0, xpathLabel2);
		grid.setWidget(nextRowNumber, 1, xpath4SelectedEndpointMsg2);
		grid.setWidget(nextRowNumber, 2, xpath2Operator);
		grid.setWidget(nextRowNumber, 3, xpath2Value);
		nextRowNumber++;
		
		grid.setWidget(nextRowNumber, 0, xpathLabel3);
		grid.setWidget(nextRowNumber, 1, xpath4SelectedEndpointMsg3);
		grid.setWidget(nextRowNumber, 2, xpath3Operator);
		grid.setWidget(nextRowNumber, 3, xpath3Value);
		nextRowNumber++;
		
		grid.setWidget(nextRowNumber, 0, xpathLabel4);
		grid.setWidget(nextRowNumber, 1, xpath4SelectedEndpointMsg4);
		grid.setWidget(nextRowNumber, 2, xpath4Operator);
		grid.setWidget(nextRowNumber, 3, xpath4Value);
		nextRowNumber++;

		grid.getFlexCellFormatter().setColSpan(nextRowNumber, 0, 2);
		grid.getFlexCellFormatter().setColSpan(nextRowNumber, 1, 2);
		grid.setWidget(nextRowNumber, 0, addButton);
		grid.setWidget(nextRowNumber, 1, cancelButton);
		nextRowNumber++;
		
		grid.getFlexCellFormatter().setColSpan(nextRowNumber, 0, 4);
		grid.setWidget(nextRowNumber, 0, errorLabelAdd);

		// Create a handler for the addButton
		class AddButtonHandler implements ClickHandler {

			// Fired when the user clicks on the sendButton.
			public void onClick(ClickEvent event) {
/*				
				Window.alert("cd=" + endpointType.getValue(endpointType.getSelectedIndex()) + " | msg=" 
							+ msg4SelectedEndpoint.getValue(msg4SelectedEndpoint.getSelectedIndex())
							+ " | xpath1=" + xpath4SelectedEndpointMsg1.getValue(xpath4SelectedEndpointMsg1.getSelectedIndex()) 
								+ xpath1Operator.getValue(xpath1Operator.getSelectedIndex()) + xpath1Value.getValue()
							+ " | xpath2=" + xpath4SelectedEndpointMsg2.getValue(xpath4SelectedEndpointMsg2.getSelectedIndex()) 
								+ xpath2Operator.getValue(xpath2Operator.getSelectedIndex()) + xpath2Value.getValue()
							+ " | xpath3=" + xpath4SelectedEndpointMsg3.getValue(xpath4SelectedEndpointMsg3.getSelectedIndex()) 
								+ xpath3Operator.getValue(xpath3Operator.getSelectedIndex()) + xpath3Value.getValue()
							);
							*/
				if (!StringUtil.stringHasValue(voobTitle.getValue()))
					Window.alert("Please put in a descriptive rule title and submit again");
				else
					addRule();
				/*
				buttonToEnable.setEnabled(true);
				dialogBox.setText("Remote Procedure Call");
				dialogBox.center();
				buttonToEnable.setFocus(true);
				dialogBox.hide();
				*/
			}

			/**
			 * Send the rule data to the server to be added to the database and
			 * wait for a response.
			 */
			private void addRule() {
				errorLabelAdd.setText("");
				// TODO-First, we validate the input.

				String version = mspVersion.getValue(mspVersion.getSelectedIndex());
				DetectionRuleDTO rule = new DetectionRuleDTO();
				rule.setRuleType(DetectionRuleTypeDTO.VALUE_OUT_OF_BOUND);
				rule.setVoobTitle(voobTitle.getValue());
				rule.setVersion(version);
				
				List<ValueOutOfBoundDetailDTO> details = new ArrayList<ValueOutOfBoundDetailDTO>();
				
				String cd = endpointType.getValue(endpointType.getSelectedIndex());
				String msg = msg4SelectedEndpoint.getValue(msg4SelectedEndpoint.getSelectedIndex());

				String detailXpathValue = xpath4SelectedEndpointMsg1.getValue(xpath4SelectedEndpointMsg1.getSelectedIndex());
				String detailOperator = xpath1Operator.getValue(xpath1Operator.getSelectedIndex());
				String detailValue = xpath1Value.getValue();
				if (StringUtil.stringHasValue(detailXpathValue) && StringUtil.stringHasValue(detailValue)) {
					// xPathId | xpath
					String[] xpathValueComponnets = detailXpathValue.split("\\|");
					Integer xpathId = StringUtil.textToInteger(xpathValueComponnets[0]);
					if (xpathValueComponnets.length == 2 && xpathId != null) {
						ValueOutOfBoundDetailDTO detail = new ValueOutOfBoundDetailDTO();
						
						VOOBKeyDTO key = new VOOBKeyDTO();
						key.setOperator(detailOperator);
						key.setxPathId(xpathId.intValue());
						detail.setKey(key);
						
						detail.setQualifiedFieldName(version + ":" + cd + ":" + msg + ":" + StringUtil.getElementNameFromXpath(xpathValueComponnets[1])); //StringUtil.getFieldnameFromReversedPath(xpath4SelectedEndpointMsg1.getItemText(xpath4SelectedEndpointMsg1.getSelectedIndex()))						
						detail.setTargetValue(detailValue);
						detail.setXpath(xpathValueComponnets[1]);
						details.add(detail);
					}
				}

				detailXpathValue = xpath4SelectedEndpointMsg2.getValue(xpath4SelectedEndpointMsg2.getSelectedIndex());
				detailOperator = xpath2Operator.getValue(xpath2Operator.getSelectedIndex());
				detailValue = xpath2Value.getValue();
				if (StringUtil.stringHasValue(detailXpathValue) && StringUtil.stringHasValue(detailValue)) {
					// xPathId | xpath
					String[] xpathValueComponnets = detailXpathValue.split("\\|");
					Integer xpathId = StringUtil.textToInteger(xpathValueComponnets[0]);
					if (xpathValueComponnets.length == 2 && xpathId != null) {
						ValueOutOfBoundDetailDTO detail = new ValueOutOfBoundDetailDTO();
						
						VOOBKeyDTO key = new VOOBKeyDTO();
						key.setOperator(detailOperator);
						key.setxPathId(xpathId.intValue());
						detail.setKey(key);
						
						detail.setQualifiedFieldName(version + ":" + cd + ":" + msg + ":" + StringUtil.getElementNameFromXpath(xpathValueComponnets[1])); //StringUtil.getFieldnameFromReversedPath(xpath4SelectedEndpointMsg1.getItemText(xpath4SelectedEndpointMsg1.getSelectedIndex()))						
						detail.setTargetValue(detailValue);
						detail.setXpath(xpathValueComponnets[1]);
						details.add(detail);
					}
				}

				detailXpathValue = xpath4SelectedEndpointMsg3.getValue(xpath4SelectedEndpointMsg3.getSelectedIndex());
				detailOperator = xpath3Operator.getValue(xpath3Operator.getSelectedIndex());
				detailValue = xpath3Value.getValue();
				if (StringUtil.stringHasValue(detailXpathValue) && StringUtil.stringHasValue(detailValue)) {
					// xPathId | xpath
					String[] xpathValueComponnets = detailXpathValue.split("\\|");
					Integer xpathId = StringUtil.textToInteger(xpathValueComponnets[0]);
					if (xpathValueComponnets.length == 2 && xpathId != null) {
						ValueOutOfBoundDetailDTO detail = new ValueOutOfBoundDetailDTO();
						
						VOOBKeyDTO key = new VOOBKeyDTO();
						key.setOperator(detailOperator);
						key.setxPathId(xpathId.intValue());
						detail.setKey(key);
						
						detail.setQualifiedFieldName(version + ":" + cd + ":" + msg + ":" + StringUtil.getElementNameFromXpath(xpathValueComponnets[1])); //StringUtil.getFieldnameFromReversedPath(xpath4SelectedEndpointMsg1.getItemText(xpath4SelectedEndpointMsg1.getSelectedIndex()))						
						detail.setTargetValue(detailValue);
						detail.setXpath(xpathValueComponnets[1]);
						details.add(detail);
					}
				}

				detailXpathValue = xpath4SelectedEndpointMsg4.getValue(xpath4SelectedEndpointMsg4.getSelectedIndex());
				detailOperator = xpath4Operator.getValue(xpath4Operator.getSelectedIndex());
				detailValue = xpath4Value.getValue();
				if (StringUtil.stringHasValue(detailXpathValue) && StringUtil.stringHasValue(detailValue)) {
					// xPathId | xpath
					String[] xpathValueComponnets = detailXpathValue.split("\\|");
					Integer xpathId = StringUtil.textToInteger(xpathValueComponnets[0]);
					if (xpathValueComponnets.length == 2 && xpathId != null) {
						ValueOutOfBoundDetailDTO detail = new ValueOutOfBoundDetailDTO();
						
						VOOBKeyDTO key = new VOOBKeyDTO();
						key.setOperator(detailOperator);
						key.setxPathId(xpathId.intValue());
						detail.setKey(key);
						
						detail.setQualifiedFieldName(version + ":" + cd + ":" + msg + ":" + StringUtil.getElementNameFromXpath(xpathValueComponnets[1])); //StringUtil.getFieldnameFromReversedPath(xpath4SelectedEndpointMsg1.getItemText(xpath4SelectedEndpointMsg1.getSelectedIndex()))						
						detail.setTargetValue(detailValue);
						detail.setXpath(xpathValueComponnets[1]);
						details.add(detail);
					}
				}
				
				// Then, we send the input to the server.
				greetingService.addValueOutOfBoundRule(rule, details, new AsyncCallbackAdapter<String>() {
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
								refreshRuleDisplay();
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
		int left = Window.getClientWidth() / 20;
		int top = Window.getClientHeight() / 20;
		dialogBox.setPopupPosition(left, top);
		dialogBox.show();
	}
}
