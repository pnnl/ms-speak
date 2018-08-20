//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: ServerWorker
//

#ifndef SERVERWORKER_H
#define SERVERWORKER_H

#include <QObject>
#include <QTcpSocket>

class ServerWorker : public QObject
{
  Q_OBJECT
private:
  enum HttpReadingState {ReadingMethodLine, ReadingHeaders, ReadingContent, ReadingDone};

  QByteArray m_buffer;
  quint32 m_bufferSize;
  quint32 m_bytesRead;
  int m_dstId;
  bool m_headerRead;
  int m_headerSize;
  int m_srcId;

  qintptr m_socketDescriptor;

public:
  ServerWorker(qintptr socketDescriptor, QObject* parent=0);
  ~ServerWorker();

private:
  void ReadMessage(QTcpSocket* socket);
 
signals:
  void Error(QAbstractSocket::SocketError socketError);
  void Finished();
  void Message(int srcId, int dstId, const QByteArray& msg);

private slots:
  void OnError(QAbstractSocket::SocketError socketError);
  void OnReadyRead();
  void OnSocketDisconnected();
  void OnStart();
};

#endif // SERVERWORKER_H
