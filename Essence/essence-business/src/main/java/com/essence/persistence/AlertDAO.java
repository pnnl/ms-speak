/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.persistence;

import java.sql.SQLException;
import java.util.*;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Query;
import javax.persistence.TypedQuery;

import com.essence.alert.AlertCount;
import com.essence.model.*;
import org.hibernate.Hibernate;

public class AlertDAO {
	EntityManagerFactory entityManagerFactory;    
	
	public static void main( String[] args)
	{
		AlertDAO dao = DAOUtil.getAlertDAO();
		/*
	for (int i=0; i<30; i++) {	
		AnalyzerResult ar = new AnalyzerResult();
		ar.setDescription("test description1");
		ar.setDetectorType(DetectionRuleType.MS_EP_CONNECTIVITY.toString());
		ar.setDstIPAddress("192.168.1.1");
		ar.setNumberOfPacketsForDoS(23);
		ar.setRunTime(System.currentTimeMillis());
		ar.setTimeWindowInSeconds(900l);
		ar.setRefRuleId(5);
		ar.setStatus(AnalyzerResultStatusType.OPEN);
		dao.addAnalyzerResult(ar);
		
		AnalyzerResult ar1 = new AnalyzerResult();
		ar1.setDescription("test description2");
		ar1.setDetectorType(DetectionRuleType.MS_EP_CONNECTIVITY.toString());
		ar1.setDstIPAddress("192.168.1.1");
		ar1.setNumberOfPacketsForDoS(25);
		ar1.setRunTime(System.currentTimeMillis());
		ar1.setTimeWindowInSeconds(900l);
		ar1.setRefRuleId(6);
		ar1.setStatus(AnalyzerResultStatusType.OPEN);
		dao.addAnalyzerResult(ar1);
		
		AnalyzerResult ar2 = new AnalyzerResult();
		ar2.setDescription("test description3");
		ar2.setDetectorType(DetectionRuleType.MS_EP_CONNECTIVITY.toString());
		ar2.setDstIPAddress("192.168.1.1");
		ar2.setNumberOfPacketsForDoS(33);
		ar2.setRunTime(System.currentTimeMillis());
		ar2.setTimeWindowInSeconds(900l);
		ar2.setRefRuleId(7);
		ar2.setStatus(AnalyzerResultStatusType.OPEN);
		dao.addAnalyzerResult(ar2);
	}
*/
		List<Alert> alerts = dao.getAllActiveAlerts();
		for (int i=0; alerts != null && i<alerts.size(); i++) {
		    alerts.get(i).print();
			if (i==0)
				dao.setSeverityOnAlert(alerts.get(i), SeverityType.INFORMATIONAL);
			if (i==1)
				dao.setSeverityOnAlert(alerts.get(i), SeverityType.HIGH);
			if (i==2)
				dao.setSeverityOnAlert(alerts.get(i), SeverityType.MEDIUM);
		}

		alerts = dao.getAllActiveAlerts();
		for (int i=0; alerts != null && i<alerts.size(); i++) {
		    alerts.get(i).print();
			if (i==0)
				dao.setSeverityOnAlert(alerts.get(i), null);
		}

		alerts = dao.getAllActiveAlerts();
		for (int i=0; alerts != null && i<alerts.size(); i++) 
		    alerts.get(i).print();
	}

	public Long addAlert(Alert a)    
	{
		if (a.getOrganizationId() <= 0) { // add to active organization
		  // add active organization to rule
		  OrganizationDAO pd = DAOUtil.getOrganizationDAO();
		  List<OrganizationProfile> os = pd.getAllActiveOrganizations();
		  assert(os != null && !os.isEmpty());
		  a.setOrganizationId(os.get(0).getId());
		}

		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
        if (a.getAnalyzerResult() != null) {
            a.getAnalyzerResult().setAlert(a);
            //entityManager.persist(a.getAnalyzerResult());
        }
        if (a.getAnomaly() != null) {
            a.getAnomaly().setAlert(a);
            //entityManager.persist(a.getAnomaly());
        }
		entityManager.persist(a);
        entityManager.flush();
		entityManager.getTransaction().commit();
		entityManager.close();
		
		return a.getId();
	}

