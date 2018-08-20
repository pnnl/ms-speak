//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: TimelineEvent
//

#ifndef TIMELINEEVENT_H
#define TIMELINEEVENT_H

#include <QDomDocument>
#include <QObject>

#include "Settings.h"

class TimelineEvent : public QObject
{
  Q_OBJECT
public:
  enum EventType {Request, Response};

private:
  QDomDocument m_doc;
  int m_dstHostId;
  QString m_host;
  int m_id;
  QString m_method;
  int m_srcHostId;
  int m_timeStamp;
  EventType m_type; // Request or Response

public:
  TimelineEvent(EventType type, int timeStamp, const QString& host, const QString& method, QDomDocument doc, QObject* parent=0);
  TimelineEvent(const TimelineEvent& e);
  ~TimelineEvent();

  void Copy(const TimelineEvent& e);
  QDomDocument Doc() const {return m_doc;}
  int DstHostId() const {return m_dstHostId;}

  QString Host() {return m_host;}
  const QString Host() const {return m_host;}

  int Id() const {return m_id;}

  QString Method() {return m_method;}
  const QString Method() const {return m_method;}

  void SetDstHostId(int id) {m_dstHostId = id;}
  void SetSrcHostId(int id) {m_srcHostId = id;}
  void SetTimeStamp(int ts) {m_timeStamp = ts;}

  int SrcHostId() const {return m_srcHostId;}
 
  int TimeStamp() const {return m_timeStamp;}
  EventType Type() const {return m_type;}
  QString TypeString(EventType type) const {return ((type == Request) ? JSON_REQUEST_TAG : JSON_RESPONSE_TAG);}
};

#endif // TIMELINEEVENT_H
