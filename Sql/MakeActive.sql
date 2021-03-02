-- Make a Tester the Active Tester
-- 	sqlite3 BizRules.db < MakeActive.sql
-- 	sqlite3 BizRules.db param set :who< MakeActive.sql

-- .param set :who %1
-- Do an UPSERT:
-- What does the '@' symbol do in SQL?
--     The @CustID means it's a parameter that you will supply a value for later in your code. 
--     This is the best way of protecting against SQL injection.
--     @ is used as a prefix denoting stored procedure and function parameter names, and also variable names
.print
.print == Make a Tester the Active Tester ==
--INSERT INTO ActiveTester(Id,Tester) VALUES(1, (SELECT Id FROM Testers WHERE Name ='Carl'))
--  ON CONFLICT(Id) DO UPDATE SET Tester=excluded.Tester;
-- 'ON' only support for sqlite 3.24+, wsl ubunutu is only 3.22
INSERT OR REPLACE INTO ActiveTester(Id,Tester) VALUES(1, (SELECT Id FROM Testers WHERE Name ='Carl'));

.print
.width 3 6
.print == Active Tester ==
select * from ActiveTester;
.print
.quit
-- SET Value = REPLACE(Value, '123', '')
-- UPDATE MyTable SET FieldA=@FieldA WHERE Key=@Key
-- 
-- IF @@ROWCOUNT = 0
--    INSERT INTO MyTable (FieldA) VALUES (@FieldA)
--    
-- WITH TesterID AS (SELECT Id FROM Testers WHERE Name ='Carl')
-- UPDATE or INSERT ActiveTester 
-- SET Tester = (SELECT * from TesterID);

-- INSERT INTO phonebook(name,phonenumber) VALUES('Alice','704-555-1212')
--  ON CONFLICT(name) DO UPDATE SET phonenumber=excluded.phonenumber;
