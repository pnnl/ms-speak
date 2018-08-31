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
// Summary: MultiSpeaker.cpp
//-------------------------------------------------------------------------------

#include <QDir>
#include <QFileDialog>
#include <QFileSystemModel>
#include <QInputDialog>
#include <QLabel>
#include <QListView>
#include <QMessageBox>
#include <QSettings>
#include <QSslError>
#include <QStandardItemModel>
#include <QStandardItem>
#include <QToolButton>

#include "CertInfoDlg.h"
#include "DockTitleBar.h"
#include "HeaderContainerWidget.h"
#include "Host.h"
#include "HostEditor.h"
#include "HostMethodListWidget.h"
#include "HostScene.h"
#include "HttpOutEditor.h"
#include "MiniNetEditor.h"
#include "MultiSpeaker.h"
#include "Settings.h"
#include "SslErrorDlg.h"
#include "TimelineEventEditor.h"
#include "TimelineScene.h"
#include "Utils.h"
#include "Version.h"
#include "WidgetContainer.h"
#include "WebServiceInfo.h"
#include "WsdlFile.h"
#include "WsdlFileView.h"

static bool CLEAR_SETTINGS_ON_EXIT = false;

//------------------------------------------------------------------------------
// MultiSpeaker
//
MultiSpeaker::MultiSpeaker(QWidget* parent)
  : QMainWindow(parent),
	m_clearSettingsShortcut(QKeySequence("Ctrl+Shift+C"), this, SLOT(OnClearSettings())),
	m_functionBlockDock(Q_NULLPTR),
	m_logDock(Q_NULLPTR),
	m_methodDock(Q_NULLPTR),
	m_miniNetCmdDock(Q_NULLPTR),
	m_wsdlDock(Q_NULLPTR)
{
	ui.setupUi(this);
	Utils::CreateRootHomePath(); // Make sure the .MultiSpeaker dir exists

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
	connect(&Hosts(), SIGNAL(LogMsg(const QString&)), this, SLOT(OnLogMsg(const QString&)));
	connect(&Hosts(), SIGNAL(MiniNetError(const QString&)), this, SLOT(OnMiniNetMsg(const QString&)));
	connect(&Hosts(), SIGNAL(MiniNetFinished(const QString&)), this, SLOT(OnMiniNetMsg(const QString&)));
	connect(&Hosts(), SIGNAL(MiniNetStdErr(const QString&)), this, SLOT(OnMiniNetMsg(const QString&)));
	connect(&Hosts(), SIGNAL(MiniNetStdOut(const QString&)), this, SLOT(OnMiniNetMsg(const QString&)));
	connect(&Hosts(), SIGNAL(TimelineEventSendSslErrors(const QList<QSslError>&, const QSslCipher&, const QList<QSslCertificate>&)), this, SLOT(OnTimelineEventSendSslErrors(const QList<QSslError>&, const QSslCipher&, const QList<QSslCertificate>&)));

	connect(&Timeline(), SIGNAL(Error(const QString&)), this, SLOT(OnTimelineError(const QString&)));
	connect(&Timeline(), SIGNAL(EventUpdated(TimelineEvent&)), this, SLOT(OnTimelineEventDoubleClicked(TimelineEvent&)));
	connect(&Timeline(), SIGNAL(EventProcessed(TimelineEvent&)), &Hosts(), SLOT(OnTimelineEventProcessed(TimelineEvent&)));
	connect(&Timeline(), SIGNAL(TimelineMouseMove(int)), this, SLOT(OnTimelineMouseMove(int)));
	connect(&Timeline(), SIGNAL(TimeSpanChanged(int)), this, SLOT(OnTimelineSpanChanged(int)));

	connect(&WsInfo(), SIGNAL(WsdlFileChanged(const QString&)), this, SLOT(OnWsdlFileChanged(const QString&)));

	MethodDockRef().show();

	ui.TheTimelineView->setMinimumSize(200, Timeline().SceneHeight());

	ui.TimelineEventListView->setModel(&Timeline().EventModel());
	ui.TimelineEventListView->setEditTriggers(QAbstractItemView::NoEditTriggers);
	connect(ui.TimelineEventListView, SIGNAL(doubleClicked(const QModelIndex&)), this, SLOT(OnTimelineEventListViewDoubleClicked(const QModelIndex&)));

	connect(ui.TimelineSpanBtn, SIGNAL(clicked()), this, SLOT(OnTimelineSpanBtnClicked()));

	RestoreState();
	Timeline().SetParentWidget(this); // Need to have this happen so signals of timeline buttons connect to timeline scene
	Timeline().Stop(); // begin in stop state as the

	ui.TimelineSpanBtn->setText(QTime(0, 0, 0, 0).addMSecs(Timeline().TimelineSpan()).toString("h:mm:ss"));
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
  toolBar->setObjectName("SpeakerToolBar");
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

  // LGI This was prep work for new versioning system...comment out for now so release can be clean
  //// Test
  //QToolButton* testBtn = new QToolButton(toolBar);
  //testBtn->setObjectName(QStringLiteral("WsdlTestBtn"));
  //testBtn->setIconSize(QSize(24, 24));
  //testBtn->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
  //testBtn->setPopupMode(QToolButton::DelayedPopup);
  //testBtn->setToolButtonStyle(Qt::ToolButtonTextOnly);
  //testBtn->setAutoRaise(true);
  //testBtn->setText("WSDL Test");
  //connect(testBtn, SIGNAL(clicked()), this, SLOT(OnWsdlTest()));
  //toolBar->addWidget(testBtn);

  // Wsdl
  QToolButton* btn = new QToolButton(toolBar);
  btn->setObjectName(QStringLiteral("WsdlBtn"));
  btn->setIconSize(QSize(24, 24));
  btn->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
  btn->setPopupMode(QToolButton::DelayedPopup);
  btn->setToolButtonStyle(Qt::ToolButtonTextOnly);
  btn->setAutoRaise(true);
  btn->setText("WSDLs");

  btn->setToolTip("Show WSDL Dock"); // chm

  connect(btn, SIGNAL(clicked()), this, SLOT(OnWsdl()));
  toolBar->addWidget(btn);

  // Don't need this functionality at the moment
  // MiniNet
  //QIcon icon; icon.addFile(QStringLiteral(":/MultiSpeaker/Resources/network_w.png"), QSize(), QIcon::Normal, QIcon::Off);
  //btn = new QToolButton(toolBar);
  //btn->setObjectName(QStringLiteral("InitMiniNetBtn"));
  //btn->setIcon(icon);
  //btn->setIconSize(QSize(24, 24));
  //btn->setPopupMode(QToolButton::DelayedPopup);
  //btn->setToolButtonStyle(Qt::ToolButtonIconOnly);
  //btn->setAutoRaise(true);
  //btn->setText("Init");
  //btn->setToolTip("Init MiniNet");
  //connect(btn, SIGNAL(clicked()), this, SLOT(OnMiniNet()));
  //toolBar->addWidget(btn);

  // chm 7.30.18, use
  // Don't need this functionality at the moment
  // HttpOut
  QIcon iconHttpOut; iconHttpOut.addFile(QStringLiteral(":/MultiSpeaker/Resources/httpout.png"), QSize(), QIcon::Normal, QIcon::Off);
  btn = new QToolButton(toolBar);
  btn->setObjectName(QStringLiteral("HttpOutBtn"));
  btn->setIcon(iconHttpOut);
  btn->setIconSize(QSize(24, 24));
  btn->setPopupMode(QToolButton::DelayedPopup);
  btn->setToolButtonStyle(Qt::ToolButtonIconOnly);
  btn->setAutoRaise(true);
  btn->setText("Http");
  btn->setToolTip("Configure Http Output Settings");
  connect(btn, SIGNAL(clicked()), this, SLOT(OnHttpOut()));
  toolBar->addWidget(btn);

  // Open
  btn = new QToolButton(toolBar);
  QIcon iconOpen; iconOpen.addFile(QStringLiteral(":/MultiSpeaker/Resources/fileopen.png"), QSize(), QIcon::Normal, QIcon::Off);
  btn->setObjectName(QStringLiteral("OpenScenarioBtn"));
  btn->setIcon(iconOpen);
  btn->setIconSize(QSize(24, 24));
  btn->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
  btn->setPopupMode(QToolButton::DelayedPopup);
  btn->setToolButtonStyle(Qt::ToolButtonIconOnly);
  btn->setAutoRaise(true);
  btn->setText("Open");
  btn->setToolTip("Open Scenario Settings");
  connect(btn, SIGNAL(clicked()), this, SLOT(OnScenarioOpen()));
  toolBar->addWidget(btn);

  // Save
  btn = new QToolButton(toolBar);
  QIcon iconSave; iconSave.addFile(QStringLiteral(":/MultiSpeaker/Resources/filesave.png"), QSize(), QIcon::Normal, QIcon::Off);
  btn->setObjectName(QStringLiteral("SaveScenarioBtn"));
  btn->setIcon(iconSave);
  btn->setIconSize(QSize(24, 24));
  btn->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
  btn->setPopupMode(QToolButton::DelayedPopup);
  btn->setToolButtonStyle(Qt::ToolButtonIconOnly);
  btn->setAutoRaise(true);
  btn->setText("Save");
  btn->setToolTip("Save Scenario Settings");
  connect(btn, SIGNAL(clicked()), this, SLOT(OnScenarioSave()));
  toolBar->addWidget(btn);

  // Settings
  QIcon icon2; icon2.addFile(QStringLiteral(":/MultiSpeaker/Resources/settings.png"), QSize(), QIcon::Normal, QIcon::Off);
  btn = new QToolButton(toolBar);
  btn->setObjectName(QStringLiteral("SettingsBtn"));
  btn->setIcon(icon2);
  btn->setIconSize(QSize(24, 24));
  btn->setPopupMode(QToolButton::DelayedPopup);
  btn->setToolButtonStyle(Qt::ToolButtonIconOnly);
  btn->setAutoRaise(true);
  btn->setToolTip("Help/About");
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
// DisplayCertChainInfo
//
void MultiSpeaker::DisplayCertChainInfo(const QSslCipher& cipher, const QList<QSslCertificate>& certChain)
{
  CertInfoDlg dlg;
  QSslCipher theCipher;
  dlg.SetCertificateChain(certChain);
  dlg.SetCipherInfo((theCipher = cipher));
  dlg.exec();
}
//-------------------------------------------------------------------------------
// DisplayHostSslErrors
//
void MultiSpeaker::DisplayHostSslErrors(const QList<QSslError>& errors)
{
  if (QSettings().value(SK_IGNORE_SSL_SELF_CERT_ERROR, false).toBool())
  {
    if (errors.count() == 1)
    {
      QSslError error = errors.at(0);
      qDebug() << "MainWindow::DisplayHostSslErrors()" << error.error() << error.errorString();
      if (error.error() == QSslError::SelfSignedCertificate)
      {
        // LGI TODO
        //m_session.IgnoreSslErrors();
        return;
      }
    }
  }
  SslErrorDlg dlg(this);
  connect(&dlg, SIGNAL(CertChainInfo()), this, SLOT(OnCertChainInfo()));
  dlg.AddErrors(errors);

  if (dlg.exec() == QDialog::Accepted) // Accepted means 'Ignored' buttton i.e. ignore the ssl errors
  {
    if (dlg.IgnoreSelfSignedCert())
      QSettings().setValue(SK_IGNORE_SSL_SELF_CERT_ERROR, true);
    else
      QSettings().setValue(SK_IGNORE_SSL_SELF_CERT_ERROR, false);
    // LGI TODO
    //m_session.IgnoreSslErrors();
  }
}
//------------------------------------------------------------------------------
// EditTimelineEvent
//
void MultiSpeaker::EditTimelineEvent(TimelineEvent& e)
{
	if (Timeline().IsRunning())
	{
		QMessageBox::warning(this, "Timeline", "Events may not be inserted while Scheduler is running.");
		return;
	}

	TimelineEvent* req(Q_NULLPTR);
	TimelineEvent* res(Q_NULLPTR);
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
	//ui.TimelineSplitter->restoreState(QSettings().value(SK_TIMELINE_SPLITTER_STATE).toByteArray());
}
//------------------------------------------------------------------------------
// SaveState
//
void MultiSpeaker::SaveState()
{
	QSettings().setValue(SK_MAIN_GEOMETRY, saveGeometry());
	QSettings().setValue(SK_MAIN_STATE, saveState());
	QSettings().setValue(SK_MAIN_SPLITTER_STATE, ui.MainSplitter->saveState());
	//QSettings().setValue(SK_TIMELINE_SPLITTER_STATE, ui.TimelineSplitter->saveState());
}
//------------------------------------------------------------------------------
// OnAbout
//
void MultiSpeaker::OnAbout()
{
	QMessageBox::about(this, "MultiSpeaker", SOFTWARE_ABOUT);
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
// OnHideTimestampLabel
//
void MultiSpeaker::OnHideTimestampLabel()
{
	ui.TimestampLabel->hide();
}
//------------------------------------------------------------------------------
// OnHostSceneChanged - when drag/drop a function block onto Topology
//
void MultiSpeaker::OnHostSceneChanged()
{
    // Brute force update for now....nuclear delete and readd.
    if (m_methodDock)
    {
        removeDockWidget(m_methodDock);
        delete m_methodDock;
        m_methodDock = Q_NULLPTR;
        CreateMethodDock();
    }

    // Brute force update for now....nuclear delete and readd.
    if (m_wsdlDock)
    {
        removeDockWidget(m_wsdlDock);
        delete m_wsdlDock;
        m_wsdlDock = Q_NULLPTR;
        CreateWsdlDock();
    }
}
//------------------------------------------------------------------------------
// OnHostDoubleClicked
//
void MultiSpeaker::OnHostDoubleClicked(int id)
{
	HttpOutEditor dlg(*Hosts().HostById(id), this);
	if (dlg.exec())
	{
		Hosts().HostById(id)->Copy(dlg.HostRef());
	}
}
//------------------------------------------------------------------------------
// OnHttpOut
bool MultiSpeaker::OnHttpOut()
{ 
	HttpOutEditor dlg(this);
	if (dlg.exec())
	{
		// Remember a few Settings for convenience
		QSettings s;
		QStringList ipList = dlg.getIpAddresses();
		s.setValue(SK_HTTP_OUT_SSL, dlg.HttpSslEnabled());

		if( !ipList.contains(dlg.HttpRequestIp()) )
			s.setValue(SK_HTTP_OUT_REQ_IP, dlg.HttpRequestIp());
		s.setValue(SK_HTTP_OUT_REQ_PORT, dlg.HttpRequestPort());
		s.setValue(SK_HTTP_OUT_REQ_FLAG, dlg.HttpRequestEnabled());

		if( !ipList.contains(dlg.HttpResponseIp()) )
			s.setValue(SK_HTTP_OUT_RES_IP, dlg.HttpResponseIp());
		s.setValue(SK_HTTP_OUT_RES_PORT, dlg.HttpResponsePort());
		s.setValue(SK_HTTP_OUT_RES_FLAG, dlg.HttpResponseEnabled());

		return true;
	}
	return false;
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
// OnScenarioOpen
//
void MultiSpeaker::OnScenarioOpen()
{
	QString seedFile = QSettings().value(SK_SCENARIO_FILENAME, QDir::homePath()).toString();

	// Load file
	QString fileName = QFileDialog::getOpenFileName(this, "Select File", seedFile, "MSS (*.mss);; All (*.*)");

	if (fileName.isEmpty())
		return;

	QFile file(fileName);
	if (!file.open(QIODevice::ReadOnly))
		return;

	QDataStream in(&file);
	in.setVersion(QDataStream::Qt_5_2);

	// Read and check the header
	quint32 magic;
	in >> magic;
	if (magic != SCENARIO_SAVE_MAGIC)
	{
		QMessageBox::critical(this, "Unknown File", QString("File, %1, is of unknown format").arg(fileName));
		return;
	}

	// Read the version
	qint32 version;
	in >> version;
	if (version != SCENARIO_SAVE_VERSION)
	{
		QMessageBox::critical(this, "Version Mismatch", QString("Unsupported version: %1.\nExpected version was %2").arg(version).arg(SCENARIO_SAVE_VERSION));
		return;
	}

	Hosts().Clear();
	Timeline().Clear();

	// Read the data
	in >> Hosts();
	in >> Timeline();
	file.close();
	OnHostSceneChanged(); // Force Update
	Timeline().Update(true, true); // Force Update
	OnTimelineSpanChanged(Timeline().TimelineSpan());
}
//------------------------------------------------------------------------------
// OnScenarioSave
//
void MultiSpeaker::OnScenarioSave()
{
	QString seedFile = QSettings().value(SK_SCENARIO_FILENAME, QDir::homePath()).toString();

	// Load file
	QString fileName = QFileDialog::getSaveFileName(this, "Select File", seedFile, "MSS (*.mss);; All (*.*)");

	if (fileName.isEmpty())
		return;

	QSettings().setValue(SK_SCENARIO_FILENAME, fileName);

	QFile file(fileName);

	if (!file.open(QIODevice::WriteOnly))
	{
		qDebug() << file.error() << file.errorString();
		return;
	}
	QDataStream out(&file);
	out.setVersion(QDataStream::Qt_5_2);

	// Write a header with a "magic number" and a version
	out << SCENARIO_SAVE_MAGIC;
	out << SCENARIO_SAVE_VERSION;

	// Write the data
	out << Hosts();
	out << Timeline();
	file.close();
}
//------------------------------------------------------------------------------
// OnTimelineSpanBtnClicked
//
void MultiSpeaker::OnTimelineSpanBtnClicked()
{
	Timeline().SetTimelineSpan(QInputDialog::getInt(this, "Change Timeline Duration", "Time Span (Minutes)",
		Timeline().TimelineSpan() / 60000,
		(Timeline().MaxTimeStamp() / 60000) + 1) * 60000); // Convert from ms to min and back
	OnTimelineSpanChanged(Timeline().TimelineSpan());
	Timeline().Update(true, false);
}
//------------------------------------------------------------------------------
// OnTimelineSpanChanged
//
void MultiSpeaker::OnTimelineSpanChanged(int timeSpan)
{
	ui.TimelineSpanBtn->setText(QTime(0, 0, 0, 0).addMSecs(timeSpan).toString("h:mm:ss"));
}
//------------------------------------------------------------------------------
// OnTimelineEventSendSslErrors
//
void MultiSpeaker::OnTimelineEventSendSslErrors(const QList<QSslError>& errors, const QSslCipher& cipher, const QList<QSslCertificate>& certChain)
{
	QStringList list;
	foreach(QSslError error, errors)
	{
		qDebug() << error.errorString();
		list << error.errorString();
	}
	DisplayCertChainInfo(cipher, certChain);
	DisplayHostSslErrors(errors);
	//DisplayError(QString("%1 SslErrors\n%2").arg(key).arg(list.join('\n')));
}
//------------------------------------------------------------------------------
// OnTimelineError
//
void MultiSpeaker::OnTimelineError(const QString& error)
{
	QMessageBox::warning(this, "Error", error);
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
// OnTimelineMouseMove
//
void MultiSpeaker::OnTimelineMouseMove(int timeStamp)
{
	ui.TimestampLabel->show();
	ui.TimestampLabel->setText(QTime(0,0,0,0).addMSecs(timeStamp).toString("h:mm:ss"));
	QTimer::singleShot(3000, this, SLOT(OnHideTimestampLabel()));
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
//------------------------------------------------------------------------------
// OnWsdlTest
//
void MultiSpeaker::OnWsdlTest()
{
	QString rootPath = "c:/Develop/MultiSpeaker";
	QScopedPointer<QFileSystemModel> model(new QFileSystemModel);
	model->setRootPath(rootPath);
	model->setNameFilters(QStringList() << "*.wsdl");
	model->setNameFilterDisables(false);

	QDialog dlg(this);

	QVBoxLayout* layout = new QVBoxLayout(&dlg);
	layout->setSpacing(2);
	layout->setContentsMargins(11, 11, 11, 11);
	layout->setObjectName(QStringLiteral("Layout"));
	layout->setContentsMargins(4, 4, 4, 4);

	QHBoxLayout* hLayout = new QHBoxLayout(&dlg);
	hLayout->setSpacing(2);
	hLayout->setContentsMargins(11, 11, 11, 11);
	hLayout->setObjectName(QStringLiteral("Layout1"));
	hLayout->setContentsMargins(4, 4, 4, 4);

	QLabel* label = new QLabel("Root", &dlg);
	hLayout->addWidget(label);

	QLineEdit* edit = new QLineEdit(&dlg);
	edit->setText(QDir::toNativeSeparators(rootPath));
	hLayout->addWidget(edit);

	QToolButton* btn = new QToolButton(&dlg);
	btn->setText("Browse");
	connect(btn, SIGNAL(clicked()), this, SLOT(OnBrowseRoot()));
	hLayout->addWidget(btn);

	layout->addLayout(hLayout);

	QTreeView* tree = new QTreeView(&dlg);
	tree->setModel(model.data());
	tree->setRootIndex(model->index(rootPath));
	layout->addWidget(tree);

	dlg.exec();
}
void MultiSpeaker::OnBrowseRoot()
{
	QString rootPath = QFileDialog::getExistingDirectory(this, "Browse For Root Directory of MultiSpeak Wsdl Files.");
	if (rootPath.isEmpty())
		return;

	if (QDialog* dlg = findChild<QDialog*>())
	{
		if (QTreeView* view = findChild<QTreeView*>())
		{
			if (QFileSystemModel* model = qobject_cast<QFileSystemModel*>(view->model()))
			{
				model->setRootPath(rootPath);
				view->setRootIndex(model->index(rootPath));
				if (QLineEdit* edit = dlg->findChild<QLineEdit*>())
					edit->setText(QDir::toNativeSeparators(rootPath));
			}
		}
	}
}

