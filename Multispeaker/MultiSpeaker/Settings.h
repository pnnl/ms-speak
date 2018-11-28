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
// Summary: Settings.h
//-------------------------------------------------------------------------------

#ifndef SPEAKERSETTINGS_H
#define SPEAKERSETTINGS_H

#include <QColor>
#include <QDataStream>
#include <QDir>
#include <QString>

const int GRAPH_TYPE_HOST = 1;
const int GRAPH_TYPE_LINE = 2;
const int GRAPH_TYPE_TIMELINE = 3;
const int GRAPH_TYPE_TIMELINE_EVENT = 4;

const QString DECOUPLE_RUN_FILE = "decouple.run";

const QString ROOT_HOME_PATH = QString("%1/.MultiSpeaker").arg(QDir::homePath());

const QString SK_XSD_FILE = "sk_xsd_file";
const QString SK_XML_FILE = "sk_xml_file";
const QString SK_INSTALL_CHECK = QStringLiteral("sk_fresh_install_check");
const QString SK_DEFAULT_NETWORK_CONFIG = QStringLiteral("sk_default_network_config");
const QString SK_HOST_ADDRESS = QStringLiteral("sk_host_address");
const QString SK_REQ_ENABLE_FLAG = QStringLiteral("sk_req_enable_flag");
const QString SK_RES_ENABLE_FLAG = QStringLiteral("sk_res_enable_flag");
const QString SK_EXPORT_XMLREQ_FILE = "sk_export_xmlreq_file";
const QString SK_EXPORT_XMLRES_FILE = "sk_export_xmlres_file";
const QString SK_SAVE_EDTREQ_FILE = "sk_save_edtreq_file";
const QString SK_SAVE_EDTRES_FILE = "sk_save_edtres_file";
const QString SK_RESTORE_EDTREQ_FILE = "sk_restore_edtreq_file";
const QString SK_RESTORE_EDTRES_FILE = "sk_restore_edtres_file";
const QString SK_RESTORE_EDTREQ_METHOD = "sk_restore_edtreq_method";
const QString SK_RESTORE_EDTRES_METHOD = "sk_restore_edtres_method";
const QString SK_SCENARIO_FILENAME = "sk_scenario_filename";

const quint32 SCENARIO_SAVE_MAGIC = 0x77777777;
const qint32 SCENARIO_SAVE_VERSION = 100;

const QString STR_NAMESPACE_MULTISPEAK_ORG_VERSION_30 = "http://www.multispeak.org/version_30";
const QString STR_NAMESPACE_PREFIX_TNS = "tns";

const QColor COLOR_CLOCK_LINE = QColor(255, 149, 68);
const QColor COLOR_EVENT_PROCESSED = QColor(0, 127, 0, 50);
const QColor COLOR_REQUEST = QColor(0, 255, 255, 127);
const QColor COLOR_RESPONSE = QColor(0, 127, 255, 127);

// JSON Tags
const QString JSON_ENABLED_TAG = "enabled";
const QString JSON_HEADERS_TAG = "headers";
const QString JSON_PARAMS_TAG = "params";
const QString JSON_REQUEST_TAG = "request";
const QString JSON_RESPONSE_TAG = "response";
const QString JSON_VALUE_TAG = "value";

// Splitter States
const QString SK_FUNCTION_BLOCK_DOCK_SCROLL_SPLITTER_STATE = "sk_function_block_dock_scroll_splitter_state";
const QString SK_MAIN_SPLITTER_STATE = "sk_main_splitter_state";
const QString SK_METHOD_DOCK_WC_SPLITTER_STATE = "sk_method_dock_wc_splitter_state";
const QString SK_TIMELINE_SPLITTER_STATE = "sk_timeline_splitter_state";
const QString SK_WSDL_DOCK_WC_SPLITTER_STATE = "sk_wsdl_dock_wc_splitter_state";

const QString SK_MINI_NET_APP = "sk_mini_net_app";
const QString SK_MINI_NET_CONF_FILE = "sk_mini_net_conf_file";
const QString SK_MINI_NET_HOST_IP = "sk_mini_net_host_ip";
const QString SK_MINI_NET_HOST_PORT = "sk_mini_net_host_port";
const QString SK_MINI_NET_NETWORK_ID = "sk_mini_net_network_id";
const QString SK_MINI_NET_SCRIPT_FILE = "sk_mini_net_script_file";

const QString SK_WSDL_IMPORT_PREFIX = "sk_wsdl_import_";

const QString SK_WMTE_GEOMETRY = "sk_wmte_geometry";

// Main Window States
const QString SK_MAIN_GEOMETRY = QStringLiteral("sk_main_geometry");
const QString SK_MAIN_STATE = QStringLiteral("sk_main_state");

const QString SK_SCENE_HEIGHT = QStringLiteral("sk_scene_height");
const QString SK_SCENE_WIDTH = QStringLiteral("sk_scene_width");

// TimelineEventEditor States
const QString SK_TEE_GEOMETRY = QStringLiteral("sk_tee_geometry");
const QString SK_TEE_MAIN_SPLIT = QStringLiteral("sk_tee_main_split");
const QString SK_TEE_REQUEST_SPLIT = QStringLiteral("sk_tee_request_split");
const QString SK_TEE_RESPONSE_SPLIT = QStringLiteral("sk_tee_response_split");

const QString SK_ID_COUNTER = "sk_id_counter";

// HttpOut
const QString SK_HTTP_OUT_REQ_FLAG = QStringLiteral("sk_http_out_req_flag");
const QString SK_HTTP_OUT_REQ_IP = QStringLiteral("sk_http_out_req_ip");
const QString SK_HTTP_OUT_REQ_PORT = QStringLiteral("sk_http_out_req_port");
const QString SK_HTTP_OUT_RES_FLAG = QStringLiteral("sk_http_out_res_flag");
const QString SK_HTTP_OUT_RES_IP = QStringLiteral("sk_http_out_res_ip");
const QString SK_HTTP_OUT_RES_PORT = QStringLiteral("sk_http_out_res_port");
const QString SK_HTTP_OUT_SSL = QStringLiteral("sk_http_out_ssl");
const QString SK_HTTP_OUT_HOSTS = QStringLiteral("sk_http_out_hosts");

const QString SK_IGNORE_SSL_SELF_CERT_ERROR = QStringLiteral("sk_ignore_ssl_self_cert_error");

// Timeline Scene
const int TIMELINE_SCENE_HEIGHT = 60;

#endif // SPEAKERSETTINGS_H