	public void setSeverityOnAlert(Alert a, SeverityType severity)    
	{
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		Query query;
		if (a != null && severity == null)
			query = entityManager.createNativeQuery("update alert set severity=null where id = " + a.getId());
		else
			query = entityManager.createNativeQuery("update alert set severity = '" + severity.toString() + "' where id = " + a.getId()); 
		query.executeUpdate();
		entityManager.getTransaction().commit();
		entityManager.close();
	}

	public void updateStatus(Alert a, AnalyzerResultStatusType type)    
	{   
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		Query query = null;
		if (a != null && type != null)
			query = entityManager.createNativeQuery("update alert set status = '" + type.toString() + "' where id = " + a.getId()); 
		query.executeUpdate();
		entityManager.getTransaction().commit();
		entityManager.close();
	}

	public void removeAlert(Alert a)    
	{
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		// inefficient implementation
		entityManager.remove(entityManager.find(Alert.class, a.getId()));
		entityManager.getTransaction().commit();
		entityManager.close();
	}
	
	public Alert getAlertById(long id)
	{
        EntityManager entityManager = entityManagerFactory.createEntityManager();
        String q = "SELECT a from Alert a left join fetch a.anomaly an left join fetch a.analyzerResult" +
                " left join fetch a.anomaly.normalEntries left join fetch a.anomaly.anomalyEntries" +
                " left join fetch a.anomaly.patternIndex left join fetch a.anomaly.predictions" +
                //" left join fetch a.anomaly.filterTypes left join fetch a.anomaly.filters left join fetch a.anomaly.featureTypes" +
                " where a.id = " + id;
        Query query = entityManager.createQuery(q);


        List<Alert> list = query.getResultList();
        Alert alert = list.get(0);
        Anomaly a = alert.getAnomaly();
        if (a != null) {
            Hibernate.initialize(a.getAnomalyEntries());
            Hibernate.initialize(a.getNormalEntries());
            Hibernate.initialize(a.getPatternIndex());
            Hibernate.initialize(a.getPredictions());
        }

        entityManager.close();
        return list.get(0);
	}

	public List<Alert> getAllActiveAlerts()
	{        
		  // retrieve alerts only for active organization
		  OrganizationDAO pd = DAOUtil.getOrganizationDAO();
		  List<OrganizationProfile> os = pd.getAllActiveOrganizations();
		  List<Alert> activeAlerts = new ArrayList<>();
		  for (OrganizationProfile p : os) {
		      activeAlerts.addAll(getAllAlertsByOrganization(p.getId()));
		  }

		  return activeAlerts;
	}

    public List<Alert> getAllActiveAlertsByIP(String ip, boolean loadCollections)
    {        
          // retrieve alerts only for active organization
          OrganizationDAO pd = DAOUtil.getOrganizationDAO();
          List<OrganizationProfile> os = pd.getAllActiveOrganizations();
          List<Alert> activeAlerts = new ArrayList<Alert>();
          for (OrganizationProfile p : os) {
              activeAlerts.addAll(getAllAlertsByOrganizationAndIP(p.getId(), ip, loadCollections));
          }

          return activeAlerts;
    }

	@SuppressWarnings("unchecked")
	public List<Alert> getAllAlertsByOrganization(int orgId)
	{
		EntityManager entityManager = entityManagerFactory.createEntityManager();
        String q = "SELECT a from Alert a left join fetch a.anomaly left join fetch a.analyzerResult" +
                " where a.organizationId = " + orgId;
		Query query = entityManager.createQuery(q);
		List<Alert> list = query.getResultList();
		entityManager.close();
		return list;
	}

    public List<Alert> getAllAnomalyAlerts()
    {
        // retrieve alerts only for active organization
        OrganizationDAO pd = DAOUtil.getOrganizationDAO();
        List<OrganizationProfile> os = pd.getAllActiveOrganizations();
        List<Alert> activeAlerts = new ArrayList<>();
        for (OrganizationProfile p : os) {
            activeAlerts.addAll(getAllAnomalyAlertsByOrganization(p.getId()));
        }

        return activeAlerts;
    }

    @SuppressWarnings("unchecked")
    public List<Alert> getAllAnomalyAlertsByOrganization(int orgId)
    {
        EntityManager entityManager = entityManagerFactory.createEntityManager();
        String q = "SELECT a from Alert a join fetch a.anomaly left join fetch a.analyzerResult" +
                " where a.organizationId = " + orgId;
        Query query = entityManager.createQuery(q);
        List<Alert> list = query.getResultList();
        entityManager.close();
        return list;
    }
	
