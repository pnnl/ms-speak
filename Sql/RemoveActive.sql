-- Remove Remove Active Tester from BizRules DB
-- 	sqlite3 BizRules.db < RemoveActive.sql

.headers ON
.mode column
.print
.print == Remove Active Tester ==
DELETE FROM ActiveTester WHERE Tester =
(SELECT Id FROM Testers WHERE Name = 'Bob');
.print
.width 3 6
.print == Active Tester ==
select * from ActiveTester;
.print
.quit

