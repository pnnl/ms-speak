//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: MultiSpeakerServer
//

#include "MultiSpeakerServer.h"
int MSG_COUNTER = 0;

//------------------------------------------------------------------------------
// MultiSpeakerServer
//
MultiSpeakerServer::MultiSpeakerServer(QWidget* parent)
  : QMainWindow(parent),
  m_server(this)
{
  ui.setupUi(this);
  connect(ui.ListenAct, SIGNAL(triggered()), this, SLOT(OnListen()));
  connect(ui.StopAct, SIGNAL(triggered()), this, SLOT(OnStop()));
  connect(&m_server, SIGNAL(Message(int, int, const QByteArray&)), this, SLOT(OnMessage(int, int, const QByteArray&)));
}
//------------------------------------------------------------------------------
// ~MultiSpeakerServer
//
MultiSpeakerServer::~MultiSpeakerServer()
{
}
//------------------------------------------------------------------------------
// OnListen
//
void MultiSpeakerServer::OnListen()
{
  if (!m_server.listen(QHostAddress("127.0.0.1"), ui.PortSpin->value())) 
  {
    qDebug() << "Server Listen Error:" << m_server.serverError() << m_server.errorString();
    ui.plainTextEdit->appendPlainText(QString("Server Listen Error: %1, %2")
      .arg(m_server.serverError())
      .arg(m_server.errorString()));
  }
  qDebug() << "Server The server is running on IP:" << m_server.serverAddress().toString() << "Port:" << m_server.serverPort();
  ui.plainTextEdit->appendPlainText(QString("Server The server is running on IP: %1 Port: %2")
    .arg(m_server.serverAddress().toString())
    .arg(m_server.serverPort()));

}
//------------------------------------------------------------------------------
// OnMessage
//
void MultiSpeakerServer::OnMessage(int srcId, int dstId, const QByteArray& msg)
{
  ui.plainTextEdit->appendPlainText("*****************************\n");
  ui.plainTextEdit->appendPlainText(QString("**** MSG COUNTER: %1 ****\n").arg(++MSG_COUNTER));
  ui.plainTextEdit->appendPlainText(QString("**** srcId: %1 dstId: %2 ****\n").arg(srcId).arg(dstId));
  ui.plainTextEdit->appendPlainText("*****************************\n");
  ui.plainTextEdit->appendPlainText(msg);
}
//------------------------------------------------------------------------------
// OnStop
//
void MultiSpeakerServer::OnStop()
{
  m_server.close();
  ui.plainTextEdit->appendPlainText("Server Closed\n");
}



