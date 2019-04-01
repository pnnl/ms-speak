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
//-------------------------------------------------------------------------------
//	History
//		2019 - Created By: Cullen Tollbom, from	https://sourceforge.net/projects/c-icap/
//		03/23/2019 - Modified By: Carl Miller <carl.miller@pnnl.gov>
//-------------------------------------------------------------------------------
// Summary: srv_msp.c
//-------------------------------------------------------------------------------

#include "common.h"
#include "c-icap.h"
#include "service.h"
#include "header.h"
#include "body.h"
#include "simple_api.h"
#include "debug.h"

#include <stdio.h>
#include <stdlib.h> 
#include <string.h>
#include <ctype.h>
#include <glib.h>
#include <glib/gprintf.h>
#include <time.h>

int msp_init_service(ci_service_xdata_t *, struct ci_server_conf *);
int msp_post_init_service(ci_service_xdata_t *, struct ci_server_conf *);
void msp_close_service();
void *msp_init_request_data(ci_request_t * );
void msp_release_request_data(void *);
int msp_check_preview_handler(char *, int, ci_request_t *);
int msp_end_of_data_handler(ci_request_t * );
int msp_io(char *, int *, char *, int *, int,	ci_request_t * );

/*
 * ICAP defines three methods:
	REQMOD - for Request Modification
	RESPMOD - for Response Modification
	OPTIONS - used by the ICAP client to retrieve
				configuration information from the ICAP server.

	ICAP error codes that differ from their HTTP counterparts are:
	100 - Continue after ICAP Preview
	204 - No modifications needed

	encapsulated sections may be the headers or bodies of HTTP messages.
	Examples of legal Encapsulated headers:
		 REQMOD request: This encapsulated HTTP request’s headers start
		 at offset 0; the HTTP request body (e.g., in a POST) starts
		 at 412.
		Encapsulated: req-hdr=0, req-body=412


	ICAP REQMOD or RESPMOD requests sent by the ICAP client to the ICAP
	server may include a "preview". This feature allows an ICAP server
	to see the beginning of a transaction, then decide if it wants to
	opt-out of the transaction early instead of receiving the remainder
	of the request message.  ICAP servers SHOULD use the OPTIONS method
	to specify how many bytes of preview are needed for a particular ICAP
	application on a per-resource basis.

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

	#define CI_NO_STATUS   0
	#define CI_OK          1
	#define CI_NEEDS_MORE  2
	#define CI_ERROR       -1
	#define CI_EOF         -2

	Request Modification Example - ICAP Request
	----------------------------------------------------------------
	REQMOD icap://icap-server.net/server?arg=87 ICAP/1.0
	Host: icap-server.net
	Encapsulated: req-hdr=0, req-body=147

	POST /origin-resource/form.pl HTTP/1.1
	Host: www.origin-server.com
	Accept: text/html, text/plain
	Accept-Encoding: compress
	Pragma: no-cache
	1e
	I am posting this information.
	0
	----------------------------------------------------------------
	Request Modification Example - ICAP Response
	----------------------------------------------------------------
	ICAP/1.0 200 OK
	Date: Mon, 10 Jan 2000 09:55:21 GMT
	Server: ICAP-Server-Software/1.0
	Connection: close
	ISTag: "W3E4R7U9-L2E4-2"
	Encapsulated: req-hdr=0, req-body=244

	POST /origin-resource/form.pl HTTP/1.1
	Host: www.origin-server.com
	Via: 1.0 icap-server.net (ICAP Example ReqMod Service 1.1)
	Accept: text/html, text/plain, image/gif
	Accept-Encoding: gzip, compress
	Pragma: no-cache
	Content-Length: 45
	2d
	I am posting this information.
	0
	ICAP powered!
	----------------------------------------------------------------

	MS Msg:

	*** HTTP Header ***
	POST / HTTP/1.1
	Accept: application / soap + xml, application / dime, multipart / related, text/<sp>*
	Host: 127.0.0.1:8888
	Content-Type: text/xml;charset=utf-8
	SOAPAction: http://www.multispeak.org/V5.0/wsdl/CD_Server/InitiateConnectDisconnect
	Content-Length: 2506
	Connection: Keep-Alive
	Accept-Encoding: gzip, deflate
	Accept-Language: en-US,*
	User-Agent: Mozilla/5.0

	*** Message Content ***

	have squid return custom page:
	Create a page at /usr/local/squid/share/errors/templates/ERR_ANY_NAME. Then add following line at the end of squid.conf:
	deny_info ERR_ANY_NAME clamav_service_req
	The clamav_service_req is same as given in ecap_service directive and ERR_ANY_NAME is a custom page to display.

 */

