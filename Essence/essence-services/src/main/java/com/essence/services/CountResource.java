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

import com.essence.alert.AlertCount;
import com.essence.persistence.AlertDAO;
import com.essence.persistence.DAOUtil;

@Path("alertcount")
public class CountResource {
//    @GET
//    @Produces(MediaType.TEXT_PLAIN)
//    public String getIt() {
//        AlertDAO dao = DAOUtil.getAlertDAO();
//        int count = 0;
//        //try {
//            //List<IPAddressAlertCount> list = dao.getAlertCountByIPAddress();
//            //count = list.size();
//        //} catch (SQLException e) {
//        //    e.printStackTrace();
//       // }
//        return "Got it! " + count;
//    }

//    @GET
//    @Produces({ MediaType.APPLICATION_JSON })
//    public IPAddressAlertCounts getCounts() throws SQLException
//    {
//        AlertDAO dao = DAOUtil.getAlertDAO();
//        HashMap<String, AlertCount> map = dao.getAlertCountByIPAddress();
//        IPAddressAlertCounts counts = new IPAddressAlertCounts();
//        counts.setItems(map);
//        return counts;
//    }
    
    @GET
    @Produces({ MediaType.APPLICATION_JSON })
    public List<AlertCount> getCount() throws SQLException
    {
        AlertDAO dao = DAOUtil.getAlertDAO();
        List<AlertCount> list = dao.getAlertCountByIPAddress();
        return list;
    }
}
