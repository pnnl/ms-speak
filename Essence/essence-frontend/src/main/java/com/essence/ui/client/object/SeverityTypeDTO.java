/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.object;


public enum SeverityTypeDTO {
	HIGH {
        @Override
        public int getOrder() {
            return 3;
        }
	},
	MEDIUM {
        @Override
        public int getOrder() {
            return 2;
        }
	},
	LOW {
        @Override
        public int getOrder() {
            return 1;
        }
	},
	INFORMATIONAL {
        @Override
        public int getOrder() {
            return 0;
        }
	};

    public abstract int getOrder();
    static public int getOrder(String sValue) {
    	if (sValue == null || sValue.isEmpty())
    		return -1;
    	try {
    	    SeverityTypeDTO t = SeverityTypeDTO.valueOf(sValue);
    		return t.getOrder();
    	} catch (Exception ex) {
    		return -1;
    	}
    }
    
	static public SeverityTypeDTO textToValue(String s) {
		if (s==null || s.isEmpty())
			return null;
		try {
			return SeverityTypeDTO.valueOf(s);
		} catch (Exception ex) {
			return null;
		}
	}
}
