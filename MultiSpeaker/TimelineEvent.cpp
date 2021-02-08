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
// Summary: TimelineEvent.cpp
//-------------------------------------------------------------------------------

#include "Settings.h"
#include "TimelineEvent.h"

//------------------------------------------------------------------------------
// TimelineEvent
//
TimelineEvent::TimelineEvent(QObject* parent)
  : QObject(parent), 
	m_doc(),
	m_host(""),
	m_method(""),
	m_namespace(STR_NAMESPACE_MULTISPEAK_ORG_VERSION_30),
	m_type(TimelineEvent::Request),
	m_id(0),
	m_srcHostId(0),
	m_timeStamp(0),
	m_enabled(false),
	m_hasBuddy(false)
{
}
//------------------------------------------------------------------------------
// TimelineEvent
//
TimelineEvent::TimelineEvent(int id, EventType type, int timeStamp, const QString& host, const QString& method, QDomDocument doc, const QString& ns, QObject* parent) 
  : QObject(parent), 
	m_doc(doc),
	m_host(host),
	m_method(method),
	m_namespace(ns),
	m_type(type),
	m_dstHostId(0),
	m_id(id),
	m_srcHostId(0),
	m_timeStamp(timeStamp),
	m_enabled(false),
	m_hasBuddy(false)
{
}
//------------------------------------------------------------------------------
// TimelineEvent
//
TimelineEvent::TimelineEvent(const TimelineEvent& e) 
  : QObject(),
	m_doc(e.m_doc),
	m_host(e.m_host),
	m_method(e.m_method),
	m_namespace(e.m_namespace),
	m_type(e.m_type),
	m_dstHostId(e.m_dstHostId),
	m_id(e.m_id),
	m_srcHostId(e.m_srcHostId),
	m_timeStamp(e.m_timeStamp),
	m_enabled(false),
	m_hasBuddy(false)
{
}
//------------------------------------------------------------------------------
// ~TimelineEvent
//
TimelineEvent::~TimelineEvent()
{
}
//------------------------------------------------------------------------------
// Copy
//
void TimelineEvent::Copy(const TimelineEvent& e)
{
	m_doc = e.m_doc;
	m_dstHostId = e.m_dstHostId;
	m_host = e.m_host;
	m_id = e.m_id;
	m_method = e.m_method;
	m_namespace = e.m_namespace;
	m_srcHostId = e.m_srcHostId;
	m_timeStamp = e.m_timeStamp;
	m_type = e.m_type;
}
//------------------------------------------------------------------------------
// TypeString
//
QString TimelineEvent::TypeString(EventType type) const 
{
	return ((type == Request) ? JSON_REQUEST_TAG : JSON_RESPONSE_TAG);
}

