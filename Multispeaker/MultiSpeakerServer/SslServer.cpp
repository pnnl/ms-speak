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
// Summary: SslServer.cpp
//-------------------------------------------------------------------------------

#include <QDebug>
#include <QFile>
#include <QFileInfo>
#include <QMessageBox>
#include <QSslSocket>
#include <QThread>

#include "ServerWorker.h"
#include "SslServer.h"

//------------------------------------------------------------------------------
// SslServer
//
SslServer::SslServer(QObject* parent)
  : Server(parent),
	m_sslLocalCertificate(),
	m_sslPrivateKey(),
	m_sslProtocol(QSsl::TlsV1_2OrLater),

	m_bufferSize(0),
	m_bytesRead(0),
	m_dstId(0),
	m_headerRead(false),
	m_headerSize(sizeof(quint32)),
	m_parseContentLengthFlag(false),
	m_parseSourceAndDestIdFlag(false),
	m_srcId(0)
{
	if (!QSslSocket::supportsSsl())
		QMessageBox::information(Q_NULLPTR, "Secure Socket Client", "This system does not support OpenSSL.");

	connect(this, SIGNAL(newConnection()), this, SLOT(OnNewConnection()));
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
  qDebug() << "SslServer::incomingConnection()";
  QSslSocket* socket = new QSslSocket(this);
  if (!socket->setSocketDescriptor(socketDescriptor))
  {
    qDebug() << "SslServer::incomingConnection() ERROR: unable to setSocketDescriptor()";
    return;
  }

  connect(socket, SIGNAL(connected()), this, SLOT(OnConnected()));
  connect(socket, SIGNAL(disconnected()), this, SLOT(OnDisconnected()));
  connect(socket, SIGNAL(error(QAbstractSocket::SocketError)), this, SLOT(OnError(QAbstractSocket::SocketError)));

  m_headerSize = 0; // set to HTTP 1.1 POST header size, approx.
  //m_headerSize = 0;
  //m_headerSize += (m_parseSourceAndDestIdFlag) ? (2 * sizeof(quint32)) : 0;
  //m_headerSize += (m_parseContentLengthFlag) ? (sizeof(quint32)) : 0;

  m_headerRead = (m_headerSize == 0) ? true : false; // If the header size if 0 then there is no header

  connect(socket, SIGNAL(encrypted()), this, SLOT(OnEncrypted()));
  connect(socket, SIGNAL(sslErrors(const QList<QSslError>&)), this, SLOT(OnSslErrors(const QList<QSslError>&)));
  connect(socket, SIGNAL(peerVerifyError(const QSslError&)), this, SLOT(OnPeerVerifyError(const QSslError&)));

  socket->setLocalCertificate(m_sslLocalCertificate);
  socket->setPrivateKey(m_sslPrivateKey);
  socket->setProtocol(m_sslProtocol);
  socket->startServerEncryption();
  //addPendingConnection(socket);
}
//------------------------------------------------------------------------------
// SetSslCertFolder
//
bool SslServer::SetSslCertFolder(const QString& folder)
{
  if (!QFileInfo::exists(folder))
    return false;

  m_sslCertFolder = folder;
  return true;
}
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
//------------------------------------------------------------------------------
// ReadMessage
//
void SslServer::ReadMessage(QSslSocket* socket)
{
	qint64 bytesAvailable = socket->bytesAvailable();
	qDebug() << "Bytes Available:" << bytesAvailable;
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
		if (m_parseSourceAndDestIdFlag)
			//   static_cast <unsigned int>(
			;//emit Message(m_srcId, m_dstId, static_cast <qint32>(m_bytesRead), m_buffer);
		else
			emit Message(static_cast <qint32>(m_bytesRead), m_buffer);
		m_headerRead = false;
	}
	if (socket->bytesAvailable())
		ReadMessage(socket);
}
//------------------------------------------------------------------------------
// OnConnected
//
void SslServer::OnConnected()
{
	qDebug() << "SslServer::OnConnected()";
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
	}
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
    if (QSslSocket* socket = qobject_cast<QSslSocket*>(nextPendingConnection()))
    {
        Q_UNUSED(socket);
        qDebug() << "SslServer::OnNewConnection()";
    }
}
//------------------------------------------------------------------------------
// OnReadyRead
//
void SslServer::OnReadyRead()
{
  qDebug() << "SslServer::OnReadyRead()";
}
//------------------------------------------------------------------------------
// OnSslErrors
//
void SslServer::OnSslErrors(const QList<QSslError>& errors)
{
  qDebug() << "SslServer::OnSslErrors() ErrorCount:" << errors.count();
}
//------------------------------------------------------------------------------
// OnPeerVerifyError
//
void SslServer::OnPeerVerifyError(const QSslError& error)
{
  qDebug() << "SslServer::OnPeerVerifyError()" << error.errorString();
}

