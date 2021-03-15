-- Add a Rule
-- 	sqlite3 BizRules.db < AddRule.sql

WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='CB_Server')
INSERT INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, numRPH, email ) VALUES
	((SELECT Id FROM Testers WHERE Name ='Carl'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='PingURL' AND EndPoint=(SELECT * from EpId))),
	75,
	32,
	14,
	9,
	'',
	'',
	"carl.miller@gmail.com");
	
.quit
