-- Show Tables of BizRules DB
-- 	sqlite3 BizRules.db < ShowTables.sql  

.headers ON
.mode column

.width 3 15
.print == Hosts ==
select * from Hosts;

.print
.width 3 20
.print == Functions ==
select * from Functions;

.print
.width 3 8 10
.print == EndPoints ==
select * from EndPoints;

.print
.width 3 8 35
.print == Methods ==
select * from Methods;

.print
.width 3 10 8 8 8 8 8 8 8 35
.print == Rules ==
--pragma table_info('Rules');
select * from Rules;

.exit
