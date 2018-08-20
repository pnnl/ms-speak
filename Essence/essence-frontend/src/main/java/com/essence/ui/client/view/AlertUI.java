/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.view;

import java.util.Date;
import java.util.List;
import java.util.Objects;

import com.essence.ui.client.GreetingService;
import com.essence.ui.client.GreetingServiceAsync;
import com.essence.ui.client.object.*;
import com.essence.ui.custom.AsyncCallbackAdapter;
import com.essence.ui.custom.HTMLFormatUtil;
import com.essence.ui.custom.MyClickableCellText;
import com.google.gwt.cell.client.FieldUpdater;
import com.google.gwt.core.client.GWT;
import com.google.gwt.event.dom.client.ChangeEvent;
import com.google.gwt.event.dom.client.ChangeHandler;
import com.google.gwt.event.dom.client.ClickEvent;
import com.google.gwt.event.dom.client.ClickHandler;
import com.google.gwt.event.logical.shared.ValueChangeEvent;
import com.google.gwt.event.logical.shared.ValueChangeHandler;
import com.google.gwt.i18n.client.DateTimeFormat;
import com.google.gwt.user.cellview.client.CellTable;
import com.google.gwt.user.cellview.client.Column;
import com.google.gwt.user.cellview.client.SimplePager;
import com.google.gwt.user.cellview.client.TextColumn;
import com.google.gwt.user.cellview.client.SimplePager.TextLocation;
import com.google.gwt.user.client.Timer;
import com.google.gwt.user.client.Window;
import com.google.gwt.user.client.ui.*;
import com.google.gwt.user.client.ui.HTMLTable.RowFormatter;
import com.google.gwt.view.client.ListDataProvider;
import com.google.gwt.view.client.NoSelectionModel;
import com.google.gwt.view.client.SelectionChangeEvent;

@SuppressWarnings("unused")
public class AlertUI {
    // The message displayed to the user when the server cannot be reached or
    // returns an error.
    private static final String SERVER_ERROR = "An error occurred while "
            + "attempting to contact the server. Please check your network "
            + "connection and try again.";

    private Timer alertRetrievalTimer;
    private Panel statusPanel;
    final private Label errorLabelDisplay = new Label();
    private List<AnomalyTargetTypeDTO> targetTypes;
    private String alertFilterType = "";

    // Create a remote service proxy to talk to the server-side Greeting
    // service.
    private final GreetingServiceAsync greetingService = GWT
            .create(GreetingService.class);
    private final ListDataProvider<AlertDTO> dataProvider = new ListDataProvider<>();

    public void updateDataProvider() {
        greetingService.getAlerts(alertFilterType, new AsyncCallbackAdapter<List<AlertDTO>>() {

            // Called by onFailure if the session is still valid
            public void doFailureAction() {
                errorLabelDisplay.setText(SERVER_ERROR);
            }

            public void onSuccess(List<AlertDTO> result) {
                dataProvider.setList(result);
                dataProvider.refresh();
            }
        });
    }

    public void updateDataProviderOnTimer() {
        greetingService.getAlerts(alertFilterType, new AsyncCallbackAdapter<List<AlertDTO>>() {

            // Called by onFailure if the session is still valid
            public void doFailureAction() {
                errorLabelDisplay.setText(SERVER_ERROR);
            }

            public void onSuccess(List<AlertDTO> result) {
                // TODO: should probably modify this to only pull down new alerts rather than retrieving the entire list each time

                dataProvider.setList(result);
                dataProvider.refresh();

                if (alertRetrievalTimer != null && !alertRetrievalTimer.isRunning()) {
                    alertRetrievalTimer.schedule(10000);
                }
            }
        });
    }

    public void setupAlertPanel2(SplitLayoutPanel alertPanel) {
        // Create a CellTable.
        final CellTable<AlertDTO> table = new CellTable<>();
        setupAlertsDisplayPanel(table, dataProvider);

        SimplePager.Resources pagerResources = GWT.create(SimplePager.Resources.class);
        SimplePager pager = new SimplePager(TextLocation.CENTER, pagerResources, false, 10, true);
        pager.setPageSize(10);
        pager.setDisplay(table);
        dataProvider.addDataDisplay(table);

        greetingService.getAlerts(alertFilterType, new AsyncCallbackAdapter<List<AlertDTO>>() {
            // Called by onFailure if the session is still valid
            public void doFailureAction() {
                errorLabelDisplay.setText(SERVER_ERROR);
            }

            public void onSuccess(List<AlertDTO> result) {
                dataProvider.setList(result);

                alertRetrievalTimer = new Timer() {
                    @Override
                    public void run() {
                        updateDataProviderOnTimer();
                    }
                };

                //alertRetrievalTimer.schedule(10000);
            }
        });

        alertPanel.getElement().setId("diplayPanel");
        alertPanel.setTitle("Alerts");

        statusPanel = new ScrollPanel();
        statusPanel.getElement().setId("statusPanel");
        alertPanel.addEast(statusPanel, 350);

        HorizontalPanel buttons = new HorizontalPanel();
        buttons.addStyleName("essencePanel");
        buttons.getElement().setId("buttonsFlowPanel");
        buttons.setSpacing(10);
        setupButtons(buttons);

        VerticalPanel vertPanel = new VerticalPanel();
        vertPanel.getElement().setId("vertPanel");
        vertPanel.add(buttons);
        vertPanel.add(errorLabelDisplay);
        vertPanel.add(pager);
        vertPanel.add(table);

        ScrollPanel tableScrollPanel = new ScrollPanel();
        tableScrollPanel.getElement().setId("tableScrollPanel");
        tableScrollPanel.addStyleName("reportPanelScroll");
        tableScrollPanel.add(vertPanel);
        alertPanel.add(tableScrollPanel);
    }

