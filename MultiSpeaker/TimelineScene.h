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
// Summary: TimelineScene.h
//-------------------------------------------------------------------------------

#ifndef TIMELINESCENE_H
#define TIMELINESCENE_H

#include <QApplication>
#include <QGraphicsScene>
#include <QList>
#include <QPair>
#include <QStandardItemModel>
#include <QTimer>

#include "DigitalClock.h"
#include "TimelineEvent.h"
#include "TimelineEventItem.h"

class QToolButton;

class TimelineScene : public QGraphicsScene
{
  Q_OBJECT
private:
  QGraphicsLineItem* m_clockLineItem;
  QWidget* m_parentWidget; // Widget used for owner of modal dialogs
  qreal m_zoomFactor;
  qreal m_xScaleConst;
  QStandardItemModel m_eventModel;
  QHash<int, TimelineEvent*> m_eventHash; // Lookup key is Event Id mem owned in m_events
  QHash<int, TimelineEventItem*> m_eventItemHash; // Lookup Kye is Event Id, mem ref only...mem owned by scene
  QHash<int, int> m_eventPairHash; // Lookup Associates Request / Response Event pairs
  QList<TimelineEvent*> m_events; // placed in order via timestamp Mem owned here
  int m_border;
  int m_currentIdx; // Current index of the events being played
  int m_timeSpan; // im ms
  int m_timeStampLastProcessed; // System Timestamp of last processed Event in ms
  int m_timeStampUserPause; // System Timestamp at time of pause in ms
  bool m_isRunning;

public:
  TimelineScene(QObject* parent=Q_NULLPTR);
  ~TimelineScene();

  void AppendTimelineEvent(TimelineEvent* te);

  void Clear();

  QStandardItemModel& EventModel() {return m_eventModel;}
  const QList<TimelineEvent*> Events() const {return m_events;}
  const QHash<int, int> EventPairs() const {return m_eventPairHash;}

  void InsertTimelineEventPair( TimelineEvent& request,  TimelineEvent& response);
  bool IsRunning() const {return m_isRunning;}
  static QString LogText(const TimelineEvent& e);
  int MaxTimeStamp() const; // in ms
  int NextTimelineEventId();
  TimelineEvent& PairedTimelineEvent(int id) const {return *m_eventHash.value(m_eventPairHash.value(id));}
  void RemoveItems(QList<QGraphicsItem*> items);
  void Reset();
  int SceneHeight() const;
  void SetParentWidget(QWidget* w) {m_parentWidget = w;}
  void SetTimelineEventPairHash(QHash<int, int> hash) {m_eventPairHash = hash;} // Used in deserialize
  void SetTimelineSpan(int timeSpan) { m_timeSpan = timeSpan; UpdateScene(); }
  void Start();
  void Stop();
  TimelineEvent& TimelineEventById(int id) {Q_ASSERT(m_eventHash.contains(id)); return *m_eventHash.value(id);}
  int TimelineSpan() const {return m_timeSpan;}
  void Update(bool doUpdateSceneItems, bool doUpdateListItems);
  void UpdateTimelineEventPair(const TimelineEvent& request, const TimelineEvent& response);
  qreal ZoomFactor() const { return m_zoomFactor; }

protected:
  virtual void dragEnterEvent(QGraphicsSceneDragDropEvent* e);
  virtual void dragMoveEvent(QGraphicsSceneDragDropEvent* e);
  virtual void dropEvent(QGraphicsSceneDragDropEvent* e);
  virtual void mouseMoveEvent(QGraphicsSceneMouseEvent* e);

private:
  void AppendTimelineEventItem(TimelineEvent* e);
  int BinarySearch(QList<TimelineEvent*> list, int first, int last, int timeStamp);

  void CalcConst() {CalcConst(sceneRect());}
  void CalcConst(const QRectF& sceneRect);
  QPixmap CreateEventIcon(int size, const QColor& color);

  int InsertTimelineEvent(const TimelineEvent& timelineEvent, bool doUpdate=true);

  qreal PixToX(qreal pix) {return (pix - m_border) / m_xScaleConst;}
  void UpdateEventModel();
  void UpdateScene();
  void UpdateTimelineEvent(const TimelineEvent& timelineEvent, bool doUpdateSceneItems=true, bool doUpdate=true);
  qreal XToPix(qreal x) {return (x * m_xScaleConst) + m_border;}
  
signals:
  void Error(const QString& msg);
  void EventProcessed(TimelineEvent& e);
  void EventUpdated(TimelineEvent& e);
  void TimelineMouseMove(int timeStamp); // in ms
  void TimeSpanChanged(int m_timeSpan); // in ms

private slots:
  void OnCalcSceneConst(const QRectF& sceneRect) {CalcConst(sceneRect);}
  void OnClear() {Clear();}
  void OnClockLineItemMove(int tics);
  void OnPause() { Stop(); }
  void OnPlay() {Start();}
  void OnReset() {Reset();}
  void OnProcessEvent();
  void OnZoomIn();
  void OnZoomOut();
  void OnZoomReset();

  friend TimelineEventItem;
};

//-------------------------------------------------------------------------------
// Timeline
//  Singleton
//
inline TimelineScene& Timeline() 
{
  // Static init will only be allocated once and dealloc when QApplication goes out of scope in main()
  static TimelineScene* STATIC_TIMELINE_SCENE = new TimelineScene(qApp);
  return *STATIC_TIMELINE_SCENE;
}

// Serializing methods
QDataStream & operator<< (QDataStream& stream, const TimelineScene& scene);
QDataStream & operator>> (QDataStream& stream, TimelineScene& scene);

#endif // TIMELINESCENE_H
