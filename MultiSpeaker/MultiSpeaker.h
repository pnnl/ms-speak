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
// Summary: MultiSpeaker.h
//-------------------------------------------------------------------------------


#ifndef MULTISPEAKER_H
#define MULTISPEAKER_H

#include "ui_MultiSpeaker.h"

#include <QHash>
#include <QMainWindow>
#include <QProcess>
#include <QShortcut>
#include <QToolBar>
#include <QNetworkProxy>

#include "FunctionBlockDock.h"
#include "LogDock.h"
#include "MethodDock.h"
#include "TimelineEvent.h"
#include "WsdlDock.h"

class QSslCertificate;
class QSslCipher;
class QSslError;

class MultiSpeaker : public QMainWindow
{
	Q_OBJECT
private:
	Ui::MultiSpeakerClass ui;

	QShortcut m_clearSettingsShortcut;
	FunctionBlockDock* m_functionBlockDock;
	LogDock* m_logDock;

	MethodDock* m_methodDock;
	LogDock* m_miniNetCmdDock;

	WsdlDock* m_wsdlDock;
	static MultiSpeaker *pMainWindow;
	bool	m_bInitDone;
	QString m_proxyUserName;
	QString m_proxyPassWord;
	QString m_proxyAddress;
	QString m_proxyPortStr;
	quint16 m_proxyPort;
	bool m_useProxy;
	bool m_useCreds;

public:
	MultiSpeaker(QWidget* parent=Q_NULLPTR);
	~MultiSpeaker();
	static MultiSpeaker *theApp();
	bool InitOk() {return m_bInitDone; }
	bool ProxyEnabled() { return m_useProxy; }
	QString ProxyAddress() { return m_proxyAddress; }
	quint16 ProxyPort() { return m_proxyPort; }

protected:
	virtual void closeEvent(QCloseEvent* e);
	virtual void resizeEvent(QResizeEvent* e) {Q_UNUSED(e); SaveState();}

private:
	void setupProxy();
	QString ProxyIp() { return m_proxyAddress; }
	bool ProxyUseCreds() { return m_useCreds; }
	QString ProxyUserName() { return m_proxyUserName; }
	QString ProxyPassWord() { return m_proxyAddress; }
	void CreateFunctionBlockDock();
	void CreateLogDock();
	void CreateMethodDock();
	void CreateMiniNetCmdDock();
	void CreateTitleToolBar();
	void CreateToolBar();
	void CreateWsdlDock();

	void DisplayCertChainInfo(const QSslCipher& cipher, const QList<QSslCertificate>& certChain);
	void DisplayHostSslErrors(const QList<QSslError>& errors);

	void EditTimelineEvent(TimelineEvent& e);

	FunctionBlockDock& FunctionBlockDockkRef() {if (!m_functionBlockDock) CreateFunctionBlockDock(); return *m_functionBlockDock;}
	LogDock& LogDockRef() {if (!m_logDock) CreateLogDock(); return *m_logDock;}

	MethodDock& MethodDockRef() {if (!m_methodDock) CreateMethodDock(); return *m_methodDock;}
	LogDock& MiniNetCmdDockRef() {if (!m_miniNetCmdDock) CreateMiniNetCmdDock(); return *m_miniNetCmdDock;}

	void RestoreState();
	void SaveState();

	WsdlDock& WsdlDockRef() {if (!m_wsdlDock) CreateWsdlDock(); return *m_wsdlDock;}

signals:
private slots:
	void OnAbout();
	void OnClearSettings();
	void OnHideTimestampLabel();
	void OnHostDoubleClicked(int id);
	void OnHostSceneChanged();
	bool OnSquidOut();
	bool OnHttpOut();
	void OnLogMsg(const QString& msg) { LogDockRef().Append(msg); }
	void OnMiniNet();
	void OnMiniNetMsg(const QString& msg) {LogDockRef().Append(msg);}
	void OnScenarioOpen();
	void OnScenarioSave();
	void OnTimelineError(const QString& error);
	void OnTimelineEventDoubleClicked(TimelineEvent& e) {EditTimelineEvent(e);}
	void OnTimelineEventListViewDoubleClicked(const QModelIndex& index);
	void OnTimelineMouseMove(int timeStamp);
	void OnTimelineSpanBtnClicked();
	void OnTimelineSpanChanged(int timeSpan);
	void OnTimelineEventSendSslErrors(const QList<QSslError>& errors, const QSslCipher& cipher, const QList<QSslCertificate>& certChain);
	void OnToolBarVisibilityChanged(bool visible) { if (!visible) qobject_cast<QToolBar*>(sender())->setVisible(true); } // Prevent user from hiding the main tool bar
	void OnWsdl() {WsdlDockRef().show();}
	void OnWsdlFileChanged(const QString& host);
	void OnWsdlTest();
	void OnBrowseRoot();
	void showProxy();

};

#endif // MULTISPEAKER_H
