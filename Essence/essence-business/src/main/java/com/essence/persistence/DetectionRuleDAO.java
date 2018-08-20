/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.persistence;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Query;

import com.essence.model.DetectionRule;
import com.essence.model.DetectionRuleType;
import com.essence.model.EndpointConfiguration;
import com.essence.model.OrganizationProfile;
import com.essence.model.ValueOutOfBoundDetail;

public class DetectionRuleDAO {
	EntityManagerFactory entityManagerFactory;    
	
	public Integer addDetectionRule(DetectionRule rule)    
	{              
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		entityManager.persist(rule);
		entityManager.flush();
		entityManager.getTransaction().commit();
		entityManager.close();
		
		return rule.getId();
	}    
	
	public void addValueOutOfBoundDetail(ValueOutOfBoundDetail d)    
	{              
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		entityManager.persist(d);
		entityManager.getTransaction().commit();
		entityManager.close();
	}    

	public void removeDetectionRule(DetectionRule rule)    
	{              
		if (rule.getRuleType().equals(DetectionRuleType.VALUE_OUT_OF_BOUND.toString()))
			removeValueOutOfBoundDetails(rule);
		
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		// inefficient implementation
		entityManager.remove(entityManager.find(DetectionRule.class, rule.getId()));
		entityManager.getTransaction().commit();
		entityManager.close();
	}    
	
	public void removeValueOutOfBoundDetails(DetectionRule rule)    
	{              
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		Query q = entityManager.createQuery("DELETE from ValueOutOfBoundDetail d where d.key.ruleId = " + rule.getId());
		q.executeUpdate();
		entityManager.getTransaction().commit();
		entityManager.close();
	}    

	@SuppressWarnings("unchecked")
	public void setDetectionRuleDetails4Rules(List<DetectionRule> rules)    
	{        
		if (rules == null || rules.isEmpty())
			return;
		
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		
		for (DetectionRule rule : rules) {
			Query query = entityManager.createQuery("SELECT d from ValueOutOfBoundDetail d where d.key.ruleId = " + rule.getId());	
	
			List<ValueOutOfBoundDetail> list = query.getResultList();       
			rule.setVoobDetails(list);
		}
		entityManager.close();
	}    

	public void setDetectionRuleXpathDetails4Voobs(List<DetectionRule> rules)    
	{        
		if (rules == null || rules.isEmpty())
			return;
		
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		MSPXpathDAO xpDao = DAOUtil.getMSPXpathDAO();
		
		for (DetectionRule rule : rules) {
			if (rule.getVoobDetails() != null && !rule.getVoobDetails().isEmpty()) {
				for (ValueOutOfBoundDetail d : rule.getVoobDetails()) {
					d.setXpathObject(xpDao.getXpathById(d.getKey().getxPathId()));
				}
			}
		}
		entityManager.close();
	}    

	public Map<Integer, List<ValueOutOfBoundDetail>> getValueOutOfBoundRuleDetailsByRuleIds(List<Integer> ruleIds) {
		EntityManager entityManager = entityManagerFactory.createEntityManager();     
		Map<Integer, List<ValueOutOfBoundDetail>> map = new HashMap<Integer, List<ValueOutOfBoundDetail>>();
		for (Integer id : ruleIds) {
			Query query = entityManager.createQuery("SELECT d from ValueOutOfBoundDetail d where d.key.ruleId = " + id);		
			@SuppressWarnings("unchecked")
			List<ValueOutOfBoundDetail> list = query.getResultList();  
			map.put(id,  list);
		}
		entityManager.close();
		return map;
	}
	
	@SuppressWarnings("unchecked")
	public List<ValueOutOfBoundDetail> getDetectionRuleDetailsByRuleId(int ruleId)    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT d from ValueOutOfBoundDetail d where d.key.ruleId = " + ruleId);	

