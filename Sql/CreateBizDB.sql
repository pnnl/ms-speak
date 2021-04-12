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

-- cls;sqlite3 BizRules.db < CreateBizDB.sql;sqlite3 BizRules.db < AddTesters.sql;sqlite3 BizRules.db < ShowTables.sql

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
insert into Functions (Name) VALUES ("Metering Management");
insert into Functions (Name) VALUES ("Work Management");
insert into Functions (Name) VALUES ("Work Order");
insert into Functions (Name) VALUES ("Customer Billing");
insert into Functions (Name) VALUES ("Distribution Engineering");
insert into Functions (Name) VALUES ("Demand Response");
insert into Functions (Name) VALUES ("Distribution Operations");

-- create EndPoints table
CREATE TABLE [EndPoints] (
	[Id] INTEGER NOT NULL PRIMARY KEY,
	[Function] INTEGER NOT NULL,
	[Name] NVARCHAR(50) NOT NULL,
	UNIQUE(Name),
	FOREIGN KEY(Function) REFERENCES Functions(Id)
);
-- set function keys
--  Metering and Service Management Functional Endpoints
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Metering Management'), "CD_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Metering Management'), "MR_Server");

--  Work Management Functional Endpoints
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Work Management'), "WR_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Work Management'), "WO_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Work Management'), "WG_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Work Management'), "SA_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Work Management'), "RM_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Work Management'), "WP_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Work Management'), "WV_Server");

--  Work Order Accounting and Inventory Functional Endpoints
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Work Order'), "ASM_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Work Order'), "FA_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Work Order'), "INV_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Work Order'), "EDTR_Server");

--  Customer Billing and PAN Management Functional Endpoints
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Customer Billing'), "CB_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Customer Billing'), "PPM_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Customer Billing'), "CP_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Customer Billing'), "MDM_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Customer Billing'), "PP_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Customer Billing'), "PG_Server");

--  Distribution Engineering and GIS Abstract Functional Endpoints
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Distribution Engineering'), "AM_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Distribution Engineering'), "DGN_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Distribution Engineering'), "EA_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Distribution Engineering'), "MOD_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Distribution Engineering'), "GIS_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Distribution Engineering'), "LOC_Server");
	
--  Demand Response Functional Endpoints
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Demand Response'), "DM_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Demand Response'), "DR_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Demand Response'), "MM_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Demand Response'), "PAN_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Demand Response'), "DER_Server");

--  Distribution Operations Functional Endpoints
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Distribution Operations'), "CH_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Distribution Operations'), "OD_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Distribution Operations'), "OA_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Distribution Operations'), "DA_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Distribution Operations'), "SCADA_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Distribution Operations'), "SWO_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Distribution Operations'), "LT_Server");
INSERT INTO EndPoints (Function, Name ) VALUES 
	((SELECT Id FROM Functions WHERE Name ='Distribution Operations'), "WEA_Server");
	
-- create Methods table
CREATE TABLE [Methods] (
	[Id] INTEGER NOT NULL PRIMARY KEY,
	[EndPoint] INTEGER NOT NULL,
	[Name] NVARCHAR(50) NOT NULL,
	UNIQUE(EndPoint, Name),
	FOREIGN KEY(EndPoint) REFERENCES EndPoints(Id)
);

-- set endpoint keys
-- All MultiSpeak endpoints SHALL implement the following methods:
--        GetMethods & PingURL
--
-- need support v3 ODEventNotification msg for Benton REA
--     OD and OA

--  Metering and Service Management Methods
--     Connect/Disconnect Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='CD_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='CD_Server'), "PingURL");
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
--     Meter reading Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='MR_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='MR_Server'), "PingURL");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='MR_Server'), "GetLatestMeterReadings");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='MR_Server'), "GetMeterReadingsByBillingCycle");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='MR_Server'), "GetEndDeviceEventsByMeterIDs");

