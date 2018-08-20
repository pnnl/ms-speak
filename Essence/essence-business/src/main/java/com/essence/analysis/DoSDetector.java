/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.analysis;

import java.util.Date;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.apache.log4j.Logger;

import com.essence.persistence.AlertDAO;
import com.essence.persistence.CassandraDAOUtil;
import com.essence.persistence.DAOUtil;
import com.essence.persistence.PacketDAO;
import com.essence.model.Alert;
import com.essence.model.AnalyzerResult;
import com.essence.model.AnalyzerResultStatusType;
import com.essence.model.DetectionRule;
import com.essence.model.DetectionRuleType;

public class DoSDetector implements PacketAnalyzer {
	
	static public final int DOS_PACKETS_NUMBER_BETWEEN_HOSTS = 20;
	static public final int DOS_PACKETS_NUMBER_FROM_A_HOST = 30;
	static public final int DOS_PACKETS_NUMBER_TO_A_HOST = 40;
	
	static Logger log = Logger.getLogger(DoSDetector.class.getName());
	
	/* State of the analyzer */
	private DetectionRule dosRule = null; // current applicable rule
	private long nowInMillis = -1l; // point of detection - end of detecting window
	private long lastRunCutoffInMillis = -1l; // point of last detection - end of last detecting window, should use packet retrieval time
	private long currentRunCutoffInMillis = -1l; // most recent timestamp of all the packets seen this time
	private Map<String, Integer> sourceCounts = null;  // count packets sent from a source
	private Map<String, Map<String,Integer>> sourceDestinationCounts = null; // count packets from a source to a destination
	
	public static void main(String[] args)    
	{    	
		DoSDetector d = new DoSDetector();
		d.activate();
		PacketDAO dao = CassandraDAOUtil.getPacketDAO();
		List<Packet> packets = dao.getAllPackets();
		d.analyse(packets);
		d.done();
		for (int i=0; i<packets.size(); i++)
			d.analyse(packets.get(i));
		d.done();
	}

	public void activate() { // set up fresh starting configuration for a run
		nowInMillis = System.currentTimeMillis();
		sourceCounts = new HashMap<String, Integer>();
		sourceDestinationCounts = new HashMap<String, Map<String,Integer>>();
		
		List<DetectionRule> dosRules = DAOUtil.getDetectionRuleDAO().getActiveDetectionRulesByType(DetectionRuleType.DENIAL_OF_SERVICE);

		if (dosRules != null && !dosRules.isEmpty()) {
			for (int i=0; i<dosRules.size(); i++)
				if (dosRules.get(i).getNumberOfPacketsForDoS() != null && dosRules.get(i).getTimeWindowInSeconds() != null) {
					dosRule = dosRules.get(i);
					break;
				}
		}
		System.out.println("done activating DoSDetector");
	}
	
	public void analyse(List<Packet> packets) {
		if (packets == null || packets.isEmpty())
			return;
		
		for (int i=0; i<packets.size(); i++)
			analyse(packets.get(i));
	}
	
	public void analyse(Packet p) {
		if (dosRule == null) {
			log.warn("No DOS rule exist!");
			return;
		}
		
		String src = p.getPacketPK().getSourceAddress();
		String dst = p.getPacketPK().getDestAddress();
		long timestamp = p.getPacketPK().getTimeStamp().getTime();
		
		if (timestamp > currentRunCutoffInMillis)
			currentRunCutoffInMillis = timestamp;
		
		if (timestamp < this.lastRunCutoffInMillis) { // already covered - no need to check again to avoid duplicate
			return;
		}
		
		if (nowInMillis - timestamp > dosRule.getTimeWindowInSeconds()*1000) // outside of time window 
			return;
		
		if (!sourceCounts.containsKey(src)) {
			sourceCounts.put(src, 1); // create an entry for source and get the first count
			Map<String, Integer> srcDestCount = new HashMap<String, Integer>();
			srcDestCount.put(dst, 1);
			sourceDestinationCounts.put(src, srcDestCount);
		} else {
			Integer cnt = sourceCounts.get(src);
			cnt++;
			sourceCounts.put(src, cnt);
			Map<String, Integer> dstCountMap = sourceDestinationCounts.get(src);
			if (!dstCountMap.containsKey(dst)) {
				dstCountMap.put(dst, 1);
			} else {
				Integer dstCnt = dstCountMap.get(dst);
				dstCnt++;
				dstCountMap.put(dst, dstCnt);
			}
			sourceDestinationCounts.put(src, dstCountMap);
		}
	}
	
