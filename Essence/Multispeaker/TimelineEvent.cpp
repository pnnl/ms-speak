//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: TimelineEvent
//

#include "TimelineEvent.h"

int TIMELINE_EVENT_ID = 0;

//------------------------------------------------------------------------------
// TimelineEvent
//
TimelineEvent::TimelineEvent(EventType type, int timeStamp, const QString& host, const QString& method, QDomDocument doc, QObject* parent) 
  : QObject(parent), 
  m_doc(doc),
  m_dstHostId(0),
  m_host(host),
  m_id(++TIMELINE_EVENT_ID),
  m_method(method), 
  m_srcHostId(0),
  m_timeStamp(timeStamp),
  m_type(type)
{
}
//------------------------------------------------------------------------------
// TimelineEvent
//
TimelineEvent::TimelineEvent(const TimelineEvent& e) 
  : QObject(),
  m_doc(e.m_doc),
  m_dstHostId(e.m_dstHostId),
  m_host(e.m_host),
  m_id(e.m_id),
  m_method(e.m_method), 
  m_srcHostId(e.m_srcHostId),
  m_timeStamp(e.m_timeStamp),
  m_type(e.m_type)
{
}
//------------------------------------------------------------------------------
// ~TimelineEvent
//
TimelineEvent::~TimelineEvent()
{
}
//------------------------------------------------------------------------------
// Copy
//
void TimelineEvent::Copy(const TimelineEvent& e)
{
  m_doc = e.m_doc;
  m_dstHostId = e.m_dstHostId;
  m_host = e.m_host;
  m_id = e.m_id;
  m_method = e.m_method;
  m_srcHostId = e.m_srcHostId;
  m_timeStamp = e.m_timeStamp;
  m_type = e.m_type;
}