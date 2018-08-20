/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.persistence;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Query;

import org.hibernate.Criteria;
import org.hibernate.HibernateException;
import org.hibernate.SQLQuery;
import org.hibernate.Session;
import org.hibernate.SessionFactory;

import com.essence.multispeak.MSPServiceOperationKey;
import com.essence.model.Xpath;
import com.essence.ui.shared.Validator;

public class MSPXpathDAO {
	EntityManagerFactory entityManagerFactory;   
	/*
	 select count(*) as cnt from msp_xpath where service_cd='NOT' and msg_name='DesignedWorkOrderNotification' and field_name not in ('extName','description','@utility','@identifierLabel','@identifierName','nameString','state','@secondaryIdentifierName','@primaryIdentifierName','@objectGUID','@ts','@cs','@decimal','index','detailedString','@referenceID','displayString','comments','noteValue','noteType','noteSubtype','city','@nounType') and value_type NOT in ('extValue', 'extType','otherKind','QName','objectRef');

	 */
	// Exclude list of field names that are not important for security rules, removed '@objectGUID'
	public static final String FIELD_NAME_EXCLUSION_LIST_CLAUSE_v5 =  "field_name NOT in ('extName','description','@utility','@identifierLabel','@identifierName','state','city','nameString','@secondaryIdentifierName','@primaryIdentifierName','@ts','@cs','@decimal','index','detailedString','@referenceID','displayString','@nounType','postalCode','country','townCode','streetNumber','addressGeneral','address1','address2','streetType','streetPrefix','suiteNumber','region','streetSuffix','postOfficeBox','buildingNumber','township','section','range','quarterSection','districtCode','subdivision','lot','districtName','townshipName','block','noteValue','noteType','noteSubtype','comments','extension','cityCode','localNumber','areaCode','countryCode')";

	// Exclude list of value types that are not important for security rules
	public static final String VALUE_TYPE_EXCLUSION_LIST_CLAUSE_v5 =  "value_type NOT in ('extValue', 'extType','otherKind','QName','objectRef','anyURI')";

	public static void main( String[] args) {
	    @SuppressWarnings("unused")
		long start = System.currentTimeMillis();
		String cd = "NOT";
		String msgName = "WorkOrdersChangedNotification";
	    @SuppressWarnings("unused")
		boolean isArray = false;
		/*
		  System.out.println("*** Called to getXpathsByServiceCDMsgName cd="+cd+" msgName="+msgName+" isArray="+isArray);
		  List<Xpath> result = DAOUtil.getMSPXpathDAO().getXpathsByServiceCDMsgName(cd, msgName, isArray);
		  long check1 = System.currentTimeMillis();
		  System.out.println("*** result size = "+result.size() + " in " + (check1-start) + " ms");
		  result = DAOUtil.getMSPXpathDAO().getXpathsByServiceCDMsgName(cd, msgName, isArray);
		  long check2 = System.currentTimeMillis();
		  System.out.println("*** result size = "+result.size() + " in " + (check2-check1) + " ms");
		  */
		  List<String> valueTypes = DAOUtil.getMSPXpathDAO().getValueTypesByServiceCDMsgName(cd, "v503", msgName);
		  for (String s : valueTypes)
			  System.out.println(s);
		  
		test2();
		return;
	}
	
	static private void test2() {
		System.out.println("Verifying v3ac ...");

		MSPXpathDAO dao = DAOUtil.getMSPXpathDAO();
		List<Xpath> list = dao.getHeaderXpaths(true, "v3ac");
		System.out.println("All header collection Xpath records size = " + list.size());
		for (Xpath p : list)
			p.print();

		list = dao.getHeaderXpaths(false, "v3ac");
		System.out.println("All header non-collection Xpath records size = " + list.size());
		for (Xpath p : list)
			p.print();

		int count = 0;
		list = dao.getXpathsByServiceCDMsgName("OA", "v3ac", "GetDownlineConnectivityResponse", true);
		System.out.println("All collection Xpath records size = " + list.size());
		for (Xpath p : list) {
			p.print();
			if (count++ > 20)
				break;
		}
		
		count = 0;
		list = dao.getXpathsByServiceCDMsgName("OA", "v3ac", "GetDownlineConnectivityResponse", false);
		System.out.println("All non-collection Xpath records size = " + list.size());
		for (Xpath p : list) {
			p.print();
			if (count++ > 50)
				break;
		}
	}
	