    @SuppressWarnings("unchecked")
    public Alert getAlertByAnomalyId(long anomalyId)
    {
        EntityManager entityManager = entityManagerFactory.createEntityManager();
        Query query = entityManager.createQuery("SELECT a from Alert a left join fetch a.anomaly" +
                " left join fetch a.anomaly.normalEntries left join fetch a.anomaly.anomalyEntries" +
                " left join fetch a.anomaly.patternIndex left join fetch a.anomaly.predictions" +
                //" left join fetch a.anomaly.filterTypes left join fetch a.anomaly.filters left join fetch a.anomaly.featureTypes" +
                " where a.anomaly IS NOT NULL AND a.anomaly.id = '" + anomalyId + "'");

        List<Alert> list = query.getResultList();
        entityManager.close();
        if (list.size() > 0) {
            return list.get(0);
        }
        return null;
    }
	
    @SuppressWarnings("unchecked")
    public List<Alert> getAllAlertsByOrganizationAndIP(int orgId, String ip, boolean loadCollections)
    {
        EntityManager entityManager = entityManagerFactory.createEntityManager();
        
        // TODO: fix this so it's one query rather than two?
        //Query query = entityManager.createQuery("SELECT a from Alert a where a.organizationId = " + orgId +
        //        " AND ((a.anomaly IS NOT NULL AND a.anomaly.sourceType = 1 AND a.anomaly.sourceValue = '" + ip + "') OR" +
        //        " (a.analyzerResult IS NOT NULL AND a.analyzerResult.srcIPAddress = '" + ip + "'))");
        String query1 = "SELECT a from Alert a join fetch a.anomaly an";
        if (loadCollections) {
            query1 += " join fetch a.anomaly.normalEntries join fetch a.anomaly.anomalyEntries" +
                    " join fetch a.anomaly.patternIndex join fetch a.anomaly.predictions";
                    //" left join fetch a.anomaly.filterTypes left join fetch a.anomaly.filters left join fetch a.anomaly.featureTypes";
        }
        query1 += " left join fetch a.analyzerResult where a.organizationId = " + orgId +
                " AND a.anomaly.sourceValue = '" + ip + "'";
        Query anomalyQuery = entityManager.createQuery(query1);
        
//        Query analyzerQuery = entityManager.createQuery("SELECT a from Alert a " +
//				(loadCollections ? "fetch all properties" : "") + " where a.organizationId = " + orgId +
//				" AND a.analyzerResult IS NOT NULL AND a.analyzerResult.srcIPAddress = '" + ip + "'");
        String query = "SELECT a from Alert as a " +
                " join fetch a.analyzerResult left join fetch a.anomaly where a.organizationId = " + orgId +
                " AND a.analyzerResult.srcIPAddress = '" + ip + "'";
        //String query = "SELECT a from Alert as a left join fetch a.analyzerResult as ar left join fetch a.anomaly as an" +
        //        " with (ar.srcIPAddress = '" + ip + "' OR an.sourceValue = '" + ip + "') " +
                //" left join an.normalEntries left join an.anomalyEntries left join an.patternIndex left join an.predictions " +
        //        " where a.organizationId = " + orgId;// +
                //" AND (a.analyzerResult.srcIPAddress = '" + ip + "' OR a.anomaly.sourceValue = '" + ip + "')";
        Query analyzerQuery = entityManager.createQuery(query);


        long lStartTime = System.nanoTime();
        List<Alert> list = anomalyQuery.getResultList();
        long lEndTime = System.nanoTime();
        long difference = lEndTime - lStartTime;
        System.out.println("Anomaly Query Elapsed milliseconds: " + difference/1000000);
        lStartTime = System.nanoTime();
        List<Alert> analyzerAlertList = analyzerQuery.getResultList();
        lEndTime = System.nanoTime();
        difference = lEndTime - lStartTime;
        System.out.println("AnalyzerResult Query Elapsed milliseconds: " + difference/1000000);
        list.addAll(analyzerAlertList);
        entityManager.close();
        return list;
    }

