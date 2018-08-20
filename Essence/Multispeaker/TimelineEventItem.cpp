//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: TimelineEventItem
//

#include <QCursor>
#include <QPainter>

#include "Timer.h"
#include "TimelineEventItem.h"

const int WIDTH = 10;
const int HEIGHT = 40;

//------------------------------------------------------------------------------
// TimelineEventItem
//
TimelineEventItem::TimelineEventItem(TimelineEvent& te, QGraphicsItem* parent)
  : QGraphicsObject(parent),
  m_timelineEvent(te)
{
  setToolTip(QString("%1 - %2").arg(Timer().ToStringMS(TimeStamp())).arg(Name()));
  setFlags(QGraphicsItem::ItemIsMovable | QGraphicsItem::ItemIsSelectable);
  setCursor(Qt::PointingHandCursor);

  QPolygonF poly;
  poly << QPointF(0,40) << QPointF(0,0) << QPointF(30,0) << QPointF(0,15);
  m_path.addPolygon(poly);
}
//------------------------------------------------------------------------------
// ~TimelineEventItem
//
TimelineEventItem::~TimelineEventItem()
{
}
//------------------------------------------------------------------------------
// paint
//
void TimelineEventItem::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* w)
{
  Q_UNUSED(option);
  Q_UNUSED(w);

  painter->setRenderHint(QPainter::Antialiasing, true);
  painter->setPen(QPen(Qt::black, 0));
  painter->setBrush(QColor(0, 255,255,127));

  painter->drawPath(m_path);
}