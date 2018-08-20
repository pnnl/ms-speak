/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.policy;

import java.util.List;

import org.hibernate.Session;

import com.essence.persistence.DAOUtil;
import com.essence.persistence.DetectionRuleDAO;
import com.essence.persistence.HibernateUtil;
import com.essence.persistence.OrganizationDAO;
import com.essence.model.DetectionRule;
import com.essence.model.DetectionRuleType;
import com.essence.model.OrganizationProfile;

public class RuleManager {
	 
		public static void main( String[] args)
		{
			System.out.println("Enter main");
			//testEnum();
			//testDetectionRulesByType(DetectionRuleType.DENIAL_OF_SERVICE);
			//testDetectionRulesByType(DetectionRuleType.MS_EP_CONNECTIVITY);
			//testDetectionRules();
			//testStocks();
			/*
			testSplit("AM,ASM,AVL,CB,CD,CH,CP,DA,DER,DGN,DM,DR,EA,EDTR,FA,GIS,INV,LOC,MDM,MM,MOD,MR,NOT,OA,OD,PAN,PG,PP,PPM,PUB,RM,SCADA,SA,SWO,WEA,WG,WO,WP,WR,WV", 60);
			testSplit("AM,ASM,AVL,CB,CD,CH,CP,DA,DER,DGN,DM,DR,EA,EDTR,FA,GIS,INV,LOC,MDM,MM,MOD,MR,NOT,OA,OD,PAN,PG,PP,PPM,PUB,RM,SCADA,SA,SWO,WEA,WG,WO,WP,WR,WV", 20);
			testSplit("AM,ASM,AVL,CB,CD,CH,CP,DA,DER,DGN,DM,DR,EA,EDTR,FA,GIS,INV,LOC,MDM,MM,MOD,MR,NOT,OA,OD,PAN,PG,PP,PPM,PUB,RM,SCADA,SA,SWO,WEA,WG,WO,WP,WR,WV", 40);
			testSplit("AM,ASM,AVL,CB,CD,CH,CP,DA,DER,DGN,DM,DR,EA,EDTR,FA,GIS,INV,LOC,MDM,MM,MOD,MR,NOT,OA,OD,PAN,PG,PP,PPM,PUB,RM,SCADA,SA,SWO,WEA,WG,WO,WP,WR,WV", 55);
			testSplit("AM,ASM,AVL,CB,CD,CH,CP,DA,DER,DGN,DM,DR,EA,EDTR,FA,GIS,INV,LOC,MDM,MM,MOD,MR,NOT,OA,OD,PAN,PG,PP,PPM,PUB,RM,SCADA,SA,SWO,WEA,WG,WO,WP,WR,WV", 23);
			*/
			testDetectionRulesByTypeAndPolicy(DetectionRuleType.MS_EP_CONNECTIVITY);
			testDetectionRulesByTypeAndPolicy(DetectionRuleType.DENIAL_OF_SERVICE);
			testDetectionRulesByTypeAndPolicy(DetectionRuleType.VALUE_OUT_OF_BOUND);
			testDetectionRulesByPolicy();
			
	        return;
	    }

        @SuppressWarnings("unused")
		static private void testSplit(String csvString, int lineSize) {
	    	int LINE_SIZE = lineSize;
	        System.out.println("input=" + csvString + "\tline-size=" +lineSize);	        
	    	StringBuffer sb = new StringBuffer();
	        sb.append("<div><table width='100%'>");
	        sb.append("\n");
	        while (csvString != null && !csvString.isEmpty()) {
	        	if (csvString.length() <= LINE_SIZE) {
	    	        sb.append("<tr><td><div>"+csvString+"</div></td></tr>");
	    	        sb.append("\n");
	        		break;
	        	} else {
	        		int splitPoint = csvString.substring(LINE_SIZE).indexOf(",");
	        		if (splitPoint == -1) { // got the final one
		    	        sb.append("<tr><td><div>"+csvString+"</div></td></tr>");
		    	        sb.append("\n");
		        		break;	        			
	        		} else {
		    	        sb.append("<tr><td><div>"+csvString.subSequence(0, LINE_SIZE+splitPoint)+"</div></td></tr>");
		    	        sb.append("\n");
		    	        csvString = csvString.substring(LINE_SIZE+splitPoint+1);
	        		}
	        	}
	        }
	        System.out.println("output=\n" + sb.toString());
		}
		
