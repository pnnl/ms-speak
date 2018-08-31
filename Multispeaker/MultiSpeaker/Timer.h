/*-------------------------------------------------------------------------------

  Multi-Speak - Secure Protocol Enterprise Access Kit(MS_SPEAK)
  Copyright © 2018, Battelle Memorial Institute
  All rights reserved.
  1.	Battelle Memorial Institute (hereinafter Battelle) hereby grants permission to any person or
		entity lawfully obtaining a copy of this software and associated documentation files
		(hereinafter “the Software”) to redistribute and use the Software in source and binary forms,
		with or without modification.  Such person or entity may use, copy, modify, merge, publish,
		distribute, sublicense, and/or sell copies of the Software, and may permit others to do so,
		subject to the following conditions:
		•	Redistributions of source code must retain the above copyright notice, this list of
			conditions and the following disclaimers.
		•	Redistributions in binary form must reproduce the above copyright notice, this list of
			conditions and the following disclaimer in the documentation and/or other materials
			provided with the distribution.
		•	Other than as used herein, neither the name Battelle Memorial Institute or Battelle may
			be used in any form whatsoever without the express written consent of Battelle.

  2.	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
		OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
		AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL BATTELLE OR CONTRIBUTORS
		BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
		(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
		OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
		CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
		OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


  This material was prepared as an account of work sponsored by an agency of the United States Government.
  Neither the United States  Government nor the United States Department of Energy, nor Battelle, nor
  any of their employees, nor any jurisdiction or organization  that has cooperated in the development
  of these materials, makes any warranty, express or implied, or assumes any legal liability or
  responsibility for the accuracy, completeness, or usefulness or any information, apparatus, product,
  software, or process disclosed, or represents that its use would not infringe privately owned rights.
  Reference herein to any specific commercial product, process, or service by trade name, trademark,
  manufacturer, or otherwise does not necessarily constitute or imply its endorsement, recommendation, or
  favoring by the United States Government or any agency thereof, or Battelle Memorial Institute. The
  views and opinions of authors expressed herein do not necessarily state or reflect those of the
  United States Government or any agency thereof.
									 PACIFIC NORTHWEST NATIONAL LABORATORY
											    operated by
												  BATTELLE
											      for the
									  UNITED STATES DEPARTMENT OF ENERGY
									   under Contract DE-AC05-76RL01830


    This notice including this sentence must appear on any copies of this computer software.
*/
//-------------------------------------------------------------------------------
//	History
//		2017 - Created By: Lance Irvine.
//		2018 - Modified By: Carl Miller <carl.miller@pnnl.gov>
//-------------------------------------------------------------------------------
//
// Summary: Timer.h
//-------------------------------------------------------------------------------

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
