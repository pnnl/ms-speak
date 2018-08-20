/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.persistence;

import java.util.ArrayList;
import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Query;

import com.essence.multispeak.MSPServiceOperation;
import com.essence.multispeak.MSPServiceOperationKey;
import com.essence.ui.shared.Validator;

//@SuppressWarnings("unused")
public class MSPServiceOperationDAO {
	EntityManagerFactory entityManagerFactory;    
	
	public static void main( String[] args)
	{
		MSPServiceOperationDAO dao = DAOUtil.getMSPServiceOperationDAO();
		/*
		MSPServiceOperation service = new MSPServiceOperation();	
		MSPServiceOperationKey key = new MSPServiceOperationKey();
		
		key.setServiceName("AM_Server");
		key.setOperationName("CreatePANDeviceGroup2");
		service.setServicePK(key);
		service.setInputMessage("CreatePANDeviceGroupSoapIn");
		service.setOutputMessage("CreatePANDeviceGroupSoapOut");
		service.setServiceCodeFromName(key.getServiceName());
		service.setSoapAction("http://www.multispeak.org/Version_5.0_Release/CreatePANDeviceGroup");
		service.setSoapHeaderMessage("MultiSpeakRequestMsgHeader");
		service.setSoapHeaderPart("MultiSpeakRequestMsgHeader");
		dao.addMSPService(service);
		*/
		/*
		List<MSPServiceOperation> services = dao.getAllMSPServiceOperations();
		for (int i=0; services != null && i<services.size(); i++)
			services.get(i).print();
			*/
		List<String> cds = dao.getEndpointCodes("v503");
		for (String cd : cds)
			System.out.println(cd);
		List<String> cds3 = dao.getEndpointCodes("v3ac");
		for (String cd : cds3)
			System.out.println(cd);
		
		List<String> msgs = dao.getEndpointMessages(cds.get(3), "v503");
		for (String msg : msgs)
			System.out.println(msg);

		List<String> msgs3 = dao.getEndpointMessages(cds3.get(0), "v3ac");
		for (String msg : msgs3)
			System.out.println(msg);

		return;
	}

	public void addMSPService(MSPServiceOperation s)    
	{              
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		entityManager.persist(s);
		entityManager.getTransaction().commit();
		entityManager.close();
	}    
	
	public void removeMSPService(MSPServiceOperation s)    
	{              
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		// inefficient implementation
		entityManager.remove(entityManager.find(MSPServiceOperation.class, s.getServicePK()));
		entityManager.getTransaction().commit();
		entityManager.close();
	}    
	
	public MSPServiceOperation getMSPServiceId(MSPServiceOperationKey id)    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		MSPServiceOperation service = entityManager.find(MSPServiceOperation.class, id);        
		return service;    
	}    
	
	@SuppressWarnings("unchecked")    
	public List<MSPServiceOperation> getAllMSPServiceOperations()    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT o from MSPServiceOperation o");	

		List<MSPServiceOperation> list = query.getResultList();       
		entityManager.close();
		return list;    
	}    

	@SuppressWarnings("unchecked")    
	public List<String> getEndpointCodes(String version)    
	{        
		if (!Validator.validateMultiSpeakVersion(version))
			return null;
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createNativeQuery("select distinct service_cd from msp_service_op where version = '" + version + "'");	
		List<String> list = query.getResultList();       
		entityManager.close();
		return list;    
	}    

	@SuppressWarnings("unchecked")    
	public List<String> getEndpointMessages(String epCode, String version)    
	{        
		if (!Validator.validateMultiSpeakEndpointCode(epCode) || !Validator.validateMultiSpeakVersion(version))
			return null;
		
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createNativeQuery("select * from msp_service_op where service_cd = '" + epCode + "' and version = '" + version + "' order by input_msg", MSPServiceOperation.class);	
		List<MSPServiceOperation> list = query.getResultList();       
		entityManager.close();
		List<String> msgs = new ArrayList<String>();
		for (MSPServiceOperation op : list) {
			msgs.add(op.getInputMessage());
			msgs.add(op.getOutputMessage());
		}
			
		return msgs;    
	}    

	/*
	@SuppressWarnings("unchecked")    
	public List<MSPService> getMSPServicesByType(DetectionRuleType type)    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT ar from AnalyzerResult ar where ar.detectorType = '" + type.toString() + "'");	

		List<AnalyzerResult> list = query.getResultList();       
		entityManager.close();
		return list;    
	}    
	*/

	public EntityManagerFactory getEntityManagerFactory()    
	{        
		return entityManagerFactory;    
	}    
	
	public void setEntityManagerFactory(EntityManagerFactory entityManagerFactory)    
	{        
		this.entityManagerFactory = entityManagerFactory;    
	}    
}
