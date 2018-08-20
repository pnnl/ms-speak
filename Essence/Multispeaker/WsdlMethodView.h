//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: WsdlMethodView
//

#ifndef WSDLMETHODVIEW_H
#define WSDLMETHODVIEW_H

#include "ui_WsdlMethodView.h"

#include <QDomDocument>
#include <QStandardItemModel>
#include <QWidget>

#include "WsdlTreeViewHeaderWidget.h"

class WsdlMethodView : public QWidget
{
  Q_OBJECT
public:
protected:
private:
  Ui::WsdlMethodView ui;

  QDomDocument m_doc;
  QString m_host;
  QString m_method;
  QStandardItemModel m_model;

public:
  WsdlMethodView(QWidget* parent=0);
  ~WsdlMethodView();

  bool DoShowInfo() {return ui.TreeHeader->InfoChecked();}
  void Init(const QString& host, const QString& method, QDomDocument doc);
  QDomDocument Document() {return m_doc;}

private:
  void CreateTreeView(const QDomDocument& doc);
  void ExpandItem(QStandardItem* item);
  void StuffItem(QDomElement node, QStandardItem* item);
  void StuffJson(QJsonObject obj, QStandardItem* item);
  void StuffJsonInfo(QStandardItem* parent, int row, const QString& title, const QJsonDocument& jsonDoc);
  void UpdateJsonInfo(QStandardItem* parent, const QString& title, const QJsonDocument& jsonDoc);
  void XmlUpdate();

signals:
private slots:
  void OnXmlExport();
  void OnInfoToggled() {CreateTreeView(m_doc);}
  void OnRefreshClicked() {XmlUpdate();}
  void OnSaveClicked() {Q_ASSERT(false);}
  void OnXmlItemChanged(QStandardItem* item);
};

#endif // WSDLMETHODVIEW_H
