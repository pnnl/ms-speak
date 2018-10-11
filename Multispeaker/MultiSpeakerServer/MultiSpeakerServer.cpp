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
// Summary: MultiSpeakerServer.cpp
//-------------------------------------------------------------------------------

#include <QDir>
#include <QFileDialog>
#include <QHostAddress>
#include <QNetworkInterface>
#include <QSettings>
#include <QTimer>

#include "MultiSpeakerServer.h"
#include "Settings.h"
#include "SslServer.h"
#include "Valid8.h"

static int MSG_COUNTER = 0;

//------------------------------------------------------------------------------
// MultiSpeakerServer
//
MultiSpeakerServer::MultiSpeakerServer(QWidget* parent)
  : QMainWindow(parent),
	m_server(Q_NULLPTR)
{
	ui.setupUi(this);
	ui.StopAct->setEnabled(false);

	connect(ui.CertFileBrowseBtn, SIGNAL(clicked()), this, SLOT(OnCertFileBrowse()));
	connect(ui.CertFolderBrowseBtn, SIGNAL(clicked()), this, SLOT(OnCertFolderBrowse()));
	connect(ui.EnableSslCheck, SIGNAL(toggled(bool)), this, SLOT(OnSslEnabledCheckChanged(bool)));
	connect(ui.ListenAct, SIGNAL(triggered()), this, SLOT(OnServerListen()));
	connect(ui.PrivateKeyFileBrowseBtn, SIGNAL(clicked()), this, SLOT(OnPrivateKeyFileBrowse()));
	connect(ui.StopAct, SIGNAL(triggered()), this, SLOT(OnServerStop()));
	connect(ui.btnClear, SIGNAL(clicked()), this, SLOT(OnClear()));
	connect(ui.btnResponse, SIGNAL(clicked()), this, SLOT(OnResponse()));

	QSettings s;
	ui.CertFileLabel->setText(QDir::toNativeSeparators(s.value(SK_SSL_CERT_FILE).toString()));
	ui.CertFolderLabel->setText(QDir::toNativeSeparators(s.value(SK_SSL_CERT_FOLDER).toString()));
	ui.PrivateKeyFileLabel->setText(QDir::toNativeSeparators(s.value(SK_SSL_PRIVATE_KEY_FILE).toString()));
	ui.EnableSslCheck->setChecked(s.value(SK_SSL_ENABLED, false).toBool());
	ui.SslFrame->setVisible(s.value(SK_SSL_ENABLED, false).toBool());

	ui.btnValid8->setEnabled(false);

	QString respFile = s.value(SK_RESPONSE_FILE, QString()).toString();
	if( respFile.isEmpty() ){
		ui.respFileName->setText(QApplication::translate("MultiSpeakerServerClass", "<No Response File>", nullptr));
	}
	else{
		QString justname = respFile.mid(respFile.lastIndexOf("/")+1);
		ui.respFileName->setText("Response File: " + justname);
	}
	connect(ui.btnValid8, SIGNAL(clicked()), this, SLOT(OnValid8()));
	RestoreState();
	QTimer::singleShot(0, this, SLOT(OnInitHostAddress()));
}
//------------------------------------------------------------------------------
// ~MultiSpeakerServer
//
MultiSpeakerServer::~MultiSpeakerServer()
{
}
//------------------------------------------------------------------------------
// FileNameBrowse
//
void MultiSpeakerServer::FileNameBrowse(const QString& msg, const QString& sk, QLabel* label)
{
	QString fileName = QFileDialog::getOpenFileName(this, msg, QSettings().value(sk, QDir::homePath()).toString());

	if (fileName.isEmpty())
		return;

	InitFileNameLabel(label, fileName);
	QSettings().setValue(sk, fileName);
}
//------------------------------------------------------------------------------
// FolderBrowse
//
void MultiSpeakerServer::FolderBrowse(const QString& msg, const QString& sk, QLabel* label)
{
	QString fileName = QFileDialog::getExistingDirectory(this, msg, QSettings().value(sk, QDir::homePath()).toString());

	if (fileName.isEmpty())
		return;

	InitFileNameLabel(label, fileName);
	QSettings().setValue(sk, fileName);
}
//------------------------------------------------------------------------------
// InitFileNameLabel
//
void MultiSpeakerServer::InitFileNameLabel(QLabel* label, const QString& folder)
{
	QString folderStr = QDir::toNativeSeparators(folder);
	//QString elideFolderStr = QFontMetrics(label->font()).elidedText(folderStr, Qt::ElideLeft, label->width());
	label->setText(folderStr);
	label->setToolTip(folderStr);
}
//------------------------------------------------------------------------------
// ServerClose
//
void MultiSpeakerServer::ServerClose()
{
	if (!m_server)
		return;
	m_server->close();
	m_server->deleteLater();
	ui.btnResponse->setEnabled(true);
	if(! m_testv8 )
		ui.btnValid8->setEnabled(false);

}
//------------------------------------------------------------------------------
// ServerListen
//
void MultiSpeakerServer::ServerListen()
{
	QSettings s;
	bool sslEnabled = s.value(SK_SSL_ENABLED, false).toBool();
	if (sslEnabled)
	{
		SslServer* server = new SslServer(this);

		QString certFolder = s.value(SK_SSL_CERT_FOLDER, QString()).toString();
		if (!server->SetSslCertFolder(certFolder))
			OnMessage(QString("Error Setting Cert Folder, %1").arg(certFolder).toLatin1());

		QString certFile = s.value(SK_SSL_CERT_FILE, QString()).toString();
		if (!server->SetSslLocalCertificate(certFile))
			OnMessage(QString("Error Reading Cert File, %1").arg(certFile).toLatin1());

		QString keyFile = s.value(SK_SSL_PRIVATE_KEY_FILE, QString()).toString();
		if (!server->SetSslPrivateKey(keyFile))
			OnMessage(QString("Error Reading Private Key File, %1").arg(keyFile).toLatin1());

		server->SetSslProtocol(QSsl::TlsV1_2);
		m_server = server;
	}
	else
	{
		m_server = new Server(this);
	}

	QString respFile = s.value(SK_RESPONSE_FILE, QString()).toString();
	if( !respFile.isEmpty() )
		if (!m_server->SetResponseFile(respFile))
			OnMessage(QString("Error Reading Response File, %1\n").arg(respFile).toLatin1());

	connect(m_server, SIGNAL(acceptError(QAbstractSocket::SocketError)), this, SLOT(OnServerAcceptError(QAbstractSocket::SocketError)));
	connect(m_server, SIGNAL(Message(const QByteArray&)), this, SLOT(OnMessage(const QByteArray&)));
	connect(m_server, SIGNAL(Message(int, const QByteArray&)), this, SLOT(OnMessage(int, const QByteArray&)));
	connect(m_server, SIGNAL(SocketError(QAbstractSocket::SocketError, const QString&)), this, SLOT(OnSocketError(QAbstractSocket::SocketError, const QString&)));
	connect(m_server, SIGNAL(destroyed(QObject*)), this, SLOT(OnServerClosed(QObject*)));

	if (!m_server->listen(QHostAddress(ui.HostCombo->currentText()), ui.PortSpin->value()))
	{
		qDebug() << "Server Listen Error:" << m_server->serverError() << m_server->errorString();
		ui.plainTextEdit->appendPlainText(QString("Server Listen Error: %1, %2")
		  .arg(m_server->serverError())
		  .arg(m_server->errorString()));
		return;
	}
	qDebug() << "Server The server is running on IP:" << m_server->serverAddress().toString() << "Port:" << m_server->serverPort();
	ui.plainTextEdit->appendPlainText(QString("Server The server is running on IP: %1 Port: %2")
	.arg(m_server->serverAddress().toString())
	.arg(m_server->serverPort()));

	ui.ListenAct->setEnabled(false);
	ui.StopAct->setEnabled(true);
	ui.CertFileBrowseBtn->setEnabled(false);
	ui.CertFolderBrowseBtn->setEnabled(false);
	ui.PrivateKeyFileBrowseBtn->setEnabled(false);
	ui.IgnoreSelfSignedCertCheck->setEnabled(false);
	ui.HostCombo->setEnabled(false);
	ui.PortSpin->setEnabled(false);
	ui.EnableSslCheck->setEnabled(false);
	ui.btnResponse->setEnabled(false);
}
//------------------------------------------------------------------------------
// OnValid8
//
void MultiSpeakerServer::OnValid8()
{
	//Test dlg(this);

	//QTemporaryFile f(
	//    QDir::temp().absoluteFilePath("mprog-XXXXXX.ext")
	//);

	//		-sd "/home/carl/Desktop/MS-SPEAK/V507/XSDS/EndPoints/"
	//		-ep "CD_Server"
	//		-xf "/home/carl/Desktop/MS-SPEAK/files/InitCDReq.xml"
	if( m_testv8 )
	{
		Valid8or dlg( "CD_Server", "/home/carl/Desktop/MS-SPEAK/files/InitCDReq.xml", this );
		dlg.exec();
	}
	else{
		Valid8or dlg( m_xmlBuff, this );
		dlg.exec();
	}
}
//------------------------------------------------------------------------------
// OnValid8
//
void MultiSpeakerServer::Valid8(const QByteArray& msg)
{
	m_testv8 = false;
	m_xmlBuff = msg;
	ui.btnValid8->setEnabled(true);
}
//------------------------------------------------------------------------------
// OnInitHostAddress
//
void MultiSpeakerServer::OnInitHostAddress()
{
	QStringList list;
	QList<QHostAddress> ipAddressesList = QNetworkInterface::allAddresses();
	foreach(const QHostAddress ip, ipAddressesList)
		// Select just IPv4 Addresses
		if( ip.protocol() == QAbstractSocket::IPv4Protocol )
			list << ip.toString();

	ui.HostCombo->insertItems(0, list);
	QString ip;
	/* Select the first non-localhost ipv4 address
	for (int i = 0; i < ipAddressesList.size(); ++i)
	{
		if (ipAddressesList.at(i) != QHostAddress::LocalHost && ipAddressesList.at(i).toIPv4Address())
		{
			ip = ipAddressesList.at(i).toString();
			break;
		}
	}*/
	// Select the loopback address
	for (int i = 0; i < ipAddressesList.size(); ++i)
	{
		if (ipAddressesList.at(i) == QHostAddress::LocalHost && ipAddressesList.at(i).toIPv4Address())
		{
			ip = ipAddressesList.at(i).toString();
			break;
		}
	}
	int idx = ui.HostCombo->findText(ip);
	ui.HostCombo->setCurrentIndex(idx);
}
//------------------------------------------------------------------------------
// OnMessage
//
void MultiSpeakerServer::OnMessage(const QByteArray& msg)
{
	//ui.plainTextEdit->appendPlainText(msg);
	// avoid extra newline added by appendPlainText
	ui.plainTextEdit->moveCursor (QTextCursor::End);
	ui.plainTextEdit->insertPlainText(msg);
	ui.plainTextEdit->moveCursor (QTextCursor::End);
}
//------------------------------------------------------------------------------
// OnMessage
//
void MultiSpeakerServer::OnMessage(int length, const QByteArray& msg)
{
	ui.plainTextEdit->appendPlainText("*****************************\n");
	ui.plainTextEdit->appendPlainText(QString("**** MSG: %1 ****\n").arg(++MSG_COUNTER));
	ui.plainTextEdit->appendPlainText(QString("**** Content Length: %1 ****\n").arg(length));
	ui.plainTextEdit->appendPlainText("*** BEGIN MSG ****************\n");
	ui.plainTextEdit->appendPlainText(msg);
	ui.plainTextEdit->appendPlainText("*** END MSG ******************\n");

	Valid8(msg);

}
//------------------------------------------------------------------------------
// OnServerAcceptError
//
void MultiSpeakerServer::OnServerAcceptError(QAbstractSocket::SocketError error)
{
	ui.plainTextEdit->appendPlainText("*****************************\n");
	ui.plainTextEdit->appendPlainText(QString("**** Server Accept Error Code: %1 ****\n").arg(error));
	ui.plainTextEdit->appendPlainText(QString("**** Server Accept Error: %1 ****\n").arg(m_server->errorString()));
	ui.plainTextEdit->appendPlainText("*****************************\n");
}
//------------------------------------------------------------------------------
// OnServerClosed
//
void MultiSpeakerServer::OnServerClosed(QObject* obj)
{
    Q_UNUSED(obj);
    ui.plainTextEdit->appendPlainText("Server Closed\n");
    ui.ListenAct->setEnabled(true);
    ui.StopAct->setEnabled(false);
    ui.CertFileBrowseBtn->setEnabled(true);
    ui.CertFolderBrowseBtn->setEnabled(true);
    ui.PrivateKeyFileBrowseBtn->setEnabled(true);
    ui.IgnoreSelfSignedCertCheck->setEnabled(true);
    ui.HostCombo->setEnabled(true);
    ui.PortSpin->setEnabled(true);
    ui.EnableSslCheck->setEnabled(true);
}
//------------------------------------------------------------------------------
// OnSocketError
//
void MultiSpeakerServer::OnSocketError(QAbstractSocket::SocketError error, const QString& errorString)
{
	ui.plainTextEdit->appendPlainText("*****************************\n");
	ui.plainTextEdit->appendPlainText(QString("**** Socket Error Code: %1 ****\n").arg(error));
	ui.plainTextEdit->appendPlainText(QString("**** Socket Error: %1 ****\n").arg(errorString));
	ui.plainTextEdit->appendPlainText("*****************************\n");
}
//------------------------------------------------------------------------------
// OnSslEnabledCheckChanged
//
void MultiSpeakerServer::OnSslEnabledCheckChanged(bool checked)
{
	ui.SslFrame->setVisible(checked);
	QSettings().setValue(SK_SSL_ENABLED, checked);
}
//------------------------------------------------------------------------------
// OnClear
//
void MultiSpeakerServer::OnClear()
{
	ui.plainTextEdit->clear();
	ui.btnValid8->setEnabled(false);
}
//------------------------------------------------------------------------------
// OnResponse
//
void MultiSpeakerServer::OnResponse()
{
	QString saveKey=SK_RESPONSE_FILE;
	QString fltr = "XML (*xml);; All (*.*)";
	QString seedFile = QSettings().value(saveKey, QVariant()).toString();
	QString fileName = QFileDialog::getOpenFileName(this, "Select Response File", seedFile, fltr);
	if( fileName.isEmpty() ){
		ui.respFileName->setText(QApplication::translate("MultiSpeakerServerClass", "<No Response File>", nullptr));
	}
	else {
		QString justname = fileName.mid(fileName.lastIndexOf("/")+1);
		ui.respFileName->setText("Response File: " + justname);
	}
	QSettings().setValue(saveKey, fileName);
}
//------------------------------------------------------------------------------
// RestoreState
//
void MultiSpeakerServer::RestoreState()
{
	restoreGeometry(QSettings().value(SK_MAIN_GEOMETRY).toByteArray());
	restoreState(QSettings().value(SK_MAIN_STATE).toByteArray());
}
//------------------------------------------------------------------------------
// SaveState
//
void MultiSpeakerServer::SaveState()
{
	QSettings().setValue(SK_MAIN_GEOMETRY, saveGeometry());
	QSettings().setValue(SK_MAIN_STATE, saveState());
}
//------------------------------------------------------------------------------
// closeEvent
//
void MultiSpeakerServer::closeEvent (QCloseEvent* e)
{
  SaveState();
  QMainWindow::closeEvent(e);
}
