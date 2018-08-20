package com.essence.multispeak;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.StringReader;
import java.io.UnsupportedEncodingException;
import java.util.List;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;

import com.essence.analysis.Packet;
import com.essence.persistence.CassandraDAOUtil;
import com.essence.persistence.PacketDAO;

/**
 * In Xpath handling, node.getNodeValue() is usually null because that's what is returned for an Element
 * node.getTextContent gives the right content
 * @author pning
 *
 */
public class XpathPlay {

	public static void main(String[] args)    
	{    	
		PacketDAO dao = CassandraDAOUtil.getPacketDAO();
		List<Packet> packets = dao.getAllPackets();
		for (Packet p : packets) {
			String msg = null;
			try {
				msg = new String(p.getContent(), "UTF-8");
				Document doc = createDocument(msg);
				String xpathString = "/Envelope/Body/GetAssetsByAssetFieldsResponse/assetContainer/parcels/parcel/premisesObjectList/premises/serviceLocations/serviceLocation/serviceAgreements/serviceAgreement/budgetBillingCode";
				String value = parseXML4XpathValue(doc, xpathString);
				System.out.println("From packet content:");
				System.out.println("xpath=" + xpathString);
				System.out.println("value=" + value);
			} catch (UnsupportedEncodingException e1) {
				e1.printStackTrace();
				return;
			} //Packet.ba2string(p.getContent()); // assuming this is the SOAP message
		}
		
		Document doc = getDocument("C:/nreca/test-messages", "GetAssetsByAssetFieldsResponse.xml");				
		String xpathString = "/Envelope/Body/GetAssetsByAssetFieldsResponse/assetContainer/parcels/parcel/premisesObjectList/premises/serviceLocations/serviceLocation/serviceAgreements/serviceAgreement/budgetBillingCode";
		String value = parseXML4XpathValue(doc, xpathString);
		System.out.println("From file:");
		System.out.println("xpath=" + xpathString);
		System.out.println("value=" + value);
	}

	public static String parseXML4XpathValue(Document doc, String xpathString) {
		if (doc == null || xpathString == null)
			return null;

		try {
			XPathFactory xPathfactory = XPathFactory.newInstance();
			XPath xpath = xPathfactory.newXPath();
			XPathExpression msgPath = xpath.compile(xpathString);
			Node msg = (Node) msgPath.evaluate(doc, XPathConstants.NODE);
			NodeList msgs = (NodeList) msgPath.evaluate(doc, XPathConstants.NODESET);
			System.out.println("Two ways for xpath: " + xpathString);
			System.out.println("one node content = " + msg.getTextContent() + "\tone node value = " + msg.getNodeValue());
			for (int i=0; i<msgs.getLength(); i++) {
				System.out.println(i + "-text=" + msgs.item(i).getTextContent() + "\t" + i + "-value=" + msgs.item(i).getNodeValue());
			}
			return msg.getTextContent();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return null;
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
			e.printStackTrace();
		} catch (SAXException e) {
			e.printStackTrace();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (Exception e) {
			e.printStackTrace();
		} 

		return null;
	}

	public static Document createDocument(String msg) {
		// Construct the DOM from message
	    DocumentBuilder db = null;
	    Document doc = null;
	    
		try {
			DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
			// prevent XXE
			factory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true); // disallows the use of DTD entities
			//factory.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true); // 64k limit on entity expansion
			//To prevent XML parsers from accessing fileFEATURE_SECURE_PROCESSINGs in the file system, use the AccessController class.
			db = factory.newDocumentBuilder();
		    InputSource is = new InputSource();
		    is.setCharacterStream(new StringReader(msg));
			doc = db.parse(is);
			// need to find out why it's not working
			doc.getDocumentElement().normalize();
			
			if (factory.isNamespaceAware())
				System.out.println("dbf is ns aware");
			else
				System.out.println("dbf is not ns aware");
			if (db.isNamespaceAware())
				System.out.println("db is ns aware");
			else
				System.out.println("db is not ns aware");
			return doc;
		} catch (ParserConfigurationException e) {
			e.printStackTrace();
			return null;
		} catch (SAXException e) {
			e.printStackTrace();
			return null;
		} catch (IOException e) {
			e.printStackTrace();
			return null;
		}
	}
}
