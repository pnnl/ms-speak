/*-------------------------------------------------------------------------------

  Multi-Speak - Secure Protocol Enterprise Access Kit(MS_SPEAK)
  Copyright © 2018, Battelle Memorial Institute
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
//		2017 - Created By: Lance Irvine.
//		2018 - Modified By: Carl Miller <carl.miller@pnnl.gov>
//-------------------------------------------------------------------------------
//
// Summary: WebServiceInfo.h
//-------------------------------------------------------------------------------

#ifndef WEBSERVICEINFO_H
#define WEBSERVICEINFO_H

#include <QApplication>
#include <QHash>
#include <QObject>
#include <QString>
#include <QStringList>

#include "Settings.h"

const QString WS_NAME_SPACE = "_Server";

const QString WS_AM_NAME_SHORT = "AM";
const QString WS_ASM_NAME_SHORT = "ASM";
const QString WS_AVL_NAME_SHORT = "AVL";
const QString WS_CB_NAME_SHORT = "CB";
const QString WS_CD_NAME_SHORT = "CD";
const QString WS_CH_NAME_SHORT = "CH";
const QString WS_CP_NAME_SHORT = "CP";
const QString WS_DA_NAME_SHORT = "DA";
const QString WS_DER_NAME_SHORT = "DER";
const QString WS_DGN_NAME_SHORT = "DGN";
const QString WS_DM_NAME_SHORT = "DM";
const QString WS_DR_NAME_SHORT = "DR";
const QString WS_EA_NAME_SHORT = "EA";
const QString WS_EDTR_NAME_SHORT = "EDTR";
const QString WS_FA_NAME_SHORT = "FA";
const QString WS_GIS_NAME_SHORT = "GIS";
const QString WS_INV_NAME_SHORT = "INV";
const QString WS_LOC_NAME_SHORT = "LOC";
const QString WS_MDM_NAME_SHORT = "MDM";
const QString WS_MM_NAME_SHORT = "MM";
const QString WS_MOD_NAME_SHORT = "MOD";
const QString WS_MR_NAME_SHORT = "MR";
const QString WS_OA_NAME_SHORT = "OA";
const QString WS_OD_NAME_SHORT = "OD";
const QString WS_PAN_NAME_SHORT = "PAN";
const QString WS_PG_NAME_SHORT = "PG";
const QString WS_PP_NAME_SHORT = "PP";
const QString WS_PPM_NAME_SHORT = "PPM";
const QString WS_RM_NAME_SHORT = "RM";
const QString WS_SA_NAME_SHORT = "SA";
const QString WS_SCADA_NAME_SHORT = "SCADA";
const QString WS_SWO_NAME_SHORT = "SWO";
const QString WS_WEA_NAME_SHORT = "WEA";
const QString WS_WG_NAME_SHORT = "WG";
const QString WS_WO_NAME_SHORT = "WO";
const QString WS_WP_NAME_SHORT = "WP";
const QString WS_WR_NAME_SHORT = "WR";
const QString WS_WV_NAME_SHORT = "WV";

const QString WS_GROUP_CBPM = "Customer Billing and PAN Management";
const QString WS_GROUP_DR = "Demand Response";
const QString WS_GROUP_DEPC = "Distribution Engineering, Planning & Construction";
const QString WS_GROUP_MSM = "Metering and Service Management";
const QString WS_GROUP_OMDO = "Outage Management & Distribution Operations";
const QString WS_GROUP_WM = "Work Management";
const QString WS_GROUP_WOAI = "Work Order Accounting and Inventory";

class QDomDocument;

class WsdlFile;

class WebServiceInfo : public QObject
{
  Q_OBJECT
private:
  QHash<QString, QString> m_serviceNames;
  QHash<QString, QStringList*> m_serviceGroups;
  QHash<QString, WsdlFile*> m_wsdlFiles; // Key is server shortName

public:
  WebServiceInfo(QObject* parent);
  ~WebServiceInfo();

  QString FullName(const QString& hostName) {return QString("%1 %2").arg(hostName, m_serviceNames.value(hostName));}
  QString FullNameDashSep(const QString& hostName) {return QString("%1 - %2").arg(hostName, m_serviceNames.value(hostName));}
  QString FullNameColonSep(const QString& hostName) {return QString("%1: %2").arg(hostName, m_serviceNames.value(hostName));}
  QStringList GroupShortNames(const QString& groupName) {return *(m_serviceGroups.value(groupName));}

  void SaveWsdlMethodTemplate(const QString& hostName, const QString& methodName, const QDomDocument& doc);
  void SetWsdlFile(const QString& hostName, const QString& fileName);

  QStringList ShortNames();
  WsdlFile* Wsdl(const QString& hostName);
  QString WsdlFileNameKey(const QString& hostName) {return QString("%1%2").arg(SK_WSDL_IMPORT_PREFIX, hostName);}
  QString WsdlMethodListJsonFileName(const QString& hostName) {return QString("%1/%2.json").arg(ROOT_HOME_PATH, hostName);}
  QDomDocument WsdlMethodTemplate(const QString& hostName, const QString& methodName);
  QString WsdlMethodTemplateFileName(const QString& hostName, const QString& methodName) {return QString("%1/%2_%3.xml").arg(ROOT_HOME_PATH, hostName, methodName);}

private:
  void InitServiceGroupHash();
  void InitServiceNameHash();

signals:
  void WsdlFileChanged(const QString& hostName);

private slots:
};

//-------------------------------------------------------------------------------
// WsInfo
//
inline WebServiceInfo& WsInfo() 
{
  // Static init will only be allocated once and dealloc when QApplication goes out of scope in main()
  static WebServiceInfo* static_web_service_info = new WebServiceInfo(qApp);
  return *static_web_service_info;
}

#endif // WEBSERVICEINFO_H
