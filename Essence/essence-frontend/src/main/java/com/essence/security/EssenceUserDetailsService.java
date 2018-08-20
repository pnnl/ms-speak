/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.security;

import java.util.Properties;

import org.apache.log4j.Logger;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;

/**
 * The EssenceUserDetailsService class is used to customize the list of
 * authorization providers to check for user authorization roles. The providers are listed within
 * a properties file. The order of the list doesn't matter, users authorization information is
 * obtained either from the database or the properties file. Never both.
 * 
 * @author Cigital Inc.
 */

public class EssenceUserDetailsService implements  UserDetailsService{
	
	public final static Logger LOGGER = Logger.getLogger(EssenceUserDetailsService.class);
	
	private Properties provider;
	//private JdbcUserDetailsService jdbcUserDetailsService;
		
    public void setProvider(Properties provider) {
		this.provider = provider;
	}
    
    public Properties getProvider()
    {
    	return this.provider;
    }

	public UserDetails loadUserByUsername(String username)
			throws UsernameNotFoundException {
            // The JDBC user details service is the only one we support
			return null; //this.getJdbcUserDetailsService().loadUserByUsername(username);
	}
/*
	public void setJdbcUserDetailsService(JdbcUserDetailsService jdbcUserDetailsService) {
		this.jdbcUserDetailsService = jdbcUserDetailsService;
	}

	public JdbcUserDetailsService getJdbcUserDetailsService() {
		return jdbcUserDetailsService;
	}
*/
}