	private Alert createAlert(String description, AnalyzerResultStatusType status, String ruleType, Integer numberOfDosPackets, Integer refRuleId,
	        Long runTime, String sourceIpAddress, String destinationIpAddress, Long timeWindowInSeconds) {
	    Alert al = new Alert();
	    al.setDescription(description);
	    al.setStatus(status);
	    al.setAlertTypeId(1);
	    al.setCreationTime(new Date());
	    
	    AnalyzerResult ar = new AnalyzerResult();
	    ar.setDetectorType(ruleType);
	    ar.setNumberOfPacketsForDoS(numberOfDosPackets);
	    ar.setRefRuleId(refRuleId);
	    ar.setRunTime(runTime);
	    ar.setSrcIPAddress(sourceIpAddress);
	    ar.setDstIPAddress(destinationIpAddress);
	    ar.setTimeWindowInSeconds(timeWindowInSeconds);

        al.setAnalyzerResult(ar);
        
	    return al;
	}
	
	public void done() {
		Set<String> srcs = sourceCounts.keySet();
		Iterator<String> srcIterator = srcs.iterator();
		AlertDAO dao = DAOUtil.getAlertDAO();
		
		while (srcIterator.hasNext()) {
			String src = srcIterator.next();
			if (sourceCounts.get(src) >= dosRule.getNumberOfPacketsForDoS()) {
				// got one from source 
				System.out.println("Host " + src + " is trying DOS attack with " + sourceCounts.get(src) + " packets within " + dosRule.getTimeWindowInSeconds() + " seconds");
				// store it
				Alert alert = createAlert("Host " + src + " is trying DOS attack with " + sourceCounts.get(src) + " packets within " + dosRule.getTimeWindowInSeconds() + " seconds",
				        AnalyzerResultStatusType.OPEN, DetectionRuleType.DENIAL_OF_SERVICE.toString(), sourceCounts.get(src), dosRule.getId(), nowInMillis,
				        src, null, dosRule.getTimeWindowInSeconds());
				
				dao.addAlert(alert);
			}
			
			Map<String, Integer> dstMap = sourceDestinationCounts.get(src);
			Set<String> dsts = dstMap.keySet();
			Iterator<String> dstIterator = dsts.iterator();
			while (dstIterator.hasNext()) {
				String dst = dstIterator.next();
				if (dstMap.get(dst) >= dosRule.getNumberOfPacketsForDoS()) {
					// got one between hosts
					System.out.println("Host " + src + " is trying DOS attack host " + dst + " with " + dstMap.get(dst) + " packets within " + dosRule.getTimeWindowInSeconds() + " seconds");
					// store it
		               Alert alert = createAlert("Host " + src + " is trying DOS attack host " + dst + " with " + dstMap.get(dst) + " packets within " + dosRule.getTimeWindowInSeconds() + " seconds",
		                        AnalyzerResultStatusType.OPEN, DetectionRuleType.DENIAL_OF_SERVICE.toString(), dstMap.get(dst), dosRule.getId(), nowInMillis,
		                        src, dst, dosRule.getTimeWindowInSeconds());
		               dao.addAlert(alert);
				}
			}	
		}
	}

	public DetectionRule getDosRule() {
		return dosRule;
	}

	public void setDosRule(DetectionRule dosRule) {
		this.dosRule = dosRule;
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
