//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: HostItem
//

#ifndef HOSTITEM_H
#define HOSTITEM_H

#include <QGraphicsObject>

#include "Host.h"
#include "Settings.h"

class AnimatedLineItem;

class HostItem : public QGraphicsObject
{
  Q_OBJECT
public:
  enum {Type = UserType + GRAPH_TYPE_HOST};

private:
  QList<AnimatedLineItem*> m_edges; // ref only...mem owned by scene
  Host& m_host;
  QPointF m_origin;

public:
  HostItem(Host& host, const QPointF& origin, QGraphicsItem* parent=0);
  ~HostItem();

  void AddEdge(AnimatedLineItem* edge) {m_edges.append(edge);}
  virtual QRectF boundingRect() const;

  const QList<AnimatedLineItem*> Edges() const {return m_edges;}
  int Id() const {return m_host.Id();}
  QString Name() const {return m_host.Name();}

  const QPointF& Origin() const {return m_origin;}

  virtual void paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* w);

  void RemoveEdge(AnimatedLineItem* edge) {if (m_edges.contains(edge)) m_edges.removeAll(edge);}

  static int Size();

  void SetId(int id) {m_host.SetId(id);}
  void SetName(const QString& name) {m_host.SetName(name);}
  virtual QPainterPath shape() const;

  QString ToolTip() const;

  virtual int type() const {return Type;}
  
protected:
  virtual QVariant itemChange(GraphicsItemChange change, const QVariant& value);
  virtual void mouseDoubleClickEvent(QGraphicsSceneMouseEvent* e) {Q_UNUSED(e); emit MouseDoubleClicked(Id());}
  virtual void mouseMoveEvent(QGraphicsSceneMouseEvent* e);
  virtual void hoverEnterEvent(QGraphicsSceneHoverEvent * e) {Q_UNUSED(e); setToolTip(ToolTip());}

signals:
  void MouseDoubleClicked(int id);
};

#endif // HOSTITEM_H
