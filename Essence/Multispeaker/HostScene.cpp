//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: HostScene
//

#include <QFileDialog>
#include <QHostAddress>
#include <QMessageBox>
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

int HOST_ID = 0;

const QString PYTHON_APP = "python";

//------------------------------------------------------------------------------
// HostScene
//
HostScene::HostScene(QObject* parent)
  : QGraphicsScene(parent),
  m_parentWidget(0)
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
  qDeleteAll(m_hosts);
}
//------------------------------------------------------------------------------
// AddHost
//
void HostScene::AddHost(const QString& name, const QPointF& pt)
{
  Host* host = AddHost(name);
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
  qDebug() << "AnimateMessageSent:" << srcId << dstId;
  HostItem* srcItem = FindHostItemById(srcId);
  HostItem* dstItem = FindHostItemById(dstId);
  if (srcItem && dstItem)
  {
    AnimatedLineItem* line = new AnimatedLineItem(srcItem, dstItem);
    connect(line, SIGNAL(Finished(AnimatedLineItem*)), this, SLOT(OnRemoveAnimatedLine(AnimatedLineItem*)));
    addItem(line);
    srcItem->AddEdge(line);
    dstItem->AddEdge(line);
    update();
  }
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
  HostItem* foundItem(0);

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
  args << "-n"; // For no password prompt for sudoers
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
    QMessageBox::critical(0, "Write Error", QString("Unable to Open MiniNet Conf File to Write Config -- %1").arg(file.errorString()));
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
//
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
//
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
    AddHost(hosts.at(i), e->scenePos() + QPointF(i*offset, i*offset));

  QGraphicsScene::dropEvent(e);
  emit HostAdded();
}
//------------------------------------------------------------------------------
// AddHost
//
Host* HostScene::AddHost(const QString& name)
{
  Host* host = new Host(++HOST_ID, name);
  m_hosts.insert(host->Id(), host);
  return host;
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
  return 0;
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
// OnTimelineEventProcessed
//
void HostScene::OnTimelineEventProcessed(TimelineEvent& e)
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
  //qDebug() << QString("%1: %2").arg(Timer().ToStringMS(e.TimeStamp())).arg(e.Method());
}
//------------------------------------------------------------------------------
// OnTimelineEventSendError
//
void HostScene::OnTimelineEventSendError(QAbstractSocket::SocketError error, const QString& errorStr)
{
  emit MiniNetError(QString("Socket Error: %1: %2").arg(error).arg(errorStr));
}