/*
 * To implement a service, one needs to implement the member functions of this struct. These functions
 * will be called by c-icap as follows:
 *   - New request arrives for this service  ->  msp_init_request_data is called
 *   - The icap client sends preview data -> msp_check_preview_handler is called.
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
    ICAP_REQMOD,				   // mod_type: service implements only and request modification
    msp_init_service,              // mod_init_service: Pointer to the function called when the service is loaded.
    msp_post_init_service, 		   // mod_post_init_service: Pointer to the function which is called after c-icap
                                   // is initialized, but before it starts serving requests.
    msp_close_service,             // mod_close_service: Called when c-icap server shuts down.
    NULL,      // mod_init_request_data: Pointer to the function called when a new request for
                                   // this services arrives at the c-icap server.
    NULL,      // mod_release_request_data: Pointer to the function which releases the service data.
    msp_check_preview_handler,     // mod_check_preview_handler: Pointer to the function which is used to preview the ICAP client request
    NULL,      // mod_end_of_data_handler: Pointer to the function called when the icap client has send all the data to the service
    NULL,                          // mod_service_io: Pointer to the function called to read/send body data from/to icap client.
    NULL,						   // mod_conf_table: Pointer to the config table of the service
    NULL						   // mod_data: This field is not used. Set it to NULL.
};

#define MAX_GROUPLEN 200
#define WILDCARD_STR "-1"
#define WILDCARD -1

const char delim[2] = "/";
char theCopy [200];

GError *error = NULL;
GKeyFileFlags flags = G_KEY_FILE_NONE;
GKeyFile *BizCfgFile;
gchar *EndPoint;
gchar *Method;
gchar MethodGroup[MAX_GROUPLEN];
gboolean bRetVal;

// note: the order of these is assumed during assignment to BIZ_DATA....
gchar *Keys[] = { "numReq", "minTemp", "maxTemp", "minHour", "maxHour" };
gint8  NumKeys = sizeof(Keys)/sizeof(Keys[0]);

gint8  idx;
gchar *BizFile = "/home/msspeak/BizRules.cfg";
size_t slen;
int	  *pBizdata;
int currtemp;  // NOTE: can force change of temp by sending CD_Server method other than InitiateConnectDisconnect
int currday;
int hour;

// note: the order of these is reliant on the order of elements in Keys[]
typedef struct _bizdata {
	int m_numReg;
	int m_minTemp;
	int m_maxTemp;
	int m_minHour;
	int m_maxHour;
	unsigned int m_RequestNo; // NOTE: can force reset to 0 by sending an Endpoint other than CD_Server
} BIZ_DATA; 

BIZ_DATA TheBizData; // todo: make generic,dynamic

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
	ci_debug_printf(0, "Initializing msp module...\n");

	// Tell to the icap clients that we can support up to 1024 size of preview data
	ci_service_set_preview(srv_xdata, 1024);

	/*Tell to the icap clients that we support 204 responses*/
	ci_service_enable_204(srv_xdata);

	/*Tell to the icap clients to send preview data for all files*/
	ci_service_set_transfer_preview(srv_xdata, "*"); // "zip, tar"
	
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
int msp_post_init_service(ci_service_xdata_t * srv_xdata,
                    struct ci_server_conf *server_conf)
{
	ci_debug_printf(2, "msp_post_init_service()\n");
	ci_debug_printf(1, "Loading Business Rules from '%s'\n", BizFile);
	
