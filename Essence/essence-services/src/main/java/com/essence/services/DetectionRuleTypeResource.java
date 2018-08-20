/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.services;

import java.util.ArrayList;
import java.util.List;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import com.essence.model.IdAndNameItem;

@Path("detectionruletype")
public class DetectionRuleTypeResource {
    static public String[][] DetectionRuleTypeList = {
            {"VALUE_OUT_OF_BOUND", "Value out of bounds"},
            {"MS_EP_CONNECTIVITY", "Multispeak Endpoint Connectivity"},
            {"WRONG_MSG_TO_MS_EP", "Wrong message to multispeak endpoint"},
            {"ERR_MSG_FROM_MS_EP", "Error message from multispeak endpoint"},
            {"WRONG_MSG_FORMAT", "Wrong message format"},
            {"DENIAL_OF_SERVICE", "Denial of service"},
            {"NW_SEGMENTATION", "Network segmentation"},
            {"NEW_HOST", "New host"},
        };
    
    @GET
    @Produces({ MediaType.APPLICATION_JSON })
    public List<IdAndNameItem> getTypes() {
        //List<DetectionRuleType> types = Arrays.asList(DetectionRuleType.values());
        //List<String> results = new ArrayList<String>();
        //String[] results = new String[types.size()];
//        for(int i = 0; i < types.size(); ++i){
//            results[i] = types.get(i).toString();
//            //results.add(types[i].toString());
//        }
        List<IdAndNameItem> list = new ArrayList<IdAndNameItem>();
        for (int i = 0; i < DetectionRuleTypeList.length; ++i) {
            IdAndNameItem type = new IdAndNameItem();
            type.setId(DetectionRuleTypeList[i][0]);
            type.setName(DetectionRuleTypeList[i][1]);
            list.add(type);
        }
        //for(DetectionRuleType type : types) {
        //    results.add(type.toString());
        //}
        
        //DetectionRuleTypes ruleTypes = new DetectionRuleTypes();
        //ruleTypes.setTypes(results);
        
        return list;
    }
}
