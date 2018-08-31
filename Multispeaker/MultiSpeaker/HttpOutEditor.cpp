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
	: QDialog(parent), m_host(host)
{
	Init(host);
}
//------------------------------------------------------------------------------
// HttpOutEditor
//		- invoked via MultiSpeaker::HttpOutBtn press.
HttpOutEditor::HttpOutEditor(QWidget* parent)
	: QDialog(parent)
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
	/* shouldn't need this check since setDuplicatesEnabled is set false...
	int idx = ui.RequestHostIpEdit->findText(ip);
	if( idx == -1 ){
		idx = 0;
		ui.RequestHostIpEdit->insertItem(idx, ip);
	}*/
	ui.RequestHostIpEdit->insertItem(0, ip);
	ui.RequestHostIpEdit->setCurrentIndex(0);
	ip = host.RespHostAddress();
	ui.ResponseHostIpEdit->insertItem(0, ip);
	ui.ResponseHostIpEdit->setCurrentIndex(0);

	// NOTE: using ui.RequestHostIpEdit->lineEdit(),SIGNAL(returnPressed()) cause SIGEV crash on slot return
	//		 (maybe due to the HttpOutEditor widget also responding to returnPressed...
	//		 also, passing QString without the ref ampersand does too.
	connect(ui.RequestHostIpEdit, SIGNAL(currentTextChanged(const QString&)),this,SLOT(OnHostIpSelectionChanged(const QString&)));
	connect(ui.RequestHostIpEdit, SIGNAL(editTextChanged(const QString&)), SLOT(RequestIpChanged(const QString&)) );

    connect(ui.ResponseHostIpEdit, SIGNAL(currentTextChanged(const QString&)),this,SLOT(OnHostIpSelectionChanged(const QString&)));
	connect(ui.ResponseHostIpEdit, SIGNAL(editTextChanged(const QString&)), SLOT(ResponseIpChanged(const QString&)) );

	ui.RequestGroup->setChecked(host.ReqHostEnable());
	ui.RequestHostPortSpin->setValue(host.ReqHostPort());
	connect(ui.RequestGroup, SIGNAL(toggled(bool)), this, SLOT(OnReqHostEnableChanged(bool)));
	connect(ui.RequestHostPortSpin, SIGNAL(valueChanged(int)), this, SLOT(OnReqHostPortChanged(int)));

	ui.ResponseGroup->setChecked(host.RespHostEnable());
	ui.ResponseHostPortSpin->setValue(host.RespHostPort());
	connect(ui.ResponseGroup, SIGNAL(toggled(bool)), this, SLOT(OnRespHostEnableChanged(bool)));
	connect(ui.ResponseHostPortSpin, SIGNAL(valueChanged(int)), this, SLOT(OnRespHostPortChanged(int)));

	ui.EnableSslCheck->setChecked(host.EnableSsl());
	connect(ui.buttonBox, SIGNAL(accepted()), this, SLOT(accept()));
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
// OnHostSelectionChanged
//
void HttpOutEditor::OnHostIpSelectionChanged(const QString& newText)
{
	QComboBox* pComboBox = qobject_cast<QComboBox*>(sender());
	qDebug() << "OnHostIpSelectionChanged() " << pComboBox->objectName() << "newText: " << newText;
	//qDebug() << "Receiver: " << this->objectName();
	OnReqHostAddressChanged(newText);
}
//------------------------------------------------------------------------------
// RequestIpChanged
//
void HttpOutEditor::RequestIpChanged( const QString& newText )
{
	QComboBox* pComboBox = qobject_cast<QComboBox*>(sender());
	// clearEditText()
	//ui.RequestHostIpEdit->setItemText( ui.RequestHostIpEdit->currentIndex(), text );
	//ui.RequestHostIpEdit->insertItem(0, text);
	qDebug() << "RequestIpChanged() " << pComboBox->objectName() << "newText: " << newText;
	OnReqHostAddressChanged(newText);
}
//------------------------------------------------------------------------------
// ResponseIpChanged
//
void HttpOutEditor::ResponseIpChanged( const QString& newText )
{
	QComboBox* pComboBox = qobject_cast<QComboBox*>(sender());
	//ui.ResponseHostIpEdit->setItemText( ui.ResponseHostIpEdit->currentIndex(), text );
	//ui.ResponseHostIpEdit->insertItem(0, text);
	qDebug() << "ResponseIpChanged() " << pComboBox->objectName() << "newText: " << newText;
	OnRespHostAddressChanged(newText);
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
