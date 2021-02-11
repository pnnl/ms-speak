-- Show Function Endpoints from BizRules DB
-- 	sqlite3 BizRules.db < ShowFunctionEndpoints.sql  

.headers ON
.mode column
.print
.width 35
.print
.print == CB_Server Methods ==
SELECT Methods.name as Name
FROM Endpoints
INNER JOIN Methods ON Methods.Endpoint = Endpoints.id
WHERE Endpoints.id =(SELECT Id FROM Endpoints WHERE Name ='CB_Server');
.print
.print == MDM_Server Methods ==
SELECT Methods.name as Name
FROM Endpoints
INNER JOIN Methods ON Methods.Endpoint = Endpoints.id
WHERE Endpoints.id =(SELECT Id FROM Endpoints WHERE Name ='MDM_Server');
.print
.print == PG_Server Methods ==
SELECT Methods.name as Name
FROM Endpoints
INNER JOIN Methods ON Methods.Endpoint = Endpoints.id
WHERE Endpoints.id =(SELECT Id FROM Endpoints WHERE Name ='PG_Server');
.print
.print == CD_Server Methods ==
SELECT Methods.name as Name
FROM Endpoints
INNER JOIN Methods ON Methods.Endpoint = Endpoints.id
WHERE Endpoints.id =(SELECT Id FROM Endpoints WHERE Name ='CD_Server');
.print
.print == MR_Server Methods ==
SELECT Methods.name as Name
FROM Endpoints
INNER JOIN Methods ON Methods.Endpoint = Endpoints.id
WHERE Endpoints.id =(SELECT Id FROM Endpoints WHERE Name ='MR_Server');
.print
.print == OD_Server Methods ==
SELECT Methods.name as Name
FROM Endpoints
INNER JOIN Methods ON Methods.Endpoint = Endpoints.id
WHERE Endpoints.id =(SELECT Id FROM Endpoints WHERE Name ='OD_Server');
.print
.exit
