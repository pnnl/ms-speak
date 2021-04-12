-- Create BizRules DB
--     sqlite3 BizRules.db < AddEndpoint.sql

PRAGMA foreign_keys = 1;

-- set method
-- All MultiSpeak endpoints SHALL implement the following methods:
--        GetMethods & PingURL
-- need support v3 ODEventNotification msg for Benton REA
INSERT INTO Methods (EndPoint, Name ) VALUES
	((SELECT Id FROM EndPoints WHERE Name ='XXXXXXXX'), "ODEventNotification"); 	

.exit
