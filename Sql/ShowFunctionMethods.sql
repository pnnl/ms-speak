-- Show Function Methods from BizRules DB
-- 	sqlite3 BizRules.db < ShowFunctionMethods.sql  

.headers ON
.mode column
.print
.width 0 35
.print
.print == Customer Billing Methods ==
SELECT endpoints.name as EndPoint, methods.name as Method
FROM Functions
INNER JOIN endpoints ON endpoints.Function = Functions.id
INNER JOIN methods ON methods.EndPoint = endpoints.id
WHERE Functions.id =(SELECT Id FROM Functions WHERE Name ='Customer Billing');
.print
.print == Metering Management Methods ==
SELECT endpoints.name as EndPoint, methods.name as Method
FROM Functions
INNER JOIN endpoints ON endpoints.Function = Functions.id
INNER JOIN methods ON methods.EndPoint = endpoints.id
WHERE Functions.id =(SELECT Id FROM Functions WHERE Name ='Metering Management');
.print
.print == Outage Management Methods ==
SELECT endpoints.name as EndPoint, methods.name as Method
FROM Functions
INNER JOIN endpoints ON endpoints.Function = Functions.id
INNER JOIN methods ON methods.EndPoint = endpoints.id
WHERE Functions.id =(SELECT Id FROM Functions WHERE Name ='Outage Management');
.print
.exit

-- == Customer Billing Methods ==
-- EndPoint    Method
-- ----------  -----------------------------------
-- CB_Server   ChangeCustomerData
-- CB_Server   ChangeMeterData
-- CB_Server   ChangeStreetLightData
-- CB_Server   PingURL
-- MDM_Server  InitiateBillingDeterminants
-- MDM_Server  PingURL
-- PG_Server   ChangePaymentTransactions
-- PG_Server   ChangeRecurringPaymentConfiguration
-- PG_Server   ProcessPaymentTransactions
-- PG_Server   PingURL