-- Create BizRules DB
--     sqlite3 BizRules.db < CreateBizDB.sql
--	   sudo apt-get install libsqlite3-dev

--	dot commands are allowed, but must be lowercase

--		Enter ".help" for usage hints.

--		Querying the database tables/schema
--			.tables
--			.schema   Shows all the CREATE statements

-- can wrap commands around Begin/Commit:
--		BEGIN;
--		COMMIT;

-- note: may want to have the DB be ephemeral, exist only
--		in memory so as to not leave a digital signature.
--		except then the testers would have to recreate all their rules each time

-- cls;sqlite3 BizRules.db < CreateBizDB.sql; sqlite3 BizRules.db < AddTesters.sql; sqlite3 BizRules.db < ShowTables.sql

PRAGMA foreign_keys = 1;

-- create tester table
CREATE TABLE [Testers] ( 
	[Id] INTEGER NOT NULL PRIMARY KEY, 
	[Name]  NVARCHAR(50) NOT NULL,
	[AppId] NVARCHAR(50),
	[Zipcode] NVARCHAR(6),
 	UNIQUE(Name)
); 

-- create ActiveTester table
CREATE TABLE [ActiveTester] ( 
	[Id] INTEGER NOT NULL PRIMARY KEY,
	[Tester] INTEGER NOT NULL,
	FOREIGN KEY(Tester) REFERENCES Testers(Id)
);	
	
-- create Functions table
CREATE TABLE [Functions] ( 
	[Id] INTEGER NOT NULL PRIMARY KEY, 
	[Name] NVARCHAR(50) NOT NULL,
	UNIQUE(Name)	
); 
insert into Functions (Name) VALUES ("Customer Billing");
insert into Functions (Name) VALUES ("Metering Management");
insert into Functions (Name) VALUES ("Outage Management");

-- create EndPoints table
CREATE TABLE [EndPoints] (
	[Id] INTEGER NOT NULL PRIMARY KEY,
	[Function] INTEGER NOT NULL,
	[Name] NVARCHAR(50) NOT NULL,
	UNIQUE(Name),
	FOREIGN KEY(Function) REFERENCES Functions(Id)
); 
-- set function keys
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Customer Billing'), "CB_Server"); 
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Customer Billing'), "MDM_Server"); 
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Customer Billing'), "PG_Server"); 
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Metering Management'), "CD_Server"); 
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Metering Management'), "MR_Server"); 
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Outage Management'), "OD_Server"); 

-- create Methods table
CREATE TABLE [Methods] (
	[Id] INTEGER NOT NULL PRIMARY KEY,
	[EndPoint] INTEGER NOT NULL,
	[Name] NVARCHAR(50) NOT NULL,
	UNIQUE(EndPoint, Name),
	FOREIGN KEY(EndPoint) REFERENCES EndPoints(Id)
); 
-- set endpoint keys
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='CB_Server'), "ChangeCustomerData"); 
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='CB_Server'), "ChangeMeterData"); 
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='CB_Server'), "ChangeStreetLightData"); 
INSERT INTO Methods (EndPoint, Name ) VALUES
	((SELECT Id FROM EndPoints WHERE Name ='CB_Server'), "PingURL"); 	

INSERT INTO Methods (EndPoint, Name ) VALUES
	((SELECT Id FROM EndPoints WHERE Name ='CD_Server'), "GetCDSupportedMeters"); 	
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='CD_Server'), "InitiateConnectDisconnect"); 	
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='CD_Server'), "IsCDSupported"); 	
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='CD_Server'), "SetCDDevicesDisabled"); 	
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='CD_Server'), "SetCDDevicesEnabled"); 	
INSERT INTO Methods (EndPoint, Name ) VALUES
	((SELECT Id FROM EndPoints WHERE Name ='CD_Server'), "PingURL"); 	

INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='MDM_Server'), "InitiateBillingDeterminants"); 
INSERT INTO Methods (EndPoint, Name ) VALUES
	((SELECT Id FROM EndPoints WHERE Name ='MDM_Server'), "PingURL"); 	

INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='MR_Server'), "GetLatestMeterReadings"); 
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='MR_Server'), "GetMeterReadingsByBillingCycle"); 
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='MR_Server'), "GetEndDeviceEventsByMeterIDs"); 
INSERT INTO Methods (EndPoint, Name ) VALUES
	((SELECT Id FROM EndPoints WHERE Name ='MR_Server'), "PingURL"); 	

INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='PG_Server'), "ChangePaymentTransactions"); 
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='PG_Server'), "ChangeRecurringPaymentConfiguration"); 
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='PG_Server'), "ProcessPaymentTransactions"); 
INSERT INTO Methods (EndPoint, Name ) VALUES
	((SELECT Id FROM EndPoints WHERE Name ='PG_Server'), "PingURL"); 	

INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='OD_Server'), "GetMeterIDsByEndDeviceStateTypes"); 
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='OD_Server'), "InitiateEndDevicePings"); 
--INSERT INTO Methods (EndPoint, Name ) VALUES
--	((SELECT Id FROM EndPoints WHERE Name ='OD_Server'), "PingURL"); 	

-- create rules table - not sure if even need to have Id
-- convert IPs:
-- 	select (ip >> 24) || '.' || ((ip >> 16) & 255) || '.' || ((ip >> 8) &
-- 		255) || '.' || (ip & 255) from mytable;
CREATE TABLE [Rules] ( 
	[Id] INTEGER NOT NULL PRIMARY KEY, 
	[Tester] INTEGER NOT NULL, 
	[Function] INTEGER NOT NULL,
	[Endpoint] INTEGER NOT NULL, 
	[Method] INTEGER NOT NULL, 
	[maxTemp] INTEGER CHECK( (maxTemp = NULL) OR (maxTemp between 32 and 120) ),
	[minTemp] INTEGER CHECK( (minTemp = NULL) OR (minTemp between 0 and 100) ),
	[maxHour] INTEGER CHECK( (maxHour = NULL) OR (maxHour between 1 and 24) ),
	[minHour] INTEGER CHECK( (minHour = NULL) OR (minHour between 0 and 23) ),
	[numReq] INTEGER,
	[numRPH] INTEGER,
	[email] NVARCHAR(50),
	UNIQUE(Tester,Endpoint,Method),
	CHECK( (maxTemp = NULL AND minTemp = NULL) OR (maxTemp > minTemp) ),
	CHECK( (maxHour = NULL AND minHour = NULL) OR (maxHour > minHour) ),
	FOREIGN KEY(Tester) REFERENCES Testers(Id),
	FOREIGN KEY(Function) REFERENCES Functions(Id),
	FOREIGN KEY(Endpoint) REFERENCES Endpoints(Id),
	FOREIGN KEY(Method) REFERENCES Methods(Id)
); 

.exit
