-- Add some rules to BizRules DB
-- 	sqlite3 BizRules.db < AddRules.sql

-- set a rule
-- maybe not use OR REPLACE as each replaces autoincrements the rule Id, use UPDATE instead

WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='CB_Server')
INSERT INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Carl'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='PingURL' AND EndPoint=(SELECT * from EpId))),
	75,
	32,
	14,
	9,
	5,
	"carl.miller@gmail.com");

WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='MDM_Server')
INSERT INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Tom Valdez'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='InitiateBillingDeterminants' AND EndPoint=(SELECT * from EpId))),	
	85,
	40,
	18,
	08,
	3,
	"tv.in.richland@gmail.com"); 

WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='MDM_Server')
INSERT INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Carl'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='InitiateBillingDeterminants' AND EndPoint=(SELECT * from EpId))),	
	79,
	44,
	13,
	05,
	4,
	"carl.miller@gmail.com");

WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='CD_Server')
INSERT OR REPLACE INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Tom M'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='IsCDSupported' AND EndPoint=(SELECT * from EpId))),	
	82,
	42,
	16,
	07,
	3,
	"tom Mcd@gmail.com");



WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='PG_Server')
INSERT INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Carl'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='PingURL' AND EndPoint=(SELECT * from EpId))),
	95,
	33,
	15,
	10,
	7,
	"carl.miller@gmail.com");

.quit