    public FlowPanel getAlertDisplay(final AlertDTO alert) {
        FlowPanel panel = new FlowPanel();
        FlexTable grid = new FlexTable();
        DateTimeFormat format = DateTimeFormat.getFormat(DateTimeFormat.PredefinedFormat.DATE_TIME_MEDIUM);

//        final Button showInGraphButton = new Button();
//        showInGraphButton.setText("Show in graph");
//        showInGraphButton.addClickHandler(new ClickHandler() {
//            @Override
//            public void onClick(ClickEvent clickEvent) {
//                if (alert.getAnalyzerResult() != null) {
//                    showAlertInGraph(alert.getAnalyzerResult().getSrcIPAddress(), String.valueOf(alert.getId()));
//                }
//                else if (alert.getAnomaly() != null) {
//                    showAlertInGraph(alert.getAnomaly().getSourceValue(), String.valueOf(alert.getId()));
//                }
//            }
//        });

        //grid.setWidget(0, 0, showInGraphButton);
        panel.add(grid);
        //panel.add(showInGraphButton);

        final Anchor stateLink = new Anchor();
        final Anchor causeLink = new Anchor();

        greetingService.getDecisionByAlert(alert.getId(), new AsyncCallbackAdapter<DecisionDTO>() {
            @Override
            public void doFailureAction() {

            }

            @Override
            public void onSuccess(final DecisionDTO decisionDTO) {

                if (decisionDTO != null) {
                    if (decisionDTO.getCause() != null) {
                        causeLink.setText(decisionDTO.getCause().getCause());
                    }
                    else {
                        causeLink.setText("Assign");
                    }
                    if (decisionDTO.getAnomalyState() != null) {
                        stateLink.setText(decisionDTO.getAnomalyState().getState());
                    }
                    else {
                        stateLink.setText("Assign");
                    }
                }
                else {
                    causeLink.setText("Assign");
                    stateLink.setText("Assign");
                }

                stateLink.addClickHandler(new ClickHandler() {
                    @Override
                    public void onClick(ClickEvent clickEvent) {
                        showAnomalyStateDialogBox(alert, decisionDTO);
                    }
                });

                causeLink.addClickHandler(new ClickHandler() {
                    @Override
                    public void onClick(ClickEvent clickEvent) {
                        showCauseDialogBox(alert, decisionDTO);
                    }
                });
            }
        });

        if (alert.getAnalyzerResult() != null) {
            AnalyzerResultDTO a = alert.getAnalyzerResult();
            grid.setWidget(1, 0, new Label("Destination IP:"));
            grid.setWidget(1, 1, new Label(a.getDstIPAddress()));
            grid.setWidget(2, 0, new Label("Packet Timestamp"));
            grid.setWidget(2, 1, new Label(alert.getAnalyzerResult().getTimeStamp().toString()));
            grid.setWidget(3, 0, new Label("Detector Type:"));
            grid.setWidget(3, 1, new Label(a.getDetectorType()));
            if (a.getNumberOfPacketsForDoS() != null && a.getNumberOfPacketsForDoS() > 0) {
                grid.setWidget(4, 0, new Label("DDOS Packet Count:"));
                grid.setWidget(4, 1, new Label(a.getNumberOfPacketsForDoS().toString()));
                if (a.getRunTime() != null) {
                    grid.setWidget(5, 0, new Label("Run Time::"));
                    grid.setWidget(6, 1, new Label(a.getRunTime().toString()));
                }
            }
        }
        else if (alert.getAnomaly() != null) {
            AnomalyDTO a = alert.getAnomaly();
            grid.setWidget(1, 0, new Label("User-supplied Anomaly State: "));
            grid.setWidget(1, 1, stateLink);
            grid.setWidget(2, 0, new Label("User-supplied Anomaly Cause: "));
            grid.setWidget(2, 1, causeLink);

            grid.setWidget(3, 0, new HTML("<h3>Anomaly Predictions</h3>"));
            int nextRow = 4;
            for (AnomalyPredictionDTO d : a.getPredictions()) {
                grid.setWidget(nextRow, 0, new Label("State: "));
                grid.setWidget(nextRow++, 1, new Label(d.getState() != null ? d.getState().getState() : ""));
                grid.setWidget(nextRow, 0, new Label("Cause: "));
                grid.setWidget(nextRow++, 1, new Label(d.getCause() != null ? d.getCause().getCause() : ""));
                grid.setWidget(nextRow, 0, new Label("Confidence Score: "));
                grid.setWidget(nextRow++, 1, new Label(d.getScore()));
                //++nextRow;
            }

            grid.setWidget(nextRow++, 0, new HTML("<h3>Training Data</h3>"));
            grid.setWidget(nextRow, 0, new Label("Training Start Time:"));
            grid.setWidget(nextRow++, 1, new Label(format.format(a.getTrainingTimeWindowStart())));
            grid.setWidget(nextRow, 0, new Label("Training End Time:"));
            grid.setWidget(nextRow++, 1, new Label(format.format(a.getTrainingTimeWindowEnd())));
            AnomalyTargetTypeDTO sourceType = null;
            AnomalyTargetTypeDTO targetType = null;
            for (AnomalyTargetTypeDTO d : targetTypes) {
                if (d.getId() == a.getSourceType()) {
                    sourceType = d;
                }
                if (d.getId() == a.getTargetType()) {
                    targetType = d;
                }
            }
            if (sourceType != null) {
                grid.setWidget(nextRow, 0, new Label("Source Type: "));
                grid.setWidget(nextRow++, 1, new Label(sourceType.getName()));
            }
            if (targetType != null) {
                grid.setWidget(nextRow, 0, new Label("Target Type:"));
                grid.setWidget(nextRow++, 1, new Label(targetType.getName()));
            }
            grid.setWidget(nextRow, 0, new Label("Source Value: "));
            grid.setWidget(nextRow++, 1, new Label(a.getSourceValue()));
            Integer[] patternIndex = new Integer[]{};
            int index = 0;
            for (Integer p : a.getPatternIndex()) {
                patternIndex[index++] = p;
            }

            if (a.getNormalEntries() != null) {
                grid.setWidget(nextRow++, 0, new HTML("<h3>Normal data</h3>"));

                for (AnomalyNormalEntryDTO e : a.getNormalEntries()) {
                    grid.setWidget(nextRow, 0, new Label("Target Value:"));
                    grid.setWidget(nextRow++, 1, new Label(e.getTargetValue()));
                    grid.setWidget(nextRow, 0, new Label("Minimum Count:"));
                    grid.setWidget(nextRow++, 1, new Label(Double.toString(e.getMinCount())));
                    grid.setWidget(nextRow, 0, new Label("Maximum Count:"));
                    grid.setWidget(nextRow++, 1, new Label(Double.toString(e.getMaxCount())));
                    grid.setWidget(nextRow, 0, new Label("Mean Count:"));
                    grid.setWidget(nextRow++, 1, new Label(Double.toString(e.getMeanCount())));
                    grid.setWidget(nextRow, 0, new Label("Standard Deviation:"));
                    grid.setWidget(nextRow++, 1, new Label(Double.toString(e.getStandardDeviation())));
                }
            }

            if (a.getAnomalyEntries() != null) {
                grid.setWidget(nextRow++, 0, new HTML("<h3>Observed data</h3>"));

                for (AnomalyAnomalyEntryDTO e : a.getAnomalyEntries()) {
                    Boolean matchesPatternIndex = false;
                    for (Integer aPatternIndex : patternIndex) {
                        if (aPatternIndex == e.getSequenceNumber()) {
                            matchesPatternIndex = true;
                            break;
                        }
                    }
                    if (matchesPatternIndex) {
                        Label valueLabel = new Label("Target Value:");
                        Label valueDisplay = new Label(e.getTargetValue());
                        valueLabel.addStyleName("anomalousDataRed");
                        valueDisplay.addStyleName("anomalousDataRed");
                        grid.setWidget(nextRow, 0, valueLabel);
                        grid.setWidget(nextRow++, 1, valueDisplay);
                        Label countLabel = new Label("Count:");
                        Label countDisplay = new Label(Integer.toString(e.getCount()));
                        countLabel.addStyleName("anomalousDataRed");
                        countDisplay.addStyleName("anomalousDataRed");
                        grid.setWidget(nextRow, 0, countLabel);
                        grid.setWidget(nextRow++, 1, countDisplay);
                    }
                    else {
                        grid.setWidget(nextRow, 0, new Label("Target Value:"));
                        grid.setWidget(nextRow++, 1, new Label(e.getTargetValue()));
                        grid.setWidget(nextRow, 0, new Label("Count:"));
                        grid.setWidget(nextRow++, 1, new Label(Integer.toString(e.getCount())));
                    }
                    //++nextRow;
                }
            }
        }
        return panel;
    }

