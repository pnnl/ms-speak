/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.multispeak;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.logging.Logger;

import javax.xml.namespace.QName;

import org.apache.xmlbeans.SchemaProperty;
import org.apache.xmlbeans.SchemaStringEnumEntry;
import org.apache.xmlbeans.SchemaType;
import org.apache.xmlbeans.XmlAnySimpleType;

import com.essence.ui.shared.StringUtil;

@SuppressWarnings("unused")
public class MSSchemaTypeParser {
	static private Logger logger = Logger.getLogger(MSSchemaTypeParser.class.getName());
	
	private QName qname;
	private Map<String, String[]> facetRestrictions;
	private SchemaType schemaType;
	private MSPSchemaTypeElement[] elementProperties;
	private MSPSchemaTypeAttribute[] attributeProperties;
	private String xPath;
	
	public MSSchemaTypeParser(SchemaType sType) {
		this(sType, "");
	}
	
	public MSSchemaTypeParser(SchemaType sType, String xPath) {
		this.schemaType = sType;
		this.setXPath(xPath);
		this.qname = sType.getName();
		this.facetRestrictions = parseFacetRestrictions(sType);
		SchemaProperty[] elmtProps = sType.getElementProperties();
		this.elementProperties = new MSPSchemaTypeElement[elmtProps.length];
//System.out.println("MSSchemaTypeParser: xpath=" + xPath + "\tname = " + qname + "\telements = " + elmtProps.length);
		for (int i=0; i<elmtProps.length; i++) {
			this.elementProperties[i] = new MSPSchemaTypeElement(elmtProps[i], xPath);
			if (elmtProps[i].getType() != null && elmtProps[i].getType().isSimpleType()) {
				String typeName = null;
				if (elmtProps[i].getType().getName() != null)
					typeName = elmtProps[i].getType().getName().getLocalPart();
				else
					typeName = elmtProps[i].getType().getBaseType().getName().getLocalPart();
				MSParser.ELEMENT_XPATHS.add(elementProperties[i].getXPath()+"-"+MSParser.CURRENT_SERVICE_CD+"-"+MSParser.CURRENT_MSG_NAME+"-"+typeName); //elmtProps[i].getType().getName().getLocalPart());
			}
			//			MSParser.ELEMENT_XPATHS.add(StringUtil.getElementNameFromXpath(elementProperties[i].getXPath()) + "-" + elementProperties[i].getXPath() + "-" + elmtProps[i].getType().getName().getLocalPart());
			else if (elmtProps[i].getType() != null && elmtProps[i].getType().getName() != null && elmtProps[i].getType().getName().getNamespaceURI().equals("http://www.multispeak.org/V5.0/enumerations"))
				//MSParser.ELEMENT_XPATHS.add(StringUtil.reverseXpath(elementProperties[i].getXPath()) + "-PRIMITIVE-TYPE");
				//MSParser.ELEMENT_XPATHS.add(elementProperties[i].getXPath()); // enums
				MSParser.ELEMENT_XPATHS.add(elementProperties[i].getXPath()+"-"+MSParser.CURRENT_SERVICE_CD+"-"+MSParser.CURRENT_MSG_NAME+"-"+elmtProps[i].getType().getName().getLocalPart());
			else if (elmtProps[i].getType() != null && elmtProps[i].getType().getContentType() == SchemaType.SIMPLE_CONTENT) {
				//MSParser.ELEMENT_XPATHS.add(StringUtil.reverseXpath(elementProperties[i].getXPath()) + "-PRIMITIVE-TYPE");
				//MSParser.ELEMENT_XPATHS.add(elementProperties[i].getXPath()); // enums
				String typeName = null;
				if (elmtProps[i].getType().getName() != null)
					typeName = elmtProps[i].getType().getName().getLocalPart();
				else
					typeName = elmtProps[i].getType().getBaseType().getName().getLocalPart();
				MSParser.ELEMENT_XPATHS.add(elementProperties[i].getXPath()+"-"+MSParser.CURRENT_SERVICE_CD+"-"+MSParser.CURRENT_MSG_NAME+"-"+typeName); //elmtProps[i].getType().getName().getLocalPart());
			}
			else if (elmtProps[i].getType() != null && elmtProps[i].getType().isPrimitiveType()) // may not be necessary as it is covered by SimpleType
				//MSParser.ELEMENT_XPATHS.add(StringUtil.reverseXpath(elementProperties[i].getXPath()) + "-PRIMITIVE-TYPE");
				//MSParser.ELEMENT_XPATHS.add(elementProperties[i].getXPath());
				MSParser.ELEMENT_XPATHS.add(elementProperties[i].getXPath()+"-"+MSParser.CURRENT_SERVICE_CD+"-"+MSParser.CURRENT_MSG_NAME+"-"+elmtProps[i].getType().getName().getLocalPart());
		}
		SchemaProperty[] attrProps = sType.getAttributeProperties();
//System.out.println("MSSchemaTypeParser:  xpath=" + xPath + "\tname = " + qname + "\tattributes = " + attrProps.length);
		this.attributeProperties = new MSPSchemaTypeAttribute[attrProps.length];
		for (int i=0; i<attrProps.length; i++) {
			this.attributeProperties[i] = new MSPSchemaTypeAttribute(attrProps[i], xPath);
			if (attrProps[i].getType() != null && attrProps[i].getType().isSimpleType())
				//MSParser.ATTR_XPATHS.add(StringUtil.getElementNameFromXpath(attributeProperties[i].getXPath()) + " - " + attributeProperties[i].getXPath() + "-" + attrProps[i].getType().getName().getLocalPart());
				//MSParser.ATTR_XPATHS.add(attributeProperties[i].getXPath());
				MSParser.ATTR_XPATHS.add(attributeProperties[i].getXPath()+"-"+MSParser.CURRENT_SERVICE_CD+"-"+MSParser.CURRENT_MSG_NAME+"-"+attrProps[i].getType().getName().getLocalPart());
			else if (attrProps[i].getType() != null && attrProps[i].getType().isPrimitiveType()) // may not be necessary as it is covered by SimpleType
				//MSParser.ATTR_XPATHS.add(StringUtil.reverseXpath(attributeProperties[i].getXPath()) + "-PRIMITIVE-TYPE");
				//MSParser.ATTR_XPATHS.add(attributeProperties[i].getXPath());
				MSParser.ATTR_XPATHS.add(attributeProperties[i].getXPath()+"-"+MSParser.CURRENT_SERVICE_CD+"-"+MSParser.CURRENT_MSG_NAME+"-"+attrProps[i].getType().getName().getLocalPart());
		}
	}
	
