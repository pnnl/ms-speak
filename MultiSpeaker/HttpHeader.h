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
// Summary: HttpHeader.h
//-------------------------------------------------------------------------------

#ifndef HTTPHEADER_H
#define HTTPHEADER_H

#include <QHash>
#include <QNetworkRequest>
#include <QObject>

const QByteArray STR_KNOWN_HEADER_CONTENT_DISPOSITION = "Content-Disposition";
const QByteArray STR_KNOWN_HEADER_CONTENT_TYPE = "Content-Type";
const QByteArray STR_KNOWN_HEADER_CONTENT_LENGTH = "Content-Length";
const QByteArray STR_KNOWN_HEADER_COOOKIE = "Cookie";
const QByteArray STR_KNOWN_HEADER_LAST_MODIFIED = "Last-Modified";
const QByteArray STR_KNOWN_HEADER_LOCATION = "Location";
const QByteArray STR_KNOWN_HEADER_SERVER = "Server";
const QByteArray STR_KNOWN_HEADER_SET_COOKIE = "Set-Cookie";
const QByteArray STR_KNOWN_HEADER_USER_AGENT = "User-Agent";

const QByteArray STR_SOAP_ACTION = "SOAPAction";

//------------------------------------------------------------------------------
// HttpHeader
//
class HttpHeader : public QObject
{
  Q_OBJECT
protected:
  QByteArray m_httpContent;
  QList<QPair<QByteArray, QByteArray> > m_httpFields;
  QUrl m_httpHost;

public:
  HttpHeader(QObject* parent);
  ~HttpHeader();

  QUrl Url() const;

  int ContentLength() const {return HeaderField(STR_KNOWN_HEADER_CONTENT_LENGTH, "0").toInt();}
  virtual int MajorVersion() const {return 1;}
  virtual int MinorVersion() const {return 1;}

  const QList<QPair<QByteArray, QByteArray> > Header() {return m_httpFields;}
  QByteArray HeaderField(const QByteArray& name, const QByteArray& defaultValue = QByteArray()) const;
  QList<QByteArray> HeaderFieldValues(const QByteArray& name) const;
  QByteArray HeaderName(QNetworkRequest::KnownHeaders header);


  virtual QByteArray ToHttpMessage() = 0; // Then entire message with header and content (Note content-length will be auto calc based on content)

  void SetContent(const QByteArray& content) {m_httpContent = content; SetHeaderField(STR_KNOWN_HEADER_CONTENT_LENGTH, QByteArray::number(m_httpContent.size()));}
  void SetHeaderField(const QByteArray& name, const QByteArray& data);
  void SetHost(const QString& host, bool useSecureHTTP = false, int port = 0);
  void SetHost(const QString& host, int port) {SetHost(host, false, port);}
  void SetUrl(const QUrl& url) {m_httpHost = url;}

protected:
  virtual void ParseHeader(const QByteArray& header);
};
//------------------------------------------------------------------------------
// HttpRequest
//
class HttpRequest : public HttpHeader
{
public:
  HttpRequest(QObject* parent=0) : HttpHeader(parent) {}
  HttpRequest(const QByteArray& httpHeader, QObject* parent=0) : HttpHeader(parent) {ParseHeader(httpHeader);}
  ~HttpRequest() {}

  virtual QByteArray ToHttpMessage();

protected:
  virtual void ParseHeader(const QByteArray& httpHeader) {HttpHeader::ParseHeader(httpHeader);}
};
//------------------------------------------------------------------------------
// HttpResponse
//
class HttpResponse : public HttpHeader
{
private:
  QByteArray m_httpStatus;

public:
  HttpResponse(QObject* parent=0) : HttpHeader(parent) {}
  HttpResponse(const QByteArray& httpHeader, QObject* parent=0) : HttpHeader(parent) {ParseHeader(httpHeader);}
  ~HttpResponse() {}

  virtual int MajorVersion() const {return 1;}
  virtual int MinorVersion() const {return 1;}

  void SetHttpStatus(const QByteArray& status) {m_httpStatus = status;}
  virtual QByteArray ToHttpMessage();

protected:
  virtual void ParseHeader(const QByteArray& httpHeader) {HttpHeader::ParseHeader(httpHeader);}
};



#endif // HTTPHEADER_H
