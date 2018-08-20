/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.services;

import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

//import org.apache.logging.log4j.Logger;
//import org.apache.logging.log4j.LogManager;
import com.essence.model.AnalyzerResult;
import com.essence.model.Anomaly;
import com.essence.services.dtos.AlertDTO;
import com.essence.services.dtos.AnalyzerResultDTO;
import com.essence.services.dtos.AnomalyDTO;
import org.glassfish.jersey.server.ContainerRequest;

import com.essence.model.Alert;
import com.essence.model.AlertClassification;
import com.essence.persistence.AlertDAO;
import com.essence.persistence.DAOUtil;
import com.essence.persistence.DecisionDAO;

@Path("alert")
public class AlertResource {
    org.apache.log4j.Logger log = org.apache.log4j.LogManager.getLogger(AlertResource.class);
    //Logger log = LogManager.getLogger(AlertResource.class);
    
    @GET    
    @Produces({ MediaType.APPLICATION_JSON })
    @Path("/ip/{ip}")
    public List<AlertDTO> getAlerts(@PathParam("ip") String ip) throws SQLException
    {
        AlertDAO dao = DAOUtil.getAlertDAO();
        List<Alert> list = dao.getAllActiveAlertsByIP(ip, false);
        List<AlertDTO> dtos = new ArrayList<>();
        for (Alert a : list) {
            AnomalyDTO anDTO = null;
            AnalyzerResultDTO arDTO = null;
            if (a.getAnomaly() != null) {
                Anomaly an = a.getAnomaly();
                anDTO = new AnomalyDTO(an.getId(), an.getDetectionTimeWindowStart(),an.getDetectionTimeWindowEnd(),
                        an.getTrainingTimeWindowStart(), an.getTrainingTimeWindowEnd(), an.getSourceType(),
                        an.getSourceValue(), an.getTargetType(), an.getScore(), an.getAlgorithm(), null,
                        null, null, null);
            }
            if (a.getAnalyzerResult() != null) {
                AnalyzerResult ar = a.getAnalyzerResult();
                arDTO = new AnalyzerResultDTO(ar.getId(), ar.getRunTime(), ar.getDetectorType(), ar.getSrcIPAddress(),
                        ar.getDstIPAddress(), ar.getNumberOfPacketsForDoS(), ar.getTimeWindowInSeconds(),
                        ar.getRefRuleId());
            }
            dtos.add(new AlertDTO(a.getId(),a.getAlertTypeId(), a.getCreationTime(), a.getDescription(), a.getStatus(),
                    a.getOrganizationId(), anDTO, arDTO, a.getSeverity()));
        }
        return dtos;
    }
    
    @GET
    @Produces({ MediaType.APPLICATION_JSON })
    public List<Alert> getAlerts() throws SQLException
    {
        log.info("getAlerts called");
        AlertDAO dao = DAOUtil.getAlertDAO();
        List<Alert> list = dao.getAllActiveAlerts();
        return list;
    }
    
    @PUT
    @Consumes({ MediaType.APPLICATION_JSON })
    @Produces(MediaType.TEXT_HTML)
    @Path("/classification")
    public Response newEndpointConfiguration(@Context ContainerRequest request, AlertClassification a){
        DecisionDAO dao = DAOUtil.getDecisionDAO();
        dao.setClassification(a.getAlertId(), a.getClassification());
//        
        return Response.ok().build();
    }
}
