/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.services;

import com.essence.model.*;
import com.essence.persistence.*;


import org.apache.log4j.LogManager;
import org.apache.log4j.Logger;
import org.glassfish.jersey.server.ContainerRequest;

import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import java.sql.SQLException;
import java.text.ParseException;
import java.util.*;

@Path("anomaly")
public class AnomalyResource {
    private Logger logger = LogManager.getLogger(AnomalyResource.class.getName());
    
    @POST
    @Consumes({ MediaType.APPLICATION_JSON })
    @Produces(MediaType.TEXT_HTML)
    public Response newAnomaly(@Context ContainerRequest request, NewAnomaly a){
        OrganizationDAO pd = DAOUtil.getOrganizationDAO();
        List<OrganizationProfile> os = pd.getAllActiveOrganizations();
        assert(os != null && !os.isEmpty());

        Anomaly anomaly = new Anomaly();
        anomaly.setAlgorithm(a.getAlgorithm());
        anomaly.setDetectionTimeWindowEnd(a.getDetectionTimeWindowEnd());
        anomaly.setDetectionTimeWindowStart(a.getDetectionTimeWindowStart());
        anomaly.setTrainingTimeWindowEnd(a.getTrainingTimeWindowEnd());
        anomaly.setTrainingTimeWindowStart(a.getTrainingTimeWindowStart());
        if (a.getPatternIndex() != null && a.getPatternIndex().size() > 0) {
            anomaly.setPatternIndex(new HashSet<>(a.getPatternIndex()));
        }
        if (a.getPredictions() != null && a.getPredictions().size() > 0) {
            anomaly.setPredictions(new HashSet<>(a.getPredictions()));

            for (AnomalyPrediction p : anomaly.getPredictions()) {
                p.setAnomaly(anomaly);
            }
        }
//        if (a.getPredictedCauses() != null && a.getPredictedCauses().size() > 0) {
//            anomaly.setPredictedCauses(new HashSet<Cause>(a.getPredictedCauses()));
//        }
//        if (a.getPredictedStates() != null && a.getPredictedStates().size() > 0) {
//            anomaly.setPredictedStates(new HashSet<AnomalyState>(a.getPredictedStates()));
//        }
        anomaly.setScore(a.getScore());
        anomaly.setSourceType(a.getSourceType());
        anomaly.setSourceValue(a.getSourceValue());
        anomaly.setTargetType(a.getTargetType());

        anomaly.setNormalEntries(new HashSet<AnomalyNormalEntry>());
        for (NewAnomalyNormalEntry e : a.getNormalEntries()) {
            AnomalyNormalEntry n = new AnomalyNormalEntry();
            n.setMaxCount(e.getMaxCount());
            n.setMeanCount(e.getMeanCount());
            n.setMinCount(e.getMinCount());
            n.setStandardDeviation(e.getStandardDeviation());
            n.setSequenceNumber(e.getSequenceNumber());
            n.setTargetValue(e.getTargetValue());
            n.setAnomaly(anomaly);
            anomaly.getNormalEntries().add(n);
        }

        anomaly.setAnomalyEntries(new HashSet<AnomalyAnomalyEntry>());
        for (NewAnomalyAnomalyEntry e : a.getAnomalyEntries()) {
            AnomalyAnomalyEntry n = new AnomalyAnomalyEntry();
            n.setCount(e.getCount());
            n.setSequenceNumber(e.getSequenceNumber());
            n.setTargetValue(e.getTargetValue());
            n.setAnomaly(anomaly);
            anomaly.getAnomalyEntries().add(n);
        }

        Alert alert = new Alert();
        alert.setAlertTypeId(2);
        alert.setAnomaly(anomaly);
        alert.setCreationTime(new Date());
        alert.setOrganizationId(os.get(0).getId());
        alert.setStatus(AnalyzerResultStatusType.OPEN);
        
        AnomalyDAO aDao = DAOUtil.getAnomalyDAO();
        List<AnomalyTargetType> types = aDao.getTargetTypes();
        String sourceType = "";
        String targetType = "";
        for (AnomalyTargetType t : types) {
            if (t.getId() == anomaly.getSourceType()) {
                sourceType = t.getName();
            }
            if (t.getId() == anomaly.getTargetType()) {
                targetType = t.getName();
            }
        }
        
        String description = "Possibly anomalous data with source type " + sourceType + " and target type " + targetType;
        alert.setDescription(description);

        AlertDAO dao = DAOUtil.getAlertDAO();
        try {
            long id = dao.addAlert(alert);
            String url = request.getUriInfo().getRequestUri().toASCIIString();

            // TODO: redo response to show alert URL
            return Response.status(Response.Status.CREATED)// 201
                    .entity("A new anomaly and alert have been created")
                    .header("Location", url + "/" + String.valueOf(id)).build();
        } catch (Exception ex) {
            // TODO: error handling
            logger.error("Error saving anomaly", ex);
            return Response.serverError().build();
            //return "Failure";
        }
    }

