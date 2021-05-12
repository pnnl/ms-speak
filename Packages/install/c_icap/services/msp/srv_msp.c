/*-------------------------------------------------------------------------------

  Multi-Speak - Secure Protocol Enterprise Access Kit(MS_SPEAK)
  Copyright © 2021, Battelle Memorial Institute
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
/*
-------------------------------------------------------------------------------
	History
		03/23/2019 - inital modification from examples @ https://sourceforge.net/projects/c-icap/: Carl Miller <carl.miller@pnnl.gov>
		04/01/2019 - CHM: added logging.
		05/13/2019 - CHM: return MS response on business rule violation.
		06/04/2019 - CHM: generalize BizData (start to at least...).
		06/05/2019 - CHM: only increment m_NumValidRequests upon seeing a response.
		06/20/2019 - CHM: ingest the complete packet, so can parse the well-formed xml inside.
		06/29/2019 - CHM: support all methods/endpoints.
		04/05/2021 - CHM: support Phase3 enhancements.
		04/15/2021 - CHM: handle version 3 MS headers with no endpoint.
							see V3_NULL_ENDPOINT.
		04/25/2021 - CHM: add back channel commands:  i.e., browse to http://192.168.1.14:3128/icap?cmd=7&arg=11
							http://192.168.1.3:3128/icap?cmd=help
							http://127.0.0.1:3128/icap?cmd=1
		05/07/2021 - CHM: ensure use of just a single process so browser commands will work
						and weather thread global access works.
		In order for the browser commands and the weather thread updates to work properly,
		I had to limit the number of child processes that the main icap process forks: I
		set 'StartServers' and 'MaxServers' in c-icap.conf to 1.
		05/10/2021 - CHM: Support version 3 messages:
							v3 msg hdr does not contain the Endpoint
							v3 msg hdr does not contain caller information
-------------------------------------------------------------------------------
	NOTE:  the following build instructions apply to a linux debian 10 system

	to build squid:
		download the most recent nightly build of Squid from http://www.squid-cache.org/Versions/v4/
			i.e., squid-4.7-20190507-r2e17b0261.tar.gz to /home/msspeak/Packages and unpack it:
				cd /home/msspeak/Packages
				tar xzf squid-4.7-20190507-r2e17b0261.tar.gz
				for convenience, rename the squid-4.7-20190507-r2e17b0261 directory:
					mv squid-4.7-20190507-r2e17b0261 squid-4.7
		build:
			cd /home/msspeak/Packages/squid-4.7
			./configure		// note: this will generate Makefile from the existing Makefile.in
							//		 no need to run automake to generate the Makefile.in)
			make			// this will take about 20 minutes

			// before running make install, modify ./src/squid.conf.default as below
			// then run: and verify the changes are in /usr/local/squid/etc/squid.conf
			sudo make install

		modify squid configuration file (/usr/local/squid/etc/squid.conf) as follows:
				(or copy squid.conf from the msp sources as ./src/squid.conf.default)
			//// start of squid.conf changes ////////////////////////////////////////////////
			#
			# Enable and configure the ICAP client in Squid
			#
			icap_enable on
			icap_preview_enable on
			icap_preview_size 0
			icap_send_client_ip on
			icap_service service_msp_req reqmod_precache icap ://127.0.0.1:1344/msp
			icap_service service_msp_resp respmod_precache icap ://127.0.0.1:1344/msp

			# This directive specifies the location of Squid’s error message files.
			# If you want to customize the error messages, you should put them into a nondefault directory.
			# Otherwise, they may be overwritten if you run make install in the future
			# point to our MSP error files
			error_directory /home/msspeak/Packages/c_icap-0.5.5/services/msp/errors

			#
			# Define what the squid content adaptation layer class maps
			#
			adaptation_access service_msp_req allow all
			adaptation_access service_msp_resp allow all

			#
			#
			# adaptation_service_set class_msp service_msp_req service_msp_respmod
			#
			#
			# This is the traffic match ACL for ICAP.   It currently funnels everything to icap for inspection.
			# This should change to an ACL that matches multispeak traffic, if possible.  Otherwise, msp will
			# will have to perform all filtering work.
			#
			#adaptation_access class_msp allow all

			# Example rule allowing access from your local networks.
			# Adapt to list your (internal) IP networks from where browsing
			# should be allowed
			#acl localnet src 0.0.0.1-0.255.255.255	# RFC 1122 "this" network (LAN)
			#acl localnet src 10.0.0.0/8		# RFC 1918 local private network (LAN)
			#acl localnet src 100.64.0.0/10		# RFC 6598 shared address space (CGN)
			#acl localnet src 169.254.0.0/16 	# RFC 3927 link-local (directly plugged) machines
			#acl localnet src 192.168.0.0/16	# RFC 1918 local private network (LAN)
			#acl localnet src fc00::/7       	# RFC 4193 local private network range
			#acl localnet src fe80::/10      	# RFC 4291 link-local (directly plugged) machines
			acl localnet src 172.20.219.0/24	# RFC 1918 local private network (LAN)

			// add
			acl Safe_ports port 8080	# http

			# Squid normally listens to port 3128
			# http_port 3128 - set to listen for ipv4 only:
			http_port 0.0.0.0:3128
			//// end of squid.conf changes ////////////////////////////////////////////////
			
			NOTE: if you run automake, it will replace the Squid.conf file(/usr/local/squid/etc/squid.conf), so
			in that case, you need to replace it with a version that allows only IPV4 addresses and
			also sets port 8080 as a safeport, as above (that version is in the repo @../Multispeaker/Proxy/squid).
				
		to run Squid:
			// Before running squid, install c-icap as below

			sudo /usr/local/squid/sbin/squid -h		// to list all options

			sudo /usr/local/squid/sbin/squid -N -d 1
			if you see this error:
				logfileHandleWrite: daemon:/var/logs/access.log: error writing ((32) Broken pipe)
			add your user to the staff group:
				usermod -a -G staff username
				(then shutdown, restart)
			cd /usr/local
				sudo chmod 777 squid -R
		to reconfigure Squid on the fly:
			sudo /usr/local/squid/sbin/squid -k reconfigure

				
	to build c-icap:
		download c_icap-0.5.5 from http://c-icap.sourceforge.net/download.html
			i.e., c_icap-0.5.5.tar.gz to /home/msspeak/Packages and unpack it:
				cd /home/msspeak/Packages
				tar xzf c_icap-0.5.5.tar.gz

			cd /home/msspeak/Packages/c_icap-0.5.5
				add 'services/msp/Makefile' to the 'configure' script file 'ac_config_files' variable
				create directory under ./c_icap-0.5.5/services called 'msp' with the following files(from msp source) in it:
					sudo mkdir services/msp
					Makefile.am, Makefile.in, makefile.w32, srv_msp.c, srv_msp_body.c, srv_msp_body.h & srv_msp.def
				also copy the 'errors' folder from the msp source  there
			
				change the line in ./services/Makefile.am and /services/Makefile.in from
					SUBDIRS = echo ex-206 
						 to
					SUBDIRS = echo ex-206 msp
			
			create /usr/local/share/c_icap/templates/msp/en
				sudo mkdir /usr/local/share/c_icap/templates/msp
				sudo mkdir /usr/local/share/c_icap/templates/msp/en			
			copy MSP_RESPONSE from the msp sources to :
				sudo cp MSP_RESPONSE /usr/local/share/c_icap/templates/msp/en

			./configure		// note: this will generate Makefile from the existing Makefile.in
							//		 no need to run automake to generate the Makefile.in)
			make			// this will take a minute or 2

			// before running make install, modify ./c_icap-0.5.5/c-icap.conf.in as below
			// then run: and verify the changes are in /usr/local/etc/c-icap.conf
			sudo make install // generates /usr/local/etc/c-icap.conf from 'c-icap.conf.in'

			modify the following section in './c_icap-0.5.5/c-icap.conf.in':
				######################################################
				# External modules comming with core c-icap server
				#
				# Module: echo
				# Description:
				#	Simple test service
				# Example:
				#	Service echo srv_echo.so
				Service echo srv_echo.so		<== change this
				Service msp srv_msp.so  		<== to this				
				
			to verify c-icap configuration:
				these lines must be in /usr/local/etc/c-icap.conf:
				Service msp srv_msp.so
				TemplateDir /usr/local/share/c_icap/templates
				(NOTE: do not place a slash at the end)
					

			if you are only modifying srv_msp.c after initial install of icap, just do the follwing from /home/msspeak/Packages/c_icap-0.5.5:
				make
				sudo make install
						
			if adding a new source file to msp, add it to Makefile.am and 
				run
					automake (requies Makefile.am)
					./configure
				then do 
					make
					sudo make install
					
			NOTES:
				automake uses Makefile.am to generate Makefile.in
				./configure uses Makefile.in to generate Makefile


		to run Squid:
			sudo /usr/local/squid/sbin/squid -N -d 1
		to run c-icap:  ( http://c-icap.sourceforge.net/install.html )
			sudo /usr/local/bin/c-icap [ -N -D -d 1 ]
			NOTE: if you see this error:
				/usr/local/bin/c-icap: error while loading shared libraries: libicapapi.so.5: cannot open shared object file: No such file or directory
				do:
					sudo ldconfig
			
		NOTE:  if the icap machine is rebooted, the directories for the icap lock file will no longer exist, and must be recreated: you may see the following error when starting c-icap:
			Cannot open the pid file: /var/run/c-icap/c-icap.pid or c-icap.ctl
										or
			Error opening control socket No such file or directory: /var/run/c-icap/c-icap.ctl.							
		do:
			sudo mkdir /var/run/c-icap
		this happens because /var/run is a tmpfs filesystem, so it
		is emptied at each boot, to have this directory created after each
		boot, add a .conf file to /run/tmpfiles.d:
			/usr/lib/tmpfiles.d/c-icap.conf with the follow content:
				d /var/run/c-icap 0755 - - -

				NOTE: the icap daemon will create the actual lock file in the directory when started.
				
		test on a single machine using:
			NOTE:  I believe QT does not pass loopback requests to a proxy, so can use the following:
				http_proxy=127.0.0.1:3128
				export http_proxy

				/usr/local/bin/c-icap-client -i 127.0.0.1 -s msp -p 1344 -req use-any-url

							or

				wget --post-file=TestConnDiscReq.xml -S http://127.0.0.1:8080
					 --header="Content-Type: text/xml"
					 --header="SOAPAction: \"http://www.multispeak.org/V5.0/wsdl/CD_Server/InitiateConnectDisconnect\"" -O response.xml

	others packages that may need to be installed:
		sudo apt-get install libglib2.0-dev
		sudo apt-get install libxml2
		sudo apt-get install libxml2-dev
		sudo apt-get install uuid-dev
-----------------------------------------------------------------------------------------------*/
#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h> 
#include <stdarg.h>
#include <ctype.h>
#include <time.h>
#include <libxml/xmlmemory.h>
#include <libxml/parser.h>
#include <uuid/uuid.h> 
#include <sqlite3.h> 
#include <curl/curl.h>
#include <pthread.h>
#include <unistd.h>
//#include <sys/types.h> // for tmp files
//#include <errno.h>

#include "common.h"
#include "c-icap.h"
#include "service.h"
#include "header.h"
#include "body.h"
#include "simple_api.h"
#include "debug.h"
#include "txt_format.h"
#include "txtTemplate.h"
#include "srv_msp_body.h"

// defines
#define CI_MAXMSGIDLEN 256
#define CI_MAXTIMESTAMPLEN 256
#define CI_MAXAPPNAMELEN 256
#define CI_MAXCOMPANYLEN 256
#define CI_MAXMETHODLEN 256
#define CI_MAXENDPOINTLEN 256
#define CI_MAXNSLEN 256
#define CI_MAACTIDLEN 256
#define MSP_NO_STATUS   0
#define MSP_OK          1
#define MSP_BIZ_VIO		2 // business rule violation
#define MSP_ERROR		3
#define MAX_GROUPLEN 80
#define WILDCARD_STR "-1"
#define WILDCARD -1
#define LOG_URL_SIZE 256
#define LOW_BUFF 256
#define MAX_DB_NAMELEN  50
#define MAX_DB_ZIPLEN    5
#define DB_COLNAME_TESTER	"Tester"
#define DB_COLNAME_APPID	"AppId"
#define DB_COLNAME_ZIPCODE	"Zipcode"
#define DB_COLNAME_FUNCTION "Function"
#define DB_COLNAME_ENDPOINT "Endpoint"
#define DB_COLNAME_METHOD	"Method"
#define DB_COLNAME_MAXTEMP	"maxTemp"
#define DB_COLNAME_MINTEMP	"minTemp"
#define DB_COLNAME_MAXHOUR	"maxHour"
#define DB_COLNAME_MINHOUR	"minHour"
#define DB_COLNAME_NUMREQ	"numReq"
#define DB_COLNAME_NUMRPH	"numRPH"
#define DB_COLNAME_EMAIL	"email"
#define APIBUFFLEN     				250
#define WEATHER_UPDATE_INTERVAL     5   // minutes
#define DATABASE_NAME "/home/msspeak/BizRules.db"
#define V3_NULL_ENDPOINT "V3_Server"
#define STRBUFF_LEN 800
#define SQL_FROM_QUERY " FROM rules"\
		" INNER JOIN functions ON functions.id = rules.function"\
		" INNER JOIN endpoints ON endpoints.id = rules.endpoint"\
		" INNER JOIN methods ON methods.id = rules.method"\
		" INNER JOIN testers ON testers.id = rules.tester"\
		" WHERE( rules.Tester =(SELECT Tester FROM ActiveTester));"
#define LOGF_NAME "/var/log/srv_msp.log"
//#define TMPF_NAME "/tmp/myTmpFile-"
//#define TMPF_NAMELEN 21

// buffer to hold the temporary file name
//char gblNameBuff[32]; // not sure why length is 32 and not 21

// types
typedef enum bc_cmd{
	BCC_NO_CMD = 0,
	BCC_SHOW_DB,
	BCC_RELOAD_DB,
	BCC_SHOW_ACT,
	BCC_CURRENT_TEMP,
	BCC_CURRENT_HOUR,
	BCC_SET_CURRENT_TEMP,
	BCC_SET_CURRENT_HOUR,
	BCC_HELP		// keep this always as the last, for BccUsage
} USER_CMD;

/*  https://openweathermap.org/current
	<current>
	<city id="0" name="Richland">
		<coord lon="-119.288" lat="46.2522"/>
		<country>US</country>
		<timezone>-28800</timezone>
		<sun rise="2021-02-19T14:53:21" set="2021-02-20T01:28:51"/>
	</city>
	<temperature value="30.16" min="28.4" max="30.99" unit="fahrenheit"/>
	<feels_like value="21.83" unit="fahrenheit"/>
	<humidity value="93" unit="%"/>
	<pressure value="1021" unit="hPa"/>
	<wind>
		<speed value="7.58" unit="mph" name="Light breeze"/>
		<gusts/>
		<direction value="210" code="SSW" name="South-southwest"/>
	</wind>
	<clouds value="90" name="overcast clouds"/>
	<visibility value="10000"/>
	<precipitation mode="no"/>
	<weather number="804" value="overcast clouds" icon="04d"/>
	<lastupdate value="2021-02-19T17:45:04"/>
	</current>
*/
typedef struct _wd{
	int currentTemp;
	bool bSuccess;
	char city[APIBUFFLEN+1];
} WEATHER_DATA;

// strncpy() Warning: If there is no null byte among the first n bytes of src, 
//		the string placed in dest will not be null-terminated.
typedef struct _tester{
	char  m_Tester[MAX_DB_NAMELEN+1];
	char  m_AppId[MAX_DB_NAMELEN+1];
	char  m_Zipcode[MAX_DB_ZIPLEN+1];
	//int   m_FileDesc;
} TESTER_DATA;

typedef struct _bizrule{
	signed long m_numReq;
	signed long m_numRPH;
	signed long m_minTemp;
	signed long m_maxTemp;
	signed long m_minHour;
	signed long m_maxHour;
	signed long m_NumRequests;
	signed long m_NumRequestsPH;
	char  m_Function[MAX_DB_NAMELEN+1];
	char  m_EndPoint[MAX_DB_NAMELEN+1];
	char  m_Method[MAX_DB_NAMELEN+1];
	char  m_Email[MAX_DB_NAMELEN+1];
	time_t m_StartTime;
} BIZ_RULE;

