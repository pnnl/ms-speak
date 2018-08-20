/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.view;

import java.util.List;

import com.essence.multispeak.MSPServiceOperationKey;
import com.essence.ui.client.GreetingService;
import com.essence.ui.client.GreetingServiceAsync;
import com.essence.ui.client.object.EndpointConfigurationDTO;
import com.essence.ui.client.object.EndpointConfigurationKeyDTO;
import com.essence.ui.client.object.OrganizationProfileDTO;
import com.essence.ui.custom.*;
import com.google.gwt.cell.client.ButtonCell;
import com.google.gwt.cell.client.FieldUpdater;
import com.google.gwt.core.client.GWT;
import com.google.gwt.dom.client.Style;
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
import com.google.gwt.user.client.ui.HorizontalPanel;
import com.google.gwt.user.client.ui.Label;
import com.google.gwt.user.client.ui.ListBox;
import com.google.gwt.user.client.ui.ScrollPanel;
import com.google.gwt.user.client.ui.TextBox;
import com.google.gwt.user.client.ui.VerticalPanel;
import com.google.gwt.view.client.ListDataProvider;
import com.google.gwt.view.client.SingleSelectionModel;

public class EndpointConfigurationUI {

	// The message displayed to the user when the server cannot be reached or
	// returns an error.
	private static final String SERVER_ERROR = "An error occurred while "
			+ "attempting to contact the server. Please check your network "
			+ "connection and try again.";

	private final ListDataProvider<EndpointConfigurationDTO> dataProvider = new ListDataProvider<EndpointConfigurationDTO>();

	// Create a remote service proxy to talk to the server-side Greeting
	// service.
	private final GreetingServiceAsync greetingService = GWT
			.create(GreetingService.class);

	public void updateDataProvider() {
		greetingService.getEndpointConfigurations(new AsyncCallbackAdapter<List<EndpointConfigurationDTO>>() {
			// Called by onFailure if the session is still valid
			public void doFailureAction() {
				// nothing
			}

			public void onSuccess(List<EndpointConfigurationDTO> result) {
				dataProvider.setList(result);
				dataProvider.refresh();
			}
		});
	}

