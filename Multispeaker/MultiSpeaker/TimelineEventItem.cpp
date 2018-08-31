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
// Summary: TimelineEventItem.cpp
//-------------------------------------------------------------------------------

#include <QCursor>
#include <QDebug>
#include <QPainter>

#include "Settings.h"
#include "TimelineEventItem.h"
#include "TimelineScene.h"

const int HEIGHT = TIMELINE_SCENE_HEIGHT - 20;

//------------------------------------------------------------------------------
// TimelineEventItem
//
TimelineEventItem::TimelineEventItem(TimelineEvent& te, QGraphicsItem* parent)
  : QGraphicsObject(parent),
	m_doAnimate(false),
	m_timelineEvent(te)
{
	setToolTip(TimelineScene::LogText(te));
	setFlags(QGraphicsItem::ItemIsMovable | QGraphicsItem::ItemIsSelectable);
	setCursor(Qt::PointingHandCursor);

	if (te.Type() == TimelineEvent::Request)
		m_path.addRoundedRect(-2, 2, 5, (HEIGHT * 0.80) - 2, 2, 2);
	else if (te.Type() == TimelineEvent::Response)
		m_path.addRoundedRect(-2, 2 + (HEIGHT * 0.20), 5, (HEIGHT * 0.80) - 2, 2, 2);
}
//------------------------------------------------------------------------------
// ~TimelineEventItem
//
TimelineEventItem::~TimelineEventItem()
{
}
//------------------------------------------------------------------------------
// Animate
//
void TimelineEventItem::Animate(bool doAnimate) 
{
	m_doAnimate = doAnimate;
	update();
	QTimer::singleShot(500, this, SLOT(OnAnimateQuit())); // show "Animated" State for 500 ms
	}
//------------------------------------------------------------------------------
// paint
//
void TimelineEventItem::paint(QPainter* p, const QStyleOptionGraphicsItem* option, QWidget* w)
{
	Q_UNUSED(option);
	Q_UNUSED(w);

	p->setRenderHint(QPainter::Antialiasing, true);

	// Draw Selection
	if (m_timelineEvent.Type() ==  TimelineEvent::Request)
		p->setBrush(COLOR_REQUEST);
	else if (m_timelineEvent.Type() == TimelineEvent::Response)
		p->setBrush(COLOR_RESPONSE);

	if (m_doAnimate)
	{
		p->setPen(QPen(Qt::black, 2));
		p->setBrush(QColor(0, 255, 0));
	}
	else if (isSelected())
	{
		p->setPen(QPen(Qt::magenta, 2, Qt::DashLine));
	}
	else
	{
		p->setPen(QPen(Qt::black, 0));
	}

	p->drawPath(m_path);
}
//------------------------------------------------------------------------------
// itemChange
//
QVariant TimelineEventItem::itemChange(GraphicsItemChange change, const QVariant& value)
{
	if (change == QGraphicsItem::ItemPositionChange)
	{
		// Round to nearest 1 sec
		QPointF newPos = value.toPointF();

		int timeSpan = Timeline().TimelineSpan();
		int ts = qRound(Timeline().PixToX(qBound(0.0, newPos.x(), Timeline().XToPix(timeSpan))) / 1000) * 1000;

		if( m_timelineEvent.HasBuddy() )
		{
			TimelineEvent& buddyEvent = Timeline().PairedTimelineEvent(m_timelineEvent.Id());
			int offset = qAbs(buddyEvent.TimeStamp() - m_timelineEvent.TimeStamp()); // Get old offset

			// Make sure the movement stays on the timeline bounds
			if (m_timelineEvent.Type() == TimelineEvent::Request)
			{
				ts = qBound(0, ts, timeSpan - offset);
				m_timelineEvent.SetTimeStamp(ts);
				buddyEvent.SetTimeStamp(ts + offset);
			}
			else
			{
				ts = qBound(offset, ts, timeSpan);
				m_timelineEvent.SetTimeStamp(ts);
				buddyEvent.SetTimeStamp(ts - offset);
			}
		}
		else{
			int offset = 0;
			if (m_timelineEvent.Type() == TimelineEvent::Request)
			{
				ts = qBound(0, ts, timeSpan - offset);
				m_timelineEvent.SetTimeStamp(ts);
			}
			else
			{
				ts = qBound(offset, ts, timeSpan);
				m_timelineEvent.SetTimeStamp(ts);
			}
		}
		return QPointF(Timeline().XToPix(ts), 0);
	}
	else if (change == ItemPositionHasChanged)
	{
		if( m_timelineEvent.HasBuddy() )
		{
			TimelineEvent& buddyEvent = Timeline().PairedTimelineEvent(m_timelineEvent.Id());
			TimelineEventItem* buddyItem = Timeline().m_eventItemHash.value(buddyEvent.Id());

			int offset = qAbs(buddyEvent.TimeStamp() - m_timelineEvent.TimeStamp()); // Get old offset

			//QPointF newPos = value.toPointF();
			//int ts = qRound(Timeline().PixToX(qBound(0.0, newPos.x(), Timeline().XToPix(Timeline().TimelineSpan()))) / 1000) * 1000;
			int ts = m_timelineEvent.TimeStamp();
			int buddyTs = (m_timelineEvent.Type() == TimelineEvent::Request) ? (ts + offset) : (ts - offset);

			m_timelineEvent.SetTimeStamp(ts);
			buddyEvent.SetTimeStamp(buddyTs);

			// Prevent stack overflow before setting pos
			setFlag(QGraphicsItem::ItemSendsGeometryChanges, false);
			buddyItem->setFlag(QGraphicsItem::ItemSendsGeometryChanges, false);

			setPos(Timeline().XToPix(ts), 0);
			setToolTip(TimelineScene::LogText(TimelineEventRef()));
			buddyItem->setPos(Timeline().XToPix(buddyTs), 0);
			buddyItem->setToolTip(TimelineScene::LogText(buddyItem->TimelineEventRef()));

			Timeline().UpdateTimelineEvent(m_timelineEvent, false);
			Timeline().UpdateTimelineEvent(buddyEvent, false);

			// Restore ability for this method, itemChange, to be called on an item move
			setFlag(QGraphicsItem::ItemSendsGeometryChanges, true);
			buddyItem->setFlag(QGraphicsItem::ItemSendsGeometryChanges, true);
		}
		else{
			int ts = m_timelineEvent.TimeStamp();
			m_timelineEvent.SetTimeStamp(ts);
			// Prevent stack overflow before setting pos
			setFlag(QGraphicsItem::ItemSendsGeometryChanges, false);
			setPos(Timeline().XToPix(ts), 0);
			setToolTip(TimelineScene::LogText(TimelineEventRef()));
			Timeline().UpdateTimelineEvent(m_timelineEvent, false);
			// Restore ability for this method, itemChange, to be called on an item move
			setFlag(QGraphicsItem::ItemSendsGeometryChanges, true);
		}
	}
	return value;
}
