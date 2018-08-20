//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: HostMethodListWidget
//

#ifndef HOSTMETHODLISTWIDGET_H
#define HOSTMETHODLISTWIDGET_H

#include <QStandardItemModel>
#include <QWidget>

#include "HeaderContainerWidget.h"

class WsdlFile;

class HostMethodListWidget : public HeaderContainerWidget
{
  Q_OBJECT
private:
  QString m_hostName;
  QStandardItemModel m_model;

public:
  HostMethodListWidget(int index, const QString& hostName, QWidget* parent=0);
  ~HostMethodListWidget();

  QString Host() {return Header()->Title();}
  virtual void Update();

private slots:
  void OnListViewDoubleClicked(const QModelIndex& index);
};

#endif // HOSTMETHODLISTWIDGET_H
