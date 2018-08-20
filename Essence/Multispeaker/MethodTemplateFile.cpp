////-------------------------------------------------------------------------------
//// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
//// Operated by Battelle for the U.S. Department of Energy
////
////  Created By: Lance Irvine
////
////  Summary: MethodTemplateFile
////
//// JSON FORMAT
////{
////    "request": {
////        "headers": {
////            "Key0": {
////                "enabled": false,
////                "value": "Value0"
////            }
////        },
////        "params": {
////            "Key0": {
////                "enabled": false,
////                "value": "Value0"
////            }
////        }
////    },
////    "response": {
////        "headers": {
////            "Key0": {
////                "enabled": false,
////                "value": "Value0"
////            }
////        },
////        "params": {
////            "Key0": {
////                "enabled": false,
////                "value": "Value0"
////            }
////        }
////    }
////}
//
//#include <QDebug>
//#include <QFile>
//#include <QJsonArray>
//#include <QJsonDocument>
//#include <QJsonParseError>
//#include <QJsonObject>
//
//#include "MethodTemplateFile.h"
//#include "Settings.h"
//
////------------------------------------------------------------------------------
//// MethodTemplateFile
////
//MethodTemplateFile::MethodTemplateFile(const QString& hostName, const QString& methodName, QObject* parent)
//  : QObject(parent),
//  m_jsonFileName(QString("%1/%2_%3.json").arg(ROOT_HOME_PATH, hostName, methodName))
//{
//  if (QFileInfo(m_jsonFileName).exists())
//    ReadJson();
//  else
//    CreateJsonDoc();
//}
////------------------------------------------------------------------------------
//// ~MethodTemplateFile
////
//MethodTemplateFile::~MethodTemplateFile()
//{
//}
////------------------------------------------------------------------------------
//// IsEnabled
////
////  Example Usage: bool enabled = IsEnabled(JSON_REQUEST_TAG, JSON_HEADERS_TAG, "CancelDemandReset);
////
////  Inputs:
////    http: either JSON_REQUEST_TAG or JSON_RESPONSE_TAG
////    type: either JSON_HEADERS_TAG or JSON_PARAMS_TAG
////    key: the name of the key
////
//bool MethodTemplateFile::IsEnabled(const QString& http, const QString& type, const QString& key) const
//{
//  return m_jsonDoc.object().find(http).value().toObject().find(type).value().toObject().value(key).toObject().value(JSON_ENABLED_TAG).toBool();
//}
////------------------------------------------------------------------------------
//// Keys
////
////  Example Usage: QStringList list = Keys(JSON_REQUEST_TAG, JSON_HEADERS_TAG);
////
////  Inputs:
////    http: either JSON_REQUEST_TAG or JSON_RESPONSE_TAG
////    type: either JSON_HEADERS_TAG or JSON_PARAMS_TAG
////
//QStringList MethodTemplateFile::Keys(const QString& http, const QString& type) const
//{
//  QStringList list;
//  QJsonObject headers = m_jsonDoc.object().find(http).value().toObject().find(type).value().toObject();
//  for (QJsonObject::const_iterator it = headers.constBegin(); it != headers.constEnd(); ++it)
//    list << it.key();
//  return list;
//}
////------------------------------------------------------------------------------
//// KeysEnabled
////
////  Example Usage: QStringList list = KeysEnabled(REQUEST_TAG, HEADERS_TAG);
////
////  Inputs:
////    http: either JSON_REQUEST_TAG or JSON_RESPONSE_TAG
////    type: either JSON_HEADERS_TAG or JSON_PARAMS_TAG
////
//QStringList MethodTemplateFile::KeysEnabled(const QString& http, const QString& type) const
//{
//  QStringList list;
//  QJsonObject headers = m_jsonDoc.object().find(http).value().toObject().find(type).value().toObject();
//  for (QJsonObject::const_iterator it = headers.constBegin(); it != headers.constEnd(); ++it)
//    if (it.value().toObject().value(JSON_ENABLED_TAG).toBool())
//      list << it.key();
//  return list;
//}
////------------------------------------------------------------------------------
//// HeaderValue
////
////  Example Usage: QString value Keys(REQUEST_TAG, HEADERS_TAG, "CancelDemandReset");
////
////  Inputs:
////    http: either REQUEST_TAG or RESPONSE_TAG
////    type: either HEADERS_TAG or PARAMS_TAG
////    key: the name of the key
////
//QString MethodTemplateFile::Value(const QString& http, const QString& type, const QString& key) const
//{
//  return m_jsonDoc.object().find(http).value().toObject().find(type).value().toObject().value(key).toObject().value(JSON_VALUE_TAG).toString();
//}
////------------------------------------------------------------------------------
//// CreateJsonDoc
////
//void MethodTemplateFile::CreateJsonDoc()
//{
//  // Request
//  QJsonObject reqObj;
//  QJsonObject reqheaders;
//  for (int i = 0; i < 3; ++i)
//  {
//    QJsonValue onOff((i % 2) ? true : false);
//    QJsonValue value(QString("Value%1").arg(i));
//    QJsonObject subObj;
//    subObj.insert(JSON_ENABLED_TAG, onOff);
//    subObj.insert(JSON_VALUE_TAG, value);
//    reqheaders.insert(QString("Key%1").arg(i), subObj);
//  }
//  reqObj.insert(JSON_HEADERS_TAG, reqheaders);
//
//  QJsonObject reqParams;
//  for (int i = 0; i < 3; ++i)
//  {
//    QJsonValue onOff((i % 2) ? true : false);
//    QJsonValue value(QString("Value%1").arg(i));
//    QJsonObject subObj;
//    subObj.insert(JSON_ENABLED_TAG, onOff);
//    subObj.insert(JSON_VALUE_TAG, value);
//    reqParams.insert(QString("Key%1").arg(i), subObj);
//  }
//  reqObj.insert(JSON_PARAMS_TAG, reqParams);
//
//  // Response
//  QJsonObject resObj;
//  QJsonObject resheaders;
//  for (int i = 0; i < 3; ++i)
//  {
//    QJsonValue onOff((i % 2) ? true : false);
//    QJsonValue value(QString("Value%1").arg(i));
//    QJsonObject subObj;
//    subObj.insert(JSON_ENABLED_TAG, onOff);
//    subObj.insert(JSON_VALUE_TAG, value);
//    resheaders.insert(QString("Key%1").arg(i), subObj);
//  }
//  resObj.insert(JSON_HEADERS_TAG, resheaders);
//
//  QJsonObject resParams;
//  for (int i = 0; i < 3; ++i)
//  {
//    QJsonValue onOff((i % 2) ? true : false);
//    QJsonValue value(QString("Value%1").arg(i));
//    QJsonObject subObj;
//    subObj.insert(JSON_ENABLED_TAG, onOff);
//    subObj.insert(JSON_VALUE_TAG, value);
//    resParams.insert(QString("Key%1").arg(i), subObj);
//  }
//  resObj.insert(JSON_PARAMS_TAG, resParams);
//
//
//  QJsonObject obj;
//  obj.insert(JSON_REQUEST_TAG, reqObj);
//  obj.insert(JSON_RESPONSE_TAG, resObj);
//
//  m_jsonDoc.setObject(obj);
//  WriteJson(); 
//}
////------------------------------------------------------------------------------
//// ReadJson
////
//void MethodTemplateFile::ReadJson()
//{
//  QFile file(m_jsonFileName);
//  if (file.open(QIODevice::ReadOnly))
//  {
//    QByteArray data = file.readAll();
//    QJsonParseError err;
//    m_jsonDoc = QJsonDocument::fromJson(data, &err);
//    if (err.error != QJsonParseError::NoError)
//      qDebug() << err.errorString();
//  }
//}
////------------------------------------------------------------------------------
//// WriteJson
////
//void MethodTemplateFile::WriteJson()
//{
//  QFile file(m_jsonFileName);
//  if (file.open(QIODevice::WriteOnly))
//  {
//    if (qint64 bytes = file.write(m_jsonDoc.toJson(QJsonDocument::Indented)) == -1)
//      qDebug() <<  "Error" << QString("Error Writing Json File, %1").arg(file.fileName());
//  }
//}
//
