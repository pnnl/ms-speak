/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.persistence;

import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Query;

import com.essence.model.Anomaly;
import com.essence.model.AnomalyState;
import com.essence.model.AnomalyTargetType;
import com.essence.model.Cause;

public class AnomalyDAO {
	EntityManagerFactory entityManagerFactory;
	
	public static void main( String[] args)
	{
	    //AnomalyDAO dao = DAOUtil.getAnomalyDAO();
		
    	//for (int i=0; i<30; i++) {	
    		//Anomaly c = new Anomaly();
//    		c.setName("Spurious Ping");
//    		c.setTestData("{PingURL: 15}");
//    		c.setTolerance("{1}");
//    		c.setTrainingData("{PingURL: 0}");
//    		dao.addAnomaly(c);
//    		
//            Anomaly c2 = new Anomaly();
//            c2.setName("Unnamed");
//            c2.setTestData("{CDStateChangedNotification: 30}");
//            c2.setTolerance("{1}");
//            c2.setTrainingData("{CDStateChangedNotification: 1}");
            //dao.addAnomaly(c2);
    	//}

		return;
	}

	public void addAnomaly(Anomaly c)    
	{
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		entityManager.persist(c);
		entityManager.getTransaction().commit();
		entityManager.close();
	}

	public void removeAnomaly(Anomaly c)    
	{
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		// inefficient implementation
		entityManager.remove(entityManager.find(Anomaly.class, c.getId()));
		entityManager.getTransaction().commit();
		entityManager.close();
	}
	
	public Anomaly getAnomalyById(long id )    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Anomaly Anomaly = entityManager.find(Anomaly.class, id);        
		return Anomaly;    
	}

	@SuppressWarnings("unchecked")
	public List<Anomaly> getAllAnomalys()
	{        
        EntityManager entityManager = entityManagerFactory.createEntityManager();
        Query query = entityManager.createQuery("SELECT c from Anomaly c");

        List<Anomaly> list = query.getResultList();
        entityManager.close();
        return list;
	}
	
	@SuppressWarnings("unchecked")
    public List<AnomalyTargetType> getTargetTypes() {
        EntityManager entityManager = entityManagerFactory.createEntityManager();
        Query query = entityManager.createQuery("SELECT t from AnomalyTargetType t");

        List<AnomalyTargetType> list = query.getResultList();
        entityManager.close();
        return list;
	}

	public List<AnomalyState> getAnomalyStates() {
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		Query query = entityManager.createQuery("SELECT s from AnomalyState s");

		List<AnomalyState> list = query.getResultList();
		entityManager.close();
		return list;
	}

	public List<Cause> getCauses() {
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		Query query = entityManager.createQuery("SELECT c from Cause c");

		List<Cause> list = query.getResultList();
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