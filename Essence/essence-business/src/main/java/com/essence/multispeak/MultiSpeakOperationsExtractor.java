/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.multispeak;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

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
import javax.xml.xpath.XPathFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;
import org.xml.sax.XMLReader;

import com.essence.persistence.DAOUtil;
import com.essence.ui.shared.StringUtil;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.logging.Logger;

public class MultiSpeakOperationsExtractor {
	static private Logger logger = Logger.getLogger(MultiSpeakOperationsExtractor.class
			.getName());

	public static void main(String argv[]) {
		/*
		 * java.text.SimpleDateFormat f = new java.text.SimpleDateFormat(); try
		 * { Date d = f.parse("09/23/2012"); } catch (Exception e) {
		 * e.printStackTrace(); }
		 */
		//parseXSDPrint("C:\\Users\\pning\\Documents\\NRECA\\reading and research\\v5\\MultiSpeakV503RCEndpoints-WSDLfiles\\EndPoints\\AM_Server\\AM_Server.xsd");
		//parseWSDLPrint("C:\\Users\\pning\\Documents\\NRECA\\reading and research\\v5\\MultiSpeakV503RCEndpoints-WSDLfiles\\EndPoints\\AM_Server\\AM_Server.wsdl");

		//parseWSDL("C:\\Users\\pning\\Documents\\NRECA\\reading and research\\v3ac\\MultiSpeakBusArchitecture_V30ac_WSDLs\\CB_Server.wsdl"); // C:\\Users\\pning\\Documents\\NRECA\\reading and research\\v5\\MultiSpeakV503RCEndpoints-WSDLfiles\\EndPoints\\AM_Server\\AM_Server.wsdl");
		
		// v5
		
		List<String> wsdls = getListOfWSDLs();
		for (int i=0; i<wsdls.size(); i++) {
			System.out.println((i+1) + " - " + wsdls.get(i));
			//if (wsdls.get(i).contains("CB_Server"))
			parseWSDL(wsdls.get(i), MSPServiceOperationKey.SUPPORTED_VERSION_5);
		}
		
		
		
		// v3ac
		List<String> wsdls3 = getListOfWSDLs3();
		for (int i=0; i<wsdls3.size(); i++) {
			System.out.println((i+1) + " - " + wsdls3.get(i));
			//if (wsdls3.get(i).contains("CB_Server.wsdl"))
				parseWSDL(wsdls3.get(i), MSPServiceOperationKey.SUPPORTED_VERSION_3);
		}		
	}

	static private String getWSDLFile(File dir) {
		if (dir == null || !dir.isDirectory())
			return null;
		File[] files = dir.listFiles();
		for (int i=0; i<files.length; i++)
			if (files[i].getName().equals(dir.getName()+".wsdl"))
				return files[i].getName();
		return null;
	}
	
	static public List<String> getListOfWSDLs() {
		String root = "C:\\Users\\pning\\Documents\\NRECA\\reading and research\\v5\\MultiSpeakV503RCEndpoints-WSDLfiles\\EndPoints";
		List<String> wsdlFileNames = new ArrayList<String>();
		File rootDir = new File(root);
		File[] subDirs = rootDir.listFiles();
		for (int i=0; i<subDirs.length; i++) {
			try {
				System.out.println((i+1) + "- absPath=" + subDirs[i].getAbsolutePath() + "\tcanPath" + subDirs[i].getCanonicalPath() + "\tpath=" + subDirs[i].getPath() + "\tname=" + subDirs[i].getName());
				System.out.println("wsdl: " + getWSDLFile(subDirs[i]));
				if (getWSDLFile(subDirs[i]) != null)
					wsdlFileNames.add(subDirs[i].getAbsolutePath() + "\\" + getWSDLFile(subDirs[i]));
			} catch (IOException ex) {
				System.out.println("ERROR: " + ex.getMessage());
			}
		}

		return wsdlFileNames;
	}

	static public List<String> getListOfWSDLs3() {
		String root = "C:\\Users\\pning\\Documents\\NRECA\\reading and research\\v3ac\\MultiSpeakBusArchitecture_V30ac_WSDLs";
		List<String> wsdlFileNames = new ArrayList<String>();
		
		File rootDir = new File(root);
		if (rootDir == null || !rootDir.isDirectory())
			return wsdlFileNames;
		File[] files = rootDir.listFiles();
		for (int i=0; i<files.length; i++)
			if (files[i].getName().endsWith(".wsdl"))
				wsdlFileNames.add(rootDir.getAbsolutePath() + "\\" + files[i].getName());
		return wsdlFileNames;
	}

