/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.multispeak;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;
import java.io.Writer;
import java.util.HashSet;
import java.util.Set;
import java.util.logging.Logger;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;

import org.hibernate.exception.ConstraintViolationException;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

import com.essence.persistence.DAOUtil;
import com.essence.model.Xpath;
import com.essence.ui.shared.StringUtil;

public class MultiSpeakMsgXpathExtractor {

	static private Logger logger = Logger.getLogger(MultiSpeakMsgXpathExtractor.class.getName());

	static private Set<String> ELEMENT_XPATHS = null;
	static private Set<String> ATTR_XPATHS = null;
	static private Set<String> COLLECTIONS_XPATHS = null;
	static private String MESSAGE_NAME = null;
	static private String SERVICE_CD = null;

	static MSParser parser = new MSParser("file:///C:/Users/pning/Documents/NRECA/reading and research/v5/MultiSpeakV503RCEndpoints-WSDLfiles/EndPoints/OD_Server/OD_Server-rev.wsdl");

	public static void main(String argv[]) {
	    @SuppressWarnings("unused")
		MSParser parser = new MSParser("file:///C:/Users/pning/Documents/NRECA/reading and research/v5/MultiSpeakV503RCEndpoints-WSDLfiles/EndPoints/OD_Server/OD_Server-rev.wsdl");
		processSOAPUIMessage("C:\\Users\\pning\\Documents\\NRECA\\data", "od-changeoutage-resp.xml");
	} 

	private static void processSOAPUIMessage(String dirName, String filename) {
		
		ELEMENT_XPATHS = new HashSet<String>();
		ATTR_XPATHS = new HashSet<String>();
		COLLECTIONS_XPATHS = new HashSet<String>();
		MESSAGE_NAME = null;
		SERVICE_CD = null;
		
		Document doc = getDocument(dirName, filename);
		extractCollectionXpath(doc);
		extractXpath(doc);
		//parseXML4Xpaths(doc);
		//extractEndpointNameMessageName(doc);
		//storeXpaths();
		reportStats();		
		compare(); // compare the instance based extracted xpaths against the schema based extraction 
		System.exit(0);
	}
	
	private static String getSubXpath(String xpath) {
		if (StringUtil.stringHasValue(xpath)) {
			if (xpath.contains(Xpath.BODY_SIGNATURE_PATH)) {
				return xpath.substring(Xpath.BODY_SIGNATURE_PATH.length());
			} else if (xpath.contains(Xpath.HEADER_SIGNATURE_PATH))
				return xpath.substring(Xpath.HEADER_SIGNATURE_PATH.length());
			else
				return xpath;
		} else
			return xpath;
	}
	
