//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: TimelineView
//

#ifndef TIMELINEVIEW_H
#define TIMELINEVIEW_H

#include <QGraphicsView>

#include "TimelineScene.h"

class TimelineView : public QGraphicsView
{
  Q_OBJECT
private:

public:
  TimelineView(QWidget* parent=0);
  ~TimelineView();

protected:
  virtual void keyReleaseEvent(QKeyEvent* e);
  virtual void resizeEvent(QResizeEvent* e) {scene()->setSceneRect(1, 1, width()-2, height()-2); QGraphicsView::resizeEvent(e);}
};

#endif // TIMELINEVIEW_H
