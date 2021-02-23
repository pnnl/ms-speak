-- Show Tables of BizRules DB
-- 	sqlite3 BizRules.db < ShowAcTables.sql  

.headers ON
.mode column

.width 3 15 32 7
.print == Testers ==
select * from Testers;
.print

.width 3 6
.print == Active Tester ==
select * from ActiveTester;
.print
.width 3 10 8 8 7 7 7 7 6 6 35
.print == Rules ==
--pragma table_info('Rules');
select * from Rules;

.exit
