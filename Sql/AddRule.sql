-- Add a Rule
-- 	sqlite3 BizRules.db < AddRule.sql

WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='CD_Server')
INSERT OR REPLACE INTO Rules (Tester, Function, Endpoint, Method, Name, maxTemp, minTemp, maxHour, minHour, numReq, numRPH, email )
VALUES(
	(SELECT Id FROM Testers WHERE Name ='ss'),
	(SELECT Id FROM Functions WHERE Name ='Metering Management'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='IsCDSupported' AND EndPoint=(SELECT * from EpId))),
	"Rule2",
	75,
	32,
	NULL,
	NULL,
	13,
	3,
	"carlm@gmail.com"
	);

.quit
