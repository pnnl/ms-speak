-- Remove a rule from BizRules DB
-- 	sqlite3 BizRules.db < RemoveRule.sql

-- this will remove ALL rules for Tester
--   DELETE FROM Rules WHERE (Tester == (SELECT Id FROM Testers WHERE Name ='Carl'));

-- should also check the Endpoint, in case multiple endpoints share the same method
--		(i.e. PingUrl)

.quit

-- SELECT * FROM Rules WHERE (Tester == (SELECT Id FROM Testers WHERE Name ='Carl'));

