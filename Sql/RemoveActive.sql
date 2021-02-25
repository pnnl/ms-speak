-- Remove a Tester and all his or her rules from BizRules DB
-- 	sqlite3 BizRules.db < RemoveTester.sql

.headers ON
.mode column
.print
.print == Remove Tester and its Rules ==
DELETE FROM Rules WHERE id = 
(SELECT rules.id FROM rules
WHERE( Tester =(SELECT id FROM Testers WHERE Name ='Shimoe'))
;
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


-- drop table if exists orders