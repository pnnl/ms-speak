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
		2019 - Created By: Cullen Tollbom, from	https://sourceforge.net/projects/c-icap/
		03/23/2019 - Modified By: Carl Miller <carl.miller@pnnl.gov>
		04/01/2019 - CHM: added logging.
		05/13/2019 - CHM: return MS response on business rule violation.
		06/04/2019 - CHM: generalize BizData.
		06/05/2019 - CHM: only increment m_ValidRequestNum upon seeing a response.
-------------------------------------------------------------------------------
	ECAP:  https://www.e-cap.org/
			https://answers.launchpad.net/ecap/+question/238792
			https://answers.launchpad.net/ecap/+faq/2516

 Summary: /home/msspeak/Packages/c_icap-0.5.5/services/msp/srv_msp.c
		to change squid configuration:
			/usr/local/squid/etc/squid.conf
				#
				# Enable and configure the ICAP client in Squid
				#
				icap_enable on
				icap_preview_enable on
				icap_preview_size 1024
				icap_send_client_ip on
				icap_service service_msp_req reqmod_precache icap ://127.0.0.1:1344/msp
				icap_service service_msp_resp respmod_precache icap ://127.0.0.1:1344/msp
				#
				# Define what the squid content adaptation layer class maps
				#
				adaptation_access service_msp_req allow all
				adaptation_access service_msp_resp allow all

			error_directory - /home/msspeak/Packages/c_icap-0.5.5/services/msp/errors
				default error file location:
					/usr/local/squid/share/errors/en
				This directive specifies the location of Squid’s error message files.
				If you want to customize the error messages, you should put them into a nondefault directory.
				Otherwise, they may be overwritten if you run make install in the future


		to build:
			cd /home/msspeak/Packages/c_icap-0.5.5
			automake   (in the case of a fresh install, ./configure.ac has changed, or a ‘make clean’ has been run)
			./configure   # only need do once otherwise
			NOTE: if you run automake, it will replace the Squid.conf file(/usr/local/squid/etc/squid.conf), so
					in that case, you need to replace it with a version that allows only IPV4 addresses and
					also sets port 8080 as a safeport (that version is in the repo @../Multispeaker/Proxy/squid). 
				  if you run automake, it will replace the msp Makefile, so if the required changes to include glib 
					are needed, copy Makefile.msp(@../Multispeaker/Proxy/c_icap/services/msp/) as Makefile afterwards.
					(NOTE: it is best to add the Makefile changes to Makefile.am, to avoid this)
					"no rule to make target 'glib-2.0', needed by 'srv_msp.la'. Stop"

			to modify c-icap configuration:
				/usr/local/etc/c-icap.conf
				these lines must be in c-icap.conf:
					Service msp srv_msp.so
					TemplateDir /usr/local/share/c-icap/templates
				and this file must be present:
					/usr/local/share/c-icap/templates/msp/en-US/MSP_RESPONSE

			if only modifying srv_msp.c after initial install of icap, just do the follwing:
				make
				sudo make install
			if adding a new source file to msp, add it to Makefile.am and 
				run
					automake
					./configure
				then do 
					make
					sudo make install
			NOTES:
				automake uses Makefile.am to generate Makefile.in
				./configure uses Makefile.in to generate Makefile

		to run Squid:
			sudo /usr/local/squid/sbin/squid [& -N -D -d 1 ]
		to run Icap:
			sudo /usr/local/bin/c-icap [ -N -D -d 1 ]
		NOTE:  if the icap machine is rebooted, the directories for the icap lock file will no longer exist,
				  and must be recreated:
					make install (from /home/msspeak/Packages/c_icap-0.5.5)
							OR
				  	sudo mkdir /run/c-icap
				  	sudo mkdir /var/run/c-icap
				NOTE: the icap daemon will create the actual lock file in the directory when started.

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

// prototypes
int msp_init_service(ci_service_xdata_t *, struct ci_server_conf *);
int msp_post_init_service(ci_service_xdata_t *, struct ci_server_conf *);
void msp_close_service();
void *msp_init_request_data(ci_request_t * );
void msp_release_request_data(void *);
int msp_preview_handler(char *, int, ci_request_t *);
int msp_end_of_data_handler(ci_request_t * );
int msp_io(char *, int *, char *, int *, int,	ci_request_t * );