		List<ValueOutOfBoundDetail> list = query.getResultList();       
		entityManager.close();
		return list;    
	}    

	public DetectionRule getDetectionRuleById(int id )    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		DetectionRule rule = entityManager.find(DetectionRule.class, id);    
		/*
		if (rule.getRuleType().equals(DetectionRuleType.VALUE_OUT_OF_BOUND.name())) {
			rule.setVoobDetails(getDetectionRuleDetailsByRuleId(id));
			System.out.println("done retrieving VOOB details for rule# " + rule.getId());
			for (ValueOutOfBoundDetail d : rule.getVoobDetails())
				d.print();
		}
		*/
		return rule;    
	}    
	
	@SuppressWarnings("unchecked")    
	@Deprecated // use API for rules under active policies
	public List<DetectionRule> getAllDetectionRules()    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT dr from DetectionRule dr");	

		List<DetectionRule> list = query.getResultList();       
		entityManager.close();
		return list;    
	}    

	public List<DetectionRule> getAllActiveDetectionRules()    
	{        
		  // retrieve rules only for active organization
		  OrganizationDAO pd = DAOUtil.getOrganizationDAO();
		  List<OrganizationProfile> ps = pd.getAllActiveOrganizations();
		  List<DetectionRule> activeRules = new ArrayList<DetectionRule>();
		  for (OrganizationProfile p : ps) {
			  activeRules.addAll(getAllDetectionRulesByOrganization(p.getId()));
		  }

		  return activeRules;
	}

	@SuppressWarnings("unchecked")    
	public List<DetectionRule> getAllDetectionRulesByOrganization(int orgId)    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT dr from DetectionRule dr where dr.organizationId = " + orgId);	

		List<DetectionRule> list = query.getResultList();       
		entityManager.close();
		return list;    
	}
	
	@SuppressWarnings("unchecked")    
    public List<DetectionRule> getAllDetectionRulesByIpAddress(String ipAddress)    
    {        
        EntityManager entityManager = entityManagerFactory.createEntityManager();        
        Query query = entityManager.createQuery("SELECT dr from DetectionRule dr where dr.srcIPAddress = '" + ipAddress + "' OR dr.dstIPAddress = '" + ipAddress + "'");  

        List<DetectionRule> list = query.getResultList();
        
        Query endpointQuery = entityManager.createQuery("SELECT ec from EndpointConfiguration ec where ec.key.hostIPAddress = '" + ipAddress + "'");
        List<EndpointConfiguration> ecList = endpointQuery.getResultList();
        
        if (ecList != null && ecList.size() > 0) {
            List<String> endpointTypes = new ArrayList<String>();
            for(EndpointConfiguration conf : ecList) {
                String[] types = conf.getEndpointCDs();
                if (types != null) {
                    for (int i = 0; i < types.length; ++i) {
                        if (!endpointTypes.contains(types[i])) {
                            endpointTypes.add(types[i]);
                        }
                    }
                }
            }
            
            if (endpointTypes.size() > 0) {
                Query ruleQuery2 = entityManager.createQuery("SELECT dr from DetectionRule dr where dr.srcEndpointType IN (:types)");
                ruleQuery2.setParameter("types", endpointTypes);
                List<DetectionRule> rulesList2 = ruleQuery2.getResultList();
                list.addAll(rulesList2);
            }
        }
        
        entityManager.close();
        return list;    
    }

	@SuppressWarnings("unchecked")    
	@Deprecated // use API for rules under active policies
	public List<DetectionRule> getDetectionRulesByType(DetectionRuleType type)    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT dr from DetectionRule dr where dr.ruleType = '" + type.toString() + "'");	

		List<DetectionRule> list = query.getResultList();       
		entityManager.close();
		return list;    
	}    

	public List<DetectionRule> getActiveDetectionRulesByType(DetectionRuleType type)    
	{        
		  // retrieve rules only for active organization
		  OrganizationDAO pd = DAOUtil.getOrganizationDAO();
		  List<OrganizationProfile> ps = pd.getAllActiveOrganizations();
		  List<DetectionRule> activeRules = new ArrayList<DetectionRule>();
		  for (OrganizationProfile p : ps) {
			  activeRules.addAll(getDetectionRulesByTypeAndOrganization(type, p.getId()));
		  }

		  return activeRules;
	}    

	@SuppressWarnings("unchecked")    
	public List<DetectionRule> getDetectionRulesByTypeAndOrganization(DetectionRuleType type, int orgId)    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT dr from DetectionRule dr where dr.ruleType = '" + type.toString() + "' and dr.organizationId = " + orgId);	

		List<DetectionRule> list = query.getResultList();       
		entityManager.close();
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
