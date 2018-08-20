/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.persistence;

import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import com.essence.action.SDNControllerNBI;

public class DAOUtil {
	
    static private ConfigurableApplicationContext context = null;
    static public ConfigurableApplicationContext getApplicationContext() {
    	if (context != null)
    		return context;
    	else {
    		context = new ClassPathXmlApplicationContext("applicationContext.xml");
    		return context;
    	}
    }    

	static public SDNControllerNBI getSDNControllerNBI() {
		return (SDNControllerNBI) getApplicationContext().getBean("sdnAPI");     	
	}
	
	static public DetectionRuleDAO getDetectionRuleDAO() {
		return (DetectionRuleDAO) getApplicationContext().getBean("detectionRuleDAO");     	
	}

	static public OrganizationDAO getOrganizationDAO() {
		return (OrganizationDAO) getApplicationContext().getBean("organizationDAO");     	
	}
	
    static public ClassificationDAO getClassificationDAO() {
        return (ClassificationDAO) getApplicationContext().getBean("classificationDAO");        
    }

	static public DecisionRuleDAO getDecisionRuleDAO() {
		return (DecisionRuleDAO) getApplicationContext().getBean("decisionRuleDAO");     	
	}

	static public DecisionDAO getDecisionDAO() {
		return (DecisionDAO) getApplicationContext().getBean("decisionDAO");     	
	}

	static public ActionDAO getActionDAO() {
		return (ActionDAO) getApplicationContext().getBean("actionDAO");     	
	}

	static public EndpointConfigurationDAO getEndpointConfigurationDAO() {
		return (EndpointConfigurationDAO) getApplicationContext().getBean("endpointConfigurationDAO");     	
	}

	static public AnalyzerResultDAO getAnalyzerResultDAO() {
		return (AnalyzerResultDAO) getApplicationContext().getBean("analyzerResultDAO");     	
	}
	
    static public AlertDAO getAlertDAO() {
        return (AlertDAO) getApplicationContext().getBean("alertDAO");        
    }
    
    static public AnomalyDAO getAnomalyDAO() {
        return (AnomalyDAO) getApplicationContext().getBean("anomalyDAO");        
    }

	static public MSPServiceOperationDAO getMSPServiceOperationDAO() {
		return (MSPServiceOperationDAO) getApplicationContext().getBean("mspServiceOperationDAO");     	
	}
	
	static public EngineRunLogDAO getEngineRunLogDAO() {
		return (EngineRunLogDAO) getApplicationContext().getBean("engineRunLogDAO");
	}

	static public MSPXpathDAO getMSPXpathDAO() {
		return (MSPXpathDAO) getApplicationContext().getBean("mspXpathDAO");
	}
	static public SettingDAO getSettingDAO() {
		return (SettingDAO) getApplicationContext().getBean("settingDAO");
	}
}