	@SuppressWarnings("unused")
    static private void parseXSDPrint(String filename) {
		File inputXMLFile = new File(filename);
		// File schemaFile = new File("inputXML.xsd");

		try {
			DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
			DocumentBuilder db = dbf.newDocumentBuilder();
			Document doc = db.parse(inputXMLFile);
			doc.getDocumentElement().normalize();
			NodeList children = doc.getChildNodes();
			Element dosAsElement = doc.getDocumentElement();
			System.out.println("doc name=" + doc.getNodeName() + "\ttype="
					+ doc.getNodeType() + "\tvalue=" + doc.getNodeValue()
					+ "\ttextContent=" + doc.getTextContent());
			System.out.println("dae name=" + dosAsElement.getNodeName()
					+ "\ttype=" + dosAsElement.getNodeType() + "\tvalue="
					+ dosAsElement.getNodeValue() + "\ttextContent="
					+ dosAsElement.getTextContent());
			Node child = doc.getFirstChild();
			printNode(child, 1, 0);

			NodeList elements = child.getChildNodes();
			int cnt = 0;
			for (int i = 0; i < elements.getLength(); i++)
				if (elements.item(i).getNodeName().contains("xs:element"))
					printTopLevelElement(elements.item(i), 1, cnt++);

		} catch (ParserConfigurationException e) {
			logger.severe(e.getMessage());
		} catch (SAXException e) {
			logger.severe(e.getMessage());
		} catch (FileNotFoundException e) {
			logger.severe(e.getMessage());
		} catch (IOException e) {
			logger.severe(e.getMessage());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	@SuppressWarnings("unused")
    static private void parseWSDLPrint(String filename) {
		File inputXMLFile = new File(filename);
		// File schemaFile = new File("inputXML.xsd");

		try {
			DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
			DocumentBuilder db = dbf.newDocumentBuilder();
			Document doc = db.parse(inputXMLFile);
			doc.getDocumentElement().normalize();
			NodeList children = doc.getChildNodes();
			Element dosAsElement = doc.getDocumentElement();
			System.out.println("doc name=" + doc.getNodeName() + "\ttype="
					+ doc.getNodeType() + "\tvalue=" + doc.getNodeValue()
					+ "\ttextContent=" + doc.getTextContent());
			System.out.println("dae name=" + dosAsElement.getNodeName()
					+ "\ttype=" + dosAsElement.getNodeType() + "\tvalue="
					+ dosAsElement.getNodeValue() + "\ttextContent="
					+ dosAsElement.getTextContent());
			// Node child = doc.getFirstChild();
			// printNode(child, 1, 0);

			XPathFactory xPathfactory = XPathFactory.newInstance();
			XPath xpath = xPathfactory.newXPath();

			System.out.println("\nServices:");
			NodeList services = doc.getElementsByTagName("wsdl:service");
			for (int i = 0; i < services.getLength(); i++) {
				NamedNodeMap m1 = services.item(i).getAttributes();
				System.out.print(services.item(i).getNodeName() + ":\t");
				for (int j = 0; j < m1.getLength(); j++)
					System.out.print(m1.item(j).getNodeName() + "="
							+ m1.item(j).getNodeValue() + "; ");
				System.out.println();
			}

			/*
			 * System.out.println("\nMEssages:"); NodeList elements =
			 * child.getChildNodes(); int cnt = 0; for (int i=0;
			 * i<elements.getLength(); i++) if
			 * (elements.item(i).getNodeName().contains("wsdl:message"))
			 * printTopLevelMessage(elements.item(i), 1, cnt++);
			 */

			System.out.println("\nMessages:");
			XPathExpression msgPath = xpath.compile("/definitions/message");
			NodeList msgs = (NodeList) msgPath.evaluate(doc,
					XPathConstants.NODESET);
			int cntMsg = 0;
			for (int i = 0; i < msgs.getLength(); i++)
				printTopLevelMessage(msgs.item(i), 1, cntMsg++);

			XPathExpression expr = xpath
					.compile("/definitions/portType/operation");
			// XPathExpression expr =
			// xpath.compile("/howto/topic[@name='PowerBuilder']/url");
			NodeList nl = (NodeList) expr.evaluate(doc, XPathConstants.NODESET);
			System.out.println("\nPortType Operations:");
			for (int i = 0; i < nl.getLength(); i++) {
				printWSDLOperationInPortType(nl.item(i), i);
			}

			XPathExpression expr2 = xpath
					.compile("/definitions/binding/operation");
			// XPathExpression expr =
			// xpath.compile("/howto/topic[@name='PowerBuilder']/url");
			NodeList nl2 = (NodeList) expr2.evaluate(doc,
					XPathConstants.NODESET);
			System.out.println("\nSOAP Binding Operations:");
			for (int i = 0; i < nl2.getLength(); i++) {
				printWSDLOperationInBinding(nl2.item(i), i);
			}

		} catch (ParserConfigurationException e) {
			logger.severe(e.getMessage());
		} catch (SAXException e) {
			logger.severe(e.getMessage());
		} catch (FileNotFoundException e) {
			logger.severe(e.getMessage());
		} catch (IOException e) {
			logger.severe(e.getMessage());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	static public void parseWSDL(String filename, String version) {
		File inputXMLFile = new File(filename);
		Map<String, MSPServiceOperation> operations = new HashMap<String, MSPServiceOperation>();
		Map<String, String> messageElementMapping = new HashMap<String, String>();

		try {
			DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
			DocumentBuilder db = dbf.newDocumentBuilder();
			Document doc = db.parse(inputXMLFile);
			doc.getDocumentElement().normalize();
		    @SuppressWarnings("unused")
			NodeList children = doc.getChildNodes();
			Element dosAsElement = doc.getDocumentElement();
			System.out.println("doc name=" + doc.getNodeName() + "\ttype="
					+ doc.getNodeType() + "\tvalue=" + doc.getNodeValue()
					+ "\ttextContent=" + doc.getTextContent());
			System.out.println("dae name=" + dosAsElement.getNodeName()
					+ "\ttype=" + dosAsElement.getNodeType() + "\tvalue="
					+ dosAsElement.getNodeValue()); // + "\ttextContent=" + dosAsElement.getTextContent());

			XPathFactory xPathfactory = XPathFactory.newInstance();
			XPath xpath = xPathfactory.newXPath();

			String service = null;
			
			System.out.println("\nServices:");
			NodeList services = doc.getElementsByTagName("wsdl:service");
			for (int i = 0; i < services.getLength(); i++) {
				NamedNodeMap m1 = services.item(i).getAttributes();
				System.out.print(services.item(i).getNodeName() + ":\t");
				for (int j = 0; j < m1.getLength(); j++) {
					System.out.print(m1.item(j).getNodeName() + "="
							+ m1.item(j).getNodeValue() + "; ");
					if (m1.item(j).getNodeName().contains("name"))
						service = m1.item(j).getNodeValue(); // obtained service name
				}
				System.out.println();
			}
			
			System.out.println("\nMessages:");
			XPathExpression msgPath = xpath.compile("/definitions/message");
			NodeList msgs = (NodeList) msgPath.evaluate(doc,
					XPathConstants.NODESET);
			int cntMsg = 0;
			for (int i = 0; i < msgs.getLength(); i++) {
				printTopLevelMessage(msgs.item(i), 1, cntMsg++);
				//messageElementMapping
				NamedNodeMap nnm = msgs.item(i).getAttributes();
				String msgName = null;
				String msgElement = null;
				for (int j = 0; j < nnm.getLength(); j++) {
					Node att = nnm.item(j);
					if (att.getNodeName().equals("name"))
						msgName = att.getNodeValue();
				}

				NodeList nl = msgs.item(i).getChildNodes();
				if (nl != null)
					for (int l = 0; l <nl.getLength(); l++) {
						if (nl.item(l).getNodeName().contains("wsdl:part")) {
							Node part = nl.item(l); // part
							NamedNodeMap nnm1 = part.getAttributes();
							if (nnm1 != null)
								for (int k = 0; k < nnm1.getLength(); k++) {
									Node att = nnm1.item(k);
									if (att.getNodeName().equals("element"))
										msgElement = att.getNodeValue();
								}
						}
					}
				messageElementMapping.put(msgName, StringUtil.removeNamespace(msgElement));
			}

			XPathExpression expr = xpath
					.compile("/definitions/portType/operation");
			// XPathExpression expr =
			// xpath.compile("/howto/topic[@name='PowerBuilder']/url");
			NodeList nl = (NodeList) expr.evaluate(doc, XPathConstants.NODESET);
			System.out.println("\nPortType Operations:");
			for (int i = 0; i < nl.getLength(); i++) {
				parseWSDLOperationInPortType(nl.item(i), i, service, operations);
			}

			XPathExpression expr2 = xpath
					.compile("/definitions/binding/operation");
			// XPathExpression expr =
			// xpath.compile("/howto/topic[@name='PowerBuilder']/url");
			NodeList nl2 = (NodeList) expr2.evaluate(doc,
					XPathConstants.NODESET);
			System.out.println("\nSOAP Binding Operations:");
			for (int i = 0; i < nl2.getLength(); i++) {
				parseWSDLOperationInBinding(nl2.item(i), i, service, operations);
			}
			
			String[] opNames = operations.keySet().toArray(new String[0]);
			for (int i=0; i<opNames.length; i++) {
				System.out.println("Opeartion-" + (i+1) +": " + opNames[i]);
				MSPServiceOperation op = operations.get(opNames[i]);
				op.setInputMessage(messageElementMapping.get(op.getInputMessage())); // map to element type for message matching
				op.setOutputMessage(messageElementMapping.get(op.getOutputMessage())); // map to element type for message matching
				op.getServicePK().setVersion(version);
				operations.get(opNames[i]).print();
				try {
					DAOUtil.getMSPServiceOperationDAO().addMSPService(operations.get(opNames[i]));
				} catch (Exception e) {
					System.out.println("Problem with storing Operation-" + (i+1) +"-" + opNames[i] + ": " + e.getMessage());
				}
			}

		} catch (ParserConfigurationException e) {
			logger.severe(e.getMessage());
		} catch (SAXException e) {
			logger.severe(e.getMessage());
		} catch (FileNotFoundException e) {
			logger.severe(e.getMessage());
		} catch (IOException e) {
			logger.severe(e.getMessage());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	static private void printWSDLOperationInPortType(Node n, int i) {
		NamedNodeMap m1 = n.getAttributes();
		System.out.print(n.getNodeName() + "-" + (i + 1) + ":\t");
		for (int j = 0; j < m1.getLength(); j++)
			System.out.print(m1.item(j).getNodeName() + "="
					+ m1.item(j).getNodeValue() + "; ");
		System.out.println();
		NodeList nl = n.getChildNodes(); //
		for (int k = 0; k < nl.getLength(); k++) {
			if (!nl.item(k).getNodeName().equals("wsdl:documentation")) {
				System.out.print("    " + nl.item(k).getNodeName() + "\t");
				NamedNodeMap m2 = nl.item(k).getAttributes();
				for (int k1 = 0; k1 < m2.getLength(); k1++)
					System.out.print(m2.item(k1).getNodeName() + "="
							+ m2.item(k1).getNodeValue() + "; ");
				System.out.println();
			}
		}		
	}

	static private void parseWSDLOperationInPortType(Node n, int i, String service, Map<String, MSPServiceOperation> operations) {

		MSPServiceOperation op = null;

		NamedNodeMap m1 = n.getAttributes();
		System.out.print(n.getNodeName() + "-" + (i + 1) + ":\t");

		for (int j = 0; j < m1.getLength(); j++) {
			System.out.print(m1.item(j).getNodeName() + "="
					+ m1.item(j).getNodeValue() + "; ");
			
			if (m1.item(j).getNodeName().equals("name")) { // op-name
				if (operations.containsKey(m1.item(j).getNodeValue()))
					op = operations.get(m1.item(j).getNodeValue());
				else {
					op = new MSPServiceOperation();
					MSPServiceOperationKey id = new MSPServiceOperationKey();
					id.setServiceName(service);
					op.setServiceCodeFromName(service);
					id.setOperationName(m1.item(j).getNodeValue());
					op.setServicePK(id);
					operations.put(m1.item(j).getNodeValue(), op);
				}
			}
		}
		System.out.println();
		NodeList nl = n.getChildNodes(); //
		for (int k = 0; k < nl.getLength(); k++) {
			if (!nl.item(k).getNodeName().equals("wsdl:documentation")) {
				System.out.print("    " + nl.item(k).getNodeName() + "\t");
				NamedNodeMap m2 = nl.item(k).getAttributes();
				if (m2 != null)
				for (int k1 = 0; k1 < m2.getLength(); k1++) {
					System.out.print(m2.item(k1).getNodeName() + "="
							+ m2.item(k1).getNodeValue() + "; ");
					if (nl.item(k).getNodeName().equals("wsdl:input") && m2.item(k1).getNodeName().equals("message")) { // port input message
						op.setInputMessage(StringUtil.removeNamespace(m2.item(k1).getNodeValue()));
					} else if (nl.item(k).getNodeName().equals("wsdl:output") && m2.item(k1).getNodeName().equals("message")) { // port output message
						op.setOutputMessage(StringUtil.removeNamespace(m2.item(k1).getNodeValue()));
					}
				}
				System.out.println();
			}
		}
	}

	static private void parseWSDLOperationInBinding(Node n, int i, String service, Map<String, MSPServiceOperation> operations) {
		MSPServiceOperation op = null;

		NamedNodeMap m1 = n.getAttributes();
		System.out.print(n.getNodeName() + "-" + (i + 1) + ":\t");
		for (int j = 0; j < m1.getLength(); j++) {
			System.out.print(m1.item(j).getNodeName() + "="
					+ m1.item(j).getNodeValue() + "; ");
			
			if (m1.item(j).getNodeName().equals("name")) { // op-name
				if (operations.containsKey(m1.item(j).getNodeValue()))
					op = operations.get(m1.item(j).getNodeValue());
				else {
					op = new MSPServiceOperation();
					MSPServiceOperationKey id = new MSPServiceOperationKey();
					id.setServiceName(service);
					op.setServiceCodeFromName(service);
					id.setOperationName(m1.item(j).getNodeValue());
					op.setServicePK(id);
					operations.put(m1.item(j).getNodeValue(), op);
				}
			}
		}
		System.out.println();
		NodeList nl = n.getChildNodes(); //
		for (int k = 0; k < nl.getLength(); k++) {
			if (nl.item(k).getNodeName().equals("soap:operation")) {
				printNodeNameAttributes(nl.item(k), "    ");
				
				NamedNodeMap map = nl.item(k).getAttributes();
				Node soapAction = map.getNamedItem("soapAction");
				op.setSoapAction(soapAction.getNodeValue());  // soapAction
			} else if (nl.item(k).getNodeName().equals("wsdl:input")) {
				System.out.println("    " + nl.item(k).getNodeName() + "\t");
				NodeList bh = nl.item(k).getChildNodes();
				for (int k1 = 0; k1 < bh.getLength(); k1++) {
					printNodeNameAttributes(bh.item(k1), "        ");
					if (bh.item(k1).getNodeName().equals("soap:header")) { // in or out message has the same header, only need to save one set
						NamedNodeMap map = bh.item(k1).getAttributes();
						Node msg = map.getNamedItem("message");
						op.setSoapRequestHeaderMessage(StringUtil.removeNamespace(msg.getNodeValue()));
						Node part = map.getNamedItem("part");
						op.setSoapRequestHeaderPart(part.getNodeValue());
					}
				}						
			} else if (nl.item(k).getNodeName().equals("wsdl:output")) {
				System.out.println("    " + nl.item(k).getNodeName() + "\t");
				NodeList bh = nl.item(k).getChildNodes();
				for (int k1 = 0; k1 < bh.getLength(); k1++) {
					printNodeNameAttributes(bh.item(k1), "        ");
					if (bh.item(k1).getNodeName().equals("soap:header")) { // in or out message has the same header, only need to save one set
						NamedNodeMap map = bh.item(k1).getAttributes();
						Node msg = map.getNamedItem("message");
						op.setSoapResponseHeaderMessage(StringUtil.removeNamespace(msg.getNodeValue()));
						Node part = map.getNamedItem("part");
						op.setSoapResponseHeaderPart(part.getNodeValue());
					}
				}						
			} 
			/*
			else if (!nl.item(k).getNodeName().equals("wsdl:documentation")) {
				System.out.println("    " + nl.item(k).getNodeName() + "\t");
				NodeList bh = nl.item(k).getChildNodes();
				for (int k1 = 0; k1 < bh.getLength(); k1++) {
					printNodeNameAttributes(bh.item(k1), "        ");
					if (bh.item(k1).getNodeName().equals("soap:header")) { // in or out message has the same header, only need to save one set
						NamedNodeMap map = bh.item(k1).getAttributes();
						Node msg = map.getNamedItem("message");
						op.setSoapRequestHeaderMessage(StringUtil.removeNamespace(msg.getNodeValue()));
						Node part = map.getNamedItem("part");
						op.setSoapRequestHeaderPart(part.getNodeValue());
					}
				}		
			}
			*/
		}
	}

	static private void printWSDLOperationInBinding(Node n, int i) {
		NamedNodeMap m1 = n.getAttributes();
		System.out.print(n.getNodeName() + "-" + (i + 1) + ":\t");
		for (int j = 0; j < m1.getLength(); j++)
			System.out.print(m1.item(j).getNodeName() + "="
					+ m1.item(j).getNodeValue() + "; ");
		System.out.println();
		NodeList nl = n.getChildNodes(); 
				
		for (int k = 0; k < nl.getLength(); k++) {
			if (nl.item(k).getNodeName().equals("soap:operation")) {
				printNodeNameAttributes(nl.item(k), "    ");
			} else if (nl.item(k).getNodeName().equals("wsdl:input") || nl.item(k).getNodeName().equals("wsdl:output")) {
				System.out.println("    " + nl.item(k).getNodeName() + "\t");
				NodeList bh = nl.item(k).getChildNodes();
				for (int k1 = 0; k1 < bh.getLength(); k1++) {
					printNodeNameAttributes(bh.item(k1), "        ");
				}						
			}  
		}
	}

	static private void printNodeNameAttributes(Node n, String preFix) {
		if (n == null)
			return;

		System.out.print(preFix + n.getNodeName() + "-: ");
		NamedNodeMap soAttrs = n.getAttributes();
		if (soAttrs != null)
			for (int k1 = 0; k1 < soAttrs.getLength(); k1++)
				System.out.print("\t" + soAttrs.item(k1).getNodeName() + "="
						+ soAttrs.item(k1).getNodeValue());
		System.out.println();
	}

	private static void printNode(Node n, int majorlevel, int minor) {
		StringBuffer preFix = new StringBuffer();
		preFix.append(majorlevel).append("-").append(minor).append(" ");
		for (int i = 1; i < majorlevel; i++)
			preFix.append("  ");
		System.out.println(preFix + "name=" + n.getNodeName() + "\ttype="
				+ n.getNodeType() + "\tvalue=" + n.getNodeValue()
				+ "\ttextContent=" + n.getTextContent());
		NamedNodeMap nnm = n.getAttributes();
		if (nnm != null) {
			System.out.print(preFix + "\t");
			for (int i = 0; i < nnm.getLength(); i++) {
				Node att = nnm.item(i);
				if (att != null)
					System.out.print("attname=" + att.getNodeName()
							+ ",attval=" + att.getNodeValue() + ";");
			}
			System.out.println();
		}
		NodeList children = n.getChildNodes();
		for (int i = 0; i < children.getLength(); i++)
			printNode(children.item(i), majorlevel + 1, i);
	}

	private static void printTopLevelElement(Node n, int majorlevel, int minor) {
		StringBuffer preFix = new StringBuffer();
		preFix.append(majorlevel).append("-").append(minor).append(" ");
		System.out.print(n.getNodeName() + ":" + preFix);
		NamedNodeMap nnm = n.getAttributes();
		System.out.print("\t");
		for (int i = 0; i < nnm.getLength(); i++) {
			Node att = nnm.item(i);
			System.out.print(att.getNodeName() + "=" + att.getNodeValue());
		}
		System.out.println();
	}

	// a more robust version to handle whitespace and newlines in the wsdl
	private static void printTopLevelMessage(Node n, int majorlevel, int minor) {
		StringBuffer preFix = new StringBuffer();
		preFix.append(majorlevel).append("-").append(minor).append(" ");
		System.out.print(n.getNodeName() + ":" + preFix);
		NamedNodeMap nnm = n.getAttributes();
		System.out.print("\t");
		if (nnm != null)
		for (int i = 0; i < nnm.getLength(); i++) {
			Node att = nnm.item(i);
			System.out
					.print(att.getNodeName() + "=" + att.getNodeValue() + ";");
		}

		NodeList nl = n.getChildNodes();
		if (nl != null)
			for (int i=0; i<nl.getLength(); i++) {
				if (nl.item(i).getNodeName().contains("wsdl:part")) {
					
					Node part = nl.item(i);
					System.out.print("\t" + part.getNodeName() + ":");
					NamedNodeMap nnm1 = part.getAttributes();
					System.out.print("\t");
					if (nnm1 != null)
					for (int j = 0; j < nnm1.getLength(); j++) {
						Node att = nnm1.item(j);
						System.out.print(att.getNodeName() + "=" + att.getNodeValue()
								+ "; ");
					}					
				}
			}
		System.out.println();
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
