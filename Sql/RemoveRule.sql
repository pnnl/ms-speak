-- Remove a rule from BizRules DB
-- 	sqlite3 BizRules.db < RemoveRule.sql

-- this will remove ALL rules for Tester
--   DELETE FROM Rules WHERE (Tester = (SELECT Id FROM Testers WHERE Name ='Carl'));

-- should also check the Endpoint, in case multiple endpoints share the same method
--		(i.e. PingUrl)
.headers ON
.mode column
.print
.print == Remove Rule ==
DELETE FROM Rules WHERE id = 
(SELECT rules.id
FROM rules
INNER JOIN endpoints ON endpoints.id = rules.endpoint
INNER JOIN methods ON methods.id = rules.method
WHERE( Tester =(SELECT id FROM Testers WHERE Name ='Carl')  AND
	   rules.endpoint =(SELECT id FROM endpoints WHERE Name ='MR_Server') AND
	   rules.method IN (SELECT id FROM methods WHERE Name ='GetMeterReadingsByBillingCycle')));
.print
.quit
 
 -- SELECT rules.id as RuleID
-- FROM rules
-- INNER JOIN endpoints ON endpoints.id = rules.endpoint
-- INNER JOIN methods ON methods.id = rules.method
-- WHERE( Tester =(SELECT id FROM Testers WHERE Name ='Carl')  AND
-- 	   rules.endpoint =(SELECT id FROM endpoints WHERE Name ='PG_Server') AND
-- 	   rules.method IN (SELECT id FROM methods WHERE Name ='PingURL')
-- );


