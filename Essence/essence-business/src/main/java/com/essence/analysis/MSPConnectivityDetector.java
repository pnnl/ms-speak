/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.analysis;

import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
//import java.util.HashSet;
//import java.util.Iterator;
import java.util.List;
import java.util.Map;
//import java.util.Set;
//import java.util.TreeSet;


import org.apache.log4j.Logger;

import com.essence.persistence.AlertDAO;
//import com.essence.persistence.AnalyzerResultDAO;
import com.essence.persistence.DAOUtil;
//import com.essence.persistence.PacketDAO;
import com.essence.model.Alert;
import com.essence.model.AnalyzerResult;
import com.essence.model.AnalyzerResultStatusType;
import com.essence.model.DetectionRule;
import com.essence.model.DetectionRuleType;
import com.essence.model.EndpointConfiguration;
//import com.essence.ui.client.object.MultiSpeakEndPointConnectivityRule;
import com.essence.ui.shared.StringUtil;
import com.essence.multispeak.MSPServiceOperation;

//import org.hibernate.criterion.Order;

public class MSPConnectivityDetector implements PacketAnalyzer {
	
	static Logger log = Logger.getLogger(MSPConnectivityDetector.class.getName());
	
	/* State of the analyzer */
	private List<Alert> alerts = null; // accumulating results and store in done()
	
	/* MSP version number is part of the lookup key for all maps */
	private Map<String, Map<String, Integer>> allowedConnectivities = null; // source endpoint-version and allowed destination endpoints and rule ID
	private Map<String, Map<String, Integer>> disallowedConnectivities = null; // source endpoint-version and disallowed destination endpoints and rule ID
	private Map<String, Map<String, MSPServiceOperation>> validEndpointOperations = null; // what operations are valid for an endpoint by name-version
	private Map<String, EndpointConfiguration> hostEndpointConfigurations = null; // map IP address to a set of endpoint codes-version

	private long nowInMillis = -1l; // point of detection - end of detecting window
	private long lastRunCutoffInMillis = -1l; // point of last detection - end of last detecting window, should use packet retrieval time
	private long currentRunCutoffInMillis = -1l; // most recent timestamp of all the packets seen this time
	
	public static void main(String[] args)    
	{    	
		MSPConnectivityDetector d = new MSPConnectivityDetector();
		d.activate();
		/*
		PacketDAO dao = DAOUtil.getPacketDAO();
		List<Packet> packets = dao.getAllPackets();
		d.analyse(packets);
		d.done();
		for (int i=0; i<packets.size(); i++)
			d.analyse(packets.get(i));
		d.done();
		*/
		d.done();
	}

