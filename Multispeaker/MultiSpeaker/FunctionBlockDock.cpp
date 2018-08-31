/*-------------------------------------------------------------------------------

  Multi-Speak - Secure Protocol Enterprise Access Kit(MS_SPEAK)
  Copyright © 2018, Battelle Memorial Institute
  All rights reserved.
  1.	Battelle Memorial Institute (hereinafter Battelle) hereby grants permission to any person or
		entity lawfully obtaining a copy of this software and associated documentation files
		(hereinafter “the Software”) to redistribute and use the Software in source and binary forms,
		with or without modification.  Such person or entity may use, copy, modify, merge, publish,
		distribute, sublicense, and/or sell copies of the Software, and may permit others to do so,
		subject to the following conditions:
		•	Redistributions of source code must retain the above copyright notice, this list of
			conditions and the following disclaimers.
		•	Redistributions in binary form must reproduce the above copyright notice, this list of
			conditions and the following disclaimer in the documentation and/or other materials
			provided with the distribution.
		•	Other than as used herein, neither the name Battelle Memorial Institute or Battelle may
			be used in any form whatsoever without the express written consent of Battelle.

  2.	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
		OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
		AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL BATTELLE OR CONTRIBUTORS
		BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
		(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
		OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
		CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
		OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


  This material was prepared as an account of work sponsored by an agency of the United States Government.
  Neither the United States  Government nor the United States Department of Energy, nor Battelle, nor
  any of their employees, nor any jurisdiction or organization  that has cooperated in the development
  of these materials, makes any warranty, express or implied, or assumes any legal liability or
  responsibility for the accuracy, completeness, or usefulness or any information, apparatus, product,
  software, or process disclosed, or represents that its use would not infringe privately owned rights.
  Reference herein to any specific commercial product, process, or service by trade name, trademark,
  manufacturer, or otherwise does not necessarily constitute or imply its endorsement, recommendation, or
  favoring by the United States Government or any agency thereof, or Battelle Memorial Institute. The
  views and opinions of authors expressed herein do not necessarily state or reflect those of the
  United States Government or any agency thereof.
									 PACIFIC NORTHWEST NATIONAL LABORATORY
											    operated by
												  BATTELLE
											      for the
									  UNITED STATES DEPARTMENT OF ENERGY
									   under Contract DE-AC05-76RL01830


    This notice including this sentence must appear on any copies of this computer software.
*/
//-------------------------------------------------------------------------------
//	History
//		2017 - Created By: Lance Irvine.
//		2018 - Modified By: Carl Miller <carl.miller@pnnl.gov>
//-------------------------------------------------------------------------------
//
// Summary: FunctionBlockDock.cpp
//-------------------------------------------------------------------------------

#include <QPainter>
#include <QSettings>
#include <QScrollArea>
#include <QSplitter>

#include "DockTitleBar.h"
#include "FunctionBlockDock.h"
#include "FunctionGroupWidget.h"
#include "Settings.h"
#include "WebServiceInfo.h"

const int REALLY_BIG_HEIGHT = 10000;

