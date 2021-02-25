-- Add a Tester and some Rules for it
-- 	sqlite3 BizRules.db < AddTesterAndRules.sql.sql


insert or ignore into Testers (Name,AppId,Zipcode) VALUES ('Shimoe','baf5768aced39529c1d7863088d0gged','99354');

WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='CB_Server')
INSERT OR REPLACE INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, numRPH, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Shimoe'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='ChangeStreetLightData' AND EndPoint=(SELECT * from EpId))),
	95,
	32,
	20,
	8,
	15,
	5,
	"Shimoe.Begoi@hotmail.com");

WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='PG_Server')
INSERT OR REPLACE INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, numRPH, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Shimoe'),
	(SELECT * from EpId),
	(SELECT Id FROM Methods WHERE (Name ='ProcessPaymentTransactions' AND EndPoint=(SELECT * from EpId))),
	95,
	32,
	21,
	7,
	15,
	5,
	"Shimoe.Begoi@hotmail.com");
	
.quit

