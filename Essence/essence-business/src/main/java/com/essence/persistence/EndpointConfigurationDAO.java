/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.persistence;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Query;

import com.essence.model.EndpointConfiguration;
import com.essence.model.EndpointConfigurationKey;
import com.essence.model.OrganizationProfile;
import com.essence.ui.shared.Validator;

public class EndpointConfigurationDAO {
	EntityManagerFactory entityManagerFactory;    
	
	public static void main(String[] args) {
		//testGetAll();
		testGetByIP();
	}

    @SuppressWarnings("unused")
	private static void testGetAll() {
		EndpointConfigurationDAO dao = DAOUtil.getEndpointConfigurationDAO();
		dao.getAllActiveEndpointConfigurations();		
	}
	
	private static void testGetByIP() {
		String testIp = "172.16.0.5";
		System.out.println("Testing getEndpointConfigurationByIP for IP " + testIp);
		EndpointConfigurationDAO dao = DAOUtil.getEndpointConfigurationDAO();
		EndpointConfiguration ec = dao.getEndpointConfigurationByIP(testIp);
		if (ec != null)
			ec.print();
		else
			System.out.println("There is no configuration record for IP " + testIp);
		
		EndpointConfigurationKey k = new EndpointConfigurationKey();
		k.setHostIPAddress(testIp);
		k.setOrganizationId(1);
		System.out.println("Testing getEndpointConfigurationById for IP " + k.getHostIPAddress() + " organization = " + k.getOrganizationId());
		ec = dao.getEndpointConfigurationById(k);
		if (ec != null)
			ec.print();
		else
			System.out.println("There is no configuration record for IP " + testIp);
	}
	
	public void addEndpointConfiguration(EndpointConfiguration ec)    
	{              
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		entityManager.persist(ec);
		entityManager.getTransaction().commit();
		entityManager.close();
	}    
	
	public void saveEndpointConfiguration(EndpointConfiguration ec)    
	{              
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		entityManager.merge(ec);
		entityManager.getTransaction().commit();
		entityManager.close();
	}    

	public void removeEndpointConfiguration(EndpointConfiguration ec)    
	{              
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		entityManager.remove(entityManager.find(EndpointConfiguration.class, ec.getKey()));
		entityManager.getTransaction().commit();
		entityManager.close();
	}    

	public EndpointConfiguration getEndpointConfigurationById(EndpointConfigurationKey id )    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		EndpointConfiguration ec = entityManager.find(EndpointConfiguration.class, id);        
		return ec;    
	}    

	@SuppressWarnings("unchecked")
    public EndpointConfiguration getEndpointConfigurationByIP(String ip )    
	{        
		if (!Validator.validateIPAddress(ip))
			return null;

		List<OrganizationProfile> ps = DAOUtil.getOrganizationDAO().getAllActiveOrganizations();
		assert(ps != null && !ps.isEmpty());
		int activeorganizationId = ps.get(0).getId();

		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT ec from EndpointConfiguration ec where ec.key.hostIPAddress = '" + ip + "' and ec.key.organizationId = " + activeorganizationId);	

		List<EndpointConfiguration> list = query.getResultList();       
		entityManager.close();
		
		if (list != null && !list.isEmpty()) {
				return list.get(0);
		}
		
		return null;    
	}
	
	@SuppressWarnings("unchecked")
    public EndpointConfiguration getEndpointConfigurationByIPAndOrganization(String ip, int organizationId)    
    {        
        if (!Validator.validateIPAddress(ip))
            return null;

        EntityManager entityManager = entityManagerFactory.createEntityManager();        
        Query query = entityManager.createQuery("SELECT ec from EndpointConfiguration ec where ec.key.hostIPAddress = '" + ip + "' and ec.key.organizationId = " + organizationId);   

        List<EndpointConfiguration> list = query.getResultList();       
        entityManager.close();
        
        if (list != null && !list.isEmpty()) {
                return list.get(0);
        }
        
        return null;    
    }
	
	@SuppressWarnings("unchecked")    
	public List<EndpointConfiguration> getAllEndpointConfigurations1()    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT ec from EndpointConfiguration ec order by ec.key.hostIPAddress");	

		List<EndpointConfiguration> list = query.getResultList();       
		entityManager.close();
		Collections.sort(list, EndpointConfiguration.Comparators.HOST_IP_ADDRESS);
		return list;    
	}    

	public List<EndpointConfiguration> getAllActiveEndpointConfigurations()    
	{        
		  // retrieve rules only for active organization
		  OrganizationDAO pd = DAOUtil.getOrganizationDAO();
		  List<OrganizationProfile> ps = pd.getAllActiveOrganizations();
		  List<EndpointConfiguration> activeECs = new ArrayList<EndpointConfiguration>();
		  for (OrganizationProfile p : ps) {
			  activeECs.addAll(getAllEndpointConfigurationsByOrganization(p.getId()));
		  }

		  return activeECs;		  
	}    

	@SuppressWarnings("unchecked")    
	public List<EndpointConfiguration> getAllEndpointConfigurationsByOrganization(int orgId)    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT ec from EndpointConfiguration ec where ec.key.organizationId = " + orgId + " order by ec.key.hostIPAddress");	

		List<EndpointConfiguration> list = query.getResultList();       
		entityManager.close();
		Collections.sort(list, EndpointConfiguration.Comparators.HOST_IP_ADDRESS);
		return list;    
	}    
	
	public EntityManagerFactory getEntityManagerFactory()    
	{        
		return entityManagerFactory;    
	}    
	
	public void setEntityManagerFactory(EntityManagerFactory entityManagerFactory)    
	{        
		this.entityManagerFactory = entityManagerFactory;    
	}    
}
