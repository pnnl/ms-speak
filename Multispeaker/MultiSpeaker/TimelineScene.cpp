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
// Summary: TimelineScene.cpp
//-------------------------------------------------------------------------------

#include <QDebug>
#include <QDragEnterEvent>
#include <QDropEvent>
#include <QGraphicsLinearLayout>
#include <QGraphicsLineItem>
#include <QGraphicsProxyWidget>
#include <QGraphicsRectItem>
#include <QGraphicsSceneDragDropEvent>
#include <QGraphicsView>
#include <QInputDialog>
#include <QMimeData>
#include <QPainter>
#include <QPixmap>
#include <QTimer>
#include <QToolButton>

#include "FunctionBlockListView.h"
#include "Host.h"
#include "HostScene.h"
#include "Settings.h"
#include "TimelineEventEditor.h"
#include "TimelineScene.h"
#include "Timer.h"
#include "WebServiceInfo.h"
#include "WsdlFile.h"

const int BORDER_MARGIN = 0;
const int SCENE_HEIGHT = 60;

//------------------------------------------------------------------------------
// TimelineScene
//
TimelineScene::TimelineScene(QObject* parent)
  : QGraphicsScene(parent),
	m_clockLineItem(Q_NULLPTR),
	m_parentWidget(Q_NULLPTR),
	m_zoomFactor(1.0),
	m_xScaleConst(1.0),
	m_border(BORDER_MARGIN),
	m_currentIdx(0),
	m_timeSpan(60000), // 1 min
	m_timeStampLastProcessed(0),
	m_timeStampUserPause(0),
	m_isRunning(false)
{
	setSceneRect(1, 1, 1, 1); // arbitrary value just to init will be changed when view is resized
	connect(this, SIGNAL(sceneRectChanged(const QRectF&)), this, SLOT(OnCalcSceneConst(const QRectF&)));
}
//------------------------------------------------------------------------------
// ~TimelineScene
//
TimelineScene::~TimelineScene()
{
	m_parentWidget = Q_NULLPTR; // When the scene finally destructs (statically) then this widget is no longer valid
	Clear();
}
//------------------------------------------------------------------------------
// AppendTimelineEvent
//
// Used in deserialize
//
void TimelineScene::AppendTimelineEvent(TimelineEvent* te)
{
	int ts = te->TimeStamp();
	if (ts > m_timeSpan)
	{
		if (ts % 60000)
			m_timeSpan = (ts / 60000) + 1; // Round up to nearest minute
		else
			m_timeSpan = ts / 60000;
	}

	m_events.append(te);
	m_eventHash.insert(te->Id(), te);
	AppendTimelineEventItem(te);
}
//------------------------------------------------------------------------------
// Clear
//
void TimelineScene::Clear()
{
	Reset();

	m_eventModel.clear();
	clear(); // Clear the Scene
	m_eventItemHash.clear(); // Clear the ref to the scene

	m_eventPairHash.clear();
	m_eventHash.clear();

	// Do this last as this is where the memory is owned
	qDeleteAll(m_events);
	m_events.clear();
}
//------------------------------------------------------------------------------
// InsertTimelineEventPair
//
void TimelineScene::InsertTimelineEventPair( TimelineEvent& request,  TimelineEvent& response)
{
	if (m_isRunning)
	{
		emit Error("Events may not be inserted while Scheduler is running.");
		return;
	}
	int reqId=-2, resId=-2;

	if( request.IsEnabled() ){
		reqId = InsertTimelineEvent(request, false);
		request.HasBuddy(response.IsEnabled());
	}
	if( response.IsEnabled() ){
		resId = InsertTimelineEvent(response, false);
		response.HasBuddy(request.IsEnabled());
	}

	if( request.IsEnabled() )
		m_eventPairHash.insert(reqId, resId);
	if( response.IsEnabled() )
		m_eventPairHash.insert(resId, reqId);

	if( reqId !=-2 || resId !=-2 ){
		QApplication::processEvents();
		Update(true, true);
	}
}
//------------------------------------------------------------------------------
// LogText
//
QString TimelineScene::LogText(const TimelineEvent& e)
{
	return QString("%1: %2%3%4 %5")
	.arg(Timer().ToStringMS(e.TimeStamp()))
	.arg(Hosts().HostById(e.SrcHostId())->Name())
	.arg((e.Type() == TimelineEvent::Request) ? "-->" : "<--")
	.arg(Hosts().HostById(e.DstHostId())->Name())
	.arg(e.Method());
}
//------------------------------------------------------------------------------
// MaxTimeStamp
//
// Returns max timestamp in ms
//
int TimelineScene::MaxTimeStamp() const
{
	if (m_events.isEmpty())
		return 60000; // Return default of 1 min

	return m_events.last()->TimeStamp();
}
//------------------------------------------------------------------------------
// NextTimelineEventId
//
int TimelineScene::NextTimelineEventId()
{
	int id = 0;
	foreach (const TimelineEvent* e, m_events)
		id = qMax(id, e->Id());

	return id + 1;
}
//------------------------------------------------------------------------------
// RemoveItems - called when select/delete timelineevent
//
void TimelineScene::RemoveItems(QList<QGraphicsItem*> items)
{
	foreach (QGraphicsItem* item, items)
	{
		if (QGraphicsLineItem* clockLine = qgraphicsitem_cast<QGraphicsLineItem*>(item))
		{
			Q_UNUSED(clockLine);
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
	m_timeStampUserPause = 0;
	m_timeStampLastProcessed = 0;
	if (m_parentWidget)
	{
		if (DigitalClock* clock = m_parentWidget->findChild<DigitalClock*>())
			clock->Reset();
	}
	m_currentIdx = 0;
	if (m_clockLineItem)
	{
		removeItem(m_clockLineItem);
		delete m_clockLineItem;
		m_clockLineItem = Q_NULLPTR;
	}
	// Enable select and movement of items on reset...disabled after start
	foreach(QGraphicsItem* item, items())
	{
		if (TimelineEventItem* teItem = qgraphicsitem_cast<TimelineEventItem*>(item))
			teItem->setFlags(QGraphicsItem::ItemIsMovable | QGraphicsItem::ItemIsSelectable | QGraphicsItem::ItemSendsGeometryChanges);
	}

	// Update the processed background role for the items
	int count = m_eventModel.rowCount();
	for (int i = 0; i < count; ++i)
		m_eventModel.item(i)->setData(QColor(Qt::white), Qt::BackgroundRole);
}
//------------------------------------------------------------------------------
// SceneHeight
//
int TimelineScene::SceneHeight() const
{
	return SCENE_HEIGHT;
}
//------------------------------------------------------------------------------
// Start
//
void TimelineScene::Start()
{
	if (DigitalClock* clock = m_parentWidget->findChild<DigitalClock*>())
	{
		clock->Start();
		connect(clock, SIGNAL(Updated(int)), this, SLOT(OnClockLineItemMove(int)), Qt::UniqueConnection); // Unique won't dup connection
	}
	if (QToolButton* btn = m_parentWidget->findChild<QToolButton*>("ClearBtn"))
		btn->setEnabled(false);
	if (QToolButton* btn = m_parentWidget->findChild<QToolButton*>("PauseBtn"))
		btn->setEnabled(true);
	if (QToolButton* btn = m_parentWidget->findChild<QToolButton*>("PlayBtn"))
		btn->setEnabled(false);
	if (QToolButton* btn = m_parentWidget->findChild<QToolButton*>("ResetBtn"))
		btn->setEnabled(false);

	m_isRunning = true;

	// Disable movement of items while running...will be reset at Reset
	foreach(QGraphicsItem* item, items())
	{
		if (TimelineEventItem* teItem = qgraphicsitem_cast<TimelineEventItem*>(item))
			teItem->setFlags(Q_NULLPTR);
	}

	if (m_currentIdx < m_events.count())
	{
		int lastEventTimeStamp = (m_currentIdx) ? m_events.at(m_currentIdx - 1)->TimeStamp() : 0;
		int elapsed = m_timeStampUserPause - m_timeStampLastProcessed; // Get where in timeline paused based on system timestamps
		int nextEventTimeSpan = m_events.at(m_currentIdx)->TimeStamp() - lastEventTimeStamp - elapsed;
		//qDebug() << m_timeStampLastProcessed << elapsed << m_events.at(m_currentIdx)->TimeStamp() << nextEventTimeSpan;
		m_timeStampUserPause = 0; // Reset;
		QTimer::singleShot(nextEventTimeSpan, this, SLOT(OnProcessEvent()));
	}
	if (!m_clockLineItem)
	{
		m_clockLineItem = addLine(QLineF(0, 0, 0, height() - 1), QPen(COLOR_CLOCK_LINE, 3));
		m_clockLineItem->setPos(XToPix(0), 0);
		m_clockLineItem->setZValue(-1);
	}
}
//------------------------------------------------------------------------------
// Stop
//
void TimelineScene::Stop() 
{
	if (m_isRunning)
		m_timeStampUserPause = Timer().TicsFromTimeInMSecs(QTime::currentTime());

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
// Update
//
void TimelineScene::Update(bool doUpdateSceneItems, bool doUpdateListItems)
{
	if (doUpdateListItems)
		UpdateEventModel();
	if (doUpdateSceneItems)
		UpdateScene();
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
	UpdateScene();
}
//------------------------------------------------------------------------------
// dragEnterEvent
//
void TimelineScene::dragEnterEvent(QGraphicsSceneDragDropEvent* e)
{
	int timeStamp = PixToX(e->scenePos().x());
	emit TimelineMouseMove(timeStamp);

	if ((qobject_cast<FunctionBlockListView*>(e->source())) || m_isRunning)
		e->ignore();
	else
		e->accept();
	}
//------------------------------------------------------------------------------
// dragMoveEvent
//
void TimelineScene::dragMoveEvent(QGraphicsSceneDragDropEvent* e)
{
	int timeStamp = PixToX(e->scenePos().x());
	emit TimelineMouseMove(timeStamp);

	if ((qobject_cast<FunctionBlockListView*>(e->source())) || m_isRunning)
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
	int timeStamp = qRound((PixToX(e->scenePos().x()) / 1000)) * 1000; // Round to nearest second

	WsdlFile* wsdl = WsInfo().Wsdl(hostName);
	int id = NextTimelineEventId(); // Get the current max Id in TimelineScene
	TimelineEvent reqEvent(id, TimelineEvent::Request, timeStamp, hostName, methodName, wsdl->MethodTemplateRequest(methodName), wsdl->NamespaceByPrefix(STR_NAMESPACE_PREFIX_TNS));
	TimelineEvent resEvent(id+1, TimelineEvent::Response, timeStamp + 500, hostName, methodName, wsdl->MethodTemplateResponse(methodName), wsdl->NamespaceByPrefix(STR_NAMESPACE_PREFIX_TNS));
	TimelineEventEditor dlg(reqEvent, resEvent, m_parentWidget);
	if (dlg.exec())
	{
		reqEvent.Copy(dlg.Request());
		resEvent.Copy(dlg.Response());// ui.ResponseMethodView
		Timeline().InsertTimelineEventPair(reqEvent, resEvent);
		QGraphicsScene::dropEvent(e);
	}
}
//-------------------------------------------------------------------------------
// mouseMoveEvent
//
//
void TimelineScene::mouseMoveEvent(QGraphicsSceneMouseEvent* e)
{
	QGraphicsScene::mouseMoveEvent(e);
	int timeStamp = PixToX(e->scenePos().x());
	emit TimelineMouseMove(timeStamp);
}
//-------------------------------------------------------------------------------
// AppendTimelineEventItem
//
void TimelineScene::AppendTimelineEventItem(TimelineEvent* e)
{
	// Add Item to scene
	TimelineEventItem* item = new TimelineEventItem(*e);
	connect(item, SIGNAL(MouseDoubleClicked(TimelineEvent&)), this, SIGNAL(EventUpdated(TimelineEvent&)));
	addItem(item);

	item->setPos(XToPix(e->TimeStamp()), 0);
	m_eventItemHash.insert(e->Id(), item);
	// Set this AFTER initial setPos otherwise stack overflow will occur in TimelineEventItem::itemChange
	item->setFlag(QGraphicsItem::ItemSendsGeometryChanges, true);
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
	if (m_events.count())
		m_timeSpan = qMax(m_events.last()->TimeStamp(), m_timeSpan);

	m_xScaleConst = (sceneRect.width()-(2*m_border)) / static_cast <qreal>(m_timeSpan);
}
//------------------------------------------------------------------------------
// CreateEventIcon
//
QPixmap TimelineScene::CreateEventIcon(int size, const QColor& color)
{
	QPixmap pix(size, size);
	pix.fill(Qt::transparent);
	QPainter p(&pix);
	p.setRenderHint(QPainter::Antialiasing);
	p.setBrush(color);
	p.drawRoundedRect(size / 2 - 3, 0, 5, size - 1, 2, 2);
	return pix;
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
		int idx = BinarySearch(m_events, 0, m_events.count() - 1, ts) + 1;
		m_events.insert(idx, e);
	}

	if (ts > m_timeSpan)
	{
		if (ts % 60000)
			m_timeSpan = ((ts / 60000) + 1) * 60000; // Round up to nearest minute
		else
			m_timeSpan = ts;

		emit TimeSpanChanged(m_timeSpan);
	}


	AppendTimelineEventItem(e);

	if (doUpdate)
		UpdateEventModel();
	return e->Id();
}
//------------------------------------------------------------------------------
// UpdateEventModel
//
void TimelineScene::UpdateEventModel()
{
	QPixmap reqPix = CreateEventIcon(10, COLOR_REQUEST);
	QPixmap resPix = CreateEventIcon(10, COLOR_RESPONSE);

	// Update Table
	m_eventModel.clear(); // Clear QStandardItems
	foreach (TimelineEvent* e, m_events)
	{
		QStandardItem* tableItem = new QStandardItem(LogText(*e));
		tableItem->setData(e->Id());
		tableItem->setData((e->Type() == TimelineEvent::Request) ? reqPix : resPix, Qt::DecorationRole);
		m_eventModel.appendRow(tableItem);
	}
}
//------------------------------------------------------------------------------
// UpdateScene
//
void TimelineScene::UpdateScene()
{
	CalcConst();
	// Update TimelineEventItem Positions
	foreach (QGraphicsItem* item, items())
	{
		if (TimelineEventItem* teItem = qgraphicsitem_cast<TimelineEventItem*>(item))
		{
			teItem->setFlag(QGraphicsItem::ItemSendsGeometryChanges, false);
			teItem->setPos(XToPix(teItem->TimelineEventRef().TimeStamp()), 0);
			teItem->setFlag(QGraphicsItem::ItemSendsGeometryChanges, true);
		}
	}
}
//------------------------------------------------------------------------------
// UpdateTimelineEvent
//
void TimelineScene::UpdateTimelineEvent(const TimelineEvent& timelineEvent, bool doUpdateSceneItems, bool doUpdate)
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

	if (doUpdate)
	{
		UpdateEventModel();
		if (doUpdateSceneItems)
			UpdateScene();
		update();
	}
}
//------------------------------------------------------------------------------
// OnClockLineItemMove
//
//  Tic is in whatever res the digital clock is...typically in seconds
void TimelineScene::OnClockLineItemMove(int tics)
{
	if (m_clockLineItem)
		m_clockLineItem->setPos(QPointF(XToPix(tics * 1000), 0));
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

	// Mark this system timestamp as when this index was processed...needed for pause and restart
	m_timeStampLastProcessed = Timer().TicsFromTimeInMSecs(QTime::currentTime());

	TimelineEvent* timelineEvent = m_events.at(m_currentIdx);
	m_eventItemHash.value(timelineEvent->Id())->Animate();
	m_eventModel.item(m_currentIdx)->setData(COLOR_EVENT_PROCESSED, Qt::BackgroundRole);
	emit EventProcessed(*timelineEvent);

	// Queue up new event
	if (++m_currentIdx < m_events.count())
	{
		TimelineEvent* nextTimelineEvent = m_events.at(m_currentIdx);
		int ts = Timer().TimeStamp();
		Q_UNUSED(ts);
		QTimer::singleShot(qMax(0, nextTimelineEvent->TimeStamp() - timelineEvent->TimeStamp()), this, SLOT(OnProcessEvent()));
	}
}
//------------------------------------------------------------------------------
// OnZoomIn
//
void TimelineScene::OnZoomIn()
{
	m_zoomFactor *= 1.25;
	QList<QGraphicsView*> list = views();
	QGraphicsView* view = list.first();
	setSceneRect(1.0, 1.0, (view->width() * Timeline().ZoomFactor()) - 2.0, view->height() - 2.0);
	UpdateScene();
}
//------------------------------------------------------------------------------
// OnZoomOut
//
void TimelineScene::OnZoomOut() 
{
	m_zoomFactor = qMax(1.0, m_zoomFactor / 1.25);
	QList<QGraphicsView*> list = views();
	QGraphicsView* view = list.first();
	setSceneRect(1.0, 1.0, (view->width() * Timeline().ZoomFactor()) - 2.0, view->height() - 2.0);
	UpdateScene();
}
//------------------------------------------------------------------------------
// OnZoomReset
//
void TimelineScene::OnZoomReset() 
{
	m_zoomFactor = 1.0;
	QList<QGraphicsView*> list = views();
	QGraphicsView* view = list.first();
	setSceneRect(1.0, 1.0, (view->width() * Timeline().ZoomFactor()) - 2.0, view->height() - 2.0);
	UpdateScene();
}
//------------------------------------------------------------------------------
// << Serialize Write
//
QDataStream & operator<< (QDataStream& s, const TimelineScene& scene)
{
	qint32 version = 1;
	s << version;

	// Events
	s << static_cast <qint32>(scene.TimelineSpan());
	s << static_cast <qint32>(scene.Events().count());
	foreach (const TimelineEvent* e, scene.Events())
	{
		s << static_cast <qint32>(e->DstHostId());
		s << e->Host();
		s << static_cast <qint32>(e->Id());
		s << e->Method();
		s << static_cast <qint32>(e->SrcHostId());
		s << static_cast <qint64>(e->TimeStamp());
		s << static_cast <qint32>(e->Type());

		s << e->Doc().toByteArray();
	}
	// Event Pairs
	s << scene.EventPairs();

	return s;
}
//------------------------------------------------------------------------------
// >> Serialize Read
//
QDataStream & operator>> (QDataStream& s, TimelineScene& scene)
{
	qint32 version(0);
	qint32 count = 0;
	qint32 val32;
	qint64 val64;
	QString valStr;
	QByteArray bytes;

	s >> version;
	if (version == 1)
	{
		s >> val32; scene.SetTimelineSpan(val32);
		s >> count;
		for (int i = 0; i < count; ++i)
		{
			TimelineEvent* te = new TimelineEvent();
			s >> val32; te->SetDstHostId(val32);
			s >> valStr; te->SetHost(valStr);
			s >> val32; te->SetId(val32);
			s >> valStr; te->SetMethod(valStr);
			s >> val32; te->SetSrcHostId(val32);
			s >> val64; te->SetTimeStamp(val64);
			s >> val32; te->SetType((TimelineEvent::EventType) val32);
			s >> bytes; te->SetDoc(bytes);
			scene.AppendTimelineEvent(te);
		}

		QHash<int, int> hash;
		s >> hash;
		scene.SetTimelineEventPairHash(hash);
	}
	//else if (version == 2) // Future
	//{
	//}
	return s;
}
