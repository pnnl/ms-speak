/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.persistence;

import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Query;

import com.essence.model.*;

//@SuppressWarnings("unused")
public class DecisionDAO {
	EntityManagerFactory entityManagerFactory;    
	
	public static void main( String[] args)
	{
		DecisionDAO dao = DAOUtil.getDecisionDAO();
		/*
		Decision d = new Decision();
		d.setDecisionRuleId(4);
		d.setDecisionType(DecisionType.BLOCK_BETWEEN_PAIR.toString());
		d.setDestinationIPAddress("172.16.0.2");
		d.setSourceIPAddress("172.16.0.3");
		d.setIssueId(2l);
		d.setStatus(DecisionStatusType.OPEN.toString());		
		dao.addDecision(d);		
		
		Decision d1 = new Decision();
		d1.setDecisionRuleId(null);
		d1.setDecisionType(DecisionType.MANUAL_ACTION.toString());
		d1.setDestinationIPAddress("172.16.0.1");
		d1.setSourceIPAddress("172.16.0.2");
		d1.setIssueId(3l);
		d1.setStatus(DecisionStatusType.OPEN.toString());		
		dao.addDecision(d1);		
		
		List<Decision> ds = dao.getAllDecisions();
		for (Decision di: ds)
			di.print();
*/
		List<Decision> ds = dao.getDecisionsByStatus(DecisionStatusType.PERFORMED);
		for (Decision di: ds) {
			di.print();
			di.getIssue().print();
		}
		
		return;
	}

	public void addDecision(Decision d)    
	{              
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		entityManager.persist(d);
		entityManager.getTransaction().commit();
		entityManager.close();
	}    

	public void updateDecisionForFinding(Long arId, Integer decisionRuleId, DecisionType type)    
	{              
		if (arId == null || decisionRuleId == null || type == null)
			return;
		
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		Query query = entityManager.createNativeQuery("update decision set decision_rule_ref=" + decisionRuleId + ", decision_type='"+ type.toString()+"' where issue_id=" + arId); 
		query.executeUpdate();
		entityManager.getTransaction().commit();
		entityManager.close();
	}    

	public void updateStatus(Decision d, DecisionStatusType type)    
	{              
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		Query query = null;
		if (d != null && type != null)
			query = entityManager.createNativeQuery("update decision set status = '" + type.toString() + "' where id = " + d.getId()); 
		query.executeUpdate();
		entityManager.getTransaction().commit();
		entityManager.close();
	}
    public void saveDecision(Decision d)    
    {              
        EntityManager entityManager = entityManagerFactory.createEntityManager();
        entityManager.getTransaction().begin();
        entityManager.persist(d);
        entityManager.getTransaction().commit();
        entityManager.close();
    } 

	public void removeDecision(Decision d)    
	{              
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		// inefficient implementation
		entityManager.remove(entityManager.find(Decision.class, d.getId()));
		entityManager.getTransaction().commit();
		entityManager.close();
	}    
	
