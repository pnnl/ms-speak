/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.services;

import java.util.List;

import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import org.glassfish.jersey.server.ContainerRequest;

import com.essence.persistence.DAOUtil;
import com.essence.persistence.DetectionRuleDAO;
import com.essence.persistence.OrganizationDAO;
import com.essence.model.DetectionRule;
import com.essence.model.OrganizationProfile;

@Path("detectionrule")
public class DetectionRuleResource {
    @POST
    @Consumes({ MediaType.APPLICATION_JSON })
    @Produces(MediaType.TEXT_HTML)
    public Response newDetectionRule(@Context ContainerRequest request, DetectionRule rule){
        OrganizationDAO pd = DAOUtil.getOrganizationDAO();
        List<OrganizationProfile> os = pd.getAllActiveOrganizations();
        assert(os != null && !os.isEmpty());
        rule.setOrganizationId(os.get(0).getId());
        
      DetectionRuleDAO dao = DAOUtil.getDetectionRuleDAO();
      try {
          Integer id = dao.addDetectionRule(rule);
          String url = request.getUriInfo().getRequestUri().toASCIIString();
          return Response.status(Response.Status.CREATED)// 201
                  .entity("A new detection rule has been created")
                  .header("Location", url + "/" + String.valueOf(id)).build();
      } catch (Exception ex) {
          // TODO: error handling
          return Response.serverError().build();
          //return "Failure";
      }
    }

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public List<DetectionRule> getRules() {
        DetectionRuleDAO dao = DAOUtil.getDetectionRuleDAO();
        List<DetectionRule> list = dao.getAllActiveDetectionRules();
        return list;
    }

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    @Path("/{id}")
    public DetectionRule getRuleById(@PathParam("id") int id) {
        DetectionRuleDAO dao = DAOUtil.getDetectionRuleDAO();
        DetectionRule d = dao.getDetectionRuleById(id);
        return d;
    }
    
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    @Path("/ip/{ip}")
    public List<DetectionRule> getRulesByIp(@PathParam("ip") String ipAddress) {
        DetectionRuleDAO dao = DAOUtil.getDetectionRuleDAO();
        List<DetectionRule> list = dao.getAllDetectionRulesByIpAddress(ipAddress);
        return list;
    }
}
