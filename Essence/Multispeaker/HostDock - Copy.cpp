//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: HostDock
//

#include <QPainter>
#include <QSettings>
#include <QTimer>

#include "DockTitleBar.h"
#include "Host.h"
#include "HostDock.h"
#include "HostMethodWidget.h"
#include "HostScene.h"
#include "HostWidget.h"
#include "WebServiceInfo.h"
#include "WidgetContainer.h"
#include "WsdlFile.h"

#include <QLabel> // debugging

//------------------------------------------------------------------------------
// HostDock
//
HostDock::HostDock(int srcId, const QString& name, QWidget* parent)
  : QDockWidget(name, parent),
  m_srcId(srcId)
{
  setAttribute(Qt::WA_DeleteOnClose, true);
  setObjectName(QString("%1%2").arg(srcId).arg(name)); // Need this to ensure that Main Window saveState() works
  setFloating(false);
  setWindowTitle(WsInfo().FullName(name));
  //setWindowTitle(QString("%1 - %2").arg(WsInfo().FullName(name)).arg(m_id));

  InitDockTitleBar();
  QTimer::singleShot(0, this, SLOT(Update())); // force update later
}
//------------------------------------------------------------------------------
// ~HostDock
//
HostDock::~HostDock()
{
}
//-------------------------------------------------------------------------------
// paintEvent
//
void HostDock::paintEvent(QPaintEvent* e)
{
  QWidget::paintEvent(e);
  QPainter p(this);

  p.setPen(Qt::black);
  p.setBrush(Qt::darkGray);
  p.drawRect(QRect(0, 0, width()-1, height()-1));
  p.end();
}
//------------------------------------------------------------------------------
// InitDockTitleBar
//
void HostDock::InitDockTitleBar()
{
	// Title Bar Stuff
	DockTitleBar* bar = new DockTitleBar(this);
	setTitleBarWidget(bar);
	bar->SetTitle(windowTitle(), 12);
  bar->SetFloating(false);
	connect(bar, SIGNAL(Close()), this, SLOT(close()));
}
//-------------------------------------------------------------------------------
// Update
//
void HostDock::Update()
{
  QList<Host*> hosts = Hosts().AllHosts();
  QList<QWidget*> hostWidgetList;

  foreach (Host* host, hosts)
  {
    if (host->Id() == m_srcId)
      continue; // Don't do own methods

    Host* hostInstance = new Host(*host);
    hostInstance->SetMethodSrcDstIds(m_srcId, host->Id());
    HostWidget* hw = new HostWidget(*hostInstance, ui.Container); 
    hostWidgetList.append(hw);

    // Methods
    WidgetContainer* methodsWC = new WidgetContainer(hw);
    QList<QWidget*> hostMethodWidgetList;

    foreach (HostMethod* method, hostInstance->Methods())
      hostMethodWidgetList.append(new HostMethodWidget(*method));

    methodsWC->SetWidgets(hostMethodWidgetList);

    ////QVBoxLayout* hostLayout = new QVBoxLayout(hw);
    ////hostLayout->setSpacing(2);
    ////hostLayout->setContentsMargins(2, 2, 2, 2);
    ////hostLayout->addWidget(methodsWC);

    //QLabel* label = new QLabel(hw);
    //label->setText("Hello");

  }
  ui.Container->SetWidgets(hostWidgetList);
  //setWidget(hostsWC);
}
