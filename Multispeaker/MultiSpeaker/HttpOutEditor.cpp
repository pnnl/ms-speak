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
// Summary: HttpOutEditor.cpp
//-------------------------------------------------------------------------------

#include <QHostAddress>
#include <QNetworkInterface>
#include <QSettings>
#include <QLineEdit>

#include "HttpOutEditor.h"
#include "Settings.h"

//------------------------------------------------------------------------------
// HttpOutEditor
//		- invoked via MultiSpeaker::OnHostDoubleClicked()
HttpOutEditor::HttpOutEditor(const Host& host, QWidget* parent)
	: QDialog(parent)
	, m_host(host)
	, m_reqIpChanged(false)
	, m_resIpChanged(false)
{
	Init(host);
}
//------------------------------------------------------------------------------
// HttpOutEditor
//		- invoked via MultiSpeaker::HttpOutBtn press.
HttpOutEditor::HttpOutEditor(QWidget* parent)
	: QDialog(parent)
	, m_reqIpChanged(false)
	, m_resIpChanged(false)
{
	//Host* pHost = new Host( -1, "tmpHost", Host::NoApp);
	Init(HostRef());
}
//------------------------------------------------------------------------------
// ~HttpOutEditor
//
HttpOutEditor::~HttpOutEditor()
{
}
//------------------------------------------------------------------------------
// Init
//
void HttpOutEditor::Init(const Host& host)
{
	ui.setupUi(this);

	//ui.RequestHostIpEdit->installEventFilter(this);
	//ui.ResponseHostIpEdit->installEventFilter(this);

	ui.RequestHostIpEdit->setEditable(true);
	ui.RequestHostIpEdit->setDuplicatesEnabled(false);
    ui.RequestHostIpEdit->lineEdit()->setAlignment(Qt::AlignCenter);
    ui.RequestHostIpEdit->lineEdit()->setInputMask( "000.000.000.000" );

	ui.ResponseHostIpEdit->setEditable(true);
	ui.ResponseHostIpEdit->setDuplicatesEnabled(false);
    ui.ResponseHostIpEdit->lineEdit()->setAlignment(Qt::AlignCenter);
    ui.ResponseHostIpEdit->lineEdit()->setInputMask( "000.000.000.000" );

	QStringList ipList = getIpAddresses();
	ui.RequestHostIpEdit->insertItems(0, ipList);
	ui.ResponseHostIpEdit->insertItems(0, ipList);

	QString ip = host.ReqHostAddress();
	int idx = ui.RequestHostIpEdit->findText(ip);
	if( idx == -1 ){
		ui.RequestHostIpEdit->insertItem(0, ip);
		ui.RequestHostIpEdit->setCurrentIndex(0);
	}

	ip = host.RespHostAddress();
	idx = ui.ResponseHostIpEdit->findText(ip);
	if( idx == -1 ){
		ui.ResponseHostIpEdit->insertItem(0, ip);
		ui.ResponseHostIpEdit->setCurrentIndex(0);
	}

	// NOTE: using ui.RequestHostIpEdit->lineEdit(),SIGNAL(returnPressed()) cause SIGEV crash on slot return
	//		 (maybe due to the HttpOutEditor widget also responding to returnPressed...
	//		 also, passing QString without the ref ampersand does too.
	connect(ui.RequestHostIpEdit, SIGNAL(editTextChanged(const QString&)),this,SLOT(OnHostIpChanged(const QString&)));
	connect(ui.ResponseHostIpEdit, SIGNAL(editTextChanged(const QString&)),this,SLOT(OnHostIpChanged(const QString&)));
	connect(ui.RequestHostIpEdit->lineEdit(), SIGNAL(editingFinished()), SLOT(OnEditingFinished()));
	connect(ui.ResponseHostIpEdit->lineEdit(), SIGNAL(editingFinished()), SLOT(OnEditingFinished()));

	ui.RequestGroup->setChecked(host.ReqHostEnable());
	ui.RequestHostPortSpin->setValue(host.ReqHostPort());
	connect(ui.RequestGroup, SIGNAL(toggled(bool)), this, SLOT(OnReqHostEnableChanged(bool)));
	connect(ui.RequestHostPortSpin, SIGNAL(valueChanged(int)), this, SLOT(OnReqHostPortChanged(int)));

	ui.ResponseGroup->setChecked(host.RespHostEnable());
	ui.ResponseHostPortSpin->setValue(host.RespHostPort());
	connect(ui.ResponseGroup, SIGNAL(toggled(bool)), this, SLOT(OnRespHostEnableChanged(bool)));
	connect(ui.ResponseHostPortSpin, SIGNAL(valueChanged(int)), this, SLOT(OnRespHostPortChanged(int)));

	ui.EnableSslCheck->setChecked(host.EnableSsl());
	connect(ui.buttonBox, SIGNAL(accepted()), this, SLOT(OnAccept()));
	connect(ui.buttonBox, SIGNAL(rejected()), this, SLOT(reject()));
	connect(ui.EnableSslCheck, SIGNAL(toggled(bool)), this, SLOT(OnEnableSslCheck(bool)));

}
//------------------------------------------------------------------------------
// eventFilter
//
bool HttpOutEditor::eventFilter(QObject *object, QEvent *event)
{
	if (event->type() == QEvent::FocusIn)
    {
        /*if (object == ui.RequestHostIpEdit)
        {
            qWarning("FocusIn: %s", object->objectName().toLatin1().data());
        }*/
		qWarning("FocusIn: %s", object->objectName().toLatin1().data());
    }
	else if (event->type() == QEvent::FocusOut)
    {
        /*if (object == ui.RequestHostIpEdit)
        {
            qWarning("FocusOut: %s", object->objectName().toLatin1().data());
        }*/
		qWarning("FocusOut: %s", object->objectName().toLatin1().data());
    }
    return false;
}
//------------------------------------------------------------------------------
// OnAccept
void HttpOutEditor::OnAccept()
{
	if( HttpRequestEnabled() && ui.RequestHostIpEdit->currentText() == "..." )
		return;

	if( HttpResponseEnabled() && ui.ResponseHostIpEdit->currentText() == "..." )
		return;

	accept();
}