// structs
/*
 * The srv_msp_data structure will store the data required to service an ICAP request.
 */
struct srv_msp_msg_info{
	char xmlnspace[CI_MAXNSLEN + 1];
	char method[CI_MAXMETHODLEN + 1];
	char endpoint[CI_MAXENDPOINTLEN + 1];
	char xactid[CI_MAACTIDLEN + 1];
	char appname[CI_MAXAPPNAMELEN + 1];
	char company[CI_MAXCOMPANYLEN + 1];
	//char msgid[CI_MAXMSGIDLEN + 1];
	//char timestamp[CI_MAXTIMESTAMPLEN + 
	bool bIsV3;
};

struct srv_msp_data{
	struct body_data body;
	struct srv_msp_msg_info msginfo;
	int64_t maxBodyData;
	int64_t expectedData;
	/*flag for marking the eof*/
	int  eof;
	int  isReqmod;
	bool bHasCommand;
	bool bHasArg;
	USER_CMD Command;
	int  CommandArg;
};

struct string{
    char *ptr;
    size_t len;
};

char ViolationMessage[300];
char str[STRBUFF_LEN];

//
// THIS IS LIKELY WHY USE OF 'globals' DOESN'T SEEM TO WORK: (i-cap.conf)
// # TAG: StartServers
//	# Format: StartServers number
//	# Description:
//	#       The initial number of server processes. Each server process
//	#       generates a number of threads, which serve the requests.
//	# Default:
//	#       StartServers 3
//
//	AND THIS:
//	# TAG: ThreadsPerChild
//	# Format:  ThreadsPerChild number
//	# Description:
//	#       The number of threads per child process.
//	# Default:
//	#       ThreadsPerChild     10
//

pid_t gblMainProc = 0;
pthread_t    gblWeatherThread;
TESTER_DATA  gblTesterStruct={};
TESTER_DATA *gblpTesterData=NULL;
BIZ_RULE	*gblpBizRules=NULL;
FILE *gblLogFile = NULL;
bool gblThreadRunning = false;
bool gblTempTestMode = false;
bool gblHourTestMode = false;
bool gblUsingTempRule = false;
bool gblNeedLoadActiveRules = true;
int gblNumBizRules=0;
int gblRowCnt=0;
int gblCurrentDay=-1;
int gblHourOfDay=-1;
int gblCurrentTemp = 0;
//int gblFileDesc = -1;
// Declaration of thread condition variable 
pthread_cond_t cond1 = PTHREAD_COND_INITIALIZER;
// declaring mutex 
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;

/*

ci_stat_uint64_inc(UC_CNT_REQUESTS, 1);
int UC_CNT_REQUESTS = -1;
UC_CNT_REQUESTS = ci_stat_entry_register("Requests processed", STAT_INT64_T,  "Service url_check");


 * ICAP defines three methods:
	REQMOD - for Request Modification
	RESPMOD - for Response Modification
	OPTIONS - used by the ICAP client to retrieve
				configuration information from the ICAP server.
				config file is @ ..\c_icap-0.5.5\c-icap.conf

	ICAP error codes that differ from their HTTP counterparts are:
	100 - Continue after ICAP Preview
	204 - No modifications needed

	ICAP REQMOD or RESPMOD requests sent by the ICAP client(i.e. Squid)
	to the ICAP server(srv_msp) may include a "preview". This feature
	allows an ICAP server to see the beginning of a transaction, then decide
	if it wants to opt-out of the transaction early instead of receiving the
	remainder of the request message.  ICAP servers SHOULD use the OPTIONS
	method to specify how many bytes of preview are needed for a particular
	ICAP application on a per-resource basis.

	After sending the preview, the ICAP client will wait for a response
	from the ICAP server. The response MUST be one of the following:
		- 204 No Content. The ICAP server does not want to (or can not)
		modify the ICAP client’s request. The ICAP client MUST treat this
		the same as if it had sent the entire message to the ICAP server
		and an identical message was returned.

		- ICAP reqmod or respmod response, depending what method was the
		original request.

		- 100 Continue. If the entire encapsulated HTTP body did not fit
		in the preview, the ICAP client MUST send the remainder of its
		ICAP message, starting from the first chunk after the preview. If
		the entire message fit in the preview (detected by the "EOF"
		symbol), then the ICAP server MUST NOT respond with 100 Continue.

	In REQMOD mode, the ICAP request MUST contain an encapsulated HTTP
	request. The headers and body (if any) MUST both be encapsulated.
	request.h
		#define CI_NO_STATUS   0
		#define CI_OK          1
		#define CI_NEEDS_MORE  2
		#define CI_ERROR       -1
		#define CI_EOF         -2
 */

/*
 * To implement a service, one needs to implement the member functions of this struct. These functions
 * will be called by c-icap as follows:
 *   - New request arrives for this service  ->  msp_init_request_data is called
 *   - The icap client sends preview data -> msp_preview_handler is called.
 *			If this function returns CI_MOD_ALLOW204 the ICAP transaction stops here.
 *			If this function returns CI_MOD_CONTINUE the ICAP client will send the rest of body data, if exists.
 *   - The client sends more data -> msp_io is called multiple times until the
 *			client has sent all the body data. The service can start sending data using this function to the client
 *			before all data has been received.
 *   - The client has sent all the data -> msp_end_of_data_handler is called.
 *   - The client waits to read the rest of data from c-icap ->  msp_io called multiple
 *			times until all the body data is sent to the client
 * 
 * 		debug as:  sudo c-icap -N -D -d 1
 *  echo -n "reconfigure" > /var/run/c-icap.ctl
		The above command will cause c-icap to reload configuration, re-initialize services and 
			modules and re-open log files
 */

void init_string(struct string *);
size_t writefunc(void *, size_t, size_t, struct string *);
int fmt_srv_msp_namespace(ci_request_t *, char *, int, const char *);
int fmt_srv_msp_msgid(ci_request_t *, char *, int, const char *);
int fmt_srv_msp_timestamp(ci_request_t *, char *, int, const char *);
int fmt_srv_msp_appname(ci_request_t *, char *, int, const char *);
int fmt_srv_msp_company(ci_request_t *, char *, int, const char *);
int fmt_srv_msp_method(ci_request_t *, char *, int, const char *);
int fmt_srv_msp_transactionid(ci_request_t *, char *, int, const char *);
struct ci_fmt_entry MspFmtTable [] ={
	{ "%MSNS", "Namespace", fmt_srv_msp_namespace },
	{ "%MSGID", "MessageID", fmt_srv_msp_msgid },
	{ "%MSTIME", "TimeStamp", fmt_srv_msp_timestamp},
	{ "%MSAPP", "AppName", fmt_srv_msp_appname},
	{ "%MSCMPY", "Company", fmt_srv_msp_company},
	{ "%MSMTHD", "Method", fmt_srv_msp_method },
	{ "%MSTXID", "XActID", fmt_srv_msp_transactionid },
   { NULL, NULL, NULL}
};

// curl -uri "http://130.20.141.136:8077/" -Method POST -Body "ICAP CMD"

/* Sequence of calls:
msp_init_service()
msp_post_init_service()
------ iterate
	msp_release_request_data()
	msp_init_request_data()
	msp_preview_handler()
	msp_io()
	msp_end_of_data_handler()
---------------
void msp_close_service();
*/
// module prototypes
void msp_close_service();
void *msp_init_request_data(ci_request_t *);
void msp_release_request_data(void *);
int msp_init_service(ci_service_xdata_t *, struct ci_server_conf *);
int msp_post_init_service(ci_service_xdata_t *, struct ci_server_conf *);
int msp_preview_handler(char *, int, ci_request_t *);
int msp_end_of_data_handler(ci_request_t *);
int msp_io(char *, int *, char *, int *, int, ci_request_t *);

CI_DECLARE_MOD_DATA ci_service_module_t service ={
	"msp",                         // mod_name: The service name
	"MultiSpeak Parser Service",   // mod_short_descr: Service short description
	ICAP_REQMOD | ICAP_RESPMOD,    // mod_type: service implements only and request modification
	msp_init_service,              // mod_init_service: function called when the service is loaded.
	msp_post_init_service, 		   // mod_post_init_service: function which is called after c-icap
								   // is initialized, but before it starts serving requests.
	msp_close_service,             // mod_close_service: Called when c-icap server shuts down.
	msp_init_request_data,         // mod_init_request_data: function called when a new request for this services arrives at the c-icap server.
	msp_release_request_data,      // mod_release_request_data: function which releases the service data.
	msp_preview_handler,     	   // mod_check_preview_handler: function which is used to preview the ICAP client request
	msp_end_of_data_handler,	   // mod_end_of_data_handler: function called when the icap client has sent all the data to the service
	msp_io,                        // mod_service_io: function called to read/send body data from/to icap client.
	NULL,						   // mod_conf_table: config table of the service
	NULL						   // mod_data: This field is not used. Set it to NULL.
};

// general prototypes
int handle_request_preview(BIZ_RULE *, char *, bool);
int handle_response_preview(BIZ_RULE *, bool);
void BccUsage(void);
void ShowDBRules( TESTER_DATA *, BIZ_RULE *, int, int );
void WriteLog(int, FILE *, const char *, ...);
void msp_dumphex(char *, int);
bool LoadActiveRules( char * );
static ci_membuf_t *generate_error_page(ci_request_t *);
static bool get_method_info(xmlNodePtr, struct srv_msp_msg_info *);
static bool get_caller_info(xmlNodePtr, struct srv_msp_msg_info *);
xmlNodePtr getChildNode(xmlNodePtr currnode, const xmlChar *elem);
BIZ_RULE *GetBusinessRecord(struct srv_msp_data *, int *);

// statics
static ci_off_t MaxBodyData = 4 * 1024 * 1024; // 4,194,304 (4M)
static int MSP_DATA_POOL = -1;

/*
typedef int (*sqlite3_callback)(
   void*  data     // Data provided in the 4th argument of sqlite3_exec(), i.e., gblpBizRules
   int    colcount // The number of columns in row 
   char** values   // An array of strings representing fields in the row 
   char** columns  // An array of strings representing column names 
);
	* If callback returns non-zero, the sqlite3_exec() routine returns 
	* SQLITE_ABORT without invoking the callback again and without running
	*  any subsequent SQL statements.
*/
static int callback(void *data, int colcount, char **values, char **columns ){
	int i;
	if( !data ){
		ci_debug_printf(0, "callback Sanity Failure: %s\n", "null data ptr");
		gblRowCnt = 0;
		return -1;
	}
	if( gblRowCnt < gblNumBizRules ){
		TESTER_DATA	*pTester=&gblTesterStruct;
		BIZ_RULE *pBizRecs = (BIZ_RULE *)data;
		BIZ_RULE *pBzd = &pBizRecs[gblRowCnt++];
		pBzd->m_NumRequests = 0;
		pBzd->m_NumRequestsPH = 0;
		for(i = 0; i<colcount; i++ ){
			if( !values[i] ){
				continue;
			}
			char *curr_key = columns[i];
			// Note, any non-existant keys will have already been preset to WILDCARD
			// strncmp is not necessary when comapring #defined strings
			if( !strcmp(curr_key, DB_COLNAME_NUMREQ) ){
				pBzd->m_numReq = atoll(values[i]);
			}
			else if( !strcmp(curr_key, DB_COLNAME_NUMRPH) ){
				pBzd->m_numRPH = atoll(values[i]);
				if( pBzd->m_numRPH == 0 ){ // special case in editor, 0 means not in use
					pBzd->m_numRPH = WILDCARD;
				}
			}
			else if( !strcmp(curr_key, DB_COLNAME_MINTEMP) ){
				pBzd->m_minTemp = atoll(values[i]);
			}
			else if( !strcmp(curr_key, DB_COLNAME_MAXTEMP) ){
				pBzd->m_maxTemp = atoll(values[i]);
				gblUsingTempRule = true;
			}
			else if( !strcmp(curr_key, DB_COLNAME_MINHOUR) ){
				pBzd->m_minHour = atoll(values[i]);
			}
			else if( !strcmp(curr_key, DB_COLNAME_MAXHOUR) ){
				pBzd->m_maxHour = atoll(values[i]);
			}
			else if( !strcmp(curr_key, DB_COLNAME_TESTER) ){
				if( gblRowCnt == 1 ){ // we only need store Tester name once
					strncpy( pTester->m_Tester, values[i], MAX_DB_NAMELEN );
				}
			}
			else if( !strcmp(curr_key, DB_COLNAME_APPID) ){
				if( gblRowCnt == 1 ){
					strncpy( pTester->m_AppId, values[i], MAX_DB_NAMELEN );
				}
			}
			else if( !strcmp(curr_key, DB_COLNAME_ZIPCODE) ){
				if( gblRowCnt == 1 ){
					strncpy( pTester->m_Zipcode, values[i], MAX_DB_ZIPLEN );
				}
			}
			else if( !strcmp(curr_key, DB_COLNAME_EMAIL) ){
				strncpy( pBzd->m_Email, values[i], MAX_DB_NAMELEN );
			}
			else if( !strcmp(curr_key, DB_COLNAME_FUNCTION) ){
				strncpy( pBzd->m_Function, values[i], MAX_DB_NAMELEN );
			}
			else if( !strcmp(curr_key, DB_COLNAME_ENDPOINT) ){
				strncpy( pBzd->m_EndPoint, values[i], MAX_DB_NAMELEN );
			}
			else if( !strcmp(curr_key, DB_COLNAME_METHOD) ){
				strncpy( pBzd->m_Method, values[i], MAX_DB_NAMELEN );
			}
			else{
				ci_debug_printf(0, "Key Lookup Sanity Failure: %s\n", curr_key);
			}
		}
	}
	else{
		ci_debug_printf(0, "Row Count Sanity Failure: %d\n", gblRowCnt);
	}
	return 0;
}

/*
 * GetTesterData - reads the business rules for the Active Tester from the DB
 */