    public void showAlertDisplayDialogBox(long alertId) {
        greetingService.getAlert(alertId, new AsyncCallbackAdapter<AlertDTO>() {
            @Override
            public void doFailureAction() {
                // TODO: Show alert in dialog?
            }

            @Override
            public void onSuccess(AlertDTO alertDTO) {
                final DialogBox box = new DialogBox();
                box.setText("Alert Details");
                FlowPanel dialogPanel = new FlowPanel();

                final Button closeButton = new Button("Close");
                closeButton.addStyleName("sendButton");
                closeButton.addClickHandler(new ClickHandler() {
                    public void onClick(ClickEvent event) {
                        box.hide();
                    }
                });
                dialogPanel.add(closeButton);

                ScrollPanel scrollPanel = new ScrollPanel();
                FlowPanel alertDisplay = getAlertDisplay(alertDTO);
                scrollPanel.add(alertDisplay);
                scrollPanel.setHeight("300px");
                dialogPanel.add(scrollPanel);
                box.setWidget(dialogPanel);

                int left = (Window.getClientWidth() / 2) - 180;
                int top = (Window.getClientHeight() / 2) - 150;
                box.setPopupPosition(left, top);
                box.show();
            }
        });
    }

    private void setupButtons(HorizontalPanel buttons) {
        Label alertTypeLabel = new Label("Alert Type");

        final ListBox alertType = new ListBox();
        alertType.setName("Alert Type");
        alertType.setTitle("Alert Type");
        alertType.addItem("", "");
        alertType.addItem("VALUE_OUT_OF_BOUND", "VALUE_OUT_OF_BOUND");
        alertType.addItem("MS_EP_CONNECTIVITY", "MS_EP_CONNECTIVITY");
        alertType.addItem("WRONG_MSG_TO_MS_EP", "WRONG_MSG_TO_MS_EP");
        //alertType.addItem("ERR_MSG_FROM_MS_EP", "ERR_MSG_FROM_MS_EP");
        //alertType.addItem("WRONG_MSG_FORMAT", "WRONG_MSG_FORMAT");
        alertType.addItem("DENIAL_OF_SERVICE", "DENIAL_OF_SERVICE");
        //alertType.addItem("NW_SEGMENTATION", "NW_SEGMENTATION");
        //alertType.addItem("NEW_HOST", "NEW_HOST");
        alertType.addItem("Anomaly", "Anomaly");
        alertType.setWidth("220");
        buttons.add(HTMLFormatUtil.getPaddingLabel());
        buttons.add(alertTypeLabel);
        buttons.add(alertType);

        alertType.addChangeHandler(new ChangeHandler() {
            @Override
            public void onChange(ChangeEvent changeEvent) {
                alertFilterType = alertType.getValue(alertType.getSelectedIndex());
            }
        });

        Button refreshButton = new Button("Refresh");
        refreshButton.addClickHandler(new ClickHandler() {
            @Override
            public void onClick(ClickEvent clickEvent) {
                updateDataProvider();
            }
        });
        buttons.add(HTMLFormatUtil.getPaddingLabel());
        buttons.add(refreshButton);

        Button clearFiltersButton = new Button("Clear Filters");
        clearFiltersButton.addClickHandler(new ClickHandler() {
            @Override
            public void onClick(ClickEvent clickEvent) {
                alertType.setSelectedIndex(0);
                alertFilterType = "";
            }
        });
        buttons.add(HTMLFormatUtil.getPaddingLabel());
        buttons.add(clearFiltersButton);
    }

