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
// Summary: ServerWorker.cpp
//-------------------------------------------------------------------------------

#include <QCoreApplication>
#include <QDataStream>
#include <QDir>
#include <QHostAddress>
#include <QTcpSocket>
#include <QTime>

#include "ServerWorker.h"
#include "HttpResponse.h"

//------------------------------------------------------------------------------
// ServerWorker
//
ServerWorker::ServerWorker(qintptr socketDescriptor, QByteArray& qba, QObject* parent)
  : QObject(parent),
	m_bufferSize(0),
	m_bytesRead(0),
	m_bytesYettoRead(0),
	m_headerRead(false),
	m_socketDescriptor(socketDescriptor),
	m_responseFile(qba)
{
}
//------------------------------------------------------------------------------
// ~ServerWorker
//
ServerWorker::~ServerWorker()
{
}
//------------------------------------------------------------------------------
// ReadMessage
//
//	Note: HTTP 1.1 requests do not need to use a Content-Length header, either. They can use
//		Transfer-Encoding: chunked instead, in which case the message length is encoded inside
//		 the message data itself.
void ServerWorker::ReadMessage(QTcpSocket* socket)
{
	//QByteArray Header = "\n*** HTTP Header ***\n";
	QByteArray Header = "\n";
	QString errString = "Failed to read Header.";
	bool ContentLenRead = false;
	quint16 content_len=0;
	qint64 initBytesAvailable = socket->bytesAvailable(); // max tcp packet: 65,535, dunno why its a qint64...
	qint64 bytesAvailable=initBytesAvailable;

	//qDebug() << "Initial Bytes Available:" << initBytesAvailable;
	if( initBytesAvailable && (m_bytesYettoRead == 0) )
	{
		m_headerRead = false;
		// the header ends with a final empty line, that separates the data block from the header block.
		QString CLString;
		QString CL = "Content-Length:";
		do{
			if( socket->canReadLine() ){
				QString line =  socket->readLine();
				Header.append(line);
				if( line.startsWith(CL) ){
					ContentLenRead = true;
					CLString = line;
				}
				else if( ContentLenRead ){
					if( line.trimmed().isEmpty() )
						m_headerRead = true;
				}
			}
			else{
				QTime dieTime= QTime::currentTime().addSecs(1);
				while (QTime::currentTime() < dieTime)
					QCoreApplication::processEvents(QEventLoop::AllEvents, 100);
			}
			bytesAvailable = socket->bytesAvailable();
			//qDebug() << "Bytes Now Available:" << bytesAvailable;
		}while( !m_headerRead && bytesAvailable );

		if( ContentLenRead ){
			QStringList LenToken = CLString.split(CL, QString::SkipEmptyParts, Qt::CaseInsensitive);
			if (LenToken.length() == 1){
				QTextStream stream(&LenToken[0]);
				stream >> content_len;
				//qDebug() << "Content Length is " << content_len;
				m_bufferSize = content_len;
				m_bytesYettoRead = content_len;
			}
			else{
				errString =  "Failed to extract " + CL;
			}
		}
		else{
			errString =   "Failed to read Content Length ";
		}
		if (!m_headerRead)
		{
			qDebug() << errString;
			emit Message(errString.toLatin1());
			socket->readAll(); // read any remaining data
			m_bytesYettoRead = 0;
			return;
		}
		emit Message(Header);
		//qDebug() << QString("Header Size: %1.").arg(initBytesAvailable-bytesAvailable);
		//qDebug() << "Bytes left to read: " << bytesAvailable;
	}
	else{
		if( initBytesAvailable == 0 ){
			//qDebug() << "No bytesAvailable";
			return;
		}
		m_bufferSize =  static_cast <int>(m_bytesYettoRead);
	}
	if( bytesAvailable == 0 )
		return;
	//Header = "*** Message Content ***\n"; // note: reusing 'Header' string
	//emit Message(Header);
	QByteArray block;
	if (m_bufferSize == 0) // buffer size of 0 means we are streaming
	{
		block = socket->readAll(); // We are streaming so read it all
		emit Message(block);  // We are streaming with no idea of size of message so just emit and return
		qDebug() << "Streaming";
		m_bytesYettoRead = 0;
		return;
	}
	else
		block = socket->read(m_bufferSize); //  - m_bytesRead, Read at most what is left in this message

	m_buffer.append(block);
	m_bytesRead = block.size();
	m_bytesYettoRead -= m_bytesRead;
	if (m_bytesRead >= m_bufferSize)
	{
		//qDebug() << "Read all " << m_bytesRead << " bytes out of " << m_bufferSize;
		emit Message(static_cast <qint32>(m_bytesRead), m_buffer);
		m_buffer.clear();
	}
	else{
		//qDebug() << "Only Read " << m_bytesRead << " bytes out of " << m_bufferSize;
		emit Message(m_buffer);
		m_buffer.clear();
		return;
	}
	if (socket->bytesAvailable()){
		qDebug() << "recursive ReadMessage";
		ReadMessage(socket); // recursive, will reset ContentLenRead
	}
	QByteArray respdata = m_responseFile;
	if( respdata.isEmpty() )
		respdata="\n*** No Response File Selected *** ";

	SendResponse(200, respdata, socket);

	//  reset;sudo tcpdump -i lo -v	# capture loopback traffic
	//  show all data, in hex:  sudo tcpdump -i lo tcp and dst port 8888 -s0 -vv -X -c 1000
	// reset;sudo tcpdump -i lo tcp and dst port 8888 -s0 -A -c 100 -q -t -v >= 400
}
//------------------------------------------------------------------------------
// SendResponse
//
void ServerWorker::SendResponse( int code, QByteArray& data, QTcpSocket* socket )
{
	QString str;
	HttpResponse response(socket); // statusCode=200, statusText="OK";
	if( code != 200 ){
		response.setStatusFromCode(code );
	}
	/*
		what Multispeaker sends is:
			POST / HTTP/1.1
			SOAPAction: http://www.multispeak.org/V5.0/wsdl/CD_Server/InitiateConnectDisconnect

			request.setRawHeader("Accept", "application / soap + xml, application / dime, multipart / related, text/ *");
			request.setRawHeader("Host", QString("%1:%2").arg(host->ReqHostAddress()).arg(host->ReqHostPort()).toLatin1());
			request.setRawHeader("Content-Type", "text/xml;charset=utf-8");
			request.setRawHeader("Content-Length", QString::number(content.length()).toLatin1());
			request.setRawHeader("SOAPAction", QString("%1/%2").arg(e.Namespace(), e.Method()).toLatin1());
			

		what MultispeakerSerer sends is:
			SOAPAction: CD/InitiateConnectDiscnnectResponse
	*/
	response.setHeader("Content-Type", response.getContentType(0));
	response.setHeader("Content-Length",QByteArray::number(data.size()));
	response.setHeader("Connection","keep-alive"); // "close"
	response.setHeader("Server","MultiSpeakerServer");
	//response.setHeader("SOAPAction", "CD/InitiateConnectDisconnectResponse");
	response.setHeader("SOAPAction", "http://www.multispeak.org/V5.0/wsdl/CD_Server/InitiateConnectDisconnect");

	response.write(data,true);

	/*
	https://developer.mozilla.org/en-US/docs/Web/HTTP
	The Accept request HTTP header advertises which content types, expressed as MIME types, the client is
	able to understand. Using content negotiation, the server then selects one of the proposals, uses it
	and informs the client of its choice with the Content-Type response header.

	The Host request header specifies the domain name of the server (for virtual hosting), and (optionally)
	the TCP port number on which the server is listening.
	If no port is given, the default port for the service requested (e.g., "80" for an HTTP URL) is implied.
	A Host header field must be sent in all HTTP/1.1 request messages. A 400 (Bad Request) status code will
	be sent to any HTTP/1.1 request message that lacks a Host header field or contains more than one.

	if you are missing the Content-Length header on your HTTP response,
	the HTTP client does not know
	when the response is complete, so it keeps on waiting for more
	*/

}

