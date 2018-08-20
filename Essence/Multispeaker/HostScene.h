//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: HostScene
//

#ifndef HOSTSCENE_H
#define HOSTSCENE_H

#include <QApplication>
#include <QGraphicsScene>
#include <QGraphicsSceneDragDropEvent>
#include <QHostAddress>
#include <QProcess>
#include <QSettings>

#include "Host.h"
#include "Settings.h"

class TimelineEvent;
class HostItem;

class HostScene : public QGraphicsScene
{
  Q_OBJECT
private:
  QHostAddress m_host; // Used for communication
  int m_hostPort; // Used for communication
  QHash<int, Host*> m_hosts;
  QProcess m_miniNetCmdProcess;
  QWidget* m_parentWidget; // Widget used for owner of modal dialogs

public:
  HostScene(QObject* parent);
  ~HostScene();

  void AddHost(const QString& name, const QPointF& pt);
  QList<HostItem*> AllHostItems() const;
  QList<Host*> AllHosts() {return m_hosts.values();}
  const QList<Host*> AllHosts() const {return m_hosts.values();}
  QStringList AllUniqueHostNames();
  void AnimateMessageSent(int srcId, int dstId);

  QPixmap CreateHostPixmap(const Host& host, int size, bool isSelected=false);

  Host* HostById(int id) {return ((m_hosts.contains(id)) ? m_hosts.value(id) : 0);}
  QStringList HostEndPoints() const;
  QStringList HostIdsByAppMode(Host::AppFlagEnum mode) const;
  HostItem* HostItemById(int id) const;
  QString HostIp() const {return QSettings().value(SK_MINI_NET_HOST_IP, QHostAddress(QHostAddress::LocalHost).toIPv4Address()).toString();}
  int HostPort() const {return QSettings().value(SK_MINI_NET_HOST_PORT, 8888).toInt();}
  QStringList HostRoles() const;

  QString MiniNetApp() const {return QSettings().value(SK_MINI_NET_APP, "python").toString();}
  //QString MiniNetCmdLine() const;
  QString MiniNetCmdLine(const QString& scriptFile, const QString& confFile, const QString& networkId) const;
  //QStringList MiniNetCmdLineArgs() const;
  QStringList MiniNetCmdLineArgs(const QString& scriptFile, const QString& confFile, const QString& networkId) const;
  QString MiniNetConfFile() const {return QSettings().value(SK_MINI_NET_CONF_FILE, "").toString();}
  QString MiniNetNetworkId() const {return QSettings().value(SK_MINI_NET_NETWORK_ID, "").toString();}
  bool MiniNetRunning() const;
  QString MiniNetRunFile() const;
  QString MiniNetScriptFile() const {return QSettings().value(SK_MINI_NET_SCRIPT_FILE, "").toString();}

  void RemoveItems(const QList<QGraphicsItem*> itemList);

  void SetHostIp(const QString& ip) {QSettings().setValue(SK_MINI_NET_HOST_IP, ip);}
  void SetHostPort(int port) {QSettings().setValue(SK_MINI_NET_HOST_PORT, port);}
  void SetMiniNetApp(const QString& app) {QSettings().setValue(SK_MINI_NET_APP, app);}
  void SetMiniNetConfFile(const QString& fileName) {QSettings().setValue(SK_MINI_NET_CONF_FILE, fileName);}
  void SetMiniNetNetworkId(const QString& id) {QSettings().setValue(SK_MINI_NET_NETWORK_ID, id);}
  void SetMiniNetScriptFile(const QString& fileName) {QSettings().setValue(SK_MINI_NET_SCRIPT_FILE, fileName);}
  void SetParentWidget(QWidget* w) {m_parentWidget = w;}
  void StartMiniNet(/*const QString& cmdLine=""*/);
  void StopMiniNet();

  bool WriteDecoupleRun(bool start);
  bool WriteMiniNetConfFile();

protected:
  virtual void dragEnterEvent(QGraphicsSceneDragDropEvent* e);
  virtual void dragMoveEvent(QGraphicsSceneDragDropEvent* e);
  virtual void dropEvent(QGraphicsSceneDragDropEvent* e);

private:
  Host* AddHost(const QString& name);
  HostItem* FindHostItemById(int id);

signals:
  void HostAdded();
  void HostDoubleClicked(int id);
  void HostRemoved(int id);
  void HostRemoved();
  void HostSelected(int id);
  void MiniNetError(const QString& msg);
  void MiniNetFinished(const QString& msg);
  void MiniNetStdErr(const QString& msg);
  void MiniNetStdOut(const QString& msg);

private slots:
  void OnMiniNetCleanup();
  void OnMiniNetError(QProcess::ProcessError error);
  void OnMiniNetFinished(int exitCode, QProcess::ExitStatus exitStatus);
  void OnMiniNetReadStandardError();
  void OnMiniNetReadStandardOut();
  void OnTimelineEventProcessed(TimelineEvent& e);
  void OnTimelineEventSendError(QAbstractSocket::SocketError error, const QString& errorStr);
};

//-------------------------------------------------------------------------------
// Hosts
//  Singleton
//
inline HostScene& Hosts() 
{
  // Static init will only be allocated once and dealloc when QApplication goes out of scope in main()
  static HostScene* STATIC_HOST_SCENE = new HostScene(qApp);
  return *STATIC_HOST_SCENE;
}

#endif // HOSTSCENE_H
