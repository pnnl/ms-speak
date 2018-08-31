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
// Summary: Utils.cpp
//-------------------------------------------------------------------------------

//#include <QTextStream>
//
//foreach(QString x, strings)
//    QTextStream(stdout) << x << endl;

#include <QComboBox>
#include <QDir>
#include <QFile>
#include <QHostAddress>
#include <QHostInfo>
#include <QNetworkInterface>
#include <QSettings>

#include "Settings.h"
#include "Utils.h"

//------------------------------------------------------------------------------
// Utils
//
Utils::Utils(QObject *parent)
  : QObject(parent)
{
}
//------------------------------------------------------------------------------
// ~Utils
//
Utils::~Utils()
{
}
//------------------------------------------------------------------------------
// DebugByteArrayToString
//
QString Utils::DebugByteArrayToString(const QByteArray& data)
{
  QStringList list;
  for (int i = 0; i < data.size(); i++)
  {
    list << QString::number((quint8)data.at(i), 16);
  }
  return list.join(" ");
}
//------------------------------------------------------------------------------
// InitHostCombo
//
void Utils::InitHostCombo(QComboBox* combo)
{
  if (!combo)
    combo = new QComboBox;
  combo->setEditable(true);
  // find out name of this machine
  QString name = QHostInfo::localHostName();
  if (!name.isEmpty()) {
      combo->addItem(name);
      QString domain = QHostInfo::localDomainName();
      if (!domain.isEmpty())
          combo->addItem(name + QChar('.') + domain);
  }
  if (name != QStringLiteral("localhost"))
      combo->addItem(QStringLiteral("localhost"));

  // Find out IP addresses of this machine
  QList<QHostAddress> ipAddressesList = QNetworkInterface::allAddresses();

  // Add non-localhost addresses
  for (int i = 0; i < ipAddressesList.size(); ++i) 
  {
    if (!ipAddressesList.at(i).isLoopback())
      combo->addItem(ipAddressesList.at(i).toString());
  }
  // Add localhost addresses
  for (int i = 0; i < ipAddressesList.size(); ++i) 
  {
    if (ipAddressesList.at(i).isLoopback())
      combo->addItem(ipAddressesList.at(i).toString());
  }

  //int row = 0;
  //combo->addItem(QHostAddress(QHostAddress::LocalHost).toString());
  //combo->setItemData(row++, "The IPv4 localhost address. Equivalent to 127.0.0.1", Qt::ToolTipRole);
  //combo->addItem(QHostAddress(QHostAddress::LocalHostIPv6).toString());
  //combo->setItemData(row++, "The IPv6 localhost address. Equivalent to ::1", Qt::ToolTipRole);
  //combo->addItem(QHostAddress(QHostAddress::Broadcast).toString());
  //combo->setItemData(row++, "The IPv4 broadcast address. Equivalent to 255.255.255.255", Qt::ToolTipRole);
  //combo->addItem(QHostAddress(QHostAddress::AnyIPv4).toString());
  //combo->setItemData(row++, "The IPv4 any-address. Equivalent to 0.0.0.0. A socket bound with this address will listen only on IPv4 interaces", Qt::ToolTipRole);
  //combo->addItem(QHostAddress(QHostAddress::AnyIPv6).toString());
  //combo->setItemData(row++, "The IPv6 any-address. Equivalent to ::. A socket bound with this address will listen only on IPv6 interaces.", Qt::ToolTipRole);
  //combo->addItem(QHostAddress(QHostAddress::Any).toString());
  //combo->setItemData(row++, "The dual stack any-address. A socket bound with this address will listen on both IPv4 and IPv6 interfaces", Qt::ToolTipRole);

  //combo->setEditText(QSettings().value(SK_HOST_ADDRESS, QHostAddress(QHostAddress::LocalHost).toString()).toString());
}
//------------------------------------------------------------------------------
// InitHostCombo
//
void Utils::InitHostCombo(QComboBox& combo, const QStringList recentAddresses)
{
  QStringList list;
  QList<QHostAddress> ipAddressesList = QNetworkInterface::allAddresses();
  foreach(const QHostAddress ip, ipAddressesList)
    list << ip.toString();

  combo.insertItems(0, list);

  // Add the recentAddresses if they exist
  if (recentAddresses.count())
  {
    for (int i = 0; i < recentAddresses.count(); ++i)
    {
      if (combo.findText(recentAddresses.at(i)) == -1)
        combo.insertItem(0, recentAddresses.at(i));
    }
  }

  // Select the first non-localhost ipv4 address
  QString ip;
  for (int i = 0; i < ipAddressesList.size(); ++i)
  {
    if (ipAddressesList.at(i) != QHostAddress::LocalHost && ipAddressesList.at(i).toIPv4Address())
    {
      ip = ipAddressesList.at(i).toString();
      break;
    }
  }
  int idx = combo.findText(ip);
  combo.setCurrentIndex(idx);
}
//------------------------------------------------------------------------------
// ParseShortName
//
QString Utils::ParseShortName(const QString& name)
{
  QStringList parts = name.split(" ");
  return parts.first();
}
//------------------------------------------------------------------------------
// ParseLongName
//
QString Utils::ParseLongName(const QString& name)
{
  QStringList parts = name.split(" ");
  parts.takeFirst();
  return parts.join(" ");
}
//------------------------------------------------------------------------------
// ProcessErrorToString
//
QString Utils::ProcessErrorToString(QProcess::ProcessError error)
{
  QString msg;
  switch (error)
  {
    case QProcess::FailedToStart: msg = "The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program."; break;
    case QProcess::Crashed: msg = "The process crashed some time after starting successfully."; break;
    case QProcess::Timedout: msg = "The last waitFor...() function timed out. The state of QProcess is unchanged, and you can try calling waitFor...() again."; break;
    case QProcess::WriteError: msg = "An error occurred when attempting to write to the process. For example, the process may not be running, or it may have closed its input channel."; break;
    case QProcess::ReadError: msg = "An error occurred when attempting to read from the process. For example, the process may not be running."; break;
    case QProcess::UnknownError: msg = "An unknown error occurred. This is the default return value of error()."; break;
  };
  return msg;
}
//------------------------------------------------------------------------------
// CreateRootHomePath
//
void Utils::CreateRootHomePath()
{
  // .Speaker
  QDir dir(ROOT_HOME_PATH);
  if (!dir.exists())
  {
    if (!dir.mkdir(ROOT_HOME_PATH))
      qDebug() << "Can not create directory structure for " << ROOT_HOME_PATH;
  }
}
