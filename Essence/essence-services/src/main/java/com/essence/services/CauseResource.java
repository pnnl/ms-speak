/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.services;

import java.util.List;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import com.essence.persistence.DAOUtil;
import com.essence.persistence.DecisionDAO;
import com.essence.model.Cause;

@Path("cause")
public class CauseResource {
    @GET
    @Produces({ MediaType.APPLICATION_JSON })
    public List<Cause> getCauses()
    {
        DecisionDAO dao = DAOUtil.getDecisionDAO();
        List<Cause> list = dao.getCauses();
        return list;
    }
}