	//@SuppressWarnings("unchecked")
	public List<Alert> getActiveAlertsByStatus(AnalyzerResultStatusType type)
	{
		  // retrieve rules only for active organization
		  OrganizationDAO pd = DAOUtil.getOrganizationDAO();
		  List<OrganizationProfile> os = pd.getAllActiveOrganizations();
		  List<Alert> activeAlerts = new ArrayList<Alert>();
		  for (OrganizationProfile p : os) {
		      activeAlerts.addAll(getAlertsByStatusAndOrganization(type, p.getId()));
		  }

		  return activeAlerts;
	}

	@SuppressWarnings("unchecked")
	public List<Alert> getAlertsByStatusAndOrganization(AnalyzerResultStatusType type, int orgId)
	{
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		Query query = entityManager.createQuery("SELECT a from Alert a" +
                " left join fetch a.anomaly left join fetch a.analyzerResult" +
                " where a.status = '" + type.toString() + "' and a.organizationId = " + orgId);

		List<Alert> list = query.getResultList();  
		entityManager.close();
		return list;
	}

    @SuppressWarnings("unchecked")
    public List<Alert> getActiveAlertsByType(DetectionRuleType type)
    {
        // retrieve rules only for active organization
        OrganizationDAO pd = DAOUtil.getOrganizationDAO();
        List<OrganizationProfile> os = pd.getAllActiveOrganizations();
        List<Alert> alerts = new ArrayList<>();
        for (OrganizationProfile p : os) {
            alerts.addAll(getAlertsByTypeAndOrganization(type, p.getId()));
        }

        return alerts;
    }

    @SuppressWarnings("unchecked")
    public List<Alert> getAlertsByTypeAndOrganization(DetectionRuleType type, int orgId)
    {
        EntityManager entityManager = entityManagerFactory.createEntityManager();
        Query query = entityManager.createQuery("SELECT a from Alert a join fetch a.analyzerResult" +
                " left join fetch a.anomaly" +
                " where a.analyzerResult.detectorType = '" + type.toString() + "' and a.organizationId = " + orgId);

        List<Alert> list = query.getResultList();
        entityManager.close();
        return list;
    }

    @SuppressWarnings("unchecked")
    public List<AlertCount> getAlertCountByIPAddress() throws SQLException
	{
        EntityManager entityManager = entityManagerFactory.createEntityManager();
        Query query = entityManager.createNamedQuery("alertCountQuery");
        List<AlertCount> list = query.getResultList();
        
//	    Connection conn = DriverManager.getConnection("jdbc:mysql://10.21.1.24:3306/essence2", "essence", "password");
//	    //Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/essence", "essence", "password");
//	    Statement st = conn.createStatement();
//	    ResultSet results = st.executeQuery("call GetAlertCountByIP");
//	    
//	    List<AlertCount> list = new ArrayList<AlertCount>();
//	    
//	    while (results.next())
//	    {
//	        AlertCount ip = new AlertCount();
//	        ip.setCount(results.getLong("count"));
//	        ip.setIpAddress(results.getString("ip"));
//	        list.add(ip);
//	    }
	    
	    return list;
	}