TESTER_DATA *GetTesterData( char *pdbFile ){
	TESTER_DATA *pRetData=NULL;
	sqlite3 *db;
	char *zErrMsg = 0;
	int rc;
	char *sql;
	/* Open database */

	ci_debug_printf(4, "Opening database: %s\n", pdbFile);

	rc = sqlite3_open_v2(pdbFile, &db, SQLITE_OPEN_READONLY, NULL);  
	if( rc ){
		ci_debug_printf(0, "Can't open database: %s\n", sqlite3_errmsg(db));
		return(pRetData);
	} else{
		;//ci_debug_printf(0, "Opened database successfully\n");
	}

	sql = "SELECT Count(*)" SQL_FROM_QUERY;  // get coount of rules for active counter

	sqlite3_stmt *stmt;
	rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
	if( rc != SQLITE_OK ){
		ci_debug_printf(0, "PREPARE failed: %s\n", sqlite3_errmsg(db));
		ci_debug_printf(0, "QUERY: %s\n", sql);
		sqlite3_close(db);
		return(pRetData);
	}
	bool bOnce = false;
	while ((rc = sqlite3_step(stmt)) == SQLITE_ROW ){
		if( !bOnce ){
			gblNumBizRules = sqlite3_column_int(stmt, 0); // sqlite3_column_text
			//ci_debug_printf(0,"gblNumBizRules = %d\n", gblNumBizRules);
			bOnce = true;
		}
		else{
			ci_debug_printf(0, "SANITY FAILURE: %s\n", "mutliple rows for Count(*)");
			sqlite3_finalize(stmt);	
			sqlite3_close(db);
			return(pRetData);
		}
	}
	if( rc != SQLITE_DONE ){
		ci_debug_printf(0, "SELECT failed: %s\n", sqlite3_errmsg(db));
		sqlite3_finalize(stmt);	
		sqlite3_close(db);
		return(pRetData);
	}
	sqlite3_finalize(stmt);	

	if( gblNumBizRules == 0 ){
		ci_debug_printf(0, "DATABASE FAILURE: %s\n", "No Active Tester Rules Found");
		sqlite3_close(db);
		return(pRetData);
	}else{
		ci_debug_printf(2, "%d Active Tester Rules Found\n", gblNumBizRules);
	}

	size_t size = gblNumBizRules * sizeof(BIZ_RULE);
	gblpBizRules = (BIZ_RULE *)calloc(1,size);
	// assure all string buffs will be null-termed
	for( int i=0; i<gblNumBizRules; i++ ){
		gblpBizRules[i].m_numReq = WILDCARD; // preset for any missing fields in DB
		gblpBizRules[i].m_numRPH = WILDCARD;
		gblpBizRules[i].m_minTemp = WILDCARD;
		gblpBizRules[i].m_maxTemp = WILDCARD;
		gblpBizRules[i].m_minHour = WILDCARD;
		gblpBizRules[i].m_maxHour = WILDCARD;
	}

	/* Execute SQL statement 
	The fourth parameter of sqlite3_exec can be used to pass information to the callback.
	A pointer to a struct to fill would be useful.
	*/
	sql = "SELECT testers.Name as Tester, testers.AppId, testers.Zipcode, functions.Name as Function, endpoints.name as Endpoint, methods.name as Method,"
		"rules.maxTemp,rules.minTemp,rules.maxHour,rules.minHour,rules.numReq,rules.numRPH,rules.email"
		 SQL_FROM_QUERY;
	gblRowCnt = 0;
	rc = sqlite3_exec(db, sql, callback, (void*)gblpBizRules, &zErrMsg);
	if( rc != SQLITE_OK ){
		ci_debug_printf(0, "SQL error getting Active Rules: %s\n", zErrMsg);
		sqlite3_free(zErrMsg);
		free( gblpBizRules );
		sqlite3_close(db);
		return(pRetData);
	} else{
		;//ci_debug_printf(0, "Operation done successfully\n");
	}
	sqlite3_close(db);
	ci_debug_printf(4, "Closed Database: %s\n", pdbFile);

	if( gblRowCnt > gblNumBizRules ){
		ci_debug_printf(0, "SANITY FAILURE: %s\n", "excess rows for query");
		free( gblpBizRules );
	}
	else{
		if( gblTesterStruct.m_Tester ){ // should have been set in 'callback'
			pRetData = &gblTesterStruct;
			/*ci_debug_printf(3,"Tester: %s, AppId: %s, Zip: %s\n", pRetData->m_Tester, pRetData->m_AppId, pRetData-> m_Zipcode);
			BIZ_RULE *pBizRecs = gblpBizRules;
			for( int i=0; i<gblNumBizRules; i++ ){
				ci_debug_printf(3,"          Function: %s, Endpoint: %s, Method: %s\n",
					   pBizRecs->m_Function,pBizRecs->m_EndPoint,pBizRecs->m_Method);
				ci_debug_printf(3,"          numReq: %ld, numRPH: %ld, maxTemp: %ld, minTemp: %ld, maxHour: %ld, minHour: %ld\n",
					pBizRecs->m_numReq,pBizRecs->m_numRPH,pBizRecs->m_maxTemp,pBizRecs->m_minTemp,pBizRecs->m_maxHour,pBizRecs->m_minHour);
				ci_debug_printf(3,"          Email: %s\n\n",pBizRecs->m_Email);
				pBizRecs++;
			}*/
			ShowDBRules( pRetData, gblpBizRules, gblNumBizRules, 3 );
		}
		else{
			ci_debug_printf(0, "SANITY FAILURE: %s\n", "null gblTesterStruct.m_Tester");
			free( gblpBizRules );
			return(NULL);
		}
	}
	return pRetData;
}

void ShowDBRules( TESTER_DATA *pTester, BIZ_RULE *pRules, int NumRules, int dbgLvl )
{
	ci_debug_printf(dbgLvl,"Tester: %s, AppId: %s, Zip: %s\n", pTester->m_Tester, pTester->m_AppId, pTester-> m_Zipcode);
	for( int i=0; i<NumRules; i++ ){
		ci_debug_printf(dbgLvl,"          Function: %s, Endpoint: %s, Method: %s\n",
			   pRules->m_Function,pRules->m_EndPoint,pRules->m_Method);
		ci_debug_printf(dbgLvl,"          numReq: %ld, numRPH: %ld, maxTemp: %ld, minTemp: %ld, maxHour: %ld, minHour: %ld\n",
			pRules->m_numReq,pRules->m_numRPH,pRules->m_maxTemp,pRules->m_minTemp,pRules->m_maxHour,pRules->m_minHour);
		ci_debug_printf(dbgLvl,"          Email: %s\n\n",pRules->m_Email);
		pRules++;
	}
}
/*
 * init_string - initializer for weather update string struct
 */
void init_string(struct string *s ){
    s->len = 0;
    s->ptr = malloc(s->len+1);
    if( s->ptr == NULL ){
      ci_debug_printf(0, "in init_string(), malloc() failed\n");
      exit(EXIT_FAILURE);
    }
    s->ptr[0] = '\0';
}

/*
 * writefunc - curl handler for weather updates
 */
size_t writefunc(void *ptr, size_t size, size_t nmemb, struct string *s)
{
    size_t new_len = s->len + size*nmemb;
    s->ptr = realloc(s->ptr, new_len+1);
    if( s->ptr == NULL ){
      ci_debug_printf(0, "realloc() failed\n");
      exit(EXIT_FAILURE);
    }
    memcpy(s->ptr+s->len, ptr, size*nmemb);
    s->ptr[new_len] = '\0';
    s->len = new_len;

    return size*nmemb;
}

/*
 * parseNode
 * 		http://www.xmlsoft.org/tutorial/ar01s04.html
 */
xmlNodePtr parseNode (xmlNodePtr cur, const xmlChar *subchild)
{
	xmlNodePtr child = NULL;
    xmlNodePtr nxt = cur->xmlChildrenNode;
    while (nxt != NULL)
   {
        if( (!xmlStrcmp(nxt->name, subchild)))
       {
			child = nxt;
			break;
        }
        nxt = nxt->next;
    }
    return child;
}

/*
 * UpdateWeather - called by thread body for weather handler
 */
bool UpdateWeather( CURL *pCurl, struct string *pXmlStr, WEATHER_DATA *pWd )
{
    CURLcode res;

	pWd->currentTemp = -273;
	pWd->bSuccess = false;
	pWd->city[0]=0; // APIBUFFLEN+1];
	
	res = curl_easy_perform(pCurl);
	if( res != CURLE_OK ){
		fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
		return false;
	} else{
		xmlNodePtr cur;
		xmlDocPtr xmlDoc;
		xmlDoc = xmlParseMemory(pXmlStr->ptr, pXmlStr->len);
		if( xmlDoc == NULL ){
			printf("XML Document not parsed successfully.\n");
			return false;
		}
		cur = xmlDocGetRootElement(xmlDoc);
		if( cur == NULL ){
			printf("Failed to get XML ROOT\n");
			xmlFreeDoc(xmlDoc);
			return false;
		}
		cur = cur->xmlChildrenNode;
		//printf("\n\n");
#ifdef _GET_ALL_WEATHER_PARAMS_
		xmlNodePtr child;
		xmlChar   *key2;
		struct tm *info;
		struct tm  result;
		time_t 	   local;
#endif
		xmlChar *key;
		while (cur != NULL)
		{
			//printf("Current Name: '%s'\n", cur->name);
			if( (!xmlStrcmp(cur->name, (const xmlChar *)"temperature")) )
			{
				if( cur->xmlChildrenNode == NULL ){
					key = xmlGetProp(cur, (const xmlChar *)"value");
					pWd->currentTemp = (int) strtol((const char *)key, (char **)NULL, 10);
					pWd->bSuccess = true;
					xmlFree(key);
#ifdef _GET_ALL_WEATHER_PARAMS_					
					key = xmlGetProp(cur, (const xmlChar *)"min");
					printf("Min Temp: %s\n", key);
					xmlFree(key);
					key = xmlGetProp(cur, (const xmlChar *)"max");
					printf("Max Temp: %s\n", key);
					xmlFree(key);
					key = xmlGetProp(cur, (const xmlChar *)"unit");
					printf("Temp Units: %s\n", key);
					xmlFree(key);
#endif
				}	
			}
			else if( (!xmlStrcmp(cur->name, (const xmlChar *)"city")) ){
				key = xmlGetProp(cur, (const xmlChar *)"name");
				//printf("City: %s\n", key);
				strncpy(pWd->city, (const char *)key, APIBUFFLEN);
				xmlFree(key);
#ifdef _GET_ALL_WEATHER_PARAMS_
				key = (xmlChar *)"coord";
				child = parseNode( cur, key);
				if( child ){
					key = xmlGetProp(child, (const xmlChar *)"lat");
					printf("Lat: %s\n", key);
					xmlFree(key);
					key = xmlGetProp(child, (const xmlChar *)"lon");
					printf("Lon: %s\n", key);
					xmlFree(key);
				}
				else{
					printf("ERROR: Failed to locate '%s'\n", key );
				}
				key = (xmlChar *)"sun";
				child = parseNode( cur, key);
				if( child ){
					key = xmlGetProp(child, (const xmlChar *)"rise");
					if( strptime( (const char *)key, "%Y-%m-%dT%H:%M:%S",&result) == NULL)
						printf("\nstrptime failed\n");					
					else{
						local = timegm(&result);
						info = localtime( &local );
						//info->tm_hour+=tmz_off;
						printf("Sunrise: %d:%d:%d\n", info->tm_hour,info->tm_min,info->tm_sec );
					}
					xmlFree(key);
					key = xmlGetProp(child, (const xmlChar *)"set");
					if( strptime( (const char *)key, "%Y-%m-%dT%H:%M:%S",&result) == NULL)
						printf("\nstrptime failed\n");					
					else{
						local = timegm(&result);
						info = localtime( &local );
						//info->tm_hour+=tmz_off;
						printf("Sunset: %d:%d:%d\n", info->tm_hour,info->tm_min,info->tm_sec );
					}
					xmlFree(key);
				}
				else{
					printf("ERROR: Failed to locate '%s'\n", key );
				}
#endif // _GET_ALL_WEATHER_PARAMS_
			}
#ifdef _GET_ALL_WEATHER_PARAMS_
			else if( (!xmlStrcmp(cur->name, (const xmlChar *)"feels_like")) ){
				key = xmlGetProp(cur, (const xmlChar *)"value");
				printf("Feels like: %s\n", key);
				xmlFree(key);
			}				
			else if( (!xmlStrcmp(cur->name, (const xmlChar *)"humidity")) ){
				key = xmlGetProp(cur, (const xmlChar *)"value");
				printf("Humidity: %s%%\n", key);
				xmlFree(key);
			}				
			else if( (!xmlStrcmp(cur->name, (const xmlChar *)"lastupdate")) ){
				// 2021-02-20T18:44:07
				key = xmlGetProp(cur, (const xmlChar *)"value");
				if( strptime( (const char *)key, "%Y-%m-%dT%H:%M:%S",&result) == NULL)
					printf("\nstrptime failed\n");					
				else{
					//time_t local = timelocal(&result);
					local = timegm(&result);
					info = localtime( &local );
					//info->tm_hour+=tmz_off;
					//printf("Current local time and date: %s", asctime(info));
					printf("Last Update: %s\n", asctime(info));
				}
				xmlFree(key);
			}
			else if( (!xmlStrcmp(cur->name, (const xmlChar *)"wind")) ){
				key = (xmlChar *)"speed";
				child = parseNode( cur, key);
				if( child ){
					key = xmlGetProp(child, (const xmlChar *)"value");
					key2 = xmlGetProp(child, (const xmlChar *)"unit");
					printf("Wind Speed: %s %s\n", key, key2);
					xmlFree(key);
					xmlFree(key2);
					key = xmlGetProp(child, (const xmlChar *)"name");
					printf(" ( %s )\n", key);
					xmlFree(key);
				}
				else{
					printf("ERROR: Failed to locate '%s'\n", key );
				}
				//<direction value="210" code="SSW" name="South-southwest"/>
				key = (xmlChar *)"direction";
				child = parseNode( cur, key);
				if( child ){
					key = xmlGetProp(child, (const xmlChar *)"name");
					if( key ){
						key2 = xmlGetProp(child, (const xmlChar *)"value");
						printf("  direction: %s (%s degrees)\n", key, key2);
						xmlFree(key2);
					}
					xmlFree(key);
				}
				else{
					printf("ERROR: Failed to locate '%s'\n", key );
				}
				key = (xmlChar *)"gusts";
				child = parseNode( cur, key);
				if( child ){
					key = xmlGetProp(child, (const xmlChar *)"value");
					if( key ){
						printf("  gusts: %s\n", key);
						xmlFree(key);
					}
				}
				else{
					printf("ERROR: Failed to locate '%s'\n", key );
				}					
			}				
			else if( (!xmlStrcmp(cur->name, (const xmlChar *)"clouds")) ){
				key = xmlGetProp(cur, (const xmlChar *)"name");
				printf("%s\n", key);
				xmlFree(key);
			}
			//.mode Possible values are 'no", name of weather phenomena as 'rain', 'snow'				
			else if( (!xmlStrcmp(cur->name, (const xmlChar *)"precipitation")) ){
				key = xmlGetProp(cur, (const xmlChar *)"value");
				if( key ){
					key2 = xmlGetProp(cur, (const xmlChar *)"mode");
					printf("precipitation: %smm, %s\n", key,key2);
					xmlFree(key2);
				}
				else{
					printf("precipitation: %s\n", "none");
				}
				xmlFree(key);
			}
#endif // _GET_ALL_WEATHER_PARAMS_
			cur = cur->next;
		}			
		xmlFreeDoc(xmlDoc);
		free(pXmlStr->ptr);
	}
	return true;	
}
	
/*
 * WeatherUpdater - thread body for weather handler
 * 		as the icap module is a library module, threads created by it apparently can not share the values
 *		of any globals defined in this file...
 */
void *WeatherUpdater(void *data)
{
	if( data )
	{
		TESTER_DATA *pData = data;
		CURL *curl;
		const static char *api_endpoint = "http://api.openweathermap.org/data/2.5/weather?appid=%s&zip=%s&units=imperial&mode=xml";
		char api_buffer[APIBUFFLEN+1];
		//unsigned seconds = WEATHER_UPDATE_INTERVAL * 60;
		unsigned seconds = WEATHER_UPDATE_INTERVAL * 18;
		bool init = true;

		curl = curl_easy_init();
		ci_debug_printf(1, "\n*** Weather Updater started ***\n");
		if( curl)
		{
			WEATHER_DATA weatherData;
			struct string xmlStr;
			init_string(&xmlStr);
			snprintf(api_buffer, APIBUFFLEN, api_endpoint, pData->m_AppId, pData->m_Zipcode );
			curl_easy_setopt(curl, CURLOPT_URL, api_buffer);
			curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, writefunc);
			curl_easy_setopt(curl, CURLOPT_WRITEDATA, &xmlStr);
			curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0); // Verify the SSL certificate, 0 (zero) means it doesn't.

			ci_debug_printf(1,"\n Getting Weather for area %s\n", pData->m_Zipcode);
			ci_debug_printf(1,"      using AppID: %s\n", pData->m_AppId);
			do{
				if( gblTempTestMode ){
					ci_debug_printf(1,"\nSimulating Temperature of %d While in Test Mode.\n",gblCurrentTemp);
				}
				else{
#ifdef _SHOW_PIDS_
					pid_t pid = getpid();
					ci_debug_printf(3, "\n*** WeatherUpdater pid: %d.\n",pid);
#endif
					if( UpdateWeather( curl, &xmlStr, &weatherData ) ){
						if( weatherData.bSuccess ){
							gblCurrentTemp = weatherData.currentTemp;
							ci_debug_printf(2,"\nCurrent Temperature: %d\n", gblCurrentTemp);
							/*errno = 0;
							// rewind the stream pointer to the start of temporary file
							if( -1 == lseek(pData->m_FileDesc,0,SEEK_SET))
							{
								ci_debug_printf(0,"\nERROR lseek failed on weather file with error [%s]\n",strerror(errno));
							}
							else{// Write some data to the temporary file
								if( -1 == write(pData->m_FileDesc, &CurrentTemp, sizeof(int)) )
								{
									ci_debug_printf(0,"\n write of CurrentTemp failed with error [%s]\n",strerror(errno));
								}
								else{
									ci_debug_printf(4,"\n CurrentTemp written to temporary file\n");
								}
							}*/
						}
						else{
							ci_debug_printf(0,"\nERROR Updating Weather, No Temperature.\n");
						}
						if( weatherData.city ){
							ci_debug_printf(2,"City: %s\n", weatherData.city);
						}
						else{
							ci_debug_printf(0,"\nERROR Updating Weather, No City.\n");
						}
						//if( bShowAll ){
						//	ci_debug_printf(0,"\n%s\n\n",xmlStr.ptr);
						//}
					}
					else{
						ci_debug_printf(0,"\nERROR Updating Weather.\n");
						break;
					}
					ci_debug_printf(3, "*** Weather Updated ***\n");
					init_string(&xmlStr);
				} // not gblTempTestMode
				if (init) {
					pthread_mutex_lock(&lock); // acquire lock 
					gblThreadRunning = true;
					pthread_cond_signal(&cond1);
					pthread_mutex_unlock(&lock);// release lock
					init = false;
				}

				sleep( seconds );
			} while( true );
			curl_easy_cleanup(curl); 
		}
	}
	else{
		ci_debug_printf(1, "\n*** WeatherUpdater:: NULL data passed.\n");
	}
	// pthread_exit can cause 5 blocks allocated from functions called by pthread_exit() 
	// that is unfreed but still reachable at process exit
	//pthread_exit(NULL);
	ci_debug_printf(1, "\n*** WeatherUpdater exiting...\n");
	gblThreadRunning = false;
	return(NULL);
}

