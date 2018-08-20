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
public class CassandraDAOUtil {
	static private ApplicationContext context = null;
	//static private XmlBeanFactory beanFactory = null;
	static public ApplicationContext getApplicationContext() {
		if (context != null) {
			return context;
		}
		else {
			context = new ClassPathXmlApplicationContext("applicationContextCassandra.xml");
			return context;
		}
	}
//	static public XmlBeanFactory getBeanFactory() {
//		if (beanFactory != null)
//			return beanFactory;
//		else {
//			beanFactory = new XmlBeanFactory(new ClassPathResource("applicationContextCassandra.xml"));
//			return beanFactory;
//		}
//	}
	
	static public PacketDAO getPacketDAO() {
		return (PacketDAO) getApplicationContext().getBean("packetDAO");
		//return (PacketDAO) getBeanFactory().getBean("packetDAO");
	}
}
