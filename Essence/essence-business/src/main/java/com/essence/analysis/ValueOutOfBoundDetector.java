/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.analysis;

import java.io.IOException;
import java.io.StringReader;
import java.io.UnsupportedEncodingException;
import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.xml.XMLConstants;
import javax.xml.bind.DatatypeConverter;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import java.lang.IllegalArgumentException;

import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathFactory;

import org.apache.log4j.Logger;
import org.w3c.dom.Document;
import org.w3c.dom.Node;
//import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;

import com.essence.multispeak.MSPServiceOperationKey;
import com.essence.persistence.AlertDAO;
import com.essence.persistence.CassandraDAOUtil;
import com.essence.persistence.DAOUtil;
import com.essence.persistence.PacketDAO;
import com.essence.model.Alert;
import com.essence.model.AnalyzerResult;
import com.essence.model.AnalyzerResultStatusType;
import com.essence.model.DetectionRule;
import com.essence.model.DetectionRuleType;
import com.essence.model.EndpointConfiguration;
import com.essence.model.ValueOperatorType;
import com.essence.model.ValueOutOfBoundDetail;
import com.essence.model.Xpath;
import com.essence.ui.shared.StringUtil;

import org.apache.commons.codec.binary.Base64;

public class ValueOutOfBoundDetector implements PacketAnalyzer {
	static Logger log = Logger.getLogger(ValueOutOfBoundDetector.class.getName());
	
	/* State of the analyzer */
	private List<Alert> alerts = null; // accumulating results and store in done()
	private Map<String, Map<String, List<DetectionRule>>> voobRulesByServiceCDandMsgName = null;
//	List<DetectionRule> voobRules = null;
	private long nowInMillis = -1l; // point of detection - end of detecting window
	private long lastRunCutoffInMillis = -1l; // point of last detection - end of last detecting window, should use packet retrieval time
	private long currentRunCutoffInMillis = -1l; // most recent timestamp of all the packets seen this time

	public static void main(String[] args)    
	{    	
		ValueOutOfBoundDetector d = new ValueOutOfBoundDetector();
		d.activate();
		
		PacketDAO dao = CassandraDAOUtil.getPacketDAO();
		List<Packet> packets = dao.getAllPacketsN(1000);
		d.analyse(packets);

		d.done();
	}

	public void activate() { // set up fresh starting configuration for a run
		
		nowInMillis = System.currentTimeMillis();
		alerts = new ArrayList<Alert>(); // fresh container for results		
		List<DetectionRule> voobRules = DAOUtil.getDetectionRuleDAO().getActiveDetectionRulesByType(DetectionRuleType.VALUE_OUT_OF_BOUND);
		if (voobRules == null || voobRules.isEmpty()) {
			log.warn("There are no MultiSpeak Connectivity Rule defined.");
		} else {
			DAOUtil.getDetectionRuleDAO().setDetectionRuleDetails4Rules(voobRules);
			DAOUtil.getDetectionRuleDAO().setDetectionRuleXpathDetails4Voobs(voobRules);			
		}
		
		voobRulesByServiceCDandMsgName = new HashMap<String, Map<String, List<DetectionRule>>>();
		for (DetectionRule r : voobRules) {
			r.print();
			int msgIdx = r.getNonHeaderIndexOfVooBDetails();
			System.out.println("msgIdx = " + msgIdx);
			String version = r.getVoobDetails().get(msgIdx).getVersion(); 
			System.out.println("version = " + version);
			String cd = r.getVoobDetails().get(msgIdx).getEndpointCode();
			String msgName = r.getVoobDetails().get(msgIdx).getMessageName();
			String key = StringUtil.combineVersion(cd, version);
			Map<String, List<DetectionRule>> byCD =  voobRulesByServiceCDandMsgName.get(key);
			if (byCD == null) { // create new submap for the CD
				byCD = new HashMap<String, List<DetectionRule>>();
				List<DetectionRule> byMsgName = new ArrayList<DetectionRule>();
				byMsgName.add(r);
				byCD.put(msgName, byMsgName);
				voobRulesByServiceCDandMsgName.put(key, byCD);
			} else {
				List<DetectionRule> byMsgName = byCD.get(msgName);
				if (byMsgName == null) {
					byMsgName = new ArrayList<DetectionRule>();
					byMsgName.add(r);
					byCD.put(msgName, byMsgName);
				} else {
					byMsgName.add(r);
				}
			}
		}
		
		System.out.println("done activating ValueOutOfBoundDetector");
	}
	
