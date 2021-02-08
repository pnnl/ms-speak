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
// Summary: WebServiceInfo.cpp
//-------------------------------------------------------------------------------

#include <QDebug>
#include <QSettings>

#include "WebServiceInfo.h"
#include "WsdlFile.h"

const QString WS_AM_NAME_LONG = "Asset Management";
const QString WS_ASM_NAME_LONG = "Assembly Management";
const QString WS_AVL_NAME_LONG = "Vehicle Location";
const QString WS_CB_NAME_LONG = "Customer Billing";
const QString WS_CD_NAME_LONG = "Connect / Disconnect";
const QString WS_CH_NAME_LONG = "Call Handling";
const QString WS_CP_NAME_LONG = "Commissioning & Provisioning";
const QString WS_DA_NAME_LONG = "Distribution Automation";
const QString WS_DER_NAME_LONG = "Distributed Energy Resources";
const QString WS_DGN_NAME_LONG = "Field Design";
const QString WS_DM_NAME_LONG = "Demand Management";
const QString WS_DR_NAME_LONG = "Demand Response";
const QString WS_EA_NAME_LONG = "Engineering Analysis (DMS)";
const QString WS_EDTR_NAME_LONG = "End Device Testing & Receiving";
const QString WS_FA_NAME_LONG = "Finance & Accounting";
const QString WS_GIS_NAME_LONG = "Geographic Information System";
const QString WS_INV_NAME_LONG = "Inventory Management";
const QString WS_LOC_NAME_LONG = "Underground Facility Locations";
const QString WS_MDM_NAME_LONG = "Meter Data Management";
const QString WS_MM_NAME_LONG = "Message Management";
const QString WS_MOD_NAME_LONG = "Power System Model Management";
const QString WS_MR_NAME_LONG = "Meter Reading";
const QString WS_OA_NAME_LONG = "Outage Analysis";
const QString WS_OD_NAME_LONG = "Outage Detection";
const QString WS_PAN_NAME_LONG = "PAN Communications";
const QString WS_PG_NAME_LONG = "Payment Gateway";
const QString WS_PP_NAME_LONG = "Payment Processing";
const QString WS_PPM_NAME_LONG = "Prepaid Metering";
const QString WS_RM_NAME_LONG = "Resource Management";
const QString WS_SA_NAME_LONG = "Scheduling & Assignment";
const QString WS_SCADA_NAME_LONG = "Supervisory Control & Data Acquisition";
const QString WS_SWO_NAME_LONG = "Switching Orders";
const QString WS_WEA_NAME_LONG = "Weather";
const QString WS_WG_NAME_LONG = "Work Generator";
const QString WS_WO_NAME_LONG = "Work Owner";
const QString WS_WP_NAME_LONG = "Work Performer";
const QString WS_WR_NAME_LONG = "Work Requester";
const QString WS_WV_NAME_LONG = "Work Viewer";

