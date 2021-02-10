-- Show Rules Table from BizRules DB
-- 	sqlite3 BizRules.db < ShowRules.sql  

.headers ON
.mode column
.print
.width 3 10 8 8 8 8 8 8 8 35
.print == Rules ==
--pragma table_info('Rules');
select * from Rules;
.print
.exit
