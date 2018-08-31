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

//------------------------------------------------------------------------------
// ServerWorker
//
ServerWorker::ServerWorker(qintptr socketDescriptor, QObject* parent)
  : QObject(parent),
	m_bufferSize(0),
	m_bytesRead(0),
	m_headerRead(false),
	m_socketDescriptor(socketDescriptor)
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
	QByteArray Header = "\n*** HTTP Header ***\n";
	QString errString;
	bool ContentLenRead = false;
	qint64 bytesAvailable = socket->bytesAvailable();
	//qDebug() << "Bytes Available:" << bytesAvailable;
	if (bytesAvailable)
	{
		// the header ends with a final empty line, that separates the data block from the header block.
		QString CLString;
		QString CL = "Content-Length:";
		do{
			if( socket->canReadLine() ){
				QString line =  socket->readLine();
				Header.append(line);
				//qDebug() << "Read Line from Socket: " << line;
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
		}while( !m_headerRead && bytesAvailable );

		if( ContentLenRead ){
			quint16 content_len;
			QStringList LenToken = CLString.split(CL, QString::SkipEmptyParts, Qt::CaseInsensitive);
			if (LenToken.length() == 1){
				QTextStream stream(&LenToken[0]);
				stream >> content_len;
				//qDebug() << "Content Length is " << content_len;
				//errString = QString("Content Length is %1.").arg(content_len);
				//emit Message(errString.toLatin1());
				m_bufferSize = content_len;
			}
			else{
				errString =  "Failed to extract " + CL;
			}
		}
		else{
			errString =   "Failed to read Content Length ";
		}
	}
	emit Message(Header);

	if (!m_headerRead)
	{
		qDebug() << errString;
		emit Message(errString.toLatin1());
		//ReadMessage(socket);
		socket->readAll(); // read any remaining data
		return;
	}
	m_headerRead = false;

	Header = "*** Message Content ***\n";
	emit Message(Header);
	QByteArray block;
	if (m_bufferSize == 0) // buffer size of 0 means we are streaming
	{
		block = socket->readAll(); // We are streaming so read it all
		emit Message(block);  // We are streaming with no idea of size of message so just emit and return
		return;
	}
	else
		block = socket->read(m_bufferSize); //  - m_bytesRead, Read at most what is left in this message

	m_buffer.append(block);
	m_bytesRead = block.size();

	if (m_bytesRead >= m_bufferSize)
	{
		/* emit complete message Get incoming Message
		QByteArray data;
		QDataStream in(m_buffer);
		in.setByteOrder(QDataStream::BigEndian); // network byte order
		in >> data;*/
		//emit Message(m_bytesRead, m_buffer);
		emit Message(m_buffer);
		//m_headerRead = false;
	}
	if (socket->bytesAvailable())
		ReadMessage(socket);

	socket->write("HTTP/1.1 200 OK\r\n********************XYZX"); // \r needs to be before \n
	/*
	 * Send back response:
	socket->write("Content-Type: text/html\r\n");
	socket->write("Content-Length: text/html\r\n");
	socket->write(_response_msg);
	*/
	//  reset;sudo tcpdump -i lo -v	# capture loopback traffic
	//  show all data, in hex:  sudo tcpdump -i lo tcp and port 7777 -s0 -vv -X -c 1000
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