	private static void compare() {
		try {
			Set<String> elePaths = new HashSet<String>();
			Set<String> attPaths = new HashSet<String>();
			Writer writer = new BufferedWriter(
					new OutputStreamWriter(
							new FileOutputStream("C:\\nreca\\outputCompare-resp.txt"),
							"utf-8"));

			int countEle = 0, countAtt = 0;
			for (String s : ELEMENT_XPATHS)
				elePaths.add(getSubXpath(s));
			
			for (String s : ATTR_XPATHS)
				attPaths.add(getSubXpath(s));

			for (String s : elePaths) {
				if (!parser.ELEMENT_XPATHS.contains(s)) {
					if (s.endsWith("/extensions"))
						writer.write("\t");
						writer.write("NOT IN PARSER: " +s+"\n");
						countEle++;
				}
			}
			for (String s: attPaths) {
				if (!parser.ATTR_XPATHS.contains(s)) {
					if (s.endsWith("/extensions"))
						writer.write("\t");
					writer.write("NOT IN PARSER: " +s+"\n");
					countAtt++;
				}
			}
			writer.write("ELE NOT IN P Count = " + countEle + "\t ATT NOT IN P count = " + countAtt + "\n");
			countEle = 0;
			countAtt = 0;
			for (String s : parser.ELEMENT_XPATHS) {
				if (!elePaths.contains(s)) {
					writer.write("NOT IN REQ: "+s+"\n");
					countEle++;
				}
			}
			for (String s: parser.ATTR_XPATHS) {
				if (!attPaths.contains(s)) {
					writer.write("NOT IN REQ: "+s+"\n");
					countAtt++;
				}
			}
			writer.write("ELE NOT IN P Count = " + countEle + "\t ATT NOT IN P count = " + countAtt +"\n");
			writer.flush();
			writer.close();
		} catch (UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
		// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	private static void reportStats() {
		logger.info("ELEMENT_XPATHS size = " + ELEMENT_XPATHS.size());
		logger.info("ATTR_XPATHS size = " + ATTR_XPATHS.size());
		logger.info("COLLECTIONS_XPATHS size = " + COLLECTIONS_XPATHS.size());

		int dupCount = 0;
		int tooLargeCount = 0;
		for (String e : ELEMENT_XPATHS) {
			if (ATTR_XPATHS.contains(e)) {
				logger.info(e + " from ELEMENT_XPATHS is also in ATTR_XPATHS");
				dupCount++;
			} else if (COLLECTIONS_XPATHS.contains(e)) {
				logger.info(e + " from ELEMENT_XPATHS is also in COLLECTIONS_XPATHS");
				dupCount++;			 
			}
			if (e.length() > 256) {
				logger.info("Element is too large: size = " + e.length() + " value = \n" + e);
				tooLargeCount++;
			}
		}

		for (String e : ATTR_XPATHS) {
			if (ELEMENT_XPATHS.contains(e)) {
				logger.info(e + " from ATTR_XPATHS is also in ELEMENT_XPATHS");
				dupCount++;
			} else if (COLLECTIONS_XPATHS.contains(e)) {
				logger.info(e + " from ATTR_XPATHS is also in COLLECTIONS_XPATHS");
				dupCount++;			 
			}
			if (e.length() > 256) {
				logger.info("ATTR is too large: size = " + e.length() + " value = \n" + e);
				tooLargeCount++;
			}
		}

		for (String e : COLLECTIONS_XPATHS) {
			if (ELEMENT_XPATHS.contains(e)) {
				logger.info(e + " from COLLECTIONS_XPATHS is also in ELEMENT_XPATHS");
				dupCount++;
			} else if (ATTR_XPATHS.contains(e)) {
				logger.info(e + " from COLLECTIONS_XPATHS is also in ATTR_XPATHS");
				dupCount++;			 
			}
			if (e.length() > 256) {
				logger.info("Collection is too large: size = " + e.length() + " value = \n" + e);
				tooLargeCount++;
			}
		}

		logger.info("total dupCount = " + dupCount);
		logger.info("total tooLargeCount = " + tooLargeCount); 
	}



	private static String getAttrName(String s) {
		if (s == null || s.isEmpty())
			return null;
		int idx = s.lastIndexOf("@");
		return s.substring(idx+1);
	}

	@SuppressWarnings("unused")
    private static void extractEndpointNameMessageName(Document doc) {
		if (doc == null)
			return;

		XPathFactory xPathfactory = XPathFactory.newInstance();
		XPath xpath = xPathfactory.newXPath();

		XPathExpression msgPath = null;
		try {
			msgPath = xpath.compile("/Envelope/Body");
		} catch (XPathExpressionException e) {
			logger.warning(e.getMessage());
		}

		Node body = null;
		try {
			body = (Node) msgPath.evaluate(doc, XPathConstants.NODE);
		} catch (XPathExpressionException e) {
			logger.warning(e.getMessage());	  
		}
		NodeList children = body.getChildNodes();

		for (int i=0; i<children.getLength(); i++) {
			if (children.item(i).getNodeType() == Node.ELEMENT_NODE) {
				int idx = children.item(i).getNodeName().indexOf(":");
				SERVICE_CD = children.item(i).getNodeName().substring(0, idx);
				MESSAGE_NAME = children.item(i).getNodeName().substring(idx+1);
			}
		}
	}

	@SuppressWarnings("unused")
    private static void storeXpaths() {

		for (String path: ELEMENT_XPATHS) {
			try{
				Xpath xpath = new Xpath();
				xpath.setFieldName(StringUtil.getElementNameFromXpath(path));
				xpath.setIsArray(false);
				if (path.contains(Xpath.REQUEST_HEADER_SIGNATURE_PATH)) {
					xpath.setMessageName(Xpath.REQUEST_HEADER_MESSAGE_NAME);
					xpath.setServiceCode(Xpath.HEADER_SERVICE_CD);
				} else if (path.contains(Xpath.RESPONSE_HEADER_SIGNATURE_PATH)) {
					xpath.setMessageName(Xpath.RESPONSE_HEADER_MESSAGE_NAME);
					xpath.setServiceCode(Xpath.HEADER_SERVICE_CD);
				} else {
					xpath.setMessageName(MESSAGE_NAME);
					xpath.setServiceCode(SERVICE_CD);
				}
				xpath.setXpath(path);
				xpath.setVersion(MSPServiceOperationKey.SUPPORTED_VERSION_5);
				DAOUtil.getMSPXpathDAO().addXpath(xpath);
			} catch (ConstraintViolationException ex) {
				logger.warning("1path=" + path);			 
				logger.warning("1msg=" + ex.getMessage());
			}
			catch (Exception e) {
				logger.warning("1path=" + path);
				logger.warning("1msg=" + e.getMessage());
			}
		}

		for (String path: ATTR_XPATHS) {
			try {
				Xpath xpath = new Xpath();
				xpath.setFieldName(getAttrName(path));
				xpath.setIsArray(false);
				if (path.contains(Xpath.REQUEST_HEADER_SIGNATURE_PATH)) {
					xpath.setMessageName(Xpath.REQUEST_HEADER_MESSAGE_NAME);
					xpath.setServiceCode(Xpath.HEADER_SERVICE_CD);
				}else if (path.contains(Xpath.RESPONSE_HEADER_SIGNATURE_PATH)) {
					xpath.setMessageName(Xpath.RESPONSE_HEADER_MESSAGE_NAME);
					xpath.setServiceCode(Xpath.HEADER_SERVICE_CD);
				} else {
					xpath.setMessageName(MESSAGE_NAME);
					xpath.setServiceCode(SERVICE_CD);
				}
				xpath.setVersion(MSPServiceOperationKey.SUPPORTED_VERSION_5);
				xpath.setXpath(path);
				DAOUtil.getMSPXpathDAO().addXpath(xpath);
			} catch (ConstraintViolationException ex) {
				logger.warning("2path=" + path);			 
				logger.warning("2msg=" + ex.getMessage());
			} catch (Exception e) {
				logger.warning("2path=" + path);
				logger.warning("2msg=" + e.getMessage());
			}
		}

		for (String path: COLLECTIONS_XPATHS) {
			try {
				Xpath xpath = new Xpath();
				xpath.setFieldName(StringUtil.getElementNameFromXpath(path));
				xpath.setIsArray(true);
				if (path.contains(Xpath.REQUEST_HEADER_SIGNATURE_PATH)) {
					xpath.setMessageName(Xpath.REQUEST_HEADER_MESSAGE_NAME);
					xpath.setServiceCode(Xpath.HEADER_SERVICE_CD);
				}else if (path.contains(Xpath.RESPONSE_HEADER_SIGNATURE_PATH)) {
					xpath.setMessageName(Xpath.RESPONSE_HEADER_MESSAGE_NAME);
					xpath.setServiceCode(Xpath.HEADER_SERVICE_CD);
				} else {
					xpath.setMessageName(MESSAGE_NAME);
					xpath.setServiceCode(SERVICE_CD);
				}
				xpath.setVersion(MSPServiceOperationKey.SUPPORTED_VERSION_5);
				xpath.setXpath(path);
				DAOUtil.getMSPXpathDAO().addXpath(xpath);
			} catch (ConstraintViolationException ex) {
				logger.warning("3path=" + path);			 
				logger.warning("3msg=" + ex.getMessage());
			} catch (Exception e) {
				logger.warning("3path=" + path);
				logger.warning("3msg=" + e.getMessage());
			}
		}
	}

	private static String removeNamespace(String s) {
		if (s == null || s.isEmpty())
			return s;
		int idx = s.lastIndexOf(":");
		return s.substring(idx+1);
	}

	private static boolean hasElementChild(Node n) {
		if (n == null)
			return false;

		NodeList children = n.getChildNodes();
		if (children != null) {
			for (int i=0; i<children.getLength(); i++)
				if (children.item(i).getNodeType() == Node.ELEMENT_NODE)
					return true;
		}

		return false;
	}

    @SuppressWarnings("unused")
    static private int countXpaths = 1;
    @SuppressWarnings("unused")
	static private int countAttrXpaths = 1;
	private static void printNodePaths(Node n, String parentPath) {
		if (n == null)
			return;

		if (n.getNodeType() == Node.ATTRIBUTE_NODE && !n.getNodeName().contains("xmlns")) {
			//System.out.println(removeNamespace(n.getNodeName()) + "-" + countAttrXpaths + ":1\t" + parentPath + "/@" + removeNamespace(n.getNodeName()));
			ATTR_XPATHS.add(parentPath + "/@" + removeNamespace(n.getNodeName()));
			countAttrXpaths++;
		} else if (n.getNodeType() == Node.TEXT_NODE) { // && n.getParentNode().getNodeType() == Node.DOCUMENT_NODE.COMMENT_NODE) {
			int idx = parentPath.lastIndexOf("/");
			String name = parentPath.substring(idx+1);
			if (name != null && !name.equals("Envelope")) {
				//System.out.println(name + "-" + countXpaths + ": p=" + n.getParentNode().getNodeType() + "\t " + parentPath);	
				ELEMENT_XPATHS.add(parentPath);
				countXpaths++;
			}
		} else {
			NamedNodeMap nnm = n.getAttributes();
			if (nnm != null) {
				for (int i=0; i<nnm.getLength(); i++) {
					Node att = nnm.item(i);
					if (att != null)
						printNodePaths(att, parentPath + "/" + removeNamespace(n.getNodeName()));
				}
			}

			if (hasElementChild(n)) {
				NodeList children = n.getChildNodes();
				if (children != null) {
					for (int i=0; i<children.getLength(); i++)
						if (children.item(i).getNodeType() == Node.ELEMENT_NODE)
							printNodePaths(children.item(i), parentPath + "/" + removeNamespace(n.getNodeName()));
				}
			} else {
				//System.out.println(removeNamespace(n.getNodeName()) + "-" + countXpaths + ":2\t" + parentPath + "/" + removeNamespace(n.getNodeName()));
				ELEMENT_XPATHS.add(parentPath + "/" + removeNamespace(n.getNodeName()));
				countXpaths++;
			}

		}	 
	}

    @SuppressWarnings("unused")
	private static int countCollections = 1;

	private static void printNodeCollectionPaths(Node n, String parentPath) {
		if (n == null)
			return;

		if (n.getNodeType() == Node.COMMENT_NODE && n.getNodeValue() != null && n.getNodeValue().contains("or more repetitions:")) {
			Node parent = n.getParentNode();
			Node sib = null;
			NodeList children = parent.getChildNodes();
			for (int i=0; i<children.getLength(); i++) {
				if (children.item(i).getNodeType() == Node.ELEMENT_NODE)
					sib = children.item(i);
			}

			//System.out.println(removeNamespace(sib.getNodeName()) + "-" + countCollections + ":\t" + parentPath + "/" + removeNamespace(sib.getNodeName()));
			COLLECTIONS_XPATHS.add(parentPath + "/" + removeNamespace(sib.getNodeName()));
			countCollections++;
		} else {
			if (hasElementChild(n)) {
				NodeList children = n.getChildNodes();
				if (children != null) {
					for (int i=0; i<children.getLength(); i++)
						printNodeCollectionPaths(children.item(i), parentPath + "/" + removeNamespace(n.getNodeName()));
				}
			} 
		}	 
	}

	private static void printTopLevelElement(Node n, int majorlevel, int minor) {
		if (n == null)
			return;
		StringBuffer preFix = new StringBuffer();
		preFix.append(majorlevel).append("-").append(minor).append(" ");
		System.out.print(n.getNodeName()+":"+preFix);
		NamedNodeMap nnm = n.getAttributes();
		if (nnm != null)
			for (int i=0; i<nnm.getLength(); i++) {
				Node att = nnm.item(i);
				System.out.print("\t"+att.getNodeName()+"="+att.getNodeValue());
			}
		System.out.println();
	}

	static private Document getDocument(String dirName, String filename) {
		File inputXMLFile = new File(dirName + "/" + filename); //C:\\Users\\pning\\Documents\\NRECA\\data\\od-changeoutage.xml");
		try {
			DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
			//dbf.setNamespaceAware(true); // Make sure it's not namespace aware for the xpath to work 
			DocumentBuilder db = dbf.newDocumentBuilder();
			Document doc = db.parse(inputXMLFile);
			doc.getDocumentElement().normalize();
			if (dbf.isNamespaceAware())
				System.out.println("dbf is ns aware");
			else
				System.out.println("dbf is not ns aware");
			if (db.isNamespaceAware())
				System.out.println("db is ns aware");
			else
				System.out.println("db is not ns aware");
			return doc;
		} catch (ParserConfigurationException e) {
			logger.severe(e.getMessage());
		} catch (SAXException e) {
			logger.severe(e.getMessage());
		} catch (FileNotFoundException e) {
			logger.severe(e.getMessage());
		} catch (IOException e) {
			logger.severe(e.getMessage());
		} catch (Exception e) {
			logger.severe(e.getMessage());
		} 

		return null;
	}

	static private void extractCollectionXpath(Document doc) {
		//File inputXMLFile = new File("C:\\Users\\pning\\Documents\\NRECA\\data\\od-changeoutage.xml");
		if (doc == null)
			return;

		try {
			/*
		  DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
		  DocumentBuilder db = dbf.newDocumentBuilder();
		  Document doc = db.parse(inputXMLFile);
		  doc.getDocumentElement().normalize();
			 */
			NodeList children = doc.getChildNodes();
			int cnt = 0;
			System.out.println("\nPrint all doc nodes:");
			for (int i=0; i<children.getLength(); i++)
				printTopLevelElement(children.item(i), 1, cnt++);

			System.out.println("\nPrint all Xpaths:");
			Node child = doc.getFirstChild();
			//		  printNodeCollectionPaths(child, "");
			children = child.getChildNodes();
			for (int i=0; i<children.getLength(); i++)
				printNodeCollectionPaths(children.item(i), "/"+removeNamespace(child.getNodeName()));

		} catch (Exception e) {
			logger.severe(e.getMessage());
		}
	}

	static private void extractXpath(Document doc) {
		if (doc == null)
			return;

		try {
			NodeList children = doc.getChildNodes();
			int cnt = 0;
			System.out.println("\nPrint all doc nodes:");
			for (int i=0; i<children.getLength(); i++)
				printTopLevelElement(children.item(i), 1, cnt++);

			//Element dosAsElement = doc.getDocumentElement();

			System.out.println("\nPrint first doc nodes:");
			Node child = doc.getFirstChild();
			printTopLevelElement(child, 1, 0);

			System.out.println("\nPrint all children of first doc node:");
			NodeList elements = child.getChildNodes();
			cnt = 0;
			for (int i=0; i<elements.getLength(); i++)
				printTopLevelElement(elements.item(i), 1, cnt++);

			System.out.println("\nPrint all Xpaths:");
			// printNodePaths(child, "");
			for (int i=0; i<elements.getLength(); i++)
				printNodePaths(elements.item(i), "/"+removeNamespace(child.getNodeName()));		  
		} catch (Exception e) {
			logger.severe(e.getMessage());
		}
	}

    @SuppressWarnings("unused")
	static private void parseXML4Xpaths(Document doc) {
		if (doc == null)
			return;

		try {
			Element dosAsElement = doc.getDocumentElement();
			System.out.println("doc name="+doc.getNodeName()+"\ttype="+doc.getNodeType()+"\tvalue="+doc.getNodeValue()+"\ttextContent="+doc.getTextContent());
			System.out.println("dae name="+dosAsElement.getNodeName()+"\ttype="+dosAsElement.getNodeType()+"\tvalue="+dosAsElement.getNodeValue()); //+"\ttextContent="+dosAsElement.getTextContent());

			XPathFactory xPathfactory = XPathFactory.newInstance();
			XPath xpath = xPathfactory.newXPath();

			int count = 1;
			for (String s: ELEMENT_XPATHS) {
				XPathExpression msgPath = xpath.compile(s);
				NodeList msgs = (NodeList) msgPath.evaluate(doc, XPathConstants.NODESET);
				int cntMsg = 0;
				for (int i=0; i<msgs.getLength(); i++) {
					System.out.println(count + "-E" + cntMsg + ":" + s + "=" + msgs.item(i).getTextContent());
				}
				count++;
			}

			for (String s: ATTR_XPATHS) {
				XPathExpression msgPath = xpath.compile(s);
				String attr = (String) msgPath.evaluate(doc, XPathConstants.STRING);
				System.out.println(count + "-A" + 99 + ":" + s + "=" + attr);
				count++;
			}

			for (String s: COLLECTIONS_XPATHS) {
				XPathExpression msgPath = xpath.compile(s);
				NodeList msgs = (NodeList) msgPath.evaluate(doc, XPathConstants.NODESET);
				System.out.println(count + "-C" + 99 + ":" + s + "=" + msgs.getLength());
				count++;
			}
		} catch (Exception e) {
			logger.severe(e.getMessage());
		}
	}
}
