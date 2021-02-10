-- Test things
-- 	sqlite3 BizRules.db < CheckRule.sql
--   can use NULL as a value

INSERT OR REPLACE INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Carl'),
	(SELECT EndPoint FROM Methods WHERE Name ='InitiateEndDevicePings'),
	(SELECT Id FROM Methods WHERE Name ='InitiateEndDevicePings'),
	99,
	32,
	-1,
	-1,
	5,
	"carl.miller@gmail.com");
	
.quit
