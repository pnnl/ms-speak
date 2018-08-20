//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: TimelineView
//

#include <QDebug>
#include <QKeyEvent>

#include "TimelineView.h"

//------------------------------------------------------------------------------
// TimelineView
//
TimelineView::TimelineView(QWidget* parent)
  : QGraphicsView(parent)
{
  setDragMode(QGraphicsView::RubberBandDrag);
  setRubberBandSelectionMode(Qt::IntersectsItemShape);
  setAcceptDrops(true);
  setAlignment(Qt::AlignLeft | Qt::AlignBottom);
  setScene(&Timeline());
}
//------------------------------------------------------------------------------
// ~TimelineView
//
TimelineView::~TimelineView()
{
}
//-------------------------------------------------------------------------------
// keyReleaseEvent
//
void TimelineView::keyReleaseEvent(QKeyEvent* e)
{
  if (e->key() == Qt::Key_Delete)
  {
    if (TimelineScene* s = qobject_cast<TimelineScene*>(scene()))
      s->RemoveItems(s->selectedItems());
  }

  QGraphicsView::keyReleaseEvent(e);
}
