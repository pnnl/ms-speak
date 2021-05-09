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
//		2021 - Carl Miller <carl.miller@pnnl.gov>
//-------------------------------------------------------------------------------
// Summary: DbConst.h
//				Database table definitions.
//-------------------------------------------------------------------------------

#ifndef DBCONST_H
#define DBCONST_H

#include <QHash>
#include <QString>
#include <QStringList>

// Functions
const QString METERING_MANAGEMENT = QStringLiteral("Metering Management");
const QString WORK_MANAGEMENT = QStringLiteral("Work Management");
const QString WORK_ORDER = QStringLiteral("Work Order");
const QString CUSTOMER_BILLING = QStringLiteral("Customer Billing");
const QString DISTRIBUTION_ENGINEERING = QStringLiteral("Distribution Engineering");
const QString DEMAND_RESPONSE = QStringLiteral("Demand Response");
const QString DISTRIBUTION_OPERATIONS = QStringLiteral("Distribution Operations");

// EndPoints
//  Metering and Service Management Functional Endpoints
const QString CD_SERVER = QStringLiteral("CD_Server");
const QString MR_SERVER = QStringLiteral("MR_Server");

//  Work Management Functional Endpoints
const QString WR_SERVER = QStringLiteral("WR_Server");
const QString WO_SERVER = QStringLiteral("WO_Server");
const QString WG_SERVER = QStringLiteral("WG_Server");
const QString SA_SERVER = QStringLiteral("SA_Server");
const QString RM_SERVER = QStringLiteral("RM_Server");
const QString WP_SERVER = QStringLiteral("WP_Server");
const QString WV_SERVER = QStringLiteral("WV_Server");

//  Work Order Accounting and Inventory Functional Endpoints
const QString ASM_SERVER = QStringLiteral("ASM_Server");
const QString FA_SERVER = QStringLiteral("FA_Server");
const QString INV_SERVER = QStringLiteral("INV_Server");
const QString EDTR_SERVER = QStringLiteral("EDTR_Server");

//  Customer Billing and PAN Management Functional Endpoints
const QString CB_SERVER = QStringLiteral("CB_Server");
const QString PPM_SERVER = QStringLiteral("PPM_Server");
const QString CP_SERVER = QStringLiteral("CP_Server");
const QString MDM_SERVER = QStringLiteral("MDM_Server");
const QString PP_SERVER = QStringLiteral("PP_Server");
const QString PG_SERVER = QStringLiteral("PG_Server");

//  Distribution Engineering and GIS Abstract Functional Endpoints
const QString AM_SERVER = QStringLiteral("AM_Server");
const QString DGN_SERVER = QStringLiteral("DGN_Server");
const QString EA_SERVER = QStringLiteral("EA_Server");
const QString MOD_SERVER = QStringLiteral("MOD_Server");
const QString GIS_SERVER = QStringLiteral("GIS_Server");
const QString LOC_SERVER = QStringLiteral("LOC_Server");

//  Demand Response Functional Endpoints
const QString DM_SERVER = QStringLiteral("DM_Server");
const QString DR_SERVER = QStringLiteral("DR_Server");
const QString MM_SERVER = QStringLiteral("MM_Server");
const QString PAN_SERVER = QStringLiteral("PAN_Server");
const QString DER_SERVER = QStringLiteral("DER_Server");

//  Distribution Operations Functional Endpoints
const QString CH_SERVER = QStringLiteral("CH_Server");
const QString OD_SERVER = QStringLiteral("OD_Server");
const QString OA_SERVER = QStringLiteral("OA_Server");
const QString DA_SERVER = QStringLiteral("DA_Server");
const QString SCADA_SERVER = QStringLiteral("SCADA_Server");
const QString SWO_SERVER = QStringLiteral("SWO_Server");
const QString LT_SERVER = QStringLiteral("LT_Server");
const QString WEA_SERVER = QStringLiteral("WEA_Server");

// Common Methods
const QString GETMETHODS = QStringLiteral("GetMethods");
const QString PINGURL = QStringLiteral("PingURL");

