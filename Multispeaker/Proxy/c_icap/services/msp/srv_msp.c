/*-------------------------------------------------------------------------------

  Multi-Speak - Secure Protocol Enterprise Access Kit(MS_SPEAK)
  Copyright © 2019, Battelle Memorial Institute
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
		06/05/2019 - CHM: only increment m_ValidRequestNum upon seeing a response.
		06/20/2019 - CHM: ingest the complete packet, so can parse the well-formed xml inside.
		06/29/2019 - CHM: support all methods/endpoints.
-------------------------------------------------------------------------------
	NOTE:  the following build instructions apply to a linux debian 9 system

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
			
		NOTE:  if the icap machine is rebooted, the directories for the icap lock file will no longer exist,
				  and must be recreated: you may see the following error when starting c-icap:
						Cannot open the pid file: /var/run/c-icap/c-icap.pid or c-icap.ctl
					do:
						sudo mkdir /var/run/c-icap
				this happens because /var/run is a tmpfs filesystem, so it
				is emptied at each boot, to have a directory created in it each
				boot, add a .conf file to /run/tmpfiles.d:
					/usr/lib/tmpfiles.d/c-icap.conf
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



	to build the business rule editor:
		TODO....
		see ~/.bash_history from Irene

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
#include <glib.h>
#include <glib/gprintf.h>
#include <time.h>
#include <libxml/xmlmemory.h>
#include <libxml/parser.h>
#include <uuid/uuid.h> 

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
 */

#define CI_MAXMSGIDLEN 256
#define CI_MAXTIMESTAMPLEN 256
#define CI_MAXAPPNAMELEN 256
#define CI_MAXCOMPANYLEN 256
#define CI_MAXMETHODLEN 256
#define CI_MAXENDPOINTLEN 256
#define CI_MAXNSLEN 256
#define CI_MAXXACTIDLEN 256

#define MSP_NO_STATUS   0
#define MSP_OK          1
#define MSP_BIZ_VIO		2 // business rule violation
#define MSP_ERROR		3

#define MAX_GROUPLEN 80
#define WILDCARD_STR "-1"
#define WILDCARD -1
#define LOG_URL_SIZE 256
#define LOW_BUFF 256

/*
 * The srv_msp_data structure will store the data required to serve an ICAP request.
 */
struct srv_msp_msg_info {
	char xmlnspace[CI_MAXNSLEN + 1];
	char method[CI_MAXMETHODLEN + 1];
	char endpoint[CI_MAXENDPOINTLEN + 1];
	char xactid[CI_MAXXACTIDLEN + 1];
	char appname[CI_MAXAPPNAMELEN + 1];
	char company[CI_MAXCOMPANYLEN + 1];
	//char msgid[CI_MAXMSGIDLEN + 1];
	//char timestamp[CI_MAXTIMESTAMPLEN + 
};

struct srv_msp_data {
	struct body_data body;
	struct srv_msp_msg_info msginfo;
	int64_t maxBodyData;
	int64_t expectedData;
	/*flag for marking the eof*/
	int eof;
	int isReqmod;
};

typedef struct _bizdata {
	gint64 m_numReq;
	gint64 m_minTemp;
	gint64 m_maxTemp;
	gint64 m_minHour;
	gint64 m_maxHour;
	gint64 m_ValidRequestNum;
	gint64 m_TotalRequestNum;
	gchar  m_Method[MAX_GROUPLEN];
	gchar *m_EndPoint;
} BIZ_DATA;

int fmt_srv_msp_namespace(ci_request_t *, char *, int, const char *);
int fmt_srv_msp_msgid(ci_request_t *, char *, int, const char *);
int fmt_srv_msp_timestamp(ci_request_t *, char *, int, const char *);
int fmt_srv_msp_appname(ci_request_t *, char *, int, const char *);
int fmt_srv_msp_company(ci_request_t *, char *, int, const char *);
int fmt_srv_msp_method(ci_request_t *, char *, int, const char *);
int fmt_srv_msp_transactionid(ci_request_t *, char *, int, const char *);
struct ci_fmt_entry MspFmtTable [] = {
	{ "%MSNS", "Namespace", fmt_srv_msp_namespace },
	{ "%MSGID", "MessageID", fmt_srv_msp_msgid },
	{ "%MSTIME", "TimeStamp", fmt_srv_msp_timestamp},
	{ "%MSAPP", "AppName", fmt_srv_msp_appname},
	{ "%MSCMPY", "Company", fmt_srv_msp_company},
	{ "%MSMTHD", "Method", fmt_srv_msp_method },
	{ "%MSTXID", "XActID", fmt_srv_msp_transactionid },
    { NULL, NULL, NULL}
};