	public void analyse(List<Packet> packets) {
		if (packets == null || packets.isEmpty())
			return;
		
		for (int i=0; i<packets.size(); i++)
			analyse(packets.get(i));
	}

	private boolean checkStringCondition(String op, String targetVal, String value) {
		ValueOperatorType opt = ValueOperatorType.textToValue(op);
		
		if (opt == ValueOperatorType.EQUAL_TO)
			return value.equalsIgnoreCase(targetVal);
		else if (opt == ValueOperatorType.GREATER_THAN)
			return value.compareTo(targetVal) > 0;
		else if (opt == ValueOperatorType.GREATER_THAN_EQUAL_TO)
				return value.compareTo(targetVal) >= 0;
		else if (opt == ValueOperatorType.LESS_THAN)
					return value.compareTo(targetVal) < 0;
		else if (opt == ValueOperatorType.LESS_THEN_EQUAL_TO)
			return value.compareTo(targetVal) <= 0;
		else if (opt == ValueOperatorType.NOT_EQUAL_TO)
			return value.compareTo(targetVal) != 0;
		
		return false;
	}
	
	private boolean checkDoubleCondition(String op, String targetVal, String value) {
		ValueOperatorType opt = ValueOperatorType.textToValue(op);
		Double target = StringUtil.textToDouble(targetVal);
		Double v = StringUtil.textToDouble(value);
		if (target == null || v == null) // not comparable
			return false;
		
		if (opt == ValueOperatorType.EQUAL_TO)
			return v.doubleValue() == target.doubleValue();
		else if (opt == ValueOperatorType.GREATER_THAN)
			return v.doubleValue() > target.doubleValue();
		else if (opt == ValueOperatorType.GREATER_THAN_EQUAL_TO)
			return v.doubleValue() >= target.doubleValue();
		else if (opt == ValueOperatorType.LESS_THAN)
			return v.doubleValue() < target.doubleValue();
		else if (opt == ValueOperatorType.LESS_THEN_EQUAL_TO)
			return v.doubleValue() <= target.doubleValue();
		else if (opt == ValueOperatorType.NOT_EQUAL_TO)
			return v.doubleValue() != target.doubleValue();
		
		return false;
	}
	
	private boolean checkLongCondition(String op, String targetVal, String value) {
		ValueOperatorType opt = ValueOperatorType.textToValue(op);
		Long target = StringUtil.textToLong(targetVal);
		Long v = StringUtil.textToLong(value);
		if (target == null || v == null) // not comparable
			return false;
		
		if (opt == ValueOperatorType.EQUAL_TO)
			return v.longValue() == target.longValue();
		else if (opt == ValueOperatorType.GREATER_THAN)
			return v.longValue() > target.longValue();
		else if (opt == ValueOperatorType.GREATER_THAN_EQUAL_TO)
			return v.longValue() >= target.longValue();
		else if (opt == ValueOperatorType.LESS_THAN)
			return v.longValue() < target.longValue();
		else if (opt == ValueOperatorType.LESS_THEN_EQUAL_TO)
			return v.longValue() <= target.longValue();
		else if (opt == ValueOperatorType.NOT_EQUAL_TO)
			return v.longValue() != target.longValue();
		
		return false;
	}
	
