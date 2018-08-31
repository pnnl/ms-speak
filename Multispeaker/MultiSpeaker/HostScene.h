/*-------------------------------------------------------------------------------

  Multi-Speak - Secure Protocol Enterprise Access Kit(MS_SPEAK)
  Copyright © 2018, Battelle Memorial Institute
  All rights reserved.
  1.	Battelle Memorial Institute (hereinafter Battelle) hereby grants permission to any person or
		entity lawfully obtaining a copy of this software and associated documentation files
		(hereinafter “the Software”) to redistribute and use the Software in source and binary forms,
		with or without modification.  Such person or entity may use, copy, modify, merge, publish,
		distribute, sublicense, and/or sell copies of the Software, and may permit others to do so,
		subject to the following conditions:
		•	Redistributions of source code must retain the above copyright notice, this list of
			conditions and the following disclaimers.
		•	Redistributions in binary form must reproduce the above copyright notice, this list of
			conditions and the following disclaimer in the documentation and/or other materials
			provided with the distribution.
		•	Other than as used herein, neither the name Battelle Memorial Institute or Battelle may
			be used in any form whatsoever without the express written consent of Battelle.

  2.	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
		OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
		AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL BATTELLE OR CONTRIBUTORS
		BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
		(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
		OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
		CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
		OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


  This material was prepared as an account of work sponsored by an agency of the United States Government.
  Neither the United States  Government nor the United States Department of Energy, nor Battelle, nor
  any of their employees, nor any jurisdiction or organization  that has cooperated in the development
  of these materials, makes any warranty, express or implied, or assumes any legal liability or
  responsibility for the accuracy, completeness, or usefulness or any information, apparatus, product,
  software, or process disclosed, or represents that its use would not infringe privately owned rights.
  Reference herein to any specific commercial product, process, or service by trade name, trademark,
  manufacturer, or otherwise does not necessarily constitute or imply its endorsement, recommendation, or
  favoring by the United States Government or any agency thereof, or Battelle Memorial Institute. The
  views and opinions of authors expressed herein do not necessarily state or reflect those of the
  United States Government or any agency thereof.
									 PACIFIC NORTHWEST NATIONAL LABORATORY
											    operated by
												  BATTELLE
											      for the
									  UNITED STATES DEPARTMENT OF ENERGY
									   under Contract DE-AC05-76RL01830


    This notice including this sentence must appear on any copies of this computer software.
*/
//-------------------------------------------------------------------------------
//	History
//		2017 - Created By: Lance Irvine.
//		2018 - Modified By: Carl Miller <carl.miller@pnnl.gov>
//-------------------------------------------------------------------------------
//
// Summary: HostScene.h
//-------------------------------------------------------------------------------

#ifndef HOSTSCENE_H
#define HOSTSCENE_H

#include <QApplication>
#include <QGraphicsScene>
#include <QGraphicsSceneDragDropEvent>
#include <QHostAddress>
#include <QNetworkReply>
#include <QProcess>
#include <QSettings>

#include "Host.h"
#include "Settings.h"

class HostItem;
class QNetworkAccessManager;
class TimelineEvent;
class QSslCertificate;
class QSslCipher;
class QSslError;

class HostScene : public QGraphicsScene
{
  Q_OBJECT
private:
  //QHostAddress m_host; // Used for communication
  //int m_hostPort; // Used for communication
  QHash<int, Host*> m_hosts;
  QProcess m_miniNetCmdProcess;
  QNetworkAccessManager* m_netAccessManager;
  QWidget* m_parentWidget; // Widget used for owner of modal dialogs

public:
  HostScene(QObject* parent);
  ~HostScene();

  void AddHost(Host* host, const QPointF& pt=QPointF(100,100));
  //void AddHost(const QString& name, const QPointF& pt);
  //void AddHost(int id, const QString& name, int appFlags=0, const QPointF& pt=QPointF(100,100));
  QList<HostItem*> AllHostItems() const;
  QList<Host*> AllHosts() {return m_hosts.values();}
  const QList<Host*> AllHosts() const {return m_hosts.values();}
  QStringList AllUniqueHostNames();
  void AnimateMessageSent(int srcId, int dstId);

  void Clear();

  QPixmap CreateHostPixmap(const Host& host, int size, bool isSelected=false);

  //const QHostAddress& HostAddress() const {return m_host;}
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
  //Host* AddHost(const QString& name);
  void DisplayRequestHeaders(QNetworkRequest& request);
  HostItem* FindHostItemById(int id);
  int NextHostId();

signals:
  void HostAdded();
  void HostDoubleClicked(int id);
  void HostRemoved(int id);
  void HostRemoved();
  void HostSelected(int id);
  void LogMsg(const QString& msg);
  void MiniNetError(const QString& msg);
  void MiniNetFinished(const QString& msg);
  void MiniNetStdErr(const QString& msg);
  void MiniNetStdOut(const QString& msg);
  void TimelineEventSendSslErrors(const QList<QSslError>& errors, const QSslCipher& cipher, const QList<QSslCertificate>& certChain);


private slots:
  void OnManagerEncrypted(QNetworkReply* reply);
  void OnManagerReplyFinished(QNetworkReply* reply);
  void OnManagerSslErrors(QNetworkReply* reply, const QList<QSslError>& errors);
  void OnMiniNetCleanup();
  void OnMiniNetError(QProcess::ProcessError error);
  void OnMiniNetFinished(int exitCode, QProcess::ExitStatus exitStatus);
  void OnMiniNetReadStandardError();
  void OnMiniNetReadStandardOut();
  void OnRemoveAnimatedLine();
  void OnReplyAboutToClose();
  void OnReplyDestroyed(QObject* obj);
  void OnReplyEncrypted();
  void OnReplyError(QNetworkReply::NetworkError error);
  void OnReplyFinished();
  void OnReplySslErrors(const QList<QSslError>& errors);
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

// Serializing methods
QDataStream & operator<< (QDataStream& stream, const HostScene& scene);
QDataStream & operator>> (QDataStream& stream, HostScene& scene);

#endif // HOSTSCENE_H