    public List<AnomalyState> getAnomalyStates(Date trainingTimeWindowStart, Date trainingTimeWindowEnd,
                                                  int sourceType, int targetType, String algorithm) {
        List<AnomalyState> states = null;

        EntityManager entityManager = entityManagerFactory.createEntityManager();
//      CriteriaBuilder b = entityManager.getCriteriaBuilder();
//      CriteriaQuery<Alert> query = b.createQuery(Alert.class);
//      Root<Alert> root = query.from(Alert.class);
//      query.select(root);
//      Join<Alert, Anomaly> anomaly = root.join("anomaly");
//
//      Subquery<Anomaly> subquery = query.subquery(Anomaly.class)

        Map<String, Object> parameters = new HashMap<String, Object>();

        String query = "SELECT DISTINCT d.anomalyState FROM Decision d LEFT JOIN d.issue i LEFT JOIN i.anomaly an WHERE ";

        if (trainingTimeWindowStart != null) {
            if (parameters.size() > 0) {
                query += " AND ";
            }
            query += "trainingTimeWindowStart <= :trainingTimeWindowStart";
            parameters.put("trainingTimeWindowStart", trainingTimeWindowStart);
        }

        if (trainingTimeWindowEnd != null) {
            if (parameters.size() > 0) {
                query += " AND ";
            }
            query += "trainingTimeWindowEnd <= :trainingTimeWindowEnd";
            parameters.put("trainingTimeWindowEnd", trainingTimeWindowEnd);
        }

        if (sourceType > 0) {
            if (parameters.size() > 0) {
                query += " AND ";
            }
            query += "sourceType = :sourceType";
            parameters.put("sourceType", sourceType);
        }

        if (targetType > 0) {
            if (parameters.size() > 0) {
                query += "  AND ";
            }
            query += "targetType = :targetType";
            parameters.put("targetType", targetType);
        }

        if (algorithm != null) {
            if (parameters.size() > 0) {
                query += "  AND ";
            }
            query += "algorithm = :algorithm";
            parameters.put("algorithm", algorithm);
        }
        
        if (parameters.size() <= 0) {
            query = "SELECT DISTINCT d.anomalyState FROM Decision d LEFT JOIN d.issue i LEFT JOIN i.anomaly";
            TypedQuery<AnomalyState> q = entityManager.createQuery(query, AnomalyState.class);
            return q.getResultList();
        }

        TypedQuery<AnomalyState> q = entityManager.createQuery(query, AnomalyState.class);

        Iterator it = parameters.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry item = (Map.Entry)it.next();
            q.setParameter((String) item.getKey(), item.getValue());
        }

        states = q.getResultList();

