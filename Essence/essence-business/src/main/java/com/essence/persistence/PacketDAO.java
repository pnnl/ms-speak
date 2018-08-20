/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.persistence;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Query;
import javax.xml.bind.DatatypeConverter;

import org.apache.log4j.Logger;
import org.springframework.stereotype.Service;

import com.essence.analysis.Packet;
import com.essence.analysis.PacketPK;
import com.essence.analysis.TimestampUtil;
import com.essence.analysis.ValueOutOfBoundDetector;
import com.essence.multispeak.MSPServiceOperationKey;
import com.essence.ui.shared.StringUtil;
import com.essence.ui.shared.Validator;

@SuppressWarnings("unused")
@Service
public class PacketDAO
{    
	static Logger log = Logger.getLogger(PacketDAO.class.getName());
	EntityManagerFactory entityManagerFactory;    

	static public String TEST_SOURCE_IP_V5 = "172.16.0.10";
	static public String TEST_DESINATION_IP_V5 = "172.16.0.11";

	static public String TEST_SOURCE_IP_V3 = "172.16.0.8";
	static public String TEST_DESINATION_IP_V3 = "172.16.0.9";

	public static void main(String[] args)    
	{    	
		/*
		if (args.length > 0)
		    testGetByDestinationInWindow(args[0]);
			*/
		//testGetPacketsBySrcDst24Hours("172.16.0.1", "172.16.0.2");
		storeTestMessagesV3NoEP();
		//storeTestMessagesV5();
		//testQueryDeleteV3(true, "2015-01-13", "2015-01-15");
		//testQueryDeleteV5(true, "2014-12-02", "2014-12-03");
		//testEngine4CBV3( "2014-12-09", "2014-12-10");
		//testGetSinceLastCutoffTime();
	}

    private static void storeTestMessagesV5() {
		testAddMsgPacket("../essence-frontend/src/test/data/TESTDATA-GetAssetsByAssetFieldsResponse.xml", "AM", "GetAssetsByAssetFieldsResponse", MSPServiceOperationKey.SUPPORTED_VERSION_5, TEST_SOURCE_IP_V5, TEST_DESINATION_IP_V5);
		testAddMsgPacket("../essence-frontend/src/test/data/TESTDATA-ChangeUsageData.xml", "CB", "ChangeUsageData", MSPServiceOperationKey.SUPPORTED_VERSION_5, TEST_SOURCE_IP_V5, TEST_DESINATION_IP_V5);
		testAddMsgPacket("../essence-frontend/src/test/data/TESTDATA-GetAllSCADAAnalogsResponse.xml", "DA", "GetAllSCADAAnalogsResponse", MSPServiceOperationKey.SUPPORTED_VERSION_5, TEST_SOURCE_IP_V5, TEST_DESINATION_IP_V5);
		testAddMsgPacket("../essence-frontend/src/test/data/TESTDATA-GetMeterReadingsByDateIntervalDataResponse.xml", "MR", "GetMeterReadingsByDateIntervalDataResponse", MSPServiceOperationKey.SUPPORTED_VERSION_5, TEST_SOURCE_IP_V5, TEST_DESINATION_IP_V5);
		
		testAddMsgPacket("../essence-frontend/src/test/data/TESTDATA-LinkAttachmentsToObjects.xml", "WV", "LinkAttachmentsToObjects", MSPServiceOperationKey.SUPPORTED_VERSION_5, TEST_SOURCE_IP_V5, TEST_DESINATION_IP_V5);
		
		log.info("start ttt");
		test3(TEST_SOURCE_IP_V5, TEST_DESINATION_IP_V5);
		log.info("end ttt");				
	}
	
