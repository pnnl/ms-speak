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
//		2021 - CHM: for Phase3
//					Call setPeerVerifyMode(QSslSocket::VerifyNone)
//					Call ReadMessage() OnReadyRead().
//-------------------------------------------------------------------------------
//
// Summary: SslServer.cpp
//-------------------------------------------------------------------------------

#include <QDebug>
#include <QFile>
#include <QFileInfo>
#include <QMessageBox>
#include <QSslSocket>
#include <QThread>
// #include <QTime>
#include <QCoreApplication>

#include "ServerWorker.h"
#include "SslServer.h"
#include "HttpResponse.h"

//------------------------------------------------------------------------------
// SslServer
//
SslServer::SslServer( QObject* parent)
  : Server(parent),
	m_sslLocalCertificate(),
	m_sslPrivateKey(),
	m_sslProtocol(QSsl::TlsV1_2OrLater),
	m_bufferSize(0),
	m_bytesRead(0),
	m_srcId(0),
	m_dstId(0),
	m_headerSize(sizeof(quint32)),
	m_headerRead(false),
	m_parseContentLengthFlag(false),
	m_parseSourceAndDestIdFlag(false),
	m_Supported(false),
	m_bytesYettoRead(0)
{
	/*
	 * qt.network.ssl: Incompatible version of OpenSSL
	qDebug() << QSslSocket::sslLibraryBuildVersionString();
		"OpenSSL 1.0.2k-fips  26 Jan 2017"
	I've copied libcrypto.so and libssl.so (v1.0.2) to my current compiler lib directory
	(<QTDIR>/5.11.1/gcc_64/lib). In my case I took theese 2 libs in /usr/lib/x86_64-linux-gnu/:
	libssl.so.1.0.0 and libcrypto.so.1.0.0, copied and renamed. It worked for me.
		sudo cp libssl.so.1.1 /opt/Qt/Qt5.11.3/5.11.3/gcc_64/lib/libssl.so.1.0.0
		sudo cp libcrypto.so.1.1 /opt/Qt/Qt5.11.3/5.11.3/gcc_64/lib/libcrypto.so.1.0.0
		this did not work, tried this:
			make/install openssl-1.0.2k.tar.gz
			cd /usr/local/ssl/lib
			sudo cp libssl.so.1.0.0 /opt/Qt/Qt5.11.3/5.11.3/gcc_64/lib/libssl.so
			sudo cp libcrypto.so.1.0.0 /opt/Qt/Qt5.11.3/5.11.3/gcc_64/lib/libcrypto.so
		got this:
			error while loading shared libraries: libssl.so.1.0.0: cannot open shared object file: No such file or directory
		so did this:
			cd /opt/Qt/Qt5.11.3/5.11.3/gcc_64/lib
			sudo ln -s libssl.so libssl.so.1.0.0
			sudo ln -s libcrypto.so libcrypto.so.1.0.0
		and this worked.

		but on windoze:
			"OpenSSL 1.1.1d  10 Sep 2019"
			On windoze, the MultiSpeaker apps are built with Qt 5.15,
			on Linux, they are built with Qt 5.11.3 so that the are compatible with the
			native Debian 10 Qt libraries.

			I did this:
			QT 5.15:
				Make sure you have installed OpenSSL Toolkit using Qt Maintenance Tool
				Go to C:\Qt\Tools\OpenSSL\Win_x64\bin and search 
					for "libcrypto-1_1-x64.dll" and "libssl-1_1-x64.dll
				Copy them into the compiler folder (C:\Qt\5.15.0\msvc2015_64\bin)
			it installed OpenSSL 1.1.1j and i got
					C:\Qt\Tools\OpenSSL
			i now no longer get !QSslSocket::supportsSsl(), but
			i don't see the MS packet either,added openssl-1.1.1l-dev

			Debian, runtime:
				"QSslSocket: cannot resolve SSL_library_init"
				"you just need to install the package libssl-dev"
					- no, doesn't help, was already installed
				BUT, i mistakenly linked to the wrong file:
					libssl.so.1.0.0 -> libcrypto.so
				fixed it and it works now:
					libssl.so.1.0.0 -> libssl.so
			*/
	if( !QSslSocket::supportsSsl() ){
		//qDebug()<<"SSL version use for run-time: "<<QSslSocket::sslLibraryVersionNumber();
		QString qs2 = QSslSocket::sslLibraryBuildVersionString();
		QString qs = QStringLiteral("System does not support Qt OpenSSL Version:\n%1").arg(qs2);
		qDebug() << qs2;
		QMessageBox::information(Q_NULLPTR, "Unsupported Secure Socket Layer", qs);
	}
	else{
		m_Supported = true;
		connect(this, SIGNAL(newConnection()), this, SLOT(OnNewConnection()));
	}
}
//------------------------------------------------------------------------------
// ~SslServer
//
SslServer::~SslServer()
{
}
//------------------------------------------------------------------------------
// incomingConnection
//
void SslServer::incomingConnection(qintptr socketDescriptor)
{
	//qDebug() << "SslServer::incomingConnection()";
	QSslSocket* socket = new QSslSocket(this);
	if (!socket->setSocketDescriptor(socketDescriptor))
	{
		qDebug() << "SslServer::incomingConnection() ERROR: unable to setSocketDescriptor()";
		return;
	}
	QString qs;
	QTextStream out(&qs);
	out << "Incoming SSL Connection from " << socket->peerAddress().toString() <<
			", port " << socket->peerPort() << endl;
	emit Message(qs.toUtf8());

	connect(socket, SIGNAL(connected()), this, SLOT(OnConnected()));
	connect(socket, SIGNAL(disconnected()), this, SLOT(OnDisconnected()));
	connect(socket, SIGNAL(error(QAbstractSocket::SocketError)), this, SLOT(OnError(QAbstractSocket::SocketError)));

	m_headerSize = 0; // set to HTTP 1.1 POST header size, approx.
	//m_headerSize = 0;
	//m_headerSize += (m_parseSourceAndDestIdFlag) ? (2 * sizeof(quint32)) : 0;
	//m_headerSize += (m_parseContentLengthFlag) ? (sizeof(quint32)) : 0;

	m_headerRead = (m_headerSize == 0) ? true : false; // If the header size if 0 then there is no header

	connect(socket, SIGNAL(encrypted()), this, SLOT(OnEncrypted()));
	connect(socket, SIGNAL(encryptedBytesWritten(qint64)), this, SLOT(OnEncryptedBytesWritten(qint64)));
	
	connect(socket, SIGNAL(sslErrors(const QList<QSslError>&)), this, SLOT(OnSslErrors(const QList<QSslError>&)));
	connect(socket, SIGNAL(peerVerifyError(const QSslError&)), this, SLOT(OnPeerVerifyError(const QSslError&)));

	socket->setLocalCertificate(m_sslLocalCertificate);
	socket->setPrivateKey(m_sslPrivateKey);
	socket->setProtocol(m_sslProtocol);
	socket->startServerEncryption();
	//addPendingConnection(socket);
	socket->setPeerVerifyMode(QSslSocket::VerifyNone);
}
//------------------------------------------------------------------------------
// SetSslCertFolder
/*
bool SslServer::SetSslCertFolder(const QString& folder)
{
	/ *
	 * 2021 - don't see any reason to have this, certfolder never used
	if (!QFileInfo::exists(folder))
		return false;

	m_sslCertFolder = folder;
	* /
	Q_UNUSED(folder)
	return true;
}*/
//------------------------------------------------------------------------------
// SetSslLocalCertificate
//
bool SslServer::SetSslLocalCertificate(const QString& path, QSsl::EncodingFormat format)
{
	QFile certificateFile(path);

	if (!certificateFile.open(QIODevice::ReadOnly))
		return false;

	m_sslLocalCertificate = QSslCertificate(certificateFile.readAll(), format);
	return true;
}
//------------------------------------------------------------------------------
// SetSslPrivateKey
//
bool SslServer::SetSslPrivateKey(const QString& fileName, QSsl::KeyAlgorithm algorithm, QSsl::EncodingFormat format, const QByteArray& passPhrase)
{
	QFile keyFile(fileName);

	if (!keyFile.open(QIODevice::ReadOnly))
		return false;

	m_sslPrivateKey = QSslKey(keyFile.readAll(), algorithm, format, QSsl::PrivateKey, passPhrase);
	return true;
}

