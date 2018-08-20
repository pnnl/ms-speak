/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
 package com.essence.ui.server;

import java.io.PrintWriter;
import java.io.StringWriter;
import java.util.*;

import javax.servlet.http.HttpServletRequest;

import com.essence.action.ActionEngine;
import com.essence.action.Device;
import com.essence.action.SDNControllerNBI;
import com.essence.analysis.DoSDetector;
import com.essence.analysis.MSPConnectivityDetector;
import com.essence.analysis.Packet;
import com.essence.analysis.PacketAnalyserEngine;
import com.essence.analysis.PacketAnalyzer;
import com.essence.decision.DecisionEngine;
import com.essence.model.*;
import com.essence.multispeak.MSPServiceOperationKey;
import com.essence.persistence.*;
import com.essence.policy.*;
import com.essence.ui.client.GreetingService;
import com.essence.ui.client.object.*;
import com.essence.ui.shared.FieldVerifier;
import com.essence.ui.shared.Validator;
import com.google.gwt.user.server.rpc.RemoteServiceServlet;

/**
 * The server side implementation of the RPC service.
 * 
 * Policy entity is not exposed through the service. This implementation automatically retrieve the active policy and apply to all detectionRule APIs
 */
@SuppressWarnings("serial")
public class GreetingServiceImpl extends RemoteServiceServlet implements
    GreetingService {
    public static void main(String[] args) {
        GreetingServiceImpl impl = new GreetingServiceImpl();
	  /*
	  List<DetectionRule> rules = impl.getDetectionRules();
	  for (int i=0; i<rules.size(); i++)
		  rules.get(i).print();
		  */
        EndpointConfigurationDTO ec = new EndpointConfigurationDTO();
        EndpointConfigurationKeyDTO key = new EndpointConfigurationKeyDTO();
        key.setHostIPAddress("192.168.1.2");
        key.setOrganizationId(1);
        ec.setKey(key);
        ec.setHostName("h2");
        ec.setEndpointList("OA,WO,WR");
        impl.addEndpointConfiguration(ec);

        List<EndpointConfigurationDTO> ecs = impl.getEndpointConfigurations();
        for (int i=0; i<ecs.size(); i++)
            ecs.get(i).print();
    }

    public String greetServer(String input) throws IllegalArgumentException {
        // Verify that the input is valid.
        if (!FieldVerifier.isValidName(input)) {
          // If the input is not valid, throw an IllegalArgumentException back to
          // the client.
          throw new IllegalArgumentException(
              "Name must be at least 4 characters long");
        }

        String serverInfo = getServletContext().getServerInfo();
        String userAgent = getThreadLocalRequest().getHeader("User-Agent");

        String name = input.substring(0, (input.length()>20?20:input.length()));
        String sym = input.substring(0, (input.length()>4?4:input.length()));

        // Escape data from the client to avoid cross-site script vulnerabilities.
        input = escapeHtml(input);
        userAgent = escapeHtml(userAgent);

        return "";
    }

    @Override
    public String getSetting(String settingName) {
        SettingDAO dao = DAOUtil.getSettingDAO();
        Setting setting =  dao.getSetting(settingName);
        if (setting != null) {
            return setting.getValue();
        }
        return null;
    }

    @Override
    public String updateSetting(String settingName, String value) {
        SettingDAO dao = DAOUtil.getSettingDAO();
        dao.updateSetting(settingName, value);
        return "Success";
    }
  
    public DetectionRuleDTO getDetectionRuleByID(int id) {
        DetectionRuleDAO dao = DAOUtil.getDetectionRuleDAO();
        DetectionRule rule = dao.getDetectionRuleById(id);
        return rule != null ? createDetectionRuleDTO(rule) : null;
    }

    public List<DetectionRuleDTO> getDetectionRules() {
      List<DetectionRule> rules = DAOUtil.getDetectionRuleDAO().getAllActiveDetectionRules();
      List<DetectionRuleDTO> dtos = new ArrayList<>();
      for (DetectionRule r : rules) {
          DetectionRuleDTO d = createDetectionRuleDTO(r);
          dtos.add(d);
      }
    //	  System.out.println("Get detection rules, size = " + rules.size());

      return dtos;
    }
  
    public List<OrganizationProfileDTO> getAllOrganizations() {
      List<OrganizationProfile> os = DAOUtil.getOrganizationDAO().getAllOrganizations();
      List<OrganizationProfileDTO> dtos = new ArrayList<>();
      for (OrganizationProfile o : os) {
          dtos.add(createOrganizationProfileDTO(o));
      }

      return dtos;
    }

    private OrganizationProfileDTO createOrganizationProfileDTO(OrganizationProfile o) {
        OrganizationProfileDTO d = new OrganizationProfileDTO(o.getDescription(), o.isEnabled());
        d.setId(o.getId());
        return d;
    }

    public String activateOrganization(int id) {
	  try {
		  DAOUtil.getOrganizationDAO().activateOrganizationProfile(id);
		  return "Success";
	  } catch (Exception ex) {
		  return "Failure";
	  }
    }

    public List<DecisionDTO> getDecisions() {
      DecisionDAO dao = DAOUtil.getDecisionDAO();
      List<Decision> ds = dao.getAllDecisions();
      List<DecisionDTO> dtoList = new ArrayList<>();
      for (Decision d : ds) {
          DecisionDTO dto = createDecisionDTOWithoutCollections(d);
          dtoList.add(dto);
      }
      return dtoList;
    }
  
    public List<DecisionDTO> getDecisionsByType(DecisionTypeDTO type) {
      DecisionDAO dao = DAOUtil.getDecisionDAO();
      List<Decision> ds = dao.getDecisionsByType(toDecisionType(type));
      List<DecisionDTO> dtoList = new ArrayList<>();
      for (Decision d : ds) {
          DecisionDTO dto = createDecisionDTO(d);
          dtoList.add(dto);
      }
      return dtoList;
    }

    @Override
    public DecisionDTO getDecisionByAlert(long alertId) {
        DecisionDAO dao = DAOUtil.getDecisionDAO();
        Decision decision = dao.getDecisionByAlertId(alertId);
        if (decision != null) {
            return createDecisionDTO(decision);
        }
        return null;
    }

    public List<ActionDTO> getActions() {
	  ActionDAO dao = DAOUtil.getActionDAO();
	  List<Action> ds = dao.getAllActions();
	  List<ActionDTO> dtoList = new ArrayList<>();
	  for (Action a : ds) {
		  dtoList.add(createActionDTO(a));
	  }
	  return dtoList;
    }

    private static SeverityType toSeverityType(SeverityTypeDTO value) {
        return SeverityType.values()[value.ordinal()];
    }

    public List<AlertDTO> getAlerts(String alertFilterType) {
        AlertDAO dao = DAOUtil.getAlertDAO();
        List<AlertDTO> dtoList = new ArrayList<>();
        List<Alert> alerts = null;
        if (alertFilterType == null || alertFilterType.length() == 0) {
            alerts = dao.getAllActiveAlerts();
        }
        else {
            if (Objects.equals(alertFilterType, "Anomaly")) {
                alerts = dao.getAllAnomalyAlerts();
            }
            else {
                DetectionRuleType type = DetectionRuleType.valueOf(alertFilterType);
                if (type != null) {
                    alerts = dao.getActiveAlertsByType(type);
                }
            }
        }

        if (alerts != null) {
            for (Alert d : alerts) {
                AlertDTO dto = createAlertDTOWithoutCollections(d);
                dtoList.add(dto);
            }
        }
        return dtoList;
    }

    @Override
    public AlertDTO getAlert(long id) {
        AlertDAO dao = DAOUtil.getAlertDAO();
        Alert alert = dao.getAlertById(id);
        AlertDTO dto = createAlertDTO(alert);
        return dto;
    }

    public String setSeverityOnAlert(AlertDTO alert, SeverityTypeDTO type) {
        if (alert == null || alert.getId() == null)
            return "Failure";

        AlertDAO dao = DAOUtil.getAlertDAO();
        try {
            Alert a = createAlert(alert);
            dao.setSeverityOnAlert(a, toSeverityType(type));

            return "Success";
        } catch (Exception ex) {
            return "Failure";
        }
    }

    private Alert createAlert(AlertDTO d) {
        Anomaly anomaly = d.getAnomaly() != null ? createAnomaly(d.getAnomaly()) : null;
        AnalyzerResult analyzerResult = d.getAnalyzerResult() != null ? createAnalyzerResult(d.getAnalyzerResult())
                : null;

        return new Alert(d.getId(), d.getAlertTypeId(), d.getCreationTime(), d.getDescription(),
                d.getStatus(), d.getOrganizationId(), anomaly, analyzerResult, d.getSeverity());
    }

    private AnalyzerResult createAnalyzerResult(AnalyzerResultDTO result) {
        return  new AnalyzerResult(result.getRunTime(), result.getDetectorType(), result.getSrcIPAddress(),
                result.getDstIPAddress(), result.getNumberOfPacketsForDoS(), result.getTimeWindowInSeconds(),
                result.getRefRuleId());
    }

    private Anomaly createAnomaly(AnomalyDTO ad) {
        Set<AnomalyNormalEntry> ns = new HashSet<>();
        if (ad.getNormalEntries() != null) {
            for (AnomalyNormalEntryDTO ne : ad.getNormalEntries()) {
                ns.add(new AnomalyNormalEntry(ne.getId(), ne.getSequenceNumber(), ne.getTargetValue(),
                        ne.getMinCount(), ne.getMaxCount(), ne.getMeanCount(), ne.getStandardDeviation()));
            }
        }

        Set<AnomalyAnomalyEntry> as = new HashSet<>();
        if (ad.getAnomalyEntries() != null) {
            for (AnomalyAnomalyEntryDTO ae : ad.getAnomalyEntries()) {
                as.add(new AnomalyAnomalyEntry(ae.getId(), ae.getSequenceNumber(), ae.getTargetValue(),
                        ae.getCount()));
            }
        }

        Set<AnomalyPrediction> predictions = new HashSet<>();
        if (ad.getPredictions() != null) {
            for (AnomalyPredictionDTO d : ad.getPredictions()) {
                AnomalyPrediction prediction = new AnomalyPrediction();
                prediction.setId(d.getId());
                prediction.setScore(d.getScore());

                if (d.getCause() != null) {
                    Cause cause = new Cause();
                    cause.setId(d.getCause().getId());
                    cause.setCause(d.getCause().getCause());
                    prediction.setCause(cause);
                }

                if (d.getState() != null) {
                    AnomalyState state = new AnomalyState();
                    state.setId(d.getState().getId());
                    state.setState(d.getState().getState());
                    prediction.setState(state);
                }

                predictions.add(prediction);
            }
        }

//        Set<Cause> causes = new HashSet<>();
//        if (ad.getPredictedCauses() != null) {
//            for (CauseDTO c : ad.getPredictedCauses()) {
//                Cause cause = new Cause();
//                cause.setId(c.getId());
//                cause.setCause(c.getCause());
//                causes.add(cause);
//            }
//        }

//        Set<AnomalyState> states = new HashSet<>();
//        if (ad.getPredictedStates() != null) {
//            for (AnomalyStateDTO asd : ad.getPredictedStates()) {
//                AnomalyState state = new AnomalyState();
//                state.setId(asd.getId());
//                state.setState(asd.getState());
//                states.add(state);
//            }
//        }

        return new Anomaly(ad.getDetectionTimeWindowStart(),
                ad.getDetectionTimeWindowEnd(), ad.getTrainingTimeWindowStart(), ad.getTrainingTimeWindowEnd(),
                ad.getSourceType(), ad.getSourceValue(), ad.getTargetType(), ad.getScore(), ad.getAlgorithm(),
                ns, as, predictions, ad.getPatternIndex());
    }

    public String setCauseOnAlert(AlertDTO alert, CauseDTO cause) {
        if (alert == null || alert.getId() == null)
            return "Failure";

        if (alert.getAlertTypeId() != 2)
            return "Causes may only be assigned to Anomalies.";

        DecisionDAO decisionDao = DAOUtil.getDecisionDAO();
        try {
            decisionDao.setCause(alert.getId(), createCause(cause));
            // Alert should be set to pending
            AlertDAO alertDAO = DAOUtil.getAlertDAO();
            Alert a = createAlert(alert);
            alertDAO.updateStatus(a, AnalyzerResultStatusType.PENDING);
            return "Success";
        } catch (Exception ex) {
            return "Failure";
        }
    }

    private Cause createCause(CauseDTO cause) {
        Cause c = new Cause();
        c.setId(cause.getId());
        c.setCause(cause.getCause());
        return c;
    }

    @Override
    public String setAnomalyStateOnAlert(AlertDTO alert, AnomalyStateDTO state) {
        if (alert == null || alert.getId() == null)
            return "Failure";

        if (alert.getAlertTypeId() != 2)
            return "Anomaly state may only be assigned to Anomalies.";

        DecisionDAO decisionDao = DAOUtil.getDecisionDAO();
        try {
            decisionDao.setState(alert.getId(), createAnomalyState(state));
            // Alert should be set to pending
            AlertDAO alertDAO = DAOUtil.getAlertDAO();
            Alert a = createAlert(alert);
            alertDAO.updateStatus(a, AnalyzerResultStatusType.PENDING);
            return "Success";
        } catch (Exception ex) {
            return "Failure";
        }
    }

    private AnomalyState createAnomalyState(AnomalyStateDTO state) {
        AnomalyState s = new AnomalyState();
        s.setId(state.getId());
        s.setState(state.getState());
        return s;
    }

    @Override
    public List<AnomalyTargetTypeDTO> getAnomalyTargetTypes() {
        AnomalyDAO dao = DAOUtil.getAnomalyDAO();
        List<AnomalyTargetType> list =  dao.getTargetTypes();
        List<AnomalyTargetTypeDTO> dtos = new ArrayList<>();
        for (AnomalyTargetType t : list) {
            dtos.add(createAnomalyTargetTypeDTO(t));
        }
        return dtos;
    }

    @Override
    public List<AnomalyStateDTO> getAnomalyStates() {
        AnomalyDAO dao = DAOUtil.getAnomalyDAO();
        List<AnomalyState> list =  dao.getAnomalyStates();
        List<AnomalyStateDTO> dtos = new ArrayList<>();
        for (AnomalyState t : list) {
            dtos.add(createAnomalyStateDTO(t));
        }
        return dtos;
    }

    @Override
    public List<CauseDTO> getCauses() {
        AnomalyDAO dao = DAOUtil.getAnomalyDAO();
        List<Cause> list =  dao.getCauses();
        List<CauseDTO> dtos = new ArrayList<>();
        for (Cause t : list) {
            dtos.add(createCauseDTO(t));
        }
        return dtos;
    }

    private AnomalyTargetTypeDTO createAnomalyTargetTypeDTO(AnomalyTargetType t) {
        AnomalyTargetTypeDTO d = new AnomalyTargetTypeDTO();
        d.setId(t.getId());
        d.setName(t.getName());
        return d;
    }

    public String setActionTypeOnManualDecision(DecisionDTO decision, DecisionTypeDTO type) {
	  if (decision == null || decision.getId() <= 0)
		  return "Failure";
	  try {
		  AlertDAO alertDAO = DAOUtil.getAlertDAO();
		  Alert alert = alertDAO.getAlertById(decision.getIssueId());
          Decision d = createDecision(decision, alert);
          DAOUtil.getDecisionDAO().setActionTypeOnManualDecision(d, toDecisionType(type));
		  if (decision.getIssue() != null && 
				  decision.getIssue().getStatus().equals(AnalyzerResultStatusType.PENDING.toString())) {
		      DAOUtil.getAlertDAO().updateStatus(alert, AnalyzerResultStatusType.PROCESSED);
		  }
		  return "Success";
	  } catch (Exception ex) {
		  return "Failure";
	  }
  }

    private static DecisionType toDecisionType(DecisionTypeDTO value) {
        return DecisionType.values()[value.ordinal()];
    }

    private Decision createDecision(DecisionDTO decision, Alert alert) {
        Cause cause = decision.getCause() != null ? new Cause(decision.getCause().getCause()) : null;
        if (cause != null) {
            cause.setId(decision.getCause().getId());
        }

        Classification classification = decision.getClassification() != null ?
                new Classification(decision.getClassification().getClassification()) : null;
        if (classification != null) {
            classification.setId(decision.getClassification().getId());
        }
        
        AnomalyState state = decision.getAnomalyState() != null ?
                new AnomalyState() : null;
                if (state != null) {
                    state.setId(decision.getAnomalyState().getId());
                    state.setState(decision.getAnomalyState().getState());
                }
                
        return new Decision(decision.getId(), decision.getDecisionType(), decision.getSourceIPAddress(),
                      decision.getDestinationIPAddress(), decision.getMemo(), decision.getIssueId(),
                      decision.getDecisionRuleId(), decision.getStatus(), cause,
                      classification, decision.getDecisionTime(), decision.getUsername(), state, alert);
    }

    public List<DecisionRuleDTO> getDecisionRules() {
        DecisionRuleDAO dao = DAOUtil.getDecisionRuleDAO();
        List<DecisionRule> drs = dao.getAllDecisionRules();
        List<DecisionRuleDTO> dtos = new ArrayList<>();
        for (DecisionRule r : drs) {
            dtos.add(createDecisionRuleDTO(r));
        }
        return dtos;
    }

    private DecisionRuleDTO createDecisionRuleDTO(DecisionRule r) {
        CauseDTO cause = r.getCause() != null ? createCauseDTO(r.getCause()) : null;
        AnomalyStateDTO state = r.getState() != null ? createAnomalyStateDTO(r.getState()) : null;

        return new DecisionRuleDTO(r.getId(), r.getDetectionRuleType(), r.getDetectionRuleRef(), r.getSeverityType(),
                r.getDecisionType(), cause, state, r.getPriority());
    }

    public List<DecisionRuleDTO> getDecisionRulesByViolationType(DetectionRuleTypeDTO drt) {
        DecisionRuleDAO dao = DAOUtil.getDecisionRuleDAO();
        List<DecisionRule> drs = dao.getDecisionRulesByViolationType(toDetectionRuleType(drt));
        List<DecisionRuleDTO> dtos = new ArrayList<>();
        for (DecisionRule d : drs) {
            dtos.add(createDecisionRuleDTO(d));
        }
        return dtos;
    }

    static DetectionRuleType toDetectionRuleType(DetectionRuleTypeDTO value) {
        return DetectionRuleType.values()[value.ordinal()];
    }

    public String addDecisionRule(DecisionRuleDTO rule) {
        DecisionRuleDAO dao = DAOUtil.getDecisionRuleDAO();
        DecisionRule d = createDecisionRule(rule);

        try {
            dao.addDecisionRule(d);
            return "Success";
        }
        catch (Exception ex) {
            return "Failure";
        }
    }

    private DecisionRule createDecisionRule(DecisionRuleDTO r) {
        Cause cause = r.getCause() != null ? createCause(r.getCause()) : null;
        AnomalyState state = r.getState() != null ? createAnomalyState(r.getState()) : null;

        return new DecisionRule(r.getDetectionRuleType(), r.getDetectionRuleRef(), r.getSeverityType(),
                r.getDecisionType(), cause, state, r.getPriority());
    }

    public String removeDecisionRule(DecisionRuleDTO rule) {
	  DecisionRuleDAO dao = DAOUtil.getDecisionRuleDAO();
      DecisionRule d = new DecisionRule();
      d.setId(rule.getId());
	try {
		dao.removeDecisionRule(d);
		return "Success";
	} catch (Exception ex) {
		return "Failure";
	}
  }

    public String runAnalyzer(DetectionRuleTypeDTO drt) {
        PacketAnalyzer a = null;
        try {
            if (drt.equals(DetectionRuleType.DENIAL_OF_SERVICE))
                a = new DoSDetector();
            else if (drt.equals(DetectionRuleType.MS_EP_CONNECTIVITY))
                a = new MSPConnectivityDetector();
            a.activate();
            PacketDAO dao = CassandraDAOUtil.getPacketDAO();
            // TO-DO Need to improve the way to get packets based on time window
            // TO-DO Need to combine analysis into engine so not to retrieve all packets again and again
            List<Packet> packets = dao.getAllPackets();
            a.analyse(packets);
            a.done();

            return "Success";
        }
        catch (Exception ex) {
            return ex.toString() + "\n" + ex.getStackTrace();
            //return "Failure";
        }
    }

    public String runAnalyzer(Boolean continous) {
        try {
            PacketAnalyserEngine engine = PacketAnalyserEngine.getInstance();
            engine.setRunContinous(continous);
            engine.run();
            return "Success";
        } catch (Exception ex) {
            StringWriter stackTrace = new StringWriter();
            ex.printStackTrace(new PrintWriter(stackTrace));
            return ex.toString() + "\n" + stackTrace.toString();
            //return "Failure";
        }
    }

    public String runDecisionEngine() {
        try {
            DecisionEngine engine = new DecisionEngine();
            engine.runEnginesOnce();
            return "Success";
        } catch (Exception ex) {
            StringWriter stackTrace = new StringWriter();
            ex.printStackTrace(new PrintWriter(stackTrace));
            return ex.toString() + "\n" + stackTrace.toString();
            //return "Failure";
        }
    }

    public String setFirewall(Boolean on) {
        try {
            SDNControllerNBI api = DAOUtil.getSDNControllerNBI();
            if (on) { // to turn firewall on
                // Enable all switch to allow traffic first
                Map<String, List<String>> switcheClusters = api.getAllSwitches();
                Set<String> keys = switcheClusters.keySet();
                for (String key : keys) {
                    List<String> switches = switcheClusters.get(key);
                    for (int i = 0; i < switches.size(); i++) {
                        System.out.println("\tEnable traffic for switch " + switches.get(i) + ": " + api.enableFirewallTraffic4Switch(switches.get(i)));
                    }
                }
                // Then turn on the firewall
                api.enableFirewall(true);
            } else { // to turn firewall off
                // Then turn off the firewall
                api.enableFirewall(false);
                // Remove all rules
                api.deleteAllRules();
            }
            return "Success";
        } catch (Exception ex) {
            return "Failure";
        }
    }

    public Boolean isFirewallOn() {
        try {
            SDNControllerNBI api = DAOUtil.getSDNControllerNBI();
            return api.isFirewallOn();
        } catch (Exception ex) {
            return false;
        }
    }

    public String runActionEngine() {
        try {
            ActionEngine engine = new ActionEngine();
            engine.runEnginesOnce();
            return "Success";
        } catch (Exception ex) {
            return "Failure";
        }
    }

    public String addMSEndPointConnectivityRule(MultiSpeakEndPointConnectivityRule r) {
        // add active policy to rule
        OrganizationDAO pd = DAOUtil.getOrganizationDAO();
        List<OrganizationProfile> os = pd.getAllActiveOrganizations();
        assert (os != null && !os.isEmpty());
        r.setOrganizationId(os.get(0).getId());

        DetectionRuleDAO dao = DAOUtil.getDetectionRuleDAO();
        DetectionRuleDTO rule = r.getDetectionRule();
        DetectionRule dr = createDetectionRule(rule);
        try {
            dao.addDetectionRule(dr);
            return "Success";
        } catch (Exception ex) {
            return "Failure";
        }
    }

    private DetectionRule createDetectionRule(DetectionRuleDTO r) {
        List<ValueOutOfBoundDetail> list = new ArrayList<>();
        if (r.getVoobDetails() != null) {
            for (ValueOutOfBoundDetailDTO d  : r.getVoobDetails()) {
                VOOBKey key = new VOOBKey(d.getKey().getRuleId(), d.getKey().getxPathId(), d.getKey().getOperator());
                XpathDTO xpathDTO = d.getXpathObject();
                Xpath xpath = new Xpath(xpathDTO.getServiceCode(), xpathDTO.getVersion(), xpathDTO.getMessageName(),
                        xpathDTO.getXpath(), xpathDTO.getFieldName(), xpathDTO.getIsArray(), xpathDTO.getValueType());
    
                list.add(new ValueOutOfBoundDetail(key, d.getTargetValue(), d.getQualifiedFieldName(),
                        d.getXpath(), xpath));
            }
        }

        return new DetectionRule(r.getOrganizationId(), r.getRuleType(), r.getSrcEndpointType(), r.getDstEndpointType(),
                r.getVersion(), r.getActionType(), r.getSrcIPAddress(), r.getDstIPAddress(),
                r.getNumberOfPacketsForDoS(), r.getTimeWindowInSeconds(), r.getPriority(), r.getVoobTitle(),
                list, r.getPolicyDescription());
    }

    public String addValueOutOfBoundRule(DetectionRuleDTO rule, List<ValueOutOfBoundDetailDTO> details) {
        System.out.println("detection rule:");
        rule.print();
        System.out.println("detection rule details:");
        for (ValueOutOfBoundDetailDTO d : details)
            d.print();

        OrganizationDAO pd = DAOUtil.getOrganizationDAO();
        List<OrganizationProfile> os = pd.getAllActiveOrganizations();
        assert (os != null && !os.isEmpty());
        rule.setOrganizationId(os.get(0).getId());


        DetectionRuleDAO dao = DAOUtil.getDetectionRuleDAO();
        DetectionRule dr = createDetectionRule(rule);
        try {
            dao.addDetectionRule(dr);
            for (ValueOutOfBoundDetailDTO d : details) {
                d.getKey().setRuleId(dr.getId());
                ValueOutOfBoundDetail detail = createValueOutOfBoundDetail(d);
                dao.addValueOutOfBoundDetail(detail);
            }
            return "Success";
        } catch (Exception ex) {
            ex.printStackTrace();
            return "Failure";
        }
    }

    private ValueOutOfBoundDetail createValueOutOfBoundDetail(ValueOutOfBoundDetailDTO d) {
        VOOBKeyDTO keydto = d.getKey();
        VOOBKey key = new VOOBKey();
        if (keydto != null) {
            key.setOperator(keydto.getOperator());
            key.setRuleId(keydto.getRuleId());
            key.setxPathId(keydto.getxPathId());
        }
        Xpath xpath = null;
        if (d.getXpathObject() != null) {
            xpath = createXpath(d.getXpathObject());
        }

        return new ValueOutOfBoundDetail(key, d.getTargetValue(), d.getQualifiedFieldName(),
                d.getXpath(), xpath);
    }

    public Map<Integer, List<ValueOutOfBoundDetailDTO>> getValueOutOfBoundRuleDetails(List<Integer> ruleIds) {
        Map<Integer, List<ValueOutOfBoundDetail>> details =
                DAOUtil.getDetectionRuleDAO().getValueOutOfBoundRuleDetailsByRuleIds(ruleIds);
        // System.out.println("Get VOOB details, size = " + details.size());

        Map<Integer, List<ValueOutOfBoundDetailDTO>> dtos = new HashMap<>();
        Iterator it = details.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry pair = (Map.Entry) it.next();
            List<ValueOutOfBoundDetail> list = (List<ValueOutOfBoundDetail>) pair.getValue();
            List<ValueOutOfBoundDetailDTO> subDtos = new ArrayList<>();
            for (ValueOutOfBoundDetail detail : list) {
                subDtos.add(createValueOutOfBoundDetailDTO(detail));
            }
            dtos.put((Integer) pair.getKey(), subDtos);
        }
        return dtos;
    }

    public String addGeneralDetectionRule(DetectionRuleDTO r) {
        // add active policy to rule
        OrganizationDAO pd = DAOUtil.getOrganizationDAO();
        List<OrganizationProfile> os = pd.getAllActiveOrganizations();
        assert (os != null && !os.isEmpty());
        r.setOrganizationId(os.get(0).getId());

        DetectionRuleDAO dao = DAOUtil.getDetectionRuleDAO();
        DetectionRule rule = createDetectionRule(r);
        try {
            dao.addDetectionRule(rule);
            return "Success";
        } catch (Exception ex) {
            return "Failure";
        }
    }

    public String removeGeneralDetectionRule(DetectionRuleDTO r) {
        DetectionRuleDAO dao = DAOUtil.getDetectionRuleDAO();
        try {
            DetectionRule rule = new DetectionRule();
            rule.setId(r.getId());
            rule.setRuleType(r.getRuleType());
            dao.removeDetectionRule(rule);
            return "Success";
        }
        catch (Exception ex) {
            return "Failure";
        }
    }

    public List<EndpointConfigurationDTO> getEndpointConfigurations() {
        // retrieve the current host list
        EndpointConfigurationDAO dao = DAOUtil.getEndpointConfigurationDAO();
        List<EndpointConfiguration> ecs = dao.getAllActiveEndpointConfigurations();

        Map<String, EndpointConfiguration> ecsMap = new HashMap<String, EndpointConfiguration>();
        if (ecs != null)
            for (int i=0; i<ecs.size(); i++)
                ecsMap.put(ecs.get(i).getKey().getHostIPAddress(), ecs.get(i));

        // query SDN controller for the latest network hosts
        SDNControllerNBI api = DAOUtil.getSDNControllerNBI();
        List<Device> deviceList = api.getAllDevices(); // never null

        OrganizationDAO pd = DAOUtil.getOrganizationDAO();
        List<OrganizationProfile> os = pd.getAllActiveOrganizations();
        assert(os != null && !os.isEmpty());
        int activePolicyId = os.get(0).getId();

        // Add new hosts to the database
        boolean hasAddition = false;
        for (int i=0; i<deviceList.size(); i++) {
            if (deviceList.get(i).getIpv4() != null && !deviceList.get(i).getIpv4().isEmpty())
                if (!ecsMap.keySet().contains(deviceList.get(i).getIpv4().get(0))) { // IP not in DB yet, add it to the database
                    EndpointConfiguration epConfig = new EndpointConfiguration();

                    epConfig.getKey().setHostIPAddress(deviceList.get(i).getIpv4().get(0));
                    if (deviceList.get(i).getMac() != null && !deviceList.get(i).getMac().isEmpty())
                        epConfig.setHostName(deviceList.get(i).getMac().get(0));
                    epConfig.getKey().setOrganizationId(activePolicyId);
                    dao.addEndpointConfiguration(epConfig);
                    hasAddition = true;
                } else if (!ecsMap.get(deviceList.get(i).getIpv4().get(0)).getHostName().equals(deviceList.get(i).getMac().get(0))) { // update info for IP
                    EndpointConfiguration epConfig = ecsMap.get(deviceList.get(i).getIpv4().get(0));
                    epConfig.setHostName(deviceList.get(i).getMac().get(0));
                    System.out.println("IP=" + deviceList.get(i).getIpv4().get(0) + "\toldMac=" + ecsMap.get(deviceList.get(i).getIpv4().get(0)).getHostName() + "\tnewMac=" + deviceList.get(i).getMac().get(0));
                    dao.saveEndpointConfiguration(epConfig); //TO-DO: need to test
                }
        }

        if (hasAddition) // refresh the list
            ecs = dao.getAllActiveEndpointConfigurations(); // need to verify order by IP

        List<EndpointConfigurationDTO> dtos = new ArrayList<>();
        for (EndpointConfiguration e : ecs) {
            dtos.add(createEndpointConfiurationDTO(e));
        }

        return dtos;
    }

    @Override
    public EndpointConfigurationDTO getEndpointConfiguration(String ipAddress) {
        EndpointConfigurationDAO dao = DAOUtil.getEndpointConfigurationDAO();
        EndpointConfiguration ec = dao.getEndpointConfigurationByIP(ipAddress);
        if (ec != null) {
           return createEndpointConfiurationDTO(ec);
        }

        return null;
    }

    private EndpointConfigurationDTO createEndpointConfiurationDTO(EndpointConfiguration e) {
        EndpointConfigurationKeyDTO key = new EndpointConfigurationKeyDTO();
        if (e.getKey() != null) {
            key.setHostIPAddress(e.getKey().getHostIPAddress());
            key.setOrganizationId(e.getKey().getOrganizationId());
        }
        return new EndpointConfigurationDTO(key, e.getHostName(), e.getEndpointList(), e.getVersion());
    }

    public String addEndpointConfiguration(EndpointConfigurationDTO ec) {
        if (validateEndpointConfig(ec) == false)
            return "Failure";

        if (ec.getHostName() != null && ec.getHostName().length() > 40)
            ec.setHostName(ec.getHostName().substring(0, 40));

        // add active policy to rule
        OrganizationDAO pd = DAOUtil.getOrganizationDAO();
        List<OrganizationProfile> os = pd.getAllActiveOrganizations();
        assert(os != null && !os.isEmpty());
        ec.getKey().setOrganizationId(os.get(0).getId());

        EndpointConfigurationDAO dao = DAOUtil.getEndpointConfigurationDAO();
        EndpointConfiguration conf = createEndpointConfiuration(ec);
        try {
            dao.addEndpointConfiguration(conf);
            return "Success";
        } catch (Exception ex) {
            return "Failure";
        }
    }

    private EndpointConfiguration createEndpointConfiuration(EndpointConfigurationDTO e) {
        EndpointConfigurationKey key = new EndpointConfigurationKey();
        if (e.getKey() != null) {
            key.setOrganizationId(e.getKey().getOrganizationId());
            key.setHostIPAddress(e.getKey().getHostIPAddress());
        }
        EndpointConfiguration ec = new EndpointConfiguration(key, e.getHostName(), e.getEndpointList(),
                e.getVersion());
        return ec;
    }

    static private List<String> MSP_ENDPOINT_CODES = null;
    static private String MSP_VERSION = null;

    public List<String> getEndpointCodes(String version) {
        if (version == null)
            return null;

        if (MSP_ENDPOINT_CODES != null && version.equals(MSP_VERSION))
            return MSP_ENDPOINT_CODES;

        try {
            MSP_ENDPOINT_CODES = DAOUtil.getMSPServiceOperationDAO().getEndpointCodes(version);
            MSP_VERSION = version;
            return MSP_ENDPOINT_CODES;
        }
        catch (Exception ex) {
            return null;
        }
    }

    public List<String> getEndpointMessages(String epCode, String version) {
        try {
            return DAOUtil.getMSPServiceOperationDAO().getEndpointMessages(epCode, version);
        } catch (Exception ex) {
            return null;
        }
    }

    public List<XpathDTO> getXpathsByServiceCDMsgName(String cd, String version, String msgName, Boolean isArray) {
        try {
            System.out.println("*** Called to getXpathsByServiceCDMsgName cd=" + cd + " msgName=" + msgName + " isArray=" + isArray);
            List<Xpath> result = DAOUtil.getMSPXpathDAO().getXpathsByServiceCDMsgName(cd, version, msgName, isArray);
            System.out.println("*** result size = "+result.size());
              /*
              for (Xpath path : result) {// pre-processed the drop-down values
                  XpathDisplay d = new XpathDisplay();
                  d.setXpath(path);
                  d.setDisplayString(StringUtil.reverseXpath(path.getXpath().substring(Xpath.BODY_SIGNATURE_PATH.length()+path.getMessageName().length()+1))+": "+path.getValueType());
                  xpathDisplays.add(d);
              }
              */
            List<XpathDTO> dtos = new ArrayList<>();
            for (Xpath x :result) {
                dtos.add(createXpathDTO(x));
            }

            return dtos;
        }
        catch (Exception ex) {
            return null;
        }
  }

    public List<XpathDTO> getHeaderXpaths(Boolean isArray, String version) {
        try {
            List<Xpath> result = DAOUtil.getMSPXpathDAO().getHeaderXpaths(isArray, version);
            List<XpathDTO> dtos = new ArrayList<>();
            for (Xpath x :result) {
              dtos.add(createXpathDTO(x));
            }

            return dtos;
        }
        catch (Exception ex) {
            return null;
        }
    }

    private Xpath createXpath(XpathDTO x) {
        return new Xpath(x.getServiceCode(), x.getVersion(), x.getMessageName(), x.getXpath(),
                x.getFieldName(), x.getIsArray(), x.getValueType());
    }

    private boolean validateEndpointConfig(EndpointConfigurationDTO ec) {
        if (ec == null)
            return false;

        if (ec.getKey().getHostIPAddress() == null || ec.getKey().getHostIPAddress().isEmpty())
            return false;

        if (!Validator.validateIPAddress(ec.getKey().getHostIPAddress()))
            return false;

        if (ec.getHostName() != null && ec.getHostName().length() > 40) // can consider more restrictive validation
            return false;

        if (ec.getVersion() != null &&
              !ec.getVersion().equalsIgnoreCase(MSPServiceOperationKey.SUPPORTED_VERSION_3) &&
                      !ec.getVersion().equalsIgnoreCase(MSPServiceOperationKey.SUPPORTED_VERSION_5))
            return false;

        if (MSPServiceOperationKey.SUPPORTED_VERSION_3.equalsIgnoreCase(ec.getVersion())) {// check v3 endpoints
            String [] cds = ec.getEndpointCDs();
            for (String cd : cds)
                if (!EndpointConfiguration.isValidEndpointCode3(cd))
                    return false;
        }
        else if (MSPServiceOperationKey.SUPPORTED_VERSION_5.equalsIgnoreCase(ec.getVersion())) { // check v5 endpoints
            String [] cds = ec.getEndpointCDs();
            for (String cd : cds)
                if (!EndpointConfiguration.isValidEndpointCode5(cd))
                    return false;
        }
        else if (ec.getEndpointList() != null) // version should be empty, so the list should also be empty
            return false;

        return true;
    }

    public String saveEndpointConfiguration(EndpointConfigurationDTO ec) {
        if (validateEndpointConfig(ec) == false)
            return "Failure";

        if (ec.getHostName() != null && ec.getHostName().length() > 40)
            ec.setHostName(ec.getHostName().substring(0, 40));

        // add active policy to rule
        OrganizationDAO pd = DAOUtil.getOrganizationDAO();
        List<OrganizationProfile> os = pd.getAllActiveOrganizations();
        assert(os != null && !os.isEmpty());
        ec.getKey().setOrganizationId(os.get(0).getId());

        EndpointConfigurationDAO dao = DAOUtil.getEndpointConfigurationDAO();
        EndpointConfiguration conf = createEndpointConfiuration(ec);

        try {
            dao.saveEndpointConfiguration(conf);
            return "Success";
        }
        catch (Exception ex) {
            return "Failure";
        }
    }

    public String removeEndpointConfiguration(EndpointConfigurationDTO ec) {
        EndpointConfigurationDAO dao = DAOUtil.getEndpointConfigurationDAO();
        try {
            EndpointConfigurationKey key = new EndpointConfigurationKey();
            key.setHostIPAddress(ec.getKey().getHostIPAddress());
            key.setOrganizationId(ec.getKey().getOrganizationId());
            EndpointConfiguration conf = new EndpointConfiguration();
            conf.setKey(key);
            dao.removeEndpointConfiguration(conf);
            return "Success";
        }
        catch (Exception ex) {
            return "Failure";
        }
    }

    public String addName(String name) {
        try {
            HttpServletRequest request = this.getThreadLocalRequest();
            request.getSession().setAttribute("NAME", escapeHtml(name));
            return "Success";
        }
        catch (Exception ex) {
            return "Failure";
        }
    }

    public String getName() {
        try {
            HttpServletRequest request = this.getThreadLocalRequest();
            return (String)request.getSession().getAttribute("NAME");
        }
        catch (Exception ex) {
            return "Failure";
        }
    }

    public Integer deleteAllEngineRunLogs() {
        EngineRunLogDAO dao = DAOUtil.getEngineRunLogDAO();
        return dao.deleteAllEngineRunLogs();
    }

    public Integer deleteAllAlerts() {
        AlertDAO dao = DAOUtil.getAlertDAO();
        return dao.deleteAllAlerts();
    }

  /**
   * Escape an html string. Escaping data received from the client helps to
   * prevent cross-site script vulnerabilities.
   *
   * @param html the html string to escape
   * @return the escaped string
   */
    private String escapeHtml(String html) {
        if (html == null) {
            return null;
        }
        return html.replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(
            ">", "&gt;");
    }

    private ActionDTO createActionDTO(Action a) {
        return new ActionDTO(a.getId(), a.getDetail(), a.getDecisionId(), a.getTimestamp(),
			  createDecisionDTO(a.getDecision()));
    }

    private DecisionDTO createDecisionDTO(Decision d) {
        AlertDTO ad = d.getIssue() != null ? createAlertDTOWithoutCollections(d.getIssue()) : null;
        CauseDTO causeDTO = d.getCause() != null ? createCauseDTO(d.getCause()) : null;
        ClassificationDTO classificationDTO = d.getClassification() != null ?
              createClassificationDTO(d.getClassification()) : null;
        AnomalyStateDTO stateDTO = d.getAnomalyState() != null ?
              createAnomalyStateDTO(d.getAnomalyState()) : null;

        return new DecisionDTO(d.getId(), d.getDecisionType(), d.getSourceIPAddress(),
              d.getDestinationIPAddress(), d.getMemo(), d.getIssueId(), d.getDecisionRuleId(),
              d.getStatus(), causeDTO, classificationDTO, d.getDecisionTime(),
              d.getUsername(), stateDTO, ad);
    }

    private DecisionDTO createDecisionDTOWithoutCollections(Decision d) {
        AlertDTO ad = d.getIssue() != null ? createAlertDTOWithoutCollections(d.getIssue()) : null;
        CauseDTO causeDTO = d.getCause() != null ? createCauseDTO(d.getCause()) : null;
        ClassificationDTO classificationDTO = d.getClassification() != null ?
                createClassificationDTO(d.getClassification()) : null;
        AnomalyStateDTO stateDTO = d.getAnomalyState() != null ?
                createAnomalyStateDTO(d.getAnomalyState()) : null;

        return new DecisionDTO(d.getId(), d.getDecisionType(), d.getSourceIPAddress(),
                d.getDestinationIPAddress(), d.getMemo(), d.getIssueId(), d.getDecisionRuleId(),
                d.getStatus(), causeDTO, classificationDTO, d.getDecisionTime(),
                d.getUsername(), stateDTO, ad);
    }

    private AlertDTO createAlertDTOWithoutCollections(Alert a) {
        AnomalyDTO anomalyDTO = a.getAnomaly() != null ? createAnomalyDTOWithoutCollections(a.getAnomaly()) : null;
        AnalyzerResultDTO analyzerResultDTO = a.getAnalyzerResult() != null ?
              createAnalyzerResultDTO(a.getAnalyzerResult()) : null;

        return new AlertDTO(a.getId(), a.getAlertTypeId(), a.getCreationTime(), a.getDescription(),
              a.getStatus(), a.getOrganizationId(), anomalyDTO, analyzerResultDTO, a.getSeverity());
    }

    private AlertDTO createAlertDTO(Alert a) {
        AnomalyDTO anomalyDTO = a.getAnomaly() != null ? createAnomalyDTO(a.getAnomaly()) : null;
        AnalyzerResultDTO analyzerResultDTO = a.getAnalyzerResult() != null ?
			  createAnalyzerResultDTO(a.getAnalyzerResult()) : null;

        return  new AlertDTO(a.getId(), a.getAlertTypeId(), a.getCreationTime(), a.getDescription(),
              a.getStatus(), a.getOrganizationId(), anomalyDTO, analyzerResultDTO, a.getSeverity());
    }

	private AnalyzerResultDTO createAnalyzerResultDTO(AnalyzerResult a) {
		return new AnalyzerResultDTO(a.getId(), a.getRunTime(), a.getDetectorType(), a.getSrcIPAddress(),
                a.getDstIPAddress(), a.getNumberOfPacketsForDoS(), a.getTimeWindowInSeconds(), a.getRefRuleId(),
                a.getTimeStamp());
	}

    private AnomalyDTO createAnomalyDTOWithoutCollections(Anomaly a) {
        return new AnomalyDTO(a.getId(), a.getDetectionTimeWindowStart(),
                a.getDetectionTimeWindowEnd(), a.getTrainingTimeWindowStart(), a.getTrainingTimeWindowEnd(),
                a.getSourceType(), a.getSourceValue(), a.getTargetType(), a.getScore(), a.getAlgorithm(),
                null, null, null, null);
    }

	private AnomalyDTO createAnomalyDTO(Anomaly a) {
        Set<AnomalyAnomalyEntryDTO> aeList = new HashSet<>();
        Set<AnomalyNormalEntryDTO> neList = new HashSet<>();
        Set<AnomalyPredictionDTO> predictionList = new HashSet<>();
        Set<Integer> patternIndex = new HashSet<>();
        for (AnomalyAnomalyEntry ae : a.getAnomalyEntries()) {
            aeList.add(createAnomalyAnomalyEntryDTO(ae));
        }
        for (AnomalyNormalEntry ae : a.getNormalEntries()) {
            neList.add(createAnomalyNormalEntryDTO(ae));
        }
        for (AnomalyPrediction p : a.getPredictions()) {
            predictionList.add(createAnomalyPredictionDTO(p));
        }
        for (Integer p : a.getPatternIndex()) {
            patternIndex.add(p);
        }

        return new AnomalyDTO(a.getId(), a.getDetectionTimeWindowStart(),
              a.getDetectionTimeWindowEnd(), a.getTrainingTimeWindowStart(), a.getTrainingTimeWindowEnd(),
              a.getSourceType(), a.getSourceValue(), a.getTargetType(), a.getScore(), a.getAlgorithm(),
              patternIndex, neList, aeList, predictionList);
    }

    private AnomalyPredictionDTO createAnomalyPredictionDTO(AnomalyPrediction p) {
        CauseDTO cause = p.getCause() != null ? createCauseDTO(p.getCause()) : null;
        AnomalyStateDTO state = p.getState() != null ? createAnomalyStateDTO(p.getState()) : null;
        return new AnomalyPredictionDTO(p.getId(), state, cause, p.getScore());
    }

    private AnomalyAnomalyEntryDTO createAnomalyAnomalyEntryDTO(AnomalyAnomalyEntry a) {
      return new AnomalyAnomalyEntryDTO(a.getId(), a.getSequenceNumber(),
              a.getTargetValue(), a.getCount());
  }

    private AnomalyNormalEntryDTO createAnomalyNormalEntryDTO(AnomalyNormalEntry a) {
        return new AnomalyNormalEntryDTO(a.getId(), a.getSequenceNumber(),
              a.getTargetValue(), a.getMinCount(), a.getMaxCount(), a.getMeanCount(), a.getStandardDeviation());
    }

    private DetectionRuleDTO createDetectionRuleDTO(DetectionRule r) {
        List<ValueOutOfBoundDetailDTO> voobDetails = new ArrayList<>();
        if (r.getVoobDetails() != null) {
            for (ValueOutOfBoundDetail v : r.getVoobDetails()) {
                voobDetails.add(createValueOutOfBoundDetailDTO(v));
            }
        }

        return new DetectionRuleDTO(r.getId(), r.getOrganizationId(), r.getRuleType(), r.getSrcEndpointType(),
			  r.getDstEndpointType(), r.getVersion(), r.getActionType(), r.getSrcIPAddress(), r.getDstIPAddress(),
			  r.getNumberOfPacketsForDoS(), r.getTimeWindowInSeconds(), r.getPriority(), r.getVoobTitle(),
			  voobDetails, r.getPolicyDescription());
    }

	private ValueOutOfBoundDetailDTO createValueOutOfBoundDetailDTO(ValueOutOfBoundDetail v) {
		VOOBKeyDTO key = v.getKey() != null ? createVOOBKeyDTO(v.getKey()) : null;
		XpathDTO xpath = v.getXpathObject() != null ? createXpathDTO(v.getXpathObject()) : null;

		return new ValueOutOfBoundDetailDTO(key, v.getTargetValue(), v.getQualifiedFieldName(),
				v.getXpath(), xpath);
	}

	private VOOBKeyDTO createVOOBKeyDTO(VOOBKey k) {
		return new VOOBKeyDTO(k.getRuleId(), k.getxPathId(), k.getOperator());
	}

	private XpathDTO createXpathDTO(Xpath x) {
		return new XpathDTO(x.getId(), x.getServiceCode(), x.getVersion(), x.getMessageName(), x.getXpath(),
				x.getFieldName(), x.getIsArray(), x.getValueType());
	}

	private CauseDTO createCauseDTO(Cause c) {
		CauseDTO d = new CauseDTO();
		d.setCause(c.getCause());
		d.setId(c.getId());
		return d;
	}

	private AnomalyStateDTO createAnomalyStateDTO(AnomalyState s) {
		AnomalyStateDTO d = new AnomalyStateDTO();
		d.setId(s.getId());
		d.setState(s.getState());
		return d;
	}

    private ClassificationDTO createClassificationDTO(Classification c) {
        ClassificationDTO d = new ClassificationDTO();
        d.setId(c.getId());
        d.setClassification(c.getClassification());
        return d;
    }
}
