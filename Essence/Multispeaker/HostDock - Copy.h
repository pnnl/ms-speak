//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: HostDock
//

#ifndef HOSTDOCK_H
#define HOSTDOCK_H

#include <QDockWidget>

class HostDock : public QDockWidget
{
  Q_OBJECT
private:
  Ui::HostDock ui;
  int m_srcId;

public:
  HostDock(int srcId, const QString& name, QWidget* parent=0);
  ~HostDock();

  int Id() const {return m_srcId;}

protected:
  virtual void closeEvent(QCloseEvent* e) {Q_UNUSED(e); emit Close(m_srcId);}
  virtual void paintEvent(QPaintEvent* e);

private:
  void InitDockTitleBar();

signals:
  void Close(int);

public slots:
  void Update();

};

#endif // HOSTDOCK_H