	@SuppressWarnings("unused")
    static private void test1() {
		MSPXpathDAO dao = DAOUtil.getMSPXpathDAO();
		Xpath p1 = new Xpath();
		p1.setServiceCode("OD");
		p1.setMessageName("ChangeOutageDetectionDevices");
		p1.setIsArray(false);
		p1.setXpath("/Envelope/Body/ChangeOutageDetectionDevices/ArrayOfOutageDetectionDevice/outageDetectionDevice/assetData/assetHistoryEvents/assetHistoryEvent/assetLocation/GPSLocation/GPSMetadata/number");
		p1.setFieldName("number");
		dao.addXpath(p1);
		
		Xpath p2 = new Xpath();
		p2.setServiceCode("OD");
		p2.setMessageName("ChangeOutageDetectionDevices");
		p2.setIsArray(false);
		p2.setXpath("/Envelope/Body/ChangeOutageDetectionDevices/ArrayOfOutageDetectionDevice/outageDetectionDevice/assetData/assetLocation/extensionsList/extensionsItem/extName");
		p2.setFieldName("extName");
		dao.addXpath(p2);

		Xpath p3 = new Xpath();
		p3.setServiceCode("OD");
		p3.setMessageName("ChangeOutageDetectionDevices");
		p3.setIsArray(true);
		p3.setXpath("/Envelope/Body/ChangeOutageDetectionDevices/ArrayOfOutageDetectionDevice/outageDetectionDevice/assetData/assetLocation/extensionsList/extensionsItem");
		p3.setFieldName("extensionsItem");
		dao.addXpath(p3);

		System.out.println("All records for OD");
		List<Xpath> list = dao.getXpathsByServiceCD("OD");
		for (Xpath p : list)
			p.print();
		
		System.out.println("All records for OD and ChangeOutageDetectionDevices");
		list = dao.getXpathsByServiceCDMsgName("OD", "v503", "ChangeOutageDetectionDevices", true);
		for (Xpath p : list)
			p.print();
		list = dao.getXpathsByServiceCDMsgName("OD", "v503", "ChangeOutageDetectionDevices", false);
		for (Xpath p : list)
			p.print();
		
		System.out.println("All records");
		list = dao.getAllXpaths();
		for (Xpath p : list)
			p.print();

		int id = list.get(0).getId();
		System.out.println("One record for id = " + id);
		Xpath p = dao.getXpathById(id);
		p.print();
	}
	
	public void addXpath(Xpath path)    
	{              
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		entityManager.persist(path);
		entityManager.getTransaction().commit();
		entityManager.close();
	}    

	public void addXpathBatch(List<Xpath> paths)    
	{              
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		for (Xpath p : paths)
			entityManager.persist(p);
		entityManager.getTransaction().commit();
		entityManager.close();
	}    

	public void removeXpath(Xpath path)    
	{              
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		// inefficient implementation
		entityManager.remove(entityManager.find(Xpath.class, path.getId()));
		entityManager.getTransaction().commit();
		entityManager.close();
	}    
	
	public Xpath getXpathById(int id )    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Xpath path = entityManager.find(Xpath.class, id);        
		return path;    
	}    
	
	@SuppressWarnings("unchecked")    
	public List<Xpath> getAllXpaths()    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT path from Xpath path");	

		List<Xpath> list = query.getResultList();       
		entityManager.close();
		return list;    
	}    

	@SuppressWarnings("unchecked")    
	public List<Xpath> getXpathsByServiceCD(String cd)    
	{        
		if (!Validator.validateMultiSpeakEndpointCode(cd))
			return null;
		
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT path from Xpath path where path.serviceCode = '" + cd + "'");	

		List<Xpath> list = query.getResultList();       
		entityManager.close();
		return list;    
	}    