    private void setupAlertsDisplayPanel(CellTable<AlertDTO> table, final ListDataProvider<AlertDTO> dataProvider) {
        greetingService.getAnomalyTargetTypes(new AsyncCallbackAdapter<List<AnomalyTargetTypeDTO>>() {
            // Called by onFailure if the session is still valid
            public void doFailureAction() {
                errorLabelDisplay.setText(SERVER_ERROR);
            }

            public void onSuccess(List<AnomalyTargetTypeDTO> result) {
                targetTypes = result;
            }
        });

        TextColumn<AlertDTO> descriptionColumn = new TextColumn<AlertDTO>() {
            @Override
            public String getValue(AlertDTO a) {
                return a.getDescription();
            }
        };
        descriptionColumn.setSortable(true);
        table.addColumn(descriptionColumn, "Description");
        table.addColumnStyleName(0, "ar_wide_column_style");

        TextColumn<AlertDTO> sourceColumn = new TextColumn<AlertDTO>() {
            @Override
            public String getValue(AlertDTO a) {
                if (a.getAnalyzerResult() != null) {
                    return a.getAnalyzerResult().getSrcIPAddress();
                } else if (a.getAnomaly() != null) {
                    return a.getAnomaly().getSourceValue();
                }
                return "";
            }
        };
        sourceColumn.setSortable(true);
        table.addColumn(sourceColumn, "Source");
        table.addColumnStyleName(1, "ar_narrow_column_style");

        final MyClickableCellText clickableCell = new MyClickableCellText();
        Column<AlertDTO,String> severityColumn = new Column<AlertDTO,String>(clickableCell) {
            @Override
            public String getValue (AlertDTO dr) {
				if (dr.getSeverity() == null)
					  return "assign";
				else
					  return dr.getSeverity();
            }
        };
        table.addColumn(severityColumn, "Severity");
        table.addColumnStyleName(2, "ar_narrow_column_style");
        severityColumn.setFieldUpdater(new FieldUpdater<AlertDTO, String>() {
            public void update (int index, AlertDTO dr, String value) {
                if (dr != null) {
                    showAssignSeverityDialog(dataProvider, dr);
                }
            }
        });

        TextColumn<AlertDTO> statusColumn = new TextColumn<AlertDTO>() {
            @Override
            public String getValue(AlertDTO r) {
                return r.getStatus();
            }
        };
        table.addColumn(statusColumn, "Status");
        table.addColumnStyleName(3, "ar_narrow_column_style");

        TextColumn<AlertDTO> creationTimeColumn = new TextColumn<AlertDTO>() {
            @Override
            public String getValue(AlertDTO a) {
                DateTimeFormat format = DateTimeFormat.getFormat(DateTimeFormat.PredefinedFormat.DATE_TIME_MEDIUM);
                Date d = a.getCreationTime();
                return format.format(d);
            }
        };
        creationTimeColumn.setSortable(true);
        table.addColumn(creationTimeColumn, "Creation Time");
        table.addColumnStyleName(4, "ar_time_column_style");

        table.setWidth("100%", true);

        final NoSelectionModel<AlertDTO> selModel = new NoSelectionModel<>();
        selModel.addSelectionChangeHandler(new SelectionChangeEvent.Handler() {
            @Override
            public void onSelectionChange(SelectionChangeEvent event) {
                AlertDTO a = selModel.getLastSelectedObject();
                greetingService.getAlert(a.getId(), new AsyncCallbackAdapter<AlertDTO>() {
                    @Override
                    public void doFailureAction() {

                    }

                    @Override
                    public void onSuccess(AlertDTO alertDTO) {
                        setAlertSidebar(alertDTO);
                    }
                });
            }
        });
        table.setSelectionModel(selModel);
    }

