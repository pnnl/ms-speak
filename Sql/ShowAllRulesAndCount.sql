-- Show all rules from BizRules DB
-- 	sqlite3 BizRules.db < ShowAllRules.sql

.headers ON
.mode column
.print
.width 10 19 10 28 7 7 7 7 7 7 20
.print
.print == Number of Rules ==
SELECT COUNT(*) as count
FROM rules
INNER JOIN endpoints ON endpoints.id = rules.endpoint
INNER JOIN methods ON methods.id = rules.method
INNER JOIN testers ON testers.id = rules.tester;
.print
.print == All Rules ==
SELECT testers.Name as who, functions.Name as Function, endpoints.name as EndPoint, methods.name as Method,
rules.maxTemp,rules.minTemp,rules.maxHour,rules.minHour,rules.numReq,rules.numRPH,rules.email
FROM rules
INNER JOIN functions ON functions.id = rules.function
INNER JOIN endpoints ON endpoints.id = rules.endpoint
INNER JOIN methods ON methods.id = rules.method
INNER JOIN testers ON testers.id = rules.tester
ORDER BY
	who;
.print
.quit
