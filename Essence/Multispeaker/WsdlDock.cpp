//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: WsdlDock
//

#include <QPainter>

#include "DockTitleBar.h"
#include "WsdlDock.h"

//------------------------------------------------------------------------------
// WsdlDock
//
WsdlDock::WsdlDock(QWidget* parent)
  : QDockWidget("WSDL", parent)
{
  setWindowTitle("WSDL");
  setObjectName("WsdlDock");
  InitDockTitleBar();
}
//------------------------------------------------------------------------------
// ~WsdlDock
//
WsdlDock::~WsdlDock()
{
}
//-------------------------------------------------------------------------------
// paintEvent
//
void WsdlDock::paintEvent(QPaintEvent* e)
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
void WsdlDock::InitDockTitleBar()
{
	// Title Bar Stuff
	DockTitleBar* bar = new DockTitleBar(this);
	setTitleBarWidget(bar);
	bar->SetTitle(windowTitle(), 12);
  bar->SetFloating(false);
	connect(bar, SIGNAL(Close()), this, SLOT(close()));
}
