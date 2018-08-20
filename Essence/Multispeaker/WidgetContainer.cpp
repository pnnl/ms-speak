//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: WidgetContainer
//

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

