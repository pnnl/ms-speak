//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: HostView
//

#include <QKeyEvent>

#include "HostScene.h"
#include "HostView.h"

//------------------------------------------------------------------------------
// HostView
//
HostView::HostView(QWidget* parent)
  : QGraphicsView(parent)
{
  setDragMode(QGraphicsView::RubberBandDrag);
  setRubberBandSelectionMode(Qt::IntersectsItemShape);
  setAlignment(Qt::AlignLeft | Qt::AlignTop);
  setAcceptDrops(true);
  setScene(&Hosts());
}
//------------------------------------------------------------------------------
// ~HostView
//
HostView::~HostView()
{
}
//-------------------------------------------------------------------------------
// keyReleaseEvent
//
void HostView::keyReleaseEvent(QKeyEvent* e)
{
  if (e->key() == Qt::Key_Delete)
  {
    if (HostScene* s = qobject_cast<HostScene*>(scene()))
      s->RemoveItems(s->selectedItems());
  }

  QGraphicsView::keyReleaseEvent(e);
}
//------------------------------------------------------------------------------
// resizeEvent
//
void HostView::resizeEvent(QResizeEvent* e)
{
  Q_UNUSED(e);
  QRectF bounding = scene()->itemsBoundingRect();
  qreal bw = bounding.width() + bounding.x() + 2.0;
  qreal bh = bounding.height() + bounding.y() + 2.0;
  qreal vw = (qreal)width() - 2.0;
  qreal vh = (qreal)height() - 2.0;
  //qDebug() << "Bound:" << bw << "View:" << vw << qMax(bw, vw);
  scene()->setSceneRect(1, 1, qMax(bw, vw), qMax(bh, vh));
}
