/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.services;

import java.util.ArrayList;
import java.util.List;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import com.essence.model.IdAndNameItem;
import com.essence.model.EndpointConfiguration;

@Path("endpointconfigurationtype")
public class EndpointConfigurationTypeResource {

    @GET
    @Produces({ MediaType.APPLICATION_JSON })
    @Path("/{version}")
    public List<IdAndNameItem> getTypes(@PathParam("version") Integer version)
    {
        List<IdAndNameItem> list = new ArrayList<IdAndNameItem>();
        
        switch (version) {
            case 3:
            default:
                for (int i = 0; i < EndpointConfiguration.EndpointTypesListItems3.length; ++i) {
                    IdAndNameItem type = new IdAndNameItem();
                    type.setId(EndpointConfiguration.EndpointTypesListItems3[i][0]);
                    type.setName(EndpointConfiguration.EndpointTypesListItems3[i][1]);
                    list.add(type);
                }
                break;
            case 5:
                for (int i = 0; i < EndpointConfiguration.EndpointTypesListItems5.length; ++i) {
                    IdAndNameItem type = new IdAndNameItem();
                    type.setId(EndpointConfiguration.EndpointTypesListItems5[i][0]);
                    type.setName(EndpointConfiguration.EndpointTypesListItems5[i][1]);
                    list.add(type);
                }
                break;
        }
        
        return list;
    }
}
