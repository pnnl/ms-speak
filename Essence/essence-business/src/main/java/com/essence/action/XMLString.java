/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.action;

import java.io.StringWriter;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerConfigurationException;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.Attr;
import org.w3c.dom.Document;
import org.w3c.dom.Element;

public class XMLString {

/*	public static void main(String[] z)
	{
		new XMLString().getBlockSourceAndDestinationIPAddressXMLObject("10.0.0.1", "32", "10.0.0.2", "32", "ipv4", "0", "1");
	}
*/
	public String getBlockSourceAndDestinationIPAddressXMLObject(String sourceIPAddress, String sourceIPAddressPrefix, String destinationIPADrress, String destinationIPADrressPrefix, String ipProto, String tableID, String flowID)
	{
		DocumentBuilderFactory docFactory = DocumentBuilderFactory.newInstance();
		StringWriter sw = new StringWriter();
		try {
			DocumentBuilder docBuilder = docFactory.newDocumentBuilder();
			Document doc = docBuilder.newDocument();
			
			Element rootElement = doc.createElement("flow");
			Attr attribute =  doc.createAttribute("xmlns");
			attribute.setValue("urn:opendaylight:flow:inventory");
			rootElement.setAttributeNode(attribute);
			doc.appendChild(rootElement);
			
			Element instructions = doc.createElement("instructions");
			rootElement.appendChild(instructions);

			Element instruction = doc.createElement("instruction");
			instructions.appendChild(instruction);

			Element order = doc.createElement("order");
			order.appendChild(doc.createTextNode("0"));
			instruction.appendChild(order);

			Element apply_actions = doc.createElement("apply-actions");
			instruction.appendChild(apply_actions);

			Element action = doc.createElement("action");
			apply_actions.appendChild(action);

			Element order1 = doc.createElement("order");
			order1.appendChild(doc.createTextNode("0"));
			action.appendChild(order1);

			Element drop_action= doc.createElement("drop-action");
			drop_action.appendChild(doc.createTextNode("drop"));
			action.appendChild(drop_action);

			Element match= doc.createElement("match");
			rootElement.appendChild(match);

			Element ethernet_match= doc.createElement("ethernet-match");
			match.appendChild(ethernet_match);

			Element ethernet_type= doc.createElement("ethernet-type");
			ethernet_match.appendChild(ethernet_type);

			Element type= doc.createElement("type");
			type.appendChild(doc.createTextNode("0x800"));
			ethernet_type.appendChild(type);


			Element ip_match= doc.createElement("ip-match");
			match.appendChild(ip_match);

			Element ip_proto= doc.createElement("ip-proto");
			ip_proto.appendChild(doc.createTextNode(ipProto));
			ip_match.appendChild(ip_proto);

			Element ip_source= doc.createElement(ipProto + "-source");
			ip_source.appendChild(doc.createTextNode(sourceIPAddress + "/" + sourceIPAddressPrefix));
			match.appendChild(ip_source);

			Element ip_destination= doc.createElement(ipProto+ "-destination");
			ip_destination.appendChild(doc.createTextNode(destinationIPADrress + "/" + destinationIPADrressPrefix));
			match.appendChild(ip_destination);

			Element table_id= doc.createElement("table_id");
			table_id.appendChild(doc.createTextNode(tableID));
			rootElement.appendChild(table_id);

			Element id= doc.createElement("id");
			id.appendChild(doc.createTextNode(flowID));
			rootElement.appendChild(id);

			Element flow_name= doc.createElement("flow-name");
			flow_name.appendChild(doc.createTextNode("IP Blocking Flow Number - " + flowID));
			rootElement.appendChild(flow_name);

			Element priority= doc.createElement("priority");
			priority.appendChild(doc.createTextNode("65000"));
			rootElement.appendChild(priority);

			TransformerFactory transformerFactory = TransformerFactory.newInstance();
			Transformer transformer = transformerFactory.newTransformer();
			DOMSource source = new DOMSource(doc);
			StreamResult result = new StreamResult(sw);
			transformer.transform(source, result);
			System.out.println(sw.toString().replaceAll("xmlns=\"\"", ""));
			//System.out.println(source);
		} catch (ParserConfigurationException e) {
			e.printStackTrace();
		} catch(TransformerConfigurationException e) {
			e.printStackTrace();
		} catch(TransformerException e) {
			e.printStackTrace();
		}
		
		return sw.toString().replaceAll("xmlns=\"\"", "");
		
	}
}