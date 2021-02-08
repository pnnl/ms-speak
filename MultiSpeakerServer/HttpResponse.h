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
// Summary: HttpResponse.h
//-------------------------------------------------------------------------------

#ifndef HTTPRESPONSE_H
#define HTTPRESPONSE_H

#include <QMap>
#include <QString>
#include <QTcpSocket>
//#include "HttpCookie.h"


/**
  This object represents a HTTP response, used to return something to the web client.
  <p>
  <code><pre>
    response.setStatus(200,"OK"); // optional, because this is the default
    response.writeBody("Hello");
    response.writeBody("World!",true);
  </pre></code>
  <p>
  Example how to return an error:
  <code><pre>
    response.setStatus(500,"server error");
    response.write("The request cannot be processed because the servers is broken",true);
  </pre></code>
  <p>
  In case of large responses (e.g. file downloads), a Content-Length header should be set
  before calling write(). Web Browsers use that information to display a progress bar.
*/

class HttpResponse { // DECLSPEC
    Q_DISABLE_COPY(HttpResponse)
public:

    /**
      Constructor.
      @param socket used to write the response
    */
    HttpResponse(QTcpSocket* socket);

    /**
      Set a HTTP response header.
      You must call this method before the first write().
      @param name name of the header
      @param value value of the header
    */
    void setHeader(QByteArray name, QByteArray value);

    /**
      Set a HTTP response header.
      You must call this method before the first write().
      @param name name of the header
      @param value value of the header
    */
    void setHeader(QByteArray name, int value);

    /** Get the map of HTTP response headers */
    QMap<QByteArray,QByteArray>& getHeaders();

	/** Get the map of cookies *
	QMap<QByteArray,HttpCookie>& getCookies();*/

	QByteArray getStatus(int return_code);
	QByteArray getContentType( int type );
	/**
      Set status code and description. The default is 200,OK.
      You must call this method before the first write().
    */
    void setStatus(int statusCode, QByteArray description=QByteArray());
	void setStatusFromCode(int return_code);
    /** Return the status code. */
    int getStatusCode() const;

    /**
      Write body data to the socket.
      <p>
      The HTTP status line, headers and cookies are sent automatically before the body.
      <p>
      If the response contains only a single chunk (indicated by lastPart=true),
      then a Content-Length header is automatically set.
      <p>
      Chunked mode is automatically selected if there is no Content-Length header
      and also no Connection:close header.
      @param data Data bytes of the body
      @param lastPart Indicates that this is the last chunk of data and flushes the output buffer.
    */
    void write(QByteArray data, bool lastPart=false);

    /**
      Indicates whether the body has been sent completely (write() has been called with lastPart=true).
    */
    bool hasSentLastPart() const;

    /**
      Set a cookie.
      You must call this method before the first write().

	void setCookie(const HttpCookie& cookie);*/

    /**
      Send a redirect response to the browser.
      Cannot be combined with write().
      @param url Destination URL
    */
    void redirect(const QByteArray& url);

    /**
     * Flush the output buffer (of the underlying socket).
     * You normally don't need to call this method because flush is
     * automatically called after HttpRequestHandler::service() returns.
     */
    void flush();

    /**
     * May be used to check whether the connection to the web client has been lost.
     * This might be useful to cancel the generation of large or slow responses.
     */
    bool isConnected() const;

private:

    /** Request headers */
    QMap<QByteArray,QByteArray> headers;

    /** Socket for writing output */
    QTcpSocket* socket;

    /** HTTP status code*/
    int statusCode;

    /** HTTP status code description */
    QByteArray statusText;

    /** Indicator whether headers have been sent */
    bool sentHeaders;

    /** Indicator whether the body has been sent completely */
    bool sentLastPart;

    /** Whether the response is sent in chunked mode */
    bool chunkedMode;

	/** Cookies
	QMap<QByteArray,HttpCookie> cookies; */

    /** Write raw data to the socket. This method blocks until all bytes have been passed to the TCP buffer */
    bool writeToSocket(QByteArray data);

    /**
      Write the response HTTP status and headers to the socket.
      Calling this method is optional, because writeBody() calls
      it automatically when required.
    */
    void writeHeaders();

};

#endif // HTTPRESPONSE_H