	public void setupEndpointConfigPanel(ScrollPanel endpointPanel, DockLayoutPanel dPanel) {
		VerticalPanel displayPanel = new VerticalPanel();
		final Label errorLabelDisplay = new Label();
		final Label errorLabelAdd = new Label();
		
		// Create a CellTable.
		final CellTable<EndpointConfigurationDTO> table = new CellTable<EndpointConfigurationDTO>();
		TextColumn<EndpointConfigurationDTO> ipColumn = new TextColumn<EndpointConfigurationDTO>() {
			@Override
			public String getValue(EndpointConfigurationDTO ec) {
				if (ec.getKey() != null ) {
					return ec.getKey().getHostIPAddress();
				}
				return "";
			}
		};
		ipColumn.setSortable(true);
		table.addColumn(ipColumn, "Host IP Address");

		TextColumn<EndpointConfigurationDTO> nameColumn = new TextColumn<EndpointConfigurationDTO>() {
			@Override
			public String getValue(EndpointConfigurationDTO ec) {
				return ec.getHostName();
			}
		};
		nameColumn.setSortable(true);
		table.addColumn(nameColumn, "Host Name / MAC");
		
		TextColumn<EndpointConfigurationDTO> versionColumn = new TextColumn<EndpointConfigurationDTO>() {
			@Override
			public String getValue(EndpointConfigurationDTO ec) {
				return ec.getVersion();
			}
		};
		table.addColumn(versionColumn, "MSP Version");

		WrappedCsvStringColumn<EndpointConfigurationDTO> wrappedEndpointColumn = new WrappedCsvStringColumn<EndpointConfigurationDTO>() {
	        // This is method in wrapped details column java file.

	        public WrapCsvString getValue(EndpointConfigurationDTO ec) {
	            return new WrapCsvString(ec.getEndpointList());
	        }
	    };    
	    table.addColumn(wrappedEndpointColumn, "Endpoint List");
		table.addColumnStyleName(3, "ep_wide_column_style");		

		ButtonCell buttonCell = new ButtonCell();
		Column<EndpointConfigurationDTO, String> buttonColumn = new Column<EndpointConfigurationDTO, String>(buttonCell) {
		  @Override
		  public String getValue(EndpointConfigurationDTO dr) {
		    // The value to display in the button.
		    return "Delete";
		  }
		};
		table.addColumn(buttonColumn, "Operation");
		buttonColumn.setFieldUpdater(new FieldUpdater<EndpointConfigurationDTO, String>() {
			  public void update(int index, EndpointConfigurationDTO dr, String value) {
	            if (dr != null) {
	                dataProvider.getList().remove(dr);
					greetingService.removeEndpointConfiguration(dr,
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

	    final SingleSelectionModel<EndpointConfigurationDTO> selectionModel = new SingleSelectionModel<EndpointConfigurationDTO>();
	    table.setSelectionModel(selectionModel);

	    /*
	    Button deleteButton = new Button("Delete Selected Entry");
	    deleteButton.addClickHandler(new ClickHandler() {

	        public void onClick(ClickEvent event) {
	        	EndpointConfigurationDTO selected = selectionModel.getSelectedObject();
	            if (selected != null) {
	                dataProvider.getList().remove(selected);
					greetingService.removeEndpointConfiguration(selected,
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
	    */
	    
		// Set the width of each column.
		// table.setColumnWidth(nameColumn, 35.0, Unit.PCT);

		greetingService.getEndpointConfigurations(new AsyncCallbackAdapter<List<EndpointConfigurationDTO>>() {
			// Called by onFailure if the session is still valid
			public void doFailureAction() {
				errorLabelDisplay.setText(SERVER_ERROR);
			}

			public void onSuccess(List<EndpointConfigurationDTO> result) {
				dataProvider.setList(result);
			}
		});

		displayPanel.add(pager);
		displayPanel.add(table);
		displayPanel.add(errorLabelDisplay);
		displayPanel.setHorizontalAlignment(VerticalPanel.ALIGN_RIGHT);
		endpointPanel.add(displayPanel);

		HorizontalPanel hPanel = new HorizontalPanel();
		HorizontalPanel chooseTypePanel = new HorizontalPanel();
		chooseTypePanel.addStyleName("essencePanel");
		chooseTypePanel.setSpacing(10);

		final Button editButton = new Button("Assign Endpoints to Selected Host");
		// We can add style names to widgets
		editButton.addStyleName("sendButton");
		editButton.addClickHandler(new ClickHandler() {
			public void onClick(ClickEvent event) {					
	        	EndpointConfigurationDTO selected = selectionModel.getSelectedObject();
	            if (selected != null) {
					showEditEndpointConfigurationDialog(editButton, selected, null);
	            }
			}
		});
		chooseTypePanel.add(editButton);
	//	chooseTypePanel.add(HTMLFormatUtil.getPaddingLabel());
	//	chooseTypePanel.add(deleteButton);

		final Button addHostButton = new Button("Add a Host");
		addHostButton.addStyleName("sendButton");
		addHostButton.addClickHandler(new ClickHandler() {
			public void onClick(ClickEvent event) {
				showAddHostDialog(addHostButton, null, null);
				//showAddHostDialog(addHostButton, dataProvider, null);
			}
		});
		chooseTypePanel.add(addHostButton);
		hPanel.add(chooseTypePanel);

		HorizontalPanel policyPanel = new HorizontalPanel();
		policyPanel.addStyleName("essencePanel");
		policyPanel.setSpacing(10);

		Label policyLabel = new Label("Choose an Organization Profile");
				
		final ListBox policies = new ListBox();
		greetingService.getAllOrganizations(new AsyncCallbackAdapter<List<OrganizationProfileDTO>>() {
			// Called by onFailure if the session is still valid
			public void doFailureAction() {
				errorLabelDisplay.addStyleName("serverResponseLabelError");
				errorLabelDisplay.setText(SERVER_ERROR);
			}

			public void onSuccess(List<OrganizationProfileDTO> result) {
				if (result != null && !result.isEmpty()) {
					policies.clear();
					int idx = 0;
					for (OrganizationProfileDTO p : result) {
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
						updateDataProvider();
					}
				});
			}
		});

		policyPanel.add(policyLabel);
		policyPanel.add(policies);
		hPanel.add(policyPanel);

		VerticalPanel vPanel = new VerticalPanel();
		
		vPanel.add(hPanel);
		vPanel.add(errorLabelAdd);
		
		dPanel.addNorth(vPanel,10);
	}

	public void showEndpointConfigurationInfoDialog(final String ipAddress){
		final DialogBox dialogBox = new DialogBox();
		dialogBox.setText("Assign Endpoints to a Host");
		dialogBox.setAnimationEnabled(true);

		final FlexTable grid = new FlexTable();

		Label hostIPLabel = new Label("Host IP Address");
		final Label hostIPAddr = new Label();
		grid.setWidget(0, 0, hostIPLabel);
		grid.setWidget(0, 1, hostIPAddr);

		Label hostNameLabel = new Label("Host Name / MAC");
		final Label hostName = new Label();
		grid.setWidget(1, 0, hostNameLabel);
		grid.setWidget(1, 1, hostName);

		Label versionLabel = new Label("MultiSpeak Version");
		final Label version = new Label();
		grid.setWidget(2, 0, versionLabel);
		grid.setWidget(2, 1, version);

		Label endpointsLabel = new Label("Endpoint Types");
		final VerticalPanel endpoints = new VerticalPanel();
		grid.setWidget(3, 0, endpointsLabel);
		grid.setWidget(3, 1, endpoints);

		final Button addButton = new Button("Change Configuration");
		// We can add style names to widgets
		addButton.addStyleName("sendButton");

		final VerticalPanel dialogPanel = new VerticalPanel();
		dialogPanel.addStyleName("essencePanel");
		dialogPanel.setSpacing(6);

		final Button cancelButton = new Button("Cancel");
		cancelButton.addStyleName("sendButton");
		cancelButton.addClickHandler(new ClickHandler() {
			public void onClick(ClickEvent event) {
				dialogBox.hide();
			}
		});

		greetingService.getEndpointConfiguration(ipAddress, new AsyncCallbackAdapter<EndpointConfigurationDTO>() {
			@Override
			public void doFailureAction() {

			}

			@Override
			public void onSuccess(final EndpointConfigurationDTO config) {
				if (config == null) {
					FlexTable noConfigGrid = new FlexTable();
					noConfigGrid.setWidget(0, 0, new Label("No configuration information available for this IP address."));
                    final Button addHostButton = new Button("Add host configuration");
                    addHostButton.addClickHandler(new ClickHandler() {
                        @Override
                        public void onClick(ClickEvent clickEvent) {
                            showAddHostDialog(addHostButton, ipAddress, dialogBox);
                        }
                    });
					noConfigGrid.setWidget(1, 0, addHostButton);
					noConfigGrid.setWidget(1, 1, cancelButton);
                    dialogPanel.add(noConfigGrid);
				}
				else {

					if (config.getKey() != null) {
						hostIPAddr.setText(config.getKey().getHostIPAddress());
					}
					hostName.setText(config.getHostName());
					version.setText(config.getVersion());

					if (config.getEndpointList() != null && config.getVersion() != null) {
						if (config.getVersion().equals(MSPServiceOperationKey.SUPPORTED_VERSION_3)) {
							for (int i = 0; i < EndpointListBoxV3.EndpointTypesListItems.length; i++) {
								if (config.getEndpointList().contains(EndpointListBoxV3.EndpointTypesListItems[i][0])) {
									endpoints.add(new Label(EndpointListBoxV3.EndpointTypesListItems[i][1]));
								}
							}
						}
					}

					addButton.addClickHandler(new ClickHandler() {
						public void onClick(ClickEvent event) {
							showEditEndpointConfigurationDialog(addButton, config, dialogBox);
						}
					});

					dialogPanel.add(grid);
				}
                dialogBox.setWidget(dialogPanel);
				int left = Window.getClientWidth() / 3;
				int top = Window.getClientHeight() / 5;
				dialogBox.setPopupPosition(left, top);
				dialogBox.show();
			}
		});

		final Label errorLabelAdd = new Label();

		grid.setWidget(4, 0, addButton);
		grid.setWidget(4, 1, cancelButton);

		grid.getFlexCellFormatter().setColSpan(5, 1, 2);
		grid.setWidget(5, 0, errorLabelAdd);
	}

	public void showEditEndpointConfigurationDialog(final Button buttonToEnable,
													final EndpointConfigurationDTO config,
													final DialogBox parentDialog) {
		// Create the dialog box
		final DialogBox dialogBox = new DialogBox();
		dialogBox.setText("Assign Endpoints to a Host");
		dialogBox.setAnimationEnabled(true);

		VerticalPanel dialogPanel = new VerticalPanel();
		dialogPanel.addStyleName("essencePanel");
		dialogPanel.setSpacing(6);

		FlexTable grid = new FlexTable();

		final Button addButton = new Button("Save");
		// We can add style names to widgets
		addButton.addStyleName("sendButton");

		final Button cancelButton = new Button("Cancel");
		cancelButton.addStyleName("sendButton");
		cancelButton.addClickHandler(new ClickHandler() {
			public void onClick(ClickEvent event) {
				dialogBox.hide();
				if (buttonToEnable != null) {
					buttonToEnable.setEnabled(true);
					buttonToEnable.setFocus(true);
				}
			}
		});

		final Label errorLabelAdd = new Label();

		Label hostIPLabel = new Label("Host IP Address");
		/*
		final TextBox hostIPAddr = new TextBox();
		hostIPAddr.setWidth("220");
		hostIPAddr.setName("Host IP Address");
		hostIPAddr.setTitle("Host IP Address Title");
		*/
		String hostIPAddress = "";
		if (config.getKey() != null) {
			hostIPAddress = config.getKey().getHostIPAddress();
		}
		Label hostIPAddr = new Label(hostIPAddress);
		grid.setWidget(0, 0, hostIPLabel);
		grid.setWidget(0, 1, hostIPAddr);

		Label hostNameLabel = new Label("Host Name / MAC");
		Label hostName = new Label(config.getHostName());
		grid.setWidget(1, 0, hostNameLabel);
		grid.setWidget(1, 1, hostName);

		final EndpointMultiChoiceListBox endpoints = new EndpointMultiChoiceListBox();
		
		Label versionLabel = new Label("MultiSpeak Version");
		final ListBox mspVersion = new ListBox(); 
		mspVersion.addItem(MSPServiceOperationKey.SUPPORTED_VERSION_3, MSPServiceOperationKey.SUPPORTED_VERSION_3);
		mspVersion.addItem(MSPServiceOperationKey.SUPPORTED_VERSION_5, MSPServiceOperationKey.SUPPORTED_VERSION_5);
		if (config.getVersion() != null && config.getVersion().equals(MSPServiceOperationKey.SUPPORTED_VERSION_3))
			mspVersion.setSelectedIndex(0);
		if (config.getVersion() != null && config.getVersion().equals(MSPServiceOperationKey.SUPPORTED_VERSION_5))
			mspVersion.setSelectedIndex(1);
		mspVersion.addChangeHandler(new ChangeHandler() {
			public void onChange(ChangeEvent arg0) {
				String version = mspVersion.getValue(mspVersion.getSelectedIndex());
				if (version != null && version.equals(MSPServiceOperationKey.SUPPORTED_VERSION_5)) {
					endpoints.setVersion(MSPServiceOperationKey.SUPPORTED_VERSION_5); // set up the list
					endpoints.setSelected(null); // clear the selected
				} else if (version != null && version.equals(MSPServiceOperationKey.SUPPORTED_VERSION_3)) {
					endpoints.setVersion(MSPServiceOperationKey.SUPPORTED_VERSION_3); // set up the list
					endpoints.setSelected(null); // clear the selected
				} 
			}
		});
		grid.setWidget(2, 0, versionLabel);
		grid.setWidget(2, 1, mspVersion);

		Label endpointsLabel = new Label("Endpoint Types");
		endpoints.setWidth("220");
		endpoints.setName("Endpoint Types");
		endpoints.setTitle("Endpoint Types Title");
		
		String version = mspVersion.getValue(mspVersion.getSelectedIndex());
		if (version != null && version.equals(MSPServiceOperationKey.SUPPORTED_VERSION_5)) {
			endpoints.setVersion(MSPServiceOperationKey.SUPPORTED_VERSION_5); // set up the list
			endpoints.setSelected(config.getEndpointList());
		} else if (version != null && version.equals(MSPServiceOperationKey.SUPPORTED_VERSION_3)) {
			endpoints.setVersion(MSPServiceOperationKey.SUPPORTED_VERSION_3); // set up the list
			endpoints.setSelected(config.getEndpointList()); 
		} 
		
		grid.setWidget(3, 0, endpointsLabel);
		grid.setWidget(3, 1, endpoints);

		grid.setWidget(4, 0, addButton);
		grid.setWidget(4, 1, cancelButton);

		grid.getFlexCellFormatter().setColSpan(5, 1, 2);
		grid.setWidget(5, 0, errorLabelAdd);

		// Create a handler for the addButton
		class AddButtonHandler implements ClickHandler {

			// Fired when the user clicks on the sendButton.
			public void onClick(ClickEvent event) {
				saveEndpointConfiguration();
			}

			/**
			 * Send the rule data to the server to be added to the database and
			 * wait for a response.
			 */
			private void saveEndpointConfiguration() {
				errorLabelAdd.setText("");
				// TODO-First, we validate the input.

				EndpointConfigurationDTO ec = new EndpointConfigurationDTO();
				EndpointConfigurationKeyDTO key = new EndpointConfigurationKeyDTO();
				ec.setKey(key);
				if (config.getKey() != null) {
					ec.getKey().setHostIPAddress(config.getKey().getHostIPAddress());
				}
				ec.setHostName(config.getHostName());
				ec.setEndpointList(endpoints.getSelectedItems()); // filter out "N/A"
				if (endpoints.getSelectedItems() != null && !endpoints.getSelectedItems().isEmpty())
					ec.setVersion(mspVersion.getValue(mspVersion.getSelectedIndex()));

				// Then, we send the input to the server.
				greetingService.saveEndpointConfiguration(ec, 
						new AsyncCallbackAdapter<String>() {
	    					// Called by onFailure if the session is still valid
	    					public void doFailureAction() {
								dialogBox.setText("Remote Procedure Call - Failure");
								errorLabelAdd.addStyleName("serverResponseLabelError");
								errorLabelAdd.setText(SERVER_ERROR);
								dialogBox.center();
								if (buttonToEnable != null) {
									buttonToEnable.setFocus(true);
								}
								dialogBox.hide();
	    					}

							public void onSuccess(String result) {
								if (parentDialog != null) {
									parentDialog.hide();
									showEndpointConfigurationInfoDialog(config.getKey().getHostIPAddress());
								}
								greetingService
										.getEndpointConfigurations(new AsyncCallbackAdapter<List<EndpointConfigurationDTO>>() {
					    					// Called by onFailure if the session is still valid
					    					public void doFailureAction() {
					    						errorLabelAdd.setText(SERVER_ERROR);
					    					}

											public void onSuccess(
													List<EndpointConfigurationDTO> result) {
												dataProvider.setList(result);
												dataProvider.refresh();
											}

										});
								if (buttonToEnable != null) {
									buttonToEnable.setEnabled(true);
								}
								dialogBox.setText("Remote Procedure Call");
								dialogBox.center();
								if (buttonToEnable != null) {
									buttonToEnable.setFocus(true);
								}
								dialogBox.hide();
							}

						});

			}
		}

		// Add a handler to send the name to the server
		AddButtonHandler handler = new AddButtonHandler();
		addButton.addClickHandler(handler);
		if (buttonToEnable != null) {
			buttonToEnable.setEnabled(false);
		}
		dialogPanel.add(grid);
		dialogBox.setWidget(dialogPanel);
		int left = Window.getClientWidth() / 3;
		int top = Window.getClientHeight() / 5;
		dialogBox.setPopupPosition(left, top);
		dialogBox.show();
	}	

	public void showAddHostDialog(final Button buttonToEnable,
								   //final ListDataProvider<EndpointConfigurationDTO> dataProvider,
								  final String ipAdress,
								  final DialogBox parentDialog) {
		// Create the dialog box
		final DialogBox dialogBox = new DialogBox();
		dialogBox.setText("Add a New Host");
		dialogBox.setAnimationEnabled(true);

		VerticalPanel dialogPanel = new VerticalPanel();
		dialogPanel.addStyleName("essencePanel");
		dialogPanel.setSpacing(6);

		FlexTable grid = new FlexTable();

		final Button addButton = new Button("Add");
		// We can add style names to widgets
		addButton.addStyleName("sendButton");

		final Button cancelButton = new Button("Cancel");
		cancelButton.addStyleName("sendButton");
		cancelButton.addClickHandler(new ClickHandler() {
			public void onClick(ClickEvent event) {
				dialogBox.hide();
				if (buttonToEnable != null) {
					buttonToEnable.setEnabled(true);
					buttonToEnable.setFocus(true);
				}
			}
		});

		final Label errorLabelAdd = new Label();

		Label hostIPLabel = new Label("Host IP Address");
		final TextBox hostIPAddr = new TextBox();
		hostIPAddr.setWidth("220");
		hostIPAddr.setName("Host IP Address");
		hostIPAddr.setTitle("Host IP Address Title");
		hostIPAddr.setText(ipAdress);
		
		grid.setWidget(0, 0, hostIPLabel);
		grid.setWidget(0, 1, hostIPAddr);

		Label hostNameLabel = new Label("Host Name / MAC");
		final TextBox hostNameMAC = new TextBox();
		hostNameMAC.setWidth("220");
		hostNameMAC.setName("Host Name / MAC");
		hostNameMAC.setTitle("Host Name / MAC Title");
		grid.setWidget(1, 0, hostNameLabel);
		grid.setWidget(1, 1, hostNameMAC);

		grid.setWidget(2, 0, addButton);
		grid.setWidget(2, 1, cancelButton);

		grid.getFlexCellFormatter().setColSpan(3, 1, 2);
		grid.setWidget(3, 0, errorLabelAdd);

		// Create a handler for the addButton
		class AddButtonHandler implements ClickHandler {

			// Fired when the user clicks on the sendButton.
			public void onClick(ClickEvent event) {
				saveEndpointConfiguration();
			}

			/**
			 * Send the rule data to the server to be added to the database and
			 * wait for a response.
			 */
			private void saveEndpointConfiguration() {
				errorLabelAdd.setText("");
				// TODO-First, we validate the input.

				EndpointConfigurationDTO ec = new EndpointConfigurationDTO();
				EndpointConfigurationKeyDTO key = new EndpointConfigurationKeyDTO();
				ec.setKey(key);
				ec.getKey().setHostIPAddress(hostIPAddr.getText());
				ec.setHostName(hostNameMAC.getText());

				// Then, we send the input to the server.
				greetingService.saveEndpointConfiguration(ec, 
						new AsyncCallbackAdapter<String>() {
	    					// Called by onFailure if the session is still valid
	    					public void doFailureAction() {
								dialogBox.setText("Remote Procedure Call - Failure");
								errorLabelAdd.addStyleName("serverResponseLabelError");
								errorLabelAdd.setText(SERVER_ERROR);
								dialogBox.center();
								if (buttonToEnable != null) {
									buttonToEnable.setFocus(true);
								}
								dialogBox.hide();
	    					}

							public void onSuccess(String result) {
								if (parentDialog != null) {
									parentDialog.hide();
									showEndpointConfigurationInfoDialog(ipAdress);
								}
								greetingService
										.getEndpointConfigurations(new AsyncCallbackAdapter<List<EndpointConfigurationDTO>>() {
					    					// Called by onFailure if the session is still valid
					    					public void doFailureAction() {
					    						errorLabelAdd.setText(SERVER_ERROR);
					    					}

											public void onSuccess(
													List<EndpointConfigurationDTO> result) {
												dataProvider.setList(result);
												dataProvider.refresh();
											}

										});
								if (buttonToEnable != null) {
									buttonToEnable.setEnabled(true);
								}
								dialogBox.setText("Remote Procedure Call");
								dialogBox.center();
								if (buttonToEnable != null) {
									buttonToEnable.setFocus(true);
								}
								dialogBox.hide();
							}

						});

			}
		}

		// Add a handler to send the name to the server
		AddButtonHandler handler = new AddButtonHandler();
		addButton.addClickHandler(handler);
		if (buttonToEnable != null) {
			buttonToEnable.setEnabled(false);
		}
		dialogPanel.add(grid);
		dialogBox.setWidget(dialogPanel);
		int left = Window.getClientWidth() / 3;
		int top = Window.getClientHeight() / 5;
		dialogBox.setPopupPosition(left, top);
		dialogBox.show();
	}	
}
