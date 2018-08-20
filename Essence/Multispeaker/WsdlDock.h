//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: WsdlDock
//

#ifndef WSDLDOCK_H
#define WSDLDOCK_H

#include <QDockWidget>

class WsdlDock : public QDockWidget
{
  Q_OBJECT

public:
  WsdlDock(QWidget* parent=0);
  ~WsdlDock();

protected:
  virtual void paintEvent(QPaintEvent* e);

private:
  void InitDockTitleBar();
};

#endif // WSDLDOCK_H
