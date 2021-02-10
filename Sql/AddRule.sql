-- Test things
-- 	sqlite3 BizRules.db < CheckRule.sql
--   can use NULL as a value

-- should also check the Endpoint, in case multiple endpoints share the same method
--		(i.e. PingUrl)
-- need to assure that the EP actually has the method defined...
-- i.e., OD_Server doesn't, for testing
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
