//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: AnimatedLineItem
//

#include <QDebug>
#include <QPainter>
#include <QPainterPath>

#include "AnimatedLineItem.h"

//------------------------------------------------------------------------------
// AnimatedLineItem
//
AnimatedLineItem::AnimatedLineItem(HostItem* src, HostItem* dst, QGraphicsItem* parent)
  : QGraphicsObject(parent), 
  m_animateFinished(false),
  m_animatePt(src->Origin()),
  m_animatePtAnimation(this, "AnimatePt"),
  m_blockDst(dst),
  m_blockSrc(src),
  m_line(src->Origin(), dst->Origin())
{
  InitAnimation();
}
//------------------------------------------------------------------------------
// ~AnimatedLineItem
//
AnimatedLineItem::~AnimatedLineItem()
{
}
//------------------------------------------------------------------------------
// InitAnimation
//
void AnimatedLineItem::InitAnimation()
{
  //m_animatePtAnimation.setEasingCurve(QEasingCurve::InOutElastic);
  m_animatePtAnimation.setStartValue(m_blockSrc->Origin());
  m_animatePtAnimation.setEndValue(m_blockDst->Origin());
  m_animatePtAnimation.setDuration(1000);
  connect(&m_animatePtAnimation, SIGNAL(finished()), this, SLOT(OnAnimateFinished()));
  Animate();
}
//------------------------------------------------------------------------------
// paint
//
void AnimatedLineItem::paint(QPainter* p, const QStyleOptionGraphicsItem* item, QWidget* w) 
{
  Q_UNUSED(item);
  Q_UNUSED(w);
  if (!m_animateFinished)
  {
    p->setRenderHint(QPainter::Antialiasing, true);
    p->setPen(QPen(Qt::black, 2));
    p->drawLine(m_line);

    p->setPen(QPen(Qt::black, 8));
    p->drawPoint(m_animatePt);
    p->setPen(QPen(Qt::green, 5));
    p->drawPoint(m_animatePt);
  }
}
//------------------------------------------------------------------------------
// shape
//
QPainterPath AnimatedLineItem::shape() const
{
  QPainterPath path(m_line.p1());
  path.lineTo(m_line.p2());
  QPainterPathStroker stroker;
  stroker.setWidth(8);
  return stroker.createStroke(path);
}
//------------------------------------------------------------------------------
// UpdatePosition
//
void AnimatedLineItem::UpdatePosition()
{
  prepareGeometryChange();
  m_line.setP1(m_blockSrc->Origin());
  m_line.setP2(m_blockDst->Origin());
  qDebug() << m_line;
  update();
}
//------------------------------------------------------------------------------
// OnAnimateFinished
//
void AnimatedLineItem::OnAnimateFinished() 
{
  if (m_animatePtAnimation.direction() == QAbstractAnimation::Forward)
  {
    m_animatePtAnimation.setDirection(QAbstractAnimation::Backward);
    Animate();
  }
  else
  {
    m_animateFinished = true;
    update(boundingRect());
    m_blockSrc->RemoveEdge(this);
    m_blockDst->RemoveEdge(this);
    emit Finished(this);
  }
}