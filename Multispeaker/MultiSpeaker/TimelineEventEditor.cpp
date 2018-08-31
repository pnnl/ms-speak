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
// Summary: TimelineEventEditor.cpp
//-------------------------------------------------------------------------------

#include <QTime>
#include <QTimer>

#include "HostScene.h"
#include "TimelineEventEditor.h"
#include "WebServiceInfo.h"
#include "WsdlFile.h"

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

	ui.TitleHeader->SetTitle(request.Method(), 12);
	ui.TitleHeader->SetColor(QColor(1,164,148));
	ui.RequestHeader->SetTitle("Request", 10);
	ui.ResponseHeader->SetTitle("Response", 10);

	//ui.Header->SetColor(QColor(120,120,120));

	// Request Namespace
	ui.RequestNamespaceEdit->setText(m_request.Namespace());

	// Response Namespace
	ui.ResponseNamespaceEdit->setText(m_response.Namespace());

	// Time
	ui.TimeStampEdit->setTime(QTime(0,0).addMSecs(request.TimeStamp()));
	ui.ResponseDelayTimeEdit->setTime(QTime(0,0).addMSecs(response.TimeStamp() - request.TimeStamp()));

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

	connect(ui.RequestNamespaceEdit, SIGNAL(editingFinished()), this, SLOT(OnRequestNamespaceChanged()));
	connect(ui.ResponseNamespaceEdit, SIGNAL(editingFinished()), this, SLOT(OnResponseNamespaceChanged()));
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
// called after close the request/response packet editor ("Edit Timeline Event")
const TimelineEvent& TimelineEventEditor::Request() 
{
	//qDebug() << "Request Dst" << ui.DstCombo->currentData().toInt();
	//qDebug() << "Request Src" << ui.SrcCombo->currentData().toInt();
	m_request.SetDstHostId(ui.DstCombo->currentData().toInt());
	m_request.SetSrcHostId(ui.SrcCombo->currentData().toInt());
	m_request.SetTimeStamp(RequestTimeStamp());

	return m_request;
}
//------------------------------------------------------------------------------
// Response
// called after close the request/response packet editor ("Edit Timeline Event")
const TimelineEvent& TimelineEventEditor::Response()
{
	//qDebug() << "Response Dst" << ui.SrcCombo->currentData().toInt();
	//qDebug() << "Response Src" << ui.DstCombo->currentData().toInt();
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
	ui.RequestMethodView->Init(&m_request);
	ui.ResponseMethodView->Init(&m_response,false);
}
//------------------------------------------------------------------------------
// OnRequestNamespaceChanged
//
void TimelineEventEditor::OnRequestNamespaceChanged() 
{
	m_request.SetNamespace(ui.RequestNamespaceEdit->text());
	ui.RequestMethodView->XmlUpdate();
}
//------------------------------------------------------------------------------
// OnResponseNamespaceChanged
//
void TimelineEventEditor::OnResponseNamespaceChanged() 
{
	m_response.SetNamespace(ui.ResponseNamespaceEdit->text());
	ui.ResponseMethodView->XmlUpdate();
}