    private static void storeTestMessagesV3() {
		
		//testAddMsgPacket("../essence-frontend/src/test/data/ModifyCBDataForMeter.xml", "CB", "ModifyCBDataForMeter", MSPServiceOperationKey.SUPPORTED_VERSION_3, TEST_SOURCE_IP_V3, TEST_DESINATION_IP_V3);
		testAddMsgPacket("../essence-frontend/src/test/data/TESTDATA-v3-CB-ModifyCBDataForMeter-117-118-119.xml", "CB", "ModifyCBDataForMeter", MSPServiceOperationKey.SUPPORTED_VERSION_3, TEST_SOURCE_IP_V3, TEST_DESINATION_IP_V3);
		
		testAddMsgPacket("../essence-frontend/src/test/data/TESTDATA-v3-MR-GetReadingsByBillingCycle-122.xml", "MR", "GetReadingsByBillingCycle", MSPServiceOperationKey.SUPPORTED_VERSION_3, TEST_SOURCE_IP_V3, TEST_DESINATION_IP_V3);
		testAddMsgPacket("../essence-frontend/src/test/data/TESTDATA-v3-OA-GetAllConnectivityResponse-121.xml", "OA", "GetAllConnectivityResponse", MSPServiceOperationKey.SUPPORTED_VERSION_3, TEST_SOURCE_IP_V3, TEST_DESINATION_IP_V3);
		
		//testAddMsgPacket("../essence-frontend/src/test/data/GetAllConnectivityResponse.xml", "OA", "GetAllConnectivityResponse", MSPServiceOperationKey.SUPPORTED_VERSION_3, TEST_SOURCE_IP_V3, TEST_DESINATION_IP_V3);
		testAddMsgPacket("../essence-frontend/src/test/data/TESTDATA-v3-OA-GetModifiedConnectivityResponse-124.xml", "OA", "GetModifiedConnectivityResponse", MSPServiceOperationKey.SUPPORTED_VERSION_3, TEST_SOURCE_IP_V3, TEST_DESINATION_IP_V3);
		testAddMsgPacket("../essence-frontend/src/test/data/TESTDATA-v3-OA-MeterExchangeNotification-120.xml", "OA", "MeterExchangeNotification", MSPServiceOperationKey.SUPPORTED_VERSION_3, TEST_SOURCE_IP_V3, TEST_DESINATION_IP_V3);
		testAddMsgPacket("../essence-frontend/src/test/data/TESTDATA-v3-OD-RegisterForService-123.xml", "OD", "RegisterForService", MSPServiceOperationKey.SUPPORTED_VERSION_3, TEST_SOURCE_IP_V3, TEST_DESINATION_IP_V3);
		
		
		log.info("start ttt");
		test3(TEST_SOURCE_IP_V3, TEST_DESINATION_IP_V3);
		log.info("end ttt");		
			
	}
	
