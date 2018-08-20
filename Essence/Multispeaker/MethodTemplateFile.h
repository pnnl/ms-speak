////-------------------------------------------------------------------------------
//// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
//// Operated by Battelle for the U.S. Department of Energy
////
////  Created By: Lance Irvine
////
////  Summary: MethodTemplateFile
////
//
//#ifndef METHODTEMPLATEFILE_H
//#define METHODTEMPLATEFILE_H
//
//#include <QFileInfo>
//#include <QJsonDocument>
//#include <QObject>
//
//#include "KeyValueList.h"
//#include "Settings.h"
//
//class MethodTemplateFile : public QObject
//{
//  Q_OBJECT
//private:
//  QString m_jsonFileName;
//  QJsonDocument m_jsonDoc;
//
//public:
//  MethodTemplateFile(const QString& hostName, const QString& methodName, QObject* parent=0);
//  ~MethodTemplateFile();
//
//  QString FileName() const {return m_jsonFileName;}
//
//  bool IsEnabled(const QString& http, const QString& type, const QString& key) const;
//  QStringList Keys(const QString& http, const QString& type) const;
//  QStringList KeysEnabled(const QString& http, const QString& type) const;
//  QString Value(const QString& http, const QString& type, const QString& key) const;
//
//private:
//  void CreateJsonDoc();
//  void ReadJson();
//  void WriteJson();
//};
//
//#endif // METHODTEMPLATEFILE_H