    private void setAlertSidebar(final AlertDTO alert) {
        FlowPanel panel = getAlertDisplay(alert);
        statusPanel.clear();
        statusPanel.add(panel);
    }

    private void showCauseDialogBox(final AlertDTO alert, final DecisionDTO decision) {
        greetingService.getCauses(new AsyncCallbackAdapter<List<CauseDTO>>() {
            @Override
            public void doFailureAction() {

            }

            @Override
            public void onSuccess(List<CauseDTO> causeDTOs) {
                final DialogBox box = new DialogBox();
                box.setText("Anomaly Cause");
                VerticalPanel panel = new VerticalPanel();
                FlexTable grid = new FlexTable();

                int currentRow = 0;
                if (alert.getAnomaly().getPredictions().size() > 0) {
                    grid.setWidget(currentRow, 0, new Label("Predicted Causes (Score):"));

                    for (AnomalyPredictionDTO p : alert.getAnomaly().getPredictions()) {
                        if (p.getCause() != null) {
                            grid.setWidget(currentRow++, 1, new Label(p.getCause().getCause() + " (" + p.getScore() + ")"));
                        }
                    }

                    ++currentRow;
                }

                grid.setWidget(currentRow, 0, new Label("Cause:"));
                final ListBox lb = new ListBox();
                final TextBox otherValue = new TextBox();
                //SelectOtherItem so = new SelectOtherItem();
                //so.setOtherTitle("Other..");
                //so.setOtherValue("OtherVal");
                //so.setTitle("Anomaly State");

                //LinkedHashMap<Long, String> i = new LinkedHashMap<Long, String>();
                //for (AnomalyStateDTO d : anomalyStateDTOs) {
                //    i.put(d.getId(), d.getState());
                //}
                //so.setValueMap(i);
                //DynamicForm form = new DynamicForm();
                //form.setWidth(300);
                //form.setFields(so);

                Long currentStateId = (long) 0;
                if (decision != null && decision.getCause() != null && decision.getCause().getId() > 0) {
                    currentStateId = decision.getCause().getId();
                }

                lb.addItem("", "-1");

                int currentIndex = 1;
                for (CauseDTO d : causeDTOs) {
                    lb.addItem(d.getCause(), d.getId().toString());

                    if (Objects.equals(currentStateId, d.getId())) {
                        lb.setSelectedIndex(currentIndex);
                    }
                    ++currentIndex;
                }
                lb.setVisibleItemCount(1);
                lb.addChangeHandler(new ChangeHandler() {
                    @Override
                    public void onChange(ChangeEvent changeEvent) {
                        if (lb.getSelectedIndex() > 0) {
                            otherValue.setText("");
                        }
                    }
                });
                grid.setWidget(currentRow++, 1, lb);
                //form.draw();

                grid.setWidget(currentRow, 0, new Label("Other Cause:"));
                grid.setWidget(currentRow++, 1, otherValue);
                otherValue.addValueChangeHandler(new ValueChangeHandler<String>() {
                    @Override
                    public void onValueChange(ValueChangeEvent<String> valueChangeEvent) {
                        if (valueChangeEvent.getValue() != null && valueChangeEvent.getValue().length() > 0) {
                            // Clear selected value from list box
                            lb.setSelectedIndex(0);
                        }
                    }
                });

                final Button cancelButton = new Button("Cancel");
                cancelButton.addStyleName("sendButton");
                cancelButton.addClickHandler(new ClickHandler() {
                    public void onClick(ClickEvent event) {
                        box.hide();
                    }
                });
                grid.setWidget(currentRow, 1, cancelButton);

                final Button saveButton = new Button("Save");
                saveButton.addStyleName("sendButton");
                saveButton.addClickHandler(new ClickHandler() {
                    @Override
                    public void onClick(ClickEvent clickEvent) {
                        CauseDTO cause = new CauseDTO();
                        if (lb.getSelectedIndex() > 0) {
                            String value = lb.getValue(lb.getSelectedIndex());
                            if (value != null) {
                                cause.setId(Long.parseLong(value));
                            }
                            cause.setCause(lb.getItemText(lb.getSelectedIndex()));
                        } else if (otherValue.getText().length() > 0) {
                            cause.setCause(otherValue.getText());
                        } else {
                            Window.alert("You must select a value from the drop down or supply a new value.");
                            return;
                        }
                        greetingService.setCauseOnAlert(alert, cause, new AsyncCallbackAdapter<String>() {
                            @Override
                            public void doFailureAction() {

                            }

                            @Override
                            public void onSuccess(String s) {
                                box.hide();
                            }
                        });
                    }
                });
                grid.setWidget(currentRow, 0, saveButton);

                panel.add(grid);
                box.setWidget(panel);

                int left = (Window.getClientWidth() / 2) - 180;
                int top = (Window.getClientHeight() / 2) - 75;
                box.setPopupPosition(left, top);
                box.show();
            }
        });
    }

