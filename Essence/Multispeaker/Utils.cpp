//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: Utils
//
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
// CreatRootHomePath
//
void Utils::CreatRootHomePath()
{
  // .Speaker
  QDir dir(ROOT_HOME_PATH);
  if (!dir.exists())
  {
    if (!dir.mkdir(ROOT_HOME_PATH))
      qDebug() << "Can not create directory structure for " << ROOT_HOME_PATH;
  }
}