	private static void storeTestMessagesV3NoEP() {
		String workingDir = System.getProperty("user.dir");
		System.out.println("Working Directory = " + workingDir);
		//testAddMsgPacket("../essence-frontend/src/test/data/ModifyCBDataForMeter.xml", "CB", "ModifyCBDataForMeter", MSPServiceOperationKey.SUPPORTED_VERSION_3, TEST_SOURCE_IP_V3, TEST_DESINATION_IP_V3);
		testAddMsgPacket("../essence-frontend/src/test/data/TESTDATA-v3-CB-ModifyCBDataForMeter-117-118-119.xml", "NULL", "ModifyCBDataForMeter", MSPServiceOperationKey.SUPPORTED_VERSION_3, TEST_SOURCE_IP_V3, TEST_DESINATION_IP_V3);
		
		testAddMsgPacket("../essence-frontend/src/test/data/TESTDATA-v3-MR-GetReadingsByBillingCycle-122.xml", "null", "GetReadingsByBillingCycle", MSPServiceOperationKey.SUPPORTED_VERSION_3, TEST_SOURCE_IP_V3, TEST_DESINATION_IP_V3);
		testAddMsgPacket("../essence-frontend/src/test/data/TESTDATA-v3-OA-GetAllConnectivityResponse-121.xml", "NULL", "GetAllConnectivityResponse", MSPServiceOperationKey.SUPPORTED_VERSION_3, TEST_SOURCE_IP_V3, TEST_DESINATION_IP_V3);
		
		//testAddMsgPacket("../essence-frontend/src/test/data/GetAllConnectivityResponse.xml", "OA", "GetAllConnectivityResponse", MSPServiceOperationKey.SUPPORTED_VERSION_3, TEST_SOURCE_IP_V3, TEST_DESINATION_IP_V3);
		testAddMsgPacket("../essence-frontend/src/test/data/TESTDATA-v3-OA-GetModifiedConnectivityResponse-124.xml", "NULL", "GetModifiedConnectivityResponse", MSPServiceOperationKey.SUPPORTED_VERSION_3, TEST_SOURCE_IP_V3, TEST_DESINATION_IP_V3);
		testAddMsgPacket("../essence-frontend/src/test/data/TESTDATA-v3-OA-MeterExchangeNotification-120.xml", "NULL", "MeterExchangeNotification", MSPServiceOperationKey.SUPPORTED_VERSION_3, TEST_SOURCE_IP_V3, TEST_DESINATION_IP_V3);
		testAddMsgPacket("../essence-frontend/src/test/data/TESTDATA-v3-OD-RegisterForService-123.xml", "NULL", "RegisterForService", MSPServiceOperationKey.SUPPORTED_VERSION_3, TEST_SOURCE_IP_V3, TEST_DESINATION_IP_V3);
		
		
		log.info("start ttt");
		test3(TEST_SOURCE_IP_V3, TEST_DESINATION_IP_V3);
		log.info("end ttt");		
			
	}
	
