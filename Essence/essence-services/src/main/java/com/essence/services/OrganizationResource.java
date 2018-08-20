/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.services;

import java.sql.SQLException;
import java.util.List;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import com.essence.persistence.DAOUtil;
import com.essence.persistence.OrganizationDAO;
import com.essence.model.OrganizationProfile;

@Path("organization")
public class OrganizationResource {
    @GET
    @Produces({ MediaType.APPLICATION_JSON })
    public List<OrganizationProfile> getOrganizations() throws SQLException
    {
        OrganizationDAO dao = DAOUtil.getOrganizationDAO();
        List<OrganizationProfile> list = dao.getAllActiveOrganizations();
        return list;
    }
}
