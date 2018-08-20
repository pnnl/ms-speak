//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  $Revision: $
//  $Date: $
//  $Author: $
//  Created By: Lance Irvine
//
//  Summary: DigitalClock
//

#ifndef DIGITALCLOCK_H
#define DIGITALCLOCK_H

#include <QLCDNumber>
#include <QTime>
#include <QTimer>

#include "Settings.h"
//#include "Timer.h"

class DigitalClock : public QLCDNumber
{
  Q_OBJECT
private:
  int m_res; // In ms
  int m_tics; // in m_res units
  QTimer* m_timer;

public:
  DigitalClock(QWidget* parent=0);
  DigitalClock(int res, QWidget* parent=0);
  ~DigitalClock();

  //void Reset() {m_timer->stop(); display(Timer().ToString());}
  void Reset() {m_timer->stop(); m_tics = 0; display(QTime(0,0,0,0).addMSecs(0).toString("h:mm:ss"));}
  void Start() {m_timer->start(m_res);}
  void Stop() {m_timer->stop();}

private slots:
  void OnShowTime() {display(QTime(0,0,0,0).addMSecs(++m_tics * m_res).toString("h:mm:ss"));}
};

#endif // DIGITALCLOCK_H
