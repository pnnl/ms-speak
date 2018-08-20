/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.persistence;

import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Query;

import com.essence.model.Action;

//@SuppressWarnings("unused")
public class ActionDAO {
	EntityManagerFactory entityManagerFactory;    
	
	public static void main( String[] args)
	{
		ActionDAO dao = DAOUtil.getActionDAO();

/*	
		Decision d = new Decision();
		d.setId(4);
		Action a = new Action();
		a.setTimestamp(new Timestamp(System.currentTimeMillis()));
		a.setDetail("Details of action");
		a.setDecision(d); // have to set the decision Id thru the object, not by a.setDecisionId(decisionId)
		dao.addAction(a);		

		*/
		
		List<Action> as = dao.getAllActions2();
		for (Action ai: as) {
			ai.print();
			ai.getDecision().print();
		}

		return;
	}

	public void addAction(Action d)    
	{              
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		entityManager.persist(d);
		entityManager.getTransaction().commit();
		entityManager.close();
	}    

	public void removeAction(Action d)    
	{              
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		// inefficient implementation
		entityManager.remove(entityManager.find(Action.class, d.getId()));
		entityManager.getTransaction().commit();
		entityManager.close();
	}    
	
	public Action getActionById(int id )    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Action d = entityManager.find(Action.class, id);        
		return d;    
	}    
	
	/*
	 * TO-DO: Using the dependent object one-to-one relationship to load is not efficient. May need to go to straight SQL query.
	 */
	@SuppressWarnings("unchecked")    
	public List<Action> getAllActions()    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT a from Action a");	

		List<Action> list = query.getResultList();       
		entityManager.close();
		return list;    
	}    

	
	@SuppressWarnings("unchecked")    
	public List<Action> getAllActions2()    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createNativeQuery("select a.*, d.* from action a, decision d where a.decision_id=d.id", Action.class);	

		List<Action> list = query.getResultList();       
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