	private boolean checkBooleanCondition(String op, String targetVal, String value) {
		ValueOperatorType opt = ValueOperatorType.textToValue(op);
		Boolean target = Boolean.valueOf(targetVal);
		Boolean v = Boolean.valueOf(value);
		if (target == null || v == null) // not comparable
			return false;
		
		if (opt == ValueOperatorType.EQUAL_TO)
			return v == target;
		else if (opt == ValueOperatorType.NOT_EQUAL_TO)
			return v != target;
		else if (opt == ValueOperatorType.GREATER_THAN)
			return false; // not applicable
		else if (opt == ValueOperatorType.GREATER_THAN_EQUAL_TO)
			return v == target;
		else if (opt == ValueOperatorType.LESS_THAN)
			return false; // not applicable
		else if (opt == ValueOperatorType.LESS_THEN_EQUAL_TO)
			return v == target;
		return false;
	}

	private boolean checkBase64BinaryCondition(String op, String targetVal, String value) {
		if (!Base64.isBase64(targetVal) || !Base64.isBase64(value))
			return false;

		ValueOperatorType opt = ValueOperatorType.textToValue(op);
		byte[] target = Base64.decodeBase64(targetVal);
		byte[] v = Base64.decodeBase64(value);
		if (target == null || v == null) // not comparable
			return false;

		int result = 0;
		for (int i=0; i<target.length && i<v.length; i++)
			if (v[i] > target[i]) {
				result = 1;
				break;
			} else if (v[i] < target[i]) {
				result = -1;
				break;
			}
		
		if (result == 0) {
			if (v.length > target.length)
				result = 1;
			else if (v.length < target.length)
				result = -1;
		}

		if (opt == ValueOperatorType.EQUAL_TO)
			return result == 0;
		else if (opt == ValueOperatorType.NOT_EQUAL_TO)
			return result != 0;
		else if (opt == ValueOperatorType.GREATER_THAN)
			return result ==1;
		else if (opt == ValueOperatorType.GREATER_THAN_EQUAL_TO)
			return result >= 0;
		else if (opt == ValueOperatorType.LESS_THAN)
			return result == -1;
		else if (opt == ValueOperatorType.LESS_THEN_EQUAL_TO)
			return result <= 0;
		
		return false;
	}

	private boolean checkDateTimeCondition(String op, String targetVal, String value) {
		ValueOperatorType opt = ValueOperatorType.textToValue(op);
		try {
			Date td = DatatypeConverter.parseDateTime(targetVal).getTime();
			Date vd = DatatypeConverter.parseDateTime(value).getTime();
			int result = vd.compareTo(td);

			if (opt == ValueOperatorType.EQUAL_TO)
				return result == 0;
			else if (opt == ValueOperatorType.NOT_EQUAL_TO)
				return result != 0;
			else if (opt == ValueOperatorType.GREATER_THAN)
				return result > 0;
			else if (opt == ValueOperatorType.GREATER_THAN_EQUAL_TO)
				return result >= 0;
			else if (opt == ValueOperatorType.LESS_THAN)
				return result < 0;
			else if (opt == ValueOperatorType.LESS_THEN_EQUAL_TO)
				return result <= 0;			
		} catch (IllegalArgumentException ex) {
			log.warn("illegal datetime format target=" + targetVal+" value="+value);
			return false;
		}
		
		return false;
	}