bool LoadActiveRules( char *pDatabaseName ){
	bool bRetVal = false;

	gblUsingTempRule = false;
	if( gblpTesterData ){ // previously loaded a DB?
		if( gblThreadRunning ){
			pthread_cancel(gblWeatherThread);
			pthread_join(gblWeatherThread, NULL);
			ci_debug_printf(3, "\n*** previous weather thread cancelled ***\n");
			gblThreadRunning = false;
		}
	}
	ci_debug_printf(3, "    Loading Business Rules from '%s'\n", pDatabaseName);
	gblpTesterData = GetTesterData( pDatabaseName ); //  sets gblUsingTempRule
	if( gblpTesterData )
	{
		bRetVal = true;
		ci_debug_printf(2, "    Successfully Loaded Business Rules.\n");
		ci_debug_printf(1, "\nActive Tester: '%s'\n\n", gblpTesterData->m_Tester);
		//if( CI_DEBUG_LEVEL >= 1 ){
		//	ci_debug_printf(3,"  %s\n", "TBD: Dump database\n");
		//}
		if( gblUsingTempRule != (gblpTesterData->m_AppId != NULL) ){
			if( gblUsingTempRule ){
				ci_debug_printf(0, "\n *** WARNING: TEMPERATURE RULE(s) ARE DEFINED, BUT NO REAL-TIME WEATHER UPDATE APPLICATION ID WAS PROVIDED. ***\n");
				gblTempTestMode = true;
				gblCurrentTemp = 50;
			}
			else{
				ci_debug_printf(0, "\n *** WARNING: NO TEMPERATURE RULE(s) ARE DEFINED, REAL-TIME WEATHER UPDATES WILL BE DISABLED. ***\n");
			}
		}
		else if( gblUsingTempRule ){ // also, m_AppId must not be NULL
			ci_debug_printf(4, "\n *** WAITING FOR WEATHER UPDATE APPLICATION TO START ***\n");
			// Create weather update thread, must be called after GetTesterData
			pthread_create(&gblWeatherThread, NULL, WeatherUpdater, gblpTesterData);
			//wait for WeatherUpdater to start
			/* pthread_cond_wait should be called with mutex locked by the
			* calling thread or undefined behaviour may result. Also, use the
			* shared boolean predicate 'gblNewSVMsg' since spurious wakeups
			* from the pthread_cond_wait() function may occur.
			*/
			pthread_mutex_lock(&lock);
			while (!gblThreadRunning) {
				pthread_cond_wait(&cond1, &lock);
			}
			pthread_mutex_unlock(&lock);
			ci_debug_printf(4, "\n *** WEATHER UPDATE APPLICATION STARTED ***\n");
		}
	}
	else{
		ci_debug_printf(0, "\n    Error loading Business Rules - NO RULES ARE IN EFFECT !\n\n");
	}
	gblNeedLoadActiveRules = false; // indicates we at least tried to load them.
	return bRetVal;
}

/*
 * This function called exactly when the service is loaded by c-icap.
 * Can be used to initialize the service.
	 param srv_xdata  - Pointer to the ci_service_xdata_t object of this service
	 param server_conf- Pointer to the struct holds the main c-icap server configuration
	 return CI_OK on success, CI_ERROR on any error. 
	 
	 CI_DEBUG_LEVEL can be set the "-d" param on the cmdline:
			sudo /usr/local/bin/c-icap -N -D -d 1
		lower values print less than higher
		
       reconfigure
              The service will reread the config file without the need to stop and restart the c-
              icap server. The services will be reinitialized
	Examples:
		To reconfigure c-icap:
			echo -n "reconfigure" > /var/run/c-icap.ctl		
		
 */
int msp_init_service(ci_service_xdata_t * srv_xdata,
					struct ci_server_conf *server_conf)
{
	//sleep(1);
	ci_debug_printf(0, "\n*** Initializing msp module v3.1 ***\n");
	 gblMainProc = getpid();
#ifdef _SHOW_PIDS_
	ci_debug_printf(3, "msp_init_service pid: %d.\n", gblMainProc);
#endif
	// Tell to the icap clients that we can support up to 2K size of preview data
	ci_service_set_preview(srv_xdata, 2048);

	unsigned int xops = CI_XCLIENTIP | CI_XSERVERIP;
	ci_service_set_xopts(srv_xdata, xops);// added from url_check

	/*Tell to the icap clients that we support 204 responses*/
	ci_service_enable_204(srv_xdata);
	/*Tell to the icap clients that we support 206 responses, added from url_check*/
	ci_service_enable_206(srv_xdata);

	/*initialize mempools          */
	MSP_DATA_POOL = ci_object_pool_register("srv_msp_data", sizeof(struct srv_msp_data));
	if( MSP_DATA_POOL < 0)
		return CI_ERROR;

	/*Tell to the icap clients to send preview data for all files*/
	// comment out for url_check ci_service_set_transfer_preview(srv_xdata, "*"); // "zip, tar"
	//ci_debug_printf(1, "Instantiating Business Rules Key File\n");
	
	return CI_OK;
}

/*
 * This function can be used to initialize the service. Unlike msp_init_service
 * when this function is called the c-icap has been initialized and it knows of
 * other system parameters like the services and modules which are loaded,
 * network ports and addresses c-icap is listening etc.
	 param srv_xdata   - Pointer to the ci_service_xadata_t object of this service
	 param server_conf - Pointer to the struct holds the main c-icap server configuration
	 return CI_OK on success, CI_ERROR on any error. 

	 the 'c-icap' process (i.e., 'aserver.c::main()') first calls
		msp_init_service then msp_post_init_service and then forks at least one child process (up to 
		CI_CONF.START_SERVERS) to handle http(s) requests.  Each child process is initialized
		with the same pc(program counter), same CPU registers, same open files which were in use by
		the parent process when it called fork(). Therefore whatever datastructs and files we want to share
		between all the child processes, needed to be created before the parent calls fork(), i.e, they
		need to be created in either msp_init_service or msp_post_init_service.
	
	 *** NOTE:  in order to be able to properly control the msp module using http commands (../icap?cmd=x),
			I needed to limit the number of child processes created to just 1, otherwise these commands would
			only affect whichever process happened to service the request.  Also, Threads are not inherited from a child process on a linux system using fork(), so the WeatherThread created in msp_post_init_service only
			exists in the parent process, not in any of the child processes.  Therefore, it should actually only
			be created in the child process.

 */
int msp_post_init_service(ci_service_xdata_t * srv_xdata, struct ci_server_conf *server_conf)
{
	ci_debug_printf(4, "\n*** msp_post_init_service:: ***\n");
	// NOTE:  this routine is called by the parent process, the others by child process(es)...

	BccUsage();

#ifdef _SHOW_PIDS_
	pid_t pid = getpid();
	ci_debug_printf(3, "msp_post_init_service (Parent)pid: %d.\n",pid);
#endif

	gblLogFile = fopen(LOGF_NAME, "a");
	if( gblLogFile == NULL )
	{
		ci_debug_printf(0, "    Log File (%s) Could not be opened.\n", LOGF_NAME);
		exit( -2 );
	}
	gblThreadRunning = false;
	/* setup a temporary file for holding weather data
	strncpy(gblNameBuff, TMPF_NAME, TMPF_NAMELEN);
	errno = 0;
	// Create the temporary file, this function will replace the 'X's
	gblFileDesc = mkstemp(gblNameBuff);
	// Call unlink so that whenever the file is closed or the program exits
	// the temporary file is deleted
	unlink(gblNameBuff);
	if( gblFileDesc < 1 )
	{
		ci_debug_printf(0, "\n Creation of temp file failed with error [%s]\n",strerror(errno));
		exit( -2 );
	}
	else
	{
		ci_debug_printf(3, "\n Temporary file [%s] created\n", gblNameBuff);
	}
	errno = 0;
	*/
	
	/* the main, 'parent' process does not need to have the DB, just its child processes
	if( !LoadActiveRules( DATABASE_NAME ) ){ //  sets gblpTesterData
		ci_debug_printf(0, "\n    Error loading Business Rules\n");
		//exit( -2 );
	}*/
	time_t currtime = time(NULL);
	struct tm *tm_struct = localtime(&currtime);
	ci_debug_printf(1, "    Current local time: %s", asctime(tm_struct));
	ci_debug_printf(3, "\n*** Waiting for Initial Request... ***\n");

	return CI_OK;
}

/*
	This function should inititalize the data and structures required for serving the request.
	param req - a pointer to the related ci_request_t structure
	returns   - a void pointer to the user defined data required for serving the request.
	The developer can obtain the service data from the related ci_request_t object using the
	macro ci_service_data.
	called when a new request for this services arrives at the c-icap server.
*/
void *msp_init_request_data(ci_request_t * req) // first call
{
	ci_debug_printf(4, "\n*** msp_init_request_data:: ***\n");

	if( gblNeedLoadActiveRules ){ // doing this here, loads them for each child process, but more 
	// importantly, the weatherthread will be created in the child process context, allowing it to
	// share the global variable 'gblCurrentTemp'.
		if( !LoadActiveRules( DATABASE_NAME ) ){ //  sets gblpTesterData
			ci_debug_printf(0, "\n    Error loading Business Rules\n");
			//exit( -2 );
		}
	}
	struct srv_msp_data *mspd = ci_object_pool_alloc(MSP_DATA_POOL);
	memset(&mspd->body, 0, sizeof(struct body_data));
	memset(&mspd->msginfo, 0, sizeof(struct srv_msp_msg_info));
	mspd->isReqmod = 0;
	mspd->maxBodyData = 0;
	mspd->expectedData = 0;
	mspd->eof = 0;
	mspd->bHasCommand = false;
	mspd->bHasArg = false;
	mspd->Command = BCC_NO_CMD;	
	return mspd;      /*Get from a pool of pre-allocated structs better...... */
}

/*
* This function called after the user request served to release the service data
*	 param data - pointer to the service data returned by msp_init_request_data
*/
void msp_release_request_data(void *data)
{
	ci_debug_printf(4, "\n*** msp_release_request_data:: ***\n");
	/*The data points to the echo_req_data struct we allocated in function echo_init_service */
	struct srv_msp_data *mspd = data;
	if( mspd->body.type ){
		body_data_destroy(&mspd->body);
	}
	ci_object_pool_free(mspd);    /*Return object to pool..... */

}

/*
 * If the client supports preview, sends some data for examination.
 * The service using this function will decide if the client request must be processed so the client
 * must send more data or no modification/processing needed so the request ends here.
		 param preview_data - Pointer to the preview data
		 param preview_data_len - The size of the preview data
		 param req - pointer to the related ci_request struct
		 returns   - CI_MOD_CONTINUE if the client must send more data, CI_MOD_ALLOW204
  		if the service does not want to modify anything, or CI_ERROR on errors.
 *
 * For example, to effect a Preview consisting of only encapsulated HTTP
 * headers, the ICAP client would add the following header to the ICAP
 * request:
 *		Preview: 0
 *
 * This indicates that the ICAP client will send only the encapsulated
 * header sections to the ICAP server, then it will send a zero-length
 * chunk and stop and wait for a "go ahead" to send more encapsulated
 * body bytes to the ICAP server.
 *
 * icap_preview_size setting in squid.conf:
 *		Default: icap_preview_size -1
 *		icap_preview_size sets the default preview size to be used. -1 means no preview.
	 #define CI_MOD_NOT_READY  0
	 #define CI_MOD_DONE       1
	 #define CI_MOD_CONTINUE 100
	 #define CI_MOD_ALLOW204 204
	 #define CI_MOD_ALLOW206 206
	 #define CI_MOD_ERROR     -1
	 206 (Partial Content) responses is an ICAP extension that allows the
	ICAP agents to optionally combine adapted and original HTTP message
	content.
	 back channel commands:  browse to http://192.168.1.14:3128/icap?2
 */