    private void showAnomalyStateDialogBox(final AlertDTO alert, final DecisionDTO decision) {
        greetingService.getAnomalyStates(new AsyncCallbackAdapter<List<AnomalyStateDTO>>() {
            @Override
            public void doFailureAction() {

            }

            @Override
            public void onSuccess(List<AnomalyStateDTO> anomalyStateDTOs) {
                final DialogBox box = new DialogBox();
                box.setText("Anomaly State");
                VerticalPanel panel = new VerticalPanel();
                FlexTable grid = new FlexTable();

                int currentRow = 0;
                if (alert.getAnomaly().getPredictions().size() > 0) {
                    grid.setWidget(currentRow, 0, new Label("Predicted States (Score):"));

                    for (AnomalyPredictionDTO p : alert.getAnomaly().getPredictions()) {
                        if (p.getState() != null) {
                            grid.setWidget(currentRow++, 1, new Label(p.getState().getState() + " (" + p.getScore() + ")"));
                        }
                    }

                    ++currentRow;
                }

                grid.setWidget(currentRow, 0, new Label("Anomaly State:"));
                final ListBox lb = new ListBox();

                Long currentStateId = (long) 0;
                if (decision != null && decision.getAnomalyState() != null && decision.getAnomalyState().getId() > 0) {
                    currentStateId = decision.getAnomalyState().getId();
                }

                lb.addItem("", "-1");

                int currentIndex = 1;
                for (AnomalyStateDTO d : anomalyStateDTOs) {
                    lb.addItem(d.getState(), d.getId().toString());

                    if (Objects.equals(currentStateId, d.getId())) {
                        lb.setSelectedIndex(currentIndex);
                    }
                    ++currentIndex;
                }
                lb.setVisibleItemCount(1);
                grid.setWidget(currentRow++, 1, lb);

                final Button cancelButton = new Button("Cancel");
                cancelButton.addStyleName("sendButton");
                cancelButton.addClickHandler(new ClickHandler() {
                    public void onClick(ClickEvent event) {
                        box.hide();
                    }
                });
                grid.setWidget(currentRow, 1, cancelButton);

                final Button saveButton = new Button("Save");
                saveButton.addStyleName("sendButton");
                saveButton.addClickHandler(new ClickHandler() {
                    @Override
                    public void onClick(ClickEvent clickEvent) {
                        AnomalyStateDTO state = new AnomalyStateDTO();
                        if (lb.getSelectedIndex() > 0) {
                            String value = lb.getValue(lb.getSelectedIndex());
                            if (value != null) {
                                state.setId(Long.parseLong(value));
                            }
                            state.setState(lb.getItemText(lb.getSelectedIndex()));
                        }
                        else {
                            Window.alert("You must select a value from the drop down.");
                            return;
                        }
                        greetingService.setAnomalyStateOnAlert(alert, state, new AsyncCallbackAdapter<String>() {
                            @Override
                            public void doFailureAction() {

                            }

                            @Override
                            public void onSuccess(String s) {
                                box.hide();
                            }
                        });
                    }
                });
                grid.setWidget(currentRow, 0, saveButton);

                panel.add(grid);
                box.setWidget(panel);

                int left = (Window.getClientWidth() / 2) - 195;
                int top = (Window.getClientHeight() / 2) - 75;
                box.setPopupPosition(left, top);
                box.show();
            }
        });
    }