	private boolean satisfyCondition(ValueOutOfBoundDetail voobDetail, String value) {
		if (voobDetail == null || value == null)
			return false;
		
		String valType = voobDetail.getXpathObject().getValueType();
		String op = voobDetail.getKey().getOperator();
		String targetVal = voobDetail.getTargetValue();
		
		if (!StringUtil.stringHasValue(valType) || !StringUtil.stringHasValue(op) || !StringUtil.stringHasValue(targetVal)) {
			log.warn("VOOB rule details not valid. RuleId = " + voobDetail.getKey().getRuleId());
			return false;
		}
		
		if ("string".equalsIgnoreCase(valType) || 
			"alphaNumericRestrictedString".equalsIgnoreCase(valType) || 
			"GUID".equalsIgnoreCase(valType) ||
			"QName".equalsIgnoreCase(valType) || 
			"anyURI".equalsIgnoreCase(valType) || 
			"voltageUnits".equalsIgnoreCase(valType) || 
			"ID".equalsIgnoreCase(valType) ||
			"action".equalsIgnoreCase(valType) || // v3 New Change Delete Replace Link Unlink
			"uom".equalsIgnoreCase(valType) || // v3
			"imageType".equalsIgnoreCase(valType) // v3
			) {
			return checkStringCondition(op, targetVal, value);
		} else if ("double".equalsIgnoreCase(valType) || 
					"float".equalsIgnoreCase(valType) || 
					"decimal".equalsIgnoreCase(valType) ||
					"voltage".equalsIgnoreCase(valType) ||
					"valueFloat".equalsIgnoreCase(valType) || // restricted type from based float
					"elementsVoltage".equalsIgnoreCase(valType) // v3
					) {
			return checkDoubleCondition(op, targetVal, value);
		} else if ("long".equalsIgnoreCase(valType) || 
					"integer".equalsIgnoreCase(valType) || 
					"int".equalsIgnoreCase(valType) ||
					"positiveInteger".equalsIgnoreCase(valType) ||
					"monthNumber".equalsIgnoreCase(valType) || 
					"dayNumber".equalsIgnoreCase(valType) ||
					"unsignedInt".equalsIgnoreCase(valType) || // v3
					"nonNegativeInteger".equalsIgnoreCase(valType) // v3					
					){
			return checkLongCondition(op, targetVal, value);
		} else if ("boolean".equalsIgnoreCase(valType)) {
			return checkBooleanCondition(op, targetVal, value);
		} else if ("base64Binary".equals(valType) ||
					"base64Image".equalsIgnoreCase(valType) // v3
				) {
			return checkBase64BinaryCondition(op, targetVal, value);
		} else if ("date".equalsIgnoreCase(valType) || 
				"dateTime".equalsIgnoreCase(valType) || 
			//	"duration".equalsIgnoreCase(valType) || // need further handling
				"mspDateTime".equalsIgnoreCase(valType) // same as dateTime
				) {
			return checkDateTimeCondition(op, targetVal, value);			
		} else 
			log.warn("Unsupported type in VOOB details: " + valType + ". Consider adding support to it.");
		
		return false;
	}
	
