/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.services;

import java.util.List;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import com.essence.persistence.ClassificationDAO;
import com.essence.persistence.DAOUtil;
import com.essence.model.Classification;

@Path("classification")
public class ClassificationResource {
    @GET
    @Produces({ MediaType.APPLICATION_JSON })
    public List<Classification> getClassifications()
    {
        ClassificationDAO dao = DAOUtil.getClassificationDAO();
        List<Classification> list = dao.getAllClassifications();
        return list;
    }
}
