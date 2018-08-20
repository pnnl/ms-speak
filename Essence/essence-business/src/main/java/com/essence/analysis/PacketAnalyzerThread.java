/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.analysis;
import java.util.List;

public class PacketAnalyzerThread implements Runnable {
	private PacketAnalyzer module;
	private List<Packet> packets;

	public PacketAnalyzerThread(PacketAnalyzer a, List<Packet> packets) {
		this.module = a;
		this.packets = packets;
		
	}
	public void run() {
		module.activate();
		module.analyse(packets);
		module.done();
	}
}

