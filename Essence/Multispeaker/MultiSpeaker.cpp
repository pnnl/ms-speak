//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: MultiSpeaker
//
//  Version: MultiSpeakerQt14.11.19

#include <QDir>
#include <QLabel>
#include <QListView>
#include <QMessageBox>
#include <QSettings>
#include <QStandardItemModel>
#include <QStandardItem>
#include <QToolButton>

#include "DockTitleBar.h"
#include "HeaderContainerWidget.h"
#include "Host.h"
#include "HostEditor.h"
#include "HostMethodListWidget.h"
#include "HostScene.h"
#include "MiniNetEditor.h"
#include "MultiSpeaker.h"
#include "Settings.h"
#include "TimelineEventEditor.h"
#include "TimelineScene.h"
#include "Utils.h"
#include "Version.h"
#include "WidgetContainer.h"
#include "WebServiceInfo.h"
#include "WsdlFile.h"
#include "WsdlFileView.h"

bool CLEAR_SETTINGS_ON_EXIT = false;

//------------------------------------------------------------------------------
// MultiSpeaker
//
MultiSpeaker::MultiSpeaker(QWidget* parent)
  : QMainWindow(parent),
    m_clearSettingsShortcut(QKeySequence("Ctrl+Shift+C"), this, SLOT(OnClearSettings())),
  m_functionBlockDock(0),
  m_logDock(0),
  m_methodDock(0),
  m_miniNetCmdDock(0),
  m_wsdlDock(0)
{
  ui.setupUi(this);
  Utils::CreatRootHomePath(); // Make sure the .MultiSpeaker dir exists

  CreateTitleToolBar();
  //ui.HostView->setScene(&m_scene);
  FunctionBlockDockkRef().show();
  LogDockRef().show();

  ui.TopologyHeader->SetTitle("Topology", 12);
  ui.TimelineHeader->SetTitle("Timeline", 14);
  ui.MethodEventsHeader->SetTitle("Events", 10);
  ui.MethodEventsHeader->SetColor(QColor(1, 164, 148));

  connect(&Hosts(), SIGNAL(HostDoubleClicked(int)), this, SLOT(OnHostDoubleClicked(int)));

  connect(&Hosts(), SIGNAL(HostAdded()), this, SLOT(OnHostSceneChanged()));
  connect(&Hosts(), SIGNAL(HostRemoved()), this, SLOT(OnHostSceneChanged()));
  connect(&Hosts(), SIGNAL(MiniNetError(const QString&)), this, SLOT(OnMiniNetMsg(const QString&)));
  connect(&Hosts(), SIGNAL(MiniNetFinished(const QString&)), this, SLOT(OnMiniNetMsg(const QString&)));
  connect(&Hosts(), SIGNAL(MiniNetStdErr(const QString&)), this, SLOT(OnMiniNetMsg(const QString&)));
  connect(&Hosts(), SIGNAL(MiniNetStdOut(const QString&)), this, SLOT(OnMiniNetMsg(const QString&)));

  connect(&Timeline(), SIGNAL(EventUpdated(TimelineEvent&)), this, SLOT(OnTimelineEventDoubleClicked(TimelineEvent&)));
  connect(&Timeline(), SIGNAL(EventProcessed(TimelineEvent&)), &Hosts(), SLOT(OnTimelineEventProcessed(TimelineEvent&)));

  connect(&WsInfo(), SIGNAL(WsdlFileChanged(const QString&)), this, SLOT(OnWsdlFileChanged(const QString&)));

  // Debug
  //Hosts().AddHost(WS_CB_NAME_SHORT, QPointF(100,100));
  //Hosts().AddHost(WS_MR_NAME_SHORT, QPointF(300,100));
  //Hosts().AddHost(WS_MDM_NAME_SHORT, QPointF(200,200));
  //Hosts().AddHost(WS_OA_NAME_SHORT, QPointF(300,200));
  // Debug

  MethodDockRef().show();

  ui.TimelineEventListView->setModel(&Timeline().EventModel());
  ui.TimelineEventListView->setEditTriggers(QAbstractItemView::NoEditTriggers);
  connect(ui.TimelineEventListView, SIGNAL(doubleClicked(const QModelIndex&)), this, SLOT(OnTimelineEventListViewDoubleClicked(const QModelIndex&)));

  RestoreState();
  Timeline().SetParentWidget(this); // Need to have this happen so signals of timeline buttons connect to timeline scene
  Timeline().Stop(); // begin in stop state as the 
}
//------------------------------------------------------------------------------
// ~MultiSpeaker
//
MultiSpeaker::~MultiSpeaker()
{
}
//------------------------------------------------------------------------------
// closeEvent
//
void MultiSpeaker::closeEvent (QCloseEvent* e)
{
  //if (QMessageBox::No == QMessageBox::warning(this, "Close", "Are You Sure You Want to Close MultiSpeaker?", QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes))
  //{
  //	e->ignore();
  //	return;
  //}
  SaveState();

  // If the user has enabled the clear settings on exit ctrl-shift-c hot key combo, then clear them after save state called
  if (CLEAR_SETTINGS_ON_EXIT)
    QSettings().clear();

  QMainWindow::closeEvent(e);
}
//------------------------------------------------------------------------------
// CreateFunctionBlockDock
//
void MultiSpeaker::CreateFunctionBlockDock()
{
  m_functionBlockDock = new FunctionBlockDock("Function Blocks", this);
  m_functionBlockDock->setFloating(false);

  //m_functionBlockDock->setWindowTitle("Function Blocks");
  m_functionBlockDock->setObjectName("FunctionBlocks"); // Need this to ensure that Main Window saveState() works
  this->addDockWidget(Qt::LeftDockWidgetArea, m_functionBlockDock);
}
//------------------------------------------------------------------------------
// CreateLogDock
//
void MultiSpeaker::CreateLogDock()
{
  m_logDock = new LogDock(this);
  addDockWidget(Qt::BottomDockWidgetArea, m_logDock);
  m_logDock->setFloating(true);
}
//------------------------------------------------------------------------------
// CreateMethodDock
//
void MultiSpeaker::CreateMethodDock()
{
  m_methodDock = new MethodDock(this);
  WidgetContainer* container = new WidgetContainer(SK_METHOD_DOCK_WC_SPLITTER_STATE, m_methodDock);

  QList<QWidget*> list;
  int index = 0;

  // Add Widgets

  foreach (const QString hostName, Hosts().AllUniqueHostNames())
  {
    HostMethodListWidget* hcw = new HostMethodListWidget(index++, hostName);
    hcw->Header()->SetColor(QColor(1,148,199));
    hcw->Header()->SetExpanded(false);
    hcw->Header()->setToolTip(WsInfo().FullName(hostName));
    hcw->Container()->setVisible(false);
    list << hcw;
  }
  container->SetWidgets(list);
  m_methodDock->setWidget(container);
  addDockWidget(Qt::RightDockWidgetArea, m_methodDock);
}
//------------------------------------------------------------------------------
// CreateMiniNetCmdDock
//
void MultiSpeaker::CreateMiniNetCmdDock()
{
  m_miniNetCmdDock = new LogDock(this);
  m_miniNetCmdDock->setWindowTitle("MiniNet Log");
  qobject_cast<DockTitleBar*>(m_miniNetCmdDock->titleBarWidget())->SetTitle("MiniNet Log", 12);
  addDockWidget(Qt::BottomDockWidgetArea, m_miniNetCmdDock);
  m_miniNetCmdDock->setFloating(true);
}
//------------------------------------------------------------------------------
// CreateTitleToolBar
//
void MultiSpeaker::CreateTitleToolBar()
{
  // Add Filter Toolbar
  QToolBar* toolBar = new QToolBar("Speaker Tool Bar", this);
  toolBar->setObjectName("SpeakeToolBar");
  toolBar->setStyleSheet("color: white; background:rgb(34, 34, 34)");
  toolBar->setMovable(false);

  connect(toolBar, SIGNAL(visibilityChanged(bool)), this, SLOT(OnToolBarVisibilityChanged(bool)));

  QLabel* label = new QLabel("MultiSpeaker", toolBar);
  //label->setPixmap(QPixmap(":/PacratDemo/Resources/PacratLogo.png"));
  label->setFont(QFont("Arial Black", 16));
  toolBar->addWidget(label);

  // Spacer
  QWidget* spacer = new QWidget(toolBar);
  spacer->setSizePolicy(QSizePolicy::MinimumExpanding, QSizePolicy::Preferred);
  toolBar->addWidget(spacer);

  QToolButton* btn = new QToolButton(toolBar);
  btn->setObjectName(QStringLiteral("WsdlBtn"));
  btn->setIconSize(QSize(22, 22));
  btn->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
  btn->setPopupMode(QToolButton::DelayedPopup);
  btn->setToolButtonStyle(Qt::ToolButtonTextOnly);
  btn->setAutoRaise(true);
  btn->setText("WSDL");
  connect(btn, SIGNAL(clicked()), this, SLOT(OnWsdl()));
  toolBar->addWidget(btn);

  QIcon icon; icon.addFile(QStringLiteral(":/MultiSpeaker/Resources/network_w.png"), QSize(), QIcon::Normal, QIcon::Off);
  btn = new QToolButton(toolBar);
  btn->setObjectName(QStringLiteral("InitMiniNetBtn"));
  btn->setIcon(icon);
  btn->setIconSize(QSize(22, 22));
  btn->setPopupMode(QToolButton::DelayedPopup);
  btn->setToolButtonStyle(Qt::ToolButtonIconOnly);
  btn->setAutoRaise(true);
  btn->setText("Init");
  btn->setToolTip("Init MiniNet");
  connect(btn, SIGNAL(clicked()), this, SLOT(OnMiniNet()));
  toolBar->addWidget(btn);

  QIcon icon2; icon2.addFile(QStringLiteral(":/MultiSpeaker/Resources/settings.png"), QSize(), QIcon::Normal, QIcon::Off);
  btn = new QToolButton(toolBar);
  btn->setObjectName(QStringLiteral("SettingsBtn"));
  btn->setIcon(icon2);
  btn->setIconSize(QSize(22, 22));
  btn->setPopupMode(QToolButton::DelayedPopup);
  btn->setToolButtonStyle(Qt::ToolButtonIconOnly);
  btn->setAutoRaise(true);
  connect(btn, SIGNAL(clicked()), this, SLOT(OnAbout()));
  toolBar->addWidget(btn);

  addToolBar(Qt::TopToolBarArea, toolBar);
}
//------------------------------------------------------------------------------
// CreateToolBar
//
void MultiSpeaker::CreateToolBar()
{
  QToolBar* tb = new QToolBar("Tool Bar", this);
  tb->setObjectName("ToolBar");
  addToolBar(tb);

  QWidget* spacer = new QWidget(tb);
  spacer->setSizePolicy(QSizePolicy::MinimumExpanding, QSizePolicy::Preferred);
  tb->addWidget(spacer);
}
//------------------------------------------------------------------------------
// CreateWsdlDock
//
void MultiSpeaker::CreateWsdlDock()
{
  m_wsdlDock = new WsdlDock(this);
  WidgetContainer* container = new WidgetContainer(SK_WSDL_DOCK_WC_SPLITTER_STATE, m_wsdlDock);

  QList<QWidget*> list;
  int index = 0;

  // Add Widgets
  foreach (const QString host, Hosts().AllUniqueHostNames())
  {
    WsdlFileView* w = new WsdlFileView(host);
    HeaderContainerWidget* hcw = new HeaderContainerWidget(index++, host);
    hcw->Header()->SetColor(QColor(1,148,199));
    hcw->Header()->SetExpanded(false);
    hcw->Container()->setVisible(false);
    hcw->Container()->layout()->addWidget(w);
    list << hcw;
  }
  container->SetWidgets(list);
  m_wsdlDock->setWidget(container);
  addDockWidget(Qt::BottomDockWidgetArea, m_wsdlDock);
  m_wsdlDock->setFloating(true);
  RestoreState();
}
//------------------------------------------------------------------------------
// EditTimelineEvent
//
void MultiSpeaker::EditTimelineEvent(TimelineEvent& e)
{
  TimelineEvent* req(0);
  TimelineEvent* res(0);
  if (e.Type() == TimelineEvent::Request)
  {
    req = &e;
    res = &Timeline().PairedTimelineEvent(e.Id());
  }
  else
  {
    req = &Timeline().PairedTimelineEvent(e.Id());
    res = &e;
  }

  TimelineEventEditor dlg(*req, *res, this);
  if (dlg.exec())
  {
    req->Copy(dlg.Request());
    res->Copy(dlg.Response());
    Timeline().UpdateTimelineEventPair(*req, *res);
  }
}
//------------------------------------------------------------------------------
// RestoreState
//
void MultiSpeaker::RestoreState()
{
  restoreGeometry(QSettings().value(SK_MAIN_GEOMETRY).toByteArray());
  restoreState(QSettings().value(SK_MAIN_STATE).toByteArray());

  ui.MainSplitter->restoreState(QSettings().value(SK_MAIN_SPLITTER_STATE).toByteArray());
  ui.TimelineSplitter->restoreState(QSettings().value(SK_TIMELINE_SPLITTER_STATE).toByteArray());
}
//------------------------------------------------------------------------------
// SaveState
//
void MultiSpeaker::SaveState()
{
  QSettings().setValue(SK_MAIN_GEOMETRY, saveGeometry());
  QSettings().setValue(SK_MAIN_STATE, saveState());

  QSettings().setValue(SK_MAIN_SPLITTER_STATE, ui.MainSplitter->saveState());
  QSettings().setValue(SK_TIMELINE_SPLITTER_STATE, ui.TimelineSplitter->saveState());
}
//------------------------------------------------------------------------------
// OnAbout
//
void MultiSpeaker::OnAbout()
{
  QMessageBox::about(this, "Speaker DEMO", SOFTWARE_ABOUT);
  QMessageBox::aboutQt(this, "Qt License");
}
//------------------------------------------------------------------------------
// OnClearSettings
//
void MultiSpeaker::OnClearSettings()
{
  if (QMessageBox::Ok == QMessageBox::question(this, "Clear Settings", "All the Settings for Windows Sizes and Docking positions will be reset on exit of application.", QMessageBox::Ok | QMessageBox::Cancel))
      CLEAR_SETTINGS_ON_EXIT = true;
}
//------------------------------------------------------------------------------
// OnHostDoubleClicked
//
void MultiSpeaker::OnHostDoubleClicked(int id)
{
  HostEditor dlg(*Hosts().HostById(id), this);

  if (dlg.exec())
    Hosts().HostById(id)->Copy(dlg.HostRef());
}
//------------------------------------------------------------------------------
// OnHostSceneChanged
//
void MultiSpeaker::OnHostSceneChanged()
{
  // Brute force update for now....nuclear delete and readd.
  if (m_methodDock)
  {
    removeDockWidget(m_methodDock);
    delete m_methodDock;
    m_methodDock = 0;
    CreateMethodDock();
  }

  // Brute force update for now....nuclear delete and readd.
  if (m_wsdlDock)
  {
    removeDockWidget(m_wsdlDock);
    delete m_wsdlDock;
    m_wsdlDock = 0;
    CreateWsdlDock();
  }
}
//------------------------------------------------------------------------------
// OnMiniNet
//
void MultiSpeaker::OnMiniNet()
{
  MiniNetEditor dlg(this);

  if (!dlg.exec())
    return;

  if (dlg.DoStart())
  {
    qDebug() << "MiniNetEditor init";
    Hosts().SetMiniNetApp(dlg.App());
    Hosts().SetMiniNetScriptFile(dlg.ScriptFile());
    Hosts().SetMiniNetConfFile(dlg.ConfFile());
    Hosts().SetMiniNetNetworkId(dlg.NetworkId());
    Hosts().StartMiniNet();/*dlg.CmdLine());*/
  }
  else if (dlg.DoStop())
  {
    qDebug() << "MiniNetEditor stop";
    Hosts().StopMiniNet();
  }
}
//------------------------------------------------------------------------------
// OnTimelineEventListViewDoubleClicked
//
void MultiSpeaker::OnTimelineEventListViewDoubleClicked(const QModelIndex& index)
{
  if (!index.isValid())
    return;

  int timelineEventId = index.data(Qt::UserRole + 1).toInt();
  TimelineEvent& te = Timeline().TimelineEventById(timelineEventId);
  EditTimelineEvent(te);
}
//------------------------------------------------------------------------------
// OnWsdlFileChanged
//
void MultiSpeaker::OnWsdlFileChanged(const QString& host)
{
  QList<HostMethodListWidget*> list = findChildren<HostMethodListWidget*>();
  foreach (HostMethodListWidget* w, list)
  {
    if (w->Host() == host)
    {
      w->Update();
        break;
    }
  }
}