		@SuppressWarnings("unused")
        static private void testEnum() {
			for(DetectionRuleType type: DetectionRuleType.values()){
		        System.out.println("DetectionRuleType: " + type);
			}			
		}
		
		public static void testDetectionRules() 
		{
			DetectionRuleDAO dao = DAOUtil.getDetectionRuleDAO();
			DetectionRule rule = new DetectionRule();
			
			rule.setRuleType(DetectionRuleType.MS_EP_CONNECTIVITY);
			rule.setSrcEndpointType("CSR");
			rule.setDstEndpointType("MR");
			rule.setActionType("Allowed");
			dao.addDetectionRule(rule);
			
			List<DetectionRule> rules = dao.getAllActiveDetectionRules();
			for (int i=0; rules != null && i<rules.size(); i++)
				rules.get(i).print();
		}
		
		public static void testDetectionRulesByType(DetectionRuleType type) 
		{
			DetectionRuleDAO dao = DAOUtil.getDetectionRuleDAO();
			List<DetectionRule> rules = dao.getActiveDetectionRulesByType(type);
			for (int i=0; rules != null && i<rules.size(); i++)
				rules.get(i).print();
		}

		public static void testDetectionRulesByTypeAndPolicy(DetectionRuleType type) 
		{
			System.out.println("\nRules for type: " + type);
			OrganizationDAO pd = DAOUtil.getOrganizationDAO();
			DetectionRuleDAO dao = DAOUtil.getDetectionRuleDAO();
			List<OrganizationProfile> ps = pd.getAllOrganizations();
			System.out.println("Rules for all policies and type = " + type);
			for (OrganizationProfile p: ps) {
				p.print();
				List<DetectionRule> rs = dao.getDetectionRulesByTypeAndOrganization(type, p.getId());
				for (DetectionRule r: rs)
					r.print();
			}			
			
			System.out.println("Only active policies and type = " + type);
			ps = pd.getAllActiveOrganizations();
			for (OrganizationProfile p: ps) {
				p.print();
				List<DetectionRule> rs = dao.getDetectionRulesByTypeAndOrganization(type, p.getId());
				for (DetectionRule r: rs)
					r.print();
			}			
			
			System.out.println("Only active policies and type = " + type + " using new combined API");
				List<DetectionRule> rs = dao.getActiveDetectionRulesByType(type);
				for (DetectionRule r: rs)
					r.print();
		}


		public static void testDetectionRulesByPolicy() 
		{
			System.out.println("\nRules for all policies:");
			OrganizationDAO pd = DAOUtil.getOrganizationDAO();
			DetectionRuleDAO dao = DAOUtil.getDetectionRuleDAO();
			List<OrganizationProfile> ps = pd.getAllOrganizations();
			for (OrganizationProfile p: ps) {
				p.print();
				List<DetectionRule> rs = dao.getAllDetectionRulesByOrganization(p.getId());
				for (DetectionRule r: rs)
					r.print();
			}			
			
			System.out.println("Only for active policies:");
			ps = pd.getAllActiveOrganizations();
			for (OrganizationProfile p: ps) {
				p.print();
				List<DetectionRule> rs = dao.getAllDetectionRulesByOrganization(p.getId());
				for (DetectionRule r: rs)
					r.print();
			}			
			
			System.out.println("Only for active policies using new combined API:");
				List<DetectionRule> rs = dao.getAllActiveDetectionRules();
				for (DetectionRule r: rs)
					r.print();
		}
}
