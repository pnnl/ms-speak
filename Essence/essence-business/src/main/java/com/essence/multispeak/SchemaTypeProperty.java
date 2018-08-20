/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.multispeak;

import javax.xml.namespace.QName;

import org.apache.xmlbeans.SchemaProperty;

import java.util.logging.Logger;

public abstract class SchemaTypeProperty {
    @SuppressWarnings("unused")
	static private Logger logger = Logger.getLogger(SchemaTypeProperty.class.getName());
	
	enum Occurs { NEVER, VARIABLE, CONSISTENTLY };
	private QName qname;
	private Occurs hasDefault;
	private Occurs hasFixed; 
	private String defaultValue = null;
	private String xPath = "";
	private MSSchemaTypeParser schemaType;
	
	public SchemaTypeProperty(SchemaProperty sProperty) {
		this(sProperty, "");
	}
	
	public SchemaTypeProperty(SchemaProperty sProperty, String xPath) {
		qname = sProperty.getName();
		String fullXPath = xPath;
		if (this instanceof MSPSchemaTypeElement)
			fullXPath += "/" + qname.getLocalPart();
		else if (this instanceof MSPSchemaTypeAttribute)
			fullXPath += "/@" + qname.getLocalPart();
		this.xPath = fullXPath;
		switch (sProperty.hasFixed()) {
			case SchemaProperty.NEVER:
				hasFixed = Occurs.NEVER;
				break;
			case SchemaProperty.VARIABLE:
				hasFixed = Occurs.VARIABLE;
				break;
			case SchemaProperty.CONSISTENTLY:
				hasFixed = Occurs.CONSISTENTLY;
				break;
		}
		switch (sProperty.hasDefault()) {
			case SchemaProperty.NEVER:
				hasDefault = Occurs.NEVER;
				break;
			case SchemaProperty.VARIABLE:
				hasDefault = Occurs.VARIABLE;
				break;
			case SchemaProperty.CONSISTENTLY:
				hasDefault = Occurs.CONSISTENTLY;
				break;
		}
		defaultValue = sProperty.getDefaultText();
		schemaType = new MSSchemaTypeParser(sProperty.getType(), fullXPath);
	}
	
	public String toString() {
		String repr = "";
		String name = "";
		if (qname != null) 
			name = qname.getLocalPart();
		repr += "name=\"" + name + "\" xPath=\"" + xPath + "\" ";
		if (hasFixed.equals(SchemaTypeProperty.Occurs.CONSISTENTLY))
			repr += "fixed=\"" + defaultValue + "\" ";
		else if (hasFixed.equals(SchemaTypeProperty.Occurs.VARIABLE))
			repr += "(fixed=\"" + defaultValue + "\")? ";
		else if (hasDefault.equals(SchemaTypeProperty.Occurs.CONSISTENTLY))
			repr += "default=\"" + defaultValue + "\" ";
		else if (hasDefault.equals(SchemaTypeProperty.Occurs.VARIABLE))
			repr += "(default=\"" + defaultValue + "\")? ";
		return repr;
	}

	public QName getQname() {
		return qname;
	}

	public void setQname(QName qname) {
		this.qname = qname;
	}

	public Occurs hasDefault() {
		return hasDefault;
	}

	public void setHasDefault(Occurs hasDefault) {
		this.hasDefault = hasDefault;
	}

	public Occurs hasFixed() {
		return hasFixed;
	}

	public void setHasFixed(Occurs hasFixed) {
		this.hasFixed = hasFixed;
	}

	public String getDefaultValue() {
		return defaultValue;
	}

	public void setDefaultValue(String defaultValue) {
		this.defaultValue = defaultValue;
	}
	
	public String getXPath() {
		return this.xPath;
	}
	
	public void setXPath(String xPath) {
		this.xPath = xPath;
	}

	public MSSchemaTypeParser getSchemaType() {
		return schemaType;
	}

	public void setSchemaType(MSSchemaTypeParser schemaType) {
		this.schemaType = schemaType;
	}

}