	public static void testAddMsgPacket(String pathToFile, String serviceCD, String msgName, String version, String srcIP, String dstIP) {
		Path path = Paths.get(pathToFile);
		byte[] data = null;
		try {
			data = Files.readAllBytes(path);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		PacketPK key = new PacketPK();
		key.setSourceAddress(srcIP);
		key.setDestAddress(dstIP);
		key.setTimeStamp(new Timestamp(System.currentTimeMillis()));
		
		Packet p = new Packet();		
		p.setPacketPK(key);
		p.setContent(data);
		p.setProtocol("MultiSpeak");
		Map<String, String> textValues = new HashMap<String, String>();
		//if (StringUtil.stringHasValue(serviceCD))
			textValues.put(Packet.ENDPOINT_NAME_KEY, serviceCD);
		//if (StringUtil.stringHasValue(msgName))
			textValues.put(Packet.MESSAGE_TYPE_KEY, msgName);		
		//if (StringUtil.stringHasValue(version))
			textValues.put(Packet.MSP_VERSION_KEY, version);		
		p.setTextValues(textValues);
		CassandraDAOUtil.getPacketDAO().addPacket(p);
	}

	private static void testGetByDestinationInWindow(String ip) {
		BufferedReader br;
		String line = null;
		try {
			br = new BufferedReader(new FileReader(ip));
			line = br.readLine();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
			log.warn(e.getMessage());
		} catch (IOException e1) {
			log.warn(e1.getMessage());
		}
		PacketDAO dao = CassandraDAOUtil.getPacketDAO();
		long now = System.currentTimeMillis();
		long ago24hours = now - 1000*60*60*24; 
		List<Packet> list = dao.getAllPacketsByDestInWindow(line, ago24hours, now);    
		for (Packet p : list) {
			p.printNoContent();
		}
	}

	public static void testQueryDeleteV5(boolean delete, String d1, String d2) {
		//String dst = "172.16.0.11";
		PacketDAO dao = CassandraDAOUtil.getPacketDAO();
		//2014-08-18 14:38:27-0400
		long td1 = DatatypeConverter.parseDateTime(d1).getTimeInMillis(); //.getTime();
		long td2 = DatatypeConverter.parseDateTime(d2).getTimeInMillis(); //.getTime();
		List<Packet> list = dao.getAllPacketsByDestInWindow(TEST_DESINATION_IP_V5, td1, td2);    
//		list = dao.getAllPacketsByDestInWindowOld(TEST_DESINATION_IP_V5, td1, td2);    
		int count = 1;
		for (Packet p : list) {
			System.out.println(count + "th LONG Record:"); 
			p.printNoContent();
			if (delete)
				dao.deletePacket(p); 
			count++;
		}
	}

    private static void testEngine4CBV3(String d1, String d2) {
		PacketDAO dao = CassandraDAOUtil.getPacketDAO();
		long td1 = DatatypeConverter.parseDateTime(d1).getTimeInMillis(); //.getTime();
		long td2 = DatatypeConverter.parseDateTime(d2).getTimeInMillis(); //.getTime();
		List<Packet> list = dao.getAllPacketsByDestInWindow(TEST_DESINATION_IP_V3, td1, td2);    
		ValueOutOfBoundDetector dtr = new ValueOutOfBoundDetector();
		dtr.activate();
		for (Packet p : list) {
			//if (p.getTextValues().get(Packet.ENDPOINT_NAME_KEY).equals("CB")) {
				dtr.analyse(p);
			//}
		}
	}

	public static void testQueryDeleteV3(boolean delete, String d1, String d2) {
		//String dst = "172.16.0.11";
		PacketDAO dao = CassandraDAOUtil.getPacketDAO();
		//2014-08-18 14:38:27-0400
		long td1 = DatatypeConverter.parseDateTime(d1).getTimeInMillis(); //.getTime();
		long td2 = DatatypeConverter.parseDateTime(d2).getTimeInMillis(); //.getTime();
		List<Packet> list = dao.getAllPacketsByDestInWindow(TEST_DESINATION_IP_V3, td1, td2);    
		int count = 1;
		byte[] selectedContent = null;
		for (Packet p : list) {
			/*
			if (p.getTextValues().get(Packet.ENDPOINT_NAME_KEY).equals("CB"))
				selectedContent = p.getContent();
				*/
			System.out.println(count + "th LONG Record:"); 
			p.printNoContent();
			if (delete)
				dao.deletePacket(p); 
			count++;
		}
		if (selectedContent != null)
			System.out.println("\tcontent = " + Packet.ba2string(selectedContent));

	}

	// test 
	private static void test3(String srcIP, String dstIP) {
		System.out.println("\nQuery #1");
		long now = System.currentTimeMillis();
		long ago24hours = now - 1000*60*60*24; 
		
		List<Packet> list = CassandraDAOUtil.getPacketDAO().getAllPacketsBySourceDest(srcIP, dstIP, ago24hours, now);    
		System.out.println("Size = " + list.size());
		for (int i=0; i<list.size(); i++) {
			System.out.print(i + "--");
			list.get(i).printNoContent();
			System.out.println("content size = " + list.get(i).getContent().length);
			String msg = null; 
			try {
				msg = new String(list.get(i).getContent(), "UTF-8");
				if (!StringUtil.stringHasValue(msg))
					return;
				int idx = msg.indexOf("<SOAP");
				if (idx < 0)
					idx = msg.indexOf("<Soap");
				if (idx < 0)
					idx = msg.indexOf("<soap");
				System.out.println("idx = " + idx);
				if (idx > 0)
					msg = msg.substring(idx);
			//	System.out.println("SOAP Message = \n" + msg);
			} catch (UnsupportedEncodingException e1) {
				log.warn(e1.getMessage());
				return;
			} // assuming this is the SOAP message
		}
	}

	private static void testGetPacketsBySrcDst24Hours(String src, String dst) {
		PacketDAO dao = CassandraDAOUtil.getPacketDAO();
		/*
		Map<String, Float> numVals = new HashMap<String, Float>();
		Map<String, String> textVals = new HashMap<String, String>();
		for (int i=0; i<12; i++) {
			long ts1 = System.currentTimeMillis();

			PacketPK key = new PacketPK();
			key.setSourceAddress("10.1.2.3");
			key.setDestAddress("10.9.8.7");
			key.setTimeStamp(new Timestamp(ts1));
			byte[] blob = ("test data blah blah"+(i+100)).getBytes();

			numVals.put("num_val1", 10f+i);
			textVals.put("text_val"+i, "text_val"+i);
			Packet packet = new Packet(key, "MultiSpeak", blob);  
			packet.setTextValues(textVals);
			packet.setNumericValues(numVals);
			dao.addPacket(packet);    	
		}
		*/
		System.out.println("\nGet packets between source " + src + " and destination " + dst + " within 24 hours");
		long now = System.currentTimeMillis();
		long ago24hours = now - 1000*60*60*24; 
		// src = "172.16.0.1", dst = "172.16.0.2"
		List<Packet> list = dao.getAllPacketsBySourceDest(src, dst, ago24hours, now);    
		System.out.println("Size = " + list.size());
		for (int i=0; i<list.size(); i++) {
			System.out.print(i + "--");
			list.get(i).print();
			String msg = null; 
			try {
				msg = new String(list.get(i).getContent(), "UTF-8");
				int idx = msg.indexOf("<SOAP");
				if (idx < 0)
					idx = msg.indexOf("<Soap");
				if (idx < 0)
					idx = msg.indexOf("<soap");
				System.out.println("idx = " + idx);
				if (idx > 0)
					msg = msg.substring(idx);
				System.out.println("SOAP Message = \n" + msg);
			} catch (UnsupportedEncodingException e1) {
				log.warn(e1.getMessage());
				return;
			} //Packet.ba2string(p.getContent()); // assuming this is the SOAP message

		}
		
		list = dao.getAllPacketsBySourceDest(dst, src, ago24hours, now);    
		System.out.println("Size = " + list.size());
		for (int i=0; i<list.size(); i++) {
			System.out.print(i + "--");
			list.get(i).print();
			System.out.println("content size = " + list.get(i).getContent().length);
			String msg = null; 
			try {
				msg = new String(list.get(i).getContent(), "UTF-8");
				int idx = msg.indexOf("<SOAP");
				if (idx < 0)
					idx = msg.indexOf("<Soap");
				if (idx < 0)
					idx = msg.indexOf("<soap");
				System.out.println("idx = " + idx);
				if (idx > 0)
					msg = msg.substring(idx);
				System.out.println("SOAP Message = \n" + msg);
			} catch (UnsupportedEncodingException e1) {
				log.warn(e1.getMessage());
				return;
			} //Packet.ba2string(p.getContent()); // assuming this is the SOAP message

		}
	}
	
	// Test cutofftime based query to a set of destinations
	private static void testGetSinceLastCutoffTime() {
		
		PacketDAO dao = CassandraDAOUtil.getPacketDAO();
		List<String> dests = new ArrayList<String>();
		for (int i=7; i<=11; i++)
			dests.add("172.16.0." + i);
		//2014-08-18 14:38:27-0400
		long td = DatatypeConverter.parseDateTime("2014-11-10").getTimeInMillis(); //.getTime();
		System.out.println("\n query based on estinations:"); 
		long t1 = 0, t2=0;
		t1 = System.currentTimeMillis();
		List<Packet> list = dao.getAllPacketsByDestsSinceLastCutoffTime(dests, td, 10);   
		t2 = System.currentTimeMillis();
		System.out.println("\n query time:" + (t2-t1)); 
		
		int count = 1;
		for (Packet p : list) {
			System.out.println(count + "th LONG Record:"); 
			p.printNoContent();
			count++;
		}

		System.out.println("\n query based on allow filtering:"); 
		t1 = System.currentTimeMillis();
		list = dao.getAllPacketsSinceLastCutoffTime(td, 9);    
		t2 = System.currentTimeMillis();
		System.out.println("\n query time:" + (t2-t1)); 
		count = 1;
		for (Packet p : list) {
			System.out.println(count + "th LONG Record:"); 
			p.printNoContent();
			count++;
		}
	}

	private String buildNumericValues4Insert(Map<String, Float> nvs) {
		StringBuffer sb = new StringBuffer(200);
		sb.append("{");
		if (nvs != null && !nvs.isEmpty()) {
			Set<String> keySet = nvs.keySet();
			Iterator<String> it = keySet.iterator();
			boolean isNotFirst = false;
			while (it.hasNext()){
				if (isNotFirst) {
					sb.append(",");
				}
				isNotFirst = true;
				String key = it.next();
				sb.append("'");
				sb.append(key);
				sb.append("'");
				sb.append(":");
				Float val = nvs.get(key);
//				sb.append("'");
				sb.append(val.toString());
	//			sb.append("'");
			}
		}
		sb.append("}");
		return sb.toString();
	}
	
	private String buildTextValues4Insert(Map<String, String> nvs) {
		StringBuffer sb = new StringBuffer(200);
		sb.append("{");
		if (nvs != null && !nvs.isEmpty()) {
			Set<String> keySet = nvs.keySet();
			Iterator<String> it = keySet.iterator();
			boolean isNotFirst = false;
			while (it.hasNext()){
				if (isNotFirst) {
					sb.append(",");
				}
				isNotFirst = true;
				String key = it.next();
				sb.append("'");
				sb.append(key);
				sb.append("'");
				sb.append(":");
				String val = nvs.get(key);
				sb.append("'");
				sb.append(val);
				sb.append("'");
			}
		}
		sb.append("}");
		return sb.toString();
	}

	public int addPacket(Packet packet)    
	{              
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		/*
		Query query = entityManager.createNativeQuery("insert into packet (source_addr, dest_addr, time_stamp, protocol, content) values ('"+
				packet.getPacketPK().getSourceAddress()+"', '"+packet.getPacketPK().getDestAddress()+"', '"+packet.getPacketPK().getTimeStamp()+
				"', '"+packet.getProtocol()+"', varcharAsBlob('"+ba2string(packet.getContent())+"'));", packet.getClass());
				*/
		String queryStr = "insert into packet (source_addr, dest_addr, time_stamp, protocol, content,  numeric_values, text_values) values ('"+
				packet.getPacketPK().getSourceAddress()+"', '"+
				packet.getPacketPK().getDestAddress()+"', '"+
				packet.getPacketPK().getTimeStamp()+"', '"+
				packet.getProtocol()+"', varcharAsBlob('"+
				ba2string(packet.getContent())+"'), "+
				buildNumericValues4Insert(packet.getNumericValues()) + "," +
				buildTextValues4Insert(packet.getTextValues()) +
				");";
		Query query = entityManager.createNativeQuery(queryStr, packet.getClass());

		int cnt = query.executeUpdate();        
		entityManager.close();        
		
		return cnt;    
	}    
	
	public Packet getPacketById(PacketPK key)    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Packet packet = entityManager.find(Packet.class, key);        
		return packet;    
	}    
	
