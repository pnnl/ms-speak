/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.object;


public enum ValueOperatorTypeDTO {
	LESS_THAN {
        @Override
        public int getOrder() {
            return 0;
        }
        
        public String valueToText() {
        	return "<";
        }
	},
	LESS_THEN_EQUAL_TO {
        @Override
        public int getOrder() {
            return 1;
        }
        
        public String valueToText() {
        	return "<=";
        }
	},
	EQUAL_TO {
        @Override
        public int getOrder() {
            return 2;
        }
        
        public String valueToText() {
        	return "=";
        }
	},
	GREATER_THAN_EQUAL_TO {
        @Override
        public int getOrder() {
            return 3;
        }
        
        public String valueToText() {
        	return ">=";
        }
	},
	GREATER_THAN {
        @Override
        public int getOrder() {
            return 4;
        }
        
        public String valueToText() {
        	return ">";
        }
	},
	NOT_EQUAL_TO {
        @Override
        public int getOrder() {
            return 5;
        }
        
        public String valueToText() {
        	return "<>";
        }
	};

	public abstract int getOrder();
	public abstract String valueToText();

	static public int getOrder(String sValue) {
    	if (sValue == null || sValue.isEmpty())
    		return -1;
    	try {
    		ValueOperatorTypeDTO t = ValueOperatorTypeDTO.textToValue(sValue);
    		return t.getOrder();
    	} catch (Exception ex) {
    		return -1;
    	}
    }

	static public ValueOperatorTypeDTO textToValue(String s) {
		if (s==null || s.isEmpty())
			return null;
		try {
			if (s.equals("<"))
				return LESS_THAN;
			else if (s.equals("<="))
				return LESS_THEN_EQUAL_TO;
			else if (s.equals("="))
				return EQUAL_TO;
			else if (s.equals(">="))
				return GREATER_THAN_EQUAL_TO;
			else if (s.equals(">"))
				return GREATER_THAN;
			else if (s.equals("<>"))
				return NOT_EQUAL_TO;
			else
				return null;
		} catch (Exception ex) {
			return null;
		}
	}
	
}