	public Decision getDecisionById(int id)    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Decision d = entityManager.find(Decision.class, id);        
		return d;    
	}

    @SuppressWarnings("unchecked")
    public Decision getDecisionByAlertId(long id)    
    {        
        EntityManager entityManager = entityManagerFactory.createEntityManager();
        Query query = entityManager.createQuery("SELECT d from Decision d join fetch d.issue i" +
                " left join fetch i.analyzerResult left join fetch i.anomaly" +
                " where d.issueId = " + id);
        List<Decision> list = query.getResultList();       
        entityManager.close();
        
        if (list != null && !list.isEmpty()) {
                return list.get(0);
        }
        
        return null;
    }

	@SuppressWarnings("unchecked")
	public List<Decision> getDecisionsByAlertIds(List<Long> ids)
	{
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		Query query = entityManager.createQuery("SELECT d from Decision d join fetch d.issue where d.issueId IN (?1)");
		query.setParameter(1, ids);
		List<Decision> list = query.getResultList();
		entityManager.close();

		return list;
	}
	
	@SuppressWarnings("unchecked")
	public List<Decision> getAllDecisions()
	{
		EntityManager entityManager = entityManagerFactory.createEntityManager();
        String q = "SELECT d from Decision d join fetch d.issue i" +
                " left join fetch i.analyzerResult left join fetch i.anomaly";
		Query query = entityManager.createQuery(q);

		List<Decision> list = query.getResultList();
		entityManager.close();
		return list;
	}

	@SuppressWarnings("unchecked")    
	public List<Decision> getDecisionsByStatus(DecisionStatusType type)    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT d from Decision d where d.status = '" + type.toString() + "'");	

		List<Decision> list = query.getResultList();       
		entityManager.close();
		return list;    
	}    

	@SuppressWarnings("unchecked")    
	public List<Decision> getDecisionsByType(DecisionType type)    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT d from Decision d where d.decisionType = '" + type.toString() + "'");	

		List<Decision> list = query.getResultList();       
		entityManager.close();
		return list;    
	}    

	@SuppressWarnings("unchecked")
    public List<Cause> getCauses() {
        EntityManager entityManager = entityManagerFactory.createEntityManager();        
        Query query = entityManager.createQuery("SELECT c from Cause c");    

        List<Cause> list = query.getResultList();       
        entityManager.close();
        return list;  
	}
	
    @SuppressWarnings("unchecked")
    public List<AnomalyState> getStates() {
        EntityManager entityManager = entityManagerFactory.createEntityManager();        
        Query query = entityManager.createQuery("SELECT a from AnomalyState a");    

        List<AnomalyState> list = query.getResultList();       
        entityManager.close();
        return list;  
    }

	public void setActionTypeOnManualDecision(Decision decision, DecisionType type) {
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		Query query = null;
		if (type == null)
			query = entityManager.createNativeQuery("update decision set memo=null where id = " + decision.getId());
		else
			query = entityManager.createNativeQuery("update decision set memo = '" + type.toString() + "' where id = " + decision.getId()); 
		query.executeUpdate();
		entityManager.getTransaction().commit();
		entityManager.close();
	}

    public void setDecisionTypeAndDecisionRuleIdOnDecision(Decision decision, String decisionType, int ruleId) {
        EntityManager entityManager = entityManagerFactory.createEntityManager();
        entityManager.getTransaction().begin();
        Query query = entityManager.createNativeQuery("update decision set decision_rule_ref = " + ruleId +
                ", decision_type = '" + decisionType + "' where id = " + decision.getId());
        query.executeUpdate();
        entityManager.getTransaction().commit();
        entityManager.close();
    }

    @SuppressWarnings("unchecked")
	public void setState(long alertId, AnomalyState state) {
        EntityManager entityManager = entityManagerFactory.createEntityManager();
        Query query = entityManager.createQuery("SELECT d from Decision d where d.issueId = " + alertId);
        List<Decision> list = query.getResultList();
        Decision d = null;

        if (list != null && !list.isEmpty()) {
            d = list.get(0);
        }

        AnomalyState storedState = null;
        if (state.getId() != null && state.getId() > 0) {
            storedState = entityManager.find(AnomalyState.class, state.getId());
        }

        entityManager.getTransaction().begin();
        if (d == null) {
            Alert alert = entityManager.find(Alert.class, alertId);

            d = new Decision();

            if (storedState != null) {
                d.setAnomalyState(storedState);
            } else {
                d.setAnomalyState(state);
            }

            d.setIssue(alert);
            d.setDecisionType(DecisionType.MANUAL_ACTION.toString()); // default to MANUAL_ACTION
            d.setStatus(DecisionStatusType.OPEN.toString());

            Anomaly an = alert.getAnomaly();
            AnalyzerResult ar = alert.getAnalyzerResult();
            if (ar != null) {
                d.setSourceIPAddress(ar.getSrcIPAddress());
            } else if (an != null) {
                d.setSourceIPAddress(an.getSourceIPAddress());
            }

            entityManager.persist(d);
        } else {
            if (storedState != null) {
                d.setAnomalyState(storedState);
            } else {
                d.setAnomalyState(state);
                entityManager.persist(state);
            }
            entityManager.flush();
        }
        entityManager.getTransaction().commit();

        entityManager.close();
    }
	   
    @SuppressWarnings("unchecked")
    public void setCause(long alertId, Cause cause) {
        EntityManager entityManager = entityManagerFactory.createEntityManager();
        Query query = entityManager.createQuery("SELECT d from Decision d where d.issueId = " + alertId);
        List<Decision> list = query.getResultList();
        Decision d = null;

        if (list != null && !list.isEmpty()) {
            d = list.get(0);
        }

        Cause storedCause = null;
        if (cause.getId() != null && cause.getId() > 0) {
            storedCause = entityManager.find(Cause.class, cause.getId());
        }

        entityManager.getTransaction().begin();
        if (d == null) {
            Alert alert = entityManager.find(Alert.class, alertId);

            d = new Decision();

            if (storedCause != null) {
                d.setCause(storedCause);
            } else {
                d.setCause(cause);
                entityManager.persist(cause);
            }

            d.setIssue(alert);
            d.setDecisionType(DecisionType.MANUAL_ACTION.toString()); // default to MANUAL_ACTION
            d.setStatus(DecisionStatusType.OPEN.toString());

            Anomaly an = alert.getAnomaly();
            AnalyzerResult ar = alert.getAnalyzerResult();
            if (ar != null) {
                d.setSourceIPAddress(ar.getSrcIPAddress());
            } else if (an != null) {
                d.setSourceIPAddress(an.getSourceIPAddress());
            }

            entityManager.persist(d);
        } else {
            if (storedCause != null) {
                d.setCause(storedCause);
            } else {
                d.setCause(cause);
                entityManager.persist(cause);
            }
            entityManager.flush();
        }
        entityManager.getTransaction().commit();

        entityManager.close();
    }
	
	@SuppressWarnings("unchecked")
    public void setClassification(long alertId, Classification classification) {
        EntityManager entityManager = entityManagerFactory.createEntityManager();
        Query query = entityManager.createQuery("SELECT d from Decision d where d.issueId = " + alertId);
        List<Decision> list = query.getResultList();
        Decision d = null;
        
        if (list != null && !list.isEmpty()) {
            d = list.get(0);
        }
        
        Classification storedClassification = null;
        if (classification.getId() > 0) {
            storedClassification = entityManager.find(Classification.class, classification.getId());
        }

        entityManager.getTransaction().begin();
        if (d == null) {
            Alert alert = entityManager.find(Alert.class, alertId);
            
            d = new Decision();
            
            if (storedClassification != null) {
                d.setClassification(storedClassification);
            } else {
                d.setClassification(classification);
            }
            
            d.setIssue(alert);
            d.setDecisionType(DecisionType.MANUAL_ACTION.toString()); // default to MANUAL_ACTION
            d.setStatus(DecisionStatusType.OPEN.toString());

            entityManager.persist(d);
        } else {
            if (storedClassification != null) {
                d.setClassification(storedClassification);
            } else {
                d.setClassification(classification);
            }
            entityManager.flush();
        }
        entityManager.getTransaction().commit();
       
        entityManager.close();
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
