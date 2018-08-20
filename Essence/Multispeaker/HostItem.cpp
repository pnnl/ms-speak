//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: HostItem
//

#include <QGraphicsScene>
#include <QGraphicsSceneDragDropEvent>
#include <QGraphicsSceneMouseEvent>
#include <QPainter>

#include "AnimatedLineItem.h"
#include "HostItem.h"
#include "HostScene.h"
#include "WebServiceInfo.h"

const int NODE_SIZE = 50;

const QString TOOL_TIP = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\"><html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">p, li { white-space: pre-wrap; }</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\"><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">TokenLong</span></p><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ID: TokenId</p><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Apache: TokenApache</p><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Firefox: TokenFireFox</p><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Wireshark: TokenWireshark</p><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Terminal: TokenTerminal</p><p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>";

//------------------------------------------------------------------------------
// HostItem
//
HostItem::HostItem(Host& host, const QPointF& origin, QGraphicsItem* parent)
  : QGraphicsObject(parent),
  m_host(host),
  m_origin(origin)
{
  setPos(origin.x() - (qreal)NODE_SIZE / 2.0, origin.y() - (qreal)NODE_SIZE / 2.0);
  setAcceptDrops(true);
  setAcceptHoverEvents(true);
  setFlags(QGraphicsItem::ItemIsSelectable | QGraphicsItem::ItemIsMovable | QGraphicsItem::ItemSendsGeometryChanges);
  setZValue(10);
  setToolTip(ToolTip());
}
//------------------------------------------------------------------------------
// ~HostItem
//
HostItem::~HostItem()
{
}
//------------------------------------------------------------------------------
// boundingRect
//
QRectF HostItem::boundingRect() const
{
  return QRectF(0,0,NODE_SIZE,NODE_SIZE);
}
//------------------------------------------------------------------------------
// Size
//
int HostItem::Size()
{
  return NODE_SIZE;
}
//------------------------------------------------------------------------------
// shape
//
QPainterPath HostItem::shape() const
{
  QPainterPath path;
  path.addRect(QRectF(0,0,NODE_SIZE,NODE_SIZE));
  return path;
}
//------------------------------------------------------------------------------
// ToolTip
//
QString HostItem::ToolTip() const
{
  QString tip = TOOL_TIP;
  //tip.replace("TokenShort", m_host.Name());
  tip.replace("TokenLong", WsInfo().FullNameDashSep(m_host.Name()));
  tip.replace("TokenId", QString::number(m_host.Id()));
  tip.replace("TokenApache", (m_host.AppFlag(Host::Apache)) ? "Yes" : "No");
  tip.replace("TokenFireFox", (m_host.AppFlag(Host::FireFox)) ? "Yes" : "No");
  tip.replace("TokenWireshark", (m_host.AppFlag(Host::WireShark)) ? "Yes" : "No");
  tip.replace("TokenTerminal", (m_host.AppFlag(Host::Terminal)) ? "Yes" : "No");
  return tip;
}
//------------------------------------------------------------------------------
// paint
//
void HostItem::paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* w)
{
  Q_UNUSED(option);
  Q_UNUSED(w);
  QPixmap pix = Hosts().CreateHostPixmap(m_host, NODE_SIZE, isSelected());
  painter->drawPixmap(0, 0, NODE_SIZE, NODE_SIZE, pix);
}

//------------------------------------------------------------------------------
// itemChange
//
QVariant HostItem::itemChange(GraphicsItemChange change, const QVariant& value)
{
  if (change == QGraphicsItem::ItemPositionChange) 
  {
    m_origin = pos() + QPointF(NODE_SIZE/2, NODE_SIZE/2);    
    foreach (AnimatedLineItem* edge, m_edges) 
      edge->UpdatePosition();
    scene()->update();
  }
  else if (change == QGraphicsItem::ItemSelectedHasChanged)
  {
    if (value.toBool())
      qDebug() << "Item Selected:" << Name();
  }

  return value;
}
//------------------------------------------------------------------------------
// mouseMoveEvent
//
void HostItem::mouseMoveEvent(QGraphicsSceneMouseEvent* e)
{
  QGraphicsItem::mouseMoveEvent(e); // move the item...

  // ...then check the bounds
  if (x() < 0)
      setPos(0, y());
  else if (x() > scene()->sceneRect().width())
      setPos(scene()->sceneRect().width(), y());

  if (y() < 0)
      setPos(x(), 0);
  else if (y() > scene()->sceneRect().height())
      setPos(x(), scene()->sceneRect().height());
}
