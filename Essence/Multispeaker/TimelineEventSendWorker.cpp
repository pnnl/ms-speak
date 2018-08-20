//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: TimelineEventSendWorker
//

#include <QTcpSocket>

#include "TimelineEventSendWorker.h"
#include "WsdlFile.h"

//------------------------------------------------------------------------------
// TimelineEventSendWorker
//
TimelineEventSendWorker::TimelineEventSendWorker(const QHostAddress& hostAddress, int hostPort, TimelineEvent& e, QObject* parent)
  : QObject(parent),
  m_hostAddress(hostAddress),
  m_hostPort(hostPort),
  m_timelineEvent(e)
{
}
//------------------------------------------------------------------------------
// ~TimelineEventSendWorker
//
TimelineEventSendWorker::~TimelineEventSendWorker()
{
}
//------------------------------------------------------------------------------
// PerformFinishedCleanup
//
void TimelineEventSendWorker::PerformFinishedCleanup(QTcpSocket* socket)
{
  socket->close();
  socket->deleteLater();
  emit Finished();
}
//------------------------------------------------------------------------------
// OnConnected
//
void TimelineEventSendWorker::OnConnected()
{
  if (QTcpSocket* socket = qobject_cast<QTcpSocket*>(sender()))
  {
    QByteArray content = WsdlFile::XmlSoap(m_timelineEvent.Host(), m_timelineEvent.Method(), m_timelineEvent.Doc());
    QDataStream os(socket);
    os.setByteOrder(QDataStream::BigEndian); // network byte order
    os << (qint32) m_timelineEvent.SrcHostId();
    os << (qint32) m_timelineEvent.DstHostId();
    os << (qint32) content.size();
    os << content;
    if (!socket->waitForBytesWritten())
      emit Error(socket->error(), socket->errorString());
    PerformFinishedCleanup(socket);
  }
}
//------------------------------------------------------------------------------
// OnError
//
void TimelineEventSendWorker::OnError(QAbstractSocket::SocketError socketError)
{
  if (QTcpSocket* socket = qobject_cast<QTcpSocket*>(sender()))
  {
    emit Error(socketError, socket->errorString());
    PerformFinishedCleanup(socket);
  }
}
//------------------------------------------------------------------------------
// OnStart
//
// Start processing data.
void TimelineEventSendWorker::OnStart()
{
  QTcpSocket* socket = new QTcpSocket(this); // Create socket in new thread
  connect(socket, SIGNAL(connected()), this, SLOT(OnConnected()));
  connect(socket, SIGNAL(error(QAbstractSocket::SocketError)), this, SLOT(OnError(QAbstractSocket::SocketError)));

  socket->connectToHost(m_hostAddress, m_hostPort);
}
