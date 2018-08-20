package com.essence.multispeak;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;
import java.util.logging.Logger;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;
import javax.xml.transform.Result;
import javax.xml.transform.Source;
import javax.xml.transform.sax.SAXResult;
import javax.xml.transform.stream.StreamSource;
import javax.xml.validation.Schema;
import javax.xml.validation.SchemaFactory;
import javax.xml.validation.Validator;
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
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;
import org.xml.sax.XMLReader;

import com.essence.model.Xpath;
import com.essence.persistence.DAOUtil;
import com.essence.ui.client.object.XpathDTO;

public class TestXpath {

	static private Logger logger = Logger.getLogger(TestXpath.class.getName());

	static private Set<String> ELEMENT_XPATHS = new HashSet<String>();
	static private Set<String> ATTR_XPATHS = new HashSet<String>();
	static private Set<String> COLLECTIONS_XPATHS = new HashSet<String>();
	static private String MESSAGE_NAME = null;
	static private String SERVICE_CD = null;
	
 public static void main(String argv[]) {
	 String dirName = "C:\\Users\\pning\\Documents\\NRECA\\data";
	 String filename = "od-changeoutage.xml";
	 Document doc = getDocument(dirName, filename);
	 extractCollectionXpath(doc);
	 extractXpath(doc);
	 parseXML4Xpaths(doc);
	 extractEndpointNameMessageName(doc);
	 storeXpaths();
	 reportStats();
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
 
 private static String getElementName(String s) {
	 if (s == null || s.isEmpty())
		 return null;
	 int idx = s.lastIndexOf("/");
	 return s.substring(idx+1);
 }

 private static String getAttrName(String s) {
	 if (s == null || s.isEmpty())
		 return null;
	 int idx = s.lastIndexOf("@");
	 return s.substring(idx+1);
 }
 
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

 private static void storeXpaths() {
	 
	 for (String path: ELEMENT_XPATHS) {
		 try{
			 Xpath xpath = new Xpath();
			 xpath.setFieldName(getElementName(path));
			 xpath.setIsArray(false);
			 if (path.contains("/Envelope/Header/MultiSpeakRequestMsgHeader/")) {
				 xpath.setMessageName("MultiSpeakRequestMsgHeader");
				 xpath.setServiceCode("ALL");
			 } else {
				 xpath.setMessageName(MESSAGE_NAME);
				 xpath.setServiceCode(SERVICE_CD);
			 }
			 xpath.setXpath(path);
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
			 if (path.contains("/Envelope/Header/MultiSpeakRequestMsgHeader/")) {
				 xpath.setMessageName("MultiSpeakRequestMsgHeader");
				 xpath.setServiceCode("ALL");
			 } else {
				 xpath.setMessageName(MESSAGE_NAME);
				 xpath.setServiceCode(SERVICE_CD);
			 }
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
			 xpath.setFieldName(getElementName(path));
			 xpath.setIsArray(true);
			 if (path.contains("/Envelope/Header/MultiSpeakRequestMsgHeader/")) {
				 xpath.setMessageName("MultiSpeakRequestMsgHeader");
				 xpath.setServiceCode("ALL");
			 } else {
				 xpath.setMessageName(MESSAGE_NAME);
				 xpath.setServiceCode(SERVICE_CD);
			 }
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
 
 private static void printNode(Node n, int majorlevel, int minor) {
	 StringBuffer preFix = new StringBuffer();
	 preFix.append(majorlevel).append("-").append(minor).append(" ");
	 for (int i=1; i<majorlevel; i++)
		 preFix.append("  ");
	 System.out.println(preFix + "name="+n.getNodeName()+"\ttype="+n.getNodeType()+"\tvalue="+n.getNodeValue() + "\ttextContent="+n.getTextContent());
	 NamedNodeMap nnm = n.getAttributes();
	 if (nnm != null) {
		 System.out.print(preFix+"\t");
		 for (int i=0; i<nnm.getLength(); i++) {
			 Node att = nnm.item(i);
			 if (att != null)
				 System.out.print("attname="+att.getNodeName()+",attval="+att.getNodeValue()+";");
		 }
		 System.out.println();
	 }
	 
	 NodeList children = n.getChildNodes();
	 for (int i=0; i<children.getLength(); i++)
		 printNode(children.item(i), majorlevel+1, i);
		 
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
 
 static private int countXpaths = 1;
 static private int countAttrXpaths = 1;
 private static void printNodePaths(Node n, String parentPath) {
	 if (n == null)
		 return;
	 
	 if (n.getNodeType() == Node.ATTRIBUTE_NODE && !n.getNodeName().contains("xmlns")) {
		 System.out.println(removeNamespace(n.getNodeName()) + "-" + countAttrXpaths + ":1\t" + parentPath + "/@" + removeNamespace(n.getNodeName()));
		 ATTR_XPATHS.add(parentPath + "/@" + removeNamespace(n.getNodeName()));
		 countAttrXpaths++;
	 } else if (n.getNodeType() == Node.TEXT_NODE) { // && n.getParentNode().getNodeType() == Node.DOCUMENT_NODE.COMMENT_NODE) {
		 int idx = parentPath.lastIndexOf("/");
		 String name = parentPath.substring(idx+1);
		 if (name != null && !name.equals("Envelope")) {
			 System.out.println(name + "-" + countXpaths + ": p=" + n.getParentNode().getNodeType() + "\t " + parentPath);	
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
			 System.out.println(removeNamespace(n.getNodeName()) + "-" + countXpaths + ":2\t" + parentPath + "/" + removeNamespace(n.getNodeName()));
			 ELEMENT_XPATHS.add(parentPath + "/" + removeNamespace(n.getNodeName()));
			 countXpaths++;
		 }
		 
	 }	 
 }

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
		 
		 System.out.println(removeNamespace(sib.getNodeName()) + "-" + countCollections + ":\t" + parentPath + "/" + removeNamespace(sib.getNodeName()));
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

		    @SuppressWarnings("unused")
		  Element dosAsElement = doc.getDocumentElement();
		  
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
	
 static private void parseXML4Xpaths(Document doc) {
	 if (doc == null)
		 return;
	 
	 try {
	     @SuppressWarnings("unused")
		  NodeList children = doc.getChildNodes();
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
				  System.out.println(count + "-" + cntMsg + ":" + s + "=" + msgs.item(i).getTextContent());
				  count++;
			  }
		  }
		  
		  for (String s: ATTR_XPATHS) {
			  XPathExpression msgPath = xpath.compile(s);
			  String attr = (String) msgPath.evaluate(doc, XPathConstants.STRING);
				  System.out.println(count + "-" + 99 + ":" + s + "=" + attr);
				  count++;
		  }
		  
		  for (String s: COLLECTIONS_XPATHS) {
			  XPathExpression msgPath = xpath.compile(s);
			  NodeList msgs = (NodeList) msgPath.evaluate(doc, XPathConstants.NODESET);
			  System.out.println(count + "-" + 99 + ":" + s + "=" + msgs.getLength());
		  }
		 } catch (Exception e) {
			logger.severe(e.getMessage());
		 }
 }

 @SuppressWarnings("unused")
static private void parseXML(String dirName, String filename) {
//	 File inputXMLFile = new File("C:\\Users\\pning\\Documents\\NRECA\\reading and research\\v5\\MultiSpeakV503RCEndpoints-WSDLfiles\\EndPoints\\AM_Server\\AM_Server.xsd");
	 File inputXMLFile = new File("C:\\Users\\pning\\Documents\\NRECA\\data\\od-changeoutage.xml");
	 try {
		  DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
		  DocumentBuilder db = dbf.newDocumentBuilder();
		  Document doc = db.parse(inputXMLFile);
		  doc.getDocumentElement().normalize();
		  NodeList children = doc.getChildNodes();
		  Element dosAsElement = doc.getDocumentElement();
		  System.out.println("doc name="+doc.getNodeName()+"\ttype="+doc.getNodeType()+"\tvalue="+doc.getNodeValue()+"\ttextContent="+doc.getTextContent());
		  System.out.println("dae name="+dosAsElement.getNodeName()+"\ttype="+dosAsElement.getNodeType()+"\tvalue="+dosAsElement.getNodeValue()); //+"\ttextContent="+dosAsElement.getTextContent());

		  XPathFactory xPathfactory = XPathFactory.newInstance();
		  XPath xpath = xPathfactory.newXPath();
		  
		  System.out.println("\noutageDetectionDevice:");
		  XPathExpression msgPath = xpath.compile("/Envelope/Body/ChangeOutageDetectionDevices/ArrayOfOutageDetectionDevice/outageDetectionDevice");
		  NodeList msgs = (NodeList) msgPath.evaluate(doc, XPathConstants.NODESET);
		  int cntMsg = 0;
		  for (int i=0; i<msgs.getLength(); i++)
			  printTopLevelElement(msgs.item(i), 1, cntMsg++);
		  
		  System.out.println("\noutageDetectionDevice-objectGUID:");
		  msgPath = xpath.compile("/Envelope/Body/ChangeOutageDetectionDevices/ArrayOfOutageDetectionDevice/outageDetectionDevice/@objectGUID");
		  Double num = (Double) msgPath.evaluate(doc, XPathConstants.NUMBER);
		  System.out.println("attribute value - objectGUID = " + num);
		  String numStr = (String) msgPath.evaluate(doc, XPathConstants.STRING);
		  System.out.println("attribute value - objectGUID = " + numStr);

		  System.out.println("\nextensionsItem-name:");
		  msgPath = xpath.compile("/Envelope/Body/ChangeOutageDetectionDevices/ArrayOfOutageDetectionDevice/outageDetectionDevice/assetData/assetLocation/extensionsList/extensionsItem/extName");
		  msgs = (NodeList) msgPath.evaluate(doc, XPathConstants.NODESET);
		  System.out.println("textContent = " + msgs.item(0).getTextContent());
		  cntMsg = 0;
		  for (int i=0; i<msgs.getLength(); i++)
				  printNode(msgs.item(i), 1, cntMsg++);
		  System.out.println("\nextensionsItem-value:");
		  msgPath = xpath.compile("/Envelope/Body/ChangeOutageDetectionDevices/ArrayOfOutageDetectionDevice/outageDetectionDevice/assetData/assetLocation/extensionsList/extensionsItem/extValue");
		  msgs = (NodeList) msgPath.evaluate(doc, XPathConstants.NODESET);
		  System.out.println("textContent = " + msgs.item(0).getTextContent());
		  cntMsg = 0;
		  for (int i=0; i<msgs.getLength(); i++)
				  printNode(msgs.item(i), 1, cntMsg++);
		  msgPath = xpath.compile("/Envelope/Body/ChangeOutageDetectionDevices/ArrayOfOutageDetectionDevice/outageDetectionDevice/assetData/assetLocation/extensionsList/extensionsItem/extValue/@units");
		  String unit = (String) msgPath.evaluate(doc, XPathConstants.STRING);
		  System.out.println("units = " + unit);

		  System.out.println("\nextensionsItem-name-short:");
		  msgPath = xpath.compile("//assetData/assetLocation/extensionsList/extensionsItem/extName");
		  msgs = (NodeList) msgPath.evaluate(doc, XPathConstants.NODESET);
		  System.out.println("textContent = " + msgs.item(0).getTextContent());
		  cntMsg = 0;
		  for (int i=0; i<msgs.getLength(); i++)
				  printNode(msgs.item(i), 1, cntMsg++);
		  System.out.println("\nextensionsItem-value-short:");
		  msgPath = xpath.compile("//assetData/assetLocation/extensionsList/extensionsItem/extValue");
		  msgs = (NodeList) msgPath.evaluate(doc, XPathConstants.NODESET);
		  System.out.println("textContent = " + msgs.item(0).getTextContent());
		  cntMsg = 0;
		  for (int i=0; i<msgs.getLength(); i++)
				  printNode(msgs.item(i), 1, cntMsg++);
		  msgPath = xpath.compile("//assetData/assetLocation/extensionsList/extensionsItem/extValue/@units");
		  unit = (String) msgPath.evaluate(doc, XPathConstants.STRING);
		  System.out.println("units = " + unit);

		  System.out.println("\nextensionsItem-org:");
		  msgPath = xpath.compile("//assetData/organizationAssociations/organizationAssociation/extensionsList");
		  msgs = (NodeList) msgPath.evaluate(doc, XPathConstants.NODESET);
		  System.out.println("textContent = " + msgs.item(0).getTextContent());
		  cntMsg = 0;
		  for (int i=0; i<msgs.getLength(); i++)
				  printNode(msgs.item(i), 1, cntMsg++);

		  /*
		  System.out.println("\nextvaluess:");
		  msgPath = xpath.compile("//extValue");
		  msgs = (NodeList) msgPath.evaluate(doc, XPathConstants.NODESET);
		  cntMsg = 0;
		  for (int i=0; i<msgs.getLength(); i++)
				  printNode(msgs.item(i), 1, cntMsg++);
		  

		  XPathExpression expr = xpath.compile("/definitions/portType/operation");
//		  XPathExpression expr = xpath.compile("/howto/topic[@name='PowerBuilder']/url");
		  NodeList nl = (NodeList) expr.evaluate(doc, XPathConstants.NODESET);
		  System.out.println("\nPortType Operations:");
		  for (int i=0; i<nl.getLength(); i++) {
			  printWSDLOperationInPortType(nl.item(i), i);
		  }
		  */
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
 }

 @SuppressWarnings("unused")
 static private void testValidationRule() {
	 File inputXMLFile = new File("input.xml");
	 File schemaFile = new File("inputXML.xsd");

	 FileReader fileReader = null;
	 InputSource inputSource = null;
	 DocumentBuilder builder = null;
	 SAXParserFactory saxFactory = SAXParserFactory.newInstance();
	 DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();

	 try {
	 	builder = dbf.newDocumentBuilder();

	 	SAXParser saxParser = saxFactory.newSAXParser();
	 	XMLReader xmlReader = saxParser.getXMLReader();

	 	fileReader = new FileReader(inputXMLFile);
	 	inputSource = new InputSource(fileReader);
	 	xmlReader.parse(inputSource);

	 	SchemaFactory factory = SchemaFactory
	 			.newInstance("http://www.w3.org/2001/XMLSchema");
	 	Schema schema = factory.newSchema(schemaFile);
	 	Validator validator = schema.newValidator();
	 	Source source = new StreamSource(fileReader);
	 	Result result = new SAXResult();
	 	validator.validate(source, result);

	 } catch (ParserConfigurationException e) {
	 	logger.severe(e.getMessage());
	 } catch (SAXException e) {
	 	logger.severe(e.getMessage());
	 } catch (FileNotFoundException e) {
	 	logger.severe(e.getMessage());
	 } catch (IOException e) {
	 	logger.severe(e.getMessage());
	 }
 }
}
