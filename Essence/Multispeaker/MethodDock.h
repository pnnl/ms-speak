//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: MethodDock
//

#ifndef METHODDOCK_H
#define METHODDOCK_H

#include <QDockWidget>

class MethodDock : public QDockWidget
{
  Q_OBJECT

public:
  MethodDock(QWidget* parent);
  ~MethodDock();

protected:
  virtual void paintEvent(QPaintEvent* e);

private:
  void InitDockTitleBar();
};

#endif // METHODDOCK_H
