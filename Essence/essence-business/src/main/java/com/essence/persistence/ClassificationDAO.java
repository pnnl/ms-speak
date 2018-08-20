/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.persistence;

import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Query;

import com.essence.model.Classification;

public class ClassificationDAO {
    EntityManagerFactory entityManagerFactory;
    
    @SuppressWarnings("unchecked")
    public List<Classification> getAllClassifications() {
        EntityManager em = entityManagerFactory.createEntityManager();
        Query query = em.createQuery("SELECT c FROM Classification c");
        List<Classification> results = query.getResultList();
        return results;
    }
    
    public Classification getDecisionById(Long id)    
    {
        EntityManager entityManager = entityManagerFactory.createEntityManager();        
        Classification d = entityManager.find(Classification.class, id);        
        return d;
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
