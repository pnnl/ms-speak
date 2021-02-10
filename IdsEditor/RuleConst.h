/*-------------------------------------------------------------------------------

  Multi-Speak - Secure Protocol Enterprise Access Kit(MS_SPEAK)
  Copyright © 2021, Battelle Memorial Institute
  All rights reserved.
  1.	Battelle Memorial Institute (hereinafter Battelle) hereby grants permission to any person or
        entity lawfully obtaining a copy of this software and associated documentation files
        (hereinafter “the Software”) to redistribute and use the Software in source and binary forms,
        with or without modification.  Such person or entity may use, copy, modify, merge, publish,
        distribute, sublicense, and/or sell copies of the Software, and may permit others to do so,
        subject to the following conditions:
        •	Redistributions of source code must retain the above copyright notice, this list of
            conditions and the following disclaimers.
        •	Redistributions in binary form must reproduce the above copyright notice, this list of
            conditions and the following disclaimer in the documentation and/or other materials
            provided with the distribution.
        •	Other than as used herein, neither the name Battelle Memorial Institute or Battelle may
            be used in any form whatsoever without the express written consent of Battelle.

  2.	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
        OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
        AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL BATTELLE OR CONTRIBUTORS
        BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
        (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
        OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
        CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
        OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


  This material was prepared as an account of work sponsored by an agency of the United States Government.
  Neither the United States  Government nor the United States Department of Energy, nor Battelle, nor
  any of their employees, nor any jurisdiction or organization  that has cooperated in the development
  of these materials, makes any warranty, express or implied, or assumes any legal liability or
  responsibility for the accuracy, completeness, or usefulness or any information, apparatus, product,
  software, or process disclosed, or represents that its use would not infringe privately owned rights.
  Reference herein to any specific commercial product, process, or service by trade name, trademark,
  manufacturer, or otherwise does not necessarily constitute or imply its endorsement, recommendation, or
  favoring by the United States Government or any agency thereof, or Battelle Memorial Institute. The
  views and opinions of authors expressed herein do not necessarily state or reflect those of the
  United States Government or any agency thereof.
                                     PACIFIC NORTHWEST NATIONAL LABORATORY
                                                operated by
                                                  BATTELLE
                                                  for the
                                      UNITED STATES DEPARTMENT OF ENERGY
                                       under Contract DE-AC05-76RL01830


    This notice including this sentence must appear on any copies of this computer software.
*/
//-------------------------------------------------------------------------------
//	History
//		2021 - Modified By: Carl Miller <carl.miller@pnnl.gov> from original by
//                  Lance Irvine, LMI Developments, LLC.
//-------------------------------------------------------------------------------
//
// Summary: RuleConst.h
//-------------------------------------------------------------------------------

#ifndef RULECONST_H
#define RULECONST_H

#include <QHash>
#include <QString>
#include <QStringList>

// Version
const QString SOFTWARE_VERSION = QStringLiteral("21.02.07");
const QString SOFTWARE_ABOUT = QString("<center><h2>MS-SPEAK IDS</h2><h3>Business Rule Editor</h3><h4>Copyright 2021</h4><h4>Pacific Northwest National Laboratory</h4><h5>All Rights Reserved.</h5><h3>Version " + SOFTWARE_VERSION + "</h3></center");

// Log Consts
//const QString SETTINGS_GROUP = QStringLiteral("[Settings]");
//const QString SETTINGS_LOG_FILE = QStringLiteral("LogFile");

// Rule Types
const QString RULE_TYPE_MAX_VALUE = QStringLiteral("MaxValue");
const QString RULE_TYPE_TEMP_RANGE = QStringLiteral("TempRange");
const QString RULE_TYPE_TIME_RANGE = QStringLiteral("TimeRange");

// Rule Keys
const QString RULE_KEY_MAXTEMP = QStringLiteral("maxTemp");
const QString RULE_KEY_MAXTIME = QStringLiteral("maxHour");
const QString RULE_KEY_MINTEMP = QStringLiteral("minTemp");
const QString RULE_KEY_MINTIME = QStringLiteral("minHour");
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