    @GET
    @Produces({ MediaType.APPLICATION_JSON })
    @Path("states")
    public List<AnomalyState> getStates(
            @QueryParam("trainingTimeWindowStart") long trainingTimeWindowStart,
            @QueryParam("trainingTimeWindowEnd") long trainingTimeWindowEnd,
            @QueryParam("sourceType") int sourceType,
            @QueryParam("targetType") int targetType,
            @QueryParam("algorithm") String algorithm) {
        //Date trainingStart = trainingTimeWindowStart > 0 ? new Date(trainingTimeWindowStart) : null;
        //Date trainingEnd = trainingTimeWindowEnd > 0 ? new Date(trainingTimeWindowEnd) : null;
        
        //AlertDAO dao = DAOUtil.getAlertDAO();
        //List<AnomalyState> list = dao.getAnomalyStates(trainingStart, trainingEnd, sourceType, targetType, algorithm);

        // Changed to return all anomaly states per Terrence's request.
        AnomalyDAO dao = DAOUtil.getAnomalyDAO();
        return dao.getAnomalyStates();
    }
    
    @GET
    @Produces({ MediaType.APPLICATION_JSON })
    @Path("causes")
    public List<Cause> getCauses(
            @QueryParam("trainingTimeWindowStart") long trainingTimeWindowStart,
            @QueryParam("trainingTimeWindowEnd") long trainingTimeWindowEnd,
            @QueryParam("sourceType") int sourceType,
            @QueryParam("targetType") int targetType,
            @QueryParam("algorithm") String algorithm) {
        //Date trainingStart = trainingTimeWindowStart > 0 ? new Date(trainingTimeWindowStart) : null;
        //Date trainingEnd = trainingTimeWindowEnd > 0 ? new Date(trainingTimeWindowEnd) : null;
        
        //AlertDAO dao = DAOUtil.getAlertDAO();
        //List<Cause> list = dao.getCauses(trainingStart, trainingEnd, sourceType, targetType, algorithm);

        // Changed to return all anomaly states per Terrence's request.
        AnomalyDAO dao = DAOUtil.getAnomalyDAO();
        return dao.getCauses();
    }

