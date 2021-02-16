-- Show All Function Methods from BizRules DB
-- 	sqlite3 BizRules.db < AllFunctionsMethods.sql  

.headers ON
.mode column
.print
.width 20 10 35
.print
.print == All Functions Methods ==
SELECT functions.name as Function, endpoints.name as EndPoint, methods.name as Method
FROM Functions
INNER JOIN endpoints ON endpoints.Function = Functions.id
INNER JOIN methods ON methods.EndPoint = endpoints.id
ORDER BY Function, EndPoint, Method;
.print
.exit
