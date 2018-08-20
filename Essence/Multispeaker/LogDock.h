//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: LogDock
//

#ifndef LOGDOCK_H
#define LOGDOCK_H

#include "ui_LogDock.h"

#include <QDockWidget>

#include "Timer.h"

class TimelineEvent;

class LogDock : public QDockWidget
{
  Q_OBJECT
private:
  Ui::LogDock ui;

public:
  LogDock(QWidget* parent=0);
  ~LogDock();

  void Append(const QString& msg) {Append(Timer().ToString(), msg);}
  void Append(const QString& timeStamp, const QString& msg);
  void Append(TimelineEvent& e);

protected:
  virtual void paintEvent(QPaintEvent* e);

private:
  void InitDockTitleBar();

signals:
private slots:
  void OnNotify(TimelineEvent& e) {Append(e);}
};

#endif // LOGDOCK_H