// 6.4.2021 - took ServerWorker::ReadMessage to use here since, we weren't
//			getting all the data, without delaying at a breakpoint
void SslServer::ReadMessage(QSslSocket* socket)
{
	//QByteArray Header = "\n*** HTTP Header ***\n";
	QByteArray Header = "\n";
	QString errString = "Failed to read Header.";
	bool ContentLenRead = false;
	quint16 content_len=0;
	qint64 initBytesAvailable = socket->bytesAvailable(); // max tcp packet: 65,535, dunno why its a qint64...
	qint64 bytesAvailable=initBytesAvailable;

	qDebug() << "Initial Bytes Available:" << initBytesAvailable;
	//emit Message("");
	if( initBytesAvailable && (m_bytesYettoRead == 0) )
	{
		m_headerRead = false;
		// the header ends with a final empty line, that separates the data block from the header block.
		QString CLString;
		QString CL = "Content-Length:";
		//bool once=false;
		do{
			if( socket->canReadLine() ){
				QString line =  socket->readLine();
				if( line.isEmpty() ){
					emit MessageLF(	"Unexpected Data Received: \\u0016\\u0003\\u0001\\u0002" );
					break; //  this seems to happen if we listen on nonssl 8443 and
					// MS sends a request as SSL
				}
				Header.append(line);
				if( line.startsWith(CL) ){
					ContentLenRead = true;
					CLString = line;
				}
				else if( ContentLenRead ){
					if( line.trimmed().isEmpty() )
						m_headerRead = true;
				}
				/*else{
					if( line.isEmpty() ){
						break;
					}
					if( !once )
					{
						errString = "";
						QTextStream out(&errString);
						//out << "Non Content-Len Data Read : " << line.toUtf8().toBase64();
						out << "Non Content-Len Data Read : " << line.toUtf8();
						emit MessageLF(errString.toUtf8());
						qDebug() << line;
						once=true;
					}
				}*/
			}
			else{
				QTime dieTime= QTime::currentTime().addSecs(1);
				while (QTime::currentTime() < dieTime)
					QCoreApplication::processEvents(QEventLoop::AllEvents, 100);
			}
			if( socket->isValid() )
				bytesAvailable = socket->bytesAvailable();
			//qDebug() << "Bytes Now Available:" << bytesAvailable; // 267
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
				errString = "Failed to extract " + CL;
			}
		}
		else{
			errString = "Failed to read Content Length";
		}
		if (!m_headerRead)
		{
			qDebug() << errString;
			emit MessageLF(errString.toLatin1());
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
		//m_buffer.clear();
	}
	else{
		//qDebug() << "Only Read " << m_bytesRead << " bytes out of " << m_bufferSize;
		emit Message(m_buffer);
		//m_buffer.clear();
		return;
	}
	if (socket->bytesAvailable()){
		qDebug() << "recursive ReadMessage";
		ReadMessage(socket); // recursive, will reset ContentLenRead
	}
	//QByteArray respdata = m_responseFile;
	QString respdata = ResponseFile();
	if( respdata.isEmpty() )
		respdata="\n*** No Response File Selected *** ";

	SendResponse(200, respdata, socket, m_buffer);
	m_buffer.clear();

	//  reset;sudo tcpdump -i lo -v	# capture loopback traffic
	//  show all data, in hex:  sudo tcpdump -i lo tcp and dst port 8888 -s0 -vv -X -c 1000
	// reset;sudo tcpdump -i lo tcp and dst port 8888 -s0 -A -c 100 -q -t -v >= 400
}

