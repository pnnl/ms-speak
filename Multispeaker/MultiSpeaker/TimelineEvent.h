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
// Summary: TimelineEvent.h
//-------------------------------------------------------------------------------

#ifndef TIMELINEEVENT_H
#define TIMELINEEVENT_H

#include <QDomDocument>
#include <QObject>

class TimelineEvent : public QObject
{
	Q_OBJECT
public:
	enum EventType {Request, Response};

private:
	QDomDocument m_doc;
	QString m_host;
	QString m_method;
	QString m_namespace; // the xmlns:tns namespace for this event
	EventType m_type;    // Request or Response
	int m_dstHostId;
	int m_id;
	int m_srcHostId;
	int m_timeStamp;
	bool m_enabled;
	bool m_hasBuddy;

public:
	TimelineEvent(QObject* parent=Q_NULLPTR);
	TimelineEvent(int id, EventType type, int timeStamp, const QString& host, const QString& method, QDomDocument doc, const QString& ns, QObject* parent=Q_NULLPTR);
	TimelineEvent(const TimelineEvent& e);
	~TimelineEvent();

	bool HasBuddy() {return m_hasBuddy;}
	void HasBuddy(bool b) {m_hasBuddy=b;}
	/* 'const' after the function name makes the function const itself. This is only for member functions. Making a member function const means that it cannot
	 * call any non-const member functions, nor can it change any member variables. It also means that the function can only be called via a const object of the class.
	 */
	bool IsEnabled() const {return m_enabled;}
	void IsEnabled(bool b) {m_enabled=b;}

	void Copy(const TimelineEvent& e);
	QDomDocument Doc() const {return m_doc;}
	int DstHostId() const {return m_dstHostId;}

	QString Host() {return m_host;}
	const QString Host() const {return m_host;}

	int Id() const {return m_id;}

	QString Method() {return m_method;}
	const QString Method() const {return m_method;}

	QString Namespace() const {return m_namespace;}

	void SetDoc(const QByteArray& bytes) {m_doc.setContent(bytes);}
	void SetDstHostId(int id) {m_dstHostId = id;}
	void SetHost(const QString& host) {m_host = host;}
	void SetId(int id) {m_id = id;}
	void SetMethod(const QString& method) {m_method = method;}
	void SetNamespace(const QString& ns) {m_namespace = ns;}
	void SetSrcHostId(int id) {m_srcHostId = id;}
	void SetTimeStamp(int ts) {m_timeStamp = ts;}
	void SetType(TimelineEvent::EventType type) {m_type = type;}

	int SrcHostId() const {return m_srcHostId;}

	int TimeStamp() const {return m_timeStamp;}
	EventType Type() const {return m_type;}
	QString TypeString(EventType type) const;
};

#endif // TIMELINEEVENT_H
