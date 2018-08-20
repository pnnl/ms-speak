//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: TimelineScene
//

#include <QDebug>
#include <QDragEnterEvent>
#include <QDropEvent>
#include <QMimeData>
#include <QGraphicsLinearLayout>
#include <QGraphicsProxyWidget>
#include <QGraphicsRectItem>
#include <QGraphicsSceneDragDropEvent>
#include <QInputDialog>
#include <QToolButton>

#include "FunctionBlockListView.h"
#include "TimelineEventEditor.h"
#include "TimelineItem.h"
#include "TimelineScene.h"
#include "Timer.h"
#include "WebServiceInfo.h"
#include "WsdlFile.h"

const int BORDER_MARGIN = 1;
//const int TIME_MAX = 300;

//------------------------------------------------------------------------------
// TimelineScene
//
TimelineScene::TimelineScene(QObject* parent)
  : QGraphicsScene(parent),
  m_border(BORDER_MARGIN),
  m_currentIdx(0), 
  m_isRunning(false),
  m_parentWidget(0),
  //m_timelineClockForm(0),
  //m_timeMax(TIME_MAX),
  //m_timeMin(0),
  m_timeSpan(60000), // 1 minute
  m_timeStampLastProcessed(0),
  m_timeStampPause(0),
  m_xScaleConst(1.0)
{
  setSceneRect(1, 1, 1, 1); // arbitrary value just to init will be changed when view is resized
  connect(this, SIGNAL(sceneRectChanged(const QRectF&)), this, SLOT(OnCalcSceneConst(const QRectF&)));

  // Timeline
  TimelineItem* item = new TimelineItem();
  connect(this, SIGNAL(sceneRectChanged(const QRectF&)), item, SLOT(OnSceneRectChanged(const QRectF&)));
  connect(item, SIGNAL(MouseDoubleClicked()), this, SLOT(OnSceneScaleChangeRequest()));
  addItem(item);

  //// PlayPause Btn
  //m_playPauseBtn->setObjectName(QStringLiteral("PlayPauseBtn"));
  //m_playPauseBtn->setIcon(QIcon(QStringLiteral(":/MultiSpeaker/Resources/media-play-32.png")));
  //m_playPauseBtn->setPopupMode(QToolButton::DelayedPopup);
  //m_playPauseBtn->setAutoRaise(true);
  ////m_playPauseBtn->setStyleSheet("background-color: transparent; border-color: black");
  //connect(m_playPauseBtn, SIGNAL(clicked()), this, SLOT(OnPlayPauseClicked()));

  //// Reset Btn
  //m_resetBtn->setObjectName(QStringLiteral("ResetBtn"));
  //m_resetBtn->setIcon(QIcon(QStringLiteral(":/MultiSpeaker/Resources/undo.png")));
  //m_resetBtn->setPopupMode(QToolButton::DelayedPopup);
  //m_resetBtn->setAutoRaise(true);
  ////m_resetBtn->setStyleSheet("background-color: transparent");
  ////m_resetBtn->setStyleSheet("border-color: black");
  //m_resetBtn->hide();
  //connect(m_resetBtn, SIGNAL(clicked()), this, SLOT(OnResetClicked()));

  //QGraphicsProxyWidget* clockProxy = addWidget(m_clock);
  //QGraphicsProxyWidget* playPauseProxy = addWidget(m_playPauseBtn);
  //QGraphicsProxyWidget* resetProxy = addWidget(m_resetBtn);

  //QGraphicsLinearLayout* layout = new QGraphicsLinearLayout();
  //layout->addItem(playPauseProxy);
  //layout->addItem(clockProxy);
  //layout->addItem(resetProxy);

  //m_timelineClockForm = new QGraphicsWidget;
  //m_timelineClockForm->setLayout(layout);
  //addItem(m_timelineClockForm);
}
//------------------------------------------------------------------------------
// ~TimelineScene
//
TimelineScene::~TimelineScene()
{
  m_parentWidget = 0; // When the scene finally destructs (statically) then this widget is no longer valid
  Clear();
  foreach (QGraphicsItem* item, items())
    removeItem(item);
}
//------------------------------------------------------------------------------
// Clear
//
void TimelineScene::Clear()
{
  Reset();

  // Delete Graphics Items before TimelineEvents because Items have a ref to TimelineEvent
  foreach (QGraphicsItem* item, items())
  {
    if (TimelineEventItem* e = qgraphicsitem_cast<TimelineEventItem*>(item))
      removeItem(e);
  }

  m_eventPairHash.clear();
  m_eventHash.clear();

  qDeleteAll(m_events);
  m_events.clear();

  m_eventModel.clear();

  //delete m_timelineClockForm;
}
//------------------------------------------------------------------------------
// InsertTimelineEventPair
//
void TimelineScene::InsertTimelineEventPair(const TimelineEvent& request, const TimelineEvent& response)
{
  if (m_isRunning)
  {
    emit Error("Events may not be inserted while Scheduler is running.");
    return;
  }
  int reqId = InsertTimelineEvent(request, false);
  int resId = InsertTimelineEvent(response, false);
  m_eventPairHash.insert(reqId, resId);
  m_eventPairHash.insert(resId, reqId);

  QApplication::processEvents();
  UpdateEventModel();
}
//------------------------------------------------------------------------------
// InsertTimelineEvent
//
// Note: if this scheduler is currently running then there will have to be some logic
//  to handle the case where the inserted item's time slot is not in the future
//  i.e before current index then m_currentIdx will have to incremented
//  i.e. edge case where item is inserted to a location during the current timeout interval...maybe best
//  way to handle this is to make a single shot  
//
//  Returns the id of the timelineEvent
//
int TimelineScene::InsertTimelineEvent(const TimelineEvent& timelineEvent, bool doUpdate)
{
  TimelineEvent* e = new TimelineEvent(timelineEvent);
  m_eventHash.insert(e->Id(), e);
  int ts = e->TimeStamp();

  if (m_events.count() == 0)
    m_events.append(e);
  else
  {
    int idx = BinarySearch(m_events, 0, m_events.count()-1, ts) + 1;
    m_events.insert(idx, e);
  }

  // Add Item to scene
  TimelineEventItem* item = new TimelineEventItem(*e);
  connect(item, SIGNAL(MouseDoubleClicked(TimelineEvent&)), this, SIGNAL(EventUpdated(TimelineEvent&)));
  item->setPos(XToPix(ts), 200);
  addItem(item);

  if (doUpdate)
    UpdateEventModel();
  return e->Id();
}
//------------------------------------------------------------------------------
// RemoveItems
//
void TimelineScene::RemoveItems(QList<QGraphicsItem*> items)
{
  foreach (QGraphicsItem* item, items)
  {
    if (TimelineItem* ti = qgraphicsitem_cast<TimelineItem*>(item))
    {
      Q_UNUSED(ti);
      continue;
    }
    removeItem(item);
  }
}
//------------------------------------------------------------------------------
// Reset
//
void TimelineScene::Reset()
{
  m_timeStampPause = 0;
  m_timeStampLastProcessed = 0;
  if (m_parentWidget)
  {
    if (DigitalClock* clock = m_parentWidget->findChild<DigitalClock*>())
      clock->Reset();
  }
  m_currentIdx = 0;
}
//------------------------------------------------------------------------------
// Start
//
void TimelineScene::Start()
{
  if (DigitalClock* clock = m_parentWidget->findChild<DigitalClock*>())
    clock->Start();
  if (QToolButton* btn = m_parentWidget->findChild<QToolButton*>("ClearBtn"))
    btn->setEnabled(false);
  if (QToolButton* btn = m_parentWidget->findChild<QToolButton*>("PauseBtn"))
    btn->setEnabled(true);
  if (QToolButton* btn = m_parentWidget->findChild<QToolButton*>("PlayBtn"))
    btn->setEnabled(false);
  if (QToolButton* btn = m_parentWidget->findChild<QToolButton*>("ResetBtn"))
    btn->setEnabled(false);

  m_isRunning = true; 
  if (m_currentIdx < m_events.count())
  {
    int elapsed = m_timeStampPause - m_timeStampLastProcessed;
    int nextEventTimeSpan = m_events.at(m_currentIdx)->TimeStamp() - elapsed;
    qDebug() << m_timeStampLastProcessed << elapsed << m_events.at(m_currentIdx)->TimeStamp() << nextEventTimeSpan;
    m_timeStampPause = 0; // Reset;
    QTimer::singleShot(nextEventTimeSpan, this, SLOT(OnProcessEvent()));
  }
}
//------------------------------------------------------------------------------
// Stop
//
void TimelineScene::Stop() 
{
  if (m_isRunning)
    m_timeStampPause = Timer().TicsFromTimeInMSecs(QTime::currentTime());
  m_isRunning = false;

  if (DigitalClock* clock = m_parentWidget->findChild<DigitalClock*>())
    clock->Stop();
  if (QToolButton* btn = m_parentWidget->findChild<QToolButton*>("ClearBtn"))
    btn->setEnabled(true);
  if (QToolButton* btn = m_parentWidget->findChild<QToolButton*>("PauseBtn"))
    btn->setEnabled(false);
  if (QToolButton* btn = m_parentWidget->findChild<QToolButton*>("PlayBtn"))
    btn->setEnabled(true);
  if (QToolButton* btn = m_parentWidget->findChild<QToolButton*>("ResetBtn"))
    btn->setEnabled(true);
}
//------------------------------------------------------------------------------
// UpdateTimelineEventPair
//
void TimelineScene::UpdateTimelineEventPair(const TimelineEvent& request, const TimelineEvent& response)
{
  if (m_isRunning)
  {
    emit Error("Events may not be updated while Scheduler is running.");
    return;
  }
  UpdateTimelineEvent(request, false);
  UpdateTimelineEvent(response, false);

  QApplication::processEvents();
  UpdateEventModel();
}
//------------------------------------------------------------------------------
// dragEnterEvent
//
void TimelineScene::dragEnterEvent(QGraphicsSceneDragDropEvent* e)
{
  if (qobject_cast<FunctionBlockListView*>(e->source()))
    e->ignore();
  else
    e->accept();
}
//------------------------------------------------------------------------------
// dragMoveEvent
//
void TimelineScene::dragMoveEvent(QGraphicsSceneDragDropEvent* e)
{
  if (qobject_cast<FunctionBlockListView*>(e->source()))
    e->ignore();
  else
    e->accept();
}
//------------------------------------------------------------------------------
// dropEvent
//
void TimelineScene::dropEvent(QGraphicsSceneDragDropEvent* e)
{
  QByteArray encoded = e->mimeData()->data("application/x-qstandarditemmodeldatalist");
  QDataStream stream(&encoded, QIODevice::ReadOnly);

  int row, col;
  QMap<int,  QVariant> roleDataMap;
  stream >> row >> col >> roleDataMap;

  QString methodName = roleDataMap.value(Qt::DisplayRole).toString();
  QString hostName = roleDataMap.value(Qt::UserRole + 1).toString();
  int timeStamp = PixToX(e->scenePos().x());

  //HostMethod method(methodName, hostName);
  WsdlFile* wsdl = WsInfo().Wsdl(hostName);
  TimelineEvent reqEvent(TimelineEvent::Request, timeStamp, hostName, methodName, wsdl->MethodTemplateRequest(methodName));
  TimelineEvent resEvent(TimelineEvent::Response, timeStamp, hostName, methodName, wsdl->MethodTemplateResponse(methodName));
  TimelineEventEditor dlg(reqEvent, resEvent, m_parentWidget);
  if (dlg.exec())
  {
    reqEvent.Copy(dlg.Request());
    resEvent.Copy(dlg.Response());
    Timeline().InsertTimelineEventPair(reqEvent, resEvent);
    QGraphicsScene::dropEvent(e);
  }
}
//-------------------------------------------------------------------------------
// BinarySearch
//  returns the index of the list just before ts.
//  so if list contained (0,1,3,5,8,9) and ts was 6 then idx would be 3
//  Note it is not advisable to call this method when the list is empty...make sure at least one entry is in list.
//
int TimelineScene::BinarySearch(QList<TimelineEvent*> list, int first, int last, int timeStamp)
{
  Q_ASSERT(!list.isEmpty());
  int idx = 0;
  if (first > last)
  {
    idx = last;//-1; // Not found so use last index -- we will append
  }
  else
  {
    int mid = (first + last) / 2;
    if (timeStamp == list.at(mid)->TimeStamp())
    {
      idx = mid;
    }
    else
    {
      if (timeStamp < list.at(mid)->TimeStamp())
        idx = BinarySearch(list, first, mid-1, timeStamp);
      else
        idx = BinarySearch(list, mid+1, last, timeStamp);
    }
  }
  return idx;
}
//-------------------------------------------------------------------------------
// CalcConst
//
void TimelineScene::CalcConst(const QRectF& sceneRect)
{
  m_xScaleConst = (sceneRect.width()-(2*m_border)) / (qreal)m_timeSpan;
}
//------------------------------------------------------------------------------
// UpdateEventModel
//
void TimelineScene::UpdateEventModel()
{
  m_eventModel.clear();
  foreach (TimelineEvent* e, m_events)
  {
    QStandardItem* item = new QStandardItem(QString("%1 %2: %3")
      .arg((e->Type() == TimelineEvent::Request) ? "-->" : "<--")
      .arg(Timer().ToStringMS(e->TimeStamp()))
      .arg(e->Method()));
    item->setData(e->Id());
    m_eventModel.appendRow(item);
  }
}
//------------------------------------------------------------------------------
// UpdateTimelineEvent
//
void TimelineScene::UpdateTimelineEvent(const TimelineEvent& timelineEvent, bool doUpdate)
{
  // Remove the timelineEvent from the m_events list and reinsert at proper time loc
  TimelineEvent* te = (TimelineEvent*)&timelineEvent;
  m_events.removeAt(m_events.indexOf(te));
  int ts = timelineEvent.TimeStamp();

  if (m_events.count() == 0)
    m_events.append(te);
  else
  {
    int idx = BinarySearch(m_events, 0, m_events.count()-1, ts) + 1;
    m_events.insert(idx, te);
  }

  // Add Item to scene
  TimelineEventItem* item = new TimelineEventItem(*te);
  connect(item, SIGNAL(MouseDoubleClicked(TimelineEvent&)), this, SIGNAL(EventUpdated(TimelineEvent&)));
  item->setPos(XToPix(ts), 200);
  addItem(item);

  if (doUpdate)
  {
    UpdateEventModel();
    update();
  }
}
//------------------------------------------------------------------------------
// OnProcessEvent
//
// Called when the scehduler wants another event to be processed
//  This event will set the singleshot timer for the next event in the timeline
//  if there are any others to be processed.
//
void TimelineScene::OnProcessEvent() 
{
  if (!m_isRunning)
    return;

  TimelineEvent* timelineEvent = m_events.at(m_currentIdx);
  qDebug() << "ProcessEvent:" << m_currentIdx << timelineEvent->TimeStamp() << timelineEvent->Method();
  emit EventProcessed(*timelineEvent);
  m_timeStampLastProcessed = Timer().TicsFromTimeInMSecs(QTime::currentTime());
  qDebug() << "ProcessEvent:" << m_timeStampLastProcessed;

  // Queue up new event
  if (++m_currentIdx < m_events.count())
  {
    TimelineEvent* nextTimelineEvent = m_events.at(m_currentIdx);
    int ts = Timer().TimeStamp();

    qDebug() << "ProcessEvent: Next:" 
      << m_currentIdx << nextTimelineEvent->TimeStamp() 
      << nextTimelineEvent->Method() 
      << qMax(0, nextTimelineEvent->TimeStamp() - ts);

    QTimer::singleShot(qMax(0, nextTimelineEvent->TimeStamp() - timelineEvent->TimeStamp()), this, SLOT(OnProcessEvent()));
  }
}
//------------------------------------------------------------------------------
// OnSceneScaleChangeRequest
//
void TimelineScene::OnSceneScaleChangeRequest()
{
  m_timeSpan = QInputDialog::getInt(m_parentWidget, "Change Timeline Duration", "Time Span (sec)", m_timeSpan / 1000) * 1000;
  CalcConst();
}