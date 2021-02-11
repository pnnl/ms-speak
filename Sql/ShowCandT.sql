-- Remove a rule from BizRules DB
-- 	sqlite3 BizRules.db < RemoveRule.sql

-- this will remove ALL rules for Tester
--   DELETE FROM Rules WHERE (Tester == (SELECT Id FROM Testers WHERE Name ='Carl'));

-- should also check the Endpoint, in case multiple endpoints share the same method
--		(i.e. PingUrl)
.headers ON
.mode column
.print
.width 10 4 10 28 7 7 7 7 7 35
.print
.print == Tom & Carl's Rules ==
SELECT testers.Name as who ,rules.id as Rule, endpoints.name as EndPoint, methods.name as Method,
rules.maxTemp,rules.minTemp,rules.maxHour,rules.minHour,rules.numReq,rules.email
FROM rules
INNER JOIN endpoints ON endpoints.id = rules.endpoint
INNER JOIN methods ON methods.id = rules.method
INNER JOIN testers ON testers.id = rules.tester
WHERE( Tester =(SELECT Id FROM Testers WHERE Name ='Carl') OR
	   Tester =(SELECT Id FROM Testers WHERE Name ='Tom Valdez')
);
.print
.quit


 
-- Method = 'PingURL' AND
-- EndPoint = 'PG_Server'

;

