/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client;

import java.util.List;
import java.util.Map;

import com.essence.ui.client.object.*;
import com.google.gwt.user.client.rpc.AsyncCallback;

public interface GreetingServiceAsync {
	void greetServer(String name, AsyncCallback<String> callback) throws IllegalArgumentException;

	void getAllOrganizations(AsyncCallback<List<OrganizationProfileDTO>> callback);
	void activateOrganization(int id, AsyncCallback<String> callback);

	void getDetectionRules(AsyncCallback<List<DetectionRuleDTO>> callback);
	void getDetectionRuleByID(int id, AsyncCallback<DetectionRuleDTO> callback);

	void addMSEndPointConnectivityRule(MultiSpeakEndPointConnectivityRule rule, AsyncCallback<String> callback);
	void addGeneralDetectionRule(DetectionRuleDTO rule, AsyncCallback<String> callback);
	void removeGeneralDetectionRule(DetectionRuleDTO rule, AsyncCallback<String> callback);
	void addValueOutOfBoundRule(DetectionRuleDTO rule, List<ValueOutOfBoundDetailDTO> details, AsyncCallback<String> callback);
	void getValueOutOfBoundRuleDetails(List<Integer> ruleIds, AsyncCallback<Map<Integer, List<ValueOutOfBoundDetailDTO>>> callback);

	void getEndpointConfigurations(AsyncCallback<List<EndpointConfigurationDTO>> callback);
	void addEndpointConfiguration(EndpointConfigurationDTO ec, AsyncCallback<String> callback);
	void removeEndpointConfiguration(EndpointConfigurationDTO ec, AsyncCallback<String> callback);
	void saveEndpointConfiguration(EndpointConfigurationDTO ec, AsyncCallback<String> callback);
	void getEndpointCodes(String version, AsyncCallback<List<String>> callback);
	void getEndpointMessages(String epCode, String version, AsyncCallback<List<String>> callback);
	void getXpathsByServiceCDMsgName(String cd, String version, String msgName, Boolean isArray, AsyncCallback<List<XpathDTO>> callback);
	void getHeaderXpaths(Boolean isArray, String version, AsyncCallback<List<XpathDTO>> callback);

//	   void getAnalyzerResults(AsyncCallback<List<AnalyzerResultDTO>> callback);
//	   void getAnalyzerResultsByType(DetectionRuleTypeDTO drt, AsyncCallback<List<AnalyzerResultDTO>> callback);
//	   void setSeverityOnAnalyzerResult(AnalyzerResultDTO ar, SeverityTypeDTO type, AsyncCallback<String> callback);

	void getAlerts(String alertFilterType, AsyncCallback<List<AlertDTO>> callback);
	void setSeverityOnAlert(AlertDTO alert, SeverityTypeDTO type, AsyncCallback<String> callback);
	void setCauseOnAlert(AlertDTO alert, CauseDTO cause, AsyncCallback<String> callback); // Used for anomalies only

	void runAnalyzer(DetectionRuleTypeDTO drt, AsyncCallback<String> callback);
	void runAnalyzer(Boolean continous, AsyncCallback<String> callback);

	void getDecisionRules(AsyncCallback<List<DecisionRuleDTO>> callback);
	void getDecisionRulesByViolationType(DetectionRuleTypeDTO drt, AsyncCallback<List<DecisionRuleDTO>> callback);

	void addDecisionRule(DecisionRuleDTO rule, AsyncCallback<String> callback);
	void removeDecisionRule(DecisionRuleDTO rule, AsyncCallback<String> callback);

	void getDecisions(AsyncCallback<List<DecisionDTO>> callback);
	void getDecisionsByType(DecisionTypeDTO type, AsyncCallback<List<DecisionDTO>> callback);
	void runDecisionEngine(AsyncCallback<String> callback);

	void getActions(AsyncCallback<List<ActionDTO>> callback);
	void runActionEngine(AsyncCallback<String> callback);
	void setActionTypeOnManualDecision(DecisionDTO decision, DecisionTypeDTO type, AsyncCallback<String> callback);

	void setFirewall(Boolean on, AsyncCallback<String> callback);
	void isFirewallOn(AsyncCallback<Boolean> callback);

	void addName(String name, AsyncCallback<String> callback);
	void getName(AsyncCallback<String> callback);

	void deleteAllEngineRunLogs(AsyncCallback<Integer> callback);
	void deleteAllAlerts(AsyncCallback<Integer> callback);

	void getAnomalyTargetTypes(AsyncCallback<List<AnomalyTargetTypeDTO>> async);

	void getEndpointConfiguration(String ipAddress, AsyncCallback<EndpointConfigurationDTO> async);

	void getDecisionByAlert(long alertId, AsyncCallback<DecisionDTO> async);

	void getAnomalyStates(AsyncCallback<List<AnomalyStateDTO>> async);

	void getSetting(String settingName, AsyncCallback<String> async);

	void updateSetting(String settingName, String value, AsyncCallback<String> async);

	void setAnomalyStateOnAlert(AlertDTO alert, AnomalyStateDTO state, AsyncCallback<String> async);

	void getCauses(AsyncCallback<List<CauseDTO>> async);

	void getAlert(long id, AsyncCallback<AlertDTO> async);
}