	@SuppressWarnings("unchecked")    
	public List<Packet> getAllPackets()    
	{        
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createQuery("SELECT p from Packet p");
		List<Packet> list = query.getResultList();       
		entityManager.close();
		return list;    
	}    

	@SuppressWarnings("unchecked")    
	public List<Packet> getAllPacketsN(int limit)    
	{         
		EntityManager entityManager = entityManagerFactory.createEntityManager();    
		Query query = entityManager.createNativeQuery("SELECT * from packet limit " + limit, Packet.class);
		List<Packet> list = query.getResultList();        
		entityManager.close();
		return list;    

	}    
 
	public void deletePacket(Packet p)    
	{         	
		EntityManager entityManager = entityManagerFactory.createEntityManager();
		entityManager.getTransaction().begin();
		// inefficient implementation
		entityManager.remove(entityManager.find(Packet.class, p.getPacketPK()));
		entityManager.getTransaction().commit();
		entityManager.close();
	}    

	// select * from packet where dest_addr='10.0.0.4' and time_stamp<'2014-03-17 14:45:00-0400' and time_stamp>'2014-03-17 14:44:00-0400';   
	@SuppressWarnings("unchecked")
    public List<Packet> getAllPacketsByDestInWindowOld(String dest, long begin, long end)    
	{    
		if (Validator.validateIPAddress(dest) == false) {
			return null;
		}
		
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
// Not working example with Timestamp
//		Query query = entityManager.createQuery("SELECT p from Packet p where p.packetPK.destAddress='"+dest+"'" + " and p.packetPK.timeStamp>='" + tsStr1 + "' and p.packetPK.timeStamp<='" + tsStr2+"'");
//		Query query = entityManager.createQuery("SELECT p from Packet p where p.packetPK.destAddress='"+dest+"'" + " and p.packetPK.timeStamp>=? and  and p.packetPK.timeStamp<=?");
		Query query = entityManager.createNativeQuery("SELECT * from packet where dest_addr='"+dest+"'" + " and time_stamp>'" + TimestampUtil.getTimestampString(begin) + "' and time_stamp<='" + TimestampUtil.getTimestampString(end)+"'", Packet.class);
		List<Packet> list = query.getResultList();        
		entityManager.close();
		return list;    
	}    
	
