/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.persistence;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Query;

import com.essence.model.EngineRunLog;


public class EngineRunLogDAO {
	EntityManagerFactory entityManagerFactory;
	
	public static void main (String[] args) {
		//for testing
		EngineRunLogDAO dao = DAOUtil.getEngineRunLogDAO();
		long runtime = 1234567L;
		long cutofftime = 7654321L;
		for (int i = 0; i<10; i++){
			EngineRunLog log = new EngineRunLog();
			log.setDescription("test engine log");
			log.setRunTime(runtime+i);
			log.setCutoffTime(cutofftime+i);
			dao.addEngineRunLog(log);
		}
		
		dao.getEngineRunLogById(1).print();
		dao.getEngineRunLogById(6).print();
		dao.getLastEngineRunLog().print();
		dao.removeEngineRunLogById(1);
		EngineRunLog entry = dao.getEngineRunLogById(2);
		if (entry == null)
			System.out.println("id does not exist");
		else
			entry.print();
	}
	public void addEngineRunLog (EngineRunLog log) {
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		entityManager.persist(log);
		entityManager.getTransaction().commit();
		entityManager.close();
		
	}
	
	public void removeEngineRunLogById (int id) {
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		entityManager.remove(entityManager.find(EngineRunLog.class,id));
		entityManager.getTransaction().commit();
		entityManager.close();		
	}
	
	public Integer deleteAllEngineRunLogs() {
        EntityManager entityManager = entityManagerFactory.createEntityManager();
        entityManager.getTransaction().begin();
        Query query = entityManager.createQuery("DELETE from EngineRunLog");
        int result = query.executeUpdate();
        entityManager.getTransaction().commit();
        return result;
	}
	
	public EngineRunLog getEngineRunLogById (int id){
		EntityManager entityManager = entityManagerFactory.createEntityManager();
        entityManager.getTransaction().begin();
		EngineRunLog log = entityManager.find(EngineRunLog.class, id);
		return log;
	}
	public EngineRunLog getLastEngineRunLog (){
		Object result;
		EngineRunLog log = new EngineRunLog();
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		Query query = entityManager.createNativeQuery("SELECT MAX(id) from engine_run_log");
		result = query.getSingleResult();
		if (result != null) {
			Integer id = (Integer) result;
			log = entityManager.find(EngineRunLog.class, id);
		}
		else
			log = null;
		return log;
	}
	public EntityManagerFactory getEntityManagerFactory(){
		return entityManagerFactory;
	}
	public void setEntityManagerFactory(EntityManagerFactory entityManagerFactory){
		this.entityManagerFactory = entityManagerFactory;
	}
	
}