/*
	@SuppressWarnings("unchecked")    
	public List<Xpath> getXpathsByServiceCDMsgName(String cd, String msgName)    
	{        
		if (!Validator.validateMultiSpeakEndpointCode(cd) || !Validator.validateAlphaNumericOnly(msgName))
			return null;
		
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT path from Xpath path where path.serviceCode = '" + cd + "' and path.messageName ='" + msgName + "'");	

		List<Xpath> list = query.getResultList();       
		entityManager.close();
		return list;    
	}    
	*/

	@SuppressWarnings("unchecked")    
	public List<Xpath> getXpathsByServiceCDMsgName(String cd, String version, String msgName, Boolean isArray)    
	{        
		if (!Validator.validateMultiSpeakEndpointCode(cd) || !Validator.validateAlphaNumericOnly(msgName) || !Validator.validateMultiSpeakVersion(version))
			return null;
		
		EntityManager entityManager = entityManagerFactory.createEntityManager();       
		String qString = null;
		
		if (version.equals(MSPServiceOperationKey.SUPPORTED_VERSION_5))
			qString = "SELECT path from Xpath path where path.serviceCode = '" + cd + "' and version = '" + version + "' and path.messageName ='" + msgName + "' and path.isArray =" + isArray + " and " + FIELD_NAME_EXCLUSION_LIST_CLAUSE_v5 + " and " + VALUE_TYPE_EXCLUSION_LIST_CLAUSE_v5 + " order by path.fieldName";
		else
			qString = "SELECT path from Xpath path where path.serviceCode = '" + cd + "' and version = '" + version + "' and path.messageName ='" + msgName + "' and path.isArray =" + isArray + " order by path.fieldName";
			
		System.out.println("qString = " + qString);
		Query query = entityManager.createQuery(qString);	

		List<Xpath> list = query.getResultList();       
		entityManager.close();
		return list;    
	}    


	@SuppressWarnings("rawtypes")    
	public List<String> getValueTypesByServiceCDMsgName(String cd, String version, String msgName)    
	{        
		if (!Validator.validateMultiSpeakEndpointCode(cd) || !Validator.validateAlphaNumericOnly(msgName) || !Validator.validateMultiSpeakVersion(version))
			return null;
		
		SessionFactory f = HibernateUtil.getSessionFactory();
	    Session session = f.openSession();
	    List<String> list = new ArrayList<String>();
	  //    Transaction tx = null;
	      try{
	    //     tx = session.beginTransaction();
	         String sql = "select distinct value_type from msp_xpath where service_cd='" + cd + "' and version = '" + version + "' and msg_name='" + msgName + "'";
	         SQLQuery query = session.createSQLQuery(sql);
	         query.setResultTransformer(Criteria.ALIAS_TO_ENTITY_MAP);
	          List result = query.list();
	          for (Object o : result) {
	        	  Map row = (Map)o;
	        	  list.add((String)row.get("value_type"));
	          }
	    //     tx.commit();
	      }catch (HibernateException e) {
	        // if (tx!=null) tx.rollback();
	         e.printStackTrace(); 
	      }finally {
	         session.close(); 
	      }
		return list;    
	}    

	private static List<Xpath> HEADER_XPATHS_NON_GROUP = null;
	private static List<Xpath> HEADER_XPATHS_GROUP = null;
	private static String VERSION4HEADER = null;
	
	@SuppressWarnings("unchecked")    
	public List<Xpath> getHeaderXpaths(Boolean isArray, String version)    
	{        
		if (!Validator.validateMultiSpeakVersion(version))
			return null;
		
		if (isArray && HEADER_XPATHS_GROUP != null && version.equals(VERSION4HEADER))
			return HEADER_XPATHS_GROUP;
		
		if (!isArray && HEADER_XPATHS_NON_GROUP != null && version.equals(VERSION4HEADER))
			return HEADER_XPATHS_NON_GROUP;

		VERSION4HEADER = version;
		
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT path from Xpath path where path.serviceCode = '" + Xpath.HEADER_SERVICE_CD + "' and path.isArray =" + isArray + " and version = '" + version + "' order by path.fieldName");	

		List<Xpath> list = query.getResultList();       
		entityManager.close();
		
		if (isArray)
			HEADER_XPATHS_GROUP = list;
		else
			HEADER_XPATHS_NON_GROUP = list;
		
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
