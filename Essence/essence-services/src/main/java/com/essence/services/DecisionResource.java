/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.services;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.WebApplicationException;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response.Status;

import com.essence.persistence.DAOUtil;
import com.essence.persistence.DecisionDAO;
import com.essence.model.Decision;

@Path("decision")
public class DecisionResource {
    @GET
    @Produces({ MediaType.APPLICATION_JSON })
    @Path("/alertid/{alertId}")
    public Decision getDecisionByAlertId(@PathParam("alertId") long alertId) {
        DecisionDAO dao = DAOUtil.getDecisionDAO();
        Decision decision = dao.getDecisionByAlertId(alertId);
        
        if (decision != null) {
            return decision;
        }

        throw new WebApplicationException("Decision with alert id " + alertId + " does not exist.", Status.NOT_FOUND);
    }
}
