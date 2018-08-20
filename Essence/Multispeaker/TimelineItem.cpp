//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: TimelineItem
//

#include <QCursor>
#include <QDebug>
#include <QGraphicsSceneMouseEvent>
#include <QGuiApplication>
#include <QPainter>
#include <QToolTip>

#include "TimelineItem.h"
#include "TimelineScene.h"


// All Times in secs
const int BORDER_MARGIN = 1;
const int HEIGHT = 30;
const bool SHOW_LABELS = true;
const int TIC_HEIGHT = 10;
const int TIC_LABEL_SEP = 5;
const int TIME_MAX = 300;
const int TIME_TIC_MAJOR_SPAN = 60;

//------------------------------------------------------------------------------
// TimelineItem
//
TimelineItem::TimelineItem(QGraphicsItem* parent)
  : QGraphicsObject(parent),
  m_border(BORDER_MARGIN),
  m_timeMax(TIME_MAX),
  m_timeMin(0),
  m_timeSpan(m_timeMax - m_timeMin),
  m_timeTicMajorSpan(TIME_TIC_MAJOR_SPAN),
  //m_timeTicMinorSpan(5),
  m_xScaleConst(1.0)
{
  //setAcceptDrops(true);
  setAcceptHoverEvents(true);
  setZValue(100);
  //setFlags(QGraphicsItem::ItemIsSelectable);
}
//------------------------------------------------------------------------------
// ~TimelineItem
//
TimelineItem::~TimelineItem()
{
}
//------------------------------------------------------------------------------
// boundingRect
//
QRectF TimelineItem::boundingRect() const
{
  return QRectF(0, 0, scene()->width(), HEIGHT);
}
//------------------------------------------------------------------------------
// paint
//
void TimelineItem::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* w)
{
  Q_UNUSED(option);
  Q_UNUSED(w);

  painter->setRenderHint(QPainter::Antialiasing, false);
  painter->setPen(QPen(Qt::black, 0));
  painter->setBrush(Qt::lightGray);
  painter->drawRect(QRectF(0, 0, scene()->width()-1, HEIGHT-1));

  PaintTicsMajor(*painter);
}
//------------------------------------------------------------------------------
// PaintTicsMajor
//
void TimelineItem::PaintTicsMajor(QPainter& p)
{
  //qDebug() << "Bounding Rect:" << boundingRect();
  p.setRenderHint(QPainter::Antialiasing, false);
  p.setPen(QPen(Qt::black, 0));

  for (int i = 1; i < m_timeTicMajor.count(); ++i) // note we are skipping first entry of 0
  {
    qreal x = m_timeTicMajor.at(i);
    if (SHOW_LABELS)
    {
      QPointF loc(x, HEIGHT - TIC_LABEL_SEP);
      QString label = m_timeTicMajorLabels.at(i);
      QSize labelSize = QSize(p.fontMetrics().boundingRect(label).width(), p.fontMetrics().boundingRect(label).height());
      QRect labelRect = QRect(loc.toPoint(), labelSize);
      labelRect.moveTop(labelRect.y() - p.fontMetrics().ascent()); // account for fact that draw Text pt is baseline
      labelRect.moveLeft(loc.x() - (labelSize.width() / 2));
      p.drawText(labelRect, label);
    }
    p.drawLine(QPointF(x, 0), QPointF(x, TIC_HEIGHT));
  }
}
//------------------------------------------------------------------------------
// shape
//
QPainterPath TimelineItem::shape() const
{
  QPainterPath path;
  path.addRect(QRectF(0, 0, scene()->width(), HEIGHT));
  return path;
}
//-------------------------------------------------------------------------------
// hoverLeaveEvent
//
void TimelineItem::hoverLeaveEvent(QGraphicsSceneHoverEvent* e)
{
  Q_UNUSED(e);
  //QGuiApplication::restoreOverrideCursor();
}
//-------------------------------------------------------------------------------
// hoverMoveEvent
//
void TimelineItem::hoverMoveEvent(QGraphicsSceneHoverEvent* e)
{
  //QCursor cursor(Qt::ArrowCursor);
  //const QBitmap* bit = cursor.bitmap();
  //QPixmap pix = cursor.pixmap();
  //QRect r = pix.rect();
  //int val = e->screenPos().x() % (1440 / 60);
  //QPainter p(&pix);
  //p.drawText(0,0, QString::number(val));

  //QGuiApplication::setOverrideCursor(cursor);

  QToolTip::hideText();
  QToolTip::showText(e->screenPos(), QString("%1:%2").arg((int)PixToX(e->pos().x()) / 60).arg(qRound(PixToX(e->pos().x())) % 60));
  //qDebug() << e->screenPos();
  //QGraphicsObject::hoverMoveEvent(e);
}
//-------------------------------------------------------------------------------
// mouseMoveEvent
//
void TimelineItem::mouseMoveEvent(QGraphicsSceneMouseEvent* e)
{
  QToolTip::showText(e->screenPos(), "HELLO");
    //// Mouse over Data Plot
    //if (m_dataRect.contains(e->pos()))
 // {
 //   bool found;
 //   QToolTip::showText(e->globalPos(), CurvePointAtPoint(e->pos(), &found));
 //   if (found)
 //     setCursor(Qt::CrossCursor);
 //   else
 //     setCursor(Qt::ArrowCursor);
 // }
 // // Mouse over one of the Scales
    //else if (m_hsRect.contains(e->pos()) || m_vsRect.contains(e->pos()))
 // {
 //   // Dragging
    //	if (m_selectedLine && m_draggingLine)
 //   {
 //     if (m_selectedLine->IsMovable())
 //     {
 //       qreal val = 0.0;
 //       if (m_selectedLine->Orientation() == PlotLine::vert)
 //       {
 //         val = qRound(1000 * NearestX(PixToX(e->x()))) * .001;
 //         val = qBound(m_hsDataMin, val, m_hsDataMax);
 //       }
 //       else
 //       {
 //         val = qRound(1000 * NearestY(PixToY(e->y()))) * .001;
 //         val = qBound(m_vsDataMin, val, m_vsDataMax);
 //       }
 //       QToolTip::showText(e->globalPos(), QString("%1:%2").arg(m_selectedLine->Label()).arg(val));
 //       setCursor(Qt::ClosedHandCursor);
 //       m_selectedLine->SetVal(val);
 //       CalcDataLine(*m_selectedLine);
    //		  update();
 //       emit LineMoved(m_selectedLine->Label(), val);
 //     }
 //   }
 //   // On Line
    //	else if (LineAtPoint(e->pos()))
 //   {
 //     PlotLine* line = LineAtPoint(e->pos());
 //     if (line->Visible())
 //     {
 //       if (LineAtPoint(e->pos())->IsMovable())
 //         setCursor(Qt::PointingHandCursor);
 //       else
 //         setCursor(Qt::ArrowCursor);
 //       QToolTip::showText(e->globalPos(), line->ToolTip());
 //     }
 //     else
 //       setCursor(Qt::ArrowCursor);
 //   }
 //   else
 //   {
 //     setCursor(Qt::ArrowCursor);
 //   }
 // }
 // else
 //   setCursor(Qt::ArrowCursor);
}
//-------------------------------------------------------------------------------
// CalcConst
//
void TimelineItem::CalcConst(const QRectF& sceneRect)
{
  setPos(1, sceneRect.height() - HEIGHT);
  m_timeTicMajor.clear();
  m_timeTicMajorLabels.clear();

  m_xScaleConst = (sceneRect.width()-(2*m_border)) / (qreal)m_timeSpan;
  //qDebug() << sceneRect.width() << (sceneRect.width()-(2*m_border)) << m_timeSpan << m_xScaleConst;
  //qDebug() << "Bounding Rect:" << boundingRect();

  int start = m_timeMin;
  if (m_timeMin % m_timeTicMajorSpan != 0)
  {
    while (m_timeMin % m_timeTicMajorSpan != 0)
      start++; // Move start to a major tic spot
  }

  int i = start;
  while (i < m_timeMax)
  {
    // pix value
    qreal pix = XToPix(i);
    m_timeTicMajor << pix;

    // Label
    m_timeTicMajorLabels << QString::number(i / TIME_TIC_MAJOR_SPAN);

    i += m_timeTicMajorSpan;
  }
  //qDebug() << m_timeTicMajor;
  //qDebug() << m_timeTicMajorLabels;
}