    @GET
    @Produces({ MediaType.APPLICATION_JSON })
    @Path("query")
    public List<AnomalyResult> getAlerts(@QueryParam("detectionTimeWindowStart") long detectionTimeWindowStart,
                                         @QueryParam("detectionTimeWindowEnd") long detectionTimeWindowEnd,
                                         @QueryParam("trainingTimeWindowStart") long trainingTimeWindowStart,
                                         @QueryParam("trainingTimeWindowEnd") long trainingTimeWindowEnd,
                                         @QueryParam("sourceValue") String sourceValue,
                                         @QueryParam("targetType") int targetType,
                                         @QueryParam("algorithm") String algorithm,
                                         @QueryParam("userState") int userState,
                                         @QueryParam("userCause") int userCause)
            throws SQLException, ParseException {
        AlertDAO dao = DAOUtil.getAlertDAO();

        Date detectionStart = detectionTimeWindowStart > 0 ? new Date(detectionTimeWindowStart) : null;
        Date detectionEnd = detectionTimeWindowEnd > 0 ? new Date(detectionTimeWindowEnd) : null;
        Date trainingStart = trainingTimeWindowStart > 0 ? new Date(trainingTimeWindowStart) : null;
        Date trainingEnd = trainingTimeWindowEnd > 0 ? new Date(trainingTimeWindowEnd) : null;

        List<Alert> list = dao.getAlertsByAnomalyCriteria(detectionStart, detectionEnd,
                trainingStart, trainingEnd, sourceValue, targetType, algorithm);

        HashMap<Long, AnomalyResult> resultMap = new HashMap<>();
        for (Alert a : list) {
            Anomaly an = a.getAnomaly();
            AnomalyResult ar = new AnomalyResult();
            ar.setAlertId(a.getId());
            ar.setDetectionTimeWindowStart(an.getDetectionTimeWindowStart());
            ar.setDetectionTimeWindowEnd(an.getDetectionTimeWindowEnd());
            ar.setTrainingTimeWindowStart(an.getTrainingTimeWindowStart());
            ar.setTrainingTimeWindowEnd(an.getTrainingTimeWindowEnd());
            ar.setSourceValue(an.getSourceValue());
            ar.setTargetType(an.getTargetType());
            ar.setAlgorithm(an.getAlgorithm());
            ar.setScore(an.getScore());
            ar.setPatternIndex(new ArrayList<>(an.getPatternIndex()));

            // TODO: Get Cause and State from decision

            List<NewAnomalyAnomalyEntry> anomalyEntries = new ArrayList<>();
            for (AnomalyAnomalyEntry ane : an.getAnomalyEntries()) {
                NewAnomalyAnomalyEntry newAne = new NewAnomalyAnomalyEntry();
                newAne.setCount(ane.getCount());
                newAne.setSequenceNumber(ane.getSequenceNumber());
                newAne.setTargetValue(ane.getTargetValue());
                anomalyEntries.add(newAne);
            }
            ar.setAnomalyEntries(anomalyEntries);

            //result.add(ar);
            resultMap.put(a.getId(), ar);
        }

        if (resultMap.size() > 0) {
            // Get decisions
            DecisionDAO decisionDao = DAOUtil.getDecisionDAO();
            Long[] ids = new Long[resultMap.size()];
            resultMap.keySet().toArray(ids);
            List<Decision> decisions = decisionDao.getDecisionsByAlertIds(Arrays.asList(ids));
    
            if (userCause > 0 || userState > 0) {
                // Only return anomalies that have decisions and match the state and/or cause
                List<AnomalyResult> resultsWithDecision = new ArrayList<>();
    
                for (Decision decision : decisions) {
                    AnomalyResult r = resultMap.get(decision.getIssueId());
    
                    r.setUserCause(decision.getCause());
                    r.setUserState(decision.getAnomalyState());
    
                    if (userCause > 0 && decision.getCause().getId() != userCause) {
                        continue;
                    }
                    if (userState > 0 && decision.getAnomalyState().getId() != userState) {
                        continue;
                    }
                    resultsWithDecision.add(r);
                }
    
                return resultsWithDecision;
            }
            else {
                List<AnomalyResult> result = new ArrayList<>();

                for (Decision decision : decisions) {
                    if (decision.getCause() != null && decision.getAnomalyState() != null) {
                        AnomalyResult r = resultMap.get(decision.getIssueId());

                        r.setUserCause(decision.getCause());
                        r.setUserState(decision.getAnomalyState());
                        result.add(r);
                    }
                }

                return result;
            }
        }

        // Method modified to only return results that have a user cause an a user state
        return new ArrayList();
        //return result;
    }

    @GET
    @Produces(MediaType.TEXT_HTML)
    @Path("/state")
    public Response setState(
            @QueryParam("anomalyId") long anomalyId,
            @QueryParam("stateId") long stateId) {
        try {
        AlertDAO alertDao = DAOUtil.getAlertDAO();
        Alert alert = alertDao.getAlertByAnomalyId(anomalyId);
        DecisionDAO dao = DAOUtil.getDecisionDAO();
        AnomalyState state = new AnomalyState();
        state.setId(stateId);
        dao.setState(alert.getId(), state);
        

        return Response.status(Response.Status.OK)// 201
                .entity("Anomaly state set").build();
        }
        catch (Exception ex) {
            System.out.println(ex);
        }
        return null;
    }

