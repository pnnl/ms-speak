/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.action;

import java.sql.Timestamp;
import java.util.List;

import com.essence.persistence.DAOUtil;
import com.essence.persistence.DecisionDAO;
import com.essence.model.Action;
import com.essence.model.Decision;
import com.essence.model.DecisionStatusType;
import com.essence.model.DecisionType;

public class ActionEngine {
	
	
	ODLNBI odlnbi = new ODLNBI();

	
	public static void main(String[] args)    
	{    
		ActionEngine engine = new ActionEngine();

		while (true) {
			engine.runEnginesOnce();
			
			try { // otherwise, wait for 1 second and try again
			    Thread.sleep(30000); // 1000 millis, 30 second
			} catch(InterruptedException ex) {
			    Thread.currentThread().interrupt();
			}
		}
	}

	public void runEnginesOnce() {
		DecisionDAO dao = DAOUtil.getDecisionDAO();
		
		List<Decision> openDecisions = dao.getDecisionsByStatus(DecisionStatusType.OPEN);
		if (openDecisions != null && !openDecisions.isEmpty()) {
			for (Decision decision: openDecisions) {
				System.out.println("Processing decision " + decision.getId());
				processDecision(decision);
			}
		}	
	}
	
	private void setCarriedOut(Decision decision, String detail) {
		Action action = new Action();
		action.setDecision(decision);
		action.setTimestamp(new Timestamp(System.currentTimeMillis()));
		if (detail == null || detail.isEmpty())
			action.setDetail("Decision successfully acted upon.");
		else
			action.setDetail(detail);
		DAOUtil.getActionDAO().addAction(action);
		DAOUtil.getDecisionDAO().updateStatus(decision, DecisionStatusType.PERFORMED);
	}

	private String sendAlert(Decision decision) {
	    // TODO: add logic for anomalies
	    
		EmailAlert a = new EmailAlert();
		a.setDestinationAddress("pning@cigital.com"); // TO-DO retrieve email from property
		a.setSubjectString("Alert Message from ESSENCE");
		StringBuffer sb = new StringBuffer();
		if (decision.getMemo() != null && !decision.getMemo().isEmpty() && 
				!decision.getDecisionType().equals(DecisionType.MANUAL_ACTION.toString())) // Manual Action uses the memo field to indicate action type 
			sb.append(decision.getMemo());
		else {
			if (decision.getIssue().getAnalyzerResult() != null && decision.getIssue().getAnalyzerResult().getRefRuleId() != null)
				sb.append("A violation of rule " + decision.getIssue().getAnalyzerResult().getRefRuleId() + " has been detected.\n");
			else
				sb.append("A violation of rule has been detected.\n");
			sb.append("Details = " + decision.getIssue().getDescription() + ".\n");
			sb.append("A manual intervention is required\n");
		}
		a.sendMessage(sb.toString());
		return sb.toString();
	}
	
	private void processDecision(Decision decision) {
		if (decision == null || !decision.getStatus().equals(DecisionStatusType.OPEN.toString()))
			return;
		
		SDNControllerNBI api = DAOUtil.getSDNControllerNBI();

		if (decision.getDecisionType().equals(DecisionType.ALERT_ONLY.toString()) || 
		   (decision.getDecisionType().equals(DecisionType.MANUAL_ACTION.toString()) && 
						DecisionType.ALERT_ONLY.toString().equals(decision.getMemo()))){

			String msg = sendAlert(decision);
			setCarriedOut(decision, "ALERT_ONLY: " + msg);
			
		} else if (decision.getDecisionType().equals(DecisionType.BLOCK_BETWEEN_PAIR.toString()) || 
				  (decision.getDecisionType().equals(DecisionType.MANUAL_ACTION.toString()) && 
						DecisionType.BLOCK_BETWEEN_PAIR.toString().equals(decision.getMemo()))){

			//if (!api.isFirewallOn())
				//api.enableFirewall(true);
			String cmd = odlnbi.applyPairBlockRule(decision.getSourceIPAddress(), "32", decision.getDestinationIPAddress(), "32", "ipv4", "drop");
			if (cmd != null)
				setCarriedOut(decision, cmd);
			
		} else if (decision.getDecisionType().equals(DecisionType.BLOCK_DESTINATION.toString()) || 
				  (decision.getDecisionType().equals(DecisionType.MANUAL_ACTION.toString()) && 
						DecisionType.BLOCK_DESTINATION.toString().equals(decision.getMemo()))){
			
			//if (!api.isFirewallOn())
				//api.enableFirewall(true);
			String cmd = odlnbi.applyDestinationBlockRule("0.0.0.0", "0",decision.getDestinationIPAddress(), "32", "ipv4", "drop");
			if (cmd != null)
				setCarriedOut(decision, cmd);
			
		} else if (decision.getDecisionType().equals(DecisionType.BLOCK_SOURCE.toString()) || 
				  (decision.getDecisionType().equals(DecisionType.MANUAL_ACTION.toString()) && 
						DecisionType.BLOCK_SOURCE.toString().equals(decision.getMemo()))){
			
			//if (!api.isFirewallOn())
				//api.enableFirewall(true);
			String cmd = odlnbi.applySourceBlockRule(decision.getSourceIPAddress(), "32", "0.0.0.0", "0", "ipv4", "drop");
			if (cmd != null)
				setCarriedOut(decision, cmd);
			
		} else if (decision.getDecisionType().equals(DecisionType.IGNORE.toString()) || 
				  (decision.getDecisionType().equals(DecisionType.MANUAL_ACTION.toString()) && 
						DecisionType.IGNORE.toString().equals(decision.getMemo()))){
			
			setCarriedOut(decision, "IGNORE: No further action.");
			
		} else if (decision.getDecisionType().equals(DecisionType.MANUAL_ACTION.toString())) {
			//TO-DO - NO-OP: not ready for action
		}
	}
}
