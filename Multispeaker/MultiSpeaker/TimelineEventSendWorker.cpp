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
// Summary: TimelineEventSendWorker.cpp
//-------------------------------------------------------------------------------

#include <QTcpSocket>

#include "TimelineEventSendWorker.h"
#include "WsdlFile.h"

//------------------------------------------------------------------------------
// TimelineEventSendWorker
//
TimelineEventSendWorker::TimelineEventSendWorker(const QHostAddress& hostAddress, int hostPort, TimelineEvent& e, QObject* parent)
  : QObject(parent),
	m_hostAddress(hostAddress),
	m_hostPort(hostPort),
	m_timelineEvent(e)
{
}
//------------------------------------------------------------------------------
// ~TimelineEventSendWorker
//
TimelineEventSendWorker::~TimelineEventSendWorker()
{
}
//------------------------------------------------------------------------------
// PerformFinishedCleanup
//
void TimelineEventSendWorker::PerformFinishedCleanup(QTcpSocket* socket)
{
	socket->close();
	socket->deleteLater();
	emit Finished();
}
//------------------------------------------------------------------------------
// OnConnected
//
void TimelineEventSendWorker::OnConnected()
{
	if (QTcpSocket* socket = qobject_cast<QTcpSocket*>(sender()))
	{
		QByteArray content = WsdlFile::XmlSoap(m_timelineEvent, 2, true);
		QDataStream os(socket);
		os.setByteOrder(QDataStream::BigEndian); // network byte order
		os << (qint32) m_timelineEvent.SrcHostId();
		os << (qint32) m_timelineEvent.DstHostId();
		//os << (qint32) content.size(); // This overloaded operator will write the size (4 bytes) before the content
		os << content;
		if (!socket->waitForBytesWritten())
			emit Error(socket->error(), socket->errorString());
		PerformFinishedCleanup(socket);
	}
}
//------------------------------------------------------------------------------
// OnError
//
void TimelineEventSendWorker::OnError(QAbstractSocket::SocketError socketError)
{
	if (QTcpSocket* socket = qobject_cast<QTcpSocket*>(sender()))
	{
		emit Error(socketError, socket->errorString());
		PerformFinishedCleanup(socket);
	}
}
//------------------------------------------------------------------------------
// OnStart
//
// Start processing data.
void TimelineEventSendWorker::OnStart()
{
	QTcpSocket* socket = new QTcpSocket(this); // Create socket in new thread
	connect(socket, SIGNAL(connected()), this, SLOT(OnConnected()));
	connect(socket, SIGNAL(error(QAbstractSocket::SocketError)), this, SLOT(OnError(QAbstractSocket::SocketError)));

	socket->connectToHost(m_hostAddress, m_hostPort);
}
