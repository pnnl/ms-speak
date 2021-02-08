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
// Summary: MiniNetEditor.cpp
//-------------------------------------------------------------------------------

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
    Q_UNUSED(port);
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

