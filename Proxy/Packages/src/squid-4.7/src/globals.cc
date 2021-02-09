#include "squid.h"
/*
 * Copyright (C) 1996-2019 The Squid Software Foundation and contributors
 *
 * Squid software is distributed under GPLv2+ license and includes
 * contributions from numerous individuals and organizations.
 * Please see the COPYING and CONTRIBUTORS files for details.
 */


#include "CacheDigest.h"
#include "defines.h"
#include "hash.h"
#include "IoStats.h"
#include "rfc2181.h"
#include "sbuf/SBuf.h"

char *ConfigFile = NULL;
char tmp_error_buf[ERROR_BUF_SZ];
char ThisCache[RFC2181_MAXHOSTNAMELEN << 1];
char ThisCache2[RFC2181_MAXHOSTNAMELEN << 1];
char config_input_line[BUFSIZ];
/// During parsing, the name of the current squid.conf directive being parsed.
const char *cfg_directive = NULL;
const char *cfg_filename = NULL;
const char *dash_str = "-";
const char *null_string = "";
const char *version_string = VERSION;
const char *appname_string = PACKAGE;
char const *visible_appname_string = NULL;
int Biggest_FD = -1;
int Number_FD = 0;
int Opening_FD = 0;
int NDnsServersAlloc = 0;
int RESERVED_FD;
int Squid_MaxFD = SQUID_MAXFD;
int config_lineno = 0;
int opt_reuseaddr = 1;
int neighbors_do_private_keys = 1;
int opt_catch_signals = 1;
int opt_foreground = 0;
int opt_foreground_rebuild = 0;
char *opt_forwarded_for = NULL;
int opt_reload_hit_only = 0;

int opt_udp_hit_obj = 0;
int opt_create_swap_dirs = 0;
int opt_store_doublecheck = 0;
int syslog_enable = 0;
int DnsSocketA = -1;
int DnsSocketB = -1;
int n_disk_objects = 0;
IoStats IOStats;

struct timeval squid_start;
int starting_up = 1;
int shutting_down = 0;
int reconfiguring = 0;
time_t hit_only_mode_until = 0;
double request_failure_ratio = 0.0;
int store_hash_buckets = 0;
hash_table *store_table = NULL;
int hot_obj_count = 0;
int CacheDigestHashFuncCount = 4;
CacheDigest *store_digest = NULL;
const char *StoreDigestFileName = "store_digest";
const char *StoreDigestMimeStr = "application/cache-digest";

const char *MultipartMsgBoundaryStr = "Unique-Squid-Separator";
#if USE_HTTP_VIOLATIONS
int refresh_nocache_hack = 0;
#endif

int store_open_disk_fd = 0;
int store_swap_low = 0;
int store_swap_high = 0;
size_t store_pages_max = 0;
int64_t store_maxobjsize = 0;
int incoming_sockets_accepted;
#if _SQUID_WINDOWS_
unsigned int WIN32_Socks_initialized = 0;
#endif
#if _SQUID_WINDOWS_
unsigned int WIN32_OS_version = 0;
char *WIN32_OS_string = NULL;
char *WIN32_Command_Line = NULL;
char *WIN32_Service_Command_Line = NULL;
unsigned int WIN32_run_mode = _WIN_SQUID_RUN_MODE_INTERACTIVE;
#endif

int ssl_ex_index_server = -1;
int ssl_ctx_ex_index_dont_verify_domain = -1;
int ssl_ex_index_cert_error_check = -1;
int ssl_ex_index_ssl_error_detail = -1;
int ssl_ex_index_ssl_peeked_cert = -1;
int ssl_ex_index_ssl_errors = -1;
int ssl_ex_index_ssl_cert_chain = -1;
int ssl_ex_index_ssl_validation_counter = -1;

const char *external_acl_message = NULL;
int opt_send_signal = -1;
int opt_no_daemon = 0;
int opt_parse_cfg_only = 0;

/// current Squid process number (e.g., 4).
/// Zero for SMP-unaware code and in no-SMP mode.
int KidIdentifier = 0;


