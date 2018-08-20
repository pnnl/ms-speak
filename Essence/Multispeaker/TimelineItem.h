//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: TimelineItem
//

#ifndef TIMELINEITEM_H
#define TIMELINEITEM_H

#include <QGraphicsObject>
#include <QGraphicsScene>

#include "Settings.h"

class TimelineItem : public QGraphicsObject
{
  Q_OBJECT
public:
  enum {Type = UserType + GRAPH_TYPE_TIMELINE};

private:
  int m_border; // The size of the border for this item...data is calc and drawn within this border
  int m_timeMax;
  int m_timeMin;
  int m_timeSpan;
  QList<qreal> m_timeTicMajor; 
  QStringList m_timeTicMajorLabels; 
  int m_timeTicMajorHeight;
  int m_timeTicMajorSpan;
  //QList<int> m_timeTicMinor;
  //int m_timeTicMinorHeight;
  //int m_timeTicMinorSpan;
  qreal m_xScaleConst;
  

public:
  TimelineItem(QGraphicsItem* parent=0);
  ~TimelineItem();

public:
  virtual QRectF boundingRect() const;
  virtual void paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* w);

  void SetTimeSpan(int min, int max) {m_timeMin = min; m_timeMax = max; m_timeSpan = max - min; CalcConst(); update();}

  virtual QPainterPath shape() const;
  virtual int type() const {return Type;}

protected:
  virtual void hoverLeaveEvent(QGraphicsSceneHoverEvent* e);
  virtual void hoverMoveEvent(QGraphicsSceneHoverEvent* e);
  virtual void mouseDoubleClickEvent(QGraphicsSceneMouseEvent* e) {Q_UNUSED(e); emit MouseDoubleClicked();}
  virtual void mouseMoveEvent(QGraphicsSceneMouseEvent* e);

private:
  void CalcConst() {CalcConst(scene()->sceneRect());}
  void CalcConst(const QRectF& sceneRect);
  void PaintTicsMajor(QPainter& p);
  //void PaintTicsMinor(QPainter& p);

  qreal XToPix(qreal x) {return (x * m_xScaleConst) + m_border;}
  //int XToPix(int x) {return qRound((qreal)x * m_xScaleConst);}
  qreal PixToX(qreal pix) {return (pix / m_xScaleConst) - m_border;}

signals:
  void MouseDoubleClicked();

private slots:
  void OnSceneRectChanged(const QRectF& sceneRect) {CalcConst(sceneRect);}
};

#endif // TIMELINEITEM_H