/*
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
	msp_end_of_data_handler,						   // mod_end_of_data_handler: function called when the icap client has sent all the data to the service
	msp_io,                          // mod_service_io: function called to read/send body data from/to icap client.
    NULL,						   // mod_conf_table: config table of the service
    NULL						   // mod_data: This field is not used. Set it to NULL.
};

#define CI_MAXMSGIDLEN 256
#define CI_MAXTIMESTAMPLEN 256
#define CI_MAXAPPNAMELEN 256
#define CI_MAXCOMPANYLEN 256
#define CI_MAXINFOLEN 256 // should be set to the largest of above

#define MSP_NO_STATUS   0
#define MSP_OK          1
#define MSP_BIZ_VIO		2 // business rule violation
#define MSP_ERROR		3

struct srv_msp_msg_info {
	char msgid[CI_MAXMSGIDLEN + 1];
	char timestamp[CI_MAXTIMESTAMPLEN + 1];
	char appname[CI_MAXAPPNAMELEN + 1];
	char company[CI_MAXCOMPANYLEN + 1];
};

/*
The srv_msp_data structure will store the data required to serve an ICAP request.
*/
static int MSP_DATA_POOL = -1;
int EARLY_RESPONSES = 1;

struct srv_msp_data {
	struct body_data body;
	struct srv_msp_msg_info msginfo;
};

/*
RFC 3507                          ICAP                        April 2003
4.8.2  Response

The response from the ICAP server back to the ICAP client(i.e. Squid) may take
one of four forms:
	-  An error indication.
	-  A 204 indicating that the ICAP client's request requires no
		adaptation (see Section 4.6 for limitations of this response).
	-  An encapsulated, adapted version of the ICAP client's request.
	-  An encapsulated HTTP error response.  Note that Request
		Modification requests may only be satisfied with HTTP responses in
		cases when the HTTP response is an error (e.g., 403 Forbidden).
*/
#define MAX_GROUPLEN 200
#define WILDCARD_STR "-1"
#define WILDCARD -1
#define LOG_URL_SIZE 256
#define LOW_BUFF 256

int fmt_srv_msp_msgid(ci_request_t *, char *, int, const char *);
int fmt_srv_msp_timestamp(ci_request_t *, char *, int, const char *);
int fmt_srv_msp_appname(ci_request_t *, char *, int, const char *);
int fmt_srv_msp_company(ci_request_t *, char *, int, const char *);
struct ci_fmt_entry MspFmtTable [] = {
    {"%MSGID", "MessageID", fmt_srv_msp_msgid},
    {"%MSTIME", "TimeStamp", fmt_srv_msp_timestamp},
    {"%MSAPP", "AppName", fmt_srv_msp_appname},
    {"%MSCMPY", "Company", fmt_srv_msp_company},
    { NULL, NULL, NULL}
};

const char delim[2] = "/";
char theCopy [200];
char str[800];

GError *error = NULL;
GKeyFileFlags flags = G_KEY_FILE_NONE;
GKeyFile *BizCfgFile;
//gchar *EndPoint;
//gchar *Method;
gchar *BizFile = "/home/msspeak/BizRules.cfg";
size_t slen;
int currtemp;  // NOTE: can force change of temp by sending CD_Server method other than InitiateConnectDisconnect
int currday;
int hour;
int MainThread = 0;

// note: the order of these is reliant on the order of elements in Keys[]
// ultimately, there should be one of these, and a rule file, for each different
// endpoint ip address....
typedef struct _bizdata {
	int m_numReg;
	int m_minTemp;
	int m_maxTemp;
	int m_minHour;
	int m_maxHour;
	unsigned int m_ValidRequestNum; // NOTE: can force reset to 0 by sending an Endpoint other than CD_Server
	unsigned int m_TotalRequestNum;
	gchar *m_EndPoint;
	gchar *m_Method;
} BIZ_DATA;


// prototypes
int handle_request_preview( ci_request_t *);
int handle_response_preview( ci_request_t *);
int get_msg_info(char *, int , struct srv_msp_msg_info *);
void WriteLog( int, FILE *, const char *, ... );
static ci_membuf_t *generate_error_page(ci_request_t *);
char *GetRetStr(int );
void msp_dumphex(char *, int );
bool find_keyval(char const*, char const*, char, char *, int );
BIZ_DATA * GetBusinessRecord(ci_request_t *, int *);

