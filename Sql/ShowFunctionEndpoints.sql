-- Show Function Endpoints from BizRules DB
-- 	sqlite3 BizRules.db < ShowFunctionEndpoints.sql  

.headers ON
.mode column
.print
.width 10
.print
.print == Customer Billing Endpoints ==
SELECT endpoints.name as Name
FROM Functions
INNER JOIN endpoints ON endpoints.Function = Functions.id
WHERE Functions.id =(SELECT Id FROM Functions WHERE Name ='Customer Billing');
.print
.print == Metering Management Endpoints ==
SELECT endpoints.name as Name
FROM Functions
INNER JOIN endpoints ON endpoints.Function = Functions.id
WHERE Functions.id =(SELECT Id FROM Functions WHERE Name ='Metering Management');
.print
.print == Outage Management Endpoints ==
SELECT endpoints.name as Name
FROM Functions
INNER JOIN endpoints ON endpoints.Function = Functions.id
WHERE Functions.id =(SELECT Id FROM Functions WHERE Name ='Outage Management');
.print
.exit

