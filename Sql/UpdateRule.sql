-- Update a rule in BizRules DB
-- 	sqlite3 BizRules.db < UpdateRule.sql

-- should also check the Endpoint, in case multiple endpoints share the same method
--		(i.e. PingUrl)

.print
.print == Update IsCDSupported Rule ==
WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='CD_Server')
UPDATE Rules 
SET maxHour = 22, minHour = 02
WHERE( Tester = (SELECT Id FROM Testers WHERE Name ='Carl') AND
	   EndPoint = (SELECT * from EpId) AND	   
       Method = (SELECT Id FROM Methods WHERE Name ='IsCDSupported')
	   );
.print	
.quit