//------------------------------------------------------------------------------
// FunctionBlockDock
//
FunctionBlockDock::FunctionBlockDock(const QString& name, QWidget* parent)
  : QDockWidget(name, parent)
{
  Init();
  InitDockTitleBar();
}
//------------------------------------------------------------------------------
// ~FunctionBlockDock
//
FunctionBlockDock::~FunctionBlockDock()
{
}
//-------------------------------------------------------------------------------
// paintEvent
//
void FunctionBlockDock::paintEvent(QPaintEvent* e)
{
  QWidget::paintEvent(e);
  QPainter p(this);

  p.setPen(Qt::black);
  p.setBrush(Qt::darkGray);
  p.drawRect(QRect(0, 0, width()-1, height()-1));
  p.end();
}
//-------------------------------------------------------------------------------
// AddControlGroup
//
QWidget* FunctionBlockDock::AddControlGroup(int index, const QString& title, const QStringList& names, QWidget* parent)
{
	QWidget* widget = new FunctionGroupWidget(index, title, names, parent);
	connect(widget, SIGNAL(Collapsed(int)), this, SLOT(OnCollapsed(int)));
	connect(widget, SIGNAL(Expanded(int)), this, SLOT(OnExpanded(int)));
	return widget;
}
//------------------------------------------------------------------------------
// Collapse
//
void FunctionBlockDock::Collapse()
{
  if (QSplitter* splitter = findChild<QSplitter*>())
  {
    for (int i = 0; i < splitter->count(); i++)
      Collapse(i);
  }
}
//------------------------------------------------------------------------------
// Collapse
//
void FunctionBlockDock::Collapse(int index)
{
  if (QSplitter* splitter = findChild<QSplitter*>())
  {
    if (HeaderContainerWidget* hcw = qobject_cast<HeaderContainerWidget*>(splitter->widget(index)))
    {
	    hcw->setMaximumHeight(hcw->minimumSizeHint().height());

      // Cycle through all the widgets in the splitter and adjust sizes
      bool aWidgetExpanded = false;
      for (int i = 0; i < splitter->count(); i++)
      {
        if (HeaderContainerWidget* w = qobject_cast<HeaderContainerWidget*>(splitter->widget(i)))
        {
          if (HeaderWidget* h = w->Header())
          {
            if (h->IsExpanded())
            {
              w->setMaximumHeight(REALLY_BIG_HEIGHT);
              aWidgetExpanded = true;
            }
          }
        }
        else if (QWidget* w = qobject_cast<QWidget*>(splitter->widget(i)))
        {
          // Adjust Filler widget based on whether any of the above widgets are expanded
          if (aWidgetExpanded)
            w->setMaximumHeight(0);
          else
            w->setMaximumHeight(REALLY_BIG_HEIGHT);
        }
      }
    }
  }
  SaveSplitterState();
}
//------------------------------------------------------------------------------
// Expand
//
void FunctionBlockDock::Expand(int index)
{
  if (QSplitter* splitter = findChild<QSplitter*>())
  {
    if (HeaderContainerWidget* w = qobject_cast<HeaderContainerWidget*>(splitter->widget(index)))
    {
    	w->setMaximumHeight(REALLY_BIG_HEIGHT); // Very Large Number
      w->Update();
    }

    // Adjust filler widget to ensure it doens't take any space
    if (QWidget* w = splitter->widget(splitter->count()-1))
    {
      w->setMaximumHeight(0);
    }
  }
  SaveSplitterState();
}
//------------------------------------------------------------------------------
// Init
//
void FunctionBlockDock::Init()
{
	// Create and populate new scrollArea
	QScrollArea* scrollArea = new QScrollArea(this);
	scrollArea->setObjectName(QString::fromUtf8("ScrollArea"));
	scrollArea->setWidgetResizable(true);
	QWidget* contents = new QWidget();
	contents->setObjectName(QString::fromUtf8("contents"));
	contents->setGeometry(QRect(0, 0, 379, 276));

	QVBoxLayout* vLayout = new QVBoxLayout(contents);
	vLayout->setSpacing(0);
	vLayout->setContentsMargins(0, 0, 0, 0);
	vLayout->setObjectName(QString::fromUtf8("vLayout"));

	QSplitter* splitter = new QSplitter(contents);
	connect(splitter, SIGNAL(splitterMoved(int,int)), this, SLOT(OnSplitterMoved(int,int)));
	splitter->setObjectName(QString::fromUtf8("Splitter"));
	splitter->setFrameShape(QFrame::NoFrame);
	splitter->setLineWidth(0);
	splitter->setOrientation(Qt::Vertical);
	splitter->setChildrenCollapsible(false);

	vLayout->addWidget(splitter);
	scrollArea->setWidget(contents);

  setWidget(scrollArea);

	// Add Widgets
	int index = 0;
	splitter->addWidget(AddControlGroup(index++, WS_GROUP_CBPM, WsInfo().GroupShortNames(WS_GROUP_CBPM), contents));
	splitter->addWidget(AddControlGroup(index++, WS_GROUP_DR, WsInfo().GroupShortNames(WS_GROUP_DR), contents));
	splitter->addWidget(AddControlGroup(index++, WS_GROUP_DEPC, WsInfo().GroupShortNames(WS_GROUP_DEPC), contents));
	splitter->addWidget(AddControlGroup(index++, WS_GROUP_MSM, WsInfo().GroupShortNames(WS_GROUP_MSM), contents));
	splitter->addWidget(AddControlGroup(index++, WS_GROUP_OMDO, WsInfo().GroupShortNames(WS_GROUP_OMDO), contents));
	splitter->addWidget(AddControlGroup(index++, WS_GROUP_WM, WsInfo().GroupShortNames(WS_GROUP_WM), contents));
	splitter->addWidget(AddControlGroup(index++, WS_GROUP_WOAI, WsInfo().GroupShortNames(WS_GROUP_WOAI), contents));

	// Add filler widget to end
	QWidget* w = new QWidget(contents);
  w->setObjectName("FillerWidget");
  w->setMaximumHeight(REALLY_BIG_HEIGHT); // Force filler to take all the height
	splitter->addWidget(w);
  Collapse();
	RestoreSplitterState();
}
//------------------------------------------------------------------------------
// InitDockTitleBar
//
void FunctionBlockDock::InitDockTitleBar()
{
	// Title Bar Stuff
	DockTitleBar* bar = new DockTitleBar(this);
	setTitleBarWidget(bar);
	bar->SetTitle(windowTitle(), 12);
  bar->SetFloating(false);
	connect(bar, SIGNAL(Close()), this, SLOT(close()));
}
//------------------------------------------------------------------------------
// RestoreSplitterState
//
void FunctionBlockDock::RestoreSplitterState()
{
  if (QSplitter* splitter = findChild<QSplitter*>())
  {
  	splitter->restoreState(QSettings().value(SK_FUNCTION_BLOCK_DOCK_SCROLL_SPLITTER_STATE).toByteArray());
  }
}
//------------------------------------------------------------------------------
// SaveSplitterState
//
void FunctionBlockDock::SaveSplitterState()
{
  if (QSplitter* splitter = findChild<QSplitter*>())
  {
  	QSettings().setValue(SK_FUNCTION_BLOCK_DOCK_SCROLL_SPLITTER_STATE, splitter->saveState());
  }
}
