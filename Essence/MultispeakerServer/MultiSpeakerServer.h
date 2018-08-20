//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: MultiSpeakerServer
//

#ifndef MULTISPEAKERSERVER_H
#define MULTISPEAKERSERVER_H

#include "ui_MultiSpeakerServer.h"

#include <QMainWindow>

#include "Server.h"

class MultiSpeakerServer : public QMainWindow
{
  Q_OBJECT
private:
  Ui::MultiSpeakerServerClass ui;

  Server m_server;

public:
  MultiSpeakerServer(QWidget* parent=0);
  ~MultiSpeakerServer();
protected:
private:
signals:
private slots:
  void OnListen();
  void OnMessage(int srcId, int dstId, const QByteArray& msg);
  void OnStop();
};

#endif // MULTISPEAKERSERVER_H
