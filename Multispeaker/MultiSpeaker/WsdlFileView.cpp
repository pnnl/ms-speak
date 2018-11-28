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
// Summary: WsdlFileView.cpp
//-------------------------------------------------------------------------------

#include <QDebug>
#include <QFileDialog>
#include <QSettings>
#include <QStandardItem>
#include <QTimer>
//#include <QMessageBox>

#include "HeaderContainerWidget.h"
#include "WsdlFileView.h"
#include "WebServiceInfo.h"
#include "WsdlMethodTemplateEditor.h"

const QString TAG_WSDL_OPERATION = "wsdl:operation";
const QString TAG_NAME = "name";

//------------------------------------------------------------------------------
// WsdlFileView
//
WsdlFileView::WsdlFileView(const QString& host, QWidget* parent)
	: QWidget(parent),
	m_host(host),
	m_wsdlFile(WsInfo().Wsdl(host))
{
	ui.setupUi(this);

	ui.TableView->setModel(&m_model);
	ui.TableView->horizontalHeader()->hide();
	ui.TableView->verticalHeader()->hide();
	ui.TableView->horizontalHeader()->setStretchLastSection(true);
	ui.TableView->setEditTriggers(QAbstractItemView::NoEditTriggers);
	connect(ui.TableView, SIGNAL(doubleClicked(const QModelIndex&)), this, SLOT(OnMethodDoubleClicked(const QModelIndex&)));

	ui.WsdlFileNameLabel->setText(QFileInfo(m_wsdlFile->FileName()).fileName());
	ui.WsdlFileNameLabel->setToolTip(QDir::toNativeSeparators(m_wsdlFile->FileName()));

	connect(ui.BrowseBtn, SIGNAL(clicked()), this, SLOT(OnBrowse()));
	connect(&m_model, SIGNAL(itemChanged(QStandardItem*)), this, SLOT(OnModelChanged(QStandardItem*)));
	//connect(m_wsdlFile, SIGNAL(WsdlMethodUpdated()), this, SLOT(OnWsdlMethodUpdated())); // chm: No such signal WsdlFile::WsdlMethodUpdated()

	// force update after the m_wsdlFile has been parsed and instantiated in its constructor
	QTimer::singleShot(0, this, SLOT(OnUpdate()));
}
//------------------------------------------------------------------------------
// ~WsdlFileView
//
WsdlFileView::~WsdlFileView()
{
}
//------------------------------------------------------------------------------
// OnBrowse
//
void WsdlFileView::OnBrowse()
{
	QString seedFile = QSettings().value(WsInfo().WsdlFileNameKey(m_host), QVariant()).toString();

	//QMessageBox messageBox;
	//QString defDir = qApp->applicationDirPath()+"/Wsdls/EndPoints";
	//QString err=QString("SeedFile'%1',  Appdir'%2'").arg(seedFile).arg(defDir);
	//messageBox.critical (Q_NULLPTR,"Files", err );

	if( seedFile.isEmpty() ){
		// delete all prior template/setting files for the host, as may be incompatible with new xsd
		QString path = ROOT_HOME_PATH;
		QDir dir(path);
		QString nf =  QString("%1_*.xml").arg(m_host);
		dir.setNameFilters(QStringList() << nf );
		dir.setFilter(QDir::Files);
		foreach(QString dirFile, dir.entryList())
		{
			dir.remove(dirFile);
		}
		nf =  QString("%1*.json").arg(m_host);
		dir.setNameFilters(QStringList() << nf );
		dir.setFilter(QDir::Files);
		foreach(QString dirFile, dir.entryList())
		{
			dir.remove(dirFile);
		}
		seedFile =  qApp->applicationDirPath()+"/Wsdls/EndPoints";
	}
	// Load file
	QString fileName = QFileDialog::getOpenFileName(this, QString("Select %1 WSDL File").arg(m_host), seedFile, "WSDL (*.wsdl);; All (*.*)");
	if (fileName.isEmpty()){
		QSettings().setValue(WsInfo().WsdlFileNameKey(m_host), "");
		return;
	}
	ui.WsdlFileNameLabel->setText(QFileInfo(fileName).fileName());
	ui.WsdlFileNameLabel->setToolTip(QDir::toNativeSeparators(fileName));

	if (HeaderContainerWidget* w = qobject_cast<HeaderContainerWidget*>(parent()->parent()))
	{
		w->Header()->SetTitle(QFileInfo(fileName).fileName());
		w->Header()->setToolTip(QDir::toNativeSeparators(fileName));
	}

	QSettings().setValue(WsInfo().WsdlFileNameKey(m_host), fileName);
	WsInfo().SetWsdlFile(m_host, fileName);
	m_wsdlFile = WsInfo().Wsdl(m_host);
	OnUpdate();
}
//------------------------------------------------------------------------------
// OnMethodDoubleClicked
//
void WsdlFileView::OnMethodDoubleClicked(const QModelIndex& index)
{
	if (!index.isValid())
		return;

	QString method = index.data(Qt::DisplayRole).toString();
	WsdlMethodTemplateEditor dlg(m_wsdlFile, method, this);
	dlg.exec();
}
//------------------------------------------------------------------------------
// OnModelChanged
//
void WsdlFileView::OnModelChanged(QStandardItem* item)
{
	bool isChecked = (item->checkState() == Qt::Checked) ? true : false;
	QString name = item->data(Qt::DisplayRole).toString();
	m_wsdlFile->SetMethodEnabled(name, isChecked);
}
//------------------------------------------------------------------------------
// OnUpdate
//
void WsdlFileView::OnUpdate()
{
	QApplication::setOverrideCursor(Qt::WaitCursor);
	m_model.clear();
	QStringList enabledMethods = m_wsdlFile->EnabledMethodNames();
	QStringList methods = m_wsdlFile->Methods().keys();
	methods.sort();
	foreach (const QString method, methods)
	{
		QStandardItem* item = new QStandardItem(method);
		item->setCheckable(true);
		item->setCheckState((enabledMethods.contains(method)) ? Qt::Checked : Qt::Unchecked);
		item->setToolTip(QString("Double Click to edit Template\n%1").arg(m_wsdlFile->Method(method)->Desc));
		m_model.appendRow(item);
	}
	ui.TableView->verticalHeader()->setSectionResizeMode(QHeaderView::ResizeToContents);
	QApplication::restoreOverrideCursor();
}