int msp_preview_handler(char *preview_data, int preview_data_len, ci_request_t * req)
{
	int showHeader = 0;
	ci_off_t content_len;
	ci_headers_list_t *pHeader = NULL;
	struct srv_msp_data *mspd = NULL;

	//ci_debug_printf(0, "\n*** msp_preview_handler::preview_data_len: %d  ***\n", preview_data_len);
	//ci_debug_printf(3, "\n*** msp_preview_handler:: ***\n");
	// TODO: each thread would handle a different connection, needs its own BIZ_RULE struct ...

	//return CI_MOD_CONTINUE;
	// If there is no body data in HTTP encapsulated object but only headers
	//	 respond with Allow204 (no modification required) and terminate the ICAP transaction here
	if( !ci_req_hasbody(req) ){
		ci_debug_printf(4, "msp_preview_handler::no body data.\n");
		pHeader = ci_http_request_headers(req);
		if( !pHeader ){
			ci_debug_printf(0, "msp_preview_handler::ERROR: unable to get http header\n");
			unlock_data(req);// this appears to prevent the browser cache having to be cleared each time
			return CI_ERROR; 
		}
		//ci_debug_printf(0, "msp_preview_handler: NO BODY:\n");
		const char *referer = ci_headers_value(pHeader, "Referer"); // : http://192.168.1.14:3128/icap?cmd=2 [&arg=]
		if( !referer ){
			ci_debug_printf(0, "msp_preview_handler::no referer in header\n");
			unlock_data(req);
			return CI_ERROR;
		}
		ci_debug_printf(4, "Referer: %s.\n", referer);
		char const *needle = "icap?cmd=";
		size_t needle_length = strlen(needle);
		char const *needle_pos = strstr(referer, needle);
		// not found, at end of referer:
		if( !needle_pos || !needle_pos[needle_length] )
		{
			ci_debug_printf(1, "Command not found from \"%s\".\n\n", needle);
			unlock_data(req);
			return CI_ERROR; // actually, still has to be done if return CI_MOD_DONE
		}
		// extract the word following the word at needle_pos:
		//char buf[1000];
		//size_t len = ci_headers_pack_to_buffer(pHeader, buf, 1000);
		//msp_dumphex(buf, len);
		//ci_debug_printf(4, "needle_pos: %s, needle_length: %d.\n", needle_pos, needle_length);
		int cmd;
		const char *cmdstr = needle_pos + needle_length;
		if( !strncasecmp(cmdstr, "help", 4) ){
			cmd = BCC_HELP;
		}
		else{
			cmd = atoi(cmdstr);
		}
		//ci_debug_printf(4, "cmdstr: %s.\n", cmdstr);
		//ci_debug_printf(3, "Command Received: %d.\n", cmd);
		mspd = ci_service_data(req);
		mspd->bHasCommand = true;
		mspd->bHasArg = false;
		mspd->Command = cmd;
		if( (cmd == BCC_SET_CURRENT_TEMP) || (cmd == BCC_SET_CURRENT_HOUR) ){
			// check to see if an arg also passed in
			//	http://192.168.1.14:3128/icap?cmd=2&arg=22 
			// &arg=22 
			needle = "&arg=";
			needle_length = strlen(needle);
			needle_pos = strstr(referer, needle);
			// not found, at end of referer:
			if( !needle_pos || !needle_pos[needle_length] )
			{
				if( !needle_pos ){
					ci_debug_printf(4, "NO COMMAND ARGUMENT PROVIDED.\n");
				}
				else{
					ci_debug_printf(1, "Command Argument not found from \"%s\".\n\n", needle);
				}
				//unlock_data(req);
				//return CI_ERROR; // actually, still has to be done if return CI_MOD_DONE
			}
			else{
				cmdstr = needle_pos + needle_length;
				int cmdarg = atoi(cmdstr);
				ci_debug_printf(4, "COMMAND ARGUMENT PROVIDED: %d.\n", cmdarg);
				mspd->bHasArg = true;
				mspd->CommandArg = cmdarg;
			}
		}
		else{
			mspd->bHasArg = false;
		}
		return CI_MOD_CONTINUE;
	}

	mspd = ci_service_data(req);
	mspd->maxBodyData = MaxBodyData;
	mspd->isReqmod = 0;
	mspd->bHasCommand = false;
	mspd->bHasArg = false;
	mspd->Command = BCC_NO_CMD;
	/*
		from the wake forest pcap data (MS v3) this is what the Post Header contains:
			POST /omsservices/services/OA_ServerSoap HTTP/1.0
			Content-Type: text/xml; charset=utf-8
			SOAPAction: "http://www.multispeak.org/Version_3.0/PingURL"
			...
		but the response does not have the SOAPAction:
			HTTP/1.1 200 OK
			Content-Type: text/xml;charset=utf-8

		so, we can't rely on the http header information to extract the endpoint & method, need to 
		read the whole message (not just preview data) and parse the whole, well-formed xml.
	*/

	// Extract the HTTP header from the request/response
	const int REQ_TYPE = ci_req_type(req);
	if( REQ_TYPE == ICAP_REQMOD ){	// Assure there is a soap action (required for soap requests according to according to https://www.w3.org/TR/2000/NOTE-SOAP-20000508 )
		mspd->isReqmod = 1;
		pHeader = ci_http_request_headers(req);
	}
	else{
		pHeader = ci_http_response_headers(req);
	}
	if( !pHeader ){
		ci_debug_printf(0, "msp_preview_handler::ERROR: unable to get http header\n");
		return CI_ERROR; 
	}

	if( REQ_TYPE == ICAP_REQMOD ){	// Assure there is a soap action (required for soap requests according to according to https://www.w3.org/TR/2000/NOTE-SOAP-20000508 )
		/*
		what Multispeaker sends is:
		POST / HTTP/1.1
		SOAPAction: http://www.multispeak.org/V5.0/wsdl/CD_Server/InitiateConnectDisconnect
		but what is in (one of) the wsdl is:
		soapAction="http://www.multispeak.org/Version_5.0_Release/InitiateConnectDisconnect"

		It appears that using the SoapAction is NOT a reliable way to extract the Endpoint and Method,
		so we now don't use the preview data, but wait to get the full packet and then parse the well-formed
		xml data to extract this info....

		Also, i DON'T think it is a requirement that the response contain a SoapAction....

		const char *soap_action;
		if( !(soap_action = ci_headers_value(pHeader, "SOAPAction"))) // uses strncasecmp, ignores case....
		{
			ci_debug_printf(0, "ERROR Getting Soap Action.\n");
			return CI_ERROR; // must not be a Multispeak Request
		}
		*/
		;
	}
	else{
		if( showHeader ){
			char buf[1000];
			size_t len = ci_headers_pack_to_buffer(pHeader, buf, 1000);
			ci_debug_printf(0, "msp_preview_handler:RESP HTTP HEADER:\n");
			msp_dumphex(buf, len);
		}
	}

	// If the content type is not xml do not process 
	/*
	const char *content_type = ci_http_response_get_header(req, "Content-Type");
	if( !content_type && REQ_TYPE == ICAP_REQMOD )
		content_type = ci_http_request_get_header(req, "Content-Type");
	*/
	const char *content_type = ci_headers_value(pHeader, "Content-Type");
	if( !content_type ){
		ci_debug_printf(0, "msp_preview_handler::no content type in header\n");
		return CI_ERROR; // TODO: should we throw an error or allow?
	}
	if( strstr(content_type, "text/xml") == NULL ){
		ci_debug_printf(0, "msp_preview_handler content type %s will not be processed...\n", content_type);
		return CI_ERROR; // TODO: should we throw an error or allow?
	}
	
	// If there is a Content-Length header, check it since we do not want to
	//		process body data with more than MaxBodyData size
	content_len = ci_http_content_length(req);
	ci_debug_printf(4, "msp_preview_handler::expected length: %"PRINTF_OFF_T"\n", (CAST_OFF_T)content_len);
	mspd->expectedData = content_len;

	/*If we do not have content len, for simplicity do not proccess it*/
	if( content_len <= 0 ){
		ci_debug_printf(0, "msp_preview_handler::no Content-Length, will not process\n");
		return CI_ERROR;
	}

	if( content_len > mspd->maxBodyData ){
		ci_debug_printf(0, "msp_preview_handler::content-length=%"PRINTF_OFF_T" > %ld will not process\n", (CAST_OFF_T)content_len, mspd->maxBodyData);
		return CI_ERROR;
	}

	body_data_init(&mspd->body, MEMORY, content_len, NULL);

	/*if we have preview data and we want to proceed with the request processing
	  we should store the preview data. There are cases where all the body
	  data of the encapsulated HTTP object is included in preview data.
	  Use the ci_req_hasalldata macro to identify these cases.
	*/
	if( preview_data_len ){
		ci_debug_printf(0, "msp_preview_handler::preview_data_len\n");
		
		body_data_write(&mspd->body, preview_data, preview_data_len, ci_req_hasalldata(req));
		mspd->eof = ci_req_hasalldata(req);
	}

	return CI_MOD_CONTINUE;
}

/*
* This function will be called when the service shutdown
* can be used to release service allocated resources
*/
void msp_close_service()
{
	ci_debug_printf(5, "\n*** msp_close_service::\n");
	if( gblThreadRunning ){
		pthread_cancel(gblWeatherThread);
		pthread_join(gblWeatherThread, NULL);
		ci_debug_printf(1, "\n*** weather thread joined ***\n");
		gblThreadRunning = false;
	}
	if( gblLogFile ){
		if( getpid() == gblMainProc ){
			WriteLog(0, gblLogFile, "The MSP Service Process is Shutting Down...");
		}
		fclose(gblLogFile);
	}
	ci_object_pool_unregister(MSP_DATA_POOL); // per url_check
	free(gblpBizRules);
}

// https://support.google.com/accounts/answer/6010255
// https://myaccount.google.com/lesssecureapps
int sendmail(const char *to, const char *from, 
			 const char *subject, const char *message)
{
    int retval = -1;
    FILE *mailpipe = popen("/usr/lib/sendmail -t", "w");
    if( mailpipe != NULL ){
        fprintf(mailpipe, "To: %s\n", to);
        fprintf(mailpipe, "From: %s\n", from);
        fprintf(mailpipe, "Subject: %s\n\n", subject);
        fwrite(message, 1, strlen(message), mailpipe);
        fwrite(".\n", 1, 2, mailpipe);
        pclose(mailpipe);
        retval = 0;
     }
     else{
         perror("Failed to invoke sendmail");
     }
     return retval;
}

void BccUsage(void)
{
	USER_CMD cmd = BCC_NO_CMD;
	char *pCmd = "http://proxyIP:port/icap?cmd=\n  i.e.,\n      http://192.168.1.14:3128/icap?cmd=4";
	ci_debug_printf(1, "\nUser Commands Available Thru: '%s'\n",pCmd);
	ci_debug_printf(1, "   (Note: Ignore the browser 'Invalid URL' return message)\n");
	while( ++cmd <= BCC_HELP ){
		switch( cmd ){
			case BCC_SHOW_DB:
				ci_debug_printf(1, "%d - Show Current Database Configuration.\n", cmd);
				break;
			case BCC_RELOAD_DB:
				ci_debug_printf(1, "%d - Reload Database Configuration.\n", cmd);
				break;
			case BCC_SHOW_ACT:
				ci_debug_printf(1, "%d - Show Current Active User.\n", cmd);
				break; 
			case BCC_CURRENT_TEMP:
				ci_debug_printf(1, "%d - Show Current Temperature(F).\n", cmd);
				break; 
			case BCC_CURRENT_HOUR:
				ci_debug_printf(1, "%d - Show Current Hour of the Day.\n", cmd);
				break; 
			case BCC_SET_CURRENT_TEMP:
				ci_debug_printf(1, "%d - Set Current Temperature(F)(enter test mode).\n", cmd);
				ci_debug_printf(1, "     (argument required: 'icap?cmd=6&arg=')\n");
				ci_debug_printf(1, "     (use -1 to disable test mode)\n");
				break; 
			case BCC_SET_CURRENT_HOUR:
				ci_debug_printf(1, "%d - Set Current Hour of the Day(enter test mode).\n", cmd);
				ci_debug_printf(1, "     (argument required: 'icap?cmd=7&arg=')\n");
				ci_debug_printf(1, "     (use -1 to disable test mode)\n");
				break; 
			case BCC_HELP:
				ci_debug_printf(1, "%d - Show This Help.\n", cmd);
				ci_debug_printf(1, "     (also via 'icap?cmd=help')\n");
				break;
			default:
				ci_debug_printf(1, "User Command '%d' Not Supported.\n", cmd);
				BccUsage();
				break;
		}
	}
	ci_debug_printf(1, "\n");
}

/*
* This function will be called if we returned CI_MOD_CONTINUE in
*  msp_check_preview_handler function, after we read all the
*  data from the ICAP client.  Called when the ICAP client has sent all its data.
* 
	returns CI_MOD_DONE if all are OK. 
			CI_MOD_ALLOW204 if the ICAP client request supports 204 responses and we 
* 				are not planning to modify anything.
			CI_ERROR on errors.
* The service must not return CI_MOD_ALLOW204 if has already send some data to the client, or the
* client does not support allow204 responses. To examine if client supports 204 responses the
* developer should use the ci_req_allow204 macro

	param req - pointer to the related ci_request struct

*/
int msp_end_of_data_handler(ci_request_t * req)
{
	int icRet = CI_NO_STATUS;
	int msRet = MSP_NO_STATUS;
	const int REQ_TYPE = ci_req_type(req);
	struct srv_msp_data *mspd = ci_service_data(req);

	ci_debug_printf(4, "\n*** msp_end_of_data_handler:: ***\n");
#ifdef _SHOW_PIDS_
	pid_t pid = getpid();
#endif
	/*if( mspd->abort ){
		// We had already start sending data....
		mspd->eof = 1;
		return CI_MOD_DONE;
	}*/
#ifdef _SHOW_PIDS_
	ci_debug_printf(2,"handle_request_preview:: Child pid: %d: \n",pid);
#endif

	if( mspd->bHasCommand ){
		switch( mspd->Command ){
			case BCC_NO_CMD:
				ci_debug_printf(1, "NULL User Command Received.\n");
				BccUsage();
				break;
			case BCC_SHOW_DB:  // 1
				ci_debug_printf(3, "Show DB Command Received.\n");
				ShowDBRules( gblpTesterData, gblpBizRules, gblNumBizRules, 1 );
				break;
			case BCC_RELOAD_DB:// 2
				ci_debug_printf(1, "Reload DB Command Received.\n");
				if( !LoadActiveRules( DATABASE_NAME ) ){
					ci_debug_printf(0, "    Business Rules Could not be Re-loaded\n");
				}
				break;
			case BCC_SHOW_ACT: // 3
				ci_debug_printf(3, "Show Active User Command Received.\n");
				ci_debug_printf(1, "   The Active Tester is '%s'\n", gblpTesterData->m_Tester);
				ci_debug_printf(1, "       Application ID is '%s'\n", gblpTesterData->m_AppId);
				ci_debug_printf(1, "       Active Weather Zipcode is '%s'\n", gblpTesterData->m_Zipcode);
				break;
			case BCC_CURRENT_TEMP:
				ci_debug_printf(3, "Show Current Temperature Command Received.\n");
				if( gblTempTestMode ){
					ci_debug_printf(1, "   Simulating Temperature of %d While in Test Mode.\n", gblCurrentTemp);
				}
				else {
					if (!gblUsingTempRule) {
						ci_debug_printf(2, "   No Temperature Rules Are Defined, therefore, no weather updates.\n");
					}
					else {
						ci_debug_printf(2, "   The Current Temperature is %d(F)\n", gblCurrentTemp);
					}
				}

				break;
			case BCC_CURRENT_HOUR:
				ci_debug_printf(3, "Show Current Hour of the Day Command Received.\n");
				ci_debug_printf(1, "   The Current Hour of the Day is '%d(F)'\n", gblHourOfDay);
				break;
			case BCC_SET_CURRENT_TEMP:
				if( mspd->bHasArg ){
					if( (mspd->CommandArg >=0) && (mspd->CommandArg < 101) ){
						gblTempTestMode = true;
						gblCurrentTemp = mspd->CommandArg;
						ci_debug_printf(1, "   Current Temperature changed to %d(F)\n", gblCurrentTemp);
					}
					else{
						if( mspd->CommandArg == -1 ){
							gblTempTestMode = false;
							ci_debug_printf(1, "   Temperature Test Mode Disabled\n");
						}
						else{
							ci_debug_printf(1, "   *** ERROR, INVALID NEW TEMP VALUE SPECIFIED: %d ***\n", mspd->CommandArg);
							ci_debug_printf(1, "   ***        temp must be between %s ***\n", "0 and 100");
						}
					}
				}
				else{
					ci_debug_printf(1, "   *** ERROR, NO NEW TEMPERATURE VALUE SUPPLIED ***\n");
				}
				break;
			case BCC_SET_CURRENT_HOUR:
				ci_debug_printf(3, "Change Current Hour of the Day Command Received.\n");
				if( mspd->bHasArg ){
					if( (mspd->CommandArg >=0) && (mspd->CommandArg < 24) ){
						gblHourTestMode = true;
						gblHourOfDay = mspd->CommandArg;
						ci_debug_printf(1, "   The Current Hour of the Day changed to %d\n", gblHourOfDay);
					}
					else{
						if( mspd->CommandArg == -1 ){
							gblHourTestMode = false;
							ci_debug_printf(1, "   Hour Test Mode Disabled\n");
						}
						else{
							ci_debug_printf(1, "   *** ERROR, INVALID NEW HOUR VALUE SPECIFIED: %d ***\n", mspd->CommandArg);
							ci_debug_printf(1, "   ***        hour must be between %s ***\n", "0 and 23");
						}
					}
				}
				else{
					ci_debug_printf(1, "   *** ERROR, NO NEW HOUR VALUE SUPPLIED ***\n");
				}
				break;
			case BCC_HELP:
				BccUsage();
				break;
			default:
				ci_debug_printf(1, "Unsupported User Command '%d' Received.\n", mspd->Command);
				BccUsage();
				break;
		}
		unlock_data(req); // this appears to prevent the browser cache having to be cleared each time
		return CI_ERROR;  // actually, still has to be done if return CI_MOD_DONE
		/* this doesn't work, only the first gets thru
		mspd->eof = 1;
		ci_req_unlock_data(req);
		return CI_MOD_DONE;
		*/
	}
	else if( !gblpTesterData ){ // no DB has been successfully loaded yet
		ci_debug_printf(0, "*** DATABASE FAILURE: NO DATABASE HAS BEEN LOADED YET!\n");
		unlock_data(req);
		return CI_ERROR;
	}

	if( gblUsingTempRule)
	{
		if( gblTempTestMode ){
			ci_debug_printf(1, "\nSimulating Temperature of %d While in Test Mode.\n", gblCurrentTemp);
		}
		else{
			/*if( -1 == lseek(gblFileDesc,0,SEEK_SET))
			{
			ci_debug_printf(0,"\nERROR Failed to seek temperature file, error [%s]\n",strerror(errno));
			}
			else{
			if( -1 == read(gblFileDesc, &gblCurrentTemp, sizeof(int)) )
			//if( -1 == fscanf(gblFileDesc, "%d", &gblCurrentTemp) )
			{
			ci_debug_printf(0,"\n read of CurrentTemp failed with error [%s]\n",strerror(errno));
			}
			else{
			ci_debug_printf(4,"\n CurrentTemp read from temporary file: %d\n",gblCurrentTemp);
			}
			}*/
			ci_debug_printf(2, "The Current Temperature is %d(F)\n", gblCurrentTemp);
		}
	}
	else{
		ci_debug_printf(2, "\nNo Temperature Rules Defined for the Active Tester.\n");
	}

	if( mspd->isReqmod ){
		ci_debug_printf(5, "All REQUEST data received, going to process!\n");
		// do sanity check, isReqmod is probably not even needed as can use ci_req_type
		if( REQ_TYPE != ICAP_REQMOD ){
			ci_debug_printf(0, "*** SANITY CHECK FAILURE: REQ_TYPE != ICAP_REQMOD!\n");
			unlock_data(req);
			return CI_ERROR;
		}
	}
	else
	{
		ci_debug_printf(5, "All RESPONSE data received, going to process!\n");
	}

	//const char * METHOD_TYPE = ci_method_string(REQ_TYPE);
	//ci_debug_printf(0, "    Message Type: %s\n", ci_method_string(REQ_TYPE));

	int ErrRet;
	BIZ_RULE *pRuleData = GetBusinessRecord(mspd, &ErrRet);
	if( !pRuleData)
	{
		if( ErrRet != MSP_OK ){
			WriteLog(0, gblLogFile, "Error Looking up Request Business Record.");
			unlock_data(req);
			return CI_ERROR;
		}
		// 'No Business Rules Defined for Endpoint', allow to send
		unlock_data(req);
		return CI_MOD_ALLOW204;
	}

	if( REQ_TYPE == ICAP_REQMOD) // #define ICAP_REQMOD    0x02
	{
		msRet = handle_request_preview(pRuleData, &ViolationMessage[0], mspd->msginfo.bIsV3);
		if( msRet == MSP_BIZ_VIO)
		{
			if( pRuleData->m_Email ){
				char *from, *subject, *message;
				from = "m_users@gmail.com";
				subject = "MULTISPEAK RULE VIOLATION";
				message = &ViolationMessage[0];
				ci_debug_printf(3,"Sending Email Notification to: %s\n", pRuleData->m_Email);
				sendmail( pRuleData->m_Email, from, subject, message );
			}
			if( !ci_req_sent_data(req) ){
				ci_membuf_t *err_page = generate_error_page(req);
				body_data_init(&mspd->body, ERROR_PAGE, 0, err_page);
			}
			else{
				ci_debug_printf(0, "*** ci_req_ALREADY_sent_data ...\n");
			}
			icRet = CI_MOD_DONE;
		}
		else if( msRet == MSP_ERROR ){
			icRet = CI_ERROR;
		}
		else if( msRet == MSP_OK ){
			icRet = CI_MOD_ALLOW204;
		}
		else{
			ci_debug_printf(0, "***BUG: Unexpected return from: %s: %d\n", "handle_request_preview", msRet);
			icRet = CI_ERROR;
		}
	}
	else if( REQ_TYPE == ICAP_RESPMOD)
	{
		ci_debug_printf(5, "*** handling_response_preview ...\n");
		msRet = handle_response_preview(pRuleData, mspd->msginfo.bIsV3);
		if( msRet == MSP_ERROR ){
			icRet = CI_ERROR;
		}
		else if( msRet == MSP_OK ){
			icRet = CI_MOD_ALLOW204;
		}
		else{
			ci_debug_printf(0, "***BUG: Unexpected return from: %s: %d\n", "handle_response_preview", msRet);
			icRet = CI_ERROR;
		}
	}
	else if( REQ_TYPE == ICAP_OPTIONS)
	{
		WriteLog( 0, gblLogFile, "ICAP OPTIONS: ignoring...");
	}
	else
	{
		//UNKNOWN ICAP METHOD
		WriteLog( 0, gblLogFile, "INVALID ICAP METHOD (%d) ignoring...", REQ_TYPE);
		icRet = CI_MOD_ALLOW204;
	}
	
	// mark the eof
	mspd->eof = 1;
	// Unlock the request body data so the c-icap server can send data
	ci_req_unlock_data(req);

	return icRet;

}

