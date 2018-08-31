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
// Summary: WidgetContainer.cpp
//-------------------------------------------------------------------------------

#include <QSettings>
#include <QSplitter>
#include <QVBoxLayout>

#include "HeaderContainerWidget.h"
#include "Settings.h"
#include "Utils.h"
#include "WidgetContainer.h"

const int REALLY_BIG_HEIGHT = 10000;

//------------------------------------------------------------------------------
// WidgetContainer
//
WidgetContainer::WidgetContainer(const QString& saveRestoreKey, QWidget* parent)
  : QScrollArea(parent),
  m_saveRestoreKey(saveRestoreKey)
{
	setObjectName(QString::fromUtf8("ScrollArea"));
	setWidgetResizable(true);
}
//------------------------------------------------------------------------------
// ~WidgetContainer
//
WidgetContainer::~WidgetContainer()
{
}
//------------------------------------------------------------------------------
// SetWidgets
//
void WidgetContainer::SetWidgets(const QList<QWidget*> list)
{
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

	// Add Widgets
  foreach (QWidget* w, list)
  {
    if (HeaderContainerWidget* hcw = qobject_cast<HeaderContainerWidget*>(w))
    {
	    connect(hcw, SIGNAL(Collapsed(int)), this, SLOT(OnCollapsed(int)));
	    connect(hcw, SIGNAL(Expanded(int)), this, SLOT(OnExpanded(int)));
    }
	  splitter->addWidget(w);
  }

	// Add filler widget to end
	QWidget* w = new QWidget(contents);
  w->setObjectName("FillerWidget");
  w->setMaximumHeight(REALLY_BIG_HEIGHT); // Force filler to take all the height
	splitter->addWidget(w);

	setWidget(contents);

  Expand(false);
	RestoreSplitterState();
}
//------------------------------------------------------------------------------
// Collapse
//
void WidgetContainer::Collapse(bool doSaveState)
{
  if (QSplitter* splitter = findChild<QSplitter*>())
  {
    for (int i = 0; i < splitter->count(); i++)
      Collapse(i, doSaveState);
  }
}
//------------------------------------------------------------------------------
// Collapse
//
//   Concept here is to force the maxHeight to Header Min Size hint if collapsed and really
//    large number otherwise so that the splitter will sort things out
//
void WidgetContainer::Collapse(int index, bool doSaveState)
{
  if (QSplitter* splitter = findChild<QSplitter*>())
  {
    if (HeaderContainerWidget* hcw = qobject_cast<HeaderContainerWidget*>(splitter->widget(index)))
    {
      hcw->Collapse();
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
    splitter->setSizes(splitter->sizes()); // Need this to force update of splitter...for restoreState to work correctly
  }
  if (doSaveState)
    SaveSplitterState();
}
//------------------------------------------------------------------------------
// Expand
//
void WidgetContainer::Expand(bool doSaveState)
{
  if (QSplitter* splitter = findChild<QSplitter*>())
  {
    for (int i = 0; i < splitter->count(); i++)
      Expand(i, doSaveState);
  }
}
//------------------------------------------------------------------------------
// Expand
//
void WidgetContainer::Expand(int index, bool doSaveState)
{
  if (QSplitter* splitter = findChild<QSplitter*>())
  {
    if (HeaderContainerWidget* hcw = qobject_cast<HeaderContainerWidget*>(splitter->widget(index)))
    {
      hcw->Expand();
    	hcw->setMaximumHeight(REALLY_BIG_HEIGHT); // Very Large Number
      hcw->Update();
    }

    // Adjust filler widget to ensure it doens't take any space
    if (QWidget* w = splitter->widget(splitter->count()-1))
    {
      w->setMaximumHeight(0);
    }
    splitter->setSizes(splitter->sizes()); // Need this to force update of splitter...for restoreState to work correctly
  }
  if (doSaveState)
    SaveSplitterState();
}
//------------------------------------------------------------------------------
// RestoreSplitterState
//
void WidgetContainer::RestoreSplitterState()
{
  if (QSplitter* splitter = findChild<QSplitter*>("Splitter"))
  {
    //qDebug() << "Restore" << splitter->sizes();
    //qDebug() << Utils::DebugByteArrayToString(QSettings().value(m_saveRestoreKey).toByteArray());
  	splitter->restoreState(QSettings().value(m_saveRestoreKey).toByteArray());
  }
}
//------------------------------------------------------------------------------
// SaveSplitterState
//
void WidgetContainer::SaveSplitterState()
{
  if (QSplitter* splitter = findChild<QSplitter*>("Splitter"))
  {
    //splitter->update();
    //qDebug() << "Save" << splitter->sizes();
    //splitter->setSizes(splitter->sizes());
    //qDebug() << Utils::DebugByteArrayToString(splitter->saveState());
    //qDebug() << "Save 1" << splitter->sizes();
  	QSettings().setValue(m_saveRestoreKey, splitter->saveState());
    //qDebug() << "Save 3" << splitter->sizes();
  }
}

