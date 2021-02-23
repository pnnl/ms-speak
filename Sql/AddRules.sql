-- Add some rules to BizRules DB
-- 	sqlite3 BizRules.db < AddRules.sql

-- set some rules

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

WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='MDM_Server')
INSERT INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, numRPH, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Tom Valdez'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='InitiateBillingDeterminants' AND EndPoint=(SELECT * from EpId))),	
	85,
	40,
	18,
	08,
	'',
	3,
	"tv.in.richland@gmail.com"); 

WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='MDM_Server')
INSERT INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, numRPH, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Carl'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='InitiateBillingDeterminants' AND EndPoint=(SELECT * from EpId))),	
	79,
	44,
	13,
	05,
	14,
	4,
	"carl.miller@gmail.com");

WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='CD_Server')
INSERT OR REPLACE INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, numRPH, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Tom M'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='IsCDSupported' AND EndPoint=(SELECT * from EpId))),	
	82,
	42,
	16,
	07,
	13,
	3,
	"tom Mcd@gmail.com");

WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='PG_Server')
INSERT INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, numRPH, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Carl'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='PingURL' AND EndPoint=(SELECT * from EpId))),
	95,
	33,
	15,
	10,
	17,
	7,
	'');

WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='PG_Server')
INSERT INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, numRPH, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Darlene'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='PingURL' AND EndPoint=(SELECT * from EpId))),
	95,
	33,
	15,
	10,
	7,
	'',
	'');


WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='PG_Server')
INSERT INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, numRPH, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Amy'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='PingURL' AND EndPoint=(SELECT * from EpId))),
	77,
	43,
	11,
	8,
	13,
	3,
	'');

.quit
