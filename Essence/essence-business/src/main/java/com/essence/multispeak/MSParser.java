/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.multispeak;

import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;
import java.io.Writer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.logging.Logger;

import javax.xml.namespace.QName;

import org.apache.xmlbeans.SchemaProperty;
import org.apache.xmlbeans.SchemaType;
import org.apache.xmlbeans.SchemaTypeLoader;
import org.apache.xmlbeans.SchemaTypeSystem;
import org.apache.xmlbeans.XmlAnySimpleType;
import org.apache.xmlbeans.XmlBeans;
import org.apache.xmlbeans.XmlError;
import org.apache.xmlbeans.XmlException;
import org.apache.xmlbeans.XmlObject;
import org.apache.xmlbeans.XmlOptions;

import com.essence.persistence.DAOUtil;
import com.essence.model.Xpath;
import com.essence.ui.shared.StringUtil;
import com.eviware.soapui.impl.wsdl.WsdlContentPart;
import com.eviware.soapui.impl.wsdl.WsdlHeaderPart;
import com.eviware.soapui.impl.wsdl.WsdlInterface;
import com.eviware.soapui.impl.wsdl.WsdlOperation;
import com.eviware.soapui.impl.wsdl.WsdlProject;
import com.eviware.soapui.impl.wsdl.support.wsdl.WsdlImporter;
import com.eviware.soapui.model.iface.MessagePart;
import com.eviware.soapui.support.SoapUIException;

@SuppressWarnings("unused")
public class MSParser {
	static private Logger logger = Logger.getLogger(MSParser.class.getName());

	private WsdlProject project;
//	private Map<String, WsdlInterface> wsdls;

	// Output from one WSDL file, the xpaths will have "-{service_cd}-{msg_name}-{type}" added to the end
	static public List<String> ELEMENT_XPATHS = new ArrayList<String>();
	static public List<String> ATTR_XPATHS = new ArrayList<String>();
	static public String CURRENT_MSG_NAME = null;
	static public String CURRENT_SERVICE_CD = null;
	static public String CURRENT_SERVICE_VERSION = null;
	static private int PERSISTENCE_COUNT = 0;

	static private boolean IS_REQUEST_HEADER_PROCESSED = false;
	static private boolean IS_RESPONSE_HEADER_PROCESSED = false;

	private void init() {
		ELEMENT_XPATHS = new ArrayList<String>();
		ATTR_XPATHS = new ArrayList<String>();
		CURRENT_MSG_NAME = null;
		CURRENT_SERVICE_CD = null;		
		PERSISTENCE_COUNT = 0;
	}
	
	public MSParser(String wsdlURL) {
		try {
			this.project = new WsdlProject();
			WsdlInterface[] wsdlInterfaces = WsdlImporter.importWsdl(project, wsdlURL);
			init();
			for (WsdlInterface wsdl : wsdlInterfaces) {
				String wsdlName = wsdl.getName();
				System.out.println("wsdl interface name = " + wsdlName);
				int idx = wsdlName.indexOf("_");
				CURRENT_SERVICE_CD = wsdlName.substring(0, idx);
				parseWsdl(wsdl, false);
				break; // only need to do the first interface PP_ServerSoap12 vs. PP_ServerSoap
			}
		} catch (XmlException e) {
			logger.severe("XML parsing error occurred during WSDL import: "
					+ e.getMessage());
		} catch (IOException e) {
			logger.severe("IO error occurred during WSDL import: "
					+ e.getMessage());
		} catch (SoapUIException e) {
			logger.severe("An error occurred in SoapUI during WSDL import: "
					+ e.getMessage());
			e.printStackTrace();
		} catch (Exception e) {
			e.printStackTrace();
			logger.severe("An unknown error occurred during WSDL import: "
					+ e.getMessage());
		}
	}

	/**
	 * store the xpath object and return a print out string 
	 */
	private Xpath formXpathObject(String xpath) {
		assert(xpath != null);
		
		String[] parts = xpath.split("-");
		assert(parts.length==4);
		
		String fullPath = null;
		String serviceCD = null;
		// TODO - for v3 need to use a differnt signature
		if (xpath.contains(Xpath.REQUEST_HEADER_MESSAGE_NAME) 
				|| xpath.contains(Xpath.RESPONSE_HEADER_MESSAGE_NAME) 
				|| xpath.contains(Xpath.REQ_RESP_HEADER_MESSAGE_NAME_V3)) {
			fullPath = Xpath.HEADER_SIGNATURE_PATH + parts[0];
			serviceCD = Xpath.HEADER_SERVICE_CD;
		} else {
			fullPath = Xpath.BODY_SIGNATURE_PATH + parts[0];
			serviceCD = parts[1];
		}
		
		Xpath xpathEntity = new Xpath();
		xpathEntity.setIsArray(false);
		xpathEntity.setValueType(parts[3]);
		xpathEntity.setXpath(fullPath);
		xpathEntity.setServiceCode(serviceCD);
		xpathEntity.setVersion(CURRENT_SERVICE_VERSION);
		xpathEntity.setMessageName(parts[2]);
		xpathEntity.setFieldName(StringUtil.getElementNameFromXpath(fullPath));
		
		return xpathEntity; //fullPath + "-" + serviceCD + "-" + parts[2] + "-" + parts[3];
	}
	
