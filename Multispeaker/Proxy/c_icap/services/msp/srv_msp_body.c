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
05/30/2019 - Carl Miller <carl.miller@pnnl.gov>
---------------------------------------------------------------------------------
*/

#include "body.h" 		
#include "request.h"	
#include "debug.h"		
#include "srv_msp_body.h"

int body_data_init(struct body_data *bd, enum body_type type,  int size, ci_membuf_t *err_page)
{
	ci_debug_printf(5, "        --->body_data_init::\n");

    if( !bd ){
		ci_debug_printf(5, "            returning %s\n", "!bd");
		return 0;
	}
	
    if( type == CACHED ){
		ci_debug_printf(5, "            type %s\n", "CACHED");
		bd->store.cached = ci_cached_file_new(size);
    }
    else if(type == RING  ){
		ci_debug_printf(5, "            type %s\n", "RING");
		bd->store.ring = ci_ring_buf_new(32768);
    }
    else if(type == ERROR_PAGE) {
		ci_debug_printf(5, "            type %s\n", "ERROR_PAGE");
		if( err_page ){
            bd->store.error_page = err_page;
		}
        else  {
			ci_debug_printf(1, "            No Error Page passed for body data.\n");
            return 0;
        }
    }
    else {
		ci_debug_printf(0, "            BUG in srv_msp, body_data_init: invalid body type:%d\n", type);
        return 0;
    }
    bd->type = type;
    bd ->eof = 0;
    return 1;
}

void body_data_destroy(struct body_data *body)
{
	ci_debug_printf(5, "    --->body_data_destroy::\n");
	if( body->type == CACHED ){
		ci_debug_printf(5, "        ci_cached_file_destroy: %s\n", "CACHED");
		ci_cached_file_destroy(body->store.cached);
        body->store.cached = NULL;
    }
    else if(body->type == RING  ){
		ci_debug_printf(5, "        ci_ring_buf_destroy: %s\n", "RING");
		ci_ring_buf_destroy(body->store.ring);
        body->store.ring = NULL;
    }
    else if(body->type == ERROR_PAGE) {
		ci_debug_printf(5, "        ci_membuf_free: %s\n", "ERROR_PAGE");
		ci_membuf_free(body->store.error_page);
        body->store.error_page = NULL;
    }
    else {
        ci_debug_printf(0, "        BUG in srv_msp, body_data_destroy: invalid body type:%d\n", body->type);
    }
    body->type = NO_BODY_TYPE;
    body->eof = 0;
}

int body_data_write(struct body_data *body, char *buf, int len, int iseof)
{
	ci_debug_printf(5, "    --->body_data_write::write client(Squid) data to a buffer...\n");
	if( iseof)
        body->eof = 1;

    if( body->type == CACHED ){
        if( buf && len)
            return ci_cached_file_write(body->store.cached, buf, len, iseof);
        else if( iseof)
            return  ci_cached_file_write(body->store.cached, NULL, 0, iseof);
        /*else ERROR*/
    }
    else if(body->type == RING  ){
        if( len && buf)
            return ci_ring_buf_write(body->store.ring, buf, len);
        else if( iseof)
            return CI_EOF;
        /*else ERROR*/
    }
    else if(body->type == ERROR_PAGE) {
		ci_debug_printf(5, "    --->ERROR_PAGE body type: error pages are read-only,don't write on them, Just discard the data\n");
		/*
          The error pages are read-only so we do not want to write on them.
          Just discard the data.
         */
		if (len && buf) {
			ci_debug_printf(5, "        returning len: %d\n", len);
			return  len;
		}
		else if (iseof) {
			ci_debug_printf(5, "        returning EOF\n");
			return CI_EOF;
		}
        /*else ERROR*/
    }
    else {
        ci_debug_printf(0, "        invalid body type:%d\n", body->type);
        return CI_ERROR;
    }

    return CI_ERROR;
}

int body_data_read(struct body_data *body, char *buf, int len)
{
	ci_debug_printf(5, "    --->body_data_read::read our saved data into client(Squid)'s receive buffer...\n");
	if( body->type == CACHED ){
        len = ci_cached_file_read(body->store.cached, buf, len);
        return len;
    }
    else if(body->type == RING  ){
        len = ci_ring_buf_read(body->store.ring, buf, len);
        if(len == 0 && body->eof == 1)
            return CI_EOF;
        return len;
    }
    else if(body->type == ERROR_PAGE) {
		len = ci_membuf_read(body->store.error_page, buf, len);
		if (len == CI_EOF) {
			ci_debug_printf(5, "        ci_membuf_read len: EOF\n");
		}
		else {
			ci_debug_printf(5, "        ci_membuf_read len: %d\n", len);
		}
		if( len == CI_ERROR)
            return CI_ERROR;

        if(len == 0)
            return CI_EOF;
        return len;
    }
    else {
        ci_debug_printf(0, "        invalid body type:%d\n", body->type);
        return CI_ERROR;
    }
}
