/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.decision;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.essence.model.*;
import com.essence.persistence.AlertDAO;
import com.essence.persistence.ClassificationDAO;
import com.essence.persistence.DecisionDAO;
import com.essence.persistence.DAOUtil;
import com.essence.persistence.DecisionRuleDAO;

/**
 * @author pning
 *
 */
@SuppressWarnings("unused")
public class DecisionEngine {
		
	// Action rules for specific detection rule results 
	Map<Integer, DecisionRule> detectionRuleBasedDecisionRules1 = new HashMap<>();

	// list of rules for a detection type in decreasing priority order
	Map<String, List<DecisionRule>> detectionTypeBasedDecisionRules2 = new HashMap<>();
	
	// list of rules for a severity type in decreasing order
	Map<String, List<DecisionRule>> severityTypeBasedDecisionRules3 = new HashMap<>();

	Map<Long, List<DecisionRule>> causeDecisionRules4 = new HashMap<>();

	Map<Long, List<DecisionRule>> stateDecisionRules5 = new HashMap<>();
	
	public static void main(String[] args)    
	{
		DecisionEngine engine = new DecisionEngine();
		
		Classification classification = new Classification();
		classification.setClassification("Test");
		
		engine.setClassification(62, classification);

//		while (true) {
//			engine.runEnginesOnce();
//			
//			try { // otherwise, wait for 1 second and try again
//			    Thread.sleep(30000); // 1000 millis, 30 second
//			} catch(InterruptedException ex) {
//			    Thread.currentThread().interrupt();
//			}
//		}
	}

	/**
	 * detectionRuleBasedDecisionRules1 - contains decision rules that are detection rule specific. 
	 * Detection rule reference ID is the only criteria used and these decision rules are not added to
	 * the other containers. Each detection rule is associated with at most one decision rule.
	 * 
	 * detectionTypeBasedDecisionRules2 - contains decision rules that are specific to detection types.
	 * Each detection type can be associated with multiple decision rules that provide candidate decisions. 
	 * The final decision will be based on tie-breaker logic. If the rules associated with the candidate decisions 
	 * contain severity, take the decision from the decision rule that has matching severity with the finding or 
	 * otherwise has the highest severity (High/Medium/Low/Informational/Null)
	 * 
	 * severityTypeBasedDecisionRules3 - contains decision rules that are specific to a severity level without
	 * predefined detection rule reference ID or detection type. Each severity type (High/Medium/Low/Informational) 
	 * can be associated with multiple decision rules that provide candidate decisions. 
	 * The final decision will be based on tie-breaker logic. By default, take the decision from the decision rule 
	 * that has matching severity with the finding.
	 *  
	 * load all active decision rules into proper containers
	 */
	private void loadDecisionRules() {
		DecisionRuleDAO dao  = DAOUtil.getDecisionRuleDAO();
		List<DecisionRule> allDecisionRules = dao.getAllDecisionRules();
		for (DecisionRule rule: allDecisionRules) {
			if (rule.getDetectionRuleRef() != null) {
				detectionRuleBasedDecisionRules1.put(rule.getDetectionRuleRef(), rule);
			} else if (rule.getDetectionRuleType() != null) { 
				// need to figure out sequence during list insertion; for now, just get all possible decisions and use tie breaker logic
				List<DecisionRule> ruleList = detectionTypeBasedDecisionRules2.get(rule.getDetectionRuleType());
				if (ruleList == null) {
					ruleList = new ArrayList<>();
					ruleList.add(rule);
					detectionTypeBasedDecisionRules2.put(rule.getDetectionRuleType(), ruleList);
				} else {
					ruleList.add(rule);
				}	
			} else if (rule.getSeverityType() != null) {
				// need to figure out sequence during list insertion; for now, just get all possible decisions and use tie breaker logic
				List<DecisionRule> ruleList = severityTypeBasedDecisionRules3.get(rule.getSeverityType());
				if (ruleList == null) {
					ruleList = new ArrayList<>();
					ruleList.add(rule);
					severityTypeBasedDecisionRules3.put(rule.getSeverityType(), ruleList);
				} else {
					ruleList.add(rule);
				}
			} else if (rule.getCause() != null && rule.getCause().getId() > 0) {
				List<DecisionRule> ruleList = causeDecisionRules4.get(rule.getCause().getId());
				if (ruleList == null) {
					ruleList = new ArrayList<>();
					ruleList.add(rule);
					causeDecisionRules4.put(rule.getCause().getId(), ruleList);
				} else {
					ruleList.add(rule);
				}
			} else if (rule.getState() != null && rule.getState().getId() > 0 &&
					(rule.getCause() == null || rule.getCause().getId() < 1)) {
                // Only add rules with only state specified and not cause
				List<DecisionRule> ruleList = stateDecisionRules5.get(rule.getState().getId());
				if (ruleList == null) {
					ruleList = new ArrayList<>();
					ruleList.add(rule);
					stateDecisionRules5.put(rule.getState().getId(), ruleList);
				} else {
					ruleList.add(rule);
				}
			}
		}
	}
	