	@SuppressWarnings("unchecked")    
	public List<Packet> getAllPacketsByDestInWindow(String dest, long begin, long end)    
	{    
		if (Validator.validateIPAddress(dest) == false) {
			return null;
		}
		
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createNativeQuery("SELECT * from packet where dest_addr='"+dest+"'" + " and time_stamp>" + begin + " and time_stamp<=" + end, Packet.class);
		List<Packet> list = query.getResultList();        
		entityManager.close();
		return list;    
	}    

	private String generateDestinationAddressesInClause(List<String> dests) {
		StringBuffer sb = new StringBuffer();
		sb.append("in (");
		boolean isFirst = true;
		for (String d : dests) {
			if (isFirst) {
				sb.append("'" + d + "'");
				isFirst = false;
			} else {
				sb.append(", '" + d + "'");
			}
		}
		sb.append(")");
		//System.out.println("in-clause: " + sb.toString());
		
		return sb.toString();
	}
	
	/*
	 * When multi-node Cassandra is used, the query may need to be called against each IP instead of the IN for better performance. This need to verify if necessary.
	 */
	@SuppressWarnings("unchecked")    
	public List<Packet> getAllPacketsByDestsSinceLastCutoffTime(List<String> dests, long lastCutoffTime, int limit)    
	{    
		if (Validator.validateIPAddresses(dests) == false) {
			return null;
		}
		
		//  select dest_addr, time_stamp, source_addr, protocol, numeric_values, text_values, voltage  from packet where dest_addr in ('172.16.0.9', '172.16.0.11', '172.16.0.10', '172.16.0.8', '172.16.0.12') and time_stamp > '2014-11-10';
		
		String queryString = null;
		if (limit > 0)
			queryString = "SELECT * from packet where dest_addr " + generateDestinationAddressesInClause(dests) + " and time_stamp>" + lastCutoffTime + " order by time_stamp asc limit " + limit + " allow filtering";
		else
			queryString = "SELECT * from packet where dest_addr " + generateDestinationAddressesInClause(dests) + " and time_stamp>" + lastCutoffTime + " order by time_stamp asc allow filtering";
			
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createNativeQuery(queryString, Packet.class);
		List<Packet> list = query.getResultList();        
		entityManager.close();
		return list;    
	}    