/*
 * This function will be called if we returned CI_MOD_CONTINUE in msp_check_preview_handler
 * when new data arrived from the ICAP client and when the ICAP client is
 * ready to get data.
 *
 * This function reads body data from the ICAP client and sends back the modified body data
 * To allow c-icap to send data to the ICAP client before all data is received by the c-icap a call
 * to the  ci_req_unlock_data function is required.
	 param wbuf - The buffer for writing data to the ICAP client
	 param wlen - The size of the write buffer. It must modified to be the size of writing data. If
					the service has sent all the data to the client this parameter must set to CI_EOF.
	 param rbuf - Pointer to the data read from the ICAP client
	 param rlen - The length of the data read from the ICAP client. If this function for a reason
					can not read all the data, it must modify the rlen to be equal to the read data
	 param iseof - has non zero value if the data in rbuf buffer are the last data from the ICAP client.
	 param req   - pointer to the related ci_request struct
	return Return CI_OK if all are OK or CI_ERROR on errors

	NOTE: this routine also gets called after returning CI_MOD_DONE from msp_end_of_data_handler in order 
			to put the (potentially modified) data into Squid's receive buffer.
*/
int msp_io(char *wbuf, int *wlen, char *rbuf, int *rlen, int iseof,
            ci_request_t * req)
{
	ci_debug_printf(4, "\n*** msp_io:: ***\n");
	int ret = CI_OK;
	struct srv_msp_data *mspd = ci_service_data(req);

	if( !mspd->body.type ){
		ci_debug_printf(0, "    !mspd->body.type\n");
		// probably 206 response.
		*wlen = CI_EOF;
		return CI_OK;
	}
	//write the data read from icap_client(i.e., Squid) to the mspd->body
	if( rlen && rbuf ){
		if( mspd->body.store.ring == NULL &&
		    (mspd->body.size + *rlen) > mspd->maxBodyData ){
			ci_debug_printf(0, "msp_io::content-length: %" PRIu64 " bigger than maxBodyData: %" PRId64 "\n",
			                (mspd->body.size + *rlen), mspd->maxBodyData);
			ci_debug_printf(0, "TODO: call srv_cf_body_to_ring\n");

			//if( !srv_cf_body_to_ring(&mspd->body))
			    return CI_ERROR;
			//ci_debug_printf(5, "Srv_Content_Filtering Stop buffering data, reverted to ring mode, and sent early response\n");
			/*We will not process body data. More data size than expected.*/
			//mspd->abort = 1;
			//ci_req_unlock_data(req);
		}

		*rlen = body_data_write(&mspd->body, rbuf, *rlen, iseof);
		if( *rlen == CI_ERROR ){
			ret = CI_ERROR;
			ci_debug_printf(5, "    rlen && rbuf::CI_ERROR\n");
		}
		else{
			;// msp_dumphex(rbuf, *rlen);
		}
	}
	/*
	else if( iseof ){
	//if( iseof ){
		ci_debug_printf(0, "    iseof\n");
		//msp_dumphex(wbuf, *wlen);
		body_data_write(&mspd->body, NULL, 0, iseof); // should return ret = CI_OK
	}
	else
		ci_debug_printf(0, "   NOT iseof\n");
	*/
	/*Do not send any data if we do not receive all of the data*/
	if( !mspd->eof /*&& !srv_content_filtering_data->abort*/ )
		return ret;

	// read some data from the srv_content_filtering_data->body and put them to the
	// write buffer to be send to the ICAP client
	if( /*mspd->body.type &&*/ wbuf && wlen ){
		ci_debug_printf(5, "    mspd->body.type && wbuf && wlen\n");
		*wlen = body_data_read(&mspd->body, wbuf, *wlen);
		if( *wlen == CI_ERROR ){
			ci_debug_printf(5, "    *wlen == CI_ERROR\n");
			ret = CI_ERROR;
		}
		else{
			;// msp_dumphex(wbuf, *wlen);
		}
	}
	if( *wlen==0 && mspd->eof==1 )
		*wlen = CI_EOF;

	return ret;
}

/************************** AUXILLIARY ROUTINES ********************************************/

/*
* handle_request_preview - is only called if GetBusinessRecord() finds a match for the
* 							method and endpoint in the packet.
*/
int handle_request_preview(BIZ_RULE *pRuleData, char *pVioBuff, bool bIsV3)
{
	char *pEpMsg;
	char *pRequestStr;

	ci_debug_printf(5, "    --->handle_request_preview::\n");

	if( bIsV3 ){
		pEpMsg =  "(first found V3)";
	}
	else{
		pEpMsg =  pRuleData->m_EndPoint;
	}

	time_t currtime = time(NULL);
	struct tm *tm_struct = localtime(&currtime);

	if( gblHourTestMode ){
		ci_debug_printf(1,"\nSimulating Hour of %d While in Test Mode.\n",gblHourTestMode);
	}
	else{
		gblHourOfDay = tm_struct->tm_hour;
		if( gblCurrentDay != tm_struct->tm_mday ){
			gblCurrentDay = tm_struct->tm_mday;
			pRuleData->m_NumRequests = 0;
			//pRuleData->m_NumRequestsPH = 0; allow hour to cross days
		}
	}

	// TODO: don't increment this count until we see a response come back from the endpoint
	//		that way, if endpoint is unreachable, we don't count these as successful requests.
	//BUT:  if we want to limit the # of ATTEMPTS, i.e., during a DDOS, then we should
	//		increment it now....
	pRuleData->m_NumRequests++;
	if( (pRuleData->m_numReq != WILDCARD) && (pRuleData->m_NumRequests > pRuleData->m_numReq) ){
		if( pRuleData->m_numReq == 1 )
			pRequestStr = "request";
		else
			pRequestStr = "requests";
		sprintf(pVioBuff, "'%s' request #%ld for the '%s' Endpoint was Rejected Due to a Frequency Violation:\n"
		    "   Only %ld %s per day are allowed.",
		    pRuleData->m_Method, pRuleData->m_NumRequests, pEpMsg, pRuleData->m_numReq, pRequestStr);
		WriteLog(1, gblLogFile, pVioBuff);
		return MSP_BIZ_VIO;
	}
	else if( pRuleData->m_numRPH != WILDCARD ){ // special case, if not WILDCARD, will be > 0
		if( pRuleData->m_NumRequestsPH == 0 ){
			time(&pRuleData->m_StartTime);
		}
		else{
			time_t now;
			time(&now);
			double ElapsedTime = difftime(now, pRuleData->m_StartTime);// seconds
			if( ElapsedTime >= 3600 ){
				pRuleData->m_NumRequestsPH = 0;
				time(&pRuleData->m_StartTime);
			}
		}
		pRuleData->m_NumRequestsPH++;
		if( pRuleData->m_NumRequestsPH > pRuleData->m_numRPH ){
			if( pRuleData->m_numReq == 1 )
				pRequestStr = "request";
			else
				pRequestStr = "requests";
			sprintf(pVioBuff, "'%s' request #%ld for the '%s' Endpoint was Rejected Due to a Frequency Violation:\n"
			"   Only %ld %s per hour are allowed.",
				pRuleData->m_Method, pRuleData->m_NumRequestsPH, pEpMsg, pRuleData->m_numRPH, pRequestStr);
			WriteLog(1, gblLogFile, pVioBuff);
			return MSP_BIZ_VIO;
		}
	}

	if( (pRuleData->m_maxHour != WILDCARD) && ((gblHourOfDay>pRuleData->m_maxHour) || (gblHourOfDay<pRuleData->m_minHour)) ){
		sprintf(pVioBuff, "'%s' request #%ld for the '%s' Endpoint was Rejected Due to a Time Violation:\n"
		    "   These type of requests are only allowed between the hours of %ld and %ld.\n",
			"   Current Hour Of Day is %ld\n"
		    pRuleData->m_Method, pRuleData->m_NumRequests, pEpMsg, pRuleData->m_minHour, pRuleData->m_maxHour, gblHourOfDay);
		WriteLog(1, gblLogFile, pVioBuff);
		return MSP_BIZ_VIO;
	}
	else if( (pRuleData->m_maxTemp != WILDCARD) && ((gblCurrentTemp >p RuleData->m_maxTemp) || (gblCurrentTemp  <pRuleData->m_minTemp)) ){
		sprintf(pVioBuff, "'%s' request #%ld for the '%s' Endpoint was Rejected Due to a Temperature Violation:\n"
		    "   These type of requests are only allowed when the temperature is between %ld and %ld degrees.",
			"   Current Temperature is %ld\n"
		    pRuleData->m_Method, pRuleData->m_NumRequests, pEpMsg, pRuleData->m_minTemp, pRuleData->m_maxTemp,gblCurrentTemp);
		WriteLog(1, gblLogFile, pVioBuff);
		return MSP_BIZ_VIO;
	}
	else{
		WriteLog(1, gblLogFile, "'%s' request %ld of %ld daily requests for the '%s' Endpoint was Accepted.", pRuleData->m_Method, pRuleData->m_NumRequests, pRuleData->m_numReq, pEpMsg);
		if( pRuleData->m_numRPH != WILDCARD ){
			WriteLog(1, gblLogFile,    "\n( %ld of %ld this hour )\n",
		    pRuleData->m_NumRequestsPH, pRuleData->m_numRPH);
		}
		return MSP_OK;
	}
}

/*
* handle_response_preview
*/
int handle_response_preview(BIZ_RULE *pRuleData, bool bIsV3)
{
	char *pEpMsg;
	ci_debug_printf(5, "    --->handle_response_preview::\n");
	if( bIsV3 ){
		pEpMsg =  "(first found V3)";
	}
	else{
		pEpMsg =  pRuleData->m_EndPoint;
	}
	/* TODO: get ip address and lookup the right BIZ_RULE per IP....
	 * ultimately, we'd want to index the src/dest ips to find the BIZ_RULE
	 * then check if the method is part of that connection's BIZ_RULE...
	 */
	//WriteLog(4, gblLogFile, "got ICAP_RESPMOD, ignoring...");
	
	//pRuleData->m_NumRequests++;
	WriteLog(1, gblLogFile, "*** Response ACCEPTED '%s' request %ld of %ld from '%s' Endpoint ***",
		pRuleData->m_Method, pRuleData->m_NumRequests, pRuleData->m_numReq, pEpMsg);
	if( pRuleData->m_numRPH != WILDCARD ){
		//pRuleData->m_NumRequestsPH++;
		WriteLog(1, gblLogFile, "*** ( %ld of %ld this hour ) ***",
		pRuleData->m_NumRequestsPH, pRuleData->m_numRPH);
	}
	return MSP_OK; // always pass the response on to client;
}

