//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: FunctionGroupWidget
//

#include <QDebug>
#include <QInputDialog>
#include <QStringList>

#include "FunctionBlockListView.h"
#include "FunctionGroupWidget.h"
#include "WebServiceInfo.h"

//------------------------------------------------------------------------------
// FunctionGroupWidget
//
FunctionGroupWidget::FunctionGroupWidget(int index, const QString& title, const QStringList& groupShortNames, QWidget* parent)
  : HeaderContainerWidget(index, title, parent)
{
  FunctionBlockListView* view = new FunctionBlockListView(this);
  view->setModel(&m_model);
  view->setEditTriggers(QAbstractItemView::NoEditTriggers);
  Container()->layout()->addWidget(view);
  Header()->SetColor(QColor(168,60,15));

  Init(groupShortNames);
}
//------------------------------------------------------------------------------
// ~FunctionGroupWidget
//
FunctionGroupWidget::~FunctionGroupWidget()
{
}
//------------------------------------------------------------------------------
// Init
//
void FunctionGroupWidget::Init(const QStringList& groupShortNames) 
{
  m_model.clear();

  QList<QStandardItem*> items;
  foreach (const QString shortName, groupShortNames)
  {
    QStandardItem* item = new QStandardItem(WsInfo().FullName(shortName));
    item->setData(shortName);
    items << item;
  }

  m_model.appendColumn(items);
}