	public String toString() {
		return toString(0);
	}
	
	public String toString(int indentLvl) {
		return describeSchema(schemaType, indentLvl);
	}
	
	public String describeSchema(SchemaType sType, int indentLvl) {
		String repr = "";
		String indent = "";
		for (int i=0; i<indentLvl; i++)
			indent += "\t";
		
		String name = "";
		String namespace = "";
		if (sType.getName() != null) {
			name = sType.getName().getLocalPart();
			namespace = sType.getName().getNamespaceURI();
		}
		if (sType.isSimpleType()) {
			repr += indent + "<simpleType name=\"" + name + "\" namespace=\"" + namespace + "\" ";
			// Don't bother describing primitive types further
			if (sType.getSimpleVariety() == SchemaType.ATOMIC && sType.isPrimitiveType())
				return repr + "/>\n";
			repr += ">\n";
			switch (sType.getSimpleVariety()) {
				case SchemaType.ATOMIC:
					repr += indent + "\t<restriction base=\"" + sType.getPrimitiveType().getName() + "\" ";
					if (!facetRestrictions.isEmpty()) {
						repr +=  ">\n";
						for (Map.Entry<String, String[]> entry : facetRestrictions.entrySet()) {
							for (String val : entry.getValue())
								repr += indent + "\t\t<" + entry.getKey() + " value=\"" + val + "\" />\n";
						}
						repr += indent + "\t</restriction>\n";
					} else
						repr += "/>\n";
					break;
				case SchemaType.LIST:
					repr += indent + "\t<list>\n";
					repr += indent + describeSchema(sType.getListItemType(), (indentLvl + 1));
					repr += indent + "\t</list>\n";
					break;
				case SchemaType.UNION:
					repr += indent + "\t<union>\n";
					for (SchemaType memberType : sType.getUnionMemberTypes())
						repr += describeSchema(memberType, (indentLvl + 2));
					repr += indent + "\t</union>\n";
					break;
				default:
					repr += indent + "\tERROR";
					break;
			}
			repr += indent + "</simpleType>\n";
		} else { // Complex type
			repr += indent + "<complexType name=\"" + name + "\" namespace=\"" + namespace + "\" ";
			if (sType.getContentType() == SchemaType.MIXED_CONTENT)
				repr += "mixed=\"true\" ";
			repr += ">\n";
			for (MSPSchemaTypeAttribute attr : attributeProperties) {
				repr += indent + "\t<attribute " + attr.toString() + ">\n";
				repr += attr.getSchemaType().toString((indentLvl + 2));
				repr += indent + "\t</attribute>\n";
			}
			switch (sType.getContentType()) {
				case SchemaType.EMPTY_CONTENT:
					repr += indent + "\t<!-- Empty Content -->\n";
					break;
				case SchemaType.SIMPLE_CONTENT:
					repr += indent + "\t<simpleContent>\n";
					repr += describeSchema(sType.getContentBasedOnType(), (indentLvl + 2));
					repr += indent + "\t</simpleContent>\n";
					break;
				default: //Element or Mixed Content
					repr += indent + "\t<complexContent>\n";
					for (MSPSchemaTypeElement elmt : elementProperties) {
						repr += indent +  "\t\t<element " + elmt.toString() + ">\n";
						repr += elmt.getSchemaType().toString((indentLvl + 3));
						repr += indent + "\t\t</element>\n";
					}
					repr += indent + "\t</complexContent>\n";
					break;
			}
			repr += indent + "</complexType>\n";
		}
		return repr;
	}