//------------------------------------------------------------------------------
// ReadMessage
/*
// 6.4.2021 - took ServerWorker::ReadMessage to use here since, we weren't
//			getting all the data, without delaying at a breakpoint
void SslServer::ReadMessage(QSslSocket* socket)
{
	qint64 bytesAvailable = socket->bytesAvailable();
	qDebug() << "Bytes Available:" << bytesAvailable;
	emit Message("ReadMessage::Bytes Available\n   ");

	if (bytesAvailable >= m_headerSize && !m_headerRead)
	{
		QDataStream in(socket);
		in.setByteOrder(QDataStream::BigEndian); // network byte order
		if (m_parseSourceAndDestIdFlag)
		{
			in >> m_srcId;
			in >> m_dstId;
			qDebug() << "SrcId:" << m_srcId << "DstId:" << m_dstId;
		}
		if (m_parseContentLengthFlag)
		{
			in >> m_bufferSize;
			qDebug() << "Content Length: " << m_bufferSize;
		}
		m_headerRead = true;
	}

	if (!m_headerRead)
	{
		ReadMessage(socket);
		return;
	}

	QByteArray block;
	if (m_bufferSize == 0) // buffer size of 0 means we are streaming
	{
		block = socket->readAll(); // We are streaming so read it all
		emit Message(block);  // We are streaming with no idea of size of message to just emit and return
		if( 0 ) //  allow for testing
			return;
	}
	else
		block = socket->read(m_bufferSize - m_bytesRead); // Read at most what is left in this message

	m_buffer.append(block);
	m_bytesRead += static_cast <unsigned int>(block.size());

	if (m_bytesRead >= m_bufferSize)
	{
		// emit complete message Get incoming Message
		QByteArray data;
		QDataStream in(m_buffer);
		in.setByteOrder(QDataStream::BigEndian); // network byte order

		in >> data;
		//qDebug() << data.count() << data;
		/ *
		if (m_parseSourceAndDestIdFlag)
			//   static_cast <unsigned int>(
			;//emit Message(m_srcId, m_dstId, static_cast <qint32>(m_bytesRead), m_buffer);
		else
			emit Message(static_cast <qint32>(m_bytesRead), m_buffer);
		* /
		m_headerRead = false;
	}
	if (socket->bytesAvailable())
		ReadMessage(socket);

	QString respdata = ResponseFile();
	if (respdata.isEmpty())
		respdata = "\n*** No Response File Selected *** ";

	SendResponse(200, respdata, socket, m_buffer);
	m_buffer.clear();

}*/