//------------------------------------------------------------------------------
// OnEditingFinished
//	emitted when the Return or Enter key is pressed or the line edit loses focus.
void HttpOutEditor::OnEditingFinished()
{
	if( !ReqIpChanged() && !ResIpChanged() ){
		//qDebug() << "Nothing Changed";
		return;
	}

	QLineEdit* pLineEdit = qobject_cast<QLineEdit*>(sender());
	QComboBox* pComboBox = qobject_cast<QComboBox*>(pLineEdit->parentWidget());
	QString newIp=pLineEdit->text();
	QHostAddress ipAddr( newIp );
	if( ipAddr.isNull() ){
		//qDebug() << "ipAddr isNull";
		pComboBox->clearEditText();
		//pComboBox->removeItem( pComboBox->currentIndex() );
		if( pComboBox == ui.RequestHostIpEdit )
			ReqIpChanged(false);
		else
			ResIpChanged(false);
	}
	else{
		if( pComboBox == ui.RequestHostIpEdit ){
			//qDebug() << "OnEditingFinished: " << pComboBox->objectName() << ", new Ip: " << newIp;
			if( ReqIpChanged() ){
				ReqIpChanged(false);
				ChangeReqHostAddress(newIp);
			}
		}
		else if( pComboBox == ui.ResponseHostIpEdit){
			if( ResIpChanged() ){
				ResIpChanged(false);
				ChangeRespHostAddress(newIp);
			}
		}
		else{
			qDebug() << "OnEditingFinished Unknown pComboBox: " << pComboBox << ", Name: " << pComboBox->objectName();
			return;
		}
		int idx = pComboBox->findText(newIp);
		if( idx == -1 ){
			idx = 0;
			pComboBox->insertItem(0, newIp);
			pComboBox->setCurrentIndex(0);
		}
	}
}
//------------------------------------------------------------------------------
// OnHostIpChanged
//
//qDebug() << "Sender: " << sender()->objectName();
//qDebug() << "Receiver: " << this->objectName();
void HttpOutEditor::OnHostIpChanged(const QString& newText)
{
	Q_UNUSED(newText)
	//QComboBox* pComboBox = qobject_cast<QComboBox*>(sender());
	//qDebug() << "Host Ip Changed for " << pComboBox->objectName() << ", new Ip: " << newText;
	if (sender() == ui.RequestHostIpEdit)
		ReqIpChanged(true);
	else if (sender() == ui.ResponseHostIpEdit)
		ResIpChanged(true);
	else
		qDebug() << "Unknown Sender: " << sender() << ", Name: " << sender()->objectName();
}
//------------------------------------------------------------------------------
// getIpAddresses
//
QStringList HttpOutEditor::getIpAddresses()
{
	QStringList list;
	QList<QHostAddress> ipAddressesList = QNetworkInterface::allAddresses();

	// Select just IPv4 Addresses
	for (int i = 0; i < ipAddressesList.size(); ++i)
	{
		if( ipAddressesList.at(i).protocol() == QAbstractSocket::IPv4Protocol )
		{
			list << ipAddressesList.at(i).toString();
		}
	}
	return list;
}