// module prototypes
int msp_init_service(ci_service_xdata_t *, struct ci_server_conf *);
int msp_post_init_service(ci_service_xdata_t *, struct ci_server_conf *);
void msp_close_service();
void *msp_init_request_data(ci_request_t *);
void msp_release_request_data(void *);
int msp_preview_handler(char *, int, ci_request_t *);
int msp_end_of_data_handler(ci_request_t *);
int msp_io(char *, int *, char *, int *, int, ci_request_t *);
CI_DECLARE_MOD_DATA ci_service_module_t service = {
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
int handle_request_preview(BIZ_DATA *);
int handle_response_preview(BIZ_DATA *);
void WriteLog(int, FILE *, const char *, ...);
void msp_dumphex(char *, int);
BIZ_DATA *GetBusinessRecord(struct srv_msp_data *, int *);
static ci_membuf_t *generate_error_page(ci_request_t *);
static bool get_method_info(xmlNodePtr root, struct srv_msp_msg_info *pMsgInfo);
static bool get_caller_info(xmlNodePtr root, struct srv_msp_msg_info *pMsgInfo);
xmlNodePtr getChildNode(xmlNodePtr currnode, const xmlChar *elem);

// globals
char str[800];
int currtemp;  // NOTE: used to be able to force change of temp by sending CD_Server method other than InitiateConnectDisconnect
int currday;
int hour;
int MainThread = 0;
int NumBizRecs;
FILE *LogFile = NULL;
BIZ_DATA *pBizRecords;

// statics
static ci_off_t MaxBodyData = 4 * 1024 * 1024; // 4,194,304 (4M)
static int MSP_DATA_POOL = -1;

/*
 * This function called exactly when the service is loaded by c-icap.
 * Can be used to initialize the service.
	 param srv_xdata  - Pointer to the ci_service_xdata_t object of this service
	 param server_conf- Pointer to the struct holds the main c-icap server configuration
	 return CI_OK on success, CI_ERROR on any error. 
 */
int msp_init_service(ci_service_xdata_t * srv_xdata,
					struct ci_server_conf *server_conf)
{
	ci_debug_printf(0, "\n*** msp_init_service::Initializing msp module v2.0 ***\n");

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
	if (MSP_DATA_POOL < 0)
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
 */
int msp_post_init_service(ci_service_xdata_t * srv_xdata, struct ci_server_conf *server_conf)
{
	gchar    *BizFile = "/home/msspeak/BizRules.cfg";
	gsize num_groups, num_keys;
	gchar **keys=NULL, *curr_key;
	gchar *str_value, *curr_grp;
	guint64	value64;
	gsize length;
	BIZ_DATA *pBzd;
	size_t 	size;
	const char *LogPath="";
	guint group, key;

	GError   *error = NULL;
	ci_debug_printf(3, "\n*** msp_post_init_service::\n");
	ci_debug_printf(1, "    Loading Business Rules from '%s'\n", BizFile);
	
	GKeyFile *BizCfgFile = g_key_file_new();
	if (!g_key_file_load_from_file (BizCfgFile, BizFile, G_KEY_FILE_NONE, &error))
	{
		if( !g_error_matches (error, G_FILE_ERROR, G_FILE_ERROR_NOENT) ){
			ci_debug_printf(0, "    Error loading Business Rule file: %s", error->message);
		}
		else{
			ci_debug_printf(0, "    Business Rule File Load Failed.\n");
		}
		g_critical("%s", error->message);
		g_key_file_free(BizCfgFile);
		exit( -2 );
		//return CI_ERROR;
	}
	ci_debug_printf(2, "    Successfully Loaded Business Rules.\n");
	if( CI_DEBUG_LEVEL >= 3 ){
		printf("  %s\n", g_key_file_to_data(BizCfgFile, &length, &error));
	}
	/*
	[Settings]
	LogFile = /home/msspeak/srv_msp.log

	[GetCDSupportedMeters@CD_Server]
	minHour = 5
	maxHour = 17
	minTemp = 32
	maxTemp = 90
	numReq = 6

	[InitiateConnectDisconnect@CD_Server]
	minTemp = 32
	maxTemp = 83
	numReq = 7
	minHour = 8
	maxHour = 14

	[GetLatestMeterReadings@MR_Server]
	minHour = 0
	maxHour = 23
	minTemp = 32
	maxTemp = 100
	numReq = 23

	[ChangeMeterData@CB_Server]
	numReq = 10

	[InitiateEndDevicePings@OD_Server]
	numReq = 12
	minHour = 9
	maxHour = 17	
	*/

	time_t currtime = time(NULL);
	struct tm *tm_struct = localtime(&currtime);
	gchar   **pgGroups;


	srand(currtime);
	//currtemp = (rand() % (90 - 32 + 1)) + 32;
	currtemp = 45;

	pgGroups = g_key_file_get_groups(BizCfgFile, &num_groups);
	NumBizRecs = num_groups-1; //deduct "Settings" group
	size = NumBizRecs * sizeof(BIZ_DATA);

	pBizRecords = (BIZ_DATA *)malloc(size);
	memset(pBizRecords, WILDCARD, size);// preset any missing fields
	pBzd = pBizRecords;
	for(group = 0;group < num_groups;group++)
	{
		error = NULL;
		curr_grp = pgGroups[group];
		if( strlen(curr_grp) > MAX_GROUPLEN-1){
			g_critical("Group Name '%s' exceeds max. length.", curr_grp);
			exit( -1 );
		}

		if( !strcmp(curr_grp, "Settings")){
			str_value = g_key_file_get_value (BizCfgFile, "Settings", "LogFile", &error);
			if( str_value == NULL )
			{
				if( g_error_matches (error, G_KEY_FILE_ERROR, G_KEY_FILE_ERROR_KEY_NOT_FOUND) )
				{
					LogPath = "/var/log/srv_msp.log";
					error = NULL;
				}
				else
				{
					if( g_error_matches (error, G_KEY_FILE_ERROR, G_KEY_FILE_ERROR_GROUP_NOT_FOUND) )
					{
						g_critical( "Group Error While Getting Value for Key '%s': %s\n", "LogFile", error->message);
					}
					else{
						g_critical( "Unexpected Error(%s) While Getting Value for Key '%s'\n", error->message, "LogFile");
					}
					exit(-1);
				}
			}
			else
			{
				LogPath = str_value;
			}
			continue;
		}

		pBzd->m_ValidRequestNum = 0;
		pBzd->m_TotalRequestNum = 0;

		keys = g_key_file_get_keys(BizCfgFile, curr_grp, &num_keys, &error);
		for(key = 0;key < num_keys;key++)
		{
			curr_key = keys[key];
			/*
				If key cannot be found then 0 is returned and error is set to G_KEY_FILE_ERROR_KEY_NOT_FOUND.
				Likewise, if the value associated with key cannot be interpreted as an integer, or is out of
				range for a gint, then 0 is returned and error is set to G_KEY_FILE_ERROR_INVALID_VALUE.
			*/
			value64 = g_key_file_get_uint64(BizCfgFile, curr_grp, curr_key, &error);
			if( value64 == 0 )
			{
				if( g_error_matches (error, G_KEY_FILE_ERROR, G_KEY_FILE_ERROR_KEY_NOT_FOUND) )
				{
					g_critical( "Sanity Failure Getting Key Value: '%s'\n", error->message);
					exit(-1);
				}
				else if( g_error_matches (error, G_KEY_FILE_ERROR, G_KEY_FILE_ERROR_INVALID_VALUE) )
				{
					g_critical( "Invalid Key Value, Error: '%s'\n", error->message);
					exit(-1);
				}
				// else must be a valid value of zero
			}
			// Note, any non-existant keys will have already been preset to WILDCARD
			if( !strcmp(curr_key, "numReq")){
				pBzd->m_numReq = value64;
			}
			else if( !strcmp(curr_key, "minTemp")){
				pBzd->m_minTemp = value64;
			}
			else if( !strcmp(curr_key, "maxTemp")){
				pBzd->m_maxTemp = value64;
			}
			else if( !strcmp(curr_key, "minHour")){
				pBzd->m_minHour = value64;
			}
			else if( !strcmp(curr_key, "maxHour")){
				pBzd->m_maxHour = value64;
			}
			else{
				g_critical( "Key Lookup Sanity Failure: %s\n", curr_key);
				exit(-1);
			}
		} //  for keys in group

		strncpy( pBzd->m_Method, curr_grp, MAX_GROUPLEN-1 );
		pBzd->m_Method[MAX_GROUPLEN-1] = 0x00;
		strtok(pBzd->m_Method, "@");
		pBzd->m_EndPoint = strtok(NULL, "@");
		if( pBzd->m_EndPoint == (gchar *)WILDCARD ) {
		   g_critical("%s", "Failed to get Method/Endpoint\n");
		   exit(-1);
		}
		pBzd++;
	} //  for groups in keyfile
	g_strfreev(keys);
	g_strfreev(pgGroups);
	g_key_file_free(BizCfgFile);

	LogFile = fopen(LogPath, "a");
	if (LogFile == NULL)
	{
		ci_debug_printf(0, "    Log File (%s) Could not be opened.\n", LogPath);
		exit( -2 );
	}
	hour = tm_struct->tm_hour;
	currday = tm_struct->tm_mday;
	//ci_debug_printf(1, "\n\nCurrent Local Time is %d:%d:%d\n", tm_struct->tm_hour, tm_struct->tm_min, tm_struct->tm_sec);
	ci_debug_printf(1, "    Current local time: %s", asctime(tm_struct));
	WriteLog( 1, LogFile, "    Current Temperature is %d\n", currtemp);
		
	return CI_OK;
}

/*
* This function will be called when the service shutdown
* can be used to release service allocated resources
*/
void msp_close_service()
{
	ci_debug_printf(5, "\n*** msp_close_service::\n");
	if (LogFile) {
		if (MainThread) // huh, this doesn't work, still see 4 of the below msgs:
			WriteLog(0, LogFile, "The MSP Service is Shutting Down...");
		fclose(LogFile);
	}
	ci_object_pool_unregister(MSP_DATA_POOL); // per url_check
	free( pBizRecords );
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
	ci_debug_printf(5, "\n*** msp_init_request_data:: ***\n");
	struct srv_msp_data *mspd = ci_object_pool_alloc(MSP_DATA_POOL);
	memset(&mspd->body, 0, sizeof(struct body_data));
	memset(&mspd->msginfo, 0, sizeof(struct srv_msp_msg_info));
	mspd->isReqmod = 0;
	mspd->maxBodyData = 0;
	mspd->expectedData = 0;
	mspd->eof = 0;
	return mspd;      /*Get from a pool of pre-allocated structs better...... */
}

/*
* This function called after the user request served to release the service data
*	 param data - pointer to the service data returned by msp_init_request_data
*/
void msp_release_request_data(void *data)
{
	ci_debug_printf(5, "\n*** msp_release_request_data:: ***\n");
	/*The data points to the echo_req_data struct we allocated in function echo_init_service */
	struct srv_msp_data *mspd = data;
	if (mspd->body.type) {
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
 */
int msp_preview_handler(char *preview_data, int preview_data_len, ci_request_t * req)
{
	ci_off_t content_len;
	int showHeader = 0;

	//ci_debug_printf(0, "\n*** msp_preview_handler::preview_data_len: %d  ***\n", preview_data_len);
	//ci_debug_printf(3, "\n*** msp_preview_handler:: ***\n");
	MainThread = 1; // TODO: each thread would handle a different connection, needs its own BIZ_DATA struct ...

	//return CI_MOD_CONTINUE;
	// If there is no body data in HTTP encapsulated object but only headers
	//	 respond with Allow204 (no modification required) and terminate the ICAP transaction here
	if (!ci_req_hasbody(req)) {
		ci_debug_printf(0, "msp_preview_handler::no body data, will not process further...\n");
		return CI_ERROR;
	}

	struct srv_msp_data *mspd = ci_service_data(req);
	mspd->maxBodyData = MaxBodyData;
	mspd->isReqmod = 0;

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
	ci_headers_list_t *pHeader = NULL;

	const int REQ_TYPE = ci_req_type(req);
	if (REQ_TYPE == ICAP_REQMOD) {	// Assure there is a soap action (required for soap requests according to according to https://www.w3.org/TR/2000/NOTE-SOAP-20000508 )
		mspd->isReqmod = 1;
		pHeader = ci_http_request_headers(req);
	}
	else {
		pHeader = ci_http_response_headers(req);
	}
	if (!pHeader) {
		ci_debug_printf(0, "msp_preview_handler::ERROR: unable to get http header\n");
		return CI_ERROR; 
	}

	if (REQ_TYPE == ICAP_REQMOD) {	// Assure there is a soap action (required for soap requests according to according to https://www.w3.org/TR/2000/NOTE-SOAP-20000508 )
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
		if (!(soap_action = ci_headers_value(pHeader, "SOAPAction"))) // uses strncasecmp, ignores case....
		{
			ci_debug_printf(0, "ERROR Getting Soap Action.\n");
			return CI_ERROR; // must not be a Multispeak Request
		}
		*/
		;
	}
	else {
		if (showHeader) {
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
	if (content_len <= 0) {
		ci_debug_printf(0, "msp_preview_handler::no Content-Length, will not process\n");
		return CI_ERROR;
	}

	if (content_len > mspd->maxBodyData) {
		ci_debug_printf(0, "msp_preview_handler::content-length=%"PRINTF_OFF_T" > %ld will not process\n", (CAST_OFF_T)content_len, mspd->maxBodyData);
		return CI_ERROR;
	}

	body_data_init(&mspd->body, MEMORY, content_len, NULL);

	/*if we have preview data and we want to proceed with the request processing
	  we should store the preview data. There are cases where all the body
	  data of the encapsulated HTTP object is included in preview data.
	  Use the ci_req_hasalldata macro to identify these cases.
	*/
	if (preview_data_len) {
		ci_debug_printf(0, "msp_preview_handler::preview_data_len\n");
		
		body_data_write(&mspd->body, preview_data, preview_data_len, ci_req_hasalldata(req));
		mspd->eof = ci_req_hasalldata(req);
	}

	return CI_MOD_CONTINUE;
}

/*
* This function will be called if we returned CI_MOD_CONTINUE in
*  msp_check_preview_handler function, after we read all the
* data from the ICAP client.  Called when the ICAP client has sent all its data.
param req - pointer to the related ci_request struct
returns   -  CI_MOD_DONE if all are OK, CI_MOD_ALLOW204 if the ICAP client request supports 204 responses
* and we are not planning to modify anything, or CI_ERROR on errors.
* The service must not return CI_MOD_ALLOW204 if has already send some data to the client, or the
* client does not support allow204 responses. To examine if client supports 204 responses the
* developer should use the ci_req_allow204 macro
*/
int msp_end_of_data_handler(ci_request_t * req)
{
	int icRet = CI_NO_STATUS;
	int msRet = MSP_NO_STATUS;
	const int REQ_TYPE = ci_req_type(req);
	struct srv_msp_data *mspd = ci_service_data(req);

	ci_debug_printf(5, "\n*** msp_end_of_data_handler:: ***\n");

	/*if (mspd->abort) {
		// We had already start sending data....
		mspd->eof = 1;
		return CI_MOD_DONE;
	}*/
	if (mspd->isReqmod) {
		ci_debug_printf(5, "All REQUEST data received, going to process!\n");
		// do sanity check, isReqmod is probably not even needed as can use ci_req_type
		if (REQ_TYPE != ICAP_REQMOD) {
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
	BIZ_DATA *pBizData = GetBusinessRecord(mspd, &ErrRet);
	if (!pBizData)
	{
		if (ErrRet != MSP_OK){
			WriteLog(0, LogFile, "Error Looking up Request Business Record.");
			unlock_data(req);
			return CI_ERROR;
		}
		// 'No Business Rules Defined for Endpoint', allow to send
		unlock_data(req);
		return CI_MOD_ALLOW204;
	}

	if (REQ_TYPE == ICAP_REQMOD) // #define ICAP_REQMOD    0x02
	{
		msRet = handle_request_preview(pBizData);
		if(msRet == MSP_BIZ_VIO)
		{		
			if (!ci_req_sent_data(req)) {
				ci_membuf_t *err_page = generate_error_page(req);
				body_data_init(&mspd->body, ERROR_PAGE, 0, err_page);
			}
			else{
				ci_debug_printf(0, "*** ci_req_ALREADY_sent_data ...\n");
			}
			icRet = CI_MOD_DONE;
		}
		else if (msRet == MSP_ERROR) {
			icRet = CI_ERROR;
		}
		else if (msRet == MSP_OK) {
			icRet = CI_MOD_ALLOW204;
		}
		else {
			ci_debug_printf(0, "***BUG: Unexpected return from: %s: %d\n", "handle_request_preview", msRet);
			icRet = CI_ERROR;
		}
	}
	else if (REQ_TYPE == ICAP_RESPMOD)
	{
		ci_debug_printf(5, "*** handling_response_preview ...\n");
		msRet = handle_response_preview(pBizData);
		if (msRet == MSP_ERROR) {
			icRet = CI_ERROR;
		}
		else if (msRet == MSP_OK) {
			icRet = CI_MOD_ALLOW204;
		}
		else {
			ci_debug_printf(0, "***BUG: Unexpected return from: %s: %d\n", "handle_response_preview", msRet);
			icRet = CI_ERROR;
		}
	}
	else if (REQ_TYPE == ICAP_OPTIONS)
	{
		WriteLog( 0, LogFile, "ICAP OPTIONS: ignoring...");
	}
	else
	{
		//UNKNOWN ICAP METHOD
		WriteLog( 0, LogFile, "INVALID ICAP METHOD (%d) ignoring...", REQ_TYPE);
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
	ci_debug_printf(5, "\n*** msp_io:: ***\n");
	int ret = CI_OK;
	struct srv_msp_data *mspd = ci_service_data(req);

	if( !mspd->body.type ){
		ci_debug_printf(0, "    !mspd->body.type\n");
		// probably 206 response.
		*wlen = CI_EOF;
		return CI_OK;
	}
	//write the data read from icap_client(i.e., Squid) to the mspd->body
	if (rlen && rbuf) {
		if (mspd->body.store.ring == NULL &&
		    (mspd->body.size + *rlen) > mspd->maxBodyData) {
			ci_debug_printf(0, "msp_io::content-length: %" PRIu64 " bigger than maxBodyData: %" PRId64 "\n",
			                (mspd->body.size + *rlen), mspd->maxBodyData);
			ci_debug_printf(0, "TODO: call srv_cf_body_to_ring\n");

			//if (!srv_cf_body_to_ring(&mspd->body))
			    return CI_ERROR;
			//ci_debug_printf(5, "Srv_Content_Filtering Stop buffering data, reverted to ring mode, and sent early response\n");
			/*We will not process body data. More data size than expected.*/
			//mspd->abort = 1;
			//ci_req_unlock_data(req);
		}

		*rlen = body_data_write(&mspd->body, rbuf, *rlen, iseof);
		if (*rlen == CI_ERROR){
			ret = CI_ERROR;
			ci_debug_printf(5, "    rlen && rbuf::CI_ERROR\n");
		}
		else {
			;// msp_dumphex(rbuf, *rlen);
		}
	}
	/*
	else if (iseof) {
	//if (iseof) {
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
	if( /*mspd->body.type &&*/ wbuf && wlen) {
		ci_debug_printf(5, "    mspd->body.type && wbuf && wlen\n");
		*wlen = body_data_read(&mspd->body, wbuf, *wlen);
		if (*wlen == CI_ERROR){
			ci_debug_printf(5, "    *wlen == CI_ERROR\n");
			ret = CI_ERROR;
		}
		else {
			;// msp_dumphex(wbuf, *wlen);
		}
	}
	if( *wlen==0 && mspd->eof==1 )
		*wlen = CI_EOF;

	return ret;
}

/************************** AUXILLIARY ROUTINES ********************************************/

/*
* handle_request_preview
*/
int handle_request_preview(BIZ_DATA *pBizData)
{

	ci_debug_printf(5, "    --->handle_request_preview::\n");

	time_t currtime = time(NULL);
	struct tm *tm_struct = localtime(&currtime);
	hour = tm_struct->tm_hour;
	if (currday != tm_struct->tm_mday) {
		currday = tm_struct->tm_mday;
		pBizData->m_ValidRequestNum = 0;
		pBizData->m_TotalRequestNum = 0;
	}
	pBizData->m_TotalRequestNum++; // TODO: only increment this TOTAL if get a response from the endpoint? - i don't think we want to wait, do it now
	// TODO: handle WILDCARDs for temp and time too
	if ((pBizData->m_numReq != WILDCARD) && (pBizData->m_ValidRequestNum >= pBizData->m_numReq)) {
		WriteLog(1, LogFile, "### REJECTing '%s' request #%d from %s Endpoint on Frequency Violation:\n"
		    "   Only %d requests per day are allowed.",
		    pBizData->m_Method, pBizData->m_TotalRequestNum, pBizData->m_EndPoint, pBizData->m_numReq);
		return MSP_BIZ_VIO;
	}
	else if ((hour>pBizData->m_maxHour) || (hour<pBizData->m_minHour)) {
		WriteLog(1, LogFile, "### REJECTing '%s' request #%d from %s Endpoint on Time Violation:\n"
		    "   These type of requests are only allowed between the hours of %d and %d.",
		    pBizData->m_Method, pBizData->m_TotalRequestNum, pBizData->m_EndPoint, pBizData->m_minHour, pBizData->m_maxHour);
		WriteLog(1, LogFile, "Current Hour is %d\n", hour);
		return MSP_BIZ_VIO;
	}
	else if ((currtemp>pBizData->m_maxTemp) || (currtemp<pBizData->m_minTemp)) {
		WriteLog(1, LogFile, "### REJECTing '%s' request #%d from %s Endpoint on Temperature Violation:\n"
		    "   These type of requests are only allowed when the temperature is between %d and %d degrees.",
		    pBizData->m_Method, pBizData->m_TotalRequestNum, pBizData->m_EndPoint, pBizData->m_minTemp, pBizData->m_maxTemp);
		WriteLog(1, LogFile, "Current Temperature is %d\n", currtemp);
		return MSP_BIZ_VIO;
	}
	else {
		// TODO: don't increment this count until we see a response come back from the endpoint
		//		that way, if endpoint is unreachable, we don't count these as successful requests.
		//pBizData->m_ValidRequestNum++;
		WriteLog(1, LogFile, "*** ACCEPTing %d of %d daily '%s' requests(%d attempts) from '%s' Endpoint ***",
		    pBizData->m_ValidRequestNum+1, pBizData->m_numReq, pBizData->m_Method, pBizData->m_TotalRequestNum, pBizData->m_EndPoint);
		return MSP_OK;
	}
}

/*
* handle_response_preview
*/
int handle_response_preview(BIZ_DATA *pBizData)
{
	ci_debug_printf(5, "    --->handle_response_preview::\n");
	/* TODO: get ip address and lookup the right BIZ_DATA per IP....
	 * ultimately, we'd want to index the src/dest ips to find the BIZ_DATA
	 * then check if the method is part of that connection's BIZ_DATA...
	 */
	//WriteLog(4, LogFile, "got ICAP_RESPMOD, ignoring...");
	
	pBizData->m_ValidRequestNum++;
	WriteLog(1, LogFile, "*** handle_response_preview::ACCEPTED '%s' request %d of %d from '%s' Endpoint ***",
		pBizData->m_Method, pBizData->m_ValidRequestNum, pBizData->m_numReq, pBizData->m_EndPoint);

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
BIZ_DATA *GetBusinessRecord(struct srv_msp_data *mspd, int *pErrRet)
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

	if (showData) {
		if (!mspd->isReqmod) {
			msp_dumphex(buf, mspd->expectedData);
		}
	}
	xmlDoc = xmlParseMemory(buf, mspd->expectedData);
	if (xmlDoc == NULL) {
		ci_debug_printf(0, "XML Document not parsed successfully.\n");
		*pErrRet = MSP_ERROR;
		return NULL;
	}
	root = xmlDocGetRootElement(xmlDoc);
	if (root == NULL) {
		ci_debug_printf(0, "Failed to get XML ROOT\n");
		xmlFreeDoc(xmlDoc);
		*pErrRet = MSP_ERROR;
		return NULL;
	}
	if (xmlStrcmp(root->name, (const xmlChar *)"Envelope")) {
		ci_debug_printf(0, "\ndocument of the wrong type, root node != 'Envelope'\n");
		xmlFreeDoc(xmlDoc);
		*pErrRet = MSP_ERROR;
		return NULL;
	}

	// Initialize msginfo struct
	struct srv_msp_msg_info *pMsgInfo = &mspd->msginfo;
	memset(pMsgInfo, 0x00, sizeof(struct srv_msp_msg_info));

	if (get_method_info(root, pMsgInfo)) // get just what is needed to find the right business rule record
	{
		pMethod = pMsgInfo->method;
		pEndpoint = pMsgInfo->endpoint;
		ci_debug_printf(4, "Namespace is: '%s'\n", pMsgInfo->xmlnspace);
		ci_debug_printf(4, "Method is: '%s'\n", pMethod);
		ci_debug_printf(4, "Endpoint is: '%s'\n", pEndpoint);
		if (*pMsgInfo->xactid != 0x00)
			// MessageID should be unique, not reused by a Request, if we want to 
			// correlate a response to a request, use transactionID
			ci_debug_printf(4, "TransactionID is: '%s'\n", pMsgInfo->xactid);
	}
	else {
		ci_debug_printf(0, "ERROR getting Method info\n");
		xmlFreeDoc(xmlDoc);
		*pErrRet = MSP_ERROR;
		return NULL;
	}

	ci_debug_printf(4, "Current XML Method is: '%s@%s'\n", pMethod, pEndpoint);

	// TODO, find pBizData from IP Addresses (src/dest) ??
	//		we may not need to do that, if each separate connection is handled by a separate
	//		c-icap thread, with it's own copy of BIZ_DATA....

	BIZ_DATA *pBizData = pBizRecords;
	for(i = 0; i < NumBizRecs; i++)
	{
		if( !strcmp( pBizData->m_EndPoint, pEndpoint) )
		{
			if( !strcmp( pBizData->m_Method, pMethod) ){
				ci_debug_printf(4, "Found Business Record for %s@%s:\n", pMethod, pEndpoint );
				break;
			}
			else{
				ci_debug_printf(4, "Checking Business Record for %s@%s:\n",
				                pBizData->m_Method,  pBizData->m_Method);
			}
		}
		pBizData++;
	}
	if( i == NumBizRecs )
	{
		ci_debug_printf(1, "\nNo Business Rules Defined for %s@%s:\n", pMethod, pEndpoint );
		*pErrRet = MSP_OK;
		pBizData = NULL;
	}
	else {
		if (mspd->isReqmod) {
			// while we have the xml parsed into memory, squirrel some info that might be needed 
			// for returning a business rule violation error page
			if( !get_caller_info(root, pMsgInfo) ) // squirrel away some info needed for returning a business rule violation error page
			{
				ci_debug_printf(0, "*** ERROR getting caller information ...\n");
				*pErrRet = MSP_ERROR;
				pBizData = NULL;
			}
			else {
				*pErrRet = MSP_OK;
				pBizData = pBizData;
			}
		}
		else {
			*pErrRet = MSP_OK;
			pBizData = pBizData;
		}
	}

	// freeing BOTH of these cause death later on
	//xmlFree((void *)pMethod);
	xmlFreeDoc(xmlDoc); 

	return pBizData;
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
	if (ci_http_response_headers(req)) {
		ci_http_response_reset_headers(req);
	}
	else {
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
	if (lang) {
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
	if (uc) {
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
	printf("generated uuid=%s\n", uuid_str);

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
	if (uc) {
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
	if (uc) {
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
	if (uc) {
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
	if (uc) {
		if (*uc->msginfo.xactid != 0x00) {
			return snprintf(buf, len, "<tns:transactionID>%s</tns:transactionID>", uc->msginfo.xactid);
		}
		return 0;
	}
	return snprintf(buf, len, "%s", "ERR");
}

//
//////////////
static bool get_method_info(xmlNodePtr root, struct srv_msp_msg_info *pMsgInfo)
{
	xmlNodePtr pReturnedNode = getChildNode(root->children, (const xmlChar *)"Body");
	if (pReturnedNode)
	{
		xmlNodePtr chld_node = pReturnedNode->xmlChildrenNode;
		while (chld_node != NULL)
		{
			if (chld_node->type == XML_ELEMENT_NODE) {
				break;
			}
			chld_node = chld_node->next;
		}
		if (chld_node) {
			strncpy(pMsgInfo->method, (char *)chld_node->name, CI_MAXMETHODLEN);
			if (chld_node->ns) {
				const xmlChar *pNsRef = chld_node->ns->href;
				strncpy(pMsgInfo->xmlnspace, (char *)pNsRef, CI_MAXNSLEN);
				char *p = strrchr((char *)pNsRef, '/');
				if (p) {
					strncpy(pMsgInfo->endpoint, p + 1, CI_MAXENDPOINTLEN);
				}
			}
			xmlNodePtr body_chld = NULL;
			for (body_chld = chld_node->children; body_chld; body_chld = body_chld->next) {
				if (body_chld->type == XML_ELEMENT_NODE) {
					if ((!xmlStrcasecmp(body_chld->name, (const xmlChar *)"transactionID"))) {
						strncpy(pMsgInfo->xactid, (char *)xmlNodeGetContent(body_chld), CI_MAXXACTIDLEN);
						break;
					}
				}
			}
		}
		else {
			printf("Failed to get child node element for '%s'\n", "Body");
		}
	}
	else {
		printf("Failed to get child node '%s' for '%s'\n", "Body", "root");
	}

	if (*pMsgInfo->xmlnspace != 0x00 && *pMsgInfo->method != 0x00 && *pMsgInfo->endpoint != 0x00)
		return true;
	else
		return false;
}

//
//////////////
static bool get_caller_info(xmlNodePtr root, struct srv_msp_msg_info *pMsgInfo)
{
	xmlNodePtr cur_node = NULL;
	xmlNodePtr nxt_node = NULL;
	xmlNodePtr chld_node = NULL;
	int num_needed = 2;
	int num_gotten = 0;
	bool bFound = false;

	for (cur_node = root; cur_node; cur_node = cur_node->next) {
		if (bFound)
			return false;
		if (cur_node->type == XML_ELEMENT_NODE)
		{
			if ((!xmlStrcasecmp(cur_node->name, (const xmlChar *)"Caller")))
			{
				for (chld_node = cur_node->children; chld_node; chld_node = chld_node->next) {
					if ((!xmlStrcasecmp(chld_node->name, (const xmlChar *)"AppName")))
					{
						strncpy(pMsgInfo->appname, (char *)xmlNodeGetContent(chld_node), CI_MAXAPPNAMELEN);
						num_gotten++;
					}
					else if ((!xmlStrcasecmp(chld_node->name, (const xmlChar *)"Company")))
					{
						strncpy(pMsgInfo->company, (char *)xmlNodeGetContent(chld_node), CI_MAXCOMPANYLEN);
						num_gotten++;
					}
					if (num_gotten == num_needed) {
						bFound = true;
						break;
					}
				}
				nxt_node = NULL;
			}
			else {
				nxt_node = cur_node->children;
			}
		}//  for 
		else {
			nxt_node = cur_node->children;
		}
		if (!bFound)
			get_caller_info(nxt_node, pMsgInfo);
	}// for

	if (*pMsgInfo->appname != 0x00 && *pMsgInfo->company != 0x00)
		return true;
	else
		return false;
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
			if (current + i < data + len)
				printf("%02x ",current[i]);
			else
				printf("   ");
		}
		for (i = 0; i < 16; i++)
		{
			if (current + i < data + len)
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
		if (n->type == XML_ELEMENT_NODE)
		{
			if ((!xmlStrcasecmp(n->name, elem)))
			{
				//printf("Found element '%s'\n", elem);
				return n;
			}
			else {
				//printf("Not Found element '%s' @ '%s'\n", elem, n->name);
				pRet = getChildNode(n->next, elem);
				if (pRet)
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

	if (pFile && (loglevel == 0))
	{
		time_t currtime = time(NULL);
		struct tm *tm_struct = localtime(&currtime);
		pStr = asctime(tm_struct);
		// asctime seems to append a <CR> so overwrite it by using len-1
		len = strlen(pStr) - 1;
		strncpy(str, pStr, len);
		strcpy(&str[len], ": ");
		vsnprintf(&str[len + 2], 800 - (len + 2), format, args);
		fprintf(pFile, "\n%s", str);
		fflush(pFile);
		ci_debug_printf(loglevel, "%s\n", &str[len + 1]);
	}
	else {
		vsprintf(str, format, args);
		ci_debug_printf(loglevel, "%s\n", str);
	}

	va_end(args);
	return;
}

