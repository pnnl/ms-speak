-- Add a Rule
-- 	sqlite3 BizRules.db < AddRule.sql

WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='CD_Server')
INSERT INTO Rules (Tester, Function, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, numRPH, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Carl'),
	(SELECT Id FROM Functions WHERE Name ='Metering Management'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='IsCDSupported' AND EndPoint=(SELECT * from EpId))),
	85,
	42,
	13,
	9,
	5,
	2,
	"carl.miller@gmail.com");
	
.quit