BIZ_DATA TheBizData={ WILDCARD,WILDCARD,WILDCARD,WILDCARD,WILDCARD,0,0}; // todo: make generic,dynamic and per-connection
FILE *LogFile = NULL;

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

	// Tell to the icap clients that we can support up to 1024 size of preview data
	//ci_service_set_preview(srv_xdata, 0); // not sure why url_check sets this to 0....
	// ... but with it set to 0, am getting 0 bytes of preview data - duh!
	ci_service_set_preview(srv_xdata, 2048);

	unsigned int xops = CI_XCLIENTIP | CI_XSERVERIP;
	ci_service_set_xopts(srv_xdata, xops);// added from url_check

	/*Tell to the icap clients that we support 204 responses*/
	ci_service_enable_204(srv_xdata);
	/*Tell to the icap clients that we support 206 responses, added from url_check*/
	ci_service_enable_206(srv_xdata);

	/*initialize mempools          */
	MSP_DATA_POOL = ci_object_pool_register("srv_msp_data",
		sizeof(struct srv_msp_data));
	if (MSP_DATA_POOL < 0)
		return CI_ERROR;

	/*Tell to the icap clients to send preview data for all files*/
	// comment out for url_check ci_service_set_transfer_preview(srv_xdata, "*"); // "zip, tar"


	//ci_debug_printf(1, "Instantiating Business Rules Key File\n");
	BizCfgFile = g_key_file_new ();
	
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
	const char *LogPath;
	gchar *val;
	gchar MethodGroup[MAX_GROUPLEN];
	gint8  idx;

	ci_debug_printf(3, "\n*** msp_post_init_service::\n");
	ci_debug_printf(1, "    Loading Business Rules from '%s'\n", BizFile);
	
	if (!g_key_file_load_from_file (BizCfgFile, BizFile, flags, &error))
	{
		if( !g_error_matches (error, G_FILE_ERROR, G_FILE_ERROR_NOENT) ){
			ci_debug_printf(0, "    Error loading key file: %s", error->message);
		}
		else{
			ci_debug_printf(0, "    Key File Load Failed.\n");
		}
		return CI_ERROR;
	}
	ci_debug_printf(2, "    Successfully Loaded Key File.\n");

	/*
	* TODO:
	*		eventually we should loop through the entire CfgFile, making a BizData for
	*		each 'MethodGroup' (section) in it...
	*
	*		Also, we would change the editor to store the section as "CD_Server-InitiateConnectDisconnect"
	*		instead of "CD_ServerInitiateConnectDisconnect" so we can parse out the endpoint and method
	*/
	TheBizData.m_EndPoint = "CD_Server";
	TheBizData.m_Method = "InitiateConnectDisconnect";
	//EndPoint = "CD_Server";
	//Method = "InitiateConnectDisconnect";
	ci_debug_printf(1, "    Storing Endpoint Method Rules for %s/%s ...\n", TheBizData.m_EndPoint, TheBizData.m_Method);

	slen = strlen(TheBizData.m_EndPoint);
	if( slen + strlen(TheBizData.m_Method) < MAX_GROUPLEN-1 ){
		strcpy(MethodGroup, TheBizData.m_EndPoint);
		strcat(MethodGroup, TheBizData.m_Method);
	}
	else{
		ci_debug_printf(0, "    Endpoint/Method Size exceeded.\n");
		return CI_ERROR;
	}
	if( !g_key_file_has_group( BizCfgFile, MethodGroup ) )
	{
		ci_debug_printf(0, "    Group '%s' not in cfg file.\n", MethodGroup);
		return CI_ERROR;
	}	
	else
	{
		//ci_debug_printf(0, "Found Group '%s'\n", MethodGroup);
		/*
		 * TODO: we could treat any missing keys as a wildcard to 'allow', i.e.
		 *		if there is no rule for min temp, set the value to -1 and allow any
		 *		minimum temperature, etc.
		 */
		int *pBizValues =(int *)&TheBizData;
		gchar *Keys[] = { "numReq", "minTemp", "maxTemp", "minHour", "maxHour" };
		for( idx = 0; idx<5; idx++ )
		{
			gchar *pKey = Keys[idx];
			val = g_key_file_get_value (BizCfgFile, MethodGroup, pKey, &error);
			if( val == NULL )
			{
				if( g_error_matches (error, G_KEY_FILE_ERROR, G_KEY_FILE_ERROR_KEY_NOT_FOUND) )
				{
					//ci_debug_printf(0, "Key Error While Getting Value for Key '%s': %s\n", pKey, error->message);
					ci_debug_printf(0, "    %s, setting WILDCARD value.", error->message);
					val = WILDCARD_STR;
					error = NULL;
				}
				else
				{
					if( g_error_matches (error, G_KEY_FILE_ERROR, G_KEY_FILE_ERROR_GROUP_NOT_FOUND) )
					{
						ci_debug_printf(0, "    Group Error While Getting Value for Key '%s': %s\n", pKey, error->message);
					}
					else{
						ci_debug_printf(0, "    Unexpected Error(%s) While Getting Value for Key '%s'\n", error->message, pKey);
					}
					return CI_ERROR;
				}
			}
			else
			{
				//ci_debug_printf(0, "'%s': '%s'\n", pKey, val);
				*pBizValues = atoi(val);
				pBizValues++;
			}
		}// end for
		val = g_key_file_get_value (BizCfgFile, "Settings", "LogFile", &error);
		if( val == NULL )
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
					ci_debug_printf(0, "    Group Error While Getting Value for Key '%s': %s\n", "LogFile", error->message);
				}
				else{
					ci_debug_printf(0, "    Unexpected Error(%s) While Getting Value for Key '%s'\n", error->message, "LogFile");
				}
				return CI_ERROR;
			}
		}
		else
		{
			LogPath = val;
		}

		time_t currtime = time(NULL);
		struct tm *tm_struct = localtime(&currtime);
		srand(currtime); 
		//currtemp = (rand() % (90 - 32 + 1)) + 32;
		currtemp = 45;
		
		LogFile = fopen(LogPath, "a");
		if (LogFile == NULL) 
		{ 
			ci_debug_printf(0, "    Log File (%s) Could not be opened.\n", LogPath);
		}
		else{
			WriteLog( 0, LogFile, "    NumReq: %d, MinTemp: %d, MaxTemp: %d, MinHour: %d, MaxHour: %d\n\t Logfile: %s",
					TheBizData.m_numReg,
					TheBizData.m_minTemp,
					TheBizData.m_maxTemp,
					TheBizData.m_minHour,
					TheBizData.m_maxHour,
					LogPath );
		}
	
		TheBizData.m_ValidRequestNum = 0;
		TheBizData.m_TotalRequestNum = 0;
		hour = tm_struct->tm_hour;
		currday = tm_struct->tm_mday;
		//ci_debug_printf(1, "\n\nCurrent Local Time is %d:%d:%d\n", tm_struct->tm_hour, tm_struct->tm_min, tm_struct->tm_sec);
		ci_debug_printf(1, "    Current local time: %s", asctime(tm_struct));
		WriteLog( 1, LogFile, "    Current Temperature is %d\n", currtemp);
	}
		
	return CI_OK;
}

