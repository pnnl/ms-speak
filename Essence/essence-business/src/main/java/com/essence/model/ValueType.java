/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.model;


/*
 * TODO--not completed
        3.2.1 string
        3.2.2 boolean
        3.2.3 decimal
        3.2.4 float
        3.2.5 double
        3.2.6 duration
        3.2.7 dateTime
        3.2.8 time
        3.2.9 date
        3.2.10 gYearMonth
        3.2.11 gYear
        3.2.12 gMonthDay
        3.2.13 gDay
        3.2.14 gMonth
        3.2.15 hexBinary
        3.2.16 base64Binary
        3.2.17 anyURI
        3.2.18 QName
        3.2.19 NOTATION
 */
public enum ValueType {
	INTEGER {
        @Override
        public int getOrder() {
            return 0;
        }        
	},
	DECIMAL {
        @Override
        public int getOrder() {
            return 1;
        }
	},
	STRING {
        @Override
        public int getOrder() {
            return 2;
        }
	},
	PATTERN {
        @Override
        public int getOrder() {
            return 3;
        }
	};

	public abstract int getOrder();

	static public int getOrder(String sValue) {
    	if (sValue == null || sValue.isEmpty())
    		return -1;
    	try {
    		ValueType t = ValueType.valueOf(sValue);
    		return t.getOrder();
    	} catch (Exception ex) {
    		return -1;
    	}
    }
}
