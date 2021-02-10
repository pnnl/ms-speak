-- Test selects
-- 	sqlite3 BizRules.db < SelectTest.sql

.headers ON
.mode column
.print
.width 3 10 8 8 8 8 8 8 8 35
.print == InitiateEndDevicePings Rule ==
SELECT * from rules 
WHERE( (Tester =(SELECT Id FROM Testers WHERE Name ='Carl') AND
       (Method =(SELECT Id FROM Methods WHERE Name ='InitiateEndDevicePings'))
));
.print
.print == IsCDSupported Rule ==
SELECT * from rules 
WHERE( (Tester =(SELECT Id FROM Testers WHERE Name ='Carl') AND
       (Method =(SELECT Id FROM Methods WHERE Name ='IsCDSupported'))
));
.print
.print == PingURL Rule ==
SELECT * from rules 
WHERE( Tester =(SELECT Id FROM Testers WHERE Name ='Carl') AND
	   EndPoint =(SELECT Id FROM EndPoints WHERE Name ='CB_Server') AND
       Method =(SELECT Id FROM Methods WHERE Name ='PingURL')
);
.print
.print == SELECT TEST ==
WITH EpId AS (SELECT Id FROM EndPoints WHERE Name ='CB_Server')
SELECT * from rules
WHERE( Tester =(SELECT Id FROM Testers WHERE Name ='Carl') AND
EndPoint =(SELECT * from EpId) AND
Method =(SELECT Id FROM Methods WHERE (Name ='PingURL' AND EndPoint=(SELECT * from EpId)))
);

.print
.quit