	/*
	 * This API uses "allow filtering" which has unpredictable performance behavior; however, when the cluster is small or only one node, this may not be an issue.
	 * Also order by cannot be used: ORDER BY is only supported when the partition key is restricted by an EQ or an IN. 
	 * Therefore the limit clause could cause some packets to be skipped if the result set is not in increasing time_stamp order.
	 * The ALLOW FILTERING means Cassandra is reading through all your data, but only returning data within the range specified. 
	 * This is only efficient if the range is most of the data. If you wanted to find records within e.g. a 5 minute time window, 
	 * this would be very inefficient.
	 * http://stackoverflow.com/questions/18697725/cassandra-get-all-records-in-time-range
	 */
	@SuppressWarnings("unchecked")    
	public List<Packet> getAllPacketsSinceLastCutoffTime(long lastCutoffTime, int limit)    
	{    
		// select dest_addr, source_addr, text_values, protocol, numeric_values, voltage  from packet where time_stamp > '2014-11-01'  limit 1000 allow filtering;
		String queryString = null;
		if (limit > 0)
			queryString = "select * from packet where time_stamp > " + lastCutoffTime + " limit " + limit + " allow filtering";
		else
			queryString = "select * from packet where time_stamp > " + lastCutoffTime + " allow filtering";

		// select dest_addr, source_addr, time_stamp, text_values, protocol, numeric_values, voltage  from packet where time_stamp > '2014-12-01' limit 1000 allow filtering;
		EntityManager entityManager = entityManagerFactory.createEntityManager();        
		Query query = entityManager.createNativeQuery(queryString, Packet.class);
		List<Packet> list = query.getResultList();        
		entityManager.close();
		return list;    
	}    