/*
    "<?xml version=\"1.0\"?>"
    "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" 
					   xmlns:res=\"http://www.multispeak.org/V5.0/ws/response\" 
					   xmlns:com=\"http://www.multispeak.org/V5.0/commonTypes\" 
					   xmlns:cd=\"http://www.multispeak.org/V5.0/wsdl/CD_Server\">"
        "<soapenv:Header>"
            "<MultiSpeakResponseMsgHeader MessageID = \"FE92A1A2-5255-4830-98CD-7403C45588F6\" TimeStamp=\"2019-06-06 14:11:00.970\">"
                "<MultiSpeakVersion>"
                    "<MajorVersion>5</MajorVersion>"
                    "<MinorVersion>1</MinorVersion>"
                    "<Build>0</Build>"
                "</MultiSpeakVersion>"
                "<Caller>"
                    "<AppName>MS-Server</AppName>"
                    "<Company>Pacific Northwest National Laboratory</Company>"
                "</Caller>"
                "<Result>"
                    "<resultIdentifier>"
                        "<replyCodeCategory>0</replyCodeCategory>"
                        "<index>0</index>"
                    "</resultIdentifier>"
                    "<resultDescription>Success/ no errors.</resultDescription>"
                "</Result>"
            "</MultiSpeakResponseMsgHeader>"
        "</soapenv:Header>"
        "<Body>"
            "<InitiateConnectDisconnectResponse/>"
        "</Body>"
    "</soapenv:Envelope>";
*/
BIZ_RULE *GetBusinessRecord(struct srv_msp_data *mspd, int *pErrRet)
{
	char *pMethod=NULL;
	char *pEndpoint=NULL;
	int showData = 0;
	int i=0;
	xmlNodePtr root;
	xmlDocPtr xmlDoc;

	char *buf = body_data_buf( &mspd->body );
	if( !buf ){
		ci_debug_printf(0, "\n*** msp_end_of_data_handler:: FAILED TO GET BODY BUFFER ! ***\n");
		*pErrRet = MSP_ERROR;
		return NULL;
	}

	if( showData ){
		if( !mspd->isReqmod ){
			msp_dumphex(buf, mspd->expectedData);
		}
	}
	xmlDoc = xmlParseMemory(buf, mspd->expectedData);
	if( xmlDoc == NULL ){
		ci_debug_printf(0, "XML Document not parsed successfully.\n");
		*pErrRet = MSP_ERROR;
		return NULL;
	}
	root = xmlDocGetRootElement(xmlDoc);
	if( root == NULL ){
		ci_debug_printf(0, "Failed to get XML ROOT\n");
		xmlFreeDoc(xmlDoc);
		*pErrRet = MSP_ERROR;
		return NULL;
	}
	if( xmlStrcmp(root->name, (const xmlChar *)"Envelope") ){
		ci_debug_printf(0, "\ndocument of the wrong type, root node != 'Envelope'\n");
		xmlFreeDoc(xmlDoc);
		*pErrRet = MSP_ERROR;
		return NULL;
	}

	// Initialize msginfo struct
	struct srv_msp_msg_info *pMsgInfo = &mspd->msginfo;
	memset(pMsgInfo, 0x00, sizeof(struct srv_msp_msg_info));

	if( get_method_info(root, pMsgInfo)) // get just what is needed to find the right business rule record
	{
		pMethod = pMsgInfo->method;
		// seems that most (not PingURL) V3 msgs don't include an endpoint
		if( !strncasecmp(pMsgInfo->endpoint, "Version", 7) ){ // Version_3.0
			//if( !strcmp(pMsgInfo->endpoint, "3") ){
				pEndpoint = V3_NULL_ENDPOINT;
				pMsgInfo->bIsV3 = true;
			//}
		}
		else{
			pEndpoint = pMsgInfo->endpoint;
		}
		ci_debug_printf(4, "Namespace is: '%s'\n", pMsgInfo->xmlnspace);
		ci_debug_printf(4, "Method is: '%s'\n", pMethod);
		ci_debug_printf(4, "Endpoint is: '%s'\n", pEndpoint);
		if( *pMsgInfo->xactid != 0x00)
			// MessageID should be unique, not reused by a Request, if we want to 
			// correlate a response to a request, use transactionID
			ci_debug_printf(4, "TransactionID is: '%s'\n", pMsgInfo->xactid);
	}
	else{
		ci_debug_printf(0, "ERROR getting Method info\n");
		xmlFreeDoc(xmlDoc);
		*pErrRet = MSP_ERROR;
		return NULL;
	}
	if (pMsgInfo->bIsV3) {
		ci_debug_printf(4, "Current XML Method is: '%s %s'\n", pMethod, "(No Endpoints in V3 Headers)");
	}
	else {
		ci_debug_printf(4, "Current XML Method and Endpoint: '%s, %s'\n", pMethod, pEndpoint);
	}
	// TODO, find pRuleData from IP Addresses (src/dest) ??
	//		we may not need to do that, if each separate connection is handled by a separate
	//		c-icap thread, with it's own copy of BIZ_RULE....

	BIZ_RULE *pRuleData = gblpBizRules;
	for(i = 0; i < gblNumBizRules; i++)
	{
		// check endpoint, if v3, it is not available
		if( pMsgInfo->bIsV3 || !strcmp( pRuleData->m_EndPoint, pEndpoint) )
		{
			// found the endpoint (or if v3, don't care), so check method now
			if( !strcmp( pRuleData->m_Method, pMethod) ){
				ci_debug_printf(4, "Found Business Record for %s / %s\n", pMethod, pEndpoint );
				break;
			}
			else{
				ci_debug_printf(4, "Checking Business Record for %s / %s\n",
					pRuleData->m_Method, pRuleData->m_EndPoint);
				ci_debug_printf(4, "( %s / %s )\n", pMethod, pEndpoint);
			}
		}
		pRuleData++;
	}
	if( i == gblNumBizRules )
	{
		if( mspd->isReqmod ){
			ci_debug_printf(1, "\nNo Business Rules Defined for %s / %s, Allowing Request.\n", pMethod, pEndpoint );
		}
		//else{
		//	ci_debug_printf(1, "\nNo Business Rules Defined for %s@%s, Allowing Response.\n", pMethod, pEndpoint );
		//}
		*pErrRet = MSP_OK;
		pRuleData = NULL;
	}
	else{
		if( mspd->isReqmod ){
			// while we have the xml parsed into memory, squirrel some info that might be needed 
			// for returning a business rule violation error page
			if( !get_caller_info(root, pMsgInfo) ) // squirrel away some info needed for returning a business rule violation error page
			{
				/*
				THE VERSION 5 WSDLS REFERENCE XSD FILES, BUT THE VERSION 3 ONES DON'T
				SO V3 DON'T USE THE MultiSpeakWebServicesRequestMsgHeader, INSTEAD THE HAVE
				THIS EMBEDDED IN THE REQUEST:
				<s:complexType name="MultiSpeakMsgHeader">
				<s:attribute name="Version" type="s:string"/>
				<s:attribute name="UserID" type="s:string"/>
				<s:attribute name="Pwd" type="s:string"/>
				<s:attribute name="AppName" type="s:string"/>
				<s:attribute name="AppVersion" type="s:string"/>
				<s:attribute name="Company" type="s:string"/>
				<s:attribute default="feet" name="CSUnits" type="tns:MessageHeaderCSUnits"/>
				<s:attribute name="CoordinateSystem" type="s:string"/>
				<s:attribute name="Datum" type="s:string"/>
				<s:attribute name="SessionID" type="s:string"/>
				<s:attribute name="PreviousSessionID" type="s:string"/>
				<s:attribute name="ObjectsRemaining" type="s:integer"/>
				<s:attribute name="LastSent" type="s:string"/>
				<s:attribute name="RegistrationID" type="s:string"/>
				<s:attribute name="AuditID" type="s:string"/>
				<s:attribute name="MessageID" type="s:string"/>
				<s:attribute name="TimeStamp" type="s:dateTime"/>
				<s:attribute name="BuildString" type="s:string"/>
				<s:anyAttribute/>
				</s:complexType>

				INSTEAD OF THIS:
				<xsd:complexType name="MultiSpeakRequestMsgHeader">
				<xsd:sequence>
				<xsd:element name="MultiSpeakVersion" type="com:MultiSpeakVersion"/>
				<xsd:element name="Caller" type="com:Caller"/>
				<xsd:element name="CodedNames" type="com:CodedNames" minOccurs="0"/>
				<xsd:element name="CoordinateSystemInformation" type="com:CoordinateSystemInformation" minOccurs="0"/>
				<xsd:element name="DataSetState" type="com:DataSetState" minOccurs="0"/>
				<xsd:element name="DoNotReply" type="com:registrationIDs" minOccurs="0">
				</xsd:element>
				</xsd:sequence>
				<xsd:attribute name="DefaultRegisteredName" type="prim:alphaNumericRestrictedString">
				</xsd:attribute>
				<xsd:attribute name="DefaultSystemName" type="prim:alphaNumericRestrictedString">
				</xsd:attribute>
				<xsd:attribute name="DefaultUtility" type="xsd:string">
				</xsd:attribute>
				<xsd:attribute name="DefaultCurrencyCode" type="enum:currencyCode" use="optional">
				</xsd:attribute>
				<xsd:attribute name="RegistrationID" type="prim:MultiSpeakGUID">
				</xsd:attribute>
				<xsd:attribute name="MessageID" type="xsd:string" use="required">
				</xsd:attribute>
				<xsd:attribute name="TimeStamp" type="xsd:dateTime" use="required">
				</xsd:attribute>
				<xsd:attribute name="MessageCreatedTimeStamp" type="xsd:dateTime">
				</xsd:attribute>
				<xsd:attribute name="Context" type="com:MessageContext">
				</xsd:attribute>
				<xsd:anyAttribute namespace="##any" processContents="lax"/>
				</xsd:complexType>
				
				AND in \mspCommonTypes.xsd
				<xs:complexType name="Caller">
				<xs:sequence>
				<xs:element name="AppName" type="xs:string">
				</xs:element>
				<xs:element name="AppVersion" type="xs:string" minOccurs="0">
				</xs:element>
				<xs:element name="Company" type="xs:string">
				</xs:element>
				<xs:element name="AuditID" type="xs:string" minOccurs="0">
				</xs:element>
				<xs:element name="AuditPassword" type="xs:string" minOccurs="0">
				</xs:element>
				<xs:element name="SystemID" type="xs:string" minOccurs="0">
				</xs:element>
				<xs:element name="Password" type="xs:string" minOccurs="0">
				</xs:element>
				</xs:sequence>
				</xs:complexType>
				*/
				/*char buf[1000];
				size_t len = ci_headers_pack_to_buffer(root, buf, 1000);
				msp_dumphex(buf, len);
				msp_dumphex(pMsgInfo, 200);*/
				/*
				* Dump the document to a buffer and print it
				* for demonstration purposes.
				* /
				xmlChar *xmlbuff;
				int buffersize;
				xmlDocDumpFormatMemory(xmlDoc, &xmlbuff, &buffersize, 1);
				printf("xmlDocDumpFormatMemory::%s", (char *)xmlbuff);
				// Free associated memory.
				xmlFree(xmlbuff);

				/ *xmlChar *s;
				int size;
				char * xmlString;
				xmlDocDumpMemory((xmlDocPtr)xmlDoc, &s, &size);
				xmlString = (char *)s;
				printf("%s", xmlString);
				xmlFree(s);* /

				// allocate a buffer to dump into
				xmlBufferPtr buf = xmlBufferCreate();
				// dump the node
				xmlNodeDump(buf, xmlDoc, root, 0, 0 );
				msp_dumphex((char *)buf, 1000);
				xmlFree(buf);
				*/
				//ci_debug_printf(0, "*** ERROR getting caller information ...\n");
				//*pErrRet = MSP_ERROR;
				//pRuleData = NULL;
				// do not consider missing calling info a big deal
				ci_debug_printf(4, "*** Caller Information is Absent.\n");
				*pErrRet = MSP_OK;
				pRuleData = pRuleData;
			}
			else{
				*pErrRet = MSP_OK;
				pRuleData = pRuleData;
			}
		}
		else{
			*pErrRet = MSP_OK;
			pRuleData = pRuleData;
		}
	}

	// freeing BOTH of these cause death later on
	//xmlFree((void *)pMethod);
	xmlFreeDoc(xmlDoc); 

	return pRuleData;
}

/*
 * generate template_page,/usr/local/share/c_icap/templates/msp/en/MSP_RESPONSE
* look for 'TemplateDir' in config file
*
* It does not seem to matter what is put before and after the code,
* Squid must be looking up each piece based on the code: ie.
*	ci_http_response_add_header(req, "HTTP/1.0 403 Forbidden");
*		gets printed by Squid as "HTTP/1.1 403 Forbidden"
*	ci_http_response_add_header(req, "HTTP/6.2 404 UnauthorizedUSOB!");
*		gets printed by Squid as "HTTP/1.1 404 Not Found"
*/
static ci_membuf_t *generate_error_page(ci_request_t *req)
{
	ci_debug_printf(4, "        --->generate_error_page::\n");
	char buf[1024];
	const char *lang;
	ci_membuf_t *err_page;
	ci_http_response_create(req, 1, 1); /*Build the response headers */
	/*
	if( ci_http_response_headers(req) ){
		ci_http_response_reset_headers(req);
	}
	else{
		ci_http_request_remove_header(req, "Content-Encoding");
		ci_http_request_remove_header(req, "Content-Length");
		//ci_http_response_create(ci_request_t * req, int has_reshdr, int has_body)
		ci_http_response_create(req, 1, 1);
	}
	*/
	ci_http_response_add_header(req, "HTTP/1.0 403 Forbidden"); /*Send an 403 Forbidden http response to web client */
	//ci_http_response_add_header(req, "Server: C-ICAP");
	ci_http_response_add_header(req, "Content-Type: text/html");
	ci_http_response_add_header(req, "Connection: close");

	err_page = ci_txt_template_build_content(req, "msp", "MSP_RESPONSE", MspFmtTable);

	lang = ci_membuf_attr_get(err_page, "lang");
	if( lang ){
		snprintf(buf, sizeof(buf), "Content-Language: %s", lang);
		buf[sizeof(buf) - 1] = '\0';
		ci_http_response_add_header(req, buf);
	}
	else
		ci_http_response_add_header(req, "Content-Language: en");
	return err_page;
}


/************************** UTILITY ROUTINES ***********************************************/

/*
 * fmt_srv_msp_namespace - handle %MSNS format specifier
 */
int fmt_srv_msp_namespace(ci_request_t *req, char *buf, int len, const char *param)
{
	ci_debug_printf(5, "*** fmt_srv_msp_namespace ***\n");
	struct srv_msp_data *uc = ci_service_data(req);
	if( uc ){
		return snprintf(buf, len, "%s", uc->msginfo.xmlnspace);
	}
	return snprintf(buf, len, "%s", "ERR");
}

/*
 * fmt_srv_msp_msgid - handle %MSGID format specifier
 */
int fmt_srv_msp_msgid(ci_request_t *req, char *buf, int len, const char *param)
{
	/* typedef unsigned char uuid_t[16];*/
	uuid_t uuid;

	// generate
	uuid_generate_time_safe(uuid);

	// unparse (to string)
	char uuid_str[37];      // ex. "1b4e28ba-2fa1-11d2-883f-0016d3cca427" + "\0"
	uuid_unparse_lower(uuid, uuid_str);
	//printf("generated uuid=%s\n", uuid_str);

	//ci_debug_printf(5, "*** fmt_srv_msp_msgid ***\n");
	//struct srv_msp_data *uc = ci_service_data(req);
	//return snprintf(buf, len, "%s", uc->msginfo.msgid);
	return snprintf(buf, len, "%s", uuid_str);
}

/*
 * fmt_srv_msp_timestamp - handle %MSTIME format specifier
 *		TimeStamp="2019-06-26 07:10:10.018"
 */
int fmt_srv_msp_timestamp(ci_request_t *req, char *buf, int len, const char *param)
{
	ci_debug_printf(5, "*** fmt_srv_msp_timestamp ***\n");
	char buffer[100];

	time_t now = time(0);
	strftime(buffer, 100, "%Y-%m-%d %H:%M:%S.000", localtime(&now));

	return snprintf(buf, len, "%s", buffer);
}

/*
 * fmt_srv_msp_appname - handle %MSAPP format specifier
 */
int fmt_srv_msp_appname(ci_request_t *req, char *buf, int len, const char *param)
{
	ci_debug_printf(5, "*** fmt_srv_msp_appname ***\n");
	struct srv_msp_data *uc = ci_service_data(req);
	if( uc ){
		return snprintf(buf, len, "%s", uc->msginfo.appname);
	}
	return snprintf(buf, len, "%s", "ERR");
}

/*
 * fmt_srv_msp_company - handle %MSCMPY format specifier
 */
int fmt_srv_msp_company(ci_request_t *req, char *buf, int len, const char *param)
{
	ci_debug_printf(5, "*** fmt_srv_msp_company ***\n");
	struct srv_msp_data *uc = ci_service_data(req);
	if( uc ){
		return snprintf(buf, len, "%s", uc->msginfo.company);
	}
	return snprintf(buf, len, "%s", "ERR");
}

/*
 * fmt_srv_msp_method - handle %MSMTHD format specifier
 */
int fmt_srv_msp_method(ci_request_t *req, char *buf, int len, const char *param)
{
	ci_debug_printf(5, "*** fmt_srv_msp_method ***\n");
	struct srv_msp_data *uc = ci_service_data(req);
	if( uc ){
		return snprintf(buf, len, "%s", uc->msginfo.method);
	}
	return snprintf(buf, len, "%s", "ERR");
}

