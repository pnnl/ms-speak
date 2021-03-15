-- Update a Tester in BizRules DB
--     sqlite3 BizRules.db < UpdateTester.sql

-- 		"INSERT OR REPLACE INTO Testers(Name, AppId, Zipcode) "
--		"VALUES (:Name, :AppId, :Zipcode)"
INSERT OR REPLACE INTO Testers (Name,AppId,Zipcode) VALUES ('Tom Valdez','65cd2a2baf95429c1342786308463577', '12345');

.exit
