-- Test things
-- 	sqlite3 BizRules.db < Write2File.sql

.headers OFF
.mode list
.separator ,
.output methods.txt

SELECT testers.Name as who, endpoints.name as EndPoint, methods.name as Method,
rules.maxTemp,rules.minTemp,rules.maxHour,rules.minHour,rules.numReq,rules.email
FROM rules
INNER JOIN endpoints ON endpoints.id = rules.endpoint
INNER JOIN methods ON methods.id = rules.method
INNER JOIN testers ON testers.id = rules.tester
;

.quit
