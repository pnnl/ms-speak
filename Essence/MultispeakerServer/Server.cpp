//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: Server
//

#include <QDataStream>
#include <QMessageBox>
#include <QNetworkInterface>
#include <QSettings>
#include <QTcpSocket>
#include <QThread>

#include "Server.h"
#include "ServerWorker.h"

//------------------------------------------------------------------------------
// Server
//
Server::Server(QObject* parent)
  : QTcpServer(parent)
{
}
//------------------------------------------------------------------------------
// ~Server
//
Server::~Server()
{
  close(); // the server will no longer listen for incoming connections
}
//------------------------------------------------------------------------------
// incomingConnection
//
//  Overwrite this virtual function to create a return message
//
void Server::incomingConnection(qintptr socketDescriptor)
{
  qDebug() << "Server::incomingConnection():" << serverAddress().toString() << serverPort();
  QThread* thread = new QThread;
  ServerWorker* worker = new ServerWorker(socketDescriptor);
  worker->moveToThread(thread);
  connect(worker, SIGNAL(Error(QAbstractSocket::SocketError)), this, SIGNAL(Error(QAbstractSocket::SocketError)));
  connect(worker, SIGNAL(Finished()), thread, SLOT(quit()));
  connect(worker, SIGNAL(Finished()), worker, SLOT(deleteLater()));
  connect(worker, SIGNAL(Message(int, int, const QByteArray&)), this, SIGNAL(Message(int, int, const QByteArray&)));
  connect(thread, SIGNAL(finished()), thread, SLOT(deleteLater()));
  connect(thread, SIGNAL(started()), worker, SLOT(OnStart()));
  thread->start();
}
