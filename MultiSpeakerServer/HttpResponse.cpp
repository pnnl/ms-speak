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
// Summary: HttpResponse.cpp
//-------------------------------------------------------------------------------
/* https://stackoverflow.com/questions/34633396/the-value-of-the-http-header-soapaction-was-not-recognized-by-the-server
	SOAP Version 1.1 requires a HTTP header in your SOAP request to specify the SOAP action. It's not in the actual XML, 
	it's part of the request (in the HTTP header), so that is why you are not seeing any difference between your SoapUI 
	request xml, and the request you're sending using the WebServiceTemplate. Soap 1.2 allows you to set it as an attribute
	on the media type, but that is not valid for a 1.1 server. Note that according to the specification, the value you use 
	doesn't have to be resolvable.

	SOAP places no restrictions on the format or specificity of the URI or that it is resolvable. An HTTP client MUST use 
	this header field when issuing a SOAP HTTP Request.

	Usually, it's specified in your WSDL, something like (taken from here):
		<soap:operation
			soapAction="http://www5v80.elsyarres.net/searchFlights"
		style="document" />
*/
#include "HttpResponse.h"

HttpResponse::HttpResponse(QTcpSocket* socket)
{
    this->socket=socket;
    statusCode=200;
    statusText="OK";
    sentHeaders=false;
    sentLastPart=false;
    chunkedMode=false;
}

void HttpResponse::setHeader(QByteArray name, QByteArray value)
{
    Q_ASSERT(sentHeaders==false);
    headers.insert(name,value);
}

void HttpResponse::setHeader(QByteArray name, int value)
{
    Q_ASSERT(sentHeaders==false);
    headers.insert(name,QByteArray::number(value));
}

QMap<QByteArray,QByteArray>& HttpResponse::getHeaders()
{
    return headers;
}

void HttpResponse::setStatusFromCode(int statusCode )
{
	setStatus(statusCode, getStatus(statusCode));
}
void HttpResponse::setStatus(int statusCode, QByteArray description)
{
	this->statusCode=statusCode;
	statusText=description;
}

int HttpResponse::getStatusCode() const
{
   return this->statusCode;
}

void HttpResponse::writeHeaders()
{
    Q_ASSERT(sentHeaders==false);
    QByteArray buffer;
    buffer.append("HTTP/1.1 ");
    buffer.append(QByteArray::number(statusCode));
    buffer.append(' ');
    buffer.append(statusText);
    buffer.append("\r\n");
    foreach(QByteArray name, headers.keys())
    {
        buffer.append(name);
        buffer.append(": ");
        buffer.append(headers.value(name));
        buffer.append("\r\n");
    }
	/*foreach(HttpCookie cookie,cookies.values())
    {
        buffer.append("Set-Cookie: ");
        buffer.append(cookie.toByteArray());
        buffer.append("\r\n");
	}*/
    buffer.append("\r\n");
    writeToSocket(buffer);
    sentHeaders=true;
}

bool HttpResponse::writeToSocket(QByteArray data)
{
    int remaining=data.size();
    char* ptr=data.data();
    while (socket->isOpen() && remaining>0)
    {
        // If the output buffer has become large, then wait until it has been sent.
        if (socket->bytesToWrite()>16384)
        {
            socket->waitForBytesWritten(-1);
        }

        int written=socket->write(ptr,remaining);
        if (written==-1)
        {
          return false;
        }
        ptr+=written;
        remaining-=written;
    }
    return true;
}

void HttpResponse::write(QByteArray data, bool lastPart)
{
    Q_ASSERT(sentLastPart==false);

    // Send HTTP headers, if not already done (that happens only on the first call to write())
    if (sentHeaders==false)
    {
        // If the whole response is generated with a single call to write(), then we know the total
        // size of the response and therefore can set the Content-Length header automatically.
        if (lastPart)
        {
           // Automatically set the Content-Length header
           headers.insert("Content-Length",QByteArray::number(data.size()));
        }

        // else if we will not close the connection at the end, them we must use the chunked mode.
        else
        {
            QByteArray connectionValue=headers.value("Connection",headers.value("connection"));
            bool connectionClose=QString::compare(connectionValue,"close",Qt::CaseInsensitive)==0;
            if (!connectionClose)
            {
                headers.insert("Transfer-Encoding","chunked");
                chunkedMode=true;
            }
        }

        writeHeaders();
    }

    // Send data
    if (data.size()>0)
    {
        if (chunkedMode)
        {
            if (data.size()>0)
            {
                QByteArray size=QByteArray::number(data.size(),16);
                writeToSocket(size);
                writeToSocket("\r\n");
                writeToSocket(data);
                writeToSocket("\r\n");
            }
        }
        else
        {
            writeToSocket(data);
        }
    }

    // Only for the last chunk, send the terminating marker and flush the buffer.
    if (lastPart)
    {
        if (chunkedMode)
        {
            writeToSocket("0\r\n\r\n");
        }
        socket->flush();
        sentLastPart=true;
    }
}

