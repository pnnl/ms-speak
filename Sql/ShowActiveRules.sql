-- Show Active Rules
-- 	sqlite3 BizRules.db < ShowActiveRules.sql

.headers ON
.mode column
.print
.width 10 4 10 28 7 7 7 7 6 6 35
.print
.print == Show Active Rules ==
SELECT testers.Name as who ,rules.id as Rule, endpoints.name as EndPoint, methods.name as Method,
rules.maxTemp,rules.minTemp,rules.maxHour,rules.minHour,rules.numReq,rules.numRPH,rules.email
FROM rules
INNER JOIN endpoints ON endpoints.id = rules.endpoint
INNER JOIN methods ON methods.id = rules.method
INNER JOIN testers ON testers.id = rules.tester
WHERE( rules.Tester =(SELECT Tester FROM ActiveTester)
);
.print
.quit

