-- Create BizRules DB
--     sqlite3 BizRules.db < BizRules.sql
--	dot commands are allowed, but must be lowercase

-- can wrap commands around Begin/Commit:
--		BEGIN;
--		COMMIT;

-- create tester table
CREATE TABLE [Testers] ( 
	[Id] INTEGER NOT NULL PRIMARY KEY, 
	[Name] NVARCHAR(50) NOT NULL  
); 
insert into Testers (Name) VALUES ('Carl');
insert into Testers (Name) VALUES ('Tom M');
insert into Testers (Name) VALUES ('Tom Valdez');

-- create Functions table
CREATE TABLE [Functions] ( 
	[Id] INTEGER NOT NULL PRIMARY KEY, 
	[Name] NVARCHAR(50) NOT NULL  
); 
insert into Functions (Name) VALUES ("Customer Billing");
insert into Functions (Name) VALUES ("Metering Management");
insert into Functions (Name) VALUES ("Outage Management");

-- create EndPoints table
CREATE TABLE [EndPoints] ( 
	[Id] INTEGER NOT NULL PRIMARY KEY, 
	[Function] INTEGER NOT NULL, 
	[Name] NVARCHAR(50) NOT NULL  
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
	[Name] NVARCHAR(50) NOT NULL  
); 
-- set endpoint keys
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='CB_Server'), "ChangeCustomerData"); 
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='CB_Server'), "ChangeMeterData"); 
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='CB_Server'), "ChangeStreetLightData"); 
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
	((SELECT Id FROM EndPoints WHERE Name ='MDM_Server'), "InitiateBillingDeterminants"); 
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='MR_Server'), "GetLatestMeterReadings"); 
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='MR_Server'), "GetMeterReadingsByBillingCycle"); 
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='MR_Server'), "GetEndDeviceEventsByMeterIDs"); 
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='PG_Server'), "ChangePaymentTransactions"); 
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='PG_Server'), "ChangeRecurringPaymentConfiguration"); 
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='PG_Server'), "ProcessPaymentTransactions"); 
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='OD_Server'), "GetMeterIDsByEndDeviceStateTypes"); 
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='OD_Server'), "InitiateEndDevicePings"); 

-- create rules table
--    Check that rule to be inserted has method EP id == the Endpoint ID
CREATE TABLE [Rules] ( 
	[Id] INTEGER NOT NULL PRIMARY KEY, 
	[Tester] INTEGER NOT NULL, 
	[Endpoint] INTEGER NOT NULL, 
	[Method] INTEGER NOT NULL, 
	[maxTemp] INTEGER,
	[minTemp] INTEGER,
	[maxHour] INTEGER,
	[minHour] INTEGER,
	[numReq] INTEGER,
	[email] NVARCHAR(50),
	UNIQUE(Tester,Endpoint,Method)
); 

.exit
