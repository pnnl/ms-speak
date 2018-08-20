//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: TimelineEventSendWorker
//

#ifndef TIMELINEEVENTSENDWORKER_H
#define TIMELINEEVENTSENDWORKER_H

#include <QHostAddress>
#include <QObject>

#include "TimelineEvent.h"

class QTcpSocket;

class TimelineEventSendWorker : public QObject
{
  Q_OBJECT
private:
  QHostAddress m_hostAddress;
  int m_hostPort;
  TimelineEvent& m_timelineEvent;

public:
  TimelineEventSendWorker(const QHostAddress& hostAddress, int hostPort, TimelineEvent& e, QObject* parent=0);
  ~TimelineEventSendWorker();
public:
protected:
private:
  void PerformFinishedCleanup(QTcpSocket* socket);

signals:
  void Error(QAbstractSocket::SocketError socketError, const QString& errorStr);
  void Finished();

private slots:
  void OnConnected();
  void OnError(QAbstractSocket::SocketError socketError);
  void OnStart();
};

#endif // TIMELINEEVENTSENDWORKER_H
