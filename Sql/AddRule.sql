-- Add a rule to BizRules DB
-- 	sqlite3 BizRules.db < AdRule.sql

-- CREATE TABLE [Rules] ( 
-- 	[Id] INTEGER NOT NULL PRIMARY KEY, 
-- 	[Tester] INTEGER NOT NULL, 
-- 	[Endpoint] INTEGER NOT NULL, 
-- 	[Method] INTEGER NOT NULL, 
-- 	[maxTemp] INTEGER NOT NULL,
-- 	[minTemp] INTEGER NOT NULL,
-- 	[maxHour] INTEGER NOT NULL,
-- 	[minHour] INTEGER NOT NULL,
-- 	[numReq] INTEGER NOT NULL,
-- 	[email] NVARCHAR(50) NOT NULL,
-- 	UNIQUE(Tester,Endpoint,Method)
-- );

-- INSERT OR REPLACE INTO t

-- since Id is not the primary key, have to explicitly add it
-- set a rule
INSERT INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Tom Valdez'),
	(SELECT EndPoint FROM Methods WHERE Name ='InitiateBillingDeterminants'),
	(SELECT Id FROM Methods WHERE Name ='InitiateBillingDeterminants'),
	85,
	40,
	18,
	08,
	3,
	"james.in.richland@gmail.com"); 

INSERT INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Carl'),
	(SELECT EndPoint FROM Methods WHERE Name ='InitiateBillingDeterminants'),
	(SELECT Id FROM Methods WHERE Name ='InitiateBillingDeterminants'),
	85,
	40,
	18,
	08,
	3,
	"carl.miller@gmail.com");

INSERT INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Tom M'),
	(SELECT EndPoint FROM Methods WHERE Name ='InitiateBillingDeterminants'),
	(SELECT Id FROM Methods WHERE Name ='InitiateBillingDeterminants'),
	85,
	40,
	18,
	08,
	3,
	"tom Mcd@gmail.com");
	
.quit