	private DecisionRule selectTieBreakerRule(List<DecisionRule> rules) {
		if (rules == null || rules.size() < 1)
			return null;
		
		// go through the rule and identify the decision based on tie-breaker
		DecisionRule selected = rules.get(0); // if nothing else, use the first rule
		int severityOrder = -1;
		int decisionTypeOrder = -1;
		for (DecisionRule r: rules) {
			// TODO - 1. priority based breaker to be implemented later when support for priority is defined
			
			// 2. severity based tiebreaker
			if (r.getSeverityType() != null || severityOrder > -1) { // This rule ocntains severity value, or a prior rule has it
				if (SeverityType.getOrder(r.getSeverityType()) > severityOrder) {
					severityOrder = SeverityType.getOrder(r.getSeverityType());
					selected = r;
				}
				continue; // got severity based tiebreaker, skip #3 check 
			}
			
			// 3. decision type based tiebreaker
			if (r.getDecisionType() != null && DecisionType.getOrder(r.getDecisionType()) > decisionTypeOrder) {
				decisionTypeOrder = DecisionType.getOrder(r.getDecisionType());
				selected = r;
			}
		}
		return selected;	
	}
	
	/**
	 * Make decision on the analyzer result entry and store it in the database for action layer
	 * Decision making process:
	 * 		1. If there is a decision rule defined in response to detected results of a specific detection rule, take the decision; else
	 * 		2. If there is a decision rule for the detection type, take that decision; else
	 * 		3. If there is a severity based rule for the severity level, take that decision
	 * Tie breakers:
	 * 		1. Higher priority rule takes precedence over lower priority one   (delayed)
	 * 		2. Higher severity rule takes precedence over lower severity one 
	 * 		3. Automated actions take precedence over manual actions, in decreasing order
	 * 					BLOCK_SOURCE,
	 *					BLOCK_DESTINATION,
	 *					BLOCK_BETWEEN_PAIR,
	 *					ALERT_ONLY,
	 *					MANUAL_ACTION,
	 *					IGNORE
	 * Only need to make decision for OPEN or PENDING items
	 * PENDING items did not have matching rules last time, and operator can only assign severity to influence the rule matching
	 * 
	 * @param al
	 */