	public void activate() { // set up fresh starting configuration for a run
		nowInMillis = System.currentTimeMillis();
		allowedConnectivities = new HashMap<>(); // source endpoint and allowed destination endpoints and rule ID
		disallowedConnectivities = new HashMap<>(); // source endpoint and disallowed destination endpoints and rule ID
		validEndpointOperations = new HashMap<>(); // what operations are valid for an endpoint by name
		hostEndpointConfigurations = new HashMap<>(); // map host IP to a set of endpoint codes that have been assigned to it
		alerts = new ArrayList<>(); // fresh container for results
		
		// Loading the rules into two maps of maps that map source to destination to ruleId, 
		// one for allowed connectivities, and one for disallowed connectivities
		List<DetectionRule> epRules = DAOUtil.getDetectionRuleDAO().getActiveDetectionRulesByType(DetectionRuleType.MS_EP_CONNECTIVITY);
		if (epRules != null && !epRules.isEmpty()) {
			for (int i=0; i<epRules.size(); i++) {
				String key = StringUtil.combineVersion(epRules.get(i).getSrcEndpointType(),epRules.get(i).getVersion());
				if (epRules.get(i).getRuleType().equals(DetectionRuleType.MS_EP_CONNECTIVITY.toString()) && epRules.get(i).getActionType().equalsIgnoreCase("allowed")) {
					Map<String, Integer> allowedMap = allowedConnectivities.get(key);
					if (allowedMap == null) {
						allowedMap = new HashMap<>();
						allowedMap.put(epRules.get(i).getDstEndpointType(), epRules.get(i).getId());
						allowedConnectivities.put(key, allowedMap);
					} else {
						allowedMap.put(epRules.get(i).getDstEndpointType(), epRules.get(i).getId());
					}
				} else if (epRules.get(i).getRuleType().equals(DetectionRuleType.MS_EP_CONNECTIVITY.toString()) && epRules.get(i).getActionType().equalsIgnoreCase("disallowed")) {
					Map<String, Integer> disallowedMap = disallowedConnectivities.get(key);
					if (disallowedMap == null) {
						disallowedMap = new HashMap<>();
						disallowedMap.put(epRules.get(i).getDstEndpointType(), epRules.get(i).getId());
						disallowedConnectivities.put(key, disallowedMap);
					} else {
						disallowedMap.put(epRules.get(i).getDstEndpointType(), epRules.get(i).getId());
					}					
				}
			}
		} else {
			log.warn("There are no MultiSpeak Connectivity Rule defined.");
		}
		
		// map endpoint code to endpoint operations to endpoint operation definitions
		List<MSPServiceOperation> operations = DAOUtil.getMSPServiceOperationDAO().getAllMSPServiceOperations();
		for (int i=0; i<operations.size(); i++) {
			String key = StringUtil.combineVersion(operations.get(i).getServiceCode(),operations.get(i).getServicePK().getVersion());
			Map<String, MSPServiceOperation> epOpMap = validEndpointOperations.get(key); // mapped by service code and version
			if (epOpMap == null) {
				epOpMap = new HashMap<>();
				epOpMap.put(operations.get(i).getServicePK().getOperationName(), operations.get(i));
				validEndpointOperations.put(key, epOpMap);
			} else {
				epOpMap.put(operations.get(i).getServicePK().getOperationName(), operations.get(i));				
			}
		}
		
		// load endpoint configurations to map IPs to the set of endpoint codes each is associated with
		List<EndpointConfiguration> hostEndpoints = DAOUtil.getEndpointConfigurationDAO().getAllActiveEndpointConfigurations();
		for (EndpointConfiguration hostEPConfig : hostEndpoints) {
			hostEndpointConfigurations.put(hostEPConfig.getKey().getHostIPAddress(), hostEPConfig);
		}
		System.out.println("done activating MSPConnectivityDetector");
	}
	
	public void analyse(List<Packet> packets) {
		if (packets == null || packets.isEmpty())
			return;

		for (Packet packet : packets) analyse(packet);
	}
	
	/**
	 * 
	 * @param hostIP host ip adress
	 * @param op operation
	 * @return endpoint code that contains the op; or null
	 */
	private String isOperationValidForHostEndpoints(String hostIP, String op, String version) {
		
		if (hostIP == null || op == null || version == null)
			return null;

		EndpointConfiguration ep = hostEndpointConfigurations.get(hostIP);
		if (ep == null || ep.getEndpointList() == null || ep.getEndpointList().isEmpty() || !version.equalsIgnoreCase(ep.getVersion())) {
			log.warn("There is no endpoint configuration for " + hostIP + " and version " + version);
			//TO-DO store result?
			return null;
		}

		String[] dstCodes = ep.getEndpointCDs();

		for (String dstCode : dstCodes) {
			String key = StringUtil.combineVersion(dstCode, version);
			if (validEndpointOperations.get(key) != null && validEndpointOperations.get(key).containsKey(op))
				return dstCode;
		}
		
		return null;
	}
	
	private Integer canSourceConnectToEndpoint(String srcHostIP, String epCode, String version) {
		
		if (srcHostIP == null || epCode == null || version == null)
			return null;

		EndpointConfiguration ep = hostEndpointConfigurations.get(srcHostIP);
		if (ep == null || ep.getEndpointList() == null || ep.getEndpointList().isEmpty() || !version.equalsIgnoreCase(ep.getVersion())) {
			log.warn("There is no endpoint configuration for " + srcHostIP + " and version " + version);
			//TO-DO store result?
			return null;
		}

		String[] srcCodes = ep.getEndpointCDs();
		for (String srcCode : srcCodes) {
			String key = StringUtil.combineVersion(srcCode, version);
			if (allowedConnectivities.get(key) != null && allowedConnectivities.get(key).get(epCode) != null)
				return allowedConnectivities.get(key).get(epCode);
		}
		
		return null;
	}
	
