/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.services;

import java.util.List;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import com.essence.model.AnomalyState;
import com.essence.persistence.DAOUtil;
import com.essence.persistence.DecisionDAO;

@Path("anomalystate")
public class AnomalyStateResource {
    @GET
    @Produces({ MediaType.APPLICATION_JSON })
    public List<AnomalyState> getCauses()
    {
        DecisionDAO dao = DAOUtil.getDecisionDAO();
        List<AnomalyState> list = dao.getStates();
        return list;
    }
}
