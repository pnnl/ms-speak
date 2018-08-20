//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: Settings
//

#ifndef SPEAKERSETTINGS_H
#define SPEAKERSETTINGS_H

#include <QDataStream>
#include <QDir>
#include <QString>

const int GRAPH_TYPE_HOST = 1;
const int GRAPH_TYPE_LINE = 2;
const int GRAPH_TYPE_TIMELINE = 3;
const int GRAPH_TYPE_TIMELINE_EVENT = 4;

const QString DECOUPLE_RUN_FILE = "decouple.run";

const QString ROOT_HOME_PATH = QString("%1/.MultiSpeaker").arg(QDir::homePath());

const QString SK_DEFAULT_NETWORK_CONFIG = QStringLiteral("sk_default_network_config");

const QString SK_HOST_ADDRESS = QStringLiteral("sk_host_address");

const QString SK_EXPORT_XML_FILE = "sk_export_xml_file";

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

#endif // SPEAKERSETTINGS_H