	private void processAlert(Alert al) {
		if (al == null)
			return;
		
		AnalyzerResult ar = al.getAnalyzerResult();
		Anomaly an = al.getAnomaly();
		
		// Only need to make decision for OPEN or PENDING items
		// PENDING items did not have matching rules last time, and operator can only assign severity to influence the rule matching
		if (al.getStatus() == null || 
		        al.getStatus().equals(AnalyzerResultStatusType.PROCESSED.toString()) ||
		        al.getStatus().equals(AnalyzerResultStatusType.ARCHIVED.toString()))
			return; 
		
		// there is a specific decision rule for the violated detection rule
		if (ar != null) {
			if (al.getStatus().equals(AnalyzerResultStatusType.OPEN.toString()) &&
					ar.getRefRuleId() != null && detectionRuleBasedDecisionRules1.get(ar.getRefRuleId()) != null) {

				// create the decision
				DecisionRule rule = detectionRuleBasedDecisionRules1.get(ar.getRefRuleId());
				Decision decision = new Decision();
				decision.setDecisionRuleId(rule.getId());
				decision.setDecisionType(rule.getDecisionType());
				decision.setDestinationIPAddress(ar.getDstIPAddress());
				decision.setIssue(al);
				decision.setSourceIPAddress(ar.getSrcIPAddress());
				decision.setStatus(DecisionStatusType.OPEN.toString());

				// store the decision in OPEN status
				DAOUtil.getDecisionDAO().addDecision(decision);

				// update the status of AR to PROCESSED
				DAOUtil.getAlertDAO().updateStatus(al, AnalyzerResultStatusType.PROCESSED);

				return; // decision found
			}

			if (al.getStatus().equals(AnalyzerResultStatusType.OPEN.toString()) &&
					ar.getDetectorType() != null &&
					detectionTypeBasedDecisionRules2.get(ar.getDetectorType()) != null &&
					detectionTypeBasedDecisionRules2.get(ar.getDetectorType()).size() > 0) {

				DecisionRule selected = this.selectTieBreakerRule(detectionTypeBasedDecisionRules2.get(ar.getDetectorType()));

				// create the decision
				Decision decision = new Decision();
				decision.setDecisionRuleId(selected.getId());
				decision.setDecisionType(selected.getDecisionType());
				decision.setDestinationIPAddress(ar.getDstIPAddress());
				decision.setIssue(al);
				decision.setSourceIPAddress(ar.getSrcIPAddress());
				decision.setStatus(DecisionStatusType.OPEN.toString());

				// store the decision in OPEN status
				DAOUtil.getDecisionDAO().addDecision(decision);

				// update the status of AR to PROCESSED
				DAOUtil.getAlertDAO().updateStatus(al, AnalyzerResultStatusType.PROCESSED);

				return; // decision found
			}
		}

		if (an != null) {
			DecisionDAO dao = DAOUtil.getDecisionDAO();
			Decision decision = dao.getDecisionByAlertId(al.getId());

			if (decision != null) {
				if (decision.getCause() != null && decision.getCause().getId() > 0) {
					// Find decision rule by action
					DecisionRule selected = selectCauseDecisionRule(causeDecisionRules4.get(decision.getCause().getId()),
							decision.getAnomalyState());
					dao.setDecisionTypeAndDecisionRuleIdOnDecision(decision, selected.getDecisionType(), selected.getId());

					DAOUtil.getAlertDAO().updateStatus(al, AnalyzerResultStatusType.PROCESSED);
					return;
				}
				if (decision.getAnomalyState() != null && decision.getAnomalyState().getId() > 0) {
					// Find decision rule by action
					DecisionRule selected = selectStateDecisionRule(stateDecisionRules5.get(decision.getAnomalyState().getId()),
							decision.getAnomalyState());
					decision.setDecisionRuleId(selected.getId());
					dao.saveDecision(decision);

					DAOUtil.getAlertDAO().updateStatus(al, AnalyzerResultStatusType.PROCESSED);
					return;
				}
			}
		}

	    if (al.getSeverity() != null &&
				severityTypeBasedDecisionRules3.get(al.getSeverity()) != null &&
				severityTypeBasedDecisionRules3.get(al.getSeverity()).size() > 0) {

			// if severity is assigned during manual action for PENDING items, rerun engine and assign new action
			DecisionRule selected = this.selectTieBreakerRule(severityTypeBasedDecisionRules3.get(al.getSeverity()));
			
			if (al.getStatus().equals(AnalyzerResultStatusType.OPEN.toString())) {
				// create the decision
				Decision decision = new Decision();
				decision.setDecisionRuleId(selected.getId());
				decision.setDecisionType(selected.getDecisionType());

				if (ar != null) {
					decision.setDestinationIPAddress(ar.getDstIPAddress());
					decision.setSourceIPAddress(ar.getSrcIPAddress());
				}
				else if (al.getAnomaly() != null) {
					decision.setSourceIPAddress(al.getAnomaly().getSourceIPAddress());
				}
				decision.setIssue(al);
				decision.setStatus(DecisionStatusType.OPEN.toString());
				
				// store the decision in OPEN status
				DAOUtil.getDecisionDAO().addDecision(decision);
				
				// update the status of AR to PROCESSED
				DAOUtil.getAlertDAO().updateStatus(al, AnalyzerResultStatusType.PROCESSED);
				return;
				
			} else if (al.getStatus().equals(AnalyzerResultStatusType.PENDING.toString())) {
				// update the decision based on selected rules
				// set decision rule ID and decision type to the current decision
				DAOUtil.getDecisionDAO().updateDecisionForFinding(al.getId(), selected.getId(),
						DecisionType.valueOf(selected.getDecisionType()));
				
				// update status to PROCESSED
				DAOUtil.getAlertDAO().updateStatus(al, AnalyzerResultStatusType.PROCESSED);
				return;
			}
		}
		
		if (al.getStatus().equals(AnalyzerResultStatusType.OPEN.toString())) {
			// default to manual action for OPEN item
			// if severity is assigned during manual action in PENDING, rerun engine and assign new decision type if applicable
			// create the decision
			Decision decision = new Decision();
			decision.setDecisionRuleId(null); // no rules applicable yet
			decision.setDecisionType(DecisionType.MANUAL_ACTION.toString()); // default to MANUAL_ACTION

			if (ar != null) {
				decision.setDestinationIPAddress(ar.getDstIPAddress());
				decision.setSourceIPAddress(ar.getSrcIPAddress());
			}
			else if (al.getAnomaly() != null) {
				decision.setSourceIPAddress(al.getAnomaly().getSourceIPAddress());
			}

			decision.setIssue(al);
			decision.setStatus(DecisionStatusType.OPEN.toString());

			// store the decision in OPEN status
			DAOUtil.getDecisionDAO().addDecision(decision);

			// update the status of AR to PROCESSED
            DAOUtil.getAlertDAO().updateStatus(al, AnalyzerResultStatusType.PENDING);
		}
	}

