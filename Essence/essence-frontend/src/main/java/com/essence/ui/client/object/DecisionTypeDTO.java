/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.ui.client.object;


public enum DecisionTypeDTO { // Outcome type of decision
	BLOCK_SOURCE {
        @Override
        public int getOrder() {
            return 5;
        }
	},
	BLOCK_BETWEEN_PAIR {
        @Override
        public int getOrder() {
            return 4;
        }
	},
	BLOCK_DESTINATION {
        @Override
        public int getOrder() {
            return 3;
        }
	},
	ALERT_ONLY {
        @Override
        public int getOrder() {
            return 2;
        }
	},
//	ASSIGN_SEVERITY, // support default actions for high/medium/low or trigger manual_action
	MANUAL_ACTION {
        @Override
        public int getOrder() {
            return 1;
        }
	},
	IGNORE {
        @Override
        public int getOrder() {
            return 0;
        }
	};

    public abstract int getOrder();
//	AUTO_SUPPRESS, //  feedback to detection to skip the specific type of detection.
    static public int getOrder(String sValue) {
    	if (sValue == null || sValue.isEmpty())
    		return -1;
    	try {
			DecisionTypeDTO t = DecisionTypeDTO.valueOf(sValue);
    		return t.getOrder();
    	} catch (Exception ex) {
    		return -1;
    	}
    }
    
	static public DecisionTypeDTO textToValue(String s) {
		if (s==null || s.isEmpty())
			return null;
		try {
			return DecisionTypeDTO.valueOf(s);
		} catch (Exception ex) {
			return null;
		}
	}
}
