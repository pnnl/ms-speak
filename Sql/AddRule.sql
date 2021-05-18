-- Add a Rule
-- 	sqlite3 BizRules.db < AddRule.sql
-- WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='CD_Server')
-- 	(SELECT Id FROM Functions WHERE Name ='Metering Management'),
-- 	(SELECT Id FROM Methods WHERE (Name ='IsCDSupported' AND EndPoint=(SELECT * from EpId))),

WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='SA_Server')
INSERT OR REPLACE INTO Rules (Tester, Function, Endpoint, Method, Name, maxTemp, minTemp, maxHour, minHour, Inverse, numReq, numRPH, email )
VALUES(
	(SELECT Id FROM Testers WHERE Name ='Carl'),
	(SELECT Id FROM Functions WHERE Name ='Work Management'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='GetMethods' AND EndPoint=(SELECT * from EpId))),
	"Rule1",
	77,
	32,
	17,
	9,
	0,
	23,
	6,
	"carlm@gmail.com"
	);

.quit