	public static Map<String, String[]> parseFacetRestrictions(SchemaType sType) {
		Map<String, String[]> facetRestrictions = new HashMap<String, String[]>();
		XmlAnySimpleType[] enumerations = sType.getEnumerationValues();
		if (enumerations != null) {
			String[] enumerationVals = new String[enumerations.length];
			for (int i=0; i < enumerations.length; i++)
				enumerationVals[i] = enumerations[i].getStringValue();
			facetRestrictions.put("enumeration", enumerationVals);
		}
		
		XmlAnySimpleType facet = sType.getFacet(SchemaType.FACET_FRACTION_DIGITS);
		if (facet != null)
			facetRestrictions.put("fractionDigits", new String[] {
					facet.getStringValue() });
		
		facet = sType.getFacet(SchemaType.FACET_LENGTH);
		if (facet != null)
			facetRestrictions.put("length", new String[] {
					facet.getStringValue() });
		
		facet = sType.getFacet(SchemaType.FACET_MAX_EXCLUSIVE);
		if (facet != null)
			facetRestrictions.put("maxExclusive", new String[] {
					facet.getStringValue() });
		
		facet = sType.getFacet(SchemaType.FACET_MAX_INCLUSIVE);
		if (facet != null)
			facetRestrictions.put("maxInclusive", new String[] {
					facet.getStringValue() });
		
		facet = sType.getFacet(SchemaType.FACET_MAX_LENGTH);
		if (facet != null)
			facetRestrictions.put("maxLength", new String[] {
					facet.getStringValue() });
		
		facet = sType.getFacet(SchemaType.FACET_MIN_EXCLUSIVE);
		if (facet != null)
			facetRestrictions.put("minExclusive", new String[] {
					facet.getStringValue() });
		
		facet = sType.getFacet(SchemaType.FACET_MIN_INCLUSIVE);
		if (facet != null)
			facetRestrictions.put("minInclusive", new String[] {
					facet.getStringValue() });
		
		facet = sType.getFacet(SchemaType.FACET_MIN_LENGTH);
		if (facet != null)
			facetRestrictions.put("minLength", new String[] {
				facet.getStringValue() });
		
		String[] patterns = sType.getPatterns();
		if (patterns.length > 0)
			facetRestrictions.put("pattern", sType.getPatterns());
		
		facet = sType.getFacet(SchemaType.FACET_TOTAL_DIGITS);
		if (facet != null)
			facetRestrictions.put("totalDigits", new String[] {
					facet.getStringValue() });
		
		String[] whiteSpaceValue;
		switch (sType.getWhiteSpaceRule()) {
			case SchemaType.WS_COLLAPSE:
				whiteSpaceValue = new String[] { "collapse" };
				break;
			case SchemaType.WS_PRESERVE:
				whiteSpaceValue = new String[] { "preserve" };
				break;
			case SchemaType.WS_REPLACE:
				whiteSpaceValue = new String[] { "replace" };
				break;
			default:
				whiteSpaceValue = null;
				break;
		}
		if (whiteSpaceValue != null)
			facetRestrictions.put("whiteSpace", whiteSpaceValue);
		return facetRestrictions;
	}
	
	public QName getQName() {
		return qname;
	}

	public void setQName(QName qname) {
		this.qname = qname;
	}

	public Map<String, String[]> getFacetRestrictions() {
		return facetRestrictions;
	}

	public void setFacetRestrictions(Map<String, String[]> facetRestrictions) {
		this.facetRestrictions = facetRestrictions;
	}
	
	public MSPSchemaTypeElement[] getElementProperties() {
		return elementProperties;
	}

	public void setElementProperties(MSPSchemaTypeElement[] elementProperties) {
		this.elementProperties = elementProperties;
	}

	public MSPSchemaTypeAttribute[] getAttributeProperties() {
		return attributeProperties;
	}

	public void setAttributeProperties(MSPSchemaTypeAttribute[] attributeProperties) {
		this.attributeProperties = attributeProperties;
	}

	public String getXPath() {
		return xPath;
	}

	public void setXPath(String xPath) {
		this.xPath = xPath;
	}
}