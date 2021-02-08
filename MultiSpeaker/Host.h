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
// Summary: Host.h
//-------------------------------------------------------------------------------


#ifndef HOST_H
#define HOST_H

#include <QObject>

class Host : public QObject
{
	Q_OBJECT
public:
	enum AppFlagEnum {NoApp = 0, Apache = 0x1, FireFox = 0x2, Terminal = 0x4, WireShark = 0x8};

private:
	QString m_ReqhostAddress;
	QString m_ResphostAddress;
	int m_ReqhostPort;
	int m_ResphostPort;
	bool m_ReqhostEnable;
	bool m_ResphostEnable;
	bool m_enableSsl;
	bool m_useProxy;
	QString m_name;
	int m_id;
	int m_appFlags;

public:
	Host(int id=0, const QString& name="", int appFlags=AppFlagEnum(Apache), QObject* parent=Q_NULLPTR);
	Host(const Host& host);
	~Host();

	bool AppFlag(Host::AppFlagEnum appFlag) const {return (m_appFlags & appFlag);}
	int AppFlags() const {return m_appFlags;}
	void Copy(const Host& host);
	bool EnableSsl() const { return m_enableSsl; }
	bool UseProxy() const { return m_useProxy; }
	QString ReqHostAddress() const  { return m_ReqhostAddress; }
	QString RespHostAddress() const  { return m_ResphostAddress; }
	int ReqHostPort() const { return m_ReqhostPort; }
	int RespHostPort() const { return m_ResphostPort; }
	bool ReqHostEnable() const { return m_ReqhostEnable; }
	bool RespHostEnable() const { return m_ResphostEnable; }

	int Id() const {return m_id;}
	QString Name() const {return m_name;}

	void SetAppFlag(Host::AppFlagEnum appFlag) {m_appFlags |= appFlag;}
	void SetAppFlags(int flags) {m_appFlags = flags;}
	void SetEnableSsl(bool flag) { m_enableSsl = flag; }
	void SetUseProxy(bool flag) { m_useProxy = flag; }
	void SetReqHostAddress(const QString& address) { m_ReqhostAddress = address; }
	void SetRespHostAddress(const QString& address) { m_ResphostAddress = address; }
	void SetReqHostPort(int port) { m_ReqhostPort = port; }
	void SetRespHostPort(int port) { m_ResphostPort = port; }
	void SetReqHostEnable(bool flag) { m_ReqhostEnable = flag; }
	void SetRespHostEnable(bool flag) { m_ResphostEnable = flag; }
	void SetId(int id) {m_id = id;}
	void SetName(const QString& name) {m_name = name;}

};

#endif // HOST_H
