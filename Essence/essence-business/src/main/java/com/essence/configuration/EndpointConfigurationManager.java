/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.configuration;

import com.essence.action.Device;
import com.essence.action.SDNControllerNBI;
import com.essence.persistence.DAOUtil;
import com.essence.persistence.EndpointConfigurationDAO;
import com.essence.persistence.OrganizationDAO;
import com.essence.model.EndpointConfiguration;
import com.essence.model.OrganizationProfile;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Created by BWintemberg on 6/7/2015.
 */
public class EndpointConfigurationManager {
    public List<EndpointConfiguration> getEndpointConfigurations() {
        // retrieve the current host list
        EndpointConfigurationDAO dao = DAOUtil.getEndpointConfigurationDAO();
        List<EndpointConfiguration> ecs = dao.getAllActiveEndpointConfigurations();

        Map<String, EndpointConfiguration> ecsMap = new HashMap<String, EndpointConfiguration>();
        if (ecs != null)
            for (int i=0; i<ecs.size(); i++)
                ecsMap.put(ecs.get(i).getKey().getHostIPAddress(), ecs.get(i));

        // query SDN controller for the latest network hosts
        SDNControllerNBI api = DAOUtil.getSDNControllerNBI();
        List<Device> deviceList = api.getAllDevices(); // never null

        OrganizationDAO pd = DAOUtil.getOrganizationDAO();
        List<OrganizationProfile> os = pd.getAllActiveOrganizations();
        assert(os != null && !os.isEmpty());
        int activePolicyId = os.get(0).getId();

        // Add new hosts to the database
        boolean hasAddition = false;
        for (int i=0; i<deviceList.size(); i++) {
            if (deviceList.get(i).getIpv4() != null && !deviceList.get(i).getIpv4().isEmpty())
                if (!ecsMap.keySet().contains(deviceList.get(i).getIpv4().get(0))) { // IP not in DB yet, add it to the database
                    EndpointConfiguration epConfig = new EndpointConfiguration();

                    epConfig.getKey().setHostIPAddress(deviceList.get(i).getIpv4().get(0));
                    if (deviceList.get(i).getMac() != null && !deviceList.get(i).getMac().isEmpty())
                        epConfig.setHostName(deviceList.get(i).getMac().get(0));
                    epConfig.getKey().setOrganizationId(activePolicyId);
                    dao.addEndpointConfiguration(epConfig);
                    hasAddition = true;
                } else if (!ecsMap.get(deviceList.get(i).getIpv4().get(0)).getHostName().equals(deviceList.get(i).getMac().get(0))) { // update info for IP
                    EndpointConfiguration epConfig = ecsMap.get(deviceList.get(i).getIpv4().get(0));
                    epConfig.setHostName(deviceList.get(i).getMac().get(0));
                    System.out.println("IP=" + deviceList.get(i).getIpv4().get(0) + "\toldMac=" + ecsMap.get(deviceList.get(i).getIpv4().get(0)).getHostName() + "\tnewMac=" + deviceList.get(i).getMac().get(0));
                    dao.saveEndpointConfiguration(epConfig); //TO-DO: need to test
                }
        }

        if (hasAddition) // refresh the list
            ecs = dao.getAllActiveEndpointConfigurations(); // need to verify order by IP

        return ecs;
    }
}
