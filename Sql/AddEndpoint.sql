-- Create BizRules DB
--     sqlite3 BizRules.db < AddEndpoint.sql

PRAGMA foreign_keys = 1;

-- set endpoint
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Customer Billing'), "XXXXXXXX"); 

-- All MultiSpeak endpoints SHALL implement the following methods:
--        GetMethods & PingURL
INSERT INTO Methods (EndPoint, Name ) VALUES
	((SELECT Id FROM EndPoints WHERE Name ='XXXXXXXX'), "PingURL"); 	

INSERT INTO Methods (EndPoint, Name ) VALUES
	((SELECT Id FROM EndPoints WHERE Name ='XXXXXXXX'), "GetMethods"); 	

.exit