//------------------------------------------------------------------------------
// OnConnected
//
void ServerWorker::OnConnected()
{
	qDebug() << "ServerWorker::OnConnected()";
}
//------------------------------------------------------------------------------
// OnDisconnected
//
//  When the socket has completed sending data back to the client the client will
//  Disconnect from host causing the 'disconnected' signal to fire back to here.  At 
//  This point the socket can be closed / deleted and the thread can be cleaned up
//  
//
void ServerWorker::OnDisconnected()
{
	qDebug() << "ServerWorker::OnConnected()";
	if (QTcpSocket* socket = qobject_cast<QTcpSocket*>(sender()))
		socket->deleteLater();
	emit Finished();
}
//------------------------------------------------------------------------------
// OnError
//
void ServerWorker::OnError(QAbstractSocket::SocketError socketError)
{
	// Don't care about the remote host closed error as the client will normally
	//  close when response message receieved
	if (socketError != QAbstractSocket::RemoteHostClosedError)
	{
		qDebug() << "ServerWorker::OnError()";
		if (QTcpSocket* socket = qobject_cast<QTcpSocket*>(sender()))
		{
			emit SocketError(socketError, socket->errorString());
			emit Finished();
		}
	}
}
//------------------------------------------------------------------------------
// OnReadyRead
//
// slot called when the socket has bytes to read
//
void ServerWorker::OnReadyRead()
{
	if (QTcpSocket* socket = qobject_cast<QTcpSocket*>(sender()))
	{
		ReadMessage(socket);
	}
}
//------------------------------------------------------------------------------
// OnStart
//
// Start processing data.
void ServerWorker::OnStart()
{
	QTcpSocket* socket = new QTcpSocket(this); // Create socket in new thread

	connect(socket, SIGNAL(connected()), this, SLOT(OnConnected()));
	connect(socket, SIGNAL(disconnected()), this, SLOT(OnDisconnected()));
	connect(socket, SIGNAL(error(QAbstractSocket::SocketError)), this, SLOT(OnError(QAbstractSocket::SocketError)));

	if (!socket->setSocketDescriptor(m_socketDescriptor))
	{
		emit SocketError(socket->error(), socket->errorString());
		qDebug() << "SpeakerServerWorker::OnStart() ERROR" << socket->errorString();
		emit Finished();
	}
	connect(socket, SIGNAL(readyRead()), this, SLOT(OnReadyRead()));
	qDebug() << "SpeakerServerWorker::OnStart()" << socket->peerAddress().toString() << socket->peerPort();
}
