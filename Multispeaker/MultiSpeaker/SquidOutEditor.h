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
// Summary: SquidOutEditor.h
//-------------------------------------------------------------------------------

#ifndef SQUIDOUTEDITOR_H
#define SQUIDOUTEDITOR_H

#include "ui_SquidOutEditor.h"

#include <QDialog>

class SquidOutEditor : public QDialog
{
	Q_OBJECT
private:
	Ui::SquidOutEditor ui;
	QString m_ProxyUserName;
	QString m_ProxyPassWord;
	QString m_ProxyAddress;
	bool m_ProxyIpChanged;
	bool m_useProxy;
	bool m_useCreds;
	int m_ProxyPort;

public:
	SquidOutEditor(QWidget* parent = Q_NULLPTR);
	~SquidOutEditor();

	QStringList getIpAddresses();
	QString ProxyIp() { return ui.ProxyIpEdit->currentText(); }
	QString ProxyUserName() { return ui.editUserName->text(); }
	QString ProxyPassWord() { return ui.editPassword->text(); }
	bool ProxyEnabled() { return ui.ProxyGroup->isChecked(); }
	bool ProxyUseCreds() { return ui.UseCreds->isChecked(); }
	int ProxyPort() { return ui.ProxyPortSpin->value(); }

	bool ProxyIpChanged() const {return m_ProxyIpChanged;}
	void ProxyIpChanged(bool b) { m_ProxyIpChanged = b; }
	void UseCreds(bool b) { m_useCreds = b; }
	bool UseCreds() { return m_useCreds; }

	void ChangeProxyAddress(const QString& text) { SetProxyAddress(text); }

	bool UseProxy() const { return m_useProxy; }
	QString ProxyAddress() const { return m_ProxyAddress; }

	void SetUseProxy(bool flag) { m_useProxy = flag; }
	void SetProxyAddress(const QString& address) { m_ProxyAddress = address; }
	void Init();

private slots:

	void OnAccept();
	void OnEnableProxyCheck(bool checked);
	void OnUseCredsCheck(bool checked);
	bool eventFilter(QObject *object, QEvent *event);
	void OnEditingFinished();
};

#endif // SQUIDOUTEDITOR_H

