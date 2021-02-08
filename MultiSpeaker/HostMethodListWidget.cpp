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
// Summary: HostMethodListWidget.cpp
//-------------------------------------------------------------------------------

#include <QListView>
#include <QMessageBox>
#include <QVBoxLayout>

#include "HostMethodListWidget.h"
#include "Settings.h"
#include "TimelineEvent.h"
#include "TimelineEventEditor.h"
#include "TimelineScene.h"
#include "WsdlFile.h"

const int HOST_ROLE = Qt::UserRole + 1;

//------------------------------------------------------------------------------
// HostMethodListWidget
//
HostMethodListWidget::HostMethodListWidget(int index, const QString& hostName, QWidget* parent)
	: HeaderContainerWidget(index, hostName, parent),
	m_hostName(hostName)
{
	/* QLayout: Attempting to add QLayout "" to HostMethodListWidget "HeaderContainerWidget", which already has a layout
	QVBoxLayout* layout = new QVBoxLayout(this);
	layout->setSpacing(0);
	layout->setObjectName(QStringLiteral("ContainerLayout"));
	layout->setContentsMargins(0, 0, 0, 0);
	*/
	// List View
	QListView* view = new QListView(this);
	view->setAcceptDrops(false);
	view->setDefaultDropAction(Qt::IgnoreAction);
	view->setDragEnabled(true);
	view->setSelectionBehavior(QAbstractItemView::SelectRows);
	view->setSelectionMode(QAbstractItemView::ExtendedSelection);
	view->setEditTriggers(QAbstractItemView::NoEditTriggers);
	view->setModel(&m_model);

	connect(view, SIGNAL(doubleClicked(const QModelIndex&)), this, SLOT(OnListViewDoubleClicked(const QModelIndex&)));

	Container()->layout()->addWidget(view);
	Header()->SetColor(QColor(168,60,15));

	Update();
}
//------------------------------------------------------------------------------
// ~HostMethodListWidget
//
HostMethodListWidget::~HostMethodListWidget()
{
}
//------------------------------------------------------------------------------
// Update
//
void HostMethodListWidget::Update()
{
	m_model.clear();
	WsdlFile* wsdlFile = WsInfo().Wsdl(m_hostName);
	QList<QStandardItem*> items;
	foreach (const WsdlMethod* m, wsdlFile->EnabledMethods())
	{
		QStandardItem* item = new QStandardItem(m->Name);
		item->setToolTip(m->Desc);
		item->setData(wsdlFile->HostName(), HOST_ROLE);
		items << item;
	}

	m_model.appendColumn(items);
}
//------------------------------------------------------------------------------
// OnListViewDoubleClicked - brings up the request/response packet editor
//
void HostMethodListWidget::OnListViewDoubleClicked(const QModelIndex& index)
{
	if (!index.isValid())
		return;

	if (Timeline().IsRunning())
	{
		QMessageBox::warning(this, "Timeline", "Events may not be inserted while Scheduler is running.");
		return;
	}

	QString methodName = index.data(Qt::DisplayRole).toString();
	QString hostName = index.data(HOST_ROLE).toString();
	WsdlFile* wsdl = WsInfo().Wsdl(hostName);
	int id = Timeline().NextTimelineEventId(); // Get the current max Id in TimelineScene
	TimelineEvent reqEvent(id, TimelineEvent::Request, 0, hostName, methodName, wsdl->MethodTemplateRequest(methodName), wsdl->NamespaceByPrefix(STR_NAMESPACE_PREFIX_TNS));
	TimelineEvent resEvent(id+1, TimelineEvent::Response, 500, hostName, methodName, wsdl->MethodTemplateResponse(methodName), wsdl->NamespaceByPrefix(STR_NAMESPACE_PREFIX_TNS));
	TimelineEventEditor dlg(reqEvent, resEvent, this);
	if (dlg.exec())
	{
		reqEvent.IsEnabled(dlg.RequestEnabled());
		resEvent.IsEnabled(dlg.ResponseEnabled());
		if( reqEvent.IsEnabled() ){
			reqEvent.Copy(dlg.Request());
		}
		if( resEvent.IsEnabled() ){
			resEvent.Copy(dlg.Response());
		}
		Timeline().InsertTimelineEventPair(reqEvent, resEvent);
	}
}