//------------------------------------------------------------------------------
// WebServiceInfo
//
WebServiceInfo::WebServiceInfo(QObject *parent)
  : QObject(parent)
{
  InitServiceNameHash();
  InitServiceGroupHash();
}
//------------------------------------------------------------------------------
// ~WebServiceInfo
//
WebServiceInfo::~WebServiceInfo()
{
  //qDeleteAll(m_methodTemplates);
  qDeleteAll(m_serviceGroups);
  qDeleteAll(m_wsdlFiles);
}
//------------------------------------------------------------------------------
// SaveWsdlMethodTemplate
//
void WebServiceInfo::SaveWsdlMethodTemplate(const QString& hostName, const QString& methodName, const QDomDocument& doc)
{
  QString fileName = WsdlMethodTemplateFileName(hostName, methodName);

  QFile file(fileName);

  if (!file.open(QIODevice::WriteOnly))
  {
    qDebug() << file.error() << file.errorString();
    return;
  }

  QByteArray bytes = doc.toByteArray(2);
  file.write(bytes);
  if (file.error() != QFileDevice::NoError)
    qDebug() << "ERROR:" << file.error() << file.errorString();
  file.close();
}
//------------------------------------------------------------------------------
// SetWsdlFile
//
void WebServiceInfo::SetWsdlFile(const QString& hostName, const QString& fileName)
{
  if (m_wsdlFiles.contains(hostName))
    delete m_wsdlFiles.take(hostName);

  if (!m_wsdlFiles.contains(hostName))
  {
    QString sk = WsdlFileNameKey(hostName); // Get the QSettings key based on the shortName
    WsdlFile* wsdlFile = new WsdlFile(hostName, fileName);
    connect(wsdlFile, SIGNAL(WsdlFileChanged(const QString&)), this, SIGNAL(WsdlFileChanged(const QString&)));
    m_wsdlFiles.insert(hostName, wsdlFile);
    QSettings().setValue(sk, fileName);
  }
  emit WsdlFileChanged(hostName);
}
//------------------------------------------------------------------------------
// ShortNames
//
QStringList WebServiceInfo::ShortNames()
{
  return QStringList()
    //<< WS_AM_NAME_SHORT
    //<< WS_ASM_NAME_SHORT
    //<< WS_AVL_NAME_SHORT
    << WS_CB_NAME_SHORT
    //<< WS_CD_NAME_SHORT
    //<< WS_CH_NAME_SHORT
    //<< WS_CP_NAME_SHORT
    //<< WS_DA_NAME_SHORT
    //<< WS_DER_NAME_SHORT
    //<< WS_DGN_NAME_SHORT
    //<< WS_DM_NAME_SHORT
    //<< WS_DR_NAME_SHORT
    //<< WS_EA_NAME_SHORT
    //<< WS_EDTR_NAME_SHORT
    //<< WS_FA_NAME_SHORT
    //<< WS_GIS_NAME_SHORT
    //<< WS_INV_NAME_SHORT
    //<< WS_LOC_NAME_SHORT
    << WS_MDM_NAME_SHORT
    //<< WS_MM_NAME_SHORT
    //<< WS_MOD_NAME_SHORT
    << WS_MR_NAME_SHORT
    << WS_OA_NAME_SHORT
    << WS_OD_NAME_SHORT
    //<< WS_PAN_NAME_SHORT
    //<< WS_PG_NAME_SHORT
    //<< WS_PP_NAME_SHORT
    //<< WS_PPM_NAME_SHORT
    //<< WS_RM_NAME_SHORT
    //<< WS_SA_NAME_SHORT
    //<< WS_SCADA_NAME_SHORT
    //<< WS_SWO_NAME_SHORT
    //<< WS_WEA_NAME_SHORT
    //<< WS_WG_NAME_SHORT
    //<< WS_WO_NAME_SHORT
    //<< WS_WP_NAME_SHORT
    //<< WS_WR_NAME_SHORT
    //<< WS_WV_NAME_SHORT
    ;
}
//------------------------------------------------------------------------------
// Wsdl
//
WsdlFile* WebServiceInfo::Wsdl(const QString& hostName)
{
  if (!m_wsdlFiles.contains(hostName))
  {
    QString sk = WsdlFileNameKey(hostName); // Get the QSettings key based on the shortName
    QString fileName = QSettings().value(sk, QString()).toString();
    WsdlFile* wsdlFile = new WsdlFile(hostName, fileName);
    connect(wsdlFile, SIGNAL(WsdlFileChanged(const QString&)), this, SIGNAL(WsdlFileChanged(const QString&)));
    m_wsdlFiles.insert(hostName, wsdlFile);
  }
  return m_wsdlFiles.value(hostName);
}
//------------------------------------------------------------------------------
// WsdlMethodTemplate
//
QDomDocument WebServiceInfo::WsdlMethodTemplate(const QString& hostName, const QString& methodName)
{
  WsdlFile* wsdlFile = Wsdl(hostName);
  return wsdlFile->MethodTemplate(methodName);
  Q_ASSERT(false);
  qDebug() << "ERROR: Method Template" << methodName << "For" << hostName << "Not Found";
  return QDomDocument("xml");
}
//------------------------------------------------------------------------------
// InitServiceGroupHash
//
void WebServiceInfo::InitServiceGroupHash()
{
  QStringList list;

  list << WS_CB_NAME_SHORT << WS_CP_NAME_SHORT << WS_MDM_NAME_SHORT << WS_PG_NAME_SHORT << WS_PP_NAME_SHORT << WS_PPM_NAME_SHORT;
  m_serviceGroups.insert(WS_GROUP_CBPM, new QStringList(list));

  list.clear();
  list << WS_AM_NAME_SHORT << WS_DGN_NAME_SHORT << WS_EA_NAME_SHORT << WS_GIS_NAME_SHORT << WS_LOC_NAME_SHORT << WS_MOD_NAME_SHORT;
  m_serviceGroups.insert(WS_GROUP_DEPC, new QStringList(list));

  list.clear();
  list << WS_DER_NAME_SHORT << WS_DM_NAME_SHORT << WS_DR_NAME_SHORT << WS_MM_NAME_SHORT << WS_PAN_NAME_SHORT;
  m_serviceGroups.insert(WS_GROUP_DR, new QStringList(list));

  list.clear();
  list << WS_CD_NAME_SHORT << WS_MR_NAME_SHORT;
  m_serviceGroups.insert(WS_GROUP_MSM, new QStringList(list));

  list.clear();
  list << WS_AVL_NAME_SHORT << WS_CH_NAME_SHORT << WS_DA_NAME_SHORT << WS_OD_NAME_SHORT << WS_OA_NAME_SHORT << WS_SCADA_NAME_SHORT << WS_SWO_NAME_SHORT << WS_WEA_NAME_SHORT;
  m_serviceGroups.insert(WS_GROUP_OMDO, new QStringList(list));

  list.clear();
  list << WS_RM_NAME_SHORT << WS_SA_NAME_SHORT << WS_WG_NAME_SHORT << WS_WO_NAME_SHORT << WS_WP_NAME_SHORT << WS_WR_NAME_SHORT << WS_WV_NAME_SHORT;
  m_serviceGroups.insert(WS_GROUP_WM, new QStringList(list));

  list.clear();
  list << WS_ASM_NAME_SHORT << WS_EDTR_NAME_SHORT << WS_FA_NAME_SHORT << WS_INV_NAME_SHORT;
  m_serviceGroups.insert(WS_GROUP_WOAI, new QStringList(list));
}
//------------------------------------------------------------------------------
// InitServiceNameHash
//
void WebServiceInfo::InitServiceNameHash()
{
  m_serviceNames.insert(WS_AM_NAME_SHORT, WS_AM_NAME_LONG);
  m_serviceNames.insert(WS_ASM_NAME_SHORT, WS_ASM_NAME_LONG);
  m_serviceNames.insert(WS_AVL_NAME_SHORT, WS_AVL_NAME_LONG);
  m_serviceNames.insert(WS_CB_NAME_SHORT, WS_CB_NAME_LONG);
  m_serviceNames.insert(WS_CD_NAME_SHORT, WS_CD_NAME_LONG);
  m_serviceNames.insert(WS_CH_NAME_SHORT, WS_CH_NAME_LONG);
  m_serviceNames.insert(WS_CP_NAME_SHORT, WS_CP_NAME_LONG);
  m_serviceNames.insert(WS_DA_NAME_SHORT, WS_DA_NAME_LONG);
  m_serviceNames.insert(WS_DER_NAME_SHORT, WS_DER_NAME_LONG);
  m_serviceNames.insert(WS_DGN_NAME_SHORT, WS_DGN_NAME_LONG);
  m_serviceNames.insert(WS_DM_NAME_SHORT, WS_DM_NAME_LONG);
  m_serviceNames.insert(WS_DR_NAME_SHORT, WS_DR_NAME_LONG);
  m_serviceNames.insert(WS_EA_NAME_SHORT, WS_EA_NAME_LONG);
  m_serviceNames.insert(WS_EDTR_NAME_SHORT, WS_EDTR_NAME_LONG);
  m_serviceNames.insert(WS_FA_NAME_SHORT, WS_FA_NAME_LONG);
  m_serviceNames.insert(WS_GIS_NAME_SHORT, WS_GIS_NAME_LONG);
  m_serviceNames.insert(WS_INV_NAME_SHORT, WS_INV_NAME_LONG);
  m_serviceNames.insert(WS_LOC_NAME_SHORT, WS_LOC_NAME_LONG);
  m_serviceNames.insert(WS_MDM_NAME_SHORT, WS_MDM_NAME_LONG);
  m_serviceNames.insert(WS_MM_NAME_SHORT, WS_MM_NAME_LONG);
  m_serviceNames.insert(WS_MOD_NAME_SHORT, WS_MOD_NAME_LONG);
  m_serviceNames.insert(WS_MR_NAME_SHORT, WS_MR_NAME_LONG);
  m_serviceNames.insert(WS_OA_NAME_SHORT, WS_OA_NAME_LONG);
  m_serviceNames.insert(WS_OD_NAME_SHORT, WS_OD_NAME_LONG);
  m_serviceNames.insert(WS_PAN_NAME_SHORT, WS_PAN_NAME_LONG);
  m_serviceNames.insert(WS_PG_NAME_SHORT, WS_PG_NAME_LONG);
  m_serviceNames.insert(WS_PP_NAME_SHORT, WS_PP_NAME_LONG);
  m_serviceNames.insert(WS_PPM_NAME_SHORT, WS_PPM_NAME_LONG);
  m_serviceNames.insert(WS_RM_NAME_SHORT, WS_RM_NAME_LONG);
  m_serviceNames.insert(WS_SA_NAME_SHORT, WS_SA_NAME_LONG);
  m_serviceNames.insert(WS_SCADA_NAME_SHORT, WS_SCADA_NAME_LONG);
  m_serviceNames.insert(WS_SWO_NAME_SHORT, WS_SWO_NAME_LONG);
  m_serviceNames.insert(WS_WEA_NAME_SHORT, WS_WEA_NAME_LONG);
  m_serviceNames.insert(WS_WG_NAME_SHORT, WS_WG_NAME_LONG);
  m_serviceNames.insert(WS_WO_NAME_SHORT, WS_WO_NAME_LONG);
  m_serviceNames.insert(WS_WP_NAME_SHORT, WS_WP_NAME_LONG);
  m_serviceNames.insert(WS_WR_NAME_SHORT, WS_WR_NAME_LONG);
  m_serviceNames.insert(WS_WV_NAME_SHORT, WS_WV_NAME_LONG);
}