	private Integer isSourceConnectToEndpointDisallowed(String srcHostIP, String epCode, String version) {
		
		if (srcHostIP == null || epCode == null || version == null)
			return null;

		EndpointConfiguration ep = hostEndpointConfigurations.get(srcHostIP);
		if (ep == null || ep.getEndpointList() == null || ep.getEndpointList().isEmpty() || !version.equalsIgnoreCase(ep.getVersion())) {
			log.warn("There is no endpoint configuration for " + srcHostIP + " and version " + version);
			//TO-DO store result?
			return null;
		}

		String[] srcCodes = ep.getEndpointCDs();
		for (String srcCode : srcCodes) {
			String key = StringUtil.combineVersion(srcCode, version);
			if (disallowedConnectivities.get(key) != null && disallowedConnectivities.get(key).get(epCode) != null)
				return disallowedConnectivities.get(key).get(epCode);
		}
		
		return null;
	}
	
	public void analyse(Packet p) {
		if (allowedConnectivities.isEmpty() && disallowedConnectivities.isEmpty()) {
			log.warn("There are no MultiSpeak Connectivity Rule defined!");
			return;
		}
		
		String src = p.getPacketPK().getSourceAddress();
		String dst = p.getPacketPK().getDestAddress();
		String version = p.getMspVersion();
		long timestamp = p.getPacketPK().getTimeStamp().getTime();
		
		// Keep track of the latest timestamp in packets
		if (timestamp > currentRunCutoffInMillis)
			currentRunCutoffInMillis = timestamp;
		
		if (timestamp <= this.lastRunCutoffInMillis) { // already covered - no need to check again to avoid duplicate
			return;
		}
		
		if (p.getTextValues() == null || p.getTextValues().get(Packet.MESSAGE_TYPE_KEY) == null || version == null) { // no message type, not applicable to this detector
			// flag a warning result? and return
			// log.warn("There is no message type for packet between " + src + " and " + dst);
			return;
		}

		EndpointConfiguration srcConfiguration = this.hostEndpointConfigurations.get(src);
		EndpointConfiguration dstConfiguration = this.hostEndpointConfigurations.get(dst);
		String srcEndpointList;
		String dstEndpointList;

		if (srcConfiguration != null) {
			srcEndpointList = srcConfiguration.getEndpointList();
		} else {
			srcEndpointList = "unknown endpoint";
		}

		if (dstConfiguration != null) {
			dstEndpointList = dstConfiguration.getEndpointList();
		} else {
			dstEndpointList = "unknown endpoint";
		}

		String msgType = p.getTextValues().get(Packet.MESSAGE_TYPE_KEY);
		
		if (msgType.endsWith("Response")) { // response message
			msgType = msgType.substring(0, msgType.length()-8);
			// step 1: check source host endpoints to see if the message is valid for them. if yes obtain the endpoint code
			String srcCDForOp = isOperationValidForHostEndpoints(src, msgType, version); // the request type should be valid for the source who is sending the response
			if (srcCDForOp == null) { // violation - message type not supported by source host endpoints
				String description = "Host " + src + "(" + srcEndpointList +
						") sent a response message for invalid type " + msgType + " for its endpoints to destination " +
						dst + " of version " + version;
				AddResult(src, dst, DetectionRuleType.WRONG_MSG_TO_MS_EP.toString(), description,
						p.getPacketPK().getTimeStamp());
				return;
			}
			
			// step 2: check rules based on endpoint code and see if the destination is explicitly disallowed to have
			// connectivity to the source endpoint sending the response
			// This category will take priority over the allowed rules
			Integer ruleId2 = isSourceConnectToEndpointDisallowed(dst, srcCDForOp, version);
			if (ruleId2 != null) { // violation - no rule to allow the connectivity
				String description = "Host " + src + "(" + srcEndpointList + ") sent a response message of " +
						msgType + " to " + dst + "(" + dstEndpointList + ") with disallowed connectivity, version " +
						version;
				AddResult(src, dst, DetectionRuleType.MS_EP_CONNECTIVITY.toString(), description,
						p.getPacketPK().getTimeStamp());
				return;
			}

			// step 3: check rules based on source host endpoint code and see if the destination host could have
			// connectivity to it
			Integer ruleId1 = canSourceConnectToEndpoint(dst, srcCDForOp, version);
			if (ruleId1 == null) { // violation - no rule to allow the connectivity
				String description = "Host " + src + "(" + srcEndpointList + ") sent a response message of " + msgType +
						" to " + dst + "(" + dstEndpointList + ") without allowed connectivity, version " + version;
				AddResult(src, dst, DetectionRuleType.MS_EP_CONNECTIVITY.toString(), description,
						p.getPacketPK().getTimeStamp());
				return;
			}
			
		} else { // request message
		
			// step 1: check host endpoints to see if the message is valid for them. if yes obtain the endpoint code
			String dstCDForOp = isOperationValidForHostEndpoints(dst, msgType, version);
			if (dstCDForOp == null) { // violation - message type not supported by host endpoints
				String description = "Host " + src + " sent a message of invalid type " + msgType +
						" for endpoints of destination " + dst + "(" + dstEndpointList + ") of version " + version;
				AddResult(src, dst, DetectionRuleType.WRONG_MSG_TO_MS_EP.toString(), description,
						p.getPacketPK().getTimeStamp());
				return;
			}

			// step 2: check rules based on endpoint code and see if the source endpoints is explicitly disallowed to have connectivity to it
			// This category will take priority over the allowed rules
			Integer ruleId2 = isSourceConnectToEndpointDisallowed(src, dstCDForOp, version);
			if (ruleId2 != null) { // violation - no rule to allow the connectivity
				String description = "Host " + src + "(" + srcEndpointList + ") sent a message of " + msgType + " to " +
						dst + "(" + dstEndpointList + ") with disallowed connectivity, version " + version;
				AddResult(src, dst, DetectionRuleType.MS_EP_CONNECTIVITY.toString(), description,
						p.getPacketPK().getTimeStamp());
				return;
			}

			// step 3: check rules based on endpoint code and see if the source endpoints can have connectivity to it
			Integer ruleId1 = canSourceConnectToEndpoint(src, dstCDForOp, version);
			if (ruleId1 == null) { // violation - no rule to allow the connectivity
				String description = "Host " + src + "(" + srcEndpointList + ") sent a message of " + msgType + " to " +
						dst + "(" + dstEndpointList + ") without allowed connectivity, version " + version;
				AddResult(src, dst, DetectionRuleType.MS_EP_CONNECTIVITY.toString(), description,
						p.getPacketPK().getTimeStamp());
				return;
			}
		}
	}

