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
// Summary: HostScene.cpp
//-------------------------------------------------------------------------------


#include <QFileDialog>
#include <QHostAddress>
#include <QMessageBox>
#include <QNetworkAccessManager>
#include <QNetworkRequest>
#include <QNetworkReply>
#include <QPainter>
#include <QPixmap>
#include <QSettings>
#include <QStandardItem>
#include <QStandardItemModel>
#include <QStringList>
#include <QThread>
#include <QTimer>
#include <QToolButton>

#include "AnimatedLineItem.h"
#include "FunctionBlockListView.h"
#include "HostItem.h"
#include "HostScene.h"
#include "Settings.h"
#include "TimelineScene.h"
#include "TimelineEvent.h"
#include "TimelineEventSendWorker.h"
#include "Timer.h"
#include "Utils.h"
#include "WebServiceInfo.h"
#include "WsdlFile.h"

//const QString PYTHON_APP = "python";

//------------------------------------------------------------------------------
// HostScene
//
HostScene::HostScene(QObject* parent)
	: QGraphicsScene(parent),
	m_netAccessManager(Q_NULLPTR),
	m_parentWidget(Q_NULLPTR)
{
	connect(&m_miniNetCmdProcess, SIGNAL(error(QProcess::ProcessError)), this, SLOT(OnMiniNetError(QProcess::ProcessError)));
	connect(&m_miniNetCmdProcess, SIGNAL(finished(int, QProcess::ExitStatus)), this, SLOT(OnMiniNetFinished(int, QProcess::ExitStatus)));
	connect(&m_miniNetCmdProcess, SIGNAL(readyReadStandardError()), this, SLOT(OnMiniNetReadStandardError()));
	connect(&m_miniNetCmdProcess, SIGNAL(readyReadStandardOutput()), this, SLOT(OnMiniNetReadStandardOut()));
}
//------------------------------------------------------------------------------
// ~HostScene
//
HostScene::~HostScene()
{
	Clear();
}
//------------------------------------------------------------------------------
// AddHost
//
void HostScene::AddHost(Host* host, const QPointF& pt)
{
	m_hosts.insert(host->Id(), host);
	HostItem* hostItem = new HostItem(*host, pt);
	connect(hostItem, SIGNAL(MouseDoubleClicked(int)), this, SIGNAL(HostDoubleClicked(int)));
	addItem(hostItem);
}
//------------------------------------------------------------------------------
// AllHostItems
//
QList<HostItem*> HostScene::AllHostItems() const
{
	QList<HostItem*> list;
	const QList<QGraphicsItem*> itemList = items();
	foreach (QGraphicsItem* item, itemList)
	{
	if (HostItem* host = qgraphicsitem_cast<HostItem*>(item))
		list << host;
	}
	return list;
}
//------------------------------------------------------------------------------
// AllUniqueHostNames
//
QStringList HostScene::AllUniqueHostNames()
{
	QStringList list;
	foreach (const Host* host, m_hosts.values())
		list << host->Name();

	list.removeDuplicates();
	list.sort();
	return list;
}
//------------------------------------------------------------------------------
// AnimateMessageSent
//
void HostScene::AnimateMessageSent(int srcId, int dstId)
{
	HostItem* srcItem = FindHostItemById(srcId);
	HostItem* dstItem = FindHostItemById(dstId);
	if (srcItem && dstItem)
	{
		AnimatedLineItem* line = new AnimatedLineItem(srcItem, dstItem);
		connect(line, SIGNAL(Finished()), this, SLOT(OnRemoveAnimatedLine()));
		addItem(line);
		srcItem->AddEdge(line);
		dstItem->AddEdge(line);
		update();
	}
}
//------------------------------------------------------------------------------
// Clear
//
void HostScene::Clear()
{
	clear();
	qDeleteAll(m_hosts);
	m_hosts.clear();
}
//------------------------------------------------------------------------------
// CreateHostPixmap
//
QPixmap HostScene::CreateHostPixmap(const Host& host, int size, bool isSelected)
{
  QPixmap pix(size, size);
  pix.fill(QColor(1, 148, 199));

  QPainter p(&pix);

  p.setRenderHint(QPainter::Antialiasing, true);
  p.setPen(QPen(Qt::black, 2));
  p.setBrush(QColor(1,148,199)); // A pleasant blue ish color
  p.drawRect(QRectF(0, 0, size, size));

  // Center text in box
  p.setPen(Qt::white);
  p.drawText(QRect(0,0,size, size), Qt::AlignCenter, host.Name());

  // Apps Enabled
  QString appString("");
  if (host.AppFlag(Host::Apache)) appString += "A";
  if (host.AppFlag(Host::FireFox)) appString += "F";
  if (host.AppFlag(Host::Terminal)) appString += "T";
  if (host.AppFlag(Host::WireShark)) appString += "W";

  QFont f = p.font();
  f.setPointSize(6);
  p.setFont(f);
  QFontMetrics m(p.fontMetrics());

  // Paint host id in top right corner
  QRect r = m.boundingRect(QString::number(host.Id()));
  p.drawText(QRectF(1, 0, r.width()+1, r.height()+1), Qt::AlignLeft, QString::number(host.Id()));

  if (!appString.isEmpty())
  {
    QRect r = m.boundingRect(appString);
    p.drawText(QRectF(size-r.width()-2, size-r.height()-1, r.width()+1, r.height()+1), Qt::AlignRight, appString);
  }

  if (isSelected)
  {
    p.setPen(QPen(Qt::magenta, 2, Qt::DashLine));
    p.setBrush(Qt::transparent);
    p.drawRect(QRectF(0, 0, size, size));
  }

  return pix;
}
//------------------------------------------------------------------------------
// HostEndPoints
//
QStringList HostScene::HostEndPoints() const
{
	QStringList list;

	foreach (const Host* host, m_hosts.values())
	{
		QString name(WsInfo().FullNameColonSep(host->Name()));
		if (!list.contains(name))
			list.append(name);
	}

	list.sort();
	return list;
}
//------------------------------------------------------------------------------
// HostIdsByAppMode
//
QStringList HostScene::HostIdsByAppMode(Host::AppFlagEnum mode) const
{
	QStringList idList;
	foreach (const Host* host, m_hosts.values())
	{
		if (host->AppFlag(mode))
			idList << QString::number(host->Id());
	}
	idList.sort();
	return idList;
}
//------------------------------------------------------------------------------
// HostItemById
//
HostItem* HostScene::HostItemById(int id) const
{
	HostItem* foundItem(Q_NULLPTR);

	const QList<QGraphicsItem*> itemList = items();
	foreach (QGraphicsItem* item, itemList)
	{
		if (HostItem* host = qgraphicsitem_cast<HostItem*>(item))
		{
			if (host->Id() == id)
			{
				foundItem = host;
				break; // found so get out
			}
		}
	}
	return foundItem;
}
//------------------------------------------------------------------------------
// HostRoles
//
QStringList HostScene::HostRoles() const
{
	QMap<QString, QStringList*> map;

	foreach (const Host* host, m_hosts.values())
	{
		if (!map.contains(host->Name()))
			map.insert(host->Name(), new QStringList);
		//QStringList list = map.value[host->Name()];
		//list << QString::number(host->Id());
		map.values(host->Name()).first()->append(QString::number(host->Id()));
		//map.value[host->Name()].append(QString::number(host->Id()));
	}

	QStringList list;
	foreach (const QString key, map.keys())
	{
		QStringList* idList = map.value(key);
		idList->sort();
		list.append(QString("%1: %2").arg(key).arg(idList->join(",")));
	}

	qDeleteAll(map);
	list.sort();
	return list;
}
////------------------------------------------------------------------------------
//// MiniNetCmdLine
////
//QString HostScene::MiniNetCmdLine() const
//{
//  QString pyFile = QDir::toNativeSeparators(MiniNetScriptFile());
//  QString args = MiniNetCmdLineArgs().join(" "); // Join all args as one
//
//  return QString("%1 %2").arg(pyFile).arg(args);
//}
//------------------------------------------------------------------------------
// MiniNetCmdLine
//
QString HostScene::MiniNetCmdLine(const QString& scriptFile, const QString& confFile, const QString& networkId) const
{
	return MiniNetCmdLineArgs(scriptFile, confFile, networkId).join(" "); // Join all args as one
}
////------------------------------------------------------------------------------
//// MiniNetCmdLineArgs
////
//QStringList HostScene::MiniNetCmdLineArgs() const
//{
//  QStringList args;
//  args << "-h" << QString::number(AllHostItems().count())
//    << "-n" << MiniNetNetworkId()
//    << "-c" << QDir::toNativeSeparators(MiniNetConfFile());
//
//  if (HostIdsByAppMode(Host::Apache).count())
//    args << "-a" << HostIdsByAppMode(Host::Apache).join(",");
//
//  if (HostIdsByAppMode(Host::FireFox).count())
//    args << "-f" << HostIdsByAppMode(Host::FireFox).join(",");
//
//  if (HostIdsByAppMode(Host::WireShark).count())
//    args << "-w" << HostIdsByAppMode(Host::WireShark).join(",");
//
//  if (HostIdsByAppMode(Host::Terminal).count())
//    args << "-x" << HostIdsByAppMode(Host::Terminal).join(",");
//
//  return args;
//}
//------------------------------------------------------------------------------
// MiniNetCmdLineArgs
//
QStringList HostScene::MiniNetCmdLineArgs(const QString& scriptFile, const QString& confFile, const QString& networkId) const
{
	QStringList args;
	//args << "-n"; // For no password prompt for sudoers ...removed for Phil lastest incarnation
	args << QDir::toNativeSeparators(scriptFile);
	args << "-h" << QString::number(AllHostItems().count())
		<< "-n" << networkId
		<< "-c" << QDir::toNativeSeparators(confFile);

	if (HostIdsByAppMode(Host::Apache).count())
		args << "-a" << HostIdsByAppMode(Host::Apache).join(",");

	if (HostIdsByAppMode(Host::FireFox).count())
		args << "-f" << HostIdsByAppMode(Host::FireFox).join(",");

	if (HostIdsByAppMode(Host::WireShark).count())
		args << "-w" << HostIdsByAppMode(Host::WireShark).join(",");

	if (HostIdsByAppMode(Host::Terminal).count())
		args << "-x" << HostIdsByAppMode(Host::Terminal).join(",");

	return args;
}
//------------------------------------------------------------------------------
// MiniNetRunning
//
bool HostScene::MiniNetRunning() const 
{
	QString fileName = MiniNetRunFile();
	if (fileName.isEmpty())
		return false;

	QFile file(fileName);
	if (!file.open(QIODevice::ReadOnly | QIODevice::Text))
		return false;

	int flag;
	QTextStream in(&file);
	in >> flag;
	file.close();

	return flag;
}
//------------------------------------------------------------------------------
// MiniNetRunFile
//
QString HostScene::MiniNetRunFile() const
{
	QString scriptFile = MiniNetScriptFile();

	QFileInfo info(scriptFile);

	if (!info.exists())
		return "";

	QString path = info.path();

	return QString("%1/%2").arg(path).arg(DECOUPLE_RUN_FILE);
}
//------------------------------------------------------------------------------
// RemoveItems
//
//  Need to process the edges to make sure that they get removed properly without
//    Memory corruption.  Each block could have edges that will need to be removed
//
void HostScene::RemoveItems(const QList<QGraphicsItem*> itemList)
{
	// Separate the lines and blocks that need to be removed
	QList<AnimatedLineItem*> lines;
	QList<HostItem*> hosts;
	foreach (QGraphicsItem* item, itemList)
	{
		if (AnimatedLineItem* line = qgraphicsitem_cast<AnimatedLineItem*>(item))
		{
			if (!lines.contains(line))
				lines.append(line);
		}
		if (HostItem* host = qgraphicsitem_cast<HostItem*>(item))
		{
			foreach (AnimatedLineItem* line, host->Edges())
			{
				line->BlockSrc()->RemoveEdge(line);
				line->BlockDst()->RemoveEdge(line);
				if (!lines.contains(line))
				lines.append(line);
			}
			if (!hosts.contains(host))
				hosts.append(host);
		}
	}
	// Remove the lines
	foreach (AnimatedLineItem* line, lines)
		removeItem(line);

	// Remove the blocks
	foreach (HostItem* host, hosts)
	{
		emit HostRemoved(host->Id());
		removeItem(host);
		delete m_hosts.take(host->Id()); // Remove host from m_hosts
	}

	// Now delete the mem because scene::removeItem does not delete
	qDeleteAll(lines);
	qDeleteAll(hosts);
	emit HostRemoved();
}
//------------------------------------------------------------------------------
// StartMiniNet
//
void HostScene::StartMiniNet(/*const QString& cmdLine*/)
{
	// Create and write the conf File
	if (!WriteMiniNetConfFile())
	{
		qDebug() << "WriteMiniNetConfFile Attempt Failed";
		return;
	}

	// Attempt to write the decouple.run file to a '1'
	int count = 0;
	while (!WriteDecoupleRun(true) && count < 100)
	{
		qDebug() << "WriteDecoupleRun Attempt" << count;
		count++;
	}
	//if (cmdLine.isEmpty())
	//{
	qDebug() << MiniNetApp() << MiniNetCmdLine(MiniNetScriptFile(), MiniNetConfFile(), MiniNetNetworkId());
	m_miniNetCmdProcess.start(MiniNetApp(), QStringList() << MiniNetCmdLineArgs(MiniNetScriptFile(), MiniNetConfFile(), MiniNetNetworkId()));
	//}
	//else
	//{
	//  qDebug() << MiniNetApp() << cmdLine;
	//  m_miniNetCmdProcess.start(MiniNetApp(), QStringList() << cmdLine);
	//}
}
//------------------------------------------------------------------------------
// StopMiniNet
//
void HostScene::StopMiniNet()
{
	// Attempt to write the decouple.run file to a '0'
	int count = 0;
	while (!WriteDecoupleRun(false) && count < 100)
	{
		qDebug() << "WriteDecoupleRun Attempt" << count;
		count++;
	}
	QApplication::setOverrideCursor(QCursor(Qt::WaitCursor));
	qDebug() << "Waiting 6 secs for decouple.run to be acknowledged by decouple.py";
	QTimer::singleShot(6000, this, SLOT(OnMiniNetCleanup()));
}
//------------------------------------------------------------------------------
// WriteDecoupleRun
//
bool HostScene::WriteDecoupleRun(bool start)
{
	QString fileName = MiniNetRunFile();
	QFile file(fileName);
	if (!file.open(QIODevice::WriteOnly | QIODevice::Text))
		return false;

	QTextStream out(&file);
	out << ((start) ? "1" : "0");
	file.close();
	return true;
}
//------------------------------------------------------------------------------
// WriteMiniNetConfFile
//
bool HostScene::WriteMiniNetConfFile()
{
	QString fileName = MiniNetConfFile();
	QFile file(fileName);
	if (!file.open(QIODevice::WriteOnly | QIODevice::Text))
	{
		QMessageBox::critical(Q_NULLPTR, "Write Error", QString("Unable to Open MiniNet Conf File to Write Config -- %1").arg(file.errorString()));
		qDebug() << "Unable to open MiniNet Conf File" << file.errorString();
		return false;
	}

	QTextStream out(&file);
	out << "[EndPoints]" << endl;
	out << endl;
	out << "# Add MultiSpeak 'EndPoints' to this section" << endl;
	out << "# for each server role in your topoloty" << endl;
	out << endl;
	out << HostEndPoints().join("\n");
	out << endl;
	out << endl;
	out << "[HostRoles]" << endl;
	out << endl;
	out << "# Add" << endl;
	out << endl;
	out << HostRoles().join("\n");
	file.close();
	return true;
}
//------------------------------------------------------------------------------
// dragEnterEvent
// called here when drag a Function Block to the Topology
void HostScene::dragEnterEvent(QGraphicsSceneDragDropEvent* e)
{
	if (qobject_cast<FunctionBlockListView*>(e->source()))
		e->accept();
	else
		e->ignore();
}
//------------------------------------------------------------------------------
// dragMoveEvent
//
void HostScene::dragMoveEvent(QGraphicsSceneDragDropEvent* e)
{
	if (qobject_cast<FunctionBlockListView*>(e->source()))
		e->accept();
	else
		e->ignore();
}
//------------------------------------------------------------------------------
// dropEvent
// called here when drop a Function Block onto the Topology
void HostScene::dropEvent(QGraphicsSceneDragDropEvent* e)
{
	const QMimeData* data = e->mimeData();

	// Create a temporary model that the mime data can be dropped on.
	QStandardItemModel model;
	model.dropMimeData(data, Qt::CopyAction, 0, 0, model.indexFromItem(model.invisibleRootItem()));

	// Get all the items in the model
	QStringList hosts;
	for (int row = 0; row < model.rowCount(); row++)
		hosts << model.item(row, 0)->data().toString();

	int offset = 10; // If there are multiple dropped then drop them stacked 10pix away from prev
	for (int i = 0; i < hosts.count(); ++i)
	{
		Host* host = new Host(NextHostId(), hosts.at(i), Host::Apache);
		AddHost(host, e->scenePos() + QPointF(i*offset, i*offset));
	}

	QGraphicsScene::dropEvent(e);
	emit HostAdded();
}
//------------------------------------------------------------------------------
// DisplayRequestHeaders
//
void HostScene::DisplayRequestHeaders(QNetworkRequest& request)
{
	QStringList headerStrings;
	foreach(const QByteArray header, request.rawHeaderList())
		headerStrings << QString("%1: %2").arg(QString(header)).arg(QString(request.rawHeader(header)));;

	emit LogMsg(QString("\n%1\n\n").arg(headerStrings.join("\n")));
}
//------------------------------------------------------------------------------
// FindHostItemById
//
HostItem* HostScene::FindHostItemById(int id)
{
	foreach (QGraphicsItem* item, items())
	{
		if (HostItem* h = qgraphicsitem_cast<HostItem*>(item))
		{
			if (h->Id() == id)
				return h;
		}
	}
	return Q_NULLPTR;
}
//------------------------------------------------------------------------------
// NextHostId
//
int HostScene::NextHostId()
{
	int id = 0;
	foreach (const Host* host, m_hosts)
		id = qMax(id, host->Id());

	return id + 1;
}
//------------------------------------------------------------------------------
// OnManagerEncrypted
//
void HostScene::OnManagerEncrypted(QNetworkReply* reply)
{
    Q_UNUSED(reply);
    qDebug() << "HostScene::OnManagerEncrypted()";
}
//------------------------------------------------------------------------------
// OnManagerReplyFinished
//
void HostScene::OnManagerReplyFinished(QNetworkReply* reply)
{
	qDebug() << "HostScene::OnManagerReplyFinished()";
	if (reply)
	{
		if (reply->error() != QNetworkReply::NoError)
			qDebug() << "OnManagerReplyFinished()" << reply->error();
	}
}
//------------------------------------------------------------------------------
// OnManagerSslErrors
//
void HostScene::OnManagerSslErrors(QNetworkReply* reply, const QList<QSslError>& errors)
{
    Q_UNUSED(errors);
    qDebug() << "HostScene::OnManagerSslErrors()";
    if (reply->error() != QNetworkReply::NoError)
        qDebug() << "HostScene::OnManagerSslErrors() Error:" << reply->error();
}
//------------------------------------------------------------------------------
// OnMiniNetError
//
void HostScene::OnMiniNetCleanup()
{
	// Break down MiniNet
	qDebug() << "Wait over calling mn -c";
	m_miniNetCmdProcess.start("sudo", QStringList() << "-n" << "mn" << "-c");
	QApplication::restoreOverrideCursor();
}
//------------------------------------------------------------------------------
// OnMiniNetError
//
void HostScene::OnMiniNetError(QProcess::ProcessError error) 
{
	emit MiniNetError(QString("MiniNet Process Error: App: %1 CmdLine: %2 Error: %3")
		.arg(m_miniNetCmdProcess.program())
		.arg(m_miniNetCmdProcess.arguments().join(" "))
		.arg(Utils::ProcessErrorToString(error)));
}
//------------------------------------------------------------------------------
// OnMiniNetFinished
//
void HostScene::OnMiniNetFinished(int exitCode, QProcess::ExitStatus exitStatus) 
{
	emit MiniNetFinished(QString("MiniNet Process Finished: App: %1 CmdLine: %2 Code: %3 Status: %4")
		.arg(m_miniNetCmdProcess.program())
		.arg(m_miniNetCmdProcess.arguments().join(" "))
		.arg(exitCode).arg(exitStatus));
}
//------------------------------------------------------------------------------
// OnMiniNetReadStandardError
//
void HostScene::OnMiniNetReadStandardError() 
{
	emit MiniNetStdErr(QString("MiniNet Process Std Err: %1").arg(QString(m_miniNetCmdProcess.readAllStandardError())));
}
//------------------------------------------------------------------------------
// OnMiniNetReadStandardOut
//
void HostScene::OnMiniNetReadStandardOut() 
{
	emit MiniNetStdOut(QString("MiniNet Process Std Out: %1").arg(QString(m_miniNetCmdProcess.readAllStandardOutput())));
}
//------------------------------------------------------------------------------
// OnRemoveAnimatedLine
//
void HostScene::OnRemoveAnimatedLine()
{
	if (AnimatedLineItem* line = qobject_cast<AnimatedLineItem*>(sender()))
	{
		removeItem(line);
		line->deleteLater();
	}
}
//------------------------------------------------------------------------------
// OnReplyAboutToClose
//
void HostScene::OnReplyAboutToClose()
{
	qDebug() << "HostScene::OnReplyAboutToClose()";
}
//------------------------------------------------------------------------------
// OnReplyDestroyed
//
void HostScene::OnReplyDestroyed(QObject* obj)
{
    Q_UNUSED(obj);
    qDebug() << "HostScene::OnReplyDestroyed()";
}
//------------------------------------------------------------------------------
// OnReplyEncrypted
//
void HostScene::OnReplyEncrypted()
{
	qDebug() << "HostScene::OnReplyEncrypted()";
}
//------------------------------------------------------------------------------
// OnReplyError
//
void HostScene::OnReplyError(QNetworkReply::NetworkError error)
{
    Q_UNUSED(error);
    if (QNetworkReply* reply = qobject_cast<QNetworkReply*>(sender()))
    {
        qDebug() << "HostScene::OnReplyError()" << reply->errorString();
    }
}
//------------------------------------------------------------------------------
// OnReplyFinished
//
void HostScene::OnReplyFinished()
{
	qDebug() << "HostScene::OnReplyFinished()";
	if (QNetworkReply* reply = qobject_cast<QNetworkReply*>(sender()))
	{
		/*if (reply->error() != QNetworkReply::NoError)
			emit LogMsg(QString("\n%1").arg(reply->error()).arg(reply->errorString()));

		QStringList headerStrings;
		foreach(const QNetworkReply::RawHeaderPair pair, reply->rawHeaderPairs())
			headerStrings << QString("%1: %2")
				.arg(QString(pair.first))
				.arg(QString(pair.second));

		emit LogMsg(QString("\n%1\n\n").arg(headerStrings.join("\n")));
		*/
		QByteArray content = reply->readAll();
		if( !content.isEmpty() )
			emit LogMsg(QString("\n%1").arg(QString(content)));

		reply->close();
		reply->deleteLater();
		//m_netAccessManager->deleteLater();
		//m_netAccessManager = 0;
  }
}
//------------------------------------------------------------------------------
// OnReplySslErrors
//
void HostScene::OnReplySslErrors(const QList<QSslError>& errors)
{
	qDebug() << "HostScene::OnReplySslErrors()";
	if (QNetworkReply* reply = qobject_cast<QNetworkReply*>(sender()))
	{
		QList<QSslError> expectedSslErrors;
		foreach(QSslError error, errors)
		{
			qDebug() << "Error:" << error.error() << error.errorString();
			expectedSslErrors.append(error);
		}
		reply->ignoreSslErrors(expectedSslErrors);
	}
}
//------------------------------------------------------------------------------
// OnTimelineEventProcessed - send packet
//
void HostScene::OnTimelineEventProcessed(TimelineEvent& e)
{
	AnimateMessageSent(e.SrcHostId(), e.DstHostId()); // Animate

	//QSettings s;
	/* Only do Mininet if HttpOut Request or Response is disabled
	if (!(s.value(SK_HTTP_OUT_REQ_FLAG, false).toBool() || s.value(SK_HTTP_OUT_RES_FLAG, false).toBool()))
	{
		QThread* thread = new QThread;
		TimelineEventSendWorker* worker = new TimelineEventSendWorker(QHostAddress(Hosts().HostIp()), Hosts().HostPort(), e);
		worker->moveToThread(thread);
		connect(worker, SIGNAL(Error(QAbstractSocket::SocketError, const QString&)), this, SLOT(OnTimelineEventSendError(QAbstractSocket::SocketError, const QString&)));
		connect(worker, SIGNAL(Finished()), thread, SLOT(quit()));
		connect(worker, SIGNAL(Finished()), worker, SLOT(deleteLater()));
		connect(thread, SIGNAL(finished()), thread, SLOT(deleteLater()));
		connect(thread, SIGNAL(started()), worker, SLOT(OnStart()));
		thread->start();
	}*/
	Host* host;
	// Initiate Connection to Request Destination Host, if enabled
	//if (s.value(SK_HTTP_OUT_REQ_FLAG, false).toBool() && e.Type() == TimelineEvent::Request)
	if ( e.Type() == TimelineEvent::Request && (host = HostById(e.DstHostId())))
	{
		if (host->ReqHostEnable())
		{
			if (!m_netAccessManager)
			{
				m_netAccessManager = new QNetworkAccessManager(this);
			}

			QByteArray content = WsdlFile::XmlSoap(e.Doc());
			qDebug() << "Content Length:" << content.length();
			qDebug() << "Host:" << host->ReqHostAddress();
			qDebug() << "Port:" << host->ReqHostPort();

			QNetworkRequest request;
			//request.setUrl(QUrl("http://64.184.186.24:8080/")); // this works!!!
			//if (s.value(SK_HTTP_OUT_SSL, false).toBool())
			if( host->EnableSsl() )
				request.setUrl(QUrl(QString("https://%1:%2/").arg(host->ReqHostAddress()).arg(host->ReqHostPort())));
			else
				request.setUrl(QUrl(QString("http://%1:%2/").arg(host->ReqHostAddress()).arg(host->ReqHostPort())));

			request.setRawHeader("Accept", "application / soap + xml, application / dime, multipart / related, text/*");
			request.setRawHeader("Host", QString("%1:%2").arg(host->ReqHostAddress()).arg(host->ReqHostPort()).toLatin1());
			request.setRawHeader("Content-Type", "text/xml;charset=utf-8");
			request.setRawHeader("Content-Length", QString::number(content.length()).toLatin1());
			request.setRawHeader("SOAPAction", QString("%1/%2").arg(e.Namespace(), e.Method()).toLatin1());

			//DisplayRequestHeaders(request); // Debugging
			QNetworkReply* reply = m_netAccessManager->post(request, content);
			connect(reply, SIGNAL(encrypted()), this, SLOT(OnReplyEncrypted()));
			connect(reply, SIGNAL(error(QNetworkReply::NetworkError)), this, SLOT(OnReplyError(QNetworkReply::NetworkError)));
			connect(reply, SIGNAL(finished()), this, SLOT(OnReplyFinished()));
			connect(reply, SIGNAL(sslErrors(const QList<QSslError>&)), this, SLOT(OnReplySslErrors(const QList<QSslError>&)));
			connect(reply, SIGNAL(aboutToClose()), this, SLOT(OnReplyAboutToClose()));
			connect(reply, SIGNAL(destroyed(QObject*)), this, SLOT(OnReplyDestroyed(QObject*)));
		}
	}
	//else if (s.value(SK_HTTP_OUT_RES_FLAG, false).toBool() && e.Type() == TimelineEvent::Response)
	else if (e.Type() == TimelineEvent::Response && (host = HostById(e.SrcHostId())))
	{ 	// Initiate Connection to Response Host
		if (host->RespHostEnable() )
		{
			if (!m_netAccessManager)
			{
				m_netAccessManager = new QNetworkAccessManager(this);
			}

			QByteArray content = WsdlFile::XmlSoap(e.Doc());
			qDebug() << "Content Length:" << content.length();
			qDebug() << "Host:" << host->RespHostAddress();
			qDebug() << "Port:" << host->RespHostPort();

			QNetworkRequest response;
			//if (s.value(SK_HTTP_OUT_SSL, false).toBool())
			if( host->EnableSsl() )
				response.setUrl(QUrl(QString("https://%1:%2/").arg(host->RespHostAddress()).arg(host->RespHostPort())));
			else
				response.setUrl(QUrl(QString("http://%1:%2/").arg(host->RespHostAddress()).arg(host->RespHostPort())));

			response.setRawHeader("Accept", "application / soap + xml, application / dime, multipart / related, text/*");
			response.setRawHeader("Host", QString("%1:%2").arg(host->RespHostAddress()).arg(host->RespHostPort()).toLatin1());
			response.setRawHeader("Content-Type", "text/xml;charset=utf-8");
			response.setRawHeader("Content-Length", QString::number(content.length()).toLatin1());
			response.setRawHeader("SOAPAction", QString("%1/%2").arg(e.Namespace(), e.Method()).toLatin1());

			QNetworkReply* reply = m_netAccessManager->post(response, content);
			connect(reply, SIGNAL(encrypted()), this, SLOT(OnReplyEncrypted()));
			connect(reply, SIGNAL(error(QNetworkReply::NetworkError)), this, SLOT(OnReplyError(QNetworkReply::NetworkError)));
			connect(reply, SIGNAL(finished()), this, SLOT(OnReplyFinished()));
			connect(reply, SIGNAL(sslErrors(const QList<QSslError>&)), this, SLOT(OnReplySslErrors(const QList<QSslError>&)));
			connect(reply, SIGNAL(aboutToClose()), this, SLOT(OnReplyAboutToClose()));
			connect(reply, SIGNAL(destroyed(QObject*)), this, SLOT(OnReplyDestroyed(QObject*)));
		}
	}
}
//------------------------------------------------------------------------------
// OnTimelineEventSendError
//
void HostScene::OnTimelineEventSendError(QAbstractSocket::SocketError error, const QString& errorStr)
{
  emit MiniNetError(QString("Socket Error: %1: %2").arg(error).arg(errorStr));
}
//------------------------------------------------------------------------------
// << Serialize Write
//
QDataStream & operator<< (QDataStream& s, const HostScene& scene)
{
  qint32 version = 1;
  s << version;

  // Hosts
  s << static_cast <qint32>(scene.AllHosts().count());
  foreach (const HostItem* hostItem, scene.AllHostItems())
  {
    const Host& host = hostItem->HostRef();
    s << static_cast <qint32>(host.Id());
    s << host.Name();
    s << static_cast <qint32>(host.AppFlags());
    s << hostItem->Origin();
  }
  return s;
}
//------------------------------------------------------------------------------
// >> Serialize Read
//
QDataStream & operator>> (QDataStream& s, HostScene& scene)
{
  qint32 version(0);

  // Hosts
  qint32 count;
  qint32 appFlags;
  qint32 id;
  QString name;
  QPointF pt;

  s >> version;
  if (version == 1)
  {
    s >> count; // Host Count
    for (qint32 i = 0; i < count; i++)
    {
      s >> id;
      s >> name;
      s >> appFlags;
      s >> pt;
      Host* host = new Host(id, name, appFlags);
      scene.AddHost(host, pt);
    }
  }
  //else if (version == 2) // Future
  //{
  //}
  return s;
}