	private DecisionRule selectStateDecisionRule(List<DecisionRule> decisionRules, AnomalyState anomalyState) {
        if (decisionRules == null) {
            return null;
        }

		for (DecisionRule r : decisionRules) {
			if (r.getState() != null && r.getState().getId() == anomalyState.getId()) {
				// If no matching state, use rule with no state
				return r;
			}
		}

		return null;
	}

	private DecisionRule selectCauseDecisionRule(List<DecisionRule> decisionRules, AnomalyState state) {
        if (decisionRules == null) {
            return null;
        }

		DecisionRule rule = null;
		for (DecisionRule r : decisionRules) {
			if (rule == null && (r.getState() == null || r.getState().getId() < 1)) {
				// If no matching state, use rule with no state
				rule = r;
			}
			else if (r.getState() != null && state != null && r.getState().getId() == state.getId()) {
				// First rule that matches decision cause and state is used
				return r;
			}
		}

		return rule;
	}

	public boolean setClassification(long alertId, Classification classification){
	    DecisionDAO dao = DAOUtil.getDecisionDAO();
	    Decision d = dao.getDecisionByAlertId(alertId);
	    
	    if (d == null) {
	        AlertDAO alertDAO = DAOUtil.getAlertDAO();
	        Alert alert = alertDAO.getAlertById(alertId);
	        
	        d = new Decision();
	        d.setClassification(classification);
	        d.setIssue(alert);
            d.setDecisionType(DecisionType.MANUAL_ACTION.toString()); // default to MANUAL_ACTION
            d.setStatus(DecisionStatusType.OPEN.toString());
            
            dao.addDecision(d);
	    } else {
	        ClassificationDAO cdao = DAOUtil.getClassificationDAO();
	        //d.setClassification(classification);
	        
	        dao.saveDecision(d);
	    }
	    
	    return false;
	}
	
	public void runEnginesOnce() {

		long lStartTime = System.nanoTime();
		loadDecisionRules();
		long lEndTime = System.nanoTime();
		long difference = lEndTime - lStartTime;
		System.out.println("loadDecisionRules Elapsed milliseconds: " + difference/1000000);
		
		AlertDAO dao = DAOUtil.getAlertDAO();
		
		List<Alert> openAlerts = dao.getActiveAlertsByStatus(AnalyzerResultStatusType.OPEN);

		lStartTime = System.nanoTime();
		if (openAlerts != null && !openAlerts.isEmpty()) {
			for (Alert alert: openAlerts)
				processAlert(alert);
		}
		lEndTime = System.nanoTime();
		difference = lEndTime - lStartTime;
		System.out.println("Process Open Alerts Elapsed milliseconds: " + difference/1000000);

		List<Alert> pendingAlerts = dao.getActiveAlertsByStatus(AnalyzerResultStatusType.PENDING);
		if (pendingAlerts != null && !pendingAlerts.isEmpty()) {
			for (Alert alert: pendingAlerts)
			    processAlert(alert);
		}	
	}
}
