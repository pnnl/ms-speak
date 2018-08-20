/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.persistence;

import java.util.ArrayList;
import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Query;

import com.essence.model.AnalyzerResult;
import com.essence.model.AnalyzerResultStatusType;
import com.essence.model.DetectionRuleType;
import com.essence.model.OrganizationProfile;
import com.essence.model.SeverityType;

public class AnalyzerResultDAO {
	EntityManagerFactory entityManagerFactory;    
	
	public static void main( String[] args)
	{
		AnalyzerResultDAO dao = DAOUtil.getAnalyzerResultDAO();
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
//		List<AnalyzerResult> ars = dao.getAllActiveAnalyzerResults();
//		for (int i=0; ars != null && i<ars.size(); i++) {
//			ars.get(i).print();
//			if (i==0)
//				dao.setSeverityOnAnalyzerResult(ars.get(i), SeverityType.INFORMATIONAL);
//			if (i==1)
//				dao.setSeverityOnAnalyzerResult(ars.get(i), SeverityType.HIGH);
//			if (i==2)
//				dao.setSeverityOnAnalyzerResult(ars.get(i), SeverityType.MEDIUM);
//		}
//
//		ars = dao.getAllActiveAnalyzerResults();
//		for (int i=0; ars != null && i<ars.size(); i++) {
//			ars.get(i).print();
//			if (i==0)
//				dao.setSeverityOnAnalyzerResult(ars.get(i), null);
//		}
//
//		ars = dao.getAllActiveAnalyzerResults();
//		for (int i=0; ars != null && i<ars.size(); i++)
//			ars.get(i).print();

		return;
	}

//	public void addAnalyzerResult(AnalyzerResult r)
//	{
////		if (r.getOrganizationId() <= 0) { // add to active organization
////		  // add active organization to rule
////		  OrganizationDAO pd = DAOUtil.getOrganizationDAO();
////		  List<OrganizationProfile> os = pd.getAllActiveOrganizations();
////		  assert(os != null && !os.isEmpty());
////		  r.setOrganizationId(os.get(0).getId());
////		}
//
//		EntityManager entityManager = entityManagerFactory.createEntityManager();
//		entityManager.getTransaction().begin();
//		entityManager.persist(r);
//		entityManager.getTransaction().commit();
//		entityManager.close();
//	}

//	public void setSeverityOnAnalyzerResult(AnalyzerResult ar, SeverityType severity)
//	{
//		EntityManager entityManager = entityManagerFactory.createEntityManager();
//		entityManager.getTransaction().begin();
//		Query query = null;
//		if (severity == null)
//			query = entityManager.createNativeQuery("update analyzer_result set severity=null where id = " + ar.getId());
//		else
//			query = entityManager.createNativeQuery("update analyzer_result set severity = '" + severity.toString() + "' where id = " + ar.getId());
//		query.executeUpdate();
//		entityManager.getTransaction().commit();
//		entityManager.close();
//	}

//	public void updateStatus(AnalyzerResult ar, AnalyzerResultStatusType type)    
//	{              
//		EntityManager entityManager = entityManagerFactory.createEntityManager();
//		entityManager.getTransaction().begin();
//		Query query = null;
//		if (ar != null && type != null)
//			query = entityManager.createNativeQuery("update analyzer_result set status = '" + type.toString() + "' where id = " + ar.getId()); 
//		query.executeUpdate();
//		entityManager.getTransaction().commit();
//		entityManager.close();
//	}    

//	public void removeAnalyzerResult(AnalyzerResult r)
//	{
//		EntityManager entityManager = entityManagerFactory.createEntityManager();
//		entityManager.getTransaction().begin();
//		// inefficient implementation
//		entityManager.remove(entityManager.find(AnalyzerResult.class, r.getId()));
//		entityManager.getTransaction().commit();
//		entityManager.close();
//	}
//
//	public AnalyzerResult getAnalyzerResultById(long id )
//	{
//		EntityManager entityManager = entityManagerFactory.createEntityManager();
//		AnalyzerResult rule = entityManager.find(AnalyzerResult.class, id);
//		return rule;
//	}
	
//	@SuppressWarnings("unchecked")
//	@Deprecated
//	public List<AnalyzerResult> getAllAnalyzerResults1()
//	{
//		EntityManager entityManager = entityManagerFactory.createEntityManager();
//		Query query = entityManager.createQuery("SELECT ar from AnalyzerResult ar");
//
//		List<AnalyzerResult> list = query.getResultList();
//		entityManager.close();
//		return list;
//	}

//    @SuppressWarnings("unchecked")
//	public List<AnalyzerResult> getAllActiveAnalyzerResults()
//	{
//        EntityManager entityManager = entityManagerFactory.createEntityManager();
//        Query query = entityManager.createQuery("SELECT ar from AnalyzerResult ar");
//
//        List<AnalyzerResult> list = query.getResultList();
//        entityManager.close();
//        return list;
//
//		  // retrieve rules only for active organization
////		  OrganizationDAO pd = DAOUtil.getOrganizationDAO();
////		  List<OrganizationProfile> os = pd.getAllActiveOrganizations();
////		  List<AnalyzerResult> activeARs = new ArrayList<AnalyzerResult>();
////
////		  for (OrganizationProfile p : os) {
////			  activeARs.addAll(getAllAnalyzerResultsByOrganization(p.getId()));
////		  }
////
////		  return activeARs;
//	}

//	@SuppressWarnings("unchecked")
//	public List<AnalyzerResult> getAllAnalyzerResultsByOrganization(int orgId)
//	{
//		EntityManager entityManager = entityManagerFactory.createEntityManager();
//		Query query = entityManager.createQuery("SELECT ar from AnalyzerResult ar where ar.organizationId = " + orgId);
//
//		List<AnalyzerResult> list = query.getResultList();
//		entityManager.close();
//		return list;
//	}
//
//	@SuppressWarnings("unchecked")
//	@Deprecated
//	public List<AnalyzerResult> getAnalyzerResultsByType1(DetectionRuleType type)
//	{
//		EntityManager entityManager = entityManagerFactory.createEntityManager();
//		Query query = entityManager.createQuery("SELECT ar from AnalyzerResult ar where ar.detectorType = '" + type.toString() + "'");
//
//		List<AnalyzerResult> list = query.getResultList();
//		entityManager.close();
//		return list;
//	}
//
//	public List<AnalyzerResult> getActiveAnalyzerResultsByType(DetectionRuleType type)
//	{
//		  // retrieve rules only for active organization
//		  OrganizationDAO pd = DAOUtil.getOrganizationDAO();
//		  List<OrganizationProfile> os = pd.getAllActiveOrganizations();
//		  List<AnalyzerResult> activeARs = new ArrayList<AnalyzerResult>();
//		  for (OrganizationProfile p : os) {
//			  activeARs.addAll(getAnalyzerResultsByTypeAndOrganization(type, p.getId()));
//		  }
//
//		  return activeARs;
//	}

//	@SuppressWarnings("unchecked")
//	public List<AnalyzerResult> getAnalyzerResultsByTypeAndOrganization(DetectionRuleType type, int orgId)
//	{
//		EntityManager entityManager = entityManagerFactory.createEntityManager();
//		Query query = entityManager.createQuery("SELECT ar from AnalyzerResult ar where ar.detectorType = '" + type.toString() + "' and ar.organizationId = " + orgId);
//
//		List<AnalyzerResult> list = query.getResultList();
//		entityManager.close();
//		return list;
//	}

//	@SuppressWarnings("unchecked")
//	@Deprecated
//	public List<AnalyzerResult> getAnalyzerResultsByStatus1(AnalyzerResultStatusType type)
//	{
//		EntityManager entityManager = entityManagerFactory.createEntityManager();
//		Query query = entityManager.createQuery("SELECT ar from AnalyzerResult ar where ar.status = '" + type.toString() + "'");
//
//		List<AnalyzerResult> list = query.getResultList();
//		entityManager.close();
//		return list;
//	}
//
//	public List<AnalyzerResult> getActiveAnalyzerResultsByStatus(AnalyzerResultStatusType type)
//	{
//		  // retrieve rules only for active organization
//		  OrganizationDAO pd = DAOUtil.getOrganizationDAO();
//		  List<OrganizationProfile> os = pd.getAllActiveOrganizations();
//		  List<AnalyzerResult> activeARs = new ArrayList<AnalyzerResult>();
//		  for (OrganizationProfile p : os) {
//			  activeARs.addAll(getAnalyzerResultsByStatusAnOrganization(type, p.getId()));
//		  }
//
//		  return activeARs;
//	}

//	@SuppressWarnings("unchecked")
//	public List<AnalyzerResult> getAnalyzerResultsByStatusAnOrganization(AnalyzerResultStatusType type, int orgId)
//	{
//		EntityManager entityManager = entityManagerFactory.createEntityManager();
//		Query query = entityManager.createQuery("SELECT ar from AnalyzerResult ar where ar.status = '" + type.toString() + "' and ar.organizationId = " + orgId);
//
//		List<AnalyzerResult> list = query.getResultList();
//		entityManager.close();
//		return list;
//	}

	public EntityManagerFactory getEntityManagerFactory()    
	{        
		return entityManagerFactory;    
	}    
	
	public void setEntityManagerFactory(EntityManagerFactory entityManagerFactory)    
	{        
		this.entityManagerFactory = entityManagerFactory;    
	}    
}
