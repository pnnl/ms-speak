//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: ServerWorker
//
#include <QHostAddress>

#include "ServerWorker.h"

//------------------------------------------------------------------------------
// ServerWorker
//
ServerWorker::ServerWorker(qintptr socketDescriptor, QObject* parent)
  : QObject(parent),
  m_bufferSize(0),
  m_bytesRead(0),
  m_dstId(0),
  m_headerRead(false),
  m_headerSize(3*sizeof(quint32)),
  m_srcId(0),
  m_socketDescriptor(socketDescriptor)
{
}
//------------------------------------------------------------------------------
// ~ServerWorker
//
ServerWorker::~ServerWorker()
{
}
//------------------------------------------------------------------------------
// ReadMessage
//
void ServerWorker::ReadMessage(QTcpSocket* socket)
{
  qDebug() << "Bytes Available:" << socket->bytesAvailable();
  if (socket->bytesAvailable() >= m_headerSize && !m_headerRead)
  {
    QDataStream in(socket);
    in.setByteOrder(QDataStream::BigEndian); // network byte order
    //in.setVersion(QDATASTREAM_VERSION);
    in >> m_srcId;
    in >> m_dstId;
    in >> m_bufferSize;
    qDebug() << "SrcId:" << m_srcId << "DstId:" << m_dstId << "BufferSize: " << m_bufferSize;
  }

  if (m_bufferSize == 0)
    return;

  QByteArray block = socket->readAll();
  m_buffer.append(block);
  m_bytesRead += block.size();

  if (m_bytesRead >= m_bufferSize)
  {
    // Get incoming Message
    QByteArray block;
    QDataStream in(m_buffer);
    in.setByteOrder(QDataStream::BigEndian); // network byte order
    //in.setVersion(QDATASTREAM_VERSION);

    in >> block;
    //qDebug() << block.count() << block;
    emit Message(m_srcId, m_dstId, block);
  }
}
//------------------------------------------------------------------------------
// OnError
//
void ServerWorker::OnError(QAbstractSocket::SocketError socketError)
{
  // Don't care about the remote host closed error as the client will normally
  //  close when response message receieved 
  if (socketError != QAbstractSocket::RemoteHostClosedError)
  {
    if (QTcpSocket* socket = qobject_cast<QTcpSocket*>(sender()))
    {
      emit Error(socketError);
      emit Finished();
    }
  }
}
//------------------------------------------------------------------------------
// OnReadyRead
//
// slot called when the socket has bytes to read
//
void ServerWorker::OnReadyRead() 
{
  if (QTcpSocket* socket = qobject_cast<QTcpSocket*>(sender()))
  {
    ReadMessage(socket);
  }
}
//------------------------------------------------------------------------------
// OnSocketDisconnected
//
//  When the socket has completed sending data back to the client the client will
//  Disconnenct from host causing the 'disconnected' signal to fire back to here.  At 
//  This point the socket can be closed / deleted and the thread can be cleaned up
//  
//
void ServerWorker::OnSocketDisconnected()
{
  if (QTcpSocket* socket = qobject_cast<QTcpSocket*>(sender()))
    socket->deleteLater();
  emit Finished();
}
//------------------------------------------------------------------------------
// OnStart
//
// Start processing data.
void ServerWorker::OnStart()
{
  QTcpSocket* socket = new QTcpSocket(this); // Create socket in new thread
  connect(socket, SIGNAL(error(QAbstractSocket::SocketError)), this, SLOT(OnError(QAbstractSocket::SocketError)));
  connect(socket, SIGNAL(disconnected()), this, SLOT(OnSocketDisconnected()));

  if (!socket->setSocketDescriptor(m_socketDescriptor)) 
  {
    emit Error(socket->error());
    qDebug() << "SpeakerServerWorker::OnStart() ERROR" << socket->errorString();
    emit Finished();
  }
  else
  {
    qDebug() << "SpeakerServerWorker::OnStart()" << socket->peerAddress().toString() << socket->peerPort();
    connect(socket, SIGNAL(readyRead()), this, SLOT(OnReadyRead()));
  }
}