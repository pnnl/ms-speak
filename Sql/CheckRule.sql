-- Check that rule to be inserted has method EP id == the Endpoint ID

-- INSERT OR REPLACE INTO t
INSERT INTO Rules (Tester, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, email ) VALUES 
	((SELECT Id FROM Testers WHERE Name ='Tom M'),
	(SELECT EndPoint FROM Methods WHERE Name ='InitiateBillingDeterminants'),
	(SELECT Id FROM Methods WHERE Name ='InitiateBillingDeterminants'),
	85,
	40,
	18,
	08,
	3,
	"carl.miller@gmail.com");
	
.quit

-- instead of hardcoding the id from 'CB_Server' get the Endpoints.Id from Methods.Endpoint
-- Endpoint == (select Id from EndPoints where id == (select EndPoint from Rules)
-- 
-- old way:
-- 	  (SELECT Id FROM Endpoints WHERE Name ='MDM_Server'),
-- new way:
-- 	  (SELECT EndPoint FROM Methods WHERE Methods.Id = Rules.Method),
--			doesn't work on an empty table

-- try:
--	  (SELECT EndPoint FROM Methods WHERE Name ='InitiateBillingDeterminants'),