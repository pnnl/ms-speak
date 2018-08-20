//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: FunctionGroupWidget
//

#ifndef FUNCTIONGROUPWIDGET_H
#define FUNCTIONGROUPWIDGET_H

#include "ui_FunctionGroupWidget.h"

#include <QStandardItemModel>

#include "HeaderContainerWidget.h"

class FunctionGroupWidget : public HeaderContainerWidget
{
  Q_OBJECT
private:
  Ui::FunctionGroupWidget ui;

  QStandardItemModel m_model;

public:
  FunctionGroupWidget(int index, const QString& title, const QStringList& names, QWidget* parent=0);
  ~FunctionGroupWidget();

private:
  virtual void Init(const QStringList& groupShortNames);
};

#endif // FUNCTIONGROUPWIDGET_H
