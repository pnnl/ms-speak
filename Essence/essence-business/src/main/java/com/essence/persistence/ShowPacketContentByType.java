/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.persistence;

import java.io.UnsupportedEncodingException;
import java.util.List;
import java.util.Map;

import com.essence.analysis.Packet;
import com.essence.ui.shared.StringUtil;

public class ShowPacketContentByType {
	public static void main(String[] args) {
		if (args == null || args.length != 1 || !StringUtil.stringHasValue(args[0])) {
			System.out.println("Please use: java com.essence.persistence.ShowPacketContentByType messageType");
			System.exit(1);
		}
	    @SuppressWarnings("unused")
		String msgType = args[0];
		
		PacketDAO dao = CassandraDAOUtil.getPacketDAO();
		long cutoffTime = System.currentTimeMillis() - 1000*60*60*24;
		List<Packet> list = dao.getAllPacketsSinceLastCutoffTime(cutoffTime, 1000);    
		for (Packet p : list) {
			Map<String, String> texts = p.getTextValues(); 
			if (args[0].equalsIgnoreCase(texts.get(Packet.MESSAGE_TYPE_KEY))) {
				System.out.println("MessageType: " + args[0]);
				try {
					System.out.println(new String(p.getContent(), "UTF-8"));
				} catch (UnsupportedEncodingException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		}	

		System.exit(0);
	}
}
