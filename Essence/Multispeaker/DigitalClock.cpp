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

#include "DigitalClock.h"

//------------------------------------------------------------------------------
// DigitalClock
//
DigitalClock::DigitalClock(QWidget* parent)
  : QLCDNumber(parent),
  m_res(1000),
  m_tics(0),
  m_timer(new QTimer())
{
  setSegmentStyle(Filled);
  setDigitCount(8);
  setPalette(Qt::black);
  QString style = "color: white; background-color: transparent";
  setStyleSheet(style);

  connect(m_timer, SIGNAL(timeout()), this, SLOT(OnShowTime()));
  display(QTime(0,0,0,0).addMSecs(0).toString("h:mm:ss"));
}
//------------------------------------------------------------------------------
// DigitalClock
//
DigitalClock::DigitalClock(int res, QWidget* parent)
  : QLCDNumber(parent),
  m_res(res),
  m_timer(new QTimer())
{
  setSegmentStyle(Filled);
  setDigitCount(8);
  setPalette(Qt::black);
  QString style = /*foreground-color: black;*/ "background-color: transparent";
  setStyleSheet(style);

  connect(m_timer, SIGNAL(timeout()), this, SLOT(OnShowTime()));
  display(QTime(0,0,0,0).addMSecs(0).toString("h:mm:ss"));
}
//------------------------------------------------------------------------------
// ~DigitalClock
//
DigitalClock::~DigitalClock()
{
  m_timer->stop();
  delete m_timer;
}