//  Metering and Service Management Methods
//     Connect/Disconnect Endpoint -verified
const QString GET_CD_SUPPORTED_METERS = QStringLiteral("GetCDSupportedMeters");
const QString INITIATE_CONNECT_DISCONNECT = QStringLiteral("InitiateConnectDisconnect");
const QString IS_CD_SUPPORTED = QStringLiteral("IsCDSupported");
const QString SET_CD_DEVICES_DISABLED = QStringLiteral("SetCDDevicesDisabled");
const QString SET_CD_DEVICES_ENABLED = QStringLiteral("SetCDDevicesEnabled");
//     Meter Reading Endpoint -verified
const QString GET_LATEST_METER_READINGS = QStringLiteral("GetLatestMeterReadings");
const QString GET_METER_READINGS_BY_BILLINGCYCLE = QStringLiteral("GetMeterReadingsByBillingCycle");
const QString GET_END_DEVICE_EVENTS_BY_METERIDS = QStringLiteral("GetEndDeviceEventsByMeterIDs");

//  Customer Billing and PAN Management Methods
//     Customer Billing Endpoint -verified
const QString CHANGE_CUSTOMER_DATA = QStringLiteral("ChangeCustomerData");
const QString CHANGE_METER_DATA = QStringLiteral("ChangeMeterData");
const QString CHANGE_STREET_LIGHT_DATA = QStringLiteral("ChangeStreetLightData");
//     Meter Data Management Endpoint
const QString INITIATE_BILLING_DETERMINANTS = QStringLiteral("InitiateBillingDeterminants");
//     Payment Gateway Endpoints
const QString CHANGE_PAYMENT_TRANSACTIONS = QStringLiteral("ChangePaymentTransactions");
const QString CHANGE_RECURRING_PAYMENT_CONFIGURATION = QStringLiteral("ChangeRecurringPaymentConfiguration");
const QString PROCESS_PAYMENT_TRANSACTIONS = QStringLiteral("ProcessPaymentTransactions");

//  Distribution Operations Methods
//     Outage Detection Endpoint
// the closest in the V3 OD WSDL is OutageEventChangedNotification
//const QString OD_EVENT_NOTIFICATION = QStringLiteral("ODEventNotification");
const QString OD_EVENT_NOTIFICATION = QStringLiteral("OutageEventChangedNotification");
const QString GET_METER_IDS_BY_END_DEVICE_STATE_TYPES = QStringLiteral("GetMeterIDsByEndDeviceStateTypes");
const QString INITIATE_END_DEVICE_PINGS = QStringLiteral("InitiateEndDevicePings");
//     Outage Analysis Endpoint
// this is in the V3 OA WSDL
const QString OA_EVENT_NOTIFICATION = QStringLiteral("ODEventNotification");

// assign function endpoints
//    Metering and Service Management Functional Endpoints
static QStringList METERING_MANAGEMENT_ENDPOINT_LIST = QStringList()
<< CD_SERVER << MR_SERVER;

//    Work Management Functional Endpoints
static QStringList WORK_MANAGEMENT_ENDPOINT_LIST = QStringList()
<< WR_SERVER << WO_SERVER << WG_SERVER << SA_SERVER << RM_SERVER << WP_SERVER << WV_SERVER;

//    Work Order Accounting and Inventory Functional Endpoints
static QStringList WORK_ORDER_ENDPOINT_LIST = QStringList()
<< ASM_SERVER << FA_SERVER << INV_SERVER << EDTR_SERVER;

//    Customer Billing and PAN Management Functional Endpoints
static QStringList CUSTOMER_BILLING_ENDPOINT_LIST = QStringList()
<< CB_SERVER << PPM_SERVER << CP_SERVER << MDM_SERVER << PP_SERVER << PG_SERVER;

//    Distribution Engineering and GIS Abstract Functional Endpoints
static QStringList DISTRIBUTION_ENGINEERING_ENDPOINT_LIST = QStringList()
<< AM_SERVER << DGN_SERVER << EA_SERVER << MOD_SERVER << GIS_SERVER << LOC_SERVER;

