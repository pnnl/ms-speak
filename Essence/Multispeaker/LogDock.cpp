//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: LogDock
//

#include <QPainter>

#include "DockTitleBar.h"
#include "HostScene.h"
#include "LogDock.h"
#include "Timer.h"
#include "TimelineScene.h"
#include "TimelineEvent.h"

//------------------------------------------------------------------------------
// LogDock
//
LogDock::LogDock(QWidget* parent)
  : QDockWidget("Log", parent)
{
  ui.setupUi(this);
  setWindowTitle("Log");
  setObjectName("LogDock");
  InitDockTitleBar();

  connect(&Timeline(), SIGNAL(EventProcessed(TimelineEvent&)), this, SLOT(OnNotify(TimelineEvent&)));
}
//------------------------------------------------------------------------------
// ~LogDock
//
LogDock::~LogDock()
{
}
//------------------------------------------------------------------------------
// Append
//
void LogDock::Append(const QString& timeStamp, const QString& msg)
{
  ui.PlainTextEdit->appendPlainText(QString("%1: %2").arg(timeStamp, msg));
}
//------------------------------------------------------------------------------
// Append
//
void LogDock::Append(TimelineEvent& e)
{
  ui.PlainTextEdit->appendPlainText(QString("%1: %2").arg(Timer().ToStringMS(e.TimeStamp())).arg(e.Method()));
}
//-------------------------------------------------------------------------------
// paintEvent
//
void LogDock::paintEvent(QPaintEvent* e)
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
void LogDock::InitDockTitleBar()
{
	// Title Bar Stuff
	DockTitleBar* bar = new DockTitleBar(this);
	setTitleBarWidget(bar);
	bar->SetTitle(windowTitle(), 12);
  bar->SetFloating(false);
	connect(bar, SIGNAL(Close()), this, SLOT(close()));
}