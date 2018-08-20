/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.analysis;

import java.util.ArrayList;
import java.util.List;

import com.essence.configuration.EndpointConfigurationManager;
import com.essence.persistence.CassandraDAOUtil;
import com.essence.persistence.DAOUtil;
import com.essence.persistence.EngineRunLogDAO;
import com.essence.persistence.PacketDAO;
import com.essence.model.EndpointConfiguration;
import com.essence.model.EngineRunLog;

public class PacketAnalyserEngine {
	List<PacketAnalyzer> activeModules = new ArrayList<PacketAnalyzer>();
	//private long lastRunCutoffInMillis = -1l; // point of last detection - end of last detecting window
	
	// Singleton support for the engine
	static private PacketAnalyserEngine engineInstance = null;
	static public PacketAnalyserEngine getInstance() {
		if (engineInstance == null) {
			System.out.println("creating engines...");
			engineInstance = new PacketAnalyserEngine();
			engineInstance.init();
			System.out.println("finished initialization of engines...");
		}
		
		return engineInstance;
	}
	private PacketAnalyserEngine() {
		// make the constructor private to support singleton
	}
	
	private Boolean runContinous = false;
	
	public void init() {
		activeModules.add(new DoSDetector());
		activeModules.add(new MSPConnectivityDetector());
		activeModules.add(new ValueOutOfBoundDetector());
	}
	
	public static void main(String[] args)    
	{    
		PacketAnalyserEngine engine = PacketAnalyserEngine.getInstance();
		engine.run();
	}

	public void run() {
		runEnginesOnce();
		while (runContinous) {
			try { // otherwise, wait for 1 second and try again
			    Thread.sleep(5000); // 1000 millis, 5 second
			} catch(InterruptedException ex) {
			    Thread.currentThread().interrupt();
			}
			runEnginesOnce();
		}		
	}
	
	public void runEnginesOnce() {
		PacketDAO dao = CassandraDAOUtil.getPacketDAO();
		EngineRunLogDAO engineRunLogDAO = DAOUtil.getEngineRunLogDAO();
		
		System.out.println("entered runEngineOnce");
		EngineRunLog log = new EngineRunLog();
		log.setRunTime(System.currentTimeMillis());
		long currentCutoffTime = -1l;
		
		// get the lastRunCutoffTime from DB
		EngineRunLog lastLog = engineRunLogDAO.getLastEngineRunLog();
		long lastRunCutoffInMillis = -1l; // default value, DB is empty so there are no results
		if (lastLog != null)
			lastRunCutoffInMillis = lastLog.getCutoffTime();

		List<String> dests = new ArrayList<String>(); // TODO - get the list of destination IPs in the network
		//GreetingServiceImpl impl = new GreetingServiceImpl();
		EndpointConfigurationManager ecm = new EndpointConfigurationManager();
		List<EndpointConfiguration> ecs = ecm.getEndpointConfigurations(); //DAOUtil.getEndpointConfigurationDAO().getAllEndpointConfigurations();
		for (EndpointConfiguration ec: ecs) {
			dests.add(ec.getKey().getHostIPAddress());
		}
		
		System.out.println("done getting ECS");
		
		if (dests == null || dests.isEmpty()) {
	        System.out.println("dests size = empty");
			return;
		}
		
		System.out.println("dests size = " + dests.size());
		List<Packet> packets = dao.getAllPacketsByDestsSinceLastCutoffTime(dests, lastRunCutoffInMillis, 1000); // at most 1000 packets in a run 
		if (packets == null || packets.isEmpty()) { // No packets to run on
	        System.out.println("get packets size = empty");
		    return;
		}
		
		System.out.println("get packets size = " + packets.size());

		List<Thread> threads = new ArrayList<Thread>();		// keep track of threads so we can join them together
		StringBuffer activeModuleNames = new StringBuffer(); 		// names of active modules

		// start a new thread for each active detection module
		for (int i=0; i<activeModules.size(); i++) { // sequential run that can be made parallel later
			PacketAnalyzer a = activeModules.get(i);
			a.setLastRunCutoffInMillis(lastRunCutoffInMillis);
			System.out.println("starting ... " + a.getClass().getName());
			Thread t = new Thread(new PacketAnalyzerThread(a,packets));
			t.start();
			threads.add(t);	
		}
		
		// join threads, wait for all detectors to finish before updating cutoff time
		for (int i =0; i < threads.size(); i++){
			try {
				threads.get(i).join();
				// get the name of the modules being run - parse the java classname
				String [] tokens = activeModules.get(i).toString().split("[.@]");
				System.out.println("joining ... " + activeModules.get(i).toString());
				activeModuleNames.append(tokens[3]+" ");
				if (currentCutoffTime < activeModules.get(i).getCurrentRunCutoffInMillis())
					currentCutoffTime = activeModules.get(i).getCurrentRunCutoffInMillis(); // most recent timestamp of the packets seen in this run
			} catch (InterruptedException e) {
				Thread.currentThread().interrupt();
			}
		}
		
		log.setCutoffTime(currentCutoffTime);

		// add the description, truncate to 100 char according to VARCHAR limit in DB
		String s = activeModuleNames.toString();
		System.out.println("writing log ... " + s);
		if (s.length() > 100)
			s = s.substring(0,99);
		log.setDescription(s); 
		engineRunLogDAO.addEngineRunLog(log);
		
		// TODO: don't write a log if there are no new packets to process,
		// need to create a list of packets which are 'new'. If this list is null
		// , then don't even call the detectors.
		
	}
	public Boolean getRunContinous() {
		return runContinous;
	}
	public void setRunContinous(Boolean runContinous) {
		this.runContinous = runContinous;
	}
}
