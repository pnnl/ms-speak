//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: TimelineScene
//

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
  int m_border;
  int m_currentIdx; // Current index of the events being played
  QStandardItemModel m_eventModel;
  QHash<int, TimelineEvent*> m_eventHash; // Lookup key is Event Id mem owned in m_events
  QHash<int, int> m_eventPairHash; // Lookup Associates Request / Response Event pairs
  QList<TimelineEvent*> m_events; // Mem owned here
  bool m_isRunning;

  QWidget* m_parentWidget; // Widget used for owner of modal dialogs
  //QGraphicsWidget* m_timelineClockForm;
  //int m_timeMax; // in ms
  //int m_timeMin; // in ms
  int m_timeSpan; // im ms
  int m_timeStampLastProcessed; // in ms
  int m_timeStampPause; // in ms
  qreal m_xScaleConst;
  
public:
  TimelineScene(QObject* parent=0);
  ~TimelineScene();

  void Clear();
  //DigitalClock* Clock() {return m_clock;}

  QStandardItemModel& EventModel() {return m_eventModel;}

  void InsertTimelineEventPair(const TimelineEvent& request, const TimelineEvent& response);
  bool IsRunning() const {return m_isRunning;}
  void RemoveItems(QList<QGraphicsItem*> items);
  void Reset();
  void SetParentWidget(QWidget* w) {m_parentWidget = w;}
  void Start();
  void Stop();
  TimelineEvent& PairedTimelineEvent(int id) const {return *m_eventHash.value(m_eventPairHash.value(id));}
  TimelineEvent& TimelineEventById(int id) {Q_ASSERT(m_eventHash.contains(id)); return *m_eventHash.value(id);}
  void UpdateTimelineEventPair(const TimelineEvent& request, const TimelineEvent& response);
  void UpdateViews() {UpdateEventModel();}

protected:
  virtual void dragEnterEvent(QGraphicsSceneDragDropEvent* e);
  virtual void dragMoveEvent(QGraphicsSceneDragDropEvent* e);
  virtual void dropEvent(QGraphicsSceneDragDropEvent* e);

private:
  int BinarySearch(QList<TimelineEvent*> list, int first, int last, int timeStamp);

  void CalcConst() {CalcConst(sceneRect());}
  void CalcConst(const QRectF& sceneRect);

  int InsertTimelineEvent(const TimelineEvent& timelineEvent, bool doUpdate=true);

  qreal PixToX(qreal pix) {return (pix / m_xScaleConst) - m_border;}
  void UpdateEventModel();
  void UpdateTimelineEvent(const TimelineEvent& timelineEvent, bool doUpdate=true);
  qreal XToPix(qreal x) {return (x * m_xScaleConst) + m_border;}
  
signals:
  void Error(const QString& msg);
  void EventProcessed(TimelineEvent& e);
  void EventUpdated(TimelineEvent& e);

private slots:
  void OnCalcSceneConst(const QRectF& sceneRect) {CalcConst(sceneRect);}
  void OnClear() {Clear();}
  void OnPause() {Stop();}
  void OnPlay() {Start();}
  void OnReset() {Reset();}
  void OnProcessEvent();
  void OnSceneScaleChangeRequest();
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

#endif // TIMELINESCENE_H
