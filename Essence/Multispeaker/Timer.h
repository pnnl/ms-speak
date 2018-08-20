//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  $Revision: $
//  $Date: $
//  $Author: $
//  Created By: Lance Irvine
//
//  Summary: Timer
//

#ifndef TIMER_H
#define TIMER_H

#include <QApplication>
#include <QDebug>
#include <QObject>
#include <QSettings>
#include <QTime>

const int MSECS_PER_HOUR = 3600000;
const int MSECS_PER_MIN = 60000;

class GlobalTimer : public QObject
{
  Q_OBJECT
private:
  int m_pausedTime; // Amount of time the timer was paused after m_startTime
  int m_skipForwardTime; // Amount of time the timer is to skip forward before playing
  int m_startTime; // Current time in ms when timer started
  int m_stopTime; // Current time in ms when timer last stopped

public:
  GlobalTimer(QObject* parent=0) : QObject(parent), m_pausedTime(0), m_skipForwardTime(0), m_startTime(0), m_stopTime(0) {}
  ~GlobalTimer() {}

  //-------------------------------------------------------------------------------
  int CurrentPausedTime(int currentTimeStamp) {return m_pausedTime + ((m_stopTime > 0) ? currentTimeStamp - m_stopTime : 0);}

  //-------------------------------------------------------------------------------
  void Reset() {m_skipForwardTime = 0; m_startTime = 0; m_pausedTime = 0; m_stopTime = 0;}

  //-------------------------------------------------------------------------------
  void SetStart(int ms) {Reset(); m_skipForwardTime = ms;}

  //-------------------------------------------------------------------------------
  void Start() 
  {
    int ts = TicsFromTimeInMSecs(QTime::currentTime());
    if (m_startTime == 0)
    {
      m_startTime = ts;
      m_pausedTime = 0;
    }
    else
    {
      m_pausedTime = m_pausedTime + ts - m_stopTime;
    }
    m_stopTime = 0; // reset for next pause
  }

  //-------------------------------------------------------------------------------
  void Stop() {m_stopTime = TicsFromTimeInMSecs(QTime::currentTime());}

  //-------------------------------------------------------------------------------
  static int TicsFromTimeInMSecs(const QTime& t) {return MSECS_PER_HOUR * t.hour() + MSECS_PER_MIN * t.minute() + 1000 * t.second() + t.msec();}

  //-------------------------------------------------------------------------------
  int TimeStamp() // in ms
  {
    if (m_startTime == 0)
      return 0;
    else 
    {
      int ts = TicsFromTimeInMSecs(QTime::currentTime());
      return (ts - m_startTime - (m_pausedTime + ((m_stopTime > 0) ? (ts - m_stopTime) : 0))) + m_skipForwardTime;
    }
  }

  //-------------------------------------------------------------------------------
  QString ToString() {return QTime(0,0,0,0).addMSecs(TimeStamp()).toString("h:mm:ss");}

  //-------------------------------------------------------------------------------
  QString ToStringS(int ts) {return QTime(0,0,0,0).addMSecs(ts).toString("h:mm:ss");}
  QString ToStringMS(int ts) {return QTime(0,0,0,0).addMSecs(ts).toString("h:mm:ss.zzz");}
};

//-------------------------------------------------------------------------------
// TimerRef
//  Singleton
//
inline GlobalTimer& Timer() 
{
  // Static init will only be allocated once and dealloc when QApplication goes out of scope in main()
  static GlobalTimer* STATIC_GLOBAL_TIMER = new GlobalTimer(qApp);
  return *STATIC_GLOBAL_TIMER;
}

#endif // TIMER_H
