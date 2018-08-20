/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.action.util;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public class Prop {

    String propertyFileName = "application.properties";
	Properties prop;
	public Prop()
	{
		prop = new Properties();
		try {
		    InputStream inputStream = getClass().getClassLoader().getResourceAsStream(propertyFileName);
		    
		    if (inputStream != null) {
		        prop.load(inputStream);
		    } else {
		        throw new FileNotFoundException("Property file " + propertyFileName + " not found in classpath");
		    }
		    
			//File appPropFile = new File("application.properties");
			//System.out.println(appPropFile.getAbsolutePath());
			//InputStream file= new FileInputStream(appPropFile );
			
			//prop.load(file);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch(IOException e) {
			e.printStackTrace();
		}
	}
	
	public String getControllerUrl()
	{
		return prop.getProperty("controllerUrl");
	}
}