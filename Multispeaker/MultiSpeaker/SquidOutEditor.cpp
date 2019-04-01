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
//		2019 - Carl Miller <carl.miller@pnnl.gov>
//-------------------------------------------------------------------------------
//
// Summary: SquidOutEditor.cpp
//-------------------------------------------------------------------------------

#include <QHostAddress>
#include <QNetworkInterface>
#include <QSettings>
#include <QLineEdit>

#include "SquidOutEditor.h"
#include "Settings.h"

//------------------------------------------------------------------------------
// SquidOutEditor
//		- invoked via MultiSpeaker::SquidOutBtn press.
SquidOutEditor::SquidOutEditor(QWidget* parent)
	: QDialog(parent)
	, m_ProxyUserName(QSettings().value(SK_PROXY_UN, "MSTest").toString())
	, m_ProxyPassWord(QSettings().value(SK_PROXY_PW, "P@SSW0RD").toString())
	, m_ProxyAddress(QSettings().value(SK_PROXY_IP, QHostAddress(QHostAddress::LocalHost).toString()).toString())
	, m_ProxyIpChanged(false)
	, m_useProxy(QSettings().value(SK_USE_PROXY, false).toBool())
	, m_useCreds(QSettings().value(SK_USE_PROXYCREDS, false).toBool())
	, m_ProxyPort(QSettings().value(SK_PROXY_PORT, 3128).toInt())
{
	Init();
}
//------------------------------------------------------------------------------
// ~SquidOutEditor
//
SquidOutEditor::~SquidOutEditor()
{
}
//------------------------------------------------------------------------------
// Init
//
void SquidOutEditor::Init()
{
	ui.setupUi(this);

	ui.ProxyIpEdit->setEditable(true);
	ui.ProxyIpEdit->setDuplicatesEnabled(false);
	ui.ProxyIpEdit->lineEdit()->setAlignment(Qt::AlignCenter);
	ui.ProxyIpEdit->lineEdit()->setInputMask("000.000.000.000");

	QStringList ipList = getIpAddresses();
	ui.ProxyIpEdit->insertItems(0, ipList);

	QString ip = m_ProxyAddress;
	int idx = ui.ProxyIpEdit->findText(ip);
	if (idx == -1) {
		ui.ProxyIpEdit->insertItem(0, ip);
		ui.ProxyIpEdit->setCurrentIndex(0);
	}
	else {
		ui.ProxyIpEdit->setCurrentIndex(idx);
	}

	ui.ProxyGroup->setChecked(UseProxy());
	ui.ProxyPortSpin->setValue(m_ProxyPort);
	ui.UseCreds->setChecked(UseCreds());

	ui.editPassword->setEchoMode(QLineEdit::Password);
	ui.labelUsername->setBuddy(ui.editUserName);
	ui.labelPassword->setBuddy(ui.editPassword);

	ui.editUserName->setText(m_ProxyUserName);
	ui.editPassword->setText(m_ProxyPassWord);

	bool bVal = false, bVal2 = false;
	if( ProxyEnabled() ) {
		bVal = true;
		if (UseCreds()) {
			bVal2 = true;
		}
	}
	ui.UseCreds->setEnabled(bVal);
	ui.editUserName->setVisible(bVal2); 
	ui.editPassword->setVisible(bVal2);
	ui.labelUsername->setVisible(bVal2);
	ui.labelPassword->setVisible(bVal2);

	connect(ui.ProxyGroup, SIGNAL(toggled(bool)), this, SLOT(OnEnableProxyCheck(bool)));
	connect(ui.UseCreds, SIGNAL(toggled(bool)), this, SLOT(OnUseCredsCheck(bool)));
	connect(ui.buttonBox, SIGNAL(accepted()), this, SLOT(OnAccept()));
	connect(ui.buttonBox, SIGNAL(rejected()), this, SLOT(reject()));

}
//------------------------------------------------------------------------------
// eventFilter
//
bool SquidOutEditor::eventFilter(QObject *object, QEvent *event)
{
	if (event->type() == QEvent::FocusIn)
    {
        /*if (object == ui.ProxyIpEdit)
        {
            qWarning("FocusIn: %s", object->objectName().toLatin1().data());
        }*/
		qWarning("FocusIn: %s", object->objectName().toLatin1().data());
    }
	else if (event->type() == QEvent::FocusOut)
    {
        /*if (object == ui.ProxyIpEdit)
        {
            qWarning("FocusOut: %s", object->objectName().toLatin1().data());
        }*/
		qWarning("FocusOut: %s", object->objectName().toLatin1().data());
    }
    return false;
}
//------------------------------------------------------------------------------
// OnAccept
void SquidOutEditor::OnAccept()
{
	if( ProxyEnabled() && ui.ProxyIpEdit->currentText() == "..." )
		return;

	accept();
}

//------------------------------------------------------------------------------
// OnEnableProxyCheck
void SquidOutEditor::OnEnableProxyCheck(bool checked)
{
	// eventual, dialog to get host, port, username and password
	SetUseProxy(checked);
	if (ProxyEnabled()) {
		ui.UseCreds->setEnabled(true);
	}
	else {
		ui.UseCreds->setEnabled(false);
	}
	OnUseCredsCheck(ui.UseCreds->isChecked());
}
//------------------------------------------------------------------------------
// UseCreds
void SquidOutEditor::OnUseCredsCheck(bool checked)
{
	ui.editUserName->setVisible(ProxyEnabled() && checked);
	ui.editPassword->setVisible(ProxyEnabled() && checked);
	ui.labelUsername->setVisible(ProxyEnabled() && checked);
	ui.labelPassword->setVisible(ProxyEnabled() && checked);
}
//------------------------------------------------------------------------------
// OnEditingFinished
//	emitted when the Return or Enter key is pressed or the IP edit loses focus.
void SquidOutEditor::OnEditingFinished()
{
	if( !ProxyIpChanged() ){
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
		if( pComboBox == ui.ProxyIpEdit )
			ProxyIpChanged(false);
	}
	else{
		if( pComboBox == ui.ProxyIpEdit ){
			//qDebug() << "OnEditingFinished: " << pComboBox->objectName() << ", new Ip: " << newIp;
			if( ProxyIpChanged() ){
				ProxyIpChanged(false);
				ChangeProxyAddress(newIp);
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
// getIpAddresses
//
QStringList SquidOutEditor::getIpAddresses()
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

