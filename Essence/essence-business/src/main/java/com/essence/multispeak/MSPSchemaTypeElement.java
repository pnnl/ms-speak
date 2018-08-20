/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.multispeak;

import java.math.BigInteger;
import java.util.logging.Logger;

import org.apache.xmlbeans.SchemaProperty;

public class MSPSchemaTypeElement extends SchemaTypeProperty{
	@SuppressWarnings("unused")
    static private Logger logger = Logger.getLogger(MSPSchemaTypeElement.class.getName());
	
	private BigInteger minOccurs;
	private BigInteger maxOccurs;
	enum Nillable { NEVER, VARIABLE, CONSISTENTLY };
	private Nillable isNillable;
	
	public MSPSchemaTypeElement(SchemaProperty sProperty) {
		this(sProperty, "");
	}
	
	public MSPSchemaTypeElement(SchemaProperty sProperty, String xPath) {
		super(sProperty, xPath);
		minOccurs = sProperty.getMinOccurs();
		maxOccurs = sProperty.getMaxOccurs();
		switch (sProperty.hasNillable()) {
			case SchemaProperty.NEVER:
				isNillable = Nillable.NEVER;
				break;
			case SchemaProperty.VARIABLE:
				isNillable = Nillable.VARIABLE;
				break;
			case SchemaProperty.CONSISTENTLY:
				isNillable = Nillable.CONSISTENTLY;
				break;
			default:
				isNillable = Nillable.NEVER;
				break;
		}
	}

	public BigInteger getMinOccurs() {
		return minOccurs;
	}

	public void setMinOccurs(BigInteger minOccurs) {
		this.minOccurs = minOccurs;
	}

	public BigInteger getMaxOccurs() {
		return maxOccurs;
	}

	public void setMaxOccurs(BigInteger maxOccurs) {
		this.maxOccurs = maxOccurs;
	}

	public Nillable isNillable() {
		return isNillable;
	}

	public void setIsNillable(Nillable nillable) {
		this.isNillable = nillable;
	}
	
	public String toString() {
		String repr = super.toString();
		if (minOccurs != null && minOccurs.intValue() != 1)
			repr += "minOccurs=\"" + minOccurs + "\" ";
		if (maxOccurs != null && maxOccurs.intValue() != 1)
			repr += "maxOccurs=\"" + maxOccurs + "\" ";
		if (maxOccurs == null)
			repr += "maxOccurs=\"unbounded\" ";
		switch (isNillable) {
			case NEVER:
				break;
			case VARIABLE:
				repr +=  "nillable=\"VARIABLE\" ";
				break;
			case CONSISTENTLY:
				repr += "nillable=\"CONSISTENTLY\" ";
				break;
		}
		return repr;
	}

}