	if (!g_key_file_load_from_file (BizCfgFile, BizFile, flags, &error))
	{
		if( !g_error_matches (error, G_FILE_ERROR, G_FILE_ERROR_NOENT) ){
			ci_debug_printf(0, "Error loading key file: %s", error->message);
		}
		else{
			ci_debug_printf(0, "Key File Load Failed.\n");
		}
		return CI_ERROR;
	}
	ci_debug_printf(2, "Successfully Loaded Key File.\n");
	EndPoint = "CD_Server";
	Method = "InitiateConnectDisconnect";

	ci_debug_printf(1, "Storing Endpoint Method Rules for %s/%s ...\n", EndPoint,Method);


	slen = strlen(EndPoint);
	if( slen + strlen(Method) < MAX_GROUPLEN-2 ){
		strcpy(MethodGroup, EndPoint);
		MethodGroup[slen] = '_';
		MethodGroup[slen+1] = 0x00;
		strcat(MethodGroup, Method);
	}
	else{
		ci_debug_printf(0, "Endpoint/Method Size exceeded.\n");
		return CI_ERROR;
	}
	if( !g_key_file_has_group( BizCfgFile, MethodGroup ) )
	{
		ci_debug_printf(0, "Group '%s' not in cfg file.\n", MethodGroup);
		return CI_ERROR;
	}	
	else
	{
		//ci_debug_printf(1, "Found Group '%s'\n", MethodGroup);
		/*
		 * TODO: we could treat any missing keys as a wildcard to 'allow', i.e.
		 *		if there is no rule for min temp, set the value to -1 and allow any
		 *		minimum temperature, etc.
		 */
		pBizdata =(int *)&TheBizData;
		for( idx = 0; idx<NumKeys; idx++ )
		{
			gchar *pKey = Keys[idx];
			gchar *val = g_key_file_get_value (BizCfgFile, MethodGroup, pKey, &error);
			if( val == NULL )
			{
				if( g_error_matches (error, G_KEY_FILE_ERROR, G_KEY_FILE_ERROR_KEY_NOT_FOUND) )
				{
					//ci_debug_printf(0, "Key Error While Getting Value for Key '%s': %s\n", pKey, error->message);
					ci_debug_printf(0, "%s, setting WILDCARD value.", error->message);
					val = WILDCARD_STR;
					error = NULL;
				}
				else
				{
					if( g_error_matches (error, G_KEY_FILE_ERROR, G_KEY_FILE_ERROR_GROUP_NOT_FOUND) )
					{
						ci_debug_printf(0, "Group Error While Getting Value for Key '%s': %s\n", pKey, error->message);
					}
					else{
						ci_debug_printf(0, "Unexpected Error(%s) While Getting Value for Key '%s'\n", error->message, pKey);
					}
					return CI_ERROR;
				}
			}
			else
			{
				//ci_debug_printf(0, "'%s': '%s'\n", pKey, val);
				*pBizdata = atoi(val);
				pBizdata++;
			}
		}// end for
		ci_debug_printf(1, "   NumReq: %d, MinTemp: %d, MaxTemp: %d, MinHour: %d, MaxHour: %d\n",
								TheBizData.m_numReg,
								TheBizData.m_minTemp,
								TheBizData.m_maxTemp,
								TheBizData.m_minHour,
								TheBizData.m_maxHour );
		TheBizData.m_RequestNo = 0;
		time_t currtime = time(NULL);
		struct tm *tm_struct = localtime(&currtime);
		hour = tm_struct->tm_hour;
		currday = tm_struct->tm_mday;
		//ci_debug_printf(1, "\nCurrent Hour is %d\n", hour);
		ci_debug_printf(1, "\n\nCurrent Local Time is %d:%d:%d\n", tm_struct->tm_hour, tm_struct->tm_min, tm_struct->tm_sec);
		srand(currtime); 
		currtemp = (rand() % (90 - 32 + 1)) + 32;
		ci_debug_printf(1, "Current Temperature is %d\n", currtemp);
	}
		
