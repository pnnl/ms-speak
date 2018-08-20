/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.services;

import java.util.List;

import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.WebApplicationException;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.Response.Status;

import com.essence.model.EndpointConfiguration;
import com.essence.model.OrganizationProfile;
import org.glassfish.jersey.server.ContainerRequest;

import com.essence.persistence.DAOUtil;
import com.essence.persistence.EndpointConfigurationDAO;
import com.essence.persistence.OrganizationDAO;

@Path("endpointconfiguration")
public class EndpointConfigurationResource {
    @PUT
    @Consumes({ MediaType.APPLICATION_JSON })
    @Produces(MediaType.TEXT_HTML)
    public Response newEndpointConfiguration(@Context ContainerRequest request, EndpointConfiguration conf){
        if (conf.getKey() == null || conf.getKey().getHostIPAddress() == null || conf.getKey().getHostIPAddress().trim().length() == 0) {
            return Response.status(Status.BAD_REQUEST).build();
        }
        
        if (conf.getKey().getOrganizationId() < 1) {
            OrganizationDAO pd = DAOUtil.getOrganizationDAO();
            List<OrganizationProfile> os = pd.getAllActiveOrganizations();
            assert(os != null && !os.isEmpty());
            conf.getKey().setOrganizationId(os.get(0).getId());
        }
        
      EndpointConfigurationDAO dao = DAOUtil.getEndpointConfigurationDAO();
      String url = request.getUriInfo().getRequestUri().toASCIIString();
      try {
          EndpointConfiguration ec = dao.getEndpointConfigurationByIPAndOrganization(conf.getKey().getHostIPAddress(), conf.getKey().getOrganizationId());
          
          if (ec == null) { 
              dao.addEndpointConfiguration(conf);
              return Response.status(Response.Status.CREATED) // 201
                      .entity("A new endpoint configuration has been created")
                      .header("Location", url + "/ip/" + String.valueOf(conf.getKey().getHostIPAddress())).build();
          }
          else {
              if (conf.getEndpointList() != null) {
                  ec.setEndpointList(conf.getEndpointList());
              }
              if (conf.getHostName() != null){
                  ec.setHostName(conf.getHostName());
              }
              if (conf.getVersion() != null && conf.getVersion().trim().length() > 0){
                  ec.setVersion(conf.getVersion());
              }
              
              dao.saveEndpointConfiguration(ec);
              return Response.status(Response.Status.OK) // 200
                      .entity("The endpoint configuration has been updated")
                      .header("Location", url + "/ip/" + String.valueOf(conf.getKey().getHostIPAddress())).build();
          }
      } catch (Exception ex) {
          // TODO: error handling
          return Response.serverError().build();
      }
    }
    
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    @Path("/organization/{organization}/ip/{ip}")
    public EndpointConfiguration getEndpointConfigurationByIpAndOrganization(@PathParam("organization") int organization, @PathParam("ip") String ipAddress) {
        EndpointConfigurationDAO dao = DAOUtil.getEndpointConfigurationDAO();
        EndpointConfiguration ec = dao.getEndpointConfigurationByIPAndOrganization(ipAddress, organization);

        return ec;
    }
    
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    @Path("/ip/{ip}")
    public EndpointConfiguration getEndpointConfigurationByIp(@PathParam("ip") String ipAddress) {
        EndpointConfigurationDAO dao = DAOUtil.getEndpointConfigurationDAO();
        EndpointConfiguration ec = dao.getEndpointConfigurationByIP(ipAddress);
        
        if (ec == null)
            throw new WebApplicationException("EndpointConfiguration with IP address " + ipAddress + " not found.", Status.NOT_FOUND);

        return ec;
    }
}
