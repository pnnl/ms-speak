/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.persistence;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * 
 * The Cassandra persistence manager does not seem to work well with ConfigurableApplicationContext,
 * so it is moved out into its own utility and appContext xml file and using the legacy XmlBeanFactory
 * loader.
 * 
 * @author pning
 *
 */
public class PacketDAOUtil {
	static private ApplicationContext context = null;
	static public ApplicationContext getApplicationContext() {
		if (context != null) {
			return context;
		}
		else {
			context = new ClassPathXmlApplicationContext("applicationContextPacket.xml");
			return context;
		}
	}
	
	static public PacketDAO getPacketDAO() {
		return (PacketDAO) getApplicationContext().getBean("packetDAO");
	}
}
