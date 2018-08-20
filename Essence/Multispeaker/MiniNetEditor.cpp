//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: MiniNetEditor
//

#include <QFileDialog>
#include <QMessageBox>
#include <QTimer>

#include "HostScene.h"
#include "MiniNetEditor.h"

//------------------------------------------------------------------------------
// MiniNetEditor
//
MiniNetEditor::MiniNetEditor(QWidget* parent)
  : QDialog(parent),
  m_doStart(false),
  m_doStop(false)
{
  ui.setupUi(this);
  QTimer::singleShot(0, this, SLOT(OnInit())); // force update after the m_wsdlFile has been parsed and instantiated in its constructor
}
//------------------------------------------------------------------------------
// ~MiniNetEditor
//
MiniNetEditor::~MiniNetEditor()
{
}
//------------------------------------------------------------------------------
// OnConfFileBrowse
//
void MiniNetEditor::OnConfFileBrowse()
{
  QString seedFile = Hosts().MiniNetConfFile();

  // Load file
  QString fileName = QFileDialog::getSaveFileName(this, "Select Conf File", seedFile, "Conf (*.cfg);; (*.conf);; All (*.*)");

  if (fileName.isEmpty())
    return;

  ui.ConfFileEdit->setText(QDir::toNativeSeparators(fileName));
  ui.ConfFileEdit->setToolTip(QDir::toNativeSeparators(fileName));

  Hosts().SetMiniNetConfFile(fileName);
  ui.CmdLineEdit->setPlainText(Hosts().MiniNetCmdLine(ui.ScriptFileEdit->text(), ui.ConfFileEdit->text(), ui.NetworkIdEdit->text()));
}
//------------------------------------------------------------------------------
// OnHostIpEditFinished
//
void MiniNetEditor::OnHostIpEditFinished()
{
  Hosts().SetHostIp(ui.HostIpEdit->text());
}
//------------------------------------------------------------------------------
// OnHostPortValueChanged
//
void MiniNetEditor::OnHostPortValueChanged(int port)
{
  Hosts().SetHostPort(ui.HostPortSpin->value());
}
//------------------------------------------------------------------------------
// OnInit
//
void MiniNetEditor::OnInit()
{
  if (Hosts().MiniNetRunning())
  {
    ui.StartBtn->hide();
    ui.AppEdit->setEnabled(false);
    ui.ConfFileEdit->setEnabled(false);
    ui.HostIpEdit->setEnabled(false);
    ui.HostPortSpin->setEnabled(false);
    ui.NetworkIdEdit->setEnabled(false);
    ui.ScriptFileEdit->setEnabled(false);
    ui.CmdLineEdit->setEnabled(false);
  }
  else
    ui.StopBtn->hide();

  ui.AppEdit->setText(Hosts().MiniNetApp());
  ui.ConfFileEdit->setText(QDir::toNativeSeparators(Hosts().MiniNetConfFile()));
  ui.ConfFileEdit->setToolTip(QDir::toNativeSeparators(Hosts().MiniNetConfFile()));
  ui.EndPointsEdit->appendPlainText(Hosts().HostEndPoints().join("\n"));
  ui.HostEdit->setText(QString::number(Hosts().AllHosts().count()));
  ui.HostRolesEdit->appendPlainText(Hosts().HostRoles().join("\n"));
  ui.HostIpEdit->setText(Hosts().HostIp());
  ui.HostPortSpin->setValue(Hosts().HostPort());
  ui.NetworkIdEdit->setText(Hosts().MiniNetNetworkId());
  ui.ApacheEdit->setText(Hosts().HostIdsByAppMode(Host::Apache).join(","));
  ui.FirefoxEdit->setText(Hosts().HostIdsByAppMode(Host::FireFox).join(","));
  ui.ScriptFileEdit->setText(QDir::toNativeSeparators(Hosts().MiniNetScriptFile()));
  ui.ScriptFileEdit->setToolTip(QDir::toNativeSeparators(Hosts().MiniNetScriptFile()));
  ui.TerminalEdit->setText(Hosts().HostIdsByAppMode(Host::Terminal).join(","));
  ui.WiresharkEdit->setText(Hosts().HostIdsByAppMode(Host::WireShark).join(","));

  ui.CmdLineEdit->setPlainText(Hosts().MiniNetCmdLine(ui.ScriptFileEdit->text(), ui.ConfFileEdit->text(), ui.NetworkIdEdit->text()));

  connect(ui.AppEdit, SIGNAL(editingFinished()), this, SLOT(OnUpdateCmdLineEdit()));
  connect(ui.CancelBtn, SIGNAL(clicked()), this, SLOT(reject()));
  connect(ui.ConfFileBrowseBtn, SIGNAL(clicked()), this, SLOT(OnConfFileBrowse()));
  connect(ui.ConfFileEdit, SIGNAL(editingFinished()), this, SLOT(OnUpdateCmdLineEdit()));
  connect(ui.HostIpEdit, SIGNAL(editingFinished()), this, SLOT(OnHostIpEditFinished()));
  connect(ui.HostPortSpin, SIGNAL(valueChanged(int)), this, SLOT(OnHostPortValueChanged(int)));
  connect(ui.NetworkIdEdit, SIGNAL(editingFinished()), this, SLOT(OnUpdateCmdLineEdit()));
  connect(ui.ScriptFileBrowseBtn, SIGNAL(clicked()), this, SLOT(OnScriptFileBrowse()));
  connect(ui.ScriptFileEdit, SIGNAL(editingFinished()), this, SLOT(OnUpdateCmdLineEdit()));
  connect(ui.StartBtn, SIGNAL(clicked()), this, SLOT(OnStartClicked()));
  connect(ui.StopBtn, SIGNAL(clicked()), this, SLOT(OnStopClicked()));
}
//------------------------------------------------------------------------------
// OnScriptFileBrowse
//
void MiniNetEditor::OnScriptFileBrowse()
{
  QString seedFile = Hosts().MiniNetScriptFile();

  // Load file
  QString fileName = QFileDialog::getOpenFileName(this, "Select Python Script File (decouple.py)", seedFile, "Python (*.py);; All (*.*)");

  if (fileName.isEmpty())
    return;

  ui.ScriptFileEdit->setText(QDir::toNativeSeparators(fileName));
  ui.ScriptFileEdit->setToolTip(QDir::toNativeSeparators(fileName));
  ui.CmdLineEdit->setPlainText(Hosts().MiniNetCmdLine(ui.ScriptFileEdit->text(), ui.ConfFileEdit->text(), ui.NetworkIdEdit->text()));
}
//------------------------------------------------------------------------------
// OnStartClicked
//
void MiniNetEditor::OnStartClicked()
{
  if (App().isEmpty() || ScriptFile().isEmpty() || ConfFile().isEmpty() || NetworkId().isEmpty())
  {
    QMessageBox::critical(this, "Incomplete Information", "Script File, Conf File, and Network Id Must Be Set Before Start can be Successful.");
  }
  else
  {
    m_doStart = true;
    accept();
  }
}
//------------------------------------------------------------------------------
// OnStopClicked
//
void MiniNetEditor::OnStopClicked()
{
  m_doStop = true;
  accept();
}
//------------------------------------------------------------------------------
// OnUpdateCmdLineEdit
//
void MiniNetEditor::OnUpdateCmdLineEdit()
{
  ui.CmdLineEdit->setPlainText(Hosts().MiniNetCmdLine(ui.ScriptFileEdit->text(), ui.ConfFileEdit->text(), ui.NetworkIdEdit->text()));
}

