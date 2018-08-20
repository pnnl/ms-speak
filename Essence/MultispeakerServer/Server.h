//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: Server
//

#ifndef SERVER_H
#define SERVER_H

#include <QHostAddress>
#include <QTcpServer>

class Server : public QTcpServer
{
  Q_OBJECT
public:
  Server(QObject* parent);
  ~Server();

protected:
  virtual void incomingConnection(qintptr socketDescriptor);

signals:
  void Error(QAbstractSocket::SocketError socketError, const QString& errorString);
  void Error(QAbstractSocket::SocketError socketError);
  void Message(int srcId, int dstId, const QByteArray& msg);
};

#endif // SERVER_H
