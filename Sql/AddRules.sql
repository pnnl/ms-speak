-- Add a rule to BizRules DB
-- 	sqlite3 BizRules.db < AddRule.sql

-- CREATE TABLE [Rules] ( 
-- 	[Id] INTEGER NOT NULL PRIMARY KEY, 
-- 	[Tester] INTEGER NOT NULL, 
-- 	[Endpoint] INTEGER NOT NULL, 
-- 	[Method] INTEGER NOT NULL, 
-- 	[maxTemp] INTEGER CHECK(maxTemp >= -1 AND maxTemp<=150),
-- 	[minTemp] INTEGER CHECK(minTemp >= -1 AND minTemp<150),
-- 	[maxHour] INTEGER CHECK(maxHour >= -1 AND maxHour<=23),
-- 	[minHour] INTEGER CHECK(minHour >= -1 AND minHour<23),
-- 	[numReq] INTEGER,
-- 	[email] NVARCHAR(50),
-- 	UNIQUE(Tester,Endpoint,Method),
-- 	CHECK (maxTemp > minTemp AND maxHour > minHour)
-- ); 

-- should also check the Endpoint, in case multiple endpoints share the same method
--		(i.e. PingUrl)

-- set a rule
-- maybe not use OR REPLACE as each replaces autoincrements the rule Id, use UPDATE instead
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
	"james.in.richland@gmail.com"); 

WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='MDM_Server')
INSERT OR REPLACE INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Tom M'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='InitiateBillingDeterminants' AND EndPoint=(SELECT * from EpId))),	
	85,
	40,
	18,
	08,
	3,
	"tom Mcd@gmail.com");

WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='MDM_Server')
INSERT INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Carl'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='InitiateBillingDeterminants' AND EndPoint=(SELECT * from EpId))),	
	85,
	40,
	18,
	08,
	3,
	"carl.miller@gmail.com");

WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='CB_Server')
INSERT INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Carl'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='PingURL' AND EndPoint=(SELECT * from EpId))),
	85,
	42,
	13,
	9,
	5,
	"carl.miller@gmail.com");

WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='PG_Server')
INSERT INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Carl'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='PingURL' AND EndPoint=(SELECT * from EpId))),
	85,
	42,
	13,
	9,
	5,
	"carl.miller@gmail.com");

.quit
