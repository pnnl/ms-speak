//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: TimelineEventItem
//

#ifndef TIMELINEEVENTITEM_H
#define TIMELINEEVENTITEM_H

#include <QGraphicsObject>

#include "Settings.h"
#include "TimelineEvent.h"

class TimelineEventItem : public QGraphicsObject
{
  Q_OBJECT
public:
  enum {Type = UserType + GRAPH_TYPE_TIMELINE_EVENT};

private:
  QPainterPath m_path;
  TimelineEvent& m_timelineEvent;

public:
  TimelineEventItem(TimelineEvent& te, QGraphicsItem* parent=0);
  ~TimelineEventItem();

  virtual QRectF boundingRect() const {return m_path.boundingRect();}

  QString Name() const {return m_timelineEvent.Method();}

  virtual void paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* w);

  virtual QPainterPath shape() const {return m_path;}

  int TimeStamp() const {return m_timelineEvent.TimeStamp();;}
  virtual int type() const {return Type;}

protected:
  virtual void mouseDoubleClickEvent(QGraphicsSceneMouseEvent* e) {Q_UNUSED(e); emit MouseDoubleClicked(m_timelineEvent);}

signals:
  void MouseDoubleClicked(TimelineEvent& e);
};
#endif // TIMELINEEVENTITEM_H