        return states;
    }
    

    public List<Cause> getCauses(Date trainingTimeWindowStart, Date trainingTimeWindowEnd,
                                                  int sourceType, int targetType, String algorithm) {
        List<Cause> causes = null;

        EntityManager entityManager = entityManagerFactory.createEntityManager();
//      CriteriaBuilder b = entityManager.getCriteriaBuilder();
//      CriteriaQuery<Alert> query = b.createQuery(Alert.class);
//      Root<Alert> root = query.from(Alert.class);
//      query.select(root);
//      Join<Alert, Anomaly> anomaly = root.join("anomaly");
//
//      Subquery<Anomaly> subquery = query.subquery(Anomaly.class)

        Map<String, Object> parameters = new HashMap<String, Object>();

        String query = "SELECT DISTINCT d.cause FROM Decision d LEFT JOIN d.issue i LEFT JOIN i.anomaly an WHERE ";

        if (trainingTimeWindowStart != null) {
            if (parameters.size() > 0) {
                query += " AND ";
            }
            query += "trainingTimeWindowStart <= :trainingTimeWindowStart";
            parameters.put("trainingTimeWindowStart", trainingTimeWindowStart);
        }

        if (trainingTimeWindowEnd != null) {
            if (parameters.size() > 0) {
                query += " AND ";
            }
            query += "trainingTimeWindowEnd <= :trainingTimeWindowEnd";
            parameters.put("trainingTimeWindowEnd", trainingTimeWindowEnd);
        }

        if (sourceType > 0) {
            if (parameters.size() > 0) {
                query += " AND ";
            }
            query += "sourceType = :sourceType";
            parameters.put("sourceType", sourceType);
        }

        if (targetType > 0) {
            if (parameters.size() > 0) {
                query += "  AND ";
            }
            query += "targetType = :targetType";
            parameters.put("targetType", targetType);
        }

        if (algorithm != null) {
            if (parameters.size() > 0) {
                query += "  AND ";
            }
            query += "algorithm = :algorithm";
            parameters.put("algorithm", algorithm);
        }
        
        if (parameters.size() <= 0) {
            query = "SELECT DISTINCT d.cause FROM Decision d LEFT JOIN d.issue i LEFT JOIN i.anomaly";
            TypedQuery<Cause> q = entityManager.createQuery(query, Cause.class);
            return q.getResultList();
        }

        TypedQuery<Cause> q = entityManager.createQuery(query, Cause.class);

        Iterator it = parameters.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry item = (Map.Entry)it.next();
            q.setParameter((String) item.getKey(), item.getValue());
        }

        causes = q.getResultList();

        return causes;
    }

	public List<Alert> getAlertsByAnomalyCriteria(Date detectionTimeWindowStart, Date detectionTimeWindowEnd,
												  Date trainingTimeWindowStart, Date trainingTimeWindowEnd,
												  String sourceValue, int targetType, String algorithm) {
		List<Alert> alerts = null;

		EntityManager entityManager = entityManagerFactory.createEntityManager();
//		CriteriaBuilder b = entityManager.getCriteriaBuilder();
//		CriteriaQuery<Alert> query = b.createQuery(Alert.class);
//		Root<Alert> root = query.from(Alert.class);
//		query.select(root);
//		Join<Alert, Anomaly> anomaly = root.join("anomaly");
//
//		Subquery<Anomaly> subquery = query.subquery(Anomaly.class)

		Map<String, Object> parameters = new HashMap<String, Object>();

		String query = "SELECT al FROM Alert al LEFT JOIN FETCH al.anomaly an WHERE ";

		if (detectionTimeWindowStart != null) {
			if (parameters.size() > 0) {
				query += " AND ";
			}
            query += "detectionTimeWindowStart >= :detectionTimeWindowStart";
            parameters.put("detectionTimeWindowStart", detectionTimeWindowStart);
		}

		if (detectionTimeWindowEnd != null) {
			if (parameters.size() > 0) {
				query += " AND ";
			}
			query += "detectionTimeWindowEnd <= :detectionTimeWindowEnd";
			parameters.put("detectionTimeWindowEnd", detectionTimeWindowEnd);
		}

		if (trainingTimeWindowStart != null) {
			if (parameters.size() > 0) {
				query += " AND ";
			}
			query += "trainingTimeWindowStart <= :trainingTimeWindowStart";
			parameters.put("trainingTimeWindowStart", trainingTimeWindowStart);
		}

		if (trainingTimeWindowEnd != null) {
			if (parameters.size() > 0) {
				query += " AND ";
			}
			query += "trainingTimeWindowEnd <= :trainingTimeWindowEnd";
			parameters.put("trainingTimeWindowEnd", trainingTimeWindowEnd);
		}

		if (sourceValue != null) {
			if (parameters.size() > 0) {
				query += " AND ";
			}
			query += "sourceValue = :sourceValue";
			parameters.put("sourceValue", sourceValue);
		}

		if (targetType > 0) {
			if (parameters.size() > 0) {
				query += " 	AND ";
			}
			query += "targetType = :targetType";
			parameters.put("targetType", targetType);
		}

		if (algorithm != null) {
			if (parameters.size() > 0) {
				query += " 	AND ";
			}
			query += "algorithm = :algorithm";
			parameters.put("algorithm", algorithm);
		}

        if (parameters.size() <= 0) {
            //try {
                query = "SELECT al FROM Alert al JOIN FETCH al.anomaly";
                TypedQuery<Alert> q = entityManager.createQuery(query, Alert.class);
                return q.getResultList();
            //}
            //catch (Exception ex) {
            //    throw;
            //}
        }
        
		TypedQuery<Alert> q = entityManager.createQuery(query, Alert.class);

		Iterator it = parameters.entrySet().iterator();
		while (it.hasNext()) {
			Map.Entry item = (Map.Entry)it.next();
			q.setParameter((String) item.getKey(), item.getValue());
		}

        alerts = q.getResultList();

        for (Alert a : alerts) {
            Hibernate.initialize(a.getAnomaly().getPredictions());
            Hibernate.initialize(a.getAnomaly().getPatternIndex());
            Hibernate.initialize(a.getAnomaly().getNormalEntries());
            Hibernate.initialize(a.getAnomaly().getAnomalyEntries());
            Hibernate.initialize(a.getAnomaly().getFilters());
            Hibernate.initialize(a.getAnomaly().getFeatureTypes());
            Hibernate.initialize(a.getAnomaly().getFilterTypes());
        }

		return alerts;
 	}
	
    public Integer deleteAllAlerts() {
        EntityManager entityManager = entityManagerFactory.createEntityManager();
        entityManager.getTransaction().begin();
        Query query1 = entityManager.createQuery("DELETE from AnalyzerResult");
        Query query2 = entityManager.createQuery("DELETE from Anomaly");
        Query query3 = entityManager.createQuery("DELETE from Alert");
        query1.executeUpdate();
        entityManager.flush();
        query2.executeUpdate();
        entityManager.flush();
        int result = query3.executeUpdate();
        entityManager.getTransaction().commit();
        return result;
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