	public void parseWsdl(WsdlInterface wsdl, boolean writeOutResult) {
		Writer writer = null;
		Writer writer2 = null;
		try {
			if (writeOutResult)
				writer = new BufferedWriter(new OutputStreamWriter(new FileOutputStream("C:\\nreca\\output.txt"), "utf-8"));
			if (writeOutResult)
				writer.write("Parsing WSDL: " + wsdl.getName() + "\n"); // binding interface
			WsdlOperation[] wsdlOperations = getOperations(wsdl);
			long start = System.currentTimeMillis();
			for (WsdlOperation operation : wsdlOperations) {
				//System.out.println(" create request="+operation.createRequest(true));
				//System.out.println(" create response="+operation.createResponse(true));
				if (writeOutResult)
					writer.write("Operation: " + operation.getName() + "\n");
				
//System.out.println("Processing request for Operation: " + operation.getName());

				List<MSSchemaTypeParser> requestSchemaTypes = parseOperationRequestSchema(operation);
				for (MSSchemaTypeParser stp: requestSchemaTypes)
					if (writeOutResult)
						writer.write(stp.toString() + "\n");

//System.out.println("Processing response for Operation: " + operation.getName());
				List<MSSchemaTypeParser> responseSchemaTypes = parseOperationResponseSchema(operation);
				for (MSSchemaTypeParser stp: responseSchemaTypes)
					if (writeOutResult)
						writer.write(stp.toString() + "\n");
				System.out.println("Processed " + operation.getName() + " in " + (System.currentTimeMillis() - start) + "ms");
				start = System.currentTimeMillis();

			}
			if (writeOutResult) {
				writer.flush();
			}
			writer2 = new BufferedWriter(
					new OutputStreamWriter(
							new FileOutputStream("C:\\nreca\\output2.txt"), 
							"utf-8"));
			System.out.println("Element xpaths count = " + ELEMENT_XPATHS.size());
			start = System.currentTimeMillis();		
			int count = 0;
			List<Xpath> xpaths = new ArrayList<Xpath>();
			for (String s : ELEMENT_XPATHS) {
				Xpath result = formXpathObject(s);
				xpaths.add(result);
				count++;
				if (count >= 500) {
					DAOUtil.getMSPXpathDAO().addXpathBatch(xpaths);
					count = 0;
					xpaths = new ArrayList<Xpath>();
				}
				if (writeOutResult)
					writer2.append(result.getXpath() +"-" + result.getServiceCode() + "-" + result.getMessageName() + "-" + result.getValueType() + "\n");
			}
			if (count > 0) {
				DAOUtil.getMSPXpathDAO().addXpathBatch(xpaths);
				count = 0;
				xpaths = new ArrayList<Xpath>();				
			}
			System.out.println("Processed ELEMENT_XPATHS of " + ELEMENT_XPATHS.size() + " records in " + (System.currentTimeMillis() - start) + "ms");
			start = System.currentTimeMillis();		
			System.out.println("Attribute xpaths count = " + ATTR_XPATHS.size());
			for (String s : ATTR_XPATHS) {
				Xpath result = formXpathObject(s);
				xpaths.add(result);
				count++;
				if (count >= 500) {
					DAOUtil.getMSPXpathDAO().addXpathBatch(xpaths);
					count = 0;
					xpaths = new ArrayList<Xpath>();
				}
				if (writeOutResult)
					writer2.append(result.getXpath() +"-" + result.getServiceCode() + "-" + result.getMessageName() + "-" + result.getValueType() + "\n");
			}
			if (count > 0) {
				DAOUtil.getMSPXpathDAO().addXpathBatch(xpaths);
				count = 0;
				xpaths = new ArrayList<Xpath>();				
			}
			System.out.println("Processed ATTR_XPATHS of " + ATTR_XPATHS.size() + " records in " + (System.currentTimeMillis() - start) + "ms");
			writer2.flush();
		} catch (UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			try {
				if (writer != null)
					writer.close();
				if (writer2 != null)
					writer2.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}

	public WsdlOperation[] getOperations(WsdlInterface wsdl) {
		WsdlOperation[] operations = new WsdlOperation[wsdl.getOperationCount()];
		for (int i=0; i < operations.length; i++)
			operations[i] = wsdl.getOperationAt(i);
		return operations;
	}

	public List<MSSchemaTypeParser> parseOperationRequestSchema(WsdlOperation operation) {
		List<MSSchemaTypeParser> schemaTypes = new ArrayList<MSSchemaTypeParser>();
		for (MessagePart msgPart : operation.getDefaultRequestParts()) {
//System.out.println("Processing msgPart: " + msgPart.getName() + "\ttype=" + msgPart.getPartType().name());

			if (msgPart.getPartType().equals(
					MessagePart.PartType.CONTENT)) {
				WsdlContentPart contentPart = (WsdlContentPart) msgPart;
				SchemaType sType = contentPart.getPartElement().getType();
				String xPath = contentPart.getPartElementName().getLocalPart();
				CURRENT_MSG_NAME = xPath;
//System.out.println("Processing CONTENT xpath: " + xPath + "\tsType="+sType.getName());
				schemaTypes.add(new MSSchemaTypeParser(sType, xPath));
			} else if (msgPart.getPartType().equals(MessagePart.PartType.HEADER) && !IS_REQUEST_HEADER_PROCESSED) { //TODO -  for v3 need to process only one set
				WsdlHeaderPart headerPart = (WsdlHeaderPart) msgPart;
				SchemaType sType = headerPart.getPartElement().getType();
				String xPath = headerPart.getPartElementName().getLocalPart();
				CURRENT_MSG_NAME = xPath;
//System.out.println("Processing HEADER xpath: " + xPath + "\tsType="+sType.getName());
				schemaTypes.add(new MSSchemaTypeParser(sType, xPath));
				IS_REQUEST_HEADER_PROCESSED = true;
				if (CURRENT_SERVICE_VERSION != null 
						&& CURRENT_SERVICE_VERSION.equals(MSPServiceOperationKey.SUPPORTED_VERSION_3)
						&& !IS_RESPONSE_HEADER_PROCESSED)
					IS_RESPONSE_HEADER_PROCESSED = true; // version 3 need to process only one time since request and response share the same header
			} else if (!msgPart.getPartType().equals(MessagePart.PartType.HEADER)) {
				System.out.println("Processing xpath NONE: part= " + msgPart.getName() + "\tpartType = " + msgPart.getPartType().name());
			}

		}
		return schemaTypes;
	}


	public List<MSSchemaTypeParser> parseOperationResponseSchema(WsdlOperation operation) {
		List<MSSchemaTypeParser> schemaTypes = new ArrayList<MSSchemaTypeParser>();
		for (MessagePart msgPart : operation.getDefaultResponseParts()) {
			if (msgPart.getPartType().equals(
					MessagePart.PartType.CONTENT)) {
				WsdlContentPart contentPart = (WsdlContentPart) msgPart;
				SchemaType sType = contentPart.getPartElement().getType();
				String xPath = contentPart.getPartElementName().getLocalPart();
				CURRENT_MSG_NAME = xPath;
				schemaTypes.add(new MSSchemaTypeParser(sType, xPath));
			} else if (msgPart.getPartType().equals(MessagePart.PartType.HEADER) && !IS_RESPONSE_HEADER_PROCESSED) {//TODO -  for v3 need to process only one set
				WsdlHeaderPart headerPart = (WsdlHeaderPart) msgPart;
				SchemaType sType = headerPart.getPartElement().getType();
				String xPath = headerPart.getPartElementName().getLocalPart();
				CURRENT_MSG_NAME = xPath;
				schemaTypes.add(new MSSchemaTypeParser(sType, xPath));
				IS_RESPONSE_HEADER_PROCESSED = true;
				if (CURRENT_SERVICE_VERSION != null 
						&& CURRENT_SERVICE_VERSION.equals(MSPServiceOperationKey.SUPPORTED_VERSION_3)
						&& !IS_REQUEST_HEADER_PROCESSED)
					IS_REQUEST_HEADER_PROCESSED = true; // version 3 need to process only one time since request and response share the same header
			}
		}
		return schemaTypes;
	}

	public static void main(String[] args) throws XmlException {
		/* process all WSDLs in v5
		CURRENT_SERVICE_VERSION = MSPServiceOperationKey.SUPPORTED_VERSION_5;
		List<String> wsdls = MultiSpeakOperationsExtractor.getListOfWSDLs();
		for (int i=39; i<40; i++) {
			System.out.println((i+1) + " - " + wsdls.get(i));
			MSParser parser = new MSParser(wsdls.get(i));
		}	
		*/	
		
		//* process all WSDLs in v3
		CURRENT_SERVICE_VERSION = MSPServiceOperationKey.SUPPORTED_VERSION_3;
		List<String> wsdls = MultiSpeakOperationsExtractor.getListOfWSDLs3();
		for (int i=0; i<wsdls.size(); i++) {
			//if (wsdls.get(i).contains("PP_Server")) {
			//if (i == 22) {//7 EA;  10 FA; 11- GIS; 14-MDM; 16-OA; 21-SGV; 22 staking
				System.out.println((i+1) + " - " + wsdls.get(i));
			MSParser parser = new MSParser(wsdls.get(i));
			//}
			//}
		}	
		
		//MSParser parser = new MSParser("file:///C:/Users/pning/Documents/NRECA/reading and research/v5/MultiSpeakV503RCEndpoints-WSDLfiles/EndPoints/AM_Server/AM_Server.wsdl");
		//				"file:///C:/Users/cpassarello/Documents/Projects/DOE/essense/essence-frontend/MultiSpeak-V503RC_Endpoints-WSDLs/EndPoints/AM_Server/AM_Server.wsdl");
		System.exit(0);
	}
}
