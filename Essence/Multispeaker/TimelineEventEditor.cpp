//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: TimelineEventEditor
//

#include <QTime>
#include <QTimer>

#include "HostScene.h"
#include "TimelineEventEditor.h"

const int HOST_NODE_SIZE = 50;
const int ITEM_HTTP_ROLE = Qt::UserRole + 2; // Request or Response
const int ITEM_TYPE_ROLE = Qt::UserRole + 3; // Header or Param

//------------------------------------------------------------------------------
// TimelineEventEditor
//
TimelineEventEditor::TimelineEventEditor(const TimelineEvent& request, const TimelineEvent& response, QWidget* parent)
  : QDialog(parent),
  m_request(request),
  m_response(response)
{
  ui.setupUi(this);
  ui.TimeCombo->hide(); // Don't want to implement yet

  ui.TitleHeader->SetTitle(request.Method(), 12);
  ui.TitleHeader->SetColor(QColor(1,164,148));
  ui.RequestHeader->SetTitle("Request", 10);
  ui.ResponseHeader->SetTitle("Response", 10);

  //ui.Header->SetColor(QColor(120,120,120));

  // Time
  ui.TimeStampEdit->setTime(QTime(0,0).addMSecs(request.TimeStamp()));
  ui.ResponseDelayTimeEdit->setTime(QTime(0,0).addMSecs(request.TimeStamp() - response.TimeStamp()));

  // SRC and DST Combos
  QFont f = ui.DstCombo->font();
  f.setPointSize(24);
  ui.DstCombo->setIconSize(QSize(HOST_NODE_SIZE, HOST_NODE_SIZE));
  ui.DstCombo->setFont(f);
  ui.SrcCombo->setIconSize(QSize(HOST_NODE_SIZE, HOST_NODE_SIZE));
  ui.SrcCombo->setFont(f);

  int dstIdx = 0;
  int srcIdx = 0;
  foreach (const Host* host, Hosts().AllHosts())
  {
    if (host->Name() == request.Host())
      ui.DstCombo->insertItem(dstIdx++, QIcon(Hosts().CreateHostPixmap(*host, HOST_NODE_SIZE, false)), "", host->Id());

    ui.SrcCombo->insertItem(srcIdx++, QIcon(Hosts().CreateHostPixmap(*host, HOST_NODE_SIZE, false)), "", host->Id());
  }

  dstIdx = ui.DstCombo->findData(request.DstHostId());
  ui.DstCombo->setCurrentIndex((dstIdx == -1) ? 0 : dstIdx);

  srcIdx = ui.SrcCombo->findData(request.SrcHostId());
  ui.SrcCombo->setCurrentIndex((srcIdx == -1) ? 0 : srcIdx);

  connect(ui.buttonBox, SIGNAL(accepted()), this, SLOT(OnAccept()));
  connect(ui.buttonBox, SIGNAL(rejected()), this, SLOT(OnReject()));
  QTimer::singleShot(0, this, SLOT(OnInit())); // force update after the m_wsdlFile has been parsed and instantiated in its constructor
}
//------------------------------------------------------------------------------
// ~TimelineEventEditor
//
TimelineEventEditor::~TimelineEventEditor()
{
}
//------------------------------------------------------------------------------
// Request
//
const TimelineEvent& TimelineEventEditor::Request() 
{
  qDebug() << "Request Dst" << ui.DstCombo->currentData().toInt();
  qDebug() << "Request Src" << ui.SrcCombo->currentData().toInt();
  m_request.SetDstHostId(ui.DstCombo->currentData().toInt());
  m_request.SetSrcHostId(ui.SrcCombo->currentData().toInt());
  m_request.SetTimeStamp(RequestTimeStamp());

  return m_request;
}
//------------------------------------------------------------------------------
// Response
//
const TimelineEvent& TimelineEventEditor::Response() 
{
  qDebug() << "Response Dst" << ui.SrcCombo->currentData().toInt();
  qDebug() << "Response Src" << ui.DstCombo->currentData().toInt();
  m_response.SetDstHostId(ui.SrcCombo->currentData().toInt());
  m_response.SetSrcHostId(ui.DstCombo->currentData().toInt());
  m_response.SetTimeStamp(ResponseTimeStamp());

  return m_response;
}
//------------------------------------------------------------------------------
// RestoreState
//
void TimelineEventEditor::RestoreState()
{
  restoreGeometry(QSettings().value(SK_TEE_GEOMETRY).toByteArray());

  ui.MainSplitter->restoreState(QSettings().value(SK_TEE_MAIN_SPLIT).toByteArray());
  //ui.RequestSplitter->restoreState(QSettings().value(SK_TEE_REQUEST_SPLIT).toByteArray());
  //ui.ResponseSplitter->restoreState(QSettings().value(SK_TEE_RESPONSE_SPLIT).toByteArray());
}
//------------------------------------------------------------------------------
// SaveState
//
void TimelineEventEditor::SaveState()
{
  QSettings().setValue(SK_TEE_GEOMETRY, saveGeometry());

  QSettings().setValue(SK_TEE_MAIN_SPLIT, ui.MainSplitter->saveState());
  //QSettings().setValue(SK_TEE_REQUEST_SPLIT, ui.RequestSplitter->saveState());
  //QSettings().setValue(SK_TEE_RESPONSE_SPLIT, ui.ResponseSplitter->saveState());
}
//------------------------------------------------------------------------------
// OnInit
//
void TimelineEventEditor::OnInit()
{
  RestoreState();
  ui.RequestMethodView->Init(m_request.Host(), m_request.Method(), m_request.Doc());
  ui.ResponseMethodView->Init(m_response.Host(), m_response.Method(), m_response.Doc());
}

