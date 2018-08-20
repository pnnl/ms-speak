package com.essence.persistence;

import com.essence.multispeak.MSPServiceOperationKey;

public class MultispeakMessagePersister {
	public static void main(String[] args)    
	{    	
		storeCoopMessages();
	}
	
	private static void storeCoopMessages() {
		String essence_root="C:/nreca/uiproject/essence-frontend/";
		String msgXml = essence_root + "src/test/data/GetMetersByCustomerNameResponse-199-36-central.xml";
		String endpointCD = "CB";
		String msgType = "GetMetersByCustomerNameResponse";
		String from = "10.200.18.36";
		String to ="148.80.253.199";
		PacketDAO.testAddMsgPacket(msgXml, endpointCD, msgType, MSPServiceOperationKey.SUPPORTED_VERSION_3, from, to);
	}
}
