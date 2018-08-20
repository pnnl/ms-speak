/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client;

import java.util.List;
import java.util.Map;

import com.essence.ui.client.object.*;
import com.google.gwt.user.client.rpc.RemoteService;
import com.google.gwt.user.client.rpc.RemoteServiceRelativePath;

/**
 * The client side stub for the RPC service.
 */
@RemoteServiceRelativePath("greet")
public interface GreetingService extends RemoteService {
    String greetServer(String name) throws IllegalArgumentException;

    String getSetting(String settingName);
    String updateSetting(String settingName, String value);

    List<OrganizationProfileDTO> getAllOrganizations();
    String activateOrganization(int id);

    List<DetectionRuleDTO> getDetectionRules();
    DetectionRuleDTO getDetectionRuleByID(int id);
    String addMSEndPointConnectivityRule(MultiSpeakEndPointConnectivityRule r);
    String addGeneralDetectionRule(DetectionRuleDTO r);
    String removeGeneralDetectionRule(DetectionRuleDTO r);
    String addValueOutOfBoundRule(DetectionRuleDTO rule, List<ValueOutOfBoundDetailDTO> details);
    Map<Integer, List<ValueOutOfBoundDetailDTO>> getValueOutOfBoundRuleDetails(List<Integer> ruleIds);

    List<EndpointConfigurationDTO> getEndpointConfigurations();
    EndpointConfigurationDTO getEndpointConfiguration(String ipAddress);
    String addEndpointConfiguration(EndpointConfigurationDTO ec);
    String removeEndpointConfiguration(EndpointConfigurationDTO ec);
    String saveEndpointConfiguration(EndpointConfigurationDTO ec);
    List<String> getEndpointCodes(String version);
    List<String> getEndpointMessages(String epCode, String version);

//  List<AnalyzerResultDTO> getAnalyzerResults();
//  List<AnalyzerResultDTO> getAnalyzerResultsByType(DetectionRuleTypeDTO drt);
//  String setSeverityOnAnalyzerResult(AnalyzerResultDTO ar, SeverityTypeDTO type);
    String runAnalyzer(DetectionRuleTypeDTO drt);
    String runAnalyzer(Boolean continous);

    List<AlertDTO> getAlerts(String alertFilterType);
    AlertDTO getAlert(long id);
    String setSeverityOnAlert(AlertDTO alert, SeverityTypeDTO type);
    String setCauseOnAlert(AlertDTO alert, CauseDTO cause); // Used for anomalies only
    String setAnomalyStateOnAlert(AlertDTO alert, AnomalyStateDTO state);

    List<AnomalyTargetTypeDTO> getAnomalyTargetTypes();
    List<AnomalyStateDTO> getAnomalyStates();
    List<CauseDTO> getCauses();

    List<DecisionRuleDTO> getDecisionRules();
    List<DecisionRuleDTO> getDecisionRulesByViolationType(DetectionRuleTypeDTO drt);
    String addDecisionRule(DecisionRuleDTO r);
    String removeDecisionRule(DecisionRuleDTO r);

    List<DecisionDTO> getDecisions();
    List<DecisionDTO> getDecisionsByType(DecisionTypeDTO type);
    DecisionDTO getDecisionByAlert(long alertId);
    String runDecisionEngine();

    List<ActionDTO> getActions();
    String runActionEngine();
    String setActionTypeOnManualDecision(DecisionDTO decision, DecisionTypeDTO type);

    String setFirewall(Boolean on);
    Boolean isFirewallOn();

    List<XpathDTO> getXpathsByServiceCDMsgName(String cd, String version, String msgName, Boolean isArray);
    List<XpathDTO> getHeaderXpaths(Boolean isArray, String version);

    String addName(String name);
    String getName();

    Integer deleteAllEngineRunLogs();
    Integer deleteAllAlerts();
}