	return CI_OK;
}

/*
 * If the client supports preview, sends some data for examination.
 * The service using this function will decide if the client request must processed so the client
 * must send more data or no modification/processing needed so the request ends here.
		 param preview_data - Pointer to the preview data
		 param preview_data_len - The size of the preview data
		 param req - pointer to the related ci_request struct
		 returns   - CI_MOD_CONTINUE if the client must send more data, CI_MOD_ALLOW204
 *		if the service doesnot want to modify anything, or CI_ERROR on errors.
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
 */
int msp_check_preview_handler(char *preview_data, int preview_data_len, ci_request_t * req)
{
	ci_debug_printf(4,"Call @ msp_check_preview_handler().\n");

	const int REQ_TYPE = ci_req_type(req);
	//const char * METHOD_TYPE = ci_method_string(REQ_TYPE);
	//ci_debug_printf(1, "Message Type: %s\n",METHOD_TYPE);

	//identify reqmod or respmod or else
	if (REQ_TYPE == ICAP_REQMOD)
	{
		ci_headers_list_t *req_header = NULL;
		ci_debug_printf(3, "got ICAP_REQMOD.\n");
		// Extract the HTTP header from the request
		if( (req_header = ci_http_request_headers(req)) != NULL ){

			/* Get the content length header
			ci_off_t content_len = ci_http_content_length(req);
			if( content_len < 0 )
			{
				ci_debug_printf( 0, "ERROR Getting Content-Length.\n" );
				return CI_ERROR;
			}
			ci_debug_printf(2, "Content-Length: %ld\n", content_len);

			// Get the content type header
			const char *content_type;
			if( !(content_type = ci_headers_value(req_header, "Content-Type")))
			{
				ci_debug_printf( 0, "ERROR Getting Content-Type.\n" );
				return CI_ERROR;
			}
			ci_debug_printf(2, "Content-Type: %s\n", content_type);

			// Get the request line (e.g "GET /index.html HTTP 1.0")
			const char *req_line;
			if( !(req_line = ci_http_request(req)))
			{
				ci_debug_printf( 0, "ERROR Getting Request Line.\n" );
				return CI_ERROR;
			}
			ci_debug_printf(2, "Request Line: %s\n", req_line);
			*/
			/* Get the soap action */
			const char *soap_action;
			if( !(soap_action = ci_headers_value(req_header, "SOAPAction")))
			{
				ci_debug_printf( 0, "ERROR Getting Soap Action.\n" );
				return CI_ERROR;
			}

			char *ep, *currmethod;
			char *wem = strstr(soap_action, "wsdl/");
			if( wem != NULL ){
				strcpy (theCopy, wem);
				ep = strtok(theCopy, delim);// consume 'wsdl'
				ep = strtok(NULL,delim);
				currmethod = strtok(NULL, delim);
				//ci_debug_printf( 1, "Got '%s' method from %s Endpoint.\n", currmethod, ep);
			}
			else{
				ci_debug_printf( 0, "ERROR Getting Soap Action\n") ;			
				return CI_ERROR;
			}
			
    		if( strcmp(EndPoint, ep) != 0 ){
				ci_debug_printf( 0, "No Business Rules Defined for Endpoint '%s', allowing....\n", ep);
				TheBizData.m_RequestNo = 0;		
				ci_debug_printf(1, "Reset Number of Requests Received so far to 0.\n");
				return CI_MOD_ALLOW204;
    		}
    		else{
		 		if( strcmp(Method, currmethod) != 0 ){
					ci_debug_printf( 0, "No Business Rules Defined for Method '%s', allowing....\n", currmethod);			
					currtemp = (rand() % (90 - 32 + 1)) + 32;
					ci_debug_printf(1, "Current Temperature is %d\n", currtemp);
					return CI_MOD_ALLOW204;
				}
	   		}
	   		time_t currtime = time(NULL);
			struct tm *tm_struct = localtime(&currtime);
			hour = tm_struct->tm_hour;
			if( currday != tm_struct->tm_mday ){
				currday = tm_struct->tm_mday;
				TheBizData.m_RequestNo = 0;
			}
			else{
				TheBizData.m_RequestNo++;
			}
			// TODO: handle WILDCARDs for temp and time too
			if(	(TheBizData.m_numReg != WILDCARD) && (TheBizData.m_RequestNo > TheBizData.m_numReg) ){
				ci_debug_printf( 0, "### REJECTing '%s' request #%d from %s Endpoint on Frequency Violation:\n", 
								currmethod, TheBizData.m_RequestNo, ep);
				ci_debug_printf( 0, "   Only %d requests per day are allowed.\n", TheBizData.m_numReg);
				/*
				 * all user-defined headers MUST follow the "X-" naming convention ("X-Extension-Header: Foo").
				 * ci_http_response_create(req, 1, 1);
				 * ci_http_response_add_header(req, "HTTP/1.1 307 Temporary Redirect");
				 * ci_http_response_add_header(req, "Server: C-ICAP");
				 * ci_http_response_add_header(req, "Connection: close");
				 * ci_http_response_add_header(req, "Content-Type: text/html");
				 * ci_http_response_add_header(req, "Content-Language: en");
				 * 
				 * 	snprintf(buf, LOW_BUFF, "X-Infection-Found: Type=0; Resolution=2; Threat=%s;", (malware[0] != '\0') ? malware : "Unknown virus");
				 * 	buf[sizeof(buf)-1] = '\0';
				 * 	ci_icap_add_xheader(req, buf);
				 * 	ci_http_request_add_header(req, buf);
				 *  ci_icap_add_xheader(req, "X-Extension-Header: FooBar");	
				 *  ci_http_request_add_header(req, "X-Extension-Header: Bar");	
				*/
				return CI_ERROR; // CI_MOD_DONE
			}
			else if( (hour>TheBizData.m_maxHour) || (hour<TheBizData.m_minHour) ){
				ci_debug_printf( 0, "### REJECTing '%s' request #%d from %s Endpoint on Time Violation:\n",
						currmethod, TheBizData.m_RequestNo, ep) ;
				ci_debug_printf( 0, "   These type of requests are only allowed between the hours of %d and %d.\n",
								TheBizData.m_minHour, TheBizData.m_maxHour);
				ci_debug_printf(1, "\nCurrent Hour is %d\n", hour);
				return CI_ERROR;
			}
			else if( (currtemp>TheBizData.m_maxTemp) || (currtemp<TheBizData.m_minTemp) ){
				ci_debug_printf( 0, "### REJECTing '%s' request #%d from %s Endpoint on Temperature Violation:\n", 
							currmethod, TheBizData.m_RequestNo, ep) ;
				ci_debug_printf( 0, "   These type of requests are only allowed when the temperature is between %d and %d degrees.\n",
								TheBizData.m_minTemp, TheBizData.m_maxTemp);
				ci_debug_printf(1, "Current Temperature is %d\n", currtemp);
				return CI_ERROR;
			}
			else{
				ci_debug_printf( 0, "*** ACCEPTing '%s' request #%d from %s Endpoint ***\n", 
								currmethod, TheBizData.m_RequestNo, ep);			
				return CI_MOD_ALLOW204;
			}	
		}
		else{
			ci_debug_printf( 0, "WARNING bad http header, can not get URL, Content-Type and Content-Length.\n" );
			return CI_ERROR;
		}
	}
	else if (REQ_TYPE == ICAP_RESPMOD)
	{
		ci_debug_printf(0, "got ICAP_RESPMOD, ignoring...\n");
	}
	else if (REQ_TYPE == ICAP_OPTIONS)
	{
		ci_debug_printf(0, "ICAP OPTIONS: ignoring...");
	}
	else
	{
		//UNKNOWN ICAP METHOD
		ci_debug_printf(0, "INVALID ICAP METHOD (%d) ignoring...", REQ_TYPE);
	}
	// Nothing to do just return an allow204 (No modification) to terminate the ICAP transaction
	ci_debug_printf(4, "Allow 204...\n");

	return CI_MOD_ALLOW204;

}
void msp_close_service()
{
	ci_debug_printf(0,"MSP Service shutdown!\n");
	/*Nothing to do*/
}
/*
 * This function should inititalize the data and structures required for serving the request.
		param req - a pointer to the related ci_request_t structure
		returns   - a void pointer to the user defined data required for serving the request.
 * The developer can obtain the service data from the related ci_request_t object using the
 * macro ci_service_data
void *msp_init_request_data(ci_request_t * req) // first call
{
	const int REQ_TYPE = ci_req_type(req);
	ci_debug_printf(4,"New Msg @ msp_init_request_data().\n");
	if (REQ_TYPE == ICAP_REQMOD)
	{
		ci_debug_printf(4, "ICAP_REQMOD.\n");
	}
	else if (REQ_TYPE == ICAP_RESPMOD)
	{
		ci_debug_printf(4, "ICAP_RESPMOD.\n");
	}
	else if (REQ_TYPE == ICAP_OPTIONS)
	{
		ci_debug_printf(4, "ICAP OPTIONS.");
	}
	else
	{
		ci_debug_printf(0, "INVALID ICAP METHOD (%d).", REQ_TYPE);
	}
	// there's nothing to do here, we are not going to modifying anything
	// just deciding whether to accept or reject the method, later, so no
	// need to allocate anything.
	return NULL;
}
 */

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
					the service has send all the data to the client this parameter must set to CI_EOF.
	 param rbuf - Pointer to the data read from the ICAP client
	 param rlen - The length of the data read from the ICAP client. If this function for a reason
					can not read all the data, it must modify the rlen to be equal to the read data
	 param iseof - has non zero value if the data in rbuf buffer are the last data from the ICAP client.
	 param req   - pointer to the related ci_request struct
	return Return CI_OK if all are OK or CI_ERROR on errors