	public List<Packet> getAllPacketsBySourceDest(String src, String dest, long begin, long end)    
	{        
		List<Packet> list = getAllPacketsByDestInWindow(dest, begin, end);
		List<Packet> result = new ArrayList<Packet>();
		for (int i=0; i<list.size(); i++)
			if (list.get(i).getPacketPK().getSourceAddress().equalsIgnoreCase(src))
				result.add(list.get(i));
		return result;    
	}    
	
	public EntityManagerFactory getEntityManagerFactory()    
	{        
		return entityManagerFactory;    
	}    
	
	public void setEntityManagerFactory(EntityManagerFactory entityManagerFactory)    
	{        
		this.entityManagerFactory = entityManagerFactory; //buildEntityManagerFactory();    
	}    
	
	// NOT working 
	/*
    private static EntityManagerFactory buildEntityManagerFactory() {
        try {
        	Properties properties = new Properties();
        	properties.load(PacketDAO.class.getClassLoader().getResourceAsStream("Kundera.properties"));
        	properties.list(System.out);
        	Map map = new HashMap();
        	map.put("kundera.nodes", properties.getProperty("kundera.node"));
        	map.put("kundera.port", properties.getProperty("kundera.port"));
        	map.put("kundera.keyspace", properties.getProperty("kundera.keyspace"));
        	map.put("sessionless", properties.getProperty("sessionless"));
        	map.put("kundera.client.lookup.class", "com.impetus.client.cassandra.pelops.PelopsClientFactory");
        	map.put("kundera.dialect", "cassandra");
       	 
        	return new EntityManagerFactoryImpl("cassandra_pu", map);
        }
        catch (Throwable ex) {
            // Make sure you log the exception, as it might be swallowed
            System.err.println("Initial SessionFactory creation failed." + ex);
            // TO-DO: handle properly
            return null;
        }
    }
    */

	public String ba2string(byte[] ba) {
		String s = ba.toString();
		try {
			String s1 = new String(ba, "UTF-8");
			return s1;
		} catch (UnsupportedEncodingException ex) {
			log.warn(ex.getMessage());
			return s;
		}
	}

}