    private void applyDataRowStyles(FlexTable grid) {
        RowFormatter rf = grid.getRowFormatter();

        for (int row = 0; row < grid.getRowCount(); ++row) {
            if ((row % 2) != 0) {
                rf.addStyleName(row, "FlexTable-OddRow");
            } else {
                rf.addStyleName(row, "FlexTable-EvenRow");
            }
        }
    }

    private void showAssignSeverityDialog(final ListDataProvider<AlertDTO> dataProvider, final AlertDTO alert) {
        boolean changeable = true;
        if (alert.getStatus() != null && (alert.getStatus().equals(AnalyzerResultStatusTypeDTO.PROCESSED.toString()) ||
                alert.getStatus().equals(AnalyzerResultStatusTypeDTO.ARCHIVED.toString())))
            changeable = false;

        // Create the dialog box
        final DialogBox dialogBox = new DialogBox();
        dialogBox.setText("Assign Severity to Alert");
        dialogBox.setAnimationEnabled(true);

        VerticalPanel dialogPanel = new VerticalPanel();
        dialogPanel.addStyleName("essencePanel");
        dialogPanel.setSpacing(6);

        FlexTable grid = new FlexTable();

        final Button saveButton = new Button("Save");
        // We can add style names to widgets
        saveButton.addStyleName("sendButton");

        final Button cancelButton = new Button("Cancel");
        if (!changeable)
            cancelButton.setText("Close");
        cancelButton.addStyleName("sendButton");
        cancelButton.addClickHandler(new ClickHandler() {
            public void onClick(ClickEvent event) {
                dialogBox.hide();
            }
        });

        final Label errorLabelAdd = new Label();

        Label idLabel = new Label("Result ID");
        Label id = new Label(alert.getId() + "");
        grid.setWidget(0, 0, idLabel);
        grid.setWidget(0, 1, id);

        int currentRow = 1;

        if (alert.getAnalyzerResult() != null) {
            Label detectionTypeLabel = new Label("Detection Rule Type");
            Label detectionType = new Label(alert.getAnalyzerResult().getDetectorType());
            grid.setWidget(currentRow, 0, detectionTypeLabel);
            grid.setWidget(currentRow++, 1, detectionType);

            Label refRuleIDLabel = new Label("Ref Rule ID");
            Label refRuleID = new Label(alert.getAnalyzerResult().getRefRuleId() + "");
            grid.setWidget(currentRow, 0, refRuleIDLabel);
            grid.setWidget(currentRow++, 1, refRuleID);

            Label detectionTimeLabel = new Label("Detection Time");
            Label detectionTime = new Label(new Date(alert.getAnalyzerResult().getRunTime()).toString());
            grid.setWidget(currentRow, 0, detectionTimeLabel);
            grid.setWidget(currentRow++, 1, detectionTime);

            Label srcIPLabel = new Label("Source IP");
            Label srcIP = new Label(alert.getAnalyzerResult().getSrcIPAddress());
            grid.setWidget(currentRow, 0, srcIPLabel);
            grid.setWidget(currentRow++, 1, srcIP);

            Label dstIPLabel = new Label("Destination IP");
            Label dstIP = new Label(alert.getAnalyzerResult().getDstIPAddress());
            grid.setWidget(currentRow, 0, dstIPLabel);
            grid.setWidget(currentRow++, 1, dstIP);

            if (alert.getAnalyzerResult().getNumberOfPacketsForDoS() != null &&
                    alert.getAnalyzerResult().getNumberOfPacketsForDoS() > 0) {
                Label dosPacketLabel = new Label("DoS Packets");
                Label dosPacket = new Label(alert.getAnalyzerResult().getNumberOfPacketsForDoS() + "");
                grid.setWidget(currentRow, 0, dosPacketLabel);
                grid.setWidget(currentRow++, 1, dosPacket);

                Label dosWindowLabel = new Label("DoS Window (seconds)");
                Label dosWindow = new Label(alert.getAnalyzerResult().getTimeWindowInSeconds() + "");
                grid.setWidget(currentRow, 0, dosWindowLabel);
                //noinspection UnusedAssignment
                grid.setWidget(currentRow++, 1, dosWindow);
            }
        }
        else if (alert.getAnomaly() != null) {
            Label srcIPLabel = new Label("Source");
            Label srcIP = new Label(alert.getAnomaly().getSourceValue());
            grid.setWidget(currentRow, 0, srcIPLabel);
            //noinspection UnusedAssignment
            grid.setWidget(currentRow++, 1, srcIP);

//            Label dstIPLabel = new Label("Target Type");
//            Label dstIP = new Label(alert.getAnomaly().getTargetType());
//            grid.setWidget(currentRow, 0, dstIPLabel);
//            grid.setWidget(currentRow++, 1, dstIP);
        }

        Label statusLabel = new Label("Status");
        Label status = new Label(alert.getStatus());
        grid.setWidget(8, 0, statusLabel);
        grid.setWidget(8, 1, status);

        Label descriptionLabel = new Label("Description");
        Label description = new Label(alert.getDescription());
        grid.setWidget(9, 0, descriptionLabel);
        grid.setWidget(9, 1, description);

        Label severityLabel = new Label("Severity");
        final ListBox severity = new ListBox();
        severity.addItem("N/A", "N/A");
        severity.addItem("HIGH", "HIGH");
        severity.addItem("MEDIUM", "MEDIUM");
        severity.addItem("LOW", "LOW");
        severity.addItem("INFORMATIONAL", "INFORMATIONAL");

		if (alert.getSeverity() != null && alert.getSeverity().equalsIgnoreCase("HIGH")) {
			severity.setSelectedIndex(1);
		} else if (alert.getSeverity() != null && alert.getSeverity().equalsIgnoreCase("MEDIUM")) {
			severity.setSelectedIndex(2);
		} else if (alert.getSeverity() != null && alert.getSeverity().equalsIgnoreCase("LOW")) {
			severity.setSelectedIndex(3);
		} else if (alert.getSeverity() != null && alert.getSeverity().equalsIgnoreCase("INFORMATIONAL")) {
			severity.setSelectedIndex(4);
		}		
		severity.setWidth("220");
		severity.setName("Severity");
		severity.setTitle("Severity Title");
		if (changeable) {
			grid.setWidget(10, 0, severityLabel);
			grid.setWidget(10, 1, severity);
		} else {
			grid.setWidget(10, 0, severityLabel);
			Label severityValue = new Label(alert.getSeverity());
			grid.setWidget(10, 1, severityValue);			
		}

        if (changeable) {
            grid.setWidget(11, 0, saveButton);
            grid.setWidget(11, 1, cancelButton);
        } else {
            grid.getFlexCellFormatter().setColSpan(11, 1, 2);
            grid.setWidget(11, 0, cancelButton);
        }

        grid.getFlexCellFormatter().setColSpan(12, 1, 2);
        grid.setWidget(12, 0, errorLabelAdd);

        // Create a handler for the addButton
        class SaveButtonHandler implements ClickHandler {
            // Fired when the user clicks on the sendButton.
            public void onClick(ClickEvent event) {
                saveSeverity();
            }

            /**
             * Send the rule data to the server to be added to the database and
             * wait for a response.
             */
            private void saveSeverity() {
                errorLabelAdd.setText("");
                // TODO-First, we validate the input.
                SeverityTypeDTO severityType = null;
                try {
                    severityType = SeverityTypeDTO.valueOf(severity.getValue(severity.getSelectedIndex()));
                } catch (Exception ex) {
                    //System.out.println(ex.getMessage());
                }

                // Then, we send the input to the server.
                greetingService.setSeverityOnAlert(alert, severityType,
                        new AsyncCallbackAdapter<String>() {
                            // Called by onFailure if the session is still valid
                            public void doFailureAction() {
                                dialogBox.setText("Remote Procedure Call - Failure");
                                errorLabelAdd.addStyleName("serverResponseLabelError");
                                errorLabelAdd.setText(SERVER_ERROR);
                                dialogBox.center();
                                //						buttonToEnable.setEnabled(true);
                                //						buttonToEnable.setFocus(true);
                                dialogBox.hide();
                            }

                            public void onSuccess(String result) {
                                updateDataProvider();
//								buttonToEnable.setEnabled(true);
                                dialogBox.setText("Remote Procedure Call");
                                dialogBox.center();
//								buttonToEnable.setFocus(true);
                                dialogBox.hide();
                            }
                        });

            }
        }

        // Add a handler to send the name to the server
        SaveButtonHandler handler = new SaveButtonHandler();
        saveButton.addClickHandler(handler);
//		buttonToEnable.setEnabled(false);
        dialogPanel.add(grid);
        dialogBox.setWidget(dialogPanel);
        int left = Window.getClientWidth() / 3;
        int top = Window.getClientHeight() / 5;
        dialogBox.setPopupPosition(left, top);
        dialogBox.show();
    }

    private native void showAlertInGraph(String ipAddress, String alertId) /*-{
        var domain = $wnd.location.protocol + "//" + $wnd.location.hostname;
        var iframe = $wnd.document.getElementById('graphFrame').contentWindow;

        var obj = { call: "showNode",
        ip: ipAddress,
        alertId: alertId};
        iframe.postMessage(obj, domain);
    }-*/;
}
