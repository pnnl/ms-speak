-- Add Testers to BizRules DB
--     sqlite3 BizRules.db < AddTesters.sql
-- 
-- CREATE TABLE [Testers] ( 
-- 	[Id] INTEGER NOT NULL PRIMARY KEY, 
-- 	[Name]  NVARCHAR(50) NOT NULL,
-- 	[AppId] NVARCHAR(50),
-- 	[Zipcode] NVARCHAR(6),
-- 	UNIQUE(Name)
-- );

insert into Testers (Name,AppId,Zipcode) VALUES ('Amy','baf95429c1395429c1d786308829c144','01824');
insert into Testers (Name,AppId) VALUES ('Bob','75cd2a23af95429c1dbbc7b308455788');
insert into Testers (Name,AppId,Zipcode) VALUES ('Carl','85cd2a23af95429c1dbbc7b308463346','99352');
insert into Testers (Name,Zipcode) VALUES ('Darlene','55788');
insert into Testers (Name) VALUES ('Tom M');
insert into Testers (Name,AppId) VALUES ('Tom Valdez','65cd2a2baf95429c1342786308463577');

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
