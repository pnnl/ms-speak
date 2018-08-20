//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: WsdlFileView
//

#ifndef WSDLFILEVIEW_H
#define WSDLFILEVIEW_H

#include "ui_WsdlFileView.h"

#include <QStandardItemModel>
#include <QWidget>

#include "WsdlFile.h"

class QStandardItem;

//------------------------------------------------------------------------------
// WsdlFileView
//
class WsdlFileView : public QWidget
{
  Q_OBJECT
private:
  Ui::WsdlFileView ui;

  QString m_host; // short name of the host
  QStandardItemModel m_model;
  WsdlFile* m_wsdlFile; 

public:
  WsdlFileView(const QString& host, QWidget* parent=0);
  ~WsdlFileView();

private slots:
  void OnBrowse();
  void OnMethodDoubleClicked(const QModelIndex& index);
  void OnModelChanged(QStandardItem* item);
  void OnUpdate();
};

#endif // WSDLFILEVIEW_H
