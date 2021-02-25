-- Remove a Tester and all his or her rules from BizRules DB
-- 	sqlite3 BizRules.db < RemoveTester.sql

.headers ON
.mode column
.print
.print == Remove Tester Rules ==
DELETE FROM Rules WHERE id IN 
(SELECT rules.id FROM rules
WHERE( Tester =(SELECT id FROM Testers WHERE Name ='Shimoe')));
.print
.print == Remove From Active Tester ==
DELETE FROM ActiveTester WHERE Tester = (SELECT Id FROM Testers WHERE Name ='Shimoe');
.print
.print == Remove Tester ==
DELETE FROM Testers WHERE Name ='Shimoe';
.print
.quit
-- drop table if exists orders
-- NOTE:  use 'IN' instead of '=' to delete ALL the records that match, else
--			it only deletes the first one it matches