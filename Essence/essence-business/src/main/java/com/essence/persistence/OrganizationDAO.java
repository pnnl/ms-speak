/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.persistence;

import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Query;

import com.essence.model.OrganizationProfile;

public class OrganizationDAO {
	EntityManagerFactory entityManagerFactory;    
	
	public static void main( String[] args)
	{
		OrganizationDAO dao = DAOUtil.getOrganizationDAO();

/*	
		Decision d = new Decision();
		d.setId(4);
		OrganizationProfile a = new OrganizationProfile();
		a.setTimestamp(new Timestamp(System.currentTimeMillis()));
		a.setDetail("Details of OrganizationProfile");
		a.setDecision(d); // have to set the decision Id thru the object, not by a.setDecisionId(decisionId)
		dao.addOrganizationProfile(a);		

		*/
		
		List<OrganizationProfile> ps = dao.getAllOrganizations();
		for (OrganizationProfile p: ps) {
			p.print();
		}
		
		ps = dao.getAllOrganizations();
		for (OrganizationProfile p: ps) {
			p.print();
		}

		return;
	}

	public void addOrganizationProfile(OrganizationProfile p)    
	{              
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		entityManager.persist(p);
		entityManager.getTransaction().commit();
		entityManager.close();
	}    

	public void removeOrganizationProfile(OrganizationProfile p)    
	{              
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		// inefficient implementation
		entityManager.remove(entityManager.find(OrganizationProfile.class, p.getId()));
		entityManager.getTransaction().commit();
		entityManager.close();
	}    
	
	public OrganizationProfile getOrganizationProfileById(int id )    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		OrganizationProfile d = entityManager.find(OrganizationProfile.class, id);        
		return d;    
	}    
	
	@SuppressWarnings("unchecked")    
	public List<OrganizationProfile> getAllOrganizations()    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT p from OrganizationProfile p");	

		List<OrganizationProfile> list = query.getResultList();       
		entityManager.close();
		return list;    
	}    
	
	public void activateOrganizationProfile(int id)    
	{              
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		//OrganizationProfile p = getOrganizationProfileById(id);
		Query query1 = entityManager.createNativeQuery("update organization set enabled = 0 where id <> " + id);
		query1.executeUpdate();
		Query query2 = entityManager.createNativeQuery("update organization set enabled = 1 where id = " + id);
		query2.executeUpdate();
		entityManager.getTransaction().commit();
		entityManager.close();
	}    

	@SuppressWarnings("unchecked")    
	public List<OrganizationProfile> getAllActiveOrganizations()    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT p from OrganizationProfile p where p.enabled = " + true);	

		List<OrganizationProfile> list = query.getResultList();       
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
