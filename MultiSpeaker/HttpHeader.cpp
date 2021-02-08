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
// Summary: HttpHeader.cpp
//-------------------------------------------------------------------------------

#include <QByteArrayMatcher>
#include <QDebug>
#include <QNetworkRequest>

#include "HttpHeader.h"

//------------------------------------------------------------------------------
// HttpHeader
//
HttpHeader::HttpHeader(QObject *parent)
  : QObject(parent)
{
}
//------------------------------------------------------------------------------
// ~HttpHeader
//
HttpHeader::~HttpHeader()
{
}
//------------------------------------------------------------------------------
// HeaderField
//
QByteArray HttpHeader::HeaderField(const QByteArray& name, const QByteArray& defaultValue) const
{
  QList<QByteArray> allValues = HeaderFieldValues(name);
  if (allValues.isEmpty())
    return defaultValue;

  // Concatinate all found values with comma delim
  QByteArray result;
  bool first = true;
  foreach (const QByteArray& value, allValues) 
  {
    if (!first)
      result += ", ";
    first = false;
    result += value;
  }
  return result;
}
//------------------------------------------------------------------------------
// HeaderFieldValues
//
QList<QByteArray> HttpHeader::HeaderFieldValues(const QByteArray& name) const
{
  QList<QByteArray> result;
  QList<QPair<QByteArray, QByteArray> >::ConstIterator it = m_httpFields.constBegin();
  for ( ; it != m_httpFields.constEnd(); ++it)
  {
    if (qstricmp(name.constData(), it->first) == 0) // qstricmp is a case insensitive compare
      result += it->second;
  }
  return result;
}
//------------------------------------------------------------------------------
// HeaderName
//
QByteArray HttpHeader::HeaderName(QNetworkRequest::KnownHeaders header)
{
  switch (header) 
  {
    case QNetworkRequest::ContentDispositionHeader: return STR_KNOWN_HEADER_CONTENT_DISPOSITION;
    case QNetworkRequest::ContentTypeHeader: return STR_KNOWN_HEADER_CONTENT_TYPE;
    case QNetworkRequest::ContentLengthHeader: return STR_KNOWN_HEADER_CONTENT_LENGTH;
    case QNetworkRequest::CookieHeader: return STR_KNOWN_HEADER_COOOKIE;
    case QNetworkRequest::LastModifiedHeader: return STR_KNOWN_HEADER_LAST_MODIFIED;
    case QNetworkRequest::LocationHeader: return STR_KNOWN_HEADER_LOCATION;
    case QNetworkRequest::ServerHeader: return STR_KNOWN_HEADER_SERVER;
    case QNetworkRequest::SetCookieHeader: return STR_KNOWN_HEADER_SET_COOKIE;
    case QNetworkRequest::UserAgentHeader: return STR_KNOWN_HEADER_USER_AGENT;
    // no default: if new values are added, this will generate a compiler warning
  };
  return QByteArray();
}
//------------------------------------------------------------------------------
// SetHeaderField
//
void HttpHeader::SetHeaderField(const QByteArray& name, const QByteArray& data)
{
  QList<QPair<QByteArray, QByteArray> >::Iterator it = m_httpFields.begin();
  while (it != m_httpFields.end()) 
  {
    if (qstricmp(name.constData(), it->first) == 0)
      it = m_httpFields.erase(it);
    else
      ++it;
  }
  m_httpFields.append(qMakePair(name, data));
}
//------------------------------------------------------------------------------
// SetHost
//
void HttpHeader::SetHost(const QString& host, bool useSecureHTTP, int port)
{
  m_httpHost.setHost(host);
  m_httpHost.setScheme(useSecureHTTP ? QLatin1String("https") : QLatin1String("http"));
  if (port)
    m_httpHost.setPort(port);
  else
    m_httpHost.setPort(useSecureHTTP ? 443 : 80);
}
//------------------------------------------------------------------------------
// ParseHeader
//
void HttpHeader::ParseHeader(const QByteArray& header)
{
  // see rfc2616, sec 4 for information about HTTP/1.1 headers.
  // allows relaxed parsing here, accepts both CRLF & LF line endings
  const QByteArrayMatcher lf("\n");
  const QByteArrayMatcher colon(":");
  int i = 0;
  while (i < header.count()) 
  {
    int j = colon.indexIn(header, i); // field-name
    if (j == -1)
      break;
    const QByteArray field = header.mid(i, j - i).trimmed();
    j++;
    // any number of LWS is allowed before and after the value
    QByteArray value;
    do 
    {
      i = lf.indexIn(header, j);
      if (i == -1)
          break;
      if (!value.isEmpty())
          value += ' ';
      // check if we have CRLF or only LF
      bool hasCR = (i && header[i-1] == '\r');
      int length = i -(hasCR ? 1: 0) - j;
      value += header.mid(j, length).trimmed();
      j = ++i;
    } while (i < header.count() && (header.at(i) == ' ' || header.at(i) == '\t'));

    if (i == -1)
      break; // something is wrong

   m_httpFields.append(qMakePair(field, value));
  }
}
//------------------------------------------------------------------------------
// HttpRequest::ToHttpMessage
//
//  Combines the Http Header info witht he content to create the entire HttpMessage 
//  Currently only does a http Post
//
QByteArray HttpRequest::ToHttpMessage()
{
  QByteArray msg;
  msg.reserve(40 + m_httpFields.length()*25 + m_httpContent.size()); // very rough lower bound estimation

  // Method line
  msg += "POST";
  msg += ' ';
  msg += m_httpHost.path().toLatin1();
  msg += " HTTP/";
  msg += QByteArray::number(MajorVersion());
  msg += '.';
  msg += QByteArray::number(MinorVersion());
  msg += "\r\n";

  // Host line
  msg += "Host: ";
  msg += m_httpHost.host().toLatin1();
  msg += ":";
  msg += QByteArray::number(m_httpHost.port());
  msg += "\r\n";

  // Header Fields
  QList<QPair<QByteArray, QByteArray> >::const_iterator it = m_httpFields.constBegin();
  for (; it != m_httpFields.constEnd(); ++it) 
  {
    msg += it->first;
    msg += ": ";
    msg += it->second;
    msg += "\r\n";
  }
  msg += "\r\n"; // Empty line signalling end of Http Header

  // Content
  msg += m_httpContent;
  
  qDebug() << msg;

  return msg;
}
//------------------------------------------------------------------------------
// HttpResponse::ToHttpMessage
//
//  Combines the Http Header info with the content to create the entire HttpMessage 
//  Currently only does a http Post Response
//
QByteArray HttpResponse::ToHttpMessage()
{
  QByteArray msg;
  msg.reserve(40 + m_httpFields.length()*25 + m_httpContent.size()); // very rough lower bound estimation

  // Status line
  msg += " HTTP/";
  msg += QByteArray::number(MajorVersion());
  msg += '.';
  msg += QByteArray::number(MinorVersion());
  msg += " 200 OK\r\n";

  // Header Fields
  QList<QPair<QByteArray, QByteArray> >::const_iterator it = m_httpFields.constBegin();
  for (; it != m_httpFields.constEnd(); ++it) 
  {
    msg += it->first;
    msg += ": ";
    msg += it->second;
    msg += "\r\n";
  }
  msg += "\r\n"; // Empty line signalling end of Http Header

  // Content
  msg += m_httpContent;
  return msg;
}

