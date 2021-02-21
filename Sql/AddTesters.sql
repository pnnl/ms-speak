-- Create BizRules DB
--     sqlite3 BizRules.db < AddTesters.sql

insert into Testers (Name,Host,AppId,Zipcode) VALUES ('Amy','155.235.205.55','baf95429c1395429c1d786308829c144','01824');
insert into Testers (Name,Host,AppId) VALUES ('Bob','10.36.245.27', '75cd2a23af95429c1dbbc7b308455788');
insert into Testers (Name,Host,AppId,Zipcode) VALUES ('Carl','172.31.153.24','85cd2a23af95429c1dbbc7b308463346','99352');
insert into Testers (Name,Host,Zipcode) VALUES ('Darlene','55.35.105.155', '55788');
insert into Testers (Name,Host) VALUES ('Tom M','0.0.0.0');
insert into Testers (Name,Host,AppId) VALUES ('Tom Valdez','192.168.7.2','65cd2a2baf95429c1342786308463577');

-- create hosts table - combine this into tester table
-- CREATE TABLE [Hosts] ( 
-- 	[Id] INTEGER NOT NULL PRIMARY KEY, 
-- 	[Addr] NVARCHAR(32) NOT NULL,
-- 	UNIQUE(Addr),
-- 	CHECK(length(Addr) >= 7 AND length(Addr)<=15)
-- ); 
-- insert into Hosts (Addr) VALUES ('255.255.255.255');
-- insert into Hosts (Addr) VALUES ('0.0.0.0');

.exit
