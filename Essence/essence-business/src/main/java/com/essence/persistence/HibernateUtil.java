/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.persistence;

import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import java.util.Properties;

public class HibernateUtil {
 
    private static final SessionFactory sessionFactory = buildSessionFactory();
 
    @SuppressWarnings("unused")
    private static SessionFactory buildSessionFactory2() {
        try {
            // Create the SessionFactory from hibernate.cfg.xml
            return new Configuration().configure().buildSessionFactory(); //Not sure why, but only the deprecated version works for now
            																// new StandardServiceRegistryBuilder().build());
        }
        catch (Throwable ex) {
            // Make sure you log the exception, as it might be swallowed
            System.err.println("Initial SessionFactory creation failed." + ex);
            throw new ExceptionInInitializerError(ex);
        }
    }
 
    private static SessionFactory buildSessionFactory() {
        try {
        	Properties properties = new Properties();
        	properties.load(HibernateUtil.class.getClassLoader().getResourceAsStream("application.properties"));
        	Configuration cfg = new Configuration(); 
        	cfg.addProperties(properties);//this one reads properties file (for connections settings) 
        	cfg.configure(); //this line reads hibernate.cfg.xml (for mapping classes)
            return cfg.buildSessionFactory(); 
        }
        catch (Throwable ex) {
            // Make sure you log the exception, as it might be swallowed
            System.err.println("Initial SessionFactory creation failed." + ex);
            throw new ExceptionInInitializerError(ex);
        }
    }

    public static SessionFactory getSessionFactory() {
        return sessionFactory;
    }
 
    public static void shutdown() {
    	// Close caches and connection pools
    	getSessionFactory().close();
    }
 
}
