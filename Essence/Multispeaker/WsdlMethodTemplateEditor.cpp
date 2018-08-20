//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: WsdlMethodTemplateEditor
//

#include <QSettings>
#include <QTimer>

#include "Settings.h"
#include "WsdlFile.h"
#include "WsdlMethodTemplateEditor.h"

//------------------------------------------------------------------------------
// WsdlMethodTemplateEditor
//
WsdlMethodTemplateEditor::WsdlMethodTemplateEditor(WsdlFile* wsdlFile, const QString& method, QWidget* parent)
  : QDialog(parent),
  m_method(method),
  m_wsdlFile(wsdlFile)
{
  ui.setupUi(this);
  setWindowTitle(method);
  connect(ui.buttonBox, SIGNAL(accepted()), this, SLOT(OnAccept()));
  connect(ui.buttonBox, SIGNAL(rejected()), this, SLOT(OnReject()));

  QTimer::singleShot(0, this, SLOT(OnInit())); // force update after the m_wsdlFile has been parsed and instantiated in its constructor
}
//------------------------------------------------------------------------------
// ~WsdlMethodTemplateEditor
//
WsdlMethodTemplateEditor::~WsdlMethodTemplateEditor()
{
}
//------------------------------------------------------------------------------
// RestoreState
//
void WsdlMethodTemplateEditor::RestoreState()
{
  restoreGeometry(QSettings().value(SK_WMTE_GEOMETRY).toByteArray());
}
//------------------------------------------------------------------------------
// SaveState
//
void WsdlMethodTemplateEditor::SaveState()
{
  QSettings().setValue(SK_WMTE_GEOMETRY, saveGeometry());
}
//------------------------------------------------------------------------------
// OnAccept
//
void WsdlMethodTemplateEditor::OnAccept()
{
  m_wsdlFile->SaveMethodTemplate(m_method, ui.View->Document());
  SaveState();
  accept();
}
//------------------------------------------------------------------------------
// OnInit
//
void WsdlMethodTemplateEditor::OnInit()
{
  RestoreState();
  ui.View->Init(m_wsdlFile->HostName(), m_method, m_wsdlFile->MethodTemplate(m_method));
}