//    Demand Response and GIS Abstract Functional Endpoints
static QStringList DEMAND_RESPONSE_ENDPOINT_LIST = QStringList()
<< DM_SERVER << DR_SERVER << MM_SERVER << PAN_SERVER << DER_SERVER;

//    Distribution Operations Functional Endpoints
static QStringList DISTRIBUTION_OPERATIONS_ENDPOINT_LIST = QStringList()
<< CH_SERVER << OD_SERVER << OA_SERVER << DA_SERVER << SCADA_SERVER
<< SWO_SERVER << LT_SERVER << WEA_SERVER;

// will give all the functions the Common Methods
static QStringList FUNCTION_LIST = QStringList()
		<< METERING_MANAGEMENT << WORK_MANAGEMENT << WORK_ORDER
		<< CUSTOMER_BILLING << DISTRIBUTION_ENGINEERING << DEMAND_RESPONSE
		<< DISTRIBUTION_OPERATIONS;

static QHash<QString, QStringList> ENDPOINT_LIST {
	{METERING_MANAGEMENT, METERING_MANAGEMENT_ENDPOINT_LIST},
	{WORK_MANAGEMENT, WORK_MANAGEMENT_ENDPOINT_LIST},
	{WORK_ORDER, WORK_ORDER_ENDPOINT_LIST},
	{CUSTOMER_BILLING, CUSTOMER_BILLING_ENDPOINT_LIST},
	{DISTRIBUTION_ENGINEERING, DISTRIBUTION_ENGINEERING_ENDPOINT_LIST},
	{DEMAND_RESPONSE, DEMAND_RESPONSE_ENDPOINT_LIST},
	{DISTRIBUTION_OPERATIONS, DISTRIBUTION_OPERATIONS_ENDPOINT_LIST}
	};

// will give these specific endpoints these specific Methods
//  Metering and Service Management Methods
//     Connect/Disconnect Endpoint
static QStringList CD_METHOD_LIST = QStringList()
<< GET_CD_SUPPORTED_METERS << INITIATE_CONNECT_DISCONNECT << IS_CD_SUPPORTED << SET_CD_DEVICES_DISABLED << SET_CD_DEVICES_ENABLED;
//     Meter reading Endpoint
static QStringList MR_METHOD_LIST = QStringList()
<< GET_LATEST_METER_READINGS << GET_METER_READINGS_BY_BILLINGCYCLE << GET_END_DEVICE_EVENTS_BY_METERIDS;

//  Customer Billing and PAN Management Functional Endpoints
//     Customer Billing Endpoint
static QStringList CB_METHOD_LIST = QStringList()
<< CHANGE_CUSTOMER_DATA << CHANGE_METER_DATA << CHANGE_STREET_LIGHT_DATA;
//     Meter Data Management Endpoint
static QStringList MDM_METHOD_LIST = QStringList()
<< INITIATE_BILLING_DETERMINANTS;
//     Payment Gateway Endpoints
static QStringList PG_METHOD_LIST = QStringList()
<< CHANGE_PAYMENT_TRANSACTIONS << CHANGE_RECURRING_PAYMENT_CONFIGURATION << PROCESS_PAYMENT_TRANSACTIONS;

//  Distribution Operations Methods
//     Outage Detection Endpoint
static QStringList OD_METHOD_LIST = QStringList()
<< OD_EVENT_NOTIFICATION << GET_METER_IDS_BY_END_DEVICE_STATE_TYPES << INITIATE_END_DEVICE_PINGS;
//     Outage Analysis Endpoint
static QStringList OA_METHOD_LIST = QStringList()
<< OA_EVENT_NOTIFICATION;

static QHash<QString, QStringList> METHOD_LIST {
	{CD_SERVER, CD_METHOD_LIST},
	{MR_SERVER, MR_METHOD_LIST},
	{CB_SERVER, CB_METHOD_LIST},
	{MDM_SERVER, MDM_METHOD_LIST},
	{PG_SERVER, PG_METHOD_LIST},
	{OD_SERVER, OD_METHOD_LIST},
	{OA_SERVER, OA_METHOD_LIST}
	};
#endif // DBCONST_H

