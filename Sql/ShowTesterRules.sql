-- Show Rules for a tester from BizRules DB
-- 	sqlite3 BizRules.db < ShowTesterRules.sql  

.headers ON
.mode column
.print
.width 4 10 28 7 7 7 7 7 35
.print
.print == Carls Rules ==
SELECT rules.id as Rule, endpoints.name as EndPoint, methods.name as Method,
rules.maxTemp,rules.minTemp,rules.maxHour,rules.minHour,rules.numReq,rules.email
FROM rules
INNER JOIN endpoints ON endpoints.id = rules.endpoint
INNER JOIN methods ON methods.id = rules.method
WHERE Tester =(SELECT Id FROM Testers WHERE Name ='Carl');
.print
.exit


-- == Carls Rules ==
-- Rule  EndPoint    Method  
-- ----  ----------  --------
-- 4     CB_Server   PingURL 
-- 3     MDM_Server  Initiate
-- 5     PG_Server   PingURL 
-- maxTemp   minTemp   maxHour   minHour   numReq    email

-- SELECT rules.id as Rule, endpoints.name as EndPoint, methods.name as Method
-- FROM rules
-- INNER JOIN endpoints ON endpoints.id = rules.endpoint
-- INNER JOIN methods ON methods.id = rules.method
-- WHERE Tester =(SELECT Id FROM Testers WHERE Name ='Carl');