	public void analyse(Packet p) {
		if (voobRulesByServiceCDandMsgName == null || voobRulesByServiceCDandMsgName.isEmpty()) {
			log.warn("There are no MultiSpeak Value Out Of Bound Rules defined!");
			return;
		}
		
		String src = p.getPacketPK().getSourceAddress();
		String dst = p.getPacketPK().getDestAddress();
		long timestamp = p.getPacketPK().getTimeStamp().getTime();
		
		// Keep track of the latest timestamp in packets
		if (timestamp > currentRunCutoffInMillis)
			currentRunCutoffInMillis = timestamp;
		
		if (timestamp <= this.lastRunCutoffInMillis) { // already covered - no need to check again to avoid duplicate
			return;
		}
		
		String version = p.getMspVersion();
		if (p.getTextValues() == null || p.getTextValues().get(Packet.MESSAGE_TYPE_KEY) == null || version == null) { // no message type, not applicable to this detector
			// flag a warning result? and return
			log.warn("There is no message type for packet between " + src + " and " + dst + " for version " + version);
			return;
		}

		String endpointName = p.getTextValues().get(Packet.ENDPOINT_NAME_KEY);
		String msgType = p.getTextValues().get(Packet.MESSAGE_TYPE_KEY);
		// Check for proper data in the message
		if (!StringUtil.stringHasValue(msgType)) 
			return;
		
		Map<String, List<DetectionRule>> voobRulesForEndpoint = null;
		List<DetectionRule> voobRulesForMsg = null;
		
		if (StringUtil.stringHasValue(endpointName) && !endpointName.equalsIgnoreCase("NULL")) { // "NULL" can be set by the parser if endpoint is not identifiable from the message. 
			String key = StringUtil.combineVersion(endpointName, version);
			voobRulesForEndpoint = voobRulesByServiceCDandMsgName.get(key);
			if (voobRulesForEndpoint == null || voobRulesForEndpoint.isEmpty())
				return;
			
			voobRulesForMsg = voobRulesForEndpoint.get(msgType);
		} else if (version.equalsIgnoreCase(MSPServiceOperationKey.SUPPORTED_VERSION_3)) { // work around for MS-3 case where endpoint code cannot be determined
			// Get the endpoints associated with dst on request, or src on response
			// Look up rules for endpoints then for msgType, until found the first one, to fill in voobRulesForMsg
			// Not 100% proof but should work for most cases: if two endpoints are assigned to the same IP and both have the same mesgType, the wrong set of rules can
			// be used. In that case there is no additional information to disambiguate the rules for the message.
			// Test it
			// TODO - 
			
			EndpointConfiguration ec = null;
			if (msgType.endsWith("Response")) // get source IP endpoints to match rules for response message
				ec = DAOUtil.getEndpointConfigurationDAO().getEndpointConfigurationByIP(src);
			else // get destination IP endpoints to match rules for request message
				ec = DAOUtil.getEndpointConfigurationDAO().getEndpointConfigurationByIP(dst);
			
			if (ec != null && MSPServiceOperationKey.SUPPORTED_VERSION_3.equalsIgnoreCase(ec.getVersion()) && ec.getEndpointCDs() != null) { // on for version 3 endpoints
				for (String ep : ec.getEndpointCDs()) { // check each endpoint for the IP for defined rules for the endpoint and message
					String key = StringUtil.combineVersion(ep, version);
					voobRulesForEndpoint = voobRulesByServiceCDandMsgName.get(key); // and rules for the endpoint?
					if (voobRulesForEndpoint == null || voobRulesForEndpoint.isEmpty())
						continue;
					
					voobRulesForMsg = voobRulesForEndpoint.get(msgType); // any rules for this message type under the endpoint?
					if (voobRulesForMsg == null || voobRulesForMsg.isEmpty())
						continue;
					else
						break; // got it
				}
			}		
		}
		
		if (voobRulesForMsg == null || voobRulesForMsg.isEmpty())
			return;

		String msg = null;
		try {
			msg = new String(p.getContent(), "UTF-8");
			if (!StringUtil.stringHasValue(msg))
				return;
			int idx = msg.indexOf("<SOAP");
			if (idx < 0)
				idx = msg.indexOf("<soap");
			if (idx < 0)
				idx = msg.indexOf("<Soap");
			if (idx > 0)
				msg = msg.substring(idx);
		} catch (UnsupportedEncodingException e1) {
			log.warn(e1.getMessage());
			return;
		} // assuming this is the SOAP message
		
		// Check for proper data in the message
		if (!StringUtil.stringHasValue(msg)) 
			return;
		
		// Construct the DOM from message
	    DocumentBuilder db = null;
	    Document doc = null;
		try {
			DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
			// prevent XXE
			factory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true); // disallows the use of DTD entities
			factory.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true); // 64k limit on entity expansion
			//To prevent XML parsers from accessing fileFEATURE_SECURE_PROCESSINGs in the file system, use the AccessController class.
			db = factory.newDocumentBuilder();
		    InputSource is = new InputSource();
		    is.setCharacterStream(new StringReader(msg));
			doc = db.parse(is);
		} catch (ParserConfigurationException e) {
			log.warn(e.getMessage());
			return;
		} catch (SAXException e) {
			log.warn(e.getMessage());
			return;
		} catch (IOException e) {
			log.warn(e.getMessage());
			return;
		}

		for (DetectionRule r : voobRulesForMsg) {
			System.out.println("\n\tProcessing rule # " + r.getId());
			List<ValueOutOfBoundDetail> voobDetails = r.getVoobDetails();
			// Ensure a valid VOOB with detailed conditions
			if (voobDetails == null || voobDetails.isEmpty()) {
				log.warn("VOOB Rule not well defined, id = " + r.getId());
				continue;
			}

			boolean hitRule = true; 
			StringBuffer suspeciousValues = new StringBuffer(); 
			for (ValueOutOfBoundDetail d : voobDetails) {
				Xpath xpathObj = d.getXpathObject();
				
				// Ensure VOOB detail has a valid xpath
				if (xpathObj == null) {
					log.fatal("VOOB Rule Xpath is not defined, id = " + d.getKey().getRuleId() + " xpathId = " + d.getKey().getxPathId());
					hitRule = false;
					break; // problem, no need to check other conditions
				}
				
				// Extract the xpath field value
				String value = parseXML4XpathValue(doc, xpathObj.getXpath());
				if (value == null || value.isEmpty()) {
					hitRule = false;
					break; // no value to match
				}
				
				if (satisfyCondition(d, value)) {
					suspeciousValues.append(" " + xpathObj.getFieldName() + "=" + value);
					continue; // check next condition
				} else {
					hitRule = false;
					break; // no need to check other conditions
				}
			}
			
			if (hitRule) {
				// log finding
			    Alert alert = createAlert("Message from " + src + " to " + dst + " of type " + msgType
			            + " violates Value Out of Bound rule #" + r.getId() + " with suspecious values: "
			            + suspeciousValues.toString(), AnalyzerResultStatusType.OPEN,
			            DetectionRuleType.VALUE_OUT_OF_BOUND.toString(), r.getId(), nowInMillis, src, dst,
						p.getPacketPK().getTimeStamp());
				this.alerts.add(alert);
			}
		}
	}
	
    private Alert createAlert(String description, AnalyzerResultStatusType status, String ruleType, Integer refRuleId,
            Long runTime, String sourceIpAddress, String destinationIpAddress, Timestamp timestamp) {
        Alert al = new Alert();
        al.setDescription(description);
        al.setStatus(status);
        al.setAlertTypeId(1);
        al.setCreationTime(new Date());
        
        AnalyzerResult ar = new AnalyzerResult();
		ar.setTimeStamp(timestamp);
        ar.setDetectorType(ruleType);
        ar.setRefRuleId(refRuleId);
        ar.setRunTime(runTime);
        ar.setSrcIPAddress(sourceIpAddress);
        ar.setDstIPAddress(destinationIpAddress);

        al.setAnalyzerResult(ar);
        
        return al;
    }
	
	public String parseXML4XpathValue(Document doc, String xpathString) {
		if (doc == null || xpathString == null)
			return null;

		try {
			XPathFactory xPathfactory = XPathFactory.newInstance();
			XPath xpath = xPathfactory.newXPath();
			XPathExpression msgPath = xpath.compile(xpathString);
			Node msg = (Node) msgPath.evaluate(doc, XPathConstants.NODE);
			//NodeList msgs = (NodeList) msgPath.evaluate(doc, XPathConstants.NODESET);
			//System.out.println("Two ways for xpath: " + xpathString);
			System.out.println("One node content = " + msg.getTextContent() + "\tOne node value = " + msg.getNodeValue());
			/* TODO - will support array in the future
			for (int i=0; i<msgs.getLength(); i++) {
				System.out.println(i + "-text=" + msgs.item(i).getTextContent() + "\t" + i + "-value=" + msgs.item(i).getNodeValue());
			}
			*/
			return msg.getTextContent();
			//return msg.getNodeValue();
		} catch (Exception e) {
			log.error(e.getMessage());
		}
		return null;
	}

	public void done() {
		
		if (alerts == null || alerts.isEmpty())
			return;

		AlertDAO dao = DAOUtil.getAlertDAO();
		
		for (int i=0; i<alerts.size(); i++) {
			dao.addAlert(alerts.get(i));
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
