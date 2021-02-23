-- Add a Rule
-- 	sqlite3 BizRules.db < AddRule.sql

WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='CD_Server')
INSERT INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Carl'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='IsCDSupported' AND EndPoint=(SELECT * from EpId))),
	85,
	42,
	13,
	9,
	5,
	"carl.miller@gmail.com");
	
.quit
