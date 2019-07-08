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
// Summary: Server.cpp
//-------------------------------------------------------------------------------

#include <QDataStream>
#include <QMessageBox>
#include <QSettings>
#include <QTcpSocket>
#include <QThread>
#include <QFile>

#include "Server.h"
#include "ServerWorker.h"

//------------------------------------------------------------------------------
// Server
//
Server::Server(QObject* parent)
  : QTcpServer(parent)
{
}
//------------------------------------------------------------------------------
// ~Server
//
Server::~Server()
{
  close(); // the server will no longer listen for incoming connections
}
//------------------------------------------------------------------------------
// incomingConnection
//
//  Overwrite this virtual function to create a return message
//
void Server::incomingConnection(qintptr socketDescriptor)
{
	qDebug() << "Server::incomingConnection():" << serverAddress().toString() << serverPort();
	QThread* thread = new QThread;
	ServerWorker* worker = new ServerWorker(socketDescriptor,m_responseFile);
	worker->moveToThread(thread);
	connect(worker, SIGNAL(SocketError(QAbstractSocket::SocketError, const QString&)), this, SIGNAL(SocketError(QAbstractSocket::SocketError, const QString&)));
	connect(worker, SIGNAL(Finished()), thread, SLOT(quit()));
	connect(worker, SIGNAL(Finished()), worker, SLOT(deleteLater()));
	connect(worker, SIGNAL(Message(const QByteArray&)), this, SIGNAL(Message(const QByteArray&)));
	connect(worker, SIGNAL(Message(int, const QByteArray&)), this, SIGNAL(Message(int, const QByteArray&)));
	connect(thread, SIGNAL(finished()), thread, SLOT(deleteLater()));
	connect(thread, SIGNAL(started()), worker, SLOT(OnStart()));
	thread->start();
}
//------------------------------------------------------------------------------
// SetResponseFile
//
bool Server::SetResponseFile(const QString& path)
{
	Q_UNUSED(path);

	/*
	QFile responseFile(path);
	if (!responseFile.open(QIODevice::ReadOnly))
		return false;
	// QByteArray m_responseFile;
	m_responseFile = responseFile.readAll();
	*/
	
	//const char  *pResponse =
	m_responseFile =
		"<?xml version=\"1.0\" encoding=\"utf-8\"?>"
		"<soapenv:Envelope xmlns:tns=\"%1\" xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:res=\"http://www.multispeak.org/V5.0/ws/response\" xmlns:com=\"http://www.multispeak.org/V5.0/commonTypes\">"
		"<soapenv:Header>"
		"<res:MultiSpeakResponseMsgHeader MessageID = \"%2\" TimeStamp=\"%3\">"
		"<res:MultiSpeakVersion>"
		"<com:MajorVersion>5</com:MajorVersion>"
		"<com:MinorVersion>1</com:MinorVersion>"
		"<com:Build>0</com:Build>"
		"</res:MultiSpeakVersion>"
		"<res:Caller>"
		"<com:AppName>%4</com:AppName>"
		"<com:Company>%5</com:Company>"
		"</res:Caller>"
		"<res:Result>"
		"<com:resultIdentifier>"
		"<com:replyCodeCategory>0</com:replyCodeCategory>"
		"<com:index>0</com:index>"
		"</com:resultIdentifier>"
		"<com:resultDescription>Success / no errors.</com:resultDescription>"
		"</res:Result>"
		"</res:MultiSpeakResponseMsgHeader>"
		"</soapenv:Header>"
		"<soapenv:Body>"
		"<tns:%6 xmlns:tns=\"%7\" xmlns:arrays=\"http://www.multispeak.org/V5.0/commonArrays\" xmlns:enum=\"http://www.multispeak.org/V5.0/enumerations\" xmlns:msp=\"http://www.multispeak.org/V5.0\" xmlns:soap12=\"http://schemas.xmlsoap.org/wsdl/soap12/\" xmlns:http=\"http://schemas.xmlsoap.org/wsdl/http/\" xmlns:mime=\"http://schemas.xmlsoap.org/wsdl/mime/\" xmlns:response=\"http://www.multispeak.org/V5.0/ws/response\" xmlns:tm=\"http://microsoft.com/wsdl/mime/textMatching/\" xmlns:soapenc=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:request=\"http://www.multispeak.org/V5.0/ws/request\" xmlns:com=\"http://www.multispeak.org/V5.0/commonTypes\" xmlns:prim=\"http://www.multispeak.org/V5.0/primitives\" xmlns:soap=\"http://schemas.xmlsoap.org/wsdl/soap/\" xmlns:ns9=\"http://www.w3.org/2005/08/addressing\" xmlns:ns8=\"http://docs.oasis-open.org/wsrf/bf-2\" xmlns:wsdl=\"http://schemas.xmlsoap.org/wsdl/\">"
			"%8"
		"</tns:%9>"
		"</soapenv:Body>"
		"</soapenv:Envelope>";
	//m_responseFile = QByteArray(pResponse, -1);

	return true;
}
