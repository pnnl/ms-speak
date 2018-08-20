/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.analysis;

import java.util.List;

public interface PacketAnalyzer {
	

	/**
	 * set up fresh starting configuration for a run
	 * Step one - set up the analyzer, loading the rules
	 */
	public void activate();
	
	/**
	 * Step 2: analyze a set of packets
	 * @param packets
	 */
	public void analyse(List<Packet> packets);

	/**
	 * Step 2: or analyzer packet one at a time
	 * @param p
	 */
	public void analyse(Packet p);
	
	/**
	 * Step 3: wrapping up, processing the results
	 */
	public void done();
	
	/**
	 * Set the last run cutoff time to allow for filtering out processed packets
	 * @param lastRunCutoffInMillis
	 */
	public void setLastRunCutoffInMillis(long lastRunCutoffInMillis);

	/**
	 * Retrieve the current cutoff time as the detector sees it from the packets. 
	 * The maximum from all detectors will be the last cut off time for the run, to
	 * be used as a starting point for next detection.
	 * @return
	 */
	public long getCurrentRunCutoffInMillis();
}