bool HttpResponse::hasSentLastPart() const
{
    return sentLastPart;
}

void HttpResponse::redirect(const QByteArray& url)
{
    setStatus(303,"See Other");
    setHeader("Location",url);
    write("Redirect",true);
}

void HttpResponse::flush()
{
    socket->flush();
}

bool HttpResponse::isConnected() const
{
    return socket->isOpen();
}
/*
 *  this method makes the HTTP header for the response
 *  the headers job is to tell the caller the result of the request
 *  among if it was successful or not.
 *  200's are used for successful requests. 300's are for redirections. 400's
 *  are used if there was a problem with the request. 500's are used if there
 *  was a problem with the server.
 */
QByteArray HttpResponse::getStatus(int return_code)
{
	QString s;
	switch (return_code) {
		case 100:
			s = "100 Continue";
			break;
		case 101:
			s = "101 Switching Protocols";
			break;
		case 102:
			s = "102 Processing";
			break;
		case 200:
			s = "200 OK";
			break;
		case 201:
			s = "201 Created";
			break;
		case 202:
			s = "202 Accepted";
			break;
		case 203:
			s = "203 Non-Authoritative Information";
			break;
		case 204:
			s = "204 No Content";
			break;
		case 205:
			s = "205 Reset Content";
			break;
		case 206:
			s = "206 Partial Content";
			break;
		case 207:
			s = "207 Multi-Status";
			break;
		case 208:
			s = "208 Already Reported";
			break;
		case 226:
			s = "226 IM Used";
			break;
		case 300:
			s = "300 Multiple Choices";
			break;
		case 301:
			s = "301 Moved Permanently";
			break;
		case 302:
			s = "302 Found";
			break;
		case 303:
			s = "303 See Other";
			break;
		case 304:
			s = "304 Not Modified";
			break;
		case 305:
			s = "305 Use Proxy";
			break;
		case 307:
			s = "307 Temporary Redirect";
			break;
		case 308:
			s = "308 Permanent Redirect";
			break;
		case 400:
			s = "400 Bad Request";
			break;
		case 401:
			s = "401 Unauthorized";
			break;
		case 402:
			s = "402 Payment Required";
			break;
		case 403:
			s = "403 Forbidden";
			break;
		case 404:
			s = "404 Not Found";
			break;
		case 405:
			s = "405 Method Not Allowed";
			break;
		case 406:
			s = "406 Not Acceptable";
			break;
		case 407:
			s = "407 Proxy Authentication Required";
			break;
		case 408:
			s = "408 Request Timeout";
			break;
		case 409:
			s = "409 Conflict";
			break;
		case 410:
			s = "410 Gone";
			break;
		case 411:
			s = "411 Length Required";
			break;
		case 412:
			s = "412 Precondition Failed";
			break;
		case 413:
			s = "413 Payload Too Large";
			break;
		case 414:
			s = "414 URI Too Long";
			break;
		case 415:
			s = "415 Unsupported Media Type";
			break;
		case 416:
			s = "416 Range Not Satisfiable";
			break;
		case 417:
			s = "417 Expectation Failed";
			break;
		case 421:
			s = "421 Misdirected Request";
			break;
		case 422:
			s = "422 Unprocessable Entity";
			break;
		case 423:
			s = "423 Locked";
			break;
		case 424:
			s = "424 Failed Dependency";
			break;
		case 426:
			s = "426 Upgrade Required";
			break;
		case 428:
			s = "428 Precondition Required";
			break;
		case 429:
			s = "429 Too Many Requests";
			break;
		case 431:
			s = "431 Request Header Fields Too Large";
			break;
		case 451:
			s = "451 Unavailable For Legal Reasons";
			break;
		case 500:
			s = "500 Internal Server Error";
			break;
		case 501:
			s = "501 Not Implemented";
			break;
		case 502:
			s = "502 Bad Gateway";
			break;
		case 503:
			s = "503 Service Unavailable";
			break;
		case 504:
			s = "504 Gateway Timeout";
			break;
		case 505:
			s = "505 HTTP Version Not Supported";
			break;
		case 506:
			s = "506 Variant Also Negotiates";
			break;
		case 507:
			s = "507 Insufficient Storage";
			break;
		case 508:
			s = "508 Loop Detected";
			break;
		case 510:
			s = "510 Not Extended";
			break;
		case 511:
			s = "511 Network Authentication Required";
			break;
	}
	return s.toUtf8();
}

QByteArray HttpResponse::getContentType( int type )
{
	QString s;

	switch (type) {
		case 0:
			s = "text/xml;charset=utf-8";
			break;
		case 1:
			s = "text/html; charset=utf-8";
			break;
		case 2:
			s = "image/gif";
			break;
		case 3:
			s = "multipart/form-data; boundary=something";
			break;
		case 4:
			s = "application/x-zip-compressed";
			break;
			break;
		default:
			s = "text/plain";
			break;
	}

	return s.toUtf8();
}
