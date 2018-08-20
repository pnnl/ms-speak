//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: AnimatedLineItem
//

#ifndef ANIMATEDLINEITEM_H
#define ANIMATEDLINEITEM_H

#include <QDebug>
#include <QPropertyAnimation>
#include <QGraphicsObject>

#include "HostItem.h"

class AnimatedLineItem : public QGraphicsObject
{
  Q_OBJECT
  Q_PROPERTY(QPointF AnimatePt READ AnimatePt WRITE SetAnimatePt)

public:
  enum {Type = UserType + GRAPH_TYPE_LINE};

private:
  bool m_animateFinished;
  QPointF m_animatePt;
  QPropertyAnimation m_animatePtAnimation;
  HostItem* m_blockDst;
  HostItem* m_blockSrc;
  QLineF m_line;

public:
  AnimatedLineItem(HostItem* src, HostItem* dst, QGraphicsItem* parent=0);
  ~AnimatedLineItem();

  HostItem* BlockDst() {return m_blockDst;}
  HostItem* BlockSrc() {return m_blockSrc;}

  virtual QRectF boundingRect() const 
  {
    return QRectF(
      qMin(m_blockSrc->Origin().x()-4, m_blockDst->Origin().x())-4, 
      qMin(m_blockSrc->Origin().y()-4, m_blockDst->Origin().y())-4, 
      qMax(1.0, qAbs(m_blockSrc->Origin().x() - m_blockDst->Origin().x())+8),
      qMax(1.0, qAbs(m_blockSrc->Origin().y() - m_blockDst->Origin().y())+12));
  }

  QPointF AnimatePt() const {return m_animatePt;}
  void InitAnimation();

  virtual void paint(QPainter* p, const QStyleOptionGraphicsItem* item, QWidget* w) ;

  void SetAnimatePt(QPointF p) {m_animatePt = p; update(boundingRect());}

  virtual QPainterPath shape() const;
  virtual int type() const {return Type;}

  void UpdatePosition();

private:
  void Animate() {m_animatePtAnimation.start();}

signals:
  void Finished(AnimatedLineItem* item);

private slots:
  void OnAnimateFinished();
};

#endif // ANIMATEDLINEITEM_H
