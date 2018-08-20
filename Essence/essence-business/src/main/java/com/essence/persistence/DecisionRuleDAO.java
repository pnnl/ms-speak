/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.persistence;

import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Query;

import com.essence.model.DecisionRule;
import com.essence.model.DecisionType;
import com.essence.model.DetectionRuleType;
import com.essence.model.SeverityType;

public class DecisionRuleDAO {
	EntityManagerFactory entityManagerFactory;    
	
	public static void main( String[] args)
	{
		DecisionRuleDAO dao = DAOUtil.getDecisionRuleDAO();
		DecisionRule rule = new DecisionRule();
		rule.setDecisionType(DecisionType.BLOCK_BETWEEN_PAIR);
		rule.setDetectionRuleRef(1234);
		rule.setDetectionRuleType(DetectionRuleType.MS_EP_CONNECTIVITY);
		rule.setPriority(8888);
		rule.setSeverityType(SeverityType.HIGH);
		dao.addDecisionRule(rule);
		DecisionRule rule1 = new DecisionRule();
		rule1.setDecisionType(DecisionType.BLOCK_SOURCE);
		rule1.setDetectionRuleRef(1234);
		rule1.setDetectionRuleType(DetectionRuleType.DENIAL_OF_SERVICE);
		rule1.setPriority(8888);
		rule1.setSeverityType(SeverityType.HIGH);
		dao.addDecisionRule(rule1);		
		
		List<DecisionRule> drs = dao.getAllDecisionRules();
		for (int i=0; drs != null && i<drs.size(); i++)
			drs.get(i).print();

		return;
	}

	public void addDecisionRule(DecisionRule rule)    
	{              
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		entityManager.persist(rule);
		entityManager.getTransaction().commit();
		entityManager.close();
	}    
	
	public void removeDecisionRule(DecisionRule rule)    
	{              
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		// inefficient implementation
		DecisionRule r = entityManager.find(DecisionRule.class, rule.getId());
		entityManager.remove(r);
		entityManager.getTransaction().commit();
		entityManager.close();
	}    
	
	public DecisionRule getDecisionRuleById(int id )    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		DecisionRule rule = entityManager.find(DecisionRule.class, id);        
		return rule;    
	}    
	
	@SuppressWarnings("unchecked")    
	public List<DecisionRule> getAllDecisionRules()    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT dr from DecisionRule dr");	

		List<DecisionRule> list = query.getResultList();       
		entityManager.close();
		return list;    
	}    

	@SuppressWarnings("unchecked")    
	public List<DecisionRule> getDecisionRulesByType(DecisionType type)    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT dr from DecisionRule dr where dr.ruleType = '" + type.toString() + "'");	

		List<DecisionRule> list = query.getResultList();       
		entityManager.close();
		return list;    
	}    

	@SuppressWarnings("unchecked")    
	public List<DecisionRule> getDecisionRulesByViolationType(DetectionRuleType type)    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT dr from DecisionRule dr where dr.detectionRuleType = '" + type.toString() + "'");	

		List<DecisionRule> list = query.getResultList();       
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