    private Alert createAlert(String description, AnalyzerResultStatusType status, String detectorType,
            Long runTime, String sourceIpAddress, String destinationIpAddress, Timestamp timestamp) {
        Alert al = new Alert();
        al.setDescription(description);
        al.setStatus(status);
        al.setAlertTypeId(1);
        al.setCreationTime(new Date());
        
        AnalyzerResult ar = new AnalyzerResult();
		ar.setTimeStamp(timestamp);
        ar.setDetectorType(detectorType);
        ar.setRunTime(runTime);
        ar.setSrcIPAddress(sourceIpAddress);
        ar.setDstIPAddress(destinationIpAddress);
        
        al.setAnalyzerResult(ar);
        
        return al;
    }

	private void AddResult(String src, String dst, String detectorType, String description, Timestamp timestamp) {
	    Alert alert = createAlert(description, AnalyzerResultStatusType.OPEN, detectorType, nowInMillis, src, dst,
				timestamp);
	    this.alerts.add(alert);
	    
		//this.detectionResults.add(ar);
	}

	public void done() {
		
		if (alerts == null || alerts.isEmpty())
			return;

		AlertDAO dao = DAOUtil.getAlertDAO();

		for (Alert alert : alerts) {
			dao.addAlert(alert);
		}
	}

	public long getLastRunCutoffInMillis() {
		return lastRunCutoffInMillis;
	}

	public void setLastRunCutoffInMillis(long lastRunCutoffInMillis) {
		this.lastRunCutoffInMillis = lastRunCutoffInMillis;
	}

	public long getCurrentRunCutoffInMillis() {
		return currentRunCutoffInMillis;
	}

	public void setCurrentRunCutoffInMillis(long currentRunCutoffInMillis) {
		this.currentRunCutoffInMillis = currentRunCutoffInMillis;
	}	
}
