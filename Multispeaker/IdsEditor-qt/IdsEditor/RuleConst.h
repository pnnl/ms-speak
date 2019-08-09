//-------------------------------------------------------------------------------
// This code created by LMI Developments, LLC
//
// Copyright 2019.  All Rights Reserved.
//
//  Created By: Lance Irvine
//
//  RuleConst
// 

#ifndef RULECONST_H
#define RULECONST_H

#include <QHash>
#include <QString>
#include <QStringList>

// Version
const QString SOFTWARE_VERSION = QStringLiteral("19.08.09");
const QString SOFTWARE_ABOUT = QString("<center><h2>IDS Editor - MS-SPEAK</h2><h4>Copyright 2019</h4><h4>LMI Developments, LLC</h4><h5>All Rights Reserved.</h5><h3>Version " + SOFTWARE_VERSION + "</h3></center");

// Log Consts
const QString SETTINGS_GROUP = QStringLiteral("[Settings]");
const QString SETTINGS_LOG_FILE = QStringLiteral("LogFile");

// Rule Types
const QString RULE_TYPE_MAX_VALUE = QStringLiteral("MaxValue");
const QString RULE_TYPE_TEMP_RANGE = QStringLiteral("TempRange");
const QString RULE_TYPE_TIME_RANGE = QStringLiteral("TimeRange");

// Rule Keys
const QString RULE_KEY_MAXTEMP = QStringLiteral("maxTemp");
const QString RULE_KEY_MAXTIME = QStringLiteral("maxTime");
const QString RULE_KEY_MINTEMP = QStringLiteral("minTemp");
const QString RULE_KEY_MINTIME = QStringLiteral("minTime");
const QString RULE_KEY_NUMREQ = QStringLiteral("numReq");

// Functions
const QString CUSTOMER_BILLING = QStringLiteral("Customer Billing");
const QString METERING_MANAGEMENT = QStringLiteral("Metering Management");
const QString OUTAGE_MANAGEMENT = QStringLiteral("Outage Management");

// EndPoints
const QString CB_SERVER = QStringLiteral("CB_Server");
const QString CD_SERVER = QStringLiteral("CD_Server");
const QString MDM_SERVER = QStringLiteral("MDM_Server");
const QString MR_SERVER = QStringLiteral("MR_Server");
const QString OD_SERVER = QStringLiteral("OD_Server");
const QString PG_SERVER = QStringLiteral("PG_Server");

// CB Methods
const QString CHANGE_CUSTOMER_DATA = QStringLiteral("ChangeCustomerData");
const QString CHANGE_METER_DATA = QStringLiteral("ChangeMeterData");
const QString CHANGE_STREET_LIGHT_DATA = QStringLiteral("ChangeStreetLightData");

// CD Methods
const QString GET_CD_SUPPORTED_METERS = QStringLiteral("GetCDSupportedMeters");
const QString INITIATE_CONNECT_DISCONNECT = QStringLiteral("InitiateConnectDisconnect");
const QString IS_CD_SUPPORTED = QStringLiteral("IsCDSupported");
const QString SET_CD_DEVICES_DISABLED = QStringLiteral("SetCDDevicesDisabled");
const QString SET_CD_DEVICES_ENABLED = QStringLiteral("SetCDDevicesEnabled");

// MDM Methods
const QString INITIATE_BILLING_DETERMINANTS = QStringLiteral("InitiateBillingDeterminants");

// MR Methods
const QString GET_LATEST_METER_READINGS = QStringLiteral("GetLatestMeterReadings");
const QString GET_METER_READINGS_BY_BILLINGCYCLE = QStringLiteral("GetMeterReadingsByBillingCycle");
const QString GET_END_DEVICE_EVENTS_BY_METERIDS = QStringLiteral("GetEndDeviceEventsByMeterIDs");

// PG Methods
const QString CHANGE_PAYMENT_TRANSACTIONS = QStringLiteral("ChangePaymentTransactions");
const QString CHANGE_RECURRING_PAYMENT_CONFIGURATION = QStringLiteral("ChangeRecurringPaymentConfiguration");
const QString PROCESS_PAYMENT_TRANSACTIONS = QStringLiteral("ProcessPaymentTransactions");

// OD Methods
const QString GET_METER_IDS_BY_END_DEVICE_STATE_TYPES = QStringLiteral("GetMeterIDsByEndDeviceStateTypes");
const QString INITIATE_END_DEVICE_PINGS = QStringLiteral("InitiateEndDevicePings");

static QStringList FUNCTION_LIST = QStringList()
<< CUSTOMER_BILLING << METERING_MANAGEMENT << OUTAGE_MANAGEMENT;

static QStringList CUSTOMER_BILLING_ENDPOINT_LIST = QStringList()
<< CB_SERVER << MDM_SERVER << PG_SERVER;

static QStringList METERING_MANAGEMENT_ENDPOINT_LIST = QStringList()
<< CD_SERVER << MR_SERVER;

static QStringList OUTAGE_MANAGEMENT_ENDPOINT_LIST = QStringList()
<< OD_SERVER;

static QStringList CB_METHOD_LIST = QStringList()
<< CHANGE_CUSTOMER_DATA << CHANGE_METER_DATA << CHANGE_STREET_LIGHT_DATA;

static QStringList CD_METHOD_LIST = QStringList()
<< GET_CD_SUPPORTED_METERS << INITIATE_CONNECT_DISCONNECT << IS_CD_SUPPORTED << SET_CD_DEVICES_DISABLED << SET_CD_DEVICES_ENABLED;

static QStringList MDM_METHOD_LIST = QStringList()
<< INITIATE_BILLING_DETERMINANTS;

static QStringList MR_METHOD_LIST = QStringList()
<< GET_LATEST_METER_READINGS << GET_METER_READINGS_BY_BILLINGCYCLE << GET_END_DEVICE_EVENTS_BY_METERIDS;

static QStringList PG_METHOD_LIST = QStringList()
<< CHANGE_PAYMENT_TRANSACTIONS << CHANGE_RECURRING_PAYMENT_CONFIGURATION << PROCESS_PAYMENT_TRANSACTIONS;

static QStringList OD_METHOD_LIST = QStringList()
<< GET_METER_IDS_BY_END_DEVICE_STATE_TYPES << INITIATE_END_DEVICE_PINGS;

#endif // RULECONST_H

