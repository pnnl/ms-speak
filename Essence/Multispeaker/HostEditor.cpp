//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: HostEditor
//

#include "HostEditor.h"
#include "WebServiceInfo.h"

//------------------------------------------------------------------------------
// HostEditor
//
HostEditor::HostEditor(const Host& host, QWidget* parent)
  : QDialog(parent),
  m_host(host)
{
  ui.setupUi(this);
  ui.TitleLabel->setText(WsInfo().FullNameDashSep(host.Name()));

  ui.ApacheCheck->setChecked(host.AppFlag(Host::Apache));
  ui.FireFoxCheck->setChecked(host.AppFlag(Host::FireFox));
  ui.TerminalCheck->setChecked(host.AppFlag(Host::Terminal));
  ui.WireSharkCheck->setChecked(host.AppFlag(Host::WireShark));

  connect(ui.buttonBox, SIGNAL(accepted()), this, SLOT(accept()));
  connect(ui.buttonBox, SIGNAL(rejected()), this, SLOT(reject()));

  connect(ui.ApacheCheck, SIGNAL(toggled(bool)), this, SLOT(OnCheckToggled(bool)));
  connect(ui.FireFoxCheck, SIGNAL(toggled(bool)), this, SLOT(OnCheckToggled(bool)));
  connect(ui.TerminalCheck, SIGNAL(toggled(bool)), this, SLOT(OnCheckToggled(bool)));
  connect(ui.WireSharkCheck, SIGNAL(toggled(bool)), this, SLOT(OnCheckToggled(bool)));
}
//------------------------------------------------------------------------------
// ~HostEditor
//
HostEditor::~HostEditor()
{
}
//------------------------------------------------------------------------------
// OnCheckToggled
//
void HostEditor::OnCheckToggled(bool checked)
{
  Q_UNUSED(checked);
  if (sender() == ui.ApacheCheck) {if (checked) m_host.SetAppFlag(Host::Apache); else m_host.SetAppFlags(m_host.AppFlags() & (~Host::Apache));}
  else if (sender() == ui.FireFoxCheck) {if (checked) m_host.SetAppFlag(Host::FireFox); else m_host.SetAppFlags(m_host.AppFlags() & (~Host::FireFox));}
  else if (sender() == ui.TerminalCheck) {if (checked) m_host.SetAppFlag(Host::Terminal); else m_host.SetAppFlags(m_host.AppFlags() & (~Host::Terminal));}
  else if (sender() == ui.WireSharkCheck) {if (checked) m_host.SetAppFlag(Host::WireShark); else m_host.SetAppFlags(m_host.AppFlags() & (~Host::WireShark));}
}