//------------------------------------------------------------------------------
// SendResponse
//
void SslServer::SendResponse( int code, QString& data, QSslSocket* socket, QByteArray& buffer)
{
	HttpResponse response(socket);
	QByteArray outbytes;
	response.SetData(code, data, buffer, outbytes);
	response.write(outbytes, true);
}

//------------------------------------------------------------------------------
// OnConnected
//
void SslServer::OnConnected()
{
	qDebug() << "SslServer::OnConnected()";
	emit Message("SslServer::OnConnected\n");
}
//------------------------------------------------------------------------------
// OnDisconnected
//
void SslServer::OnDisconnected()
{
	qDebug() << "SslServer::OnDisconnected()";
	if (QSslSocket* socket = qobject_cast<QSslSocket*>(sender()))
		socket->deleteLater();
}

//------------------------------------------------------------------------------
// OnEncrypted
//
void SslServer::OnEncrypted()
{
	qDebug() << "SslServer::OnEncrypted()";

	if (QSslSocket* socket = qobject_cast<QSslSocket*>(sender()))
	{
		connect(socket, SIGNAL(readyRead()), this, SLOT(OnReadyRead()));
		emit Message("SslServer::OnEncrypted\n");
	}
}

//------------------------------------------------------------------------------
// OnEncryptedBytesWritten
//
void SslServer::OnEncryptedBytesWritten(qint64 written)
{
	QString qs = QString("\nSslServer::OnEncryptedBytesWritten: %1\n").arg(written);
	QByteArray qb = qs.toUtf8();
	emit Message(qb);
	//emit MessageLF(qb);
}

//------------------------------------------------------------------------------
// OnError
//
void SslServer::OnError(QAbstractSocket::SocketError error)
{
	// Don't care about the remote host closed error as the client will normally
	//  close when response message receieved
	if (error != QAbstractSocket::RemoteHostClosedError)
	{
		qDebug() << "SslServer::OnError()";
		if (QTcpSocket* socket = qobject_cast<QTcpSocket*>(sender()))
		{
			emit SocketError(error, socket->errorString());
		}
	}
}
//------------------------------------------------------------------------------
// OnNewConnection
//
void SslServer::OnNewConnection()
{
	;
	//emit Message("Client connected to Server\n");

	/*
		Call nextPendingConnection() to accept the pending connection as a
		connected QTcpSocket. The function returns a pointer to a QTcpSocket in
		QAbstractSocket::ConnectedState that you can use for communicating with the
		client.
		If an error occurs, serverError() returns the type of error, and
		errorString() can be called to get a human readable description of what
		happened.

		Note: The returned QTcpSocket object cannot be used from another thread. 
		If you want to use an incoming connection from another thread, you need to 
		override incomingConnection().

	*/
	if( QSslSocket* socket = qobject_cast<QSslSocket*>(nextPendingConnection())  )
    {
		Q_UNUSED(socket);
		//qDebug() << "SslServer::OnNewConnection()";
		//emit Message("SslServer::OnNewConnection\n");
	}
	//else {
	//	emit Message("SslServer::OnNewConnection - No next Pending Connection\n");
	//}
}
//------------------------------------------------------------------------------
// OnReadyRead
//
void SslServer::OnReadyRead()
{
	qDebug() << "SslServer::OnReadyRead()";
	emit Message("SslServer::OnReadyRead\n");

	if (QSslSocket* socket = qobject_cast<QSslSocket*>(sender()))
	{
		ReadMessage(socket);
	}
}

//------------------------------------------------------------------------------
// OnSslErrors
//
void SslServer::OnSslErrors(const QList<QSslError>& errors)
{
	qDebug() << "SslServer::OnSslErrors() ErrorCount:" << errors.count();
	emit Message("SslServer::OnSslErrors\n");
}
//------------------------------------------------------------------------------
// OnPeerVerifyError
//
void SslServer::OnPeerVerifyError(const QSslError& error)
{
	qDebug() << "SslServer::OnPeerVerifyError()" << error.errorString();
	emit Message("SslServer::OnPeerVerifyError\n");
}

