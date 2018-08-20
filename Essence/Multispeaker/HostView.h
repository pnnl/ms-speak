//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: HostView
//

#ifndef HOSTVIEW_H
#define HOSTVIEW_H

#include <QGraphicsView>

class HostView : public QGraphicsView
{
  Q_OBJECT

public:
protected:
private:
public:
  HostView(QWidget *parent);
  ~HostView();
public:
protected:
  virtual void keyReleaseEvent(QKeyEvent* e);
  virtual void resizeEvent(QResizeEvent* e);
private:
signals:
private slots:
};

#endif // HOSTVIEW_H