    @GET
    @Produces(MediaType.TEXT_HTML)
    @Path("/cause")
    public Response setCause(
            @QueryParam("anomalyId") long anomalyId,
            @QueryParam("causeId") long causeId,
            @QueryParam("cause") String cause) {
        AlertDAO alertDao = DAOUtil.getAlertDAO();
        Alert alert = alertDao.getAlertByAnomalyId(anomalyId);
        DecisionDAO dao = DAOUtil.getDecisionDAO();
        Cause causeModel = new Cause();
        causeModel.setId(causeId);
        causeModel.setCause(cause);
        dao.setCause(alert.getId(), causeModel);
        

        return Response.status(Response.Status.OK)// 201
                .entity("Anomaly cause set").build();
    }

    @GET
    @Produces(MediaType.TEXT_HTML)
    @Path("/confirm")
    public Response confirmAnomaly() {
        AlertDAO dao = DAOUtil.getAlertDAO();
        List<Alert> alerts = dao.getAllActiveAlerts();
        
        for (Alert a : alerts) {
            if (a.getAnomaly() != null) {
                DecisionDAO dDao = DAOUtil.getDecisionDAO();

                if (a.getAnomaly().getPredictions() != null && a.getAnomaly().getPredictions().size() > 0) {
                    AnomalyPrediction[] predictions = new AnomalyPrediction[a.getAnomaly().getPredictions().size()];
                    dDao.setCause(a.getId(), a.getAnomaly().getPredictions().toArray(predictions)[0].getCause());
                    dDao.setState(a.getId(), a.getAnomaly().getPredictions().toArray(predictions)[0].getState());

                    // Set alert to pending
                    dao.updateStatus(a, AnalyzerResultStatusType.PENDING);
                }

//                if (a.getAnomaly().getPredictedCauses().size() > 0) {
//                    dDao.setCause(a.getId(), (Cause)a.getAnomaly().getPredictedCauses().toArray()[0]);
//                }
//
//                if (a.getAnomaly().getPredictedStates().size() > 0) {
//                    dDao.setState(a.getId(), (AnomalyState)a.getAnomaly().getPredictedStates().toArray()[0]);
//                }
            }
        }
        
        return Response.status(Response.Status.OK)// 201
                .entity("Anomaly states and causes confirmed").build();
    }
    
    @GET
    @Produces(MediaType.TEXT_HTML)
    @Path("/confirm/{anomalyId}")
    public Response confirmAnomaly(@PathParam("anomalyId") long anomalyId) {
        AlertDAO dao = DAOUtil.getAlertDAO();
        Alert a = dao.getAlertByAnomalyId(anomalyId);
        
        if (a != null && a.getAnomaly() != null) {
            DecisionDAO dDao = DAOUtil.getDecisionDAO();

            if (a.getAnomaly().getPredictions() != null && a.getAnomaly().getPredictions().size() > 0) {
                AnomalyPrediction[] predictions = new AnomalyPrediction[a.getAnomaly().getPredictions().size()];
                dDao.setCause(a.getId(), a.getAnomaly().getPredictions().toArray(predictions)[0].getCause());
                dDao.setState(a.getId(), a.getAnomaly().getPredictions().toArray(predictions)[0].getState());
            }

//            if (a.getAnomaly().getPredictedCauses().size() > 0) {
//                dDao.setCause(a.getId(), (Cause)a.getAnomaly().getPredictedCauses().toArray()[0]);
//            }
//
//            if (a.getAnomaly().getPredictedStates().size() > 0) {
//                dDao.setState(a.getId(), (AnomalyState)a.getAnomaly().getPredictedStates().toArray()[0]);
//            }
        }
        else {
            return Response.status(Response.Status.OK)// 201
                    .entity("Anomaly doesn't exist").build();
        }
        
        return Response.status(Response.Status.OK)// 201
                .entity("Anomaly state and cause confirmed").build();
    }
}