/*
 * fmt_srv_msp_transactionid - handle %MSTXID format specifier
 */
int fmt_srv_msp_transactionid(ci_request_t *req, char *buf, int len, const char *param)
{
	ci_debug_printf(5, "*** fmt_srv_msp_transactionid ***\n");
	struct srv_msp_data *uc = ci_service_data(req);
	if( uc ){
		if( *uc->msginfo.xactid != 0x00 ){
			return snprintf(buf, len, "<tns:transactionID>%s</tns:transactionID>", uc->msginfo.xactid);
		}
		return 0;
	}
	return snprintf(buf, len, "%s", "ERR");
}

//
/////////////
/*
	Version 5 PingURL:
	<?xml version="1.0" encoding="utf-8"?>
	<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
	  <soap:Header>
		<request:MultiSpeakRequestMsgHeader xmlns:http="http://schemas.xmlsoap.org/wsdl/http/" MessageID="?" TimeStamp="?" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:com="http://www.multispeak.org/V5.0/commonTypes" xmlns:response="http://www.multispeak.org/V5.0/ws/response" xmlns:ns8="http://docs.oasis-open.org/wsrf/bf-2" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:tns="http://www.multispeak.org/V5.0/wsdl/OA_Server" xmlns:mime="http://schemas.xmlsoap.org/wsdl/mime/" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:request="http://www.multispeak.org/V5.0/ws/request" xmlns:prim="http://www.multispeak.org/V5.0/primitives" xmlns:enum="http://www.multispeak.org/V5.0/enumerations" xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/" xmlns:soap12="http://schemas.xmlsoap.org/wsdl/soap12/" xmlns:ns9="http://www.w3.org/2005/08/addressing">
		  <request:MultiSpeakVersion>
			<com:MajorVersion>?</com:MajorVersion>
			<com:MinorVersion>?</com:MinorVersion>
			<com:Build>?</com:Build>
		  </request:MultiSpeakVersion>
		  <request:Caller>
			<com:AppName>?</com:AppName>
			<com:Company>?</com:Company>
		  </request:Caller>
		</request:MultiSpeakRequestMsgHeader>
	  </soap:Header>
	  <soap:Body>
		<tns:PingURL xmlns:http="http://schemas.xmlsoap.org/wsdl/http/" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:com="http://www.multispeak.org/V5.0/commonTypes" xmlns:response="http://www.multispeak.org/V5.0/ws/response" xmlns:ns8="http://docs.oasis-open.org/wsrf/bf-2" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:tns="http://www.multispeak.org/V5.0/wsdl/OA_Server" xmlns:mime="http://schemas.xmlsoap.org/wsdl/mime/" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:request="http://www.multispeak.org/V5.0/ws/request" xmlns:arrays="http://www.multispeak.org/V5.0/commonArrays" xmlns:msp="http://www.multispeak.org/V5.0" xmlns:prim="http://www.multispeak.org/V5.0/primitives" xmlns:enum="http://www.multispeak.org/V5.0/enumerations" xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/" xmlns:soap12="http://schemas.xmlsoap.org/wsdl/soap12/" xmlns:ns9="http://www.w3.org/2005/08/addressing">?</tns:PingURL>
	  </soap:Body>
	</soap:Envelope>

	Version 3 PingURL: it is using a V5 header!
	<?xml version="1.0" encoding="utf-8"?>
	<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
	  <soap:Header>
		<request:MultiSpeakRequestMsgHeader xmlns:http="http://schemas.xmlsoap.org/wsdl/http/" MessageID="?" TimeStamp="?" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:com="http://www.multispeak.org/V5.0/commonTypes" xmlns:response="http://www.multispeak.org/V5.0/ws/response" xmlns:ns8="http://docs.oasis-open.org/wsrf/bf-2" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:tns="http://www.multispeak.org/V5.0/wsdl/OA_Server" xmlns:mime="http://schemas.xmlsoap.org/wsdl/mime/" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:request="http://www.multispeak.org/V5.0/ws/request" xmlns:prim="http://www.multispeak.org/V5.0/primitives" xmlns:enum="http://www.multispeak.org/V5.0/enumerations" xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/" xmlns:soap12="http://schemas.xmlsoap.org/wsdl/soap12/" xmlns:ns9="http://www.w3.org/2005/08/addressing">
		  <request:MultiSpeakVersion>
			<com:MajorVersion>?</com:MajorVersion>
			<com:MinorVersion>?</com:MinorVersion>
			<com:Build>?</com:Build>
		  </request:MultiSpeakVersion>
		  <request:Caller>
			<com:AppName>?</com:AppName>
			<com:Company>?</com:Company>
		  </request:Caller>
		</request:MultiSpeakRequestMsgHeader>
	  </soap:Header>
	  <soap:Body>
		<tns:PingURL xmlns:http="http://schemas.xmlsoap.org/wsdl/http/" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:com="http://www.multispeak.org/V5.0/commonTypes" xmlns:response="http://www.multispeak.org/V5.0/ws/response" xmlns:ns8="http://docs.oasis-open.org/wsrf/bf-2" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:tns="http://www.multispeak.org/V5.0/wsdl/OA_Server" xmlns:mime="http://schemas.xmlsoap.org/wsdl/mime/" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:request="http://www.multispeak.org/V5.0/ws/request" xmlns:arrays="http://www.multispeak.org/V5.0/commonArrays" xmlns:msp="http://www.multispeak.org/V5.0" xmlns:prim="http://www.multispeak.org/V5.0/primitives" xmlns:enum="http://www.multispeak.org/V5.0/enumerations" xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/" xmlns:soap12="http://schemas.xmlsoap.org/wsdl/soap12/" xmlns:ns9="http://www.w3.org/2005/08/addressing">?</tns:PingURL>
	  </soap:Body>
	</soap:Envelope>

	NOTE: xmlns:tns="http://www.multispeak.org/V5.0/wsdl/OA_Server"


BUT: this is the ODEventNotification (v3 only)
it is using a V3 header

SOAPAction: http://www.multispeak.org/Version_3.0/ODEventNotification
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <tns:MultiSpeakMsgHeader xmlns:tns="http://www.multispeak.org/Version_3.0" xmlns:http="http://schemas.xmlsoap.org/wsdl/http/" xmlns:soap12="http://schemas.xmlsoap.org/wsdl/soap12/" xmlns:mime="http://schemas.xmlsoap.org/wsdl/mime/" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">?</tns:MultiSpeakMsgHeader>
  </soap:Header>
  <soap:Body>
    <tns:ODEventNotification xmlns:tns="http://www.multispeak.org/Version_3.0" xmlns:http="http://schemas.xmlsoap.org/wsdl/http/" xmlns:soap12="http://schemas.xmlsoap.org/wsdl/soap12/" xmlns:mime="http://schemas.xmlsoap.org/wsdl/mime/" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"/>
  </soap:Body>
</soap:Envelope>

	NOTE: xmlns:tns="http://www.multispeak.org/Version_3.0"

*/
static bool get_method_info(xmlNodePtr root, struct srv_msp_msg_info *pMsgInfo)
{
	xmlNodePtr pReturnedNode = getChildNode(root->children, (const xmlChar *)"Body");
	if( pReturnedNode)
	{
		xmlNodePtr chld_node = pReturnedNode->xmlChildrenNode;
		while (chld_node != NULL)
		{
			if( chld_node->type == XML_ELEMENT_NODE ){
				break;
			}
			chld_node = chld_node->next;
		}
		if( chld_node ){
			strncpy(pMsgInfo->method, (char *)chld_node->name, CI_MAXMETHODLEN);
			if( chld_node->ns ){
				const xmlChar *pNsRef = chld_node->ns->href;
				strncpy(pMsgInfo->xmlnspace, (char *)pNsRef, CI_MAXNSLEN);
				char *p = strrchr((char *)pNsRef, '/');
				if( p ){
					strncpy(pMsgInfo->endpoint, p + 1, CI_MAXENDPOINTLEN);
				}
			}
			xmlNodePtr body_chld = NULL;
			for (body_chld = chld_node->children; body_chld; body_chld = body_chld->next ){
				if( body_chld->type == XML_ELEMENT_NODE ){
					if( (!xmlStrcasecmp(body_chld->name, (const xmlChar *)"transactionID")) ){
						strncpy(pMsgInfo->xactid, (char *)xmlNodeGetContent(body_chld), CI_MAACTIDLEN);
						break;
					}
				}
			}
		}
		else{
			ci_debug_printf(0,"Failed to get child node element for '%s'\n", "Body");
		}
	}
	else{
		ci_debug_printf(0,"Failed to get child node '%s' for '%s'\n", "Body", "root");
	}

	if( *pMsgInfo->xmlnspace != 0x00 && *pMsgInfo->method != 0x00 && *pMsgInfo->endpoint != 0x00)
		return true;
	else
		return false;
}

//
//////////////
static bool get_caller_info(xmlNodePtr root, struct srv_msp_msg_info *pMsgInfo )
{
	xmlNodePtr cur_node = NULL;
	xmlNodePtr nxt_node = NULL;
	xmlNodePtr chld_node = NULL;
	xmlAttr *cur_attr = NULL;
	xmlChar *attr = NULL;

	int num_needed = 2;
	int num_gotten = 0;
	bool bFound = false;
	bool bFoundAttr = false;

	for (cur_node = root; cur_node; cur_node = cur_node->next ){
		if( bFound)
			return false;
		if( cur_node->type == XML_ELEMENT_NODE)
		{
			ci_debug_printf(4, "*** %s \n", cur_node->name);
			/* if Version3:
				*** Envelope
				*** Header
				*** MultiSpeakMsgHeader		<===============
				*** Body
				*** PingURL
			if Version5:
				*** Envelope
				*** Header
				*** MultiSpeakRequestMsgHeader \ MultiSpeakResponseMsgHeader
				*** MultiSpeakVersion
				*** MajorVersion
				*** MinorVersion
				*** Build
				*** Caller					<===============
				*** Body
				*** PingURL
			*/
			if( (!xmlStrcasecmp(cur_node->name, (const xmlChar *)"MultiSpeakMsgHeader")) ||
				(!xmlStrcasecmp(cur_node->name, (const xmlChar *)"Caller")) )
			{
				//ci_debug_printf(4, "*** cur_node->name: %s Found \n", cur_node->name);
				if (pMsgInfo->bIsV3) { // MultiSpeakMsgHeader
					chld_node = cur_node;
				}
				else {
					chld_node = cur_node->children;
				}

				for (; chld_node; ) {
					//ci_debug_printf(4, "*** chld_node->name: %s Found \n", chld_node->name);
					if (pMsgInfo->bIsV3) {
						for (cur_attr = chld_node->properties; cur_attr; cur_attr = cur_attr->next) {
							bFoundAttr = true;
							if ((!xmlStrcasecmp(cur_attr->name, (const xmlChar *)"AppName")))
							{
								strncpy(pMsgInfo->appname, (char *)xmlNodeGetContent((const xmlNode *)cur_attr), CI_MAXAPPNAMELEN);
								ci_debug_printf(4, "*** AppName Found: %s \n", pMsgInfo->appname);
								num_gotten++;
							}
							else if ((!xmlStrcasecmp(cur_attr->name, (const xmlChar *)"Company")))
							{
								strncpy(pMsgInfo->company, (char *)xmlNodeGetContent((const xmlNode *)cur_attr), CI_MAXCOMPANYLEN);
								ci_debug_printf(4, "*** Company Found: %s \n", pMsgInfo->company);
								num_gotten++;
							}
							else
							{
								ci_debug_printf(4, "  -> Found attribute : %s\n", cur_attr->name);
								attr = xmlNodeGetContent((const xmlNode *)cur_attr);
								ci_debug_printf(4, "     -> with Value: %s\n", attr);
							}
						} // for cur_attr
						if( !bFoundAttr )
							ci_debug_printf(4, "No Attributes Found\n");
						bFound = true;
						chld_node = NULL;
					}
					else {
						if ((!xmlStrcasecmp(chld_node->name, (const xmlChar *)"AppName")))
						{
							strncpy(pMsgInfo->appname, (char *)xmlNodeGetContent(chld_node), CI_MAXAPPNAMELEN);
							ci_debug_printf(4, "*** AppName Found: %s \n", pMsgInfo->appname);
							num_gotten++;
						}
						else if ((!xmlStrcasecmp(chld_node->name, (const xmlChar *)"Company")))
						{
							strncpy(pMsgInfo->company, (char *)xmlNodeGetContent(chld_node), CI_MAXCOMPANYLEN);
							ci_debug_printf(4, "*** Company Found: %s \n", pMsgInfo->company);
							num_gotten++;
						}
						chld_node = chld_node->next;
						if (num_gotten == num_needed) {
							bFound = true;
							break;
						}
					} // v5
				} // for chld_node
				nxt_node = NULL;
			}
			else{
				nxt_node = cur_node->children;
			}
		}//  if XML_ELEMENT_NODE 
		else{
			nxt_node = cur_node->children;
		}
		//if( !pMsgInfo->bIsV3 && !bFound )
		if( !bFound )
			get_caller_info(nxt_node, pMsgInfo);
	}// for

	if( *pMsgInfo->appname != 0x00 && *pMsgInfo->company != 0x00)
		return true;
	else{
		if( *pMsgInfo->appname == 0x00 )
			strncpy(pMsgInfo->appname, "N/A", CI_MAXAPPNAMELEN);
		if( *pMsgInfo->company == 0x00 )
			strncpy(pMsgInfo->company, "N/A", CI_MAXCOMPANYLEN);
		return false;
	}
}

void msp_dumphex(  char *data, int len )
{
	char *current = data;
	int offset,i;
	ci_debug_printf(2, "    msp_dumphex:: len: %d\n",len);

	for(offset = 0; offset < len; offset += 16)
	{
		printf("   %08x ",offset);
		//ci_debug_printf(2, "msp_preview_handler:: ***\n");

		for (i = 0; i < 16; i++)
		{
			if( current + i < data + len)
				printf("%02x ",current[i]);
			else
				printf("   ");
		}
		for (i = 0; i < 16; i++)
		{
			if( current + i < data + len)
				printf("%c", isprint(current[i]) ? current[i] : '.');
			else
				printf(" ");
		}
		printf("\n");
		current += 16;
	}
}
// 
///////////////////////////////////////////////////////////////////////////////
xmlNodePtr getChildNode(xmlNodePtr currnode, const xmlChar *elem)
{
	xmlNodePtr pRet;
	xmlNodePtr n;

	//if( !currnode )
	//	return NULL;
	for (n = currnode; n; n = n->next)
	{
		if( n->type == XML_ELEMENT_NODE)
		{
			if( (!xmlStrcasecmp(n->name, elem)))
			{
				//printf("Found element '%s'\n", elem);
				return n;
			}
			else{
				//printf("Not Found element '%s' @ '%s'\n", elem, n->name);
				pRet = getChildNode(n->next, elem);
				if( pRet)
					return pRet;
			}
		}
	}
	return NULL;
}

// Write formatted output to Log File (if loglevel = 0)
void WriteLog(int loglevel, FILE *pFile, const char *format, ...)
{
	char *pStr;
	int len;

	// WARNING, THERE IS NO CHECK THAT THE # OF ARGS MATCHES THE NUMBER OF FORMAT SPECIFIERS
	//		A MISMATCH WILL CAUSE A SEGMENTATION FAULT
	va_list args;
	va_start(args, format);

	if( pFile && (loglevel == 0))
	{
		time_t currtime = time(NULL);
		struct tm *tm_struct = localtime(&currtime);
		pStr = asctime(tm_struct);
		len = strnlen(pStr,STRBUFF_LEN);
		if( len == STRBUFF_LEN ){
			ci_debug_printf(loglevel, "%s\n", str);
		}
		else{
			// asctime seems to append a <CR> so overwrite it by using len-1
			len--;
			strncpy(str, pStr, len);
			strcpy(&str[len], ": ");
			vsnprintf(&str[len + 2], STRBUFF_LEN - (len + 2), format, args);
			fprintf(pFile, "\n%s", str);
			fflush(pFile);
			ci_debug_printf(loglevel, "%s\n", &str[len + 1]);
		}
	}
	else{
		vsprintf(str, format, args);
		ci_debug_printf(loglevel, "%s\n", str);
	}

	va_end(args);
	return;
}

