/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.multispeak;

import java.util.logging.Logger;

import org.apache.xmlbeans.SchemaProperty;

public class MSPSchemaTypeAttribute extends SchemaTypeProperty{
	@SuppressWarnings("unused")
    static private Logger logger = Logger.getLogger(MSPSchemaTypeAttribute.class.getName());
	
	enum Use { OPTIONAL, REQUIRED, PROHIBITED };
	private Use use = Use.OPTIONAL;
	
	public MSPSchemaTypeAttribute(SchemaProperty sProperty) {
		this(sProperty, "");
	}
	
	public MSPSchemaTypeAttribute(SchemaProperty sProperty, String xPath) {
		super(sProperty, xPath);
		if (sProperty.getMaxOccurs().intValue() == 0)
			setUse(Use.PROHIBITED);
		else if (sProperty.getMinOccurs().intValue() == 1)
			setUse(Use.REQUIRED);
	}
	
	public Use getUse() {
		return use;
	}
	
	public void setUse(Use use) {
		this.use = use;
	}
	
	public String toString() {
		String repr = super.toString();
		repr += "use=\"";
		switch (use) {
			case OPTIONAL:
				repr += "optional";
				break;
			case REQUIRED:
				repr += "required";
				break;
			case PROHIBITED:
				repr += "prohibited";
				break;
		}
		repr += "\" ";
		return repr;
	}
}
