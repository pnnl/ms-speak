-- Show Active Tester
-- 	sqlite3 BizRules.db < ShowActiveTester.sql

.headers ON
.mode column
.print
.width 3 15 32 7
.print
.print == Show Active Tester ==
SELECT ActiveTester.Tester as Id, Name, AppId, Zipcode
FROM Testers
INNER JOIN ActiveTester ON testers.id = ActiveTester.Tester
WHERE( Testers.Id =(SELECT Tester FROM ActiveTester));
.print
.width 15
.print == Active Tester Name ==
SELECT Name
FROM Testers
INNER JOIN ActiveTester ON testers.id = ActiveTester.Tester
WHERE( Testers.Id =(SELECT Tester FROM ActiveTester));
.print
.quit