int msp_io(char *wbuf, int *wlen, char *rbuf, int *rlen, int iseof,
            ci_request_t * req)
{
	ci_debug_printf(1, "msp_io::Processing Request...\n");
	return CI_OK;
}
 */

/*
 * This function called after the user request served to release the service data
	 param srv_data - pointer to the service data returned by msp_init_request_data
void msp_release_request_data(void *srv_data)
{
	ci_debug_printf(0, "msp_release_request_data()\n");
}
 */

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
int msp_end_of_data_handler(ci_request_t * req)
{
	ci_debug_printf(1, "msp_end_of_data_handler()\n");
	return CI_MOD_DONE;
}
 */

/*
 * This function will be called when the service shutdown
	can be used to release service allocated resources
*/

/*
void msp_dumphex(FILE *mds, char *data, int len)
{
	char *current = data;
	int offset,i;

	for(offset = 0; offset < len; offset += 16)
	{
		fprintf(mds,"   %08x ",offset);
		for (i = 0; i < 16; i++)
		{
			if (current + i < data + len)
				fprintf(mds,"%02x ",current[i]);
			else
				fprintf(mds,"   ");
		}
		for (i = 0; i < 16; i++)
		{
			if (current + i < data + len)
				fprintf(mds,"%c", isprint(current[i]) ? current[i] : '.');
			else
				fprintf(mds," ");
		}
		fprintf(mds,"\n");
		current += 16;
	}
}
*/