/*
* This function will be called when the service shutdown
* can be used to release service allocated resources
*/
void msp_close_service()
{
	ci_debug_printf(3, "\n*** msp_close_service::\n");
	if (LogFile) {
		if (MainThread) // huh, this doesn't work, still see 4 of the below msgs:
			WriteLog(0, LogFile, "The MSP Service is Shutting Down...");
		fclose(LogFile);
	}
	ci_object_pool_unregister(MSP_DATA_POOL); // per url_check
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
	ci_debug_printf(3, "\n*** msp_init_request_data:: ***\n");
	struct srv_msp_data *mspd = ci_object_pool_alloc(MSP_DATA_POOL);
	memset(&mspd->body, 0, sizeof(struct body_data));
	return mspd;      /*Get from a pool of pre-allocated structs better...... */
}

/*
* This function called after the user request served to release the service data
*	 param data - pointer to the service data returned by msp_init_request_data
*/
void msp_release_request_data(void *data)
{
	ci_debug_printf(3, "\n*** msp_release_request_data:: ***\n");
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
	int icRet = CI_NO_STATUS;
	int msRet = MSP_NO_STATUS;

	ci_debug_printf(3, "\n*** msp_preview_handler:: ***\n");
		
	MainThread = 1; // TODO: each thread would handle a different connection, needs its own BIZ_DATA struct ...

	const int REQ_TYPE = ci_req_type(req);
	//const char * METHOD_TYPE = ci_method_string(REQ_TYPE);
	//ci_debug_printf(1, "    Message Type: %s\n",METHOD_TYPE);

#ifdef _INSPECT_DEEP
	/* Get the content length header */
	content_length = ci_http_content_length(req);
	if ((content_length > 0) && (maxsize > 0) && (content_length >= maxsize)) {
		ci_debug_printf(2, "     No antivir check, content-length upper than maxsize (%" PRINTF_OFF_T " > %d)\n", (CAST_OFF_T)content_length, (int)maxsize);
		return CI_MOD_ALLOW204;
	}

	/* No data, so nothing to scan */
	if (!data || !ci_req_hasbody(req)) {
		ci_debug_printf(2, "     No body data, allow 204\n");
		return CI_MOD_ALLOW204;
	}
#endif
	//identify reqmod or respmod or else
	// it appears that preview_data is the content, not starting with the http header...
	if (REQ_TYPE == ICAP_REQMOD)
	{
		//ci_debug_printf(0, "*** got ICAP_REQMOD:");
		//msp_dumphex(preview_data, preview_data_len);
		msRet = handle_request_preview(req);
		if(msRet == MSP_BIZ_VIO){
			struct srv_msp_data *mspd = ci_service_data(req);
			if (!get_msg_info(preview_data, preview_data_len, &mspd->msginfo)) { /*Unknown method or something else...*/
				ci_debug_printf(4, "    --->Can not get required information to process request. Firstline: %s\n", ci_http_request(req));
				return CI_ERROR;
			}
			ci_membuf_t *err_page = generate_error_page(req);
			body_data_init(&mspd->body, ERROR_PAGE, 0, err_page);

			unlock_data(req);
			ci_debug_printf(4, "        returning %s\n", "CI_MOD_CONTINUE");
			return CI_MOD_CONTINUE;
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
		//ci_debug_printf(0, "*** got ICAP_RESPMOD:");
		//msp_dumphex(preview_data, preview_data_len);

		msRet = handle_response_preview(req);
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
	return icRet;

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
	ci_debug_printf(3, "\n*** msp_end_of_data_handler:: ***\n");
	/*
	printf("Buffer size=%d, Data size=%d\n ",
	((struct membuf *)b)->bufsize,((struct membuf *)b)->endpos);
	*/
	return CI_MOD_DONE;
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
*/
int msp_io(char *wbuf, int *wlen, char *rbuf, int *rlen, int iseof,
            ci_request_t * req)
{
	ci_debug_printf(3, "\n*** msp_io:: ***\n");
	int ret;
	struct srv_msp_data *mspd = ci_service_data(req);

	if (!mspd->body.type) {
		ci_debug_printf(5, "    !mspd->body.type\n");
		// probably 206 response.
		*wlen = CI_EOF;
		return CI_OK;
	}

	ret = CI_OK;

	if (rlen && rbuf) {
		ci_debug_printf(5, "    rlen && rbuf\n");
		
		*rlen = body_data_write(&mspd->body, rbuf, *rlen, iseof);
		if (*rlen == CI_ERROR){
			ret = CI_ERROR;
			ci_debug_printf(5, "    rlen && rbuf::CI_ERROR\n");
		}
		else {
			;// msp_dumphex(rbuf, *rlen);
		}
	}
	else if (iseof){
		ci_debug_printf(5, "    iseof\n");
		body_data_write(&mspd->body, NULL, 0, iseof); /*should return ret = CI_OK*/
	}
	
	if (mspd->body.type && wbuf && wlen) {
		ci_debug_printf(5, "    mspd->body.type && wbuf && wlen\n");
		if (EARLY_RESPONSES || body_data_haseof((&mspd->body))) {
			ci_debug_printf(5, "    EARLY_RESPONSES\n");
			*wlen = body_data_read(&mspd->body, wbuf, *wlen);
			if (*wlen == CI_ERROR){
				ci_debug_printf(5, "    *wlen == CI_ERROR\n");
				ret = CI_ERROR;
			}
			else {
				;// msp_dumphex(wbuf, *wlen);
			}
		}
		else {
			ci_debug_printf(5, "    Does not allow early responses, wait for eof before send data\n");
			*wlen = 0;
		}
	}
	else {
		ci_debug_printf(5, "    returning %s\n", GetRetStr(ret));

	}
	return ret;
}

/************************** AUXILLIARY ROUTINES ********************************************/

/*
* handle_request_preview
*/
int handle_request_preview(ci_request_t * req)
{
	int ErrRet;

	ci_debug_printf(4, "    --->handle_request_preview::\n");
	BIZ_DATA *pBizData = GetBusinessRecord(req, &ErrRet);
	if (!pBizData)
	{
		if( ErrRet != MSP_OK )
			WriteLog(0, LogFile, "Error Looking up Request Business Record.");
		return ErrRet;
	}

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
	if ((pBizData->m_numReg != WILDCARD) && (pBizData->m_ValidRequestNum >= pBizData->m_numReg)) {
		WriteLog(1, LogFile, "### REJECTing '%s' request #%d from %s Endpoint on Frequency Violation:\n"
		    "   Only %d requests per day are allowed.",
		    pBizData->m_Method, pBizData->m_TotalRequestNum, pBizData->m_EndPoint, pBizData->m_numReg);
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
		    pBizData->m_ValidRequestNum+1, pBizData->m_numReg, pBizData->m_Method, pBizData->m_TotalRequestNum, pBizData->m_EndPoint);
		return MSP_OK;
	}
}

/*
* handle_response_preview
*/
int handle_response_preview(ci_request_t * req)
{
	int ErrRet;
	ci_debug_printf(4, "    --->handle_response_preview::\n");
	/* TODO: get ip address and lookup the right BIZ_DATA per IP....
	 * ultimately, we'd want to index the src/dest ips to find the BIZ_DATA
	 * then check if the method is part of that connection's BIZ_DATA...
	 */
	//WriteLog(4, LogFile, "got ICAP_RESPMOD, ignoring...");
	
	BIZ_DATA *pBizData = GetBusinessRecord(req, &ErrRet);
	if (!pBizData)
	{
		if( ErrRet != MSP_OK )
			WriteLog(0, LogFile, "Error Looking up Response Business Record.");
		return ErrRet;
	}
	pBizData->m_ValidRequestNum++;
	WriteLog(1, LogFile, "*** ACCEPTED '%s' request %d of %d from '%s' Endpoint ***",
		pBizData->m_Method, pBizData->m_ValidRequestNum, pBizData->m_numReg, pBizData->m_EndPoint);

	return MSP_OK; // always pass the response on to client;
}

/*
* GetBusinessRecord
*/
BIZ_DATA * GetBusinessRecord(ci_request_t *req, int *pErrRet)
{
	// Extract the HTTP header from the request/response
	ci_headers_list_t *pHeader = NULL;
	if (!(pHeader = ci_http_response_headers(req))) {
		/* Then maybe is a reqmod request, try to get request headers */
		if (!(pHeader = ci_http_request_headers(req))){
			ci_debug_printf(0, "GetBusinessRecord::ERROR Getting http_headers\n");
			*pErrRet = MSP_ERROR;
			return NULL;
		}
	}
	//char buf[1000];
	//size_t len = ci_headers_pack_to_buffer(pHeader, buf, 1000);
	//msp_dumphex(buf, len);

	////////// TEST //////////////////////////////////////////
	// return &TheBizData;
	////////// TEST //////////////////////////////////////////

	/* Get the soap action */
	const char *soap_action;
	if (!(soap_action = ci_headers_value(pHeader, "SOAPAction")))
	{
		ci_debug_printf(0, "ERROR Getting Soap Action.\n");
		*pErrRet = MSP_ERROR;
		return NULL;
	}
	// SOAPAction: http://www.multispeak.org/V5.0/wsdl/CD_Server/InitiateConnectDisconnect
	char *ep, *currmethod;
	char *wem = strstr(soap_action, "wsdl/");
	if (wem != NULL) {
		strcpy(theCopy, wem);
		ep = strtok(theCopy, delim);// consume 'wsdl'
		ep = strtok(NULL, delim);
		currmethod = strtok(NULL, delim);
		//ci_debug_printf( 1, "Got '%s' method from %s Endpoint.\n", currmethod, ep);
	}
	else {
		ci_debug_printf(0, "ERROR Getting Soap Action\n");
		*pErrRet = MSP_ERROR;
		return NULL;
	}

	// TODO, find pBizData from IP Addresses (src/dest)
	BIZ_DATA *pBizData = &TheBizData;
	// TODO: for set of BIZ_DATA for a give IP pair, find the
	//		one for our Endpoint / Method
	gchar *EndPoint = pBizData->m_EndPoint;
	gchar *Method   = pBizData->m_Method;
	if (strcmp(EndPoint, ep) != 0) {
		ci_debug_printf(0, "No Business Rules Defined for Endpoint '%s', allowing....\n", ep);
		//TheBizData.m_ValidRequestNum = 0;
		//ci_debug_printf(1, "Reset Number of Requests Received so far to 0.\n");
		*pErrRet = MSP_OK;
		pBizData = NULL;
	}
	else {
		if (strcmp(Method, currmethod) != 0) {
			ci_debug_printf(0, "No Business Rules Defined for Method '%s', allowing....\n", currmethod);
			//currtemp = (rand() % (90 - 32 + 1)) + 32;
			//currtemp = 55;
			//ci_debug_printf(1, "Current Temperature is %d\n", currtemp);
			*pErrRet = MSP_OK;
			pBizData = NULL;
		}
		*pErrRet = MSP_OK;
		pBizData = pBizData;
	}
	return pBizData;
}

/*
* generate template_page, /usr/share/c_icap/templates/msp/en/MSP_RESPONSE
* look for TemplateDir /usr/local/share/c_icap/templates/ in config file
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
	ci_http_response_add_header(req, "HTTP/1.0 403 Forbidden"); /*Send an 403 Forbidden http responce to web client */
	ci_http_response_add_header(req, "Server: C-ICAP");
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
 * fmt_srv_msp_msgid - handle %MSGID format specifier
 */
int fmt_srv_msp_msgid(ci_request_t *req, char *buf, int len, const char *param)
{
	ci_debug_printf(5, "*** fmt_srv_msp_msgid ***\n");
	struct srv_msp_data *uc = ci_service_data(req);
	return snprintf(buf, len, "%s", uc->msginfo.msgid);
}

/*
 * fmt_srv_msp_timestamp - handle %MSTIME format specifier
 */
int fmt_srv_msp_timestamp(ci_request_t *req, char *buf, int len, const char *param)
{
	ci_debug_printf(5, "*** fmt_srv_msp_timestamp ***\n");
	struct srv_msp_data *uc = ci_service_data(req);
	return snprintf(buf, len, "%s", uc->msginfo.timestamp);
}

/*
 * fmt_srv_msp_appname - handle %MSAPP format specifier
 */
int fmt_srv_msp_appname(ci_request_t *req, char *buf, int len, const char *param)
{
	ci_debug_printf(5, "*** fmt_srv_msp_appname ***\n");
	struct srv_msp_data *uc = ci_service_data(req);
	return snprintf(buf, len, "%s", uc->msginfo.appname);
}

/*
 * fmt_srv_msp_company - handle %MSCMPY format specifier
 */
int fmt_srv_msp_company(ci_request_t *req, char *buf, int len, const char *param)
{
	ci_debug_printf(5, "*** fmt_srv_msp_company ***\n");
	struct srv_msp_data *uc = ci_service_data(req);
	return snprintf(buf, len, "%s", uc->msginfo.company);
}

int get_msg_info(char *preview_data, int preview_data_len, struct srv_msp_msg_info *msginfo)
{
	ci_debug_printf(4, "        --->get_msg_info::\n");

	/*Initialize msginfo struct*/
	memset(msginfo->msgid, 0x00, sizeof(msginfo->msgid) );
	memset(msginfo->timestamp, 0x00, sizeof(msginfo->timestamp) );
	memset(msginfo->appname, 0x00, sizeof(msginfo->appname) );
	memset(msginfo->company, 0x00, sizeof(msginfo->company) );

	char* keys[4] = { "MessageID=\"", "TimeStamp=\"", ":AppName>", ":Company>" };
	char  terms[4] = { '\"', '\"', '<', '<' };
	char term;
	char* key;

	preview_data[preview_data_len - 1] = 0x00;// make into a null-terminated string
	int i = 0;
	key = keys[i];
	term = terms[i++];
	bool found = find_keyval(preview_data, key, term, msginfo->msgid, CI_MAXMSGIDLEN);
	if(found)
	{
		ci_debug_printf(3, "***  the value of keyword '%s' is '%s'\n", key, msginfo->msgid);
	}
	else
	{
		ci_debug_printf(0, "***  did not find next word after '%s' terminated with '%c'\n", key, term);
		strncpy(msginfo->msgid, "----", CI_MAXMSGIDLEN);
	}

	key = keys[i];
	term = terms[i++];
	found = find_keyval(preview_data, key, term, msginfo->timestamp, CI_MAXTIMESTAMPLEN);
	if (found)
	{
		ci_debug_printf(3, "***  the value of keyword '%s' is '%s'\n", key, msginfo->timestamp);
	}
	else
	{
		ci_debug_printf(0, "***  did not find next word after '%s' terminated with '%c'\n", key, term);
		strncpy(msginfo->timestamp, "----", CI_MAXTIMESTAMPLEN);
	}

	key = keys[i];
	term = terms[i++];
	found = find_keyval(preview_data, key, term, msginfo->appname, CI_MAXAPPNAMELEN);
	if (found)
	{
		ci_debug_printf(3, "***  the value of keyword '%s' is '%s'\n", key, msginfo->appname);
	}
	else
	{
		ci_debug_printf(0, "***  did not find next word after '%s' terminated with '%c'\n", key, term);
		strncpy(msginfo->appname, "----", CI_MAXAPPNAMELEN);
	}

	key = keys[i];
	term = terms[i++];
	found = find_keyval(preview_data, key, term, msginfo->company, CI_MAXCOMPANYLEN);
	if (found)
	{
		ci_debug_printf(3, "***  the value of keyword '%s' is '%s'\n", key, msginfo->company);
	}
	else
	{
		ci_debug_printf(0, "***  did not find next word after '%s' terminated with '%c'\n", key, term);
		strncpy(msginfo->company, "----", CI_MAXCOMPANYLEN);
	}
	return 1;
}

bool find_keyval(char const *strbuf, char const *substr, char terminator, char *result, int reslen)
{

	bool found_nxt = false;

	if(!strbuf)
	{
		printf("ERROR: empty buffer passed.\n");
		return NULL;
	}
	if(!result)
	{
		printf("ERROR: empty result buffer passed.\n");
		return NULL;
	}
	if(!substr)
	{
		printf("ERROR: NULL string passed.\n");
		return NULL;
	}
	if(strlen(substr) == 0 )
	{
		printf("ERROR: empty string passed.\n");
		return NULL;
	}

	char* pos = strstr(strbuf, substr);
	if(pos)
	{
		//printf("-->found the string '%s' in '%s' at position: %ld\n", substr, strbuf, pos - strbuf);
		;//printf("-->found the string '%s' at position: %ld\n", substr, pos - strbuf);
	}
	else
	{
		//printf("-->the string '%s' was not found\n", substr);
		return pos;
	}
	// run through found string until find the terminator
	int sublen = strlen(substr);
	int remaining_len = strlen(strbuf) - (pos - strbuf) - sublen;
	pos += sublen;
	char const* start=pos;
	//printf("-->searching for next word in '%s', len %d\n", pos, remaining_len);
	for( int i=0; i<remaining_len; i++ )
	{
		//printf("-->comparing terminator '%c' to '%c' ...\n", terminator, *pos);
		if( *pos == terminator )
		{
			if( i != 0 ) // case first str terminated with same terminator as sought string
			{
				int cpylen = pos - start;
				//printf("Found it.\n");
				if (cpylen > reslen)
					cpylen = reslen;
				memcpy(result, start, cpylen);
				found_nxt = true;
				break;
			}
			else{
				start +=1;
			}
		}
		pos +=1;
	}
	return found_nxt;
}

char *GetRetStr(int iRet) {
	switch (iRet)
	{
		case CI_MOD_NOT_READY:
			return "CI_MOD_NOT_READY";
		case CI_MOD_DONE:
			return "CI_MOD_DONE";
		case CI_MOD_CONTINUE:
			return "CI_MOD_CONTINUE";
		case CI_MOD_ALLOW204:
			return "CI_MOD_ALLOW204";
		case CI_MOD_ALLOW206:
			return "CI_MOD_ALLOW206";
		case CI_MOD_ERROR:
			return "CI_MOD_ERROR";
		default:
			return "ERROR: INVALID TYPE";
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

