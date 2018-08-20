//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: HostMethodListWidget
//

#include <QListView>
#include <QVBoxLayout>

#include "HostMethodListWidget.h"
#include "TimelineEvent.h"
#include "TimelineEventEditor.h"
#include "TimelineScene.h"
#include "WsdlFile.h"

const int HOST_ROLE = Qt::UserRole + 1;

//------------------------------------------------------------------------------
// HostMethodListWidget
//
HostMethodListWidget::HostMethodListWidget(int index, const QString& hostName, QWidget* parent)
  : HeaderContainerWidget(index, hostName, parent),
  m_hostName(hostName)
{
  QVBoxLayout* layout = new QVBoxLayout(this);
  layout->setSpacing(0);
  layout->setObjectName(QStringLiteral("ContainerLayout"));
  layout->setContentsMargins(0, 0, 0, 0);

  // List View
  QListView* view = new QListView(this);
  view->setAcceptDrops(false);
  view->setDefaultDropAction(Qt::IgnoreAction);
  view->setDragEnabled(true);
  view->setSelectionBehavior(QAbstractItemView::SelectRows);
  view->setSelectionMode(QAbstractItemView::ExtendedSelection);
  view->setEditTriggers(QAbstractItemView::NoEditTriggers);
  view->setModel(&m_model);

  connect(view, SIGNAL(doubleClicked(const QModelIndex&)), this, SLOT(OnListViewDoubleClicked(const QModelIndex&)));

  Container()->layout()->addWidget(view);
  Header()->SetColor(QColor(168,60,15));

  Update();
}
//------------------------------------------------------------------------------
// ~HostMethodListWidget
//
HostMethodListWidget::~HostMethodListWidget()
{
}
//------------------------------------------------------------------------------
// Update
//
void HostMethodListWidget::Update()
{
  m_model.clear();
  WsdlFile* wsdlFile = WsInfo().Wsdl(m_hostName);
  QList<QStandardItem*> items;
  foreach (const WsdlMethod* m, wsdlFile->EnabledMethods())
  {
    QStandardItem* item = new QStandardItem(m->Name);
    item->setToolTip(m->Desc);
    item->setData(wsdlFile->HostName(), HOST_ROLE);
    items << item;
  }

  m_model.appendColumn(items);
}
//------------------------------------------------------------------------------
// OnListViewDoubleClicked
//
void HostMethodListWidget::OnListViewDoubleClicked(const QModelIndex& index)
{
  if (!index.isValid())
    return;

  QString methodName = index.data(Qt::DisplayRole).toString();
  QString hostName = index.data(HOST_ROLE).toString();
  WsdlFile* wsdl = WsInfo().Wsdl(hostName);
  TimelineEvent reqEvent(TimelineEvent::Request, 0, hostName, methodName, wsdl->MethodTemplateRequest(methodName));
  TimelineEvent resEvent(TimelineEvent::Response, 0, hostName, methodName, wsdl->MethodTemplateResponse(methodName));
  TimelineEventEditor dlg(reqEvent, resEvent, this);
  if (dlg.exec())
  {
    reqEvent.Copy(dlg.Request());
    resEvent.Copy(dlg.Response());
    Timeline().InsertTimelineEventPair(reqEvent, resEvent);
  }
}