--  Work Management Methods
--     Work Requester Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='WR_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='WR_Server'), "PingURL");
--     Work Owner Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='WO_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='WO_Server'), "PingURL");
--     Work Generator Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='WG_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='WG_Server'), "PingURL");
--     Scheduling & Assignment Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='SA_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='SA_Server'), "PingURL");
--     Resource Management Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='RM_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='RM_Server'), "PingURL");
--     Work Performer Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='WP_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='WP_Server'), "PingURL");
--     Work Viewer Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='WV_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='WV_Server'), "PingURL");

--  Work Order Accounting and Inventory Methods
--     Assembly Management Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='ASM_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='ASM_Server'), "PingURL");
--     Finance and Accounting Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='FA_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='FA_Server'), "PingURL");
--     Inventory Management Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='INV_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='INV_Server'), "PingURL");
--     End Device Testing and Receiving Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='EDTR_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='EDTR_Server'), "PingURL");

--  Customer Billing and PAN Management Methods
--     Customer Billing Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='CB_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='CB_Server'), "PingURL");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='CB_Server'), "ChangeCustomerData");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='CB_Server'), "ChangeMeterData");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='CB_Server'), "ChangeStreetLightData");
--     Prepaid Metering Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='PPM_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='PPM_Server'), "PingURL");
--     Commissioning and Provisioning Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='CP_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='CP_Server'), "PingURL");
--     Meter Data Management Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='MDM_Server'), "InitiateBillingDeterminants");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='MDM_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='MDM_Server'), "PingURL");
--     Payment Processing Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='PP_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='PP_Server'), "PingURL");
--     Payment Gateway Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='PG_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='PG_Server'), "PingURL");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='PG_Server'), "ChangePaymentTransactions");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='PG_Server'), "ChangeRecurringPaymentConfiguration");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='PG_Server'), "ProcessPaymentTransactions");

--  Distribution Engineering and GIS Abstract Methods
--     Asset management Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='AM_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='AM_Server'), "PingURL");
--     Field Design Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='DGN_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='DGN_Server'), "PingURL");
--     Engineering Analysis Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='EA_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='EA_Server'), "PingURL");
--     Network Model Management Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='MOD_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='MOD_Server'), "PingURL");
--     Geographic Information System Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='GIS_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='GIS_Server'), "PingURL");
--     Underground Facility Location Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='LOC_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='LOC_Server'), "PingURL");
	
--  Demand Response Methods
--     Demand Management Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='DM_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='DM_Server'), "PingURL");
--     Demand Response Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='DR_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='DR_Server'), "PingURL");
--     Message Management Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='MM_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='MM_Server'), "PingURL");
--     PAN Communications Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='PAN_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='PAN_Server'), "PingURL");
--     Distributed Energy Resources Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='DER_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='DER_Server'), "PingURL");

--  Distribution Operations Methods
--     Call Handling Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='CH_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='CH_Server'), "PingURL");
--     Outage Detection Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='OD_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='OD_Server'), "PingURL");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='OD_Server'), "ODEventNotification");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='OD_Server'), "GetMeterIDsByEndDeviceStateTypes");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='OD_Server'), "InitiateEndDevicePings");	
--     Outage Analysis Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='OA_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='OA_Server'), "PingURL");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='OA_Server'), "ODEventNotification");
--     Distribution Automation Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='DA_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='DA_Server'), "PingURL");
--     Supervisory Control and Data Acquisition Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='SCADA_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='SCADA_Server'), "PingURL");
--     Switching Orders Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='SWO_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='SWO_Server'), "PingURL");
--     Location Tracking Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='LT_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='LT_Server'), "PingURL");
--     Weather Endpoint
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='WEA_Server'), "GetMethods");
INSERT INTO Methods (EndPoint, Name ) VALUES 
	((SELECT Id FROM EndPoints WHERE Name ='WEA_Server'), "PingURL");

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
