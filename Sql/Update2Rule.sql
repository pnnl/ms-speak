-- Add a Rule
-- 	sqlite3 BizRules.db < AddRule.sql

WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='CD_Server')
UPDATE Rules (Tester, Function, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, numRPH, email )
VALUES(
	(SELECT Id FROM Testers WHERE Name ='Carl'),
	(SELECT Id FROM Functions WHERE Name ='Metering Management'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='IsCDSupported' AND EndPoint=(SELECT * from EpId))),
	1,
	2,
	16,
	07,
	13,
	3,
	"carlm@gmail.com"
	);

.quit
