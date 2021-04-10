/* include/autoconf.h.  Generated from autoconf.h.in by configure.  */
/* include/autoconf.h.in.  Generated from configure.ac by autoheader.  */

/* Define if building universal (internal helper macro) */
/* #undef AC_APPLE_UNIVERSAL_BUILD */

/* Defines how many threads aufs uses for I/O */
/* #undef AUFS_IO_THREADS */

/* If you are upset that the cachemgr.cgi form comes up with the hostname
   field blank, then define this to getfullhostname() */
/* #undef CACHEMGR_HOSTNAME */

/* Host type from configure */
#define CONFIG_HOST_TYPE "x86_64-pc-linux-gnu"

/* Define to one of `_getb67', `GETB67', `getb67' for Cray-2 and Cray-YMP
   systems. This function is required for `alloca.c' support on those systems.
   */
/* #undef CRAY_STACKSEG_END */

/* Define to 1 if using `alloca.c'. */
/* #undef C_ALLOCA */

/* Default FD_SETSIZE value */
#define DEFAULT_FD_SETSIZE 1024

/* The install prefix */
#define DEFAULT_PREFIX /usr/local/squid

/* Enable following X-Forwarded-For headers */
#define FOLLOW_X_FORWARDED_FOR 1

/* If gettimeofday is known to take only one argument */
/* #undef GETTIMEOFDAY_NO_TZP */

/* Define to 1 if you have the <aio.h> header file. */
#define HAVE_AIO_H 1

/* Define to 1 if you have `alloca', as a function or macro. */
#define HAVE_ALLOCA 1

/* Define to 1 if you have <alloca.h> and it should be used (not on Ultrix).
   */
#define HAVE_ALLOCA_H 1

/* Define to 1 if you have the `argz_add' function. */
#define HAVE_ARGZ_ADD 1

/* Define to 1 if you have the `argz_append' function. */
#define HAVE_ARGZ_APPEND 1

/* Define to 1 if you have the `argz_count' function. */
#define HAVE_ARGZ_COUNT 1

/* Define to 1 if you have the `argz_create_sep' function. */
#define HAVE_ARGZ_CREATE_SEP 1

/* Define to 1 if you have the <argz.h> header file. */
#define HAVE_ARGZ_H 1

/* Define to 1 if you have the `argz_insert' function. */
#define HAVE_ARGZ_INSERT 1

/* Define to 1 if you have the `argz_next' function. */
#define HAVE_ARGZ_NEXT 1

/* Define to 1 if you have the `argz_stringify' function. */
#define HAVE_ARGZ_STRINGIFY 1

/* Define to 1 if you have the <arpa/inet.h> header file. */
#define HAVE_ARPA_INET_H 1

/* Define to 1 if you have the <arpa/nameser.h> header file. */
#define HAVE_ARPA_NAMESER_H 1

/* Define to 1 if you have the <assert.h> header file. */
#define HAVE_ASSERT_H 1

/* Basic auth module is built */
#define HAVE_AUTH_MODULE_BASIC 1

/* Digest auth module is built */
#define HAVE_AUTH_MODULE_DIGEST 1

/* Negotiate auth module is built */
#define HAVE_AUTH_MODULE_NEGOTIATE 1

/* NTLM auth module is built */
#define HAVE_AUTH_MODULE_NTLM 1

/* Define to 1 if you have the `backtrace_symbols_fd' function. */
#define HAVE_BACKTRACE_SYMBOLS_FD 1

/* Define to 1 if you have the `bcopy' function. */
#define HAVE_BCOPY 1

/* Define to 1 if Heimdal krb5.h is broken for C++ */
/* #undef HAVE_BROKEN_HEIMDAL_KRB5_H */

/* Define to 1 if Solaris krb5.h is broken for C++ */
/* #undef HAVE_BROKEN_SOLARIS_KRB5_H */

/* Define to 1 if you have the <bstring.h> header file. */
/* #undef HAVE_BSTRING_H */

/* Define to 1 if you have the `bswap16' function. */
/* #undef HAVE_BSWAP16 */

/* Define to 1 if you have the `bswap32' function. */
/* #undef HAVE_BSWAP32 */

/* Define to 1 if you have the `bswap_16' function. */
/* #undef HAVE_BSWAP_16 */

/* Define to 1 if you have the `bswap_32' function. */
/* #undef HAVE_BSWAP_32 */

/* Define to 1 if you have the <byteswap.h> header file. */
#define HAVE_BYTESWAP_H 1

/* Define to 1 if you have the `closedir' function. */
#define HAVE_CLOSEDIR 1

/* The system provides struct cmsghdr */
#define HAVE_CMSGHDR 1

/* Define to 1 if you have the <com_err.h> header file. */
/* #undef HAVE_COM_ERR_H */

/* Define to 1 if CMSG_SPACE is constant */
#define HAVE_CONSTANT_CMSG_SPACE 1

/* Define to 1 if you have the <cppunit/extensions/HelperMacros.h> header
   file. */
/* #undef HAVE_CPPUNIT_EXTENSIONS_HELPERMACROS_H */

/* Support setting CPU affinity for workers */
#define HAVE_CPU_AFFINITY 1

/* cpu_set_t is defined by the system headers */
#define HAVE_CPU_SET_T 1

/* Define to 1 if you have the `crypt' function. */
#define HAVE_CRYPT 1

/* Define to 1 if you have the <crypt.h> header file. */
#define HAVE_CRYPT_H 1

/* Define to 1 if you have the <ctype.h> header file. */
#define HAVE_CTYPE_H 1

/* define if the compiler supports basic C++11 syntax */
/* #undef HAVE_CXX11 */

/* Define to 1 if you have the <db_185.h> header file. */
/* #undef HAVE_DB_185_H */

/* Define to 1 if you have the <db.h> header file. */
/* #undef HAVE_DB_H */

/* Define to 1 if you have the declaration of `cygwin_conv_path', and to 0 if
   you don't. */
/* #undef HAVE_DECL_CYGWIN_CONV_PATH */

/* Define to 1 if you have the declaration of `getaddrinfo', and to 0 if you
   don't. */
#define HAVE_DECL_GETADDRINFO 1

/* Define to 1 if you have the declaration of `getnameinfo', and to 0 if you
   don't. */
#define HAVE_DECL_GETNAMEINFO 1

/* Define to 1 if you have the declaration of `InetNtopA', and to 0 if you
   don't. */
#define HAVE_DECL_INETNTOPA 0

/* Define to 1 if you have the declaration of `InetPtonA', and to 0 if you
   don't. */
#define HAVE_DECL_INETPTONA 0

/* Define to 1 if you have the declaration of `inet_ntop', and to 0 if you
   don't. */
#define HAVE_DECL_INET_NTOP 1

/* Define to 1 if you have the declaration of `inet_pton', and to 0 if you
   don't. */
#define HAVE_DECL_INET_PTON 1

/* Define to 1 if you have the declaration of `krb5_kt_free_entry', and to 0
   if you don't. */
/* #undef HAVE_DECL_KRB5_KT_FREE_ENTRY */

/* Define to 1 if you have the <direct.h> header file. */
/* #undef HAVE_DIRECT_H */

/* Define to 1 if you have the <dirent.h> header file, and it defines `DIR'.
   */
#define HAVE_DIRENT_H 1

/* POSIX AIO Disk I/O module is built */
#define HAVE_DISKIO_MODULE_AIO 1

/* Blocking Disk I/O module is built */
#define HAVE_DISKIO_MODULE_BLOCKING 1

/* DiskDaemon Disk I/O module is built */
#define HAVE_DISKIO_MODULE_DISKDAEMON 1

/* DiskThreads Disk I/O module is built */
#define HAVE_DISKIO_MODULE_DISKTHREADS 1

/* IpcIo Disk I/O module is built */
#define HAVE_DISKIO_MODULE_IPCIO 1

/* Mmapped Disk I/O module is built */
#define HAVE_DISKIO_MODULE_MMAPPED 1

/* Define if you have the GNU dld library. */
/* #undef HAVE_DLD */

/* Define to 1 if you have the <dld.h> header file. */
/* #undef HAVE_DLD_H */

/* Define to 1 if you have the `dlerror' function. */
#define HAVE_DLERROR 1

/* Define to 1 if you have the <dlfcn.h> header file. */
#define HAVE_DLFCN_H 1

/* Define to 1 if you have the <dl.h> header file. */
/* #undef HAVE_DL_H */

/* Define if you have the _dyld_func_lookup function. */
/* #undef HAVE_DYLD */

/* Define to 1 if you have the <endian.h> header file. */
#define HAVE_ENDIAN_H 1

/* Define to 1 if you have the <errno.h> header file. */
#define HAVE_ERRNO_H 1

/* Define to 1 if you have error_message */
/* #undef HAVE_ERROR_MESSAGE */

/* Define to 1 if the system has the type `error_t'. */
#define HAVE_ERROR_T 1

/* Define to 1 if you have the <et/com_err.h> header file. */
/* #undef HAVE_ET_COM_ERR_H */

/* Define to 1 if you have the `eui64_aton' function. */
/* #undef HAVE_EUI64_ATON */

/* Define to 1 if you have the <execinfo.h> header file. */
#define HAVE_EXECINFO_H 1

/* Define to 1 if you have the <expat.h> header file. */
/* #undef HAVE_EXPAT_H */

/* Define to 1 if you have the `fchmod' function. */
#define HAVE_FCHMOD 1

/* Define to 1 if you have the <fcntl.h> header file. */
#define HAVE_FCNTL_H 1

/* fd_mask is defined by the system headers */
#define HAVE_FD_MASK 1

/* Define to 1 if you have the <fnmatch.h> header file. */
#define HAVE_FNMATCH_H 1

/* "Define to 1 if aufs filesystem module is build" */
#define HAVE_FS_AUFS 1

/* "Define to 1 if diskd filesystem module is build" */
#define HAVE_FS_DISKD 1

/* "Define to 1 if rock filesystem module is build" */
#define HAVE_FS_ROCK 1

/* "Define to 1 if ufs filesystem module is build" */
#define HAVE_FS_UFS 1

/* Define if struct statfs has field f_frsize (Linux 2.6 or later) */
/* #undef HAVE_F_FRSIZE_IN_STATFS */

/* Define to 1 if you have the `getdtablesize' function. */
#define HAVE_GETDTABLESIZE 1

/* Define to 1 if you have the <getopt.h> header file. */
#define HAVE_GETOPT_H 1

/* Define to 1 if you have the `getpagesize' function. */
#define HAVE_GETPAGESIZE 1

/* Define to 1 if you have the `getpass' function. */
#define HAVE_GETPASS 1

/* Define to 1 if you have the `getrlimit' function. */
#define HAVE_GETRLIMIT 1

/* Define to 1 if you have the `getrusage' function. */
#define HAVE_GETRUSAGE 1

/* Define to 1 if you have the `getspnam' function. */
#define HAVE_GETSPNAM 1

/* Define to 1 if you have the `gettimeofday' function. */
#define HAVE_GETTIMEOFDAY 1

/* Define to 1 if you have krb5_get_init_creds_keytab */
/* #undef HAVE_GET_INIT_CREDS_KEYTAB */

/* Define to 1 if you have the <glib.h> header file. */
/* #undef HAVE_GLIB_H */

/* Define to 1 if you have the `glob' function. */
#define HAVE_GLOB 1

/* Define to 1 if you have the <glob.h> header file. */
#define HAVE_GLOB_H 1

/* Define to 1 if you have the <gnumalloc.h> header file. */
/* #undef HAVE_GNUMALLOC_H */

/* Define to 1 if you have the <gnutls/abstract.h> header file. */
/* #undef HAVE_GNUTLS_ABSTRACT_H */

/* Define to 1 if you have the <gnutls/gnutls.h> header file. */
/* #undef HAVE_GNUTLS_GNUTLS_H */

/* Define to 1 if you have the <gnutls/x509.h> header file. */
/* #undef HAVE_GNUTLS_X509_H */

/* Define to 1 if you have the <grp.h> header file. */
#define HAVE_GRP_H 1

/* GSSAPI support */
/* #undef HAVE_GSSAPI */

/* Define to 1 if you have the <gssapi/gssapi_ext.h> header file. */
/* #undef HAVE_GSSAPI_GSSAPI_EXT_H */

/* Define to 1 if you have the <gssapi/gssapi_generic.h> header file. */
/* #undef HAVE_GSSAPI_GSSAPI_GENERIC_H */

/* Define to 1 if you have the <gssapi/gssapi.h> header file. */
/* #undef HAVE_GSSAPI_GSSAPI_H */

/* Define to 1 if you have the <gssapi/gssapi_krb5.h> header file. */
/* #undef HAVE_GSSAPI_GSSAPI_KRB5_H */

/* Define to 1 if you have the <gssapi.h> header file. */
/* #undef HAVE_GSSAPI_H */

/* Define to 1 if you have the `gsskrb5_extract_authz_data_from_sec_context'
   function. */
/* #undef HAVE_GSSKRB5_EXTRACT_AUTHZ_DATA_FROM_SEC_CONTEXT */

/* Define to 1 if you have the <gss.h> header file. */
/* #undef HAVE_GSS_H */

/* Define to 1 if you have gss_map_name_to_any */
/* #undef HAVE_GSS_MAP_ANY_TO_ANY */

/* Define to 1 if you have the `gss_map_name_to_any' function. */
/* #undef HAVE_GSS_MAP_NAME_TO_ANY */

/* Define to 1 if you have the `htole16' function. */
/* #undef HAVE_HTOLE16 */

/* Define to 1 if you have the `htole32' function. */
/* #undef HAVE_HTOLE32 */

/* Define to 1 if you have the `initgroups' function. */
#define HAVE_INITGROUPS 1

/* Define to 1 if you have the <inttypes.h> header file. */
#define HAVE_INTTYPES_H 1

/* Define to 1 if you have the `ioctl' function. */
#define HAVE_IOCTL 1

/* The system provides struct iovec */
#define HAVE_IOVEC 1

/* Define to 1 if you have the <iphlpapi.h> header file. */
/* #undef HAVE_IPHLPAPI_H */

/* Define to 1 if you have the <ipl.h> header file. */
/* #undef HAVE_IPL_H */

/* Define to 1 if you have the <ip_compat.h> header file. */
/* #undef HAVE_IP_COMPAT_H */

/* Define to 1 if you have the <ip_fil_compat.h> header file. */
/* #undef HAVE_IP_FIL_COMPAT_H */

/* Define to 1 if you have the <ip_fil.h> header file. */
/* #undef HAVE_IP_FIL_H */

/* Define to 1 if you have the <ip_nat.h> header file. */
/* #undef HAVE_IP_NAT_H */

/* Define to 1 if you have the `kqueue' function. */
/* #undef HAVE_KQUEUE */

/* KRB5 support */
/* #undef HAVE_KRB5 */

/* Define to 1 if you have krb5_free_error_message */
/* #undef HAVE_KRB5_FREE_ERROR_MESSAGE */

/* Define to 1 if you have krb5_free_error_string */
/* #undef HAVE_KRB5_FREE_ERROR_STRING */

/* Define to 1 if you have krb5_get_error_message */
/* #undef HAVE_KRB5_GET_ERROR_MESSAGE */

/* Define to 1 if you have krb5_get_err_text */
/* #undef HAVE_KRB5_GET_ERR_TEXT */

/* Define to 1 if you krb5_get_init_creds_free requires krb5_context */
/* #undef HAVE_KRB5_GET_INIT_CREDS_FREE_CONTEXT */

/* Define to 1 if you have krb5_get_init_creds_opt_alloc */
/* #undef HAVE_KRB5_GET_INIT_CREDS_OPT_ALLOC */

/* Define to 1 if you have krb5_get_max_time_skew */
/* #undef HAVE_KRB5_GET_MAX_TIME_SKEW */

/* Define to 1 if you have krb5_get_profile */
/* #undef HAVE_KRB5_GET_PROFILE */

/* Define to 1 if you have krb5_get_renewed_creds */
/* #undef HAVE_KRB5_GET_RENEWED_CREDS */

/* Define to 1 if you have the <krb5.h> header file. */
/* #undef HAVE_KRB5_H */

/* Define to 1 if you have krb5_kt_free_entry */
/* #undef HAVE_KRB5_KT_FREE_ENTRY */

/* Define if kerberos has MEMORY: cache support */
/* #undef HAVE_KRB5_MEMORY_CACHE */

/* Define if kerberos has MEMORY: keytab support */
/* #undef HAVE_KRB5_MEMORY_KEYTAB */

/* Define to 1 if you have krb5_pac */
/* #undef HAVE_KRB5_PAC */

/* Define to 1 if you have krb5_principal_get_realm */
/* #undef HAVE_KRB5_PRINCIPAL_GET_REALM */

/* Define to 1 if you have the <lber.h> header file. */
/* #undef HAVE_LBER_H */

/* LDAP support */
/* #undef HAVE_LDAP */

/* Define to 1 if you have ldapssl_client_init */
/* #undef HAVE_LDAPSSL_CLIENT_INIT */

/* Define to 1 if you have the <ldap.h> header file. */
/* #undef HAVE_LDAP_H */

/* Define to 1 if you have LDAP_REBINDPROC_CALLBACK */
/* #undef HAVE_LDAP_REBINDPROC_CALLBACK */

/* Define to 1 if you have LDAP_REBIND_FUNCTION */
/* #undef HAVE_LDAP_REBIND_FUNCTION */

/* Define to 1 if you have LDAP_REBIND_PROC */
/* #undef HAVE_LDAP_REBIND_PROC */

/* Define to 1 if you have LDAP_SCOPE_DEFAULT */
/* #undef HAVE_LDAP_SCOPE_DEFAULT */

/* Define to 1 if you have ldap_start_tls_s */
/* #undef HAVE_LDAP_START_TLS_S */

/* Define to 1 if you have ldap_url_desc2str */
/* #undef HAVE_LDAP_URL_DESC2STR */

/* Define to 1 if you have LDAPURLDesc.lud_scheme */
/* #undef HAVE_LDAP_URL_LUD_SCHEME */

/* Define to 1 if you have ldap_url_parse */
/* #undef HAVE_LDAP_URL_PARSE */

/* Define to 1 if you have the `le16toh' function. */
/* #undef HAVE_LE16TOH */

/* Define to 1 if you have the `le32toh' function. */
/* #undef HAVE_LE32TOH */

/* Define to 1 if you have the `cap' library (-lcap). */
/* #undef HAVE_LIBCAP */

/* "Define to 1 if the ASN1_STRING_get0_data() OpenSSL API function exists" */
/* #undef HAVE_LIBCRYPTO_ASN1_STRING_GET0_DATA */

/* "Define to 1 if the BIO_get_data() OpenSSL API function exists" */
/* #undef HAVE_LIBCRYPTO_BIO_GET_DATA */

/* "Define to 1 if the BIO_get_init() OpenSSL API function exists" */
/* #undef HAVE_LIBCRYPTO_BIO_GET_INIT */

/* "Define to 1 if the BIO_meth_new() OpenSSL API function exists" */
/* #undef HAVE_LIBCRYPTO_BIO_METH_NEW */

/* "Define to 1 if the DH_up_ref() OpenSSL API function exists" */
/* #undef HAVE_LIBCRYPTO_DH_UP_REF */

/* "Define to 1 if the EVP_PKEY_get0_RSA() OpenSSL API function exists" */
/* #undef HAVE_LIBCRYPTO_EVP_PKEY_GET0_RSA */

/* "Define to 1 if the EVP_PKEY_up_ref() OpenSSL API function exists" */
/* #undef HAVE_LIBCRYPTO_EVP_PKEY_UP_REF */

/* "Define to 1 if the OPENSSL_LH_strhash() OpenSSL API function exists" */
/* #undef HAVE_LIBCRYPTO_OPENSSL_LH_STRHASH */

/* "Define to 1 if the X509_CRL_up_ref() OpenSSL API function exists" */
/* #undef HAVE_LIBCRYPTO_X509_CRL_UP_REF */

/* "Define to 1 if the X509_get0_signature() OpenSSL API function exists" */
/* #undef HAVE_LIBCRYPTO_X509_GET0_SIGNATURE */

/* "Define to 1 if the X509_STORE_CTX_get0_cert() OpenSSL API function exists"
   */
/* #undef HAVE_LIBCRYPTO_X509_STORE_CTX_GET0_CERT */

/* "Define to 1 if the X509_STORE_CTX_get0_untrusted() OpenSSL API function
   exists" */
/* #undef HAVE_LIBCRYPTO_X509_STORE_CTX_GET0_UNTRUSTED */

/* "Define to 1 if the X509_up_ref() OpenSSL API function exists" */
/* #undef HAVE_LIBCRYPTO_X509_UP_REF */

/* "Define to 1 if the X509_VERIFY_PARAM_get_depth() OpenSSL API function
   exists" */
/* #undef HAVE_LIBCRYPTO_X509_VERIFY_PARAM_GET_DEPTH */

/* Define to 1 if you have the <libc.h> header file. */
/* #undef HAVE_LIBC_H */

/* Define to 1 if you have the `dl' library (-ldl). */
#define HAVE_LIBDL 1

/* Define if libdlloader will be built on this platform */
#define HAVE_LIBDLLOADER 1

/* Define to 1 if you have the expat library */
#define HAVE_LIBEXPAT 0

/* Define to 1 if you have the `gnumalloc' library (-lgnumalloc). */
/* #undef HAVE_LIBGNUMALLOC */

/* Define to 1 if you have the `intl' library (-lintl). */
/* #undef HAVE_LIBINTL */

/* Define to 1 if you have the `malloc' library (-lmalloc). */
/* #undef HAVE_LIBMALLOC */

/* Define to 1 if you have the
   <libnetfilter_conntrack/libnetfilter_conntrack.h> header file. */
/* #undef HAVE_LIBNETFILTER_CONNTRACK_LIBNETFILTER_CONNTRACK_H */

/* Define to 1 if you have the
   <libnetfilter_conntrack/libnetfilter_conntrack_tcp.h> header file. */
/* #undef HAVE_LIBNETFILTER_CONNTRACK_LIBNETFILTER_CONNTRACK_TCP_H */

/* "Define to 1 if the OPENSSL_init_ssl() OpenSSL API function exists" */
/* #undef HAVE_LIBSSL_OPENSSL_INIT_SSL */

/* "Define to 1 if the SSL_CIPHER_find() OpenSSL API function exists" */
/* #undef HAVE_LIBSSL_SSL_CIPHER_FIND */

/* "Define to 1 if the SSL_CTX_set_tmp_rsa_callback() OpenSSL API function
   exists" */
/* #undef HAVE_LIBSSL_SSL_CTX_SET_TMP_RSA_CALLBACK */

/* "Define to 1 if the SSL_SESSION_get_id() OpenSSL API function exists" */
/* #undef HAVE_LIBSSL_SSL_SESSION_GET_ID */

/* Define to 1 if you have the libxml2 library */
#define HAVE_LIBXML2 1

/* Define to 1 if you have the <libxml/HTMLparser.h> header file. */
#define HAVE_LIBXML_HTMLPARSER_H 1

/* Define to 1 if you have the <libxml/HTMLtree.h> header file. */
#define HAVE_LIBXML_HTMLTREE_H 1

/* Define to 1 if you have the <libxml/parser.h> header file. */
#define HAVE_LIBXML_PARSER_H 1

/* Define to 1 if you have the <limits.h> header file. */
#define HAVE_LIMITS_H 1

/* Define to 1 if you have the <linux/netfilter_ipv4.h> header file. */
#define HAVE_LINUX_NETFILTER_IPV4_H 1

/* Define to 1 if you have the <linux/netfilter_ipv6/ip6_tables.h> header
   file. */
/* #undef HAVE_LINUX_NETFILTER_IPV6_IP6_TABLES_H */

/* Define to 1 if you have the <linux/posix_types.h> header file. */
#define HAVE_LINUX_POSIX_TYPES_H 1

/* Define to 1 if you have the <linux/types.h> header file. */
#define HAVE_LINUX_TYPES_H 1

/* Define this if a modern libltdl is already installed */
/* #undef HAVE_LTDL */

/* Define to 1 if you have the <machine/byte_swap.h> header file. */
/* #undef HAVE_MACHINE_BYTE_SWAP_H */

/* Define to 1 if you have the <mach-o/dyld.h> header file. */
/* #undef HAVE_MACH_O_DYLD_H */

/* Define to 1 if you have the `mallocblksize' function. */
/* #undef HAVE_MALLOCBLKSIZE */

/* Define to 1 if you have the <malloc.h> header file. */
#define HAVE_MALLOC_H 1

/* Define to 1 if you have the `mallopt' function. */
#define HAVE_MALLOPT 1

/* Define to 1 if you have the <math.h> header file. */
#define HAVE_MATH_H 1

/* Define to 1 if you have the `memcpy' function. */
#define HAVE_MEMCPY 1

/* Define to 1 if you have the `memmove' function. */
#define HAVE_MEMMOVE 1

/* Define to 1 if you have the <memory.h> header file. */
#define HAVE_MEMORY_H 1

/* Define to 1 if you have the `memrchr' function. */
#define HAVE_MEMRCHR 1

/* Define to 1 if you have the `memset' function. */
#define HAVE_MEMSET 1

/* Define to 1 if you have the `mkstemp' function. */
#define HAVE_MKSTEMP 1

/* Define to 1 if you have the `mktime' function. */
#define HAVE_MKTIME 1

/* mode_t is defined by the system headers */
#define HAVE_MODE_T 1

/* Define to 1 if you have the <mount.h> header file. */
/* #undef HAVE_MOUNT_H */

/* Mozilla LDAP SDK support */
/* #undef HAVE_MOZILLA_LDAP_SDK */

/* Define to 1 if you have the <mozldap/ldap.h> header file. */
/* #undef HAVE_MOZLDAP_LDAP_H */

/* The system provides struct msghdr */
#define HAVE_MSGHDR 1

/* Define to 1 if you have the `mstats' function. */
/* #undef HAVE_MSTATS */

/* Define to 1 if you have the <mswsock.h> header file. */
/* #undef HAVE_MSWSOCK_H */

/* mtyp_t is defined by the system headers */
/* #undef HAVE_MTYP_T */

/* Define to 1 if you have the <ndir.h> header file, and it defines `DIR'. */
/* #undef HAVE_NDIR_H */

/* Define to 1 if you have the <netdb.h> header file. */
#define HAVE_NETDB_H 1

/* Define to 1 if you have the <netinet/icmp6.h> header file. */
#define HAVE_NETINET_ICMP6_H 1

/* Define to 1 if you have the <netinet/if_ether.h> header file. */
#define HAVE_NETINET_IF_ETHER_H 1

/* Define to 1 if you have the <netinet/in.h> header file. */
#define HAVE_NETINET_IN_H 1

/* Define to 1 if you have the <netinet/in_systm.h> header file. */
#define HAVE_NETINET_IN_SYSTM_H 1

/* Define to 1 if you have the <netinet/ip6.h> header file. */
#define HAVE_NETINET_IP6_H 1

/* Define to 1 if you have the <netinet/ipl.h> header file. */
/* #undef HAVE_NETINET_IPL_H */

/* Define to 1 if you have the <netinet/ip_compat.h> header file. */
/* #undef HAVE_NETINET_IP_COMPAT_H */

/* Define to 1 if you have the <netinet/ip_fil_compat.h> header file. */
/* #undef HAVE_NETINET_IP_FIL_COMPAT_H */

/* Define to 1 if you have the <netinet/ip_fil.h> header file. */
/* #undef HAVE_NETINET_IP_FIL_H */

/* Define to 1 if you have the <netinet/ip.h> header file. */
#define HAVE_NETINET_IP_H 1

/* Define to 1 if you have the <netinet/ip_icmp.h> header file. */
#define HAVE_NETINET_IP_ICMP_H 1

/* Define to 1 if you have the <netinet/ip_nat.h> header file. */
/* #undef HAVE_NETINET_IP_NAT_H */

/* Define to 1 if you have the <netinet/tcp.h> header file. */
#define HAVE_NETINET_TCP_H 1

/* set to 1 if Nettle 3.4 API will link */
/* #undef HAVE_NETTLE34_BASE64 */

/* Define to 1 if you have the <nettle/base64.h> header file. */
/* #undef HAVE_NETTLE_BASE64_H */

/* Define to 1 if you have the <nettle/md5.h> header file. */
/* #undef HAVE_NETTLE_MD5_H */

/* Define to 1 if you have the <net/if_arp.h> header file. */
#define HAVE_NET_IF_ARP_H 1

/* Define to 1 if you have the <net/if_dl.h> header file. */
/* #undef HAVE_NET_IF_DL_H */

/* Define to 1 if you have the <net/if.h> header file. */
#define HAVE_NET_IF_H 1

/* Define to 1 if you have the <net/pfvar.h> header file. */
/* #undef HAVE_NET_PFVAR_H */

/* Define to 1 if you have the <net/pf/pfvar.h> header file. */
/* #undef HAVE_NET_PF_PFVAR_H */

/* Define to 1 if you have the <net/route.h> header file. */
#define HAVE_NET_ROUTE_H 1

/* Define to 1 if nullptr_t is supported */
#define HAVE_NULLPTR_T 1

/* Define to 1 if you have the `opendir' function. */
#define HAVE_OPENDIR 1

/* OpenLDAP support */
/* #undef HAVE_OPENLDAP */

/* Define to 1 if you have the <openssl/asn1.h> header file. */
/* #undef HAVE_OPENSSL_ASN1_H */

/* Define to 1 if you have the <openssl/bio.h> header file. */
/* #undef HAVE_OPENSSL_BIO_H */

/* Define to 1 if you have the <openssl/bn.h> header file. */
/* #undef HAVE_OPENSSL_BN_H */

/* Define to 1 if you have the <openssl/crypto.h> header file. */
/* #undef HAVE_OPENSSL_CRYPTO_H */

/* Define to 1 if you have the <openssl/dh.h> header file. */
/* #undef HAVE_OPENSSL_DH_H */

/* Define to 1 if you have the <openssl/engine.h> header file. */
/* #undef HAVE_OPENSSL_ENGINE_H */

/* Define to 1 if you have the <openssl/err.h> header file. */
/* #undef HAVE_OPENSSL_ERR_H */

/* Define to 1 if you have the <openssl/evp.h> header file. */
/* #undef HAVE_OPENSSL_EVP_H */

/* Define to 1 if you have the <openssl/lhash.h> header file. */
/* #undef HAVE_OPENSSL_LHASH_H */

/* Define to 1 if you have the <openssl/md5.h> header file. */
/* #undef HAVE_OPENSSL_MD5_H */

/* Define to 1 if you have the <openssl/opensslv.h> header file. */
/* #undef HAVE_OPENSSL_OPENSSLV_H */

/* Define to 1 if you have the <openssl/rsa.h> header file. */
/* #undef HAVE_OPENSSL_RSA_H */

/* Define to 1 if you have the <openssl/ssl.h> header file. */
/* #undef HAVE_OPENSSL_SSL_H */

/* "Define to 1 if the TLS_client_method() OpenSSL API function exists" */
/* #undef HAVE_OPENSSL_TLS_CLIENT_METHOD */

/* "Define to 1 if the TLS_method() OpenSSL API function exists" */
/* #undef HAVE_OPENSSL_TLS_METHOD */

/* "Define to 1 if the TLS_server_method() OpenSSL API function exists" */
/* #undef HAVE_OPENSSL_TLS_SERVER_METHOD */

/* Define to 1 if you have the <openssl/txt_db.h> header file. */
/* #undef HAVE_OPENSSL_TXT_DB_H */

/* Define to 1 if you have the <openssl/x509v3.h> header file. */
/* #undef HAVE_OPENSSL_X509V3_H */

/* Define to 1 if you have the <openssl/x509.h> header file. */
/* #undef HAVE_OPENSSL_X509_H */

/* pad128_t is defined in system headers */
/* #undef HAVE_PAD128_T */

/* Define to 1 if you have the <paths.h> header file. */
#define HAVE_PATHS_H 1

/* Define to 1 if you have the `poll' function. */
#define HAVE_POLL 1

/* Define to 1 if you have the <poll.h> header file. */
#define HAVE_POLL_H 1

/* Define to 1 if you have the `prctl' function. */
#define HAVE_PRCTL 1

/* Define if libtool can extract symbol lists from object files. */
#define HAVE_PRELOADED_SYMBOLS 1

/* Define to 1 if you have profile_get_integer */
/* #undef HAVE_PROFILE_GET_INTEGER */

/* Define to 1 if you have the <profile.h> header file. */
/* #undef HAVE_PROFILE_H */

/* Define to 1 if you have profile_release */
/* #undef HAVE_PROFILE_RELEASE */

/* Define to 1 if you have the `psignal' function. */
#define HAVE_PSIGNAL 1

/* Define to 1 if you have the `pthread_attr_setschedparam' function. */
#define HAVE_PTHREAD_ATTR_SETSCHEDPARAM 1

/* Define to 1 if you have the `pthread_attr_setscope' function. */
#define HAVE_PTHREAD_ATTR_SETSCOPE 1

/* Define to 1 if you have the `pthread_setschedparam' function. */
#define HAVE_PTHREAD_SETSCHEDPARAM 1

/* Define to 1 if you have the `pthread_sigmask' function. */
/* #undef HAVE_PTHREAD_SIGMASK */

/* Define to 1 if you have the `putenv' function. */
#define HAVE_PUTENV 1

/* Define to 1 if you have the <pwd.h> header file. */
#define HAVE_PWD_H 1

/* Define to 1 if you have the `readdir' function. */
#define HAVE_READDIR 1

/* Define to 1 if you have the `regcomp' function. */
#define HAVE_REGCOMP 1

/* Define to 1 if you have the `regexec' function. */
#define HAVE_REGEXEC 1

/* Define to 1 if you have the <regex.h> header file. */
#define HAVE_REGEX_H 1

/* Define to 1 if you have the `regfree' function. */
#define HAVE_REGFREE 1

/* Define to 1 if you have the <resolv.h> header file. */
#define HAVE_RESOLV_H 1

/* Define to 1 if you have the `res_init' function. */
/* #undef HAVE_RES_INIT */

/* Define to 1 if you have the `rint' function. */
#define HAVE_RINT 1

/* Define to 1 if you have the <rpcsvc/ypclnt.h> header file. */
#define HAVE_RPCSVC_YPCLNT_H 1

/* Define to 1 if you have the <rpcsvc/yp_prot.h> header file. */
#define HAVE_RPCSVC_YP_PROT_H 1

/* Define to 1 if you have the <rpc/rpc.h> header file. */
#define HAVE_RPC_RPC_H 1

/* Define to 1 if Mac Darwin without sasl.h */
/* #undef HAVE_SASL_DARWIN */

/* Define to 1 if you have the <sasl.h> header file. */
/* #undef HAVE_SASL_H */

/* Define to 1 if you have the <sasl/sasl.h> header file. */
/* #undef HAVE_SASL_SASL_H */

/* Define to 1 if you have the `sched_getaffinity' function. */
#define HAVE_SCHED_GETAFFINITY 1

/* Define to 1 if you have the <sched.h> header file. */
#define HAVE_SCHED_H 1

/* Define to 1 if you have the `sched_setaffinity' function. */
#define HAVE_SCHED_SETAFFINITY 1

/* Define to 1 if you have the <security/pam_appl.h> header file. */
/* #undef HAVE_SECURITY_PAM_APPL_H */

/* Define to 1 if you have the `select' function. */
#define HAVE_SELECT 1

/* Define to 1 if you have the `seteuid' function. */
#define HAVE_SETEUID 1

/* Define to 1 if you have the `setgroups' function. */
#define HAVE_SETGROUPS 1

/* Define to 1 if you have the `setpgrp' function. */
#define HAVE_SETPGRP 1

/* Yay! Another Linux brokenness. Knowing that setresuid() exists is not
   enough, because RedHat 5.0 declares setresuid() but does not implement it.
   */
#define HAVE_SETRESUID 1

/* Define to 1 if you have the `setrlimit' function. */
#define HAVE_SETRLIMIT 1

/* Define to 1 if you have the `setsid' function. */
#define HAVE_SETSID 1

/* Define to 1 if you have the <shadow.h> header file. */
#define HAVE_SHADOW_H 1

/* Define if you have the shl_load function. */
/* #undef HAVE_SHL_LOAD */

/* Support shared memory features */
#define HAVE_SHM 1

/* Define to 1 if you have the `sigaction' function. */
#define HAVE_SIGACTION 1

/* Define to 1 if you have the <siginfo.h> header file. */
/* #undef HAVE_SIGINFO_H */

/* Define to 1 if you have the <signal.h> header file. */
#define HAVE_SIGNAL_H 1

/* Defined if struct sockaddr_in6 has sin6_len */
#define HAVE_SIN6_LEN_IN_SAI 0

/* Define if sockaddr_in has field sin_len */
#define HAVE_SIN_LEN_IN_SAI 0

/* Define to 1 if you have the `snprintf' function. */
#define HAVE_SNPRINTF 1

/* The system provides sockaddr_un */
#define HAVE_SOCKADDR_UN 1

/* Define to 1 if you have the `socketpair' function. */
#define HAVE_SOCKETPAIR 1

/* socklen_t is defined by the system headers */
#define HAVE_SOCKLEN_T 1

/* SPNEGO support */
/* #undef HAVE_SPNEGO */

/* SSL_CTX_get0_certificate is available */
/* #undef HAVE_SSL_CTX_GET0_CERTIFICATE */

/* Define if sockaddr_storage has field ss_len */
#define HAVE_SS_LEN_IN_SS 0

/* Define to 1 if you have the `statfs' function. */
/* #undef HAVE_STATFS */

/* set to 1 if our system has statvfs(), and if it actually works */
#define HAVE_STATVFS 1

/* Define to 1 if you have the <stdarg.h> header file. */
#define HAVE_STDARG_H 1

/* Define to 1 if you have the <stddef.h> header file. */
#define HAVE_STDDEF_H 1

/* Define to 1 if you have the <stdint.h> header file. */
#define HAVE_STDINT_H 1

/* Define to 1 if you have the <stdio.h> header file. */
#define HAVE_STDIO_H 1

/* Define to 1 if you have the <stdlib.h> header file. */
#define HAVE_STDLIB_H 1

/* Define if stdlibc support std::underlying_type for enums */
#define HAVE_STD_UNDERLYING_TYPE 1

/* Define if c++11 std::uniform_int_distribution is supported */
#define HAVE_STD_UNIFORM_INT_DISTRIBUTION 1

/* Define if c++11 std::uniform_real_distribution is supported */
#define HAVE_STD_UNIFORM_REAL_DISTRIBUTION 1

/* Define to 1 if you have the `strerror' function. */
#define HAVE_STRERROR 1

/* Define to 1 if you have the <strings.h> header file. */
#define HAVE_STRINGS_H 1

/* Define to 1 if you have the <string.h> header file. */
#define HAVE_STRING_H 1

/* Define to 1 if you have the `strlcat' function. */
/* #undef HAVE_STRLCAT */

/* Define to 1 if you have the `strlcpy' function. */
/* #undef HAVE_STRLCPY */

/* MacOS brokenness: strnstr() can overrun on that system */
/* #undef HAVE_STRNSTR */

/* Define to 1 if you have the `strtoll' function. */
#define HAVE_STRTOLL 1

/* Define to 1 if `ip_hl' is a member of `struct iphdr'. */
#define HAVE_STRUCT_IPHDR_IP_HL 1

/* Define to 1 if `nl_inipaddr.in6' is a member of `struct natlookup'. */
/* #undef HAVE_STRUCT_NATLOOKUP_NL_INIPADDR_IN6 */

/* Define to 1 if `nl_realipaddr.in6' is a member of `struct natlookup '. */
/* #undef HAVE_STRUCT_NATLOOKUP_NL_REALIPADDR_IN6___ */

/* The system provides struct rusage */
#define HAVE_STRUCT_RUSAGE 1

/* Define to 1 if `tm_gmtoff' is a member of `struct tm'. */
#define HAVE_STRUCT_TM_TM_GMTOFF 1

/* Sun LDAP SDK support */
/* #undef HAVE_SUN_LDAP_SDK */

/* Define to 1 if you have the <syscall.h> header file. */
#define HAVE_SYSCALL_H 1

/* Define to 1 if you have the `sysconf' function. */
#define HAVE_SYSCONF 1

/* Define to 1 if you have the `syslog' function. */
#define HAVE_SYSLOG 1

/* Define to 1 if you have the <syslog.h> header file. */
#define HAVE_SYSLOG_H 1

/* Define to 1 if you have the <sys/bitypes.h> header file. */
#define HAVE_SYS_BITYPES_H 1

/* Define to 1 if you have the <sys/bswap.h> header file. */
/* #undef HAVE_SYS_BSWAP_H */

/* Define to 1 if you have the <sys/capability.h> header file. */
/* #undef HAVE_SYS_CAPABILITY_H */

/* Define to 1 if you have the <sys/devpoll.h> header file. */
/* #undef HAVE_SYS_DEVPOLL_H */

/* Define to 1 if you have the <sys/dir.h> header file, and it defines `DIR'.
   */
/* #undef HAVE_SYS_DIR_H */

/* Define to 1 if you have the <sys/dl.h> header file. */
/* #undef HAVE_SYS_DL_H */

/* Define to 1 if you have the <sys/endian.h> header file. */
/* #undef HAVE_SYS_ENDIAN_H */

/* Define to 1 if you have the <sys/epoll.h> header file. */
#define HAVE_SYS_EPOLL_H 1

/* Define to 1 if you have the <sys/event.h> header file. */
/* #undef HAVE_SYS_EVENT_H */

/* Define to 1 if you have the <sys/file.h> header file. */
#define HAVE_SYS_FILE_H 1

/* Define to 1 if you have the <sys/ioccom.h> header file. */
/* #undef HAVE_SYS_IOCCOM_H */

/* Define to 1 if you have the <sys/ioctl.h> header file. */
#define HAVE_SYS_IOCTL_H 1

/* Define to 1 if you have the <sys/ipc.cc> header file. */
/* #undef HAVE_SYS_IPC_CC */

/* Define to 1 if you have the <sys/md5.h> header file. */
/* #undef HAVE_SYS_MD5_H */

/* Define to 1 if you have the <sys/mman.h> header file. */
#define HAVE_SYS_MMAN_H 1

/* Define to 1 if you have the <sys/mount.h> header file. */
#define HAVE_SYS_MOUNT_H 1

/* Define to 1 if you have the <sys/msg.h> header file. */
#define HAVE_SYS_MSG_H 1

/* Define to 1 if you have the <sys/ndir.h> header file, and it defines `DIR'.
   */
/* #undef HAVE_SYS_NDIR_H */

/* Define to 1 if you have the <sys/param.h> header file. */
#define HAVE_SYS_PARAM_H 1

/* Define to 1 if you have the <sys/prctl.h> header file. */
#define HAVE_SYS_PRCTL_H 1

/* Define to 1 if you have the <sys/resource.h> header file. */
#define HAVE_SYS_RESOURCE_H 1

/* Define to 1 if you have the <sys/select.h> header file. */
#define HAVE_SYS_SELECT_H 1

/* Define to 1 if you have the <sys/shm.h> header file. */
#define HAVE_SYS_SHM_H 1

/* Define to 1 if you have the <sys/socket.h> header file. */
#define HAVE_SYS_SOCKET_H 1

/* Define to 1 if you have the <sys/sockio.h> header file. */
/* #undef HAVE_SYS_SOCKIO_H */

/* Define to 1 if you have the <sys/statfs.h> header file. */
/* #undef HAVE_SYS_STATFS_H */

/* Define to 1 if you have the <sys/statvfs.h> header file. */
#define HAVE_SYS_STATVFS_H 1

/* Define to 1 if you have the <sys/stat.h> header file. */
#define HAVE_SYS_STAT_H 1

/* Define to 1 if you have the <sys/syscall.h> header file. */
#define HAVE_SYS_SYSCALL_H 1

/* Define to 1 if you have the <sys/sysctl.h> header file. */
#define HAVE_SYS_SYSCTL_H 1

/* Define to 1 if you have the <sys/time.h> header file. */
#define HAVE_SYS_TIME_H 1

/* Define to 1 if you have the <sys/types.h> header file. */
#define HAVE_SYS_TYPES_H 1

/* Define to 1 if you have the <sys/uio.h> header file. */
#define HAVE_SYS_UIO_H 1

/* Define to 1 if you have the <sys/un.h> header file. */
#define HAVE_SYS_UN_H 1

/* Define to 1 if you have the <sys/vfs.h> header file. */
#define HAVE_SYS_VFS_H 1

/* Define to 1 if you have the <sys/wait.h> header file. */
#define HAVE_SYS_WAIT_H 1

/* Define to 1 if you have the `tempnam' function. */
#define HAVE_TEMPNAM 1

/* Define to 1 if you have the `timegm' function. */
#define HAVE_TIMEGM 1

/* Define to 1 if you have the <time.h> header file. */
#define HAVE_TIME_H 1

/* Define to 1 if you have the <tr1/random> header file. */
#define HAVE_TR1_RANDOM 1

/* Define to 1 if std::unique_ptr<T> is supported */
#define HAVE_UNIQUE_PTR 1

/* Define to 1 if you have the <unistd.h> header file. */
#define HAVE_UNISTD_H 1

/* System supports unix sockets */
#define HAVE_UNIXSOCKET 1

/* upad128_t is defined in system headers */
/* #undef HAVE_UPAD128_T */

/* Define to 1 if you have the <utime.h> header file. */
#define HAVE_UTIME_H 1

/* Define to 1 if you have the <valgrind/memcheck.h> header file. */
/* #undef HAVE_VALGRIND_MEMCHECK_H */

/* Define to 1 if you have the <varargs.h> header file. */
/* #undef HAVE_VARARGS_H */

/* Define to 1 if you have the `vfork' function. */
#define HAVE_VFORK 1

/* Define to 1 if you have the `vsnprintf' function. */
#define HAVE_VSNPRINTF 1

/* Define to 1 if you have the <w32api/windows.h> header file. */
/* #undef HAVE_W32API_WINDOWS_H */

/* Define to 1 if you have the <wchar.h> header file. */
#define HAVE_WCHAR_H 1

/* Define if you have PSAPI.DLL on Windows systems */
/* #undef HAVE_WIN32_PSAPI */

/* Define to 1 if you have the <windows.h> header file. */
/* #undef HAVE_WINDOWS_H */

/* Define to 1 if you have the <winldap.h> header file. */
/* #undef HAVE_WINLDAP_H */

/* Define to 1 if you have the <winsock2.h> header file. */
/* #undef HAVE_WINSOCK2_H */

/* Define to 1 if you have the <winsock.h> header file. */
/* #undef HAVE_WINSOCK_H */

/* This value is set to 1 to indicate that the system argz facility works */
#define HAVE_WORKING_ARGZ 1

/* Define to 1 if you have the `write' function. */
#define HAVE_WRITE 1

/* Define to 1 if you have the <ws2tcpip.h> header file. */
/* #undef HAVE_WS2TCPIP_H */

/* Define to 1 if you have the `__htole16' function. */
/* #undef HAVE___HTOLE16 */

/* Define to 1 if you have the `__htole32' function. */
/* #undef HAVE___HTOLE32 */

/* Define to 1 if you have the `__le16toh' function. */
/* #undef HAVE___LE16TOH */

/* Define to 1 if you have the `__le32toh' function. */
/* #undef HAVE___LE32TOH */

/* Define to 1 if you have the `__res_init' function. */
#define HAVE___RES_INIT 1

/* Enable ICAP client features in Squid */
#define ICAP_CLIENT 1

/* Enable support for Transparent Proxy on systems using FreeBSD IPFW-style
   firewalling. */
#define IPFW_TRANSPARENT 0

/* Enable support for IPF-style transparent proxying */
#define IPF_TRANSPARENT 0

/* A dangerous feature which causes Squid to kill its parent process
   (presumably the RunCache script) upon receipt of SIGTERM or SIGINT.
   Deprecated, Use with caution. */
#define KILL_PARENT_OPT 0

/* libcap2 headers are broken and clashing with glibc */
#define LIBCAP_BROKEN 0

/* libresolv.a has been hacked to export _dns_ttl_ */
#define LIBRESOLV_DNS_TTL_HACK 0

/* Enable support for Transparent Proxy on Linux via Netfilter */
#define LINUX_NETFILTER 1

/* Define if the OS needs help to load dependent libraries for dlopen(). */
/* #undef LTDL_DLOPEN_DEPLIBS */

/* Define to the system default library search path. */
#define LT_DLSEARCH_PATH "/lib:/usr/lib:/usr/lib/x86_64-linux-gnu/libfakeroot:/usr/local/lib:/usr/local/lib/x86_64-linux-gnu:/lib/x86_64-linux-gnu:/usr/lib/x86_64-linux-gnu"

/* The archive extension */
#define LT_LIBEXT "a"

/* The archive prefix */
#define LT_LIBPREFIX "lib"

/* Define to the extension used for runtime loadable modules, say, ".so". */
#define LT_MODULE_EXT ".so"

/* Define to the name of the environment variable that determines the run-time
   module search path. */
#define LT_MODULE_PATH_VAR "LD_LIBRARY_PATH"

/* Define to the sub-directory where libtool stores uninstalled libraries. */
#define LT_OBJDIR ".libs/"

/* Define to the shared library suffix, say, ".dylib". */
/* #undef LT_SHARED_EXT */

/* Define to the shared archive member specification, say "(shr.o)". */
/* #undef LT_SHARED_LIB_MEMBER */

/* If MAXPATHLEN has not been defined */
/* #undef MAXPATHLEN */

/* If we need to declare sys_errlist as extern */
#define NEED_SYS_ERRLIST 1

/* Define if dlsym() requires a leading underscore in symbol names. */
/* #undef NEED_USCORE */

/* Name of package */
#define PACKAGE "squid"

/* Define to the address where bug reports for this package should be sent. */
#define PACKAGE_BUGREPORT "http://bugs.squid-cache.org/"

/* Define to the full name of this package. */
#define PACKAGE_NAME "Squid Web Proxy"

/* Define to the full name and version of this package. */
#define PACKAGE_STRING "Squid Web Proxy 4.7-20190507-r2e17b0261"

/* Define to the one symbol short name of this package. */
#define PACKAGE_TARNAME "squid"

/* Define to the home page for this package. */
#define PACKAGE_URL ""

/* Define to the version of this package. */
#define PACKAGE_VERSION "4.7-20190507-r2e17b0261"

/* Defined to const or empty depending on the style used by the OS to refer to
   the PAM message dialog func */
/* #undef PAM_CONV_FUNC_CONST_PARM */

/* Enable support for PF-style transparent proxying */
#define PF_TRANSPARENT 0

/* Print stack traces on fatal errors */
#define PRINT_STACK_TRACE 0

/* Compiler supports %zu printf macro */
#define PRIuSIZE "zu"

/* Base type of the second argument to recv(2) */
#define RECV_ARG_TYPE char

/* The size of `int64_t', as computed by sizeof. */
#define SIZEOF_INT64_T 8

/* The size of `long', as computed by sizeof. */
#define SIZEOF_LONG 8

/* The size of `off_t', as computed by sizeof. */
#define SIZEOF_OFF_T 8

/* The size of `size_t', as computed by sizeof. */
#define SIZEOF_SIZE_T 8

/* The size of `void *', as computed by sizeof. */
#define SIZEOF_VOID_P 8

/* Squid extended build info field for "squid -v" output */
#define SQUID_BUILD_INFO ""

/* configure command line used to configure Squid */
#define SQUID_CONFIGURE_OPTIONS " --enable-ltdl-convenience"

/* Define to const if X509_get0_signature() accepts const parameters; define
   as empty otherwise. Don't leave it undefined! */
/* #undef SQUID_CONST_X509_GET0_SIGNATURE_ARGS */

/* UDP receive buffer size */
#define SQUID_DETECT_UDP_SO_RCVBUF 163840

/* UDP send buffer size */
#define SQUID_DETECT_UDP_SO_SNDBUF 163840

/* Maximum number of open filedescriptors */
#define SQUID_MAXFD 32768

/* Define to enable SNMP monitoring of Squid */
#define SQUID_SNMP 1

/* "Define to 1 if the SSL_get_certificate crashes squid" */
/* #undef SQUID_SSLGETCERTIFICATE_BUGGY */

/* "Define to 1 if the TXT_DB uses OPENSSL_PSTRING data member" */
/* #undef SQUID_SSLTXTDB_PSTRINGDATA */

/* "Define to 1 to use squid workaround for buggy versions of
   sk_OPENSSL_PSTRING_value" */
/* #undef SQUID_STACKOF_PSTRINGDATA_HACK */

/* TCP receive buffer size */
#define SQUID_TCP_SO_RCVBUF 65535

/* TCP send buffer size */
#define SQUID_TCP_SO_SNDBUF 32768

/* "Define to 1 if the SSL_get_new_ex_index() dup callback accepts 'const
   CRYPTO_EX_DATA *'" */
/* #undef SQUID_USE_CONST_CRYPTO_EX_DATA_DUP */

/* "Define to 1 if the SSL_CTX_new and similar openSSL API functions require
   'const SSL_METHOD *'" */
/* #undef SQUID_USE_CONST_SSL_METHOD */

/* "Define to 1 if the SSL_CTX_sess_set_get_cb() callback accepts a const ID
   argument" */
/* #undef SQUID_USE_CONST_SSL_SESSION_CBID */

/* "Define to 1 if hello message can be overwritten in SSL struct" */
/* #undef SQUID_USE_OPENSSL_HELLO_OVERWRITE_HACK */

/* "Define to 1 to use squid workaround for SSL_get_certificate" */
/* #undef SQUID_USE_SSLGETCERTIFICATE_HACK */

/* "Define to 1 to use squid workaround for openssl IMPLEMENT_LHASH_* type
   conversion errors" */
/* #undef SQUID_USE_SSLLHASH_HACK */

/* If using the C implementation of alloca, define if you know the
   direction of stack growth for your system; otherwise it will be
   automatically deduced at runtime.
	STACK_DIRECTION > 0 => grows toward higher addresses
	STACK_DIRECTION < 0 => grows toward lower addresses
	STACK_DIRECTION = 0 => direction of growth unknown */
/* #undef STACK_DIRECTION */

/* Define to 1 if you have the ANSI C header files. */
#define STDC_HEADERS 1

/* Define to 1 if your <sys/time.h> declares `struct tm'. */
/* #undef TM_IN_SYS_TIME */

/* common adaptation support */
#define USE_ADAPTATION 1

/* Apple Kerberos support is available */
/* #undef USE_APPLE_KRB5 */

/* Enable support for authentication */
#define USE_AUTH 1

/* Use Cache Digests for locating objects in neighbor caches. */
#define USE_CACHE_DIGESTS 0

/* Enable support for cbdata debug information */
#define USE_CBDATA_DEBUG 0

/* Enable chunked Memory Pools support (experimental) */
#define USE_CHUNKEDMEMPOOLS 0

/* Traffic management via "delay pools". */
/* #undef USE_DELAY_POOLS */

/* Use /dev/poll for the IO loop */
/* #undef USE_DEVPOLL */

/* DiskIO modules are expected to be available. */
#define USE_DISKIO 1

/* Whether to use eCAP support */
#define USE_ECAP 0

/* Use epoll() for the IO loop */
#define USE_EPOLL 1

/* Use multi-language support on error pages */
#define USE_ERR_LOCALES 1

/* Enable Forw/Via database */
#define USE_FORW_VIA_DB 0

/* GNU Kerberos support is available */
/* #undef USE_GNUGSS */

/* Define if we should use GNU regex */
#define USE_GNUREGEX 0

/* GnuTLS support is available */
/* #undef USE_GNUTLS */

/* Heimdal Kerberos support is available */
/* #undef USE_HEIMDAL_KRB5 */

/* Define this to include code for the Hypertext Cache Protocol (HTCP) */
#define USE_HTCP 1

/* Define to enable code which volates the HTTP standard specification */
#define USE_HTTP_VIOLATIONS 1

/* Define to use Squid ICMP and Network Measurement features (highly
   recommended!) */
/* #undef USE_ICMP */

/* Support for Ident (RFC 931) lookups */
#define USE_IDENT 1

/* Enable support for IPv6 */
#define USE_IPV6 1

/* Use kqueue() for the IO loop */
/* #undef USE_KQUEUE */

/* Enable code for assisting in finding memory leaks. Not for the faint of
   heart */
#define USE_LEAKFINDER 0

/* use libcap to set capabilities required for TPROXY */
#define USE_LIBCAP 0

/* Enable support for QOS netfilter mark preservation */
#define USE_LIBNETFILTERCONNTRACK 0

/* Support Loadable Modules */
#define USE_LOADABLE_MODULES 1

/* MIT Kerberos support is available */
/* #undef USE_MIT_KRB5 */

/* Enable support for /dev/pf NAT lookups */
#define USE_NAT_DEVPF 0

/* OpenSSL support is available */
/* #undef USE_OPENSSL */

/* Use poll() for the IO loop */
/* #undef USE_POLL */

/* Enable Zero Penalty Hit QOS. When set, Squid will alter the TOS field of
   HIT responses to help policing network traffic */
#define USE_QOS_TOS 1

/* Use select() for the IO loop */
/* #undef USE_SELECT */

/* Use Winsock select() for the IO loop */
/* #undef USE_SELECT_WIN32 */

/* Workaround IPFilter minor_t breakage */
/* #undef USE_SOLARIS_IPFILTER_MINOR_T_HACK */

/* Solaris Kerberos support is available */
/* #undef USE_SOLARIS_KRB5 */

/* Compile the ESI processor */
#define USE_SQUID_ESI 1

/* Define this to include code which lets you use ethernet addresses. This
   code uses API initially defined in 4.4-BSD. */
#define USE_SQUID_EUI 1

/* Use ssl-crtd daemon */
#define USE_SSL_CRTD 0

/* Enable extensions on AIX 3, Interix.  */
#ifndef _ALL_SOURCE
/* # undef _ALL_SOURCE */
#endif
/* Enable GNU extensions on systems that have them.  */
#ifndef _GNU_SOURCE
/* # undef _GNU_SOURCE */
#endif
/* Enable threading extensions on Solaris.  */
#ifndef _POSIX_PTHREAD_SEMANTICS
/* # undef _POSIX_PTHREAD_SEMANTICS */
#endif
/* Enable extensions on HP NonStop.  */
#ifndef _TANDEM_SOURCE
/* # undef _TANDEM_SOURCE */
#endif
/* Enable general extensions on Solaris.  */
#ifndef __EXTENSIONS__
/* # undef __EXTENSIONS__ */
#endif


/* Enable useage of unlinkd */
#define USE_UNLINKD 1

/* Define to enable WCCP */
#define USE_WCCP 1

/* Define to enable WCCP V2 */
#define USE_WCCPv2 1

/* Enable code supporting MS Windows service mode */
#define USE_WIN32_SERVICE 0

/* Define to enable CPU profiling within Squid */
#define USE_XPROF_STATS 0

/* Version number of package */
#define VERSION "4.7-20190507-r2e17b0261"

/* Valgrind memory debugger support */
#define WITH_VALGRIND 0

/* Define WORDS_BIGENDIAN to 1 if your processor stores words with the most
   significant byte first (like Motorola and SPARC, unlike Intel). */
#if defined AC_APPLE_UNIVERSAL_BUILD
# if defined __BIG_ENDIAN__
#  define WORDS_BIGENDIAN 1
# endif
#else
# ifndef WORDS_BIGENDIAN
/* #  undef WORDS_BIGENDIAN */
# endif
#endif

/* Show malloc statistics in status page */
#define XMALLOC_STATISTICS 0

/* Enable support for the X-Accelerator-Vary HTTP header */
#define X_ACCELERATOR_VARY 0

/* Define to 1 if on MINIX. */
/* #undef _MINIX */

/* Define to 2 if the system does not provide POSIX.1 features except with
   this defined. */
/* #undef _POSIX_1_SOURCE */

/* Define to 1 if you need to in order for `stat' and other things to work. */
/* #undef _POSIX_SOURCE */

/* Nameserver Counter for IPv6 _res */
/* #undef _SQUID_RES_NSADDR6_COUNT */

/* If _res_ext structure has nsaddr_list member */
/* #undef _SQUID_RES_NSADDR6_LARRAY */

/* If _res structure has _ext.nsaddrs member */
/* #undef _SQUID_RES_NSADDR6_LPTR */

/* Nameserver counter for IPv4 _res */
#define _SQUID_RES_NSADDR_COUNT _res.nscount

/* If _res structure has ns_list member */
#define _SQUID_RES_NSADDR_LIST _res.nsaddr_list

/* Define for Solaris 2.5.1 so the uint32_t typedef from <sys/synch.h>,
   <pthread.h>, or <semaphore.h> is not used. If the typedef were allowed, the
   #define below would cause a syntax error. */
/* #undef _UINT32_T */

/* Define for Solaris 2.5.1 so the uint64_t typedef from <sys/synch.h>,
   <pthread.h>, or <semaphore.h> is not used. If the typedef were allowed, the
   #define below would cause a syntax error. */
/* #undef _UINT64_T */

/* Define for Solaris 2.5.1 so the uint8_t typedef from <sys/synch.h>,
   <pthread.h>, or <semaphore.h> is not used. If the typedef were allowed, the
   #define below would cause a syntax error. */
/* #undef _UINT8_T */

/* Include inline methods into header file */
#define _USE_INLINE_ 1

/* Define so that glibc/gnulib argp.h does not typedef error_t. */
/* #undef __error_t_defined */

/* Define to empty if `const' does not conform to ANSI C. */
/* #undef const */

/* Define to a type to use for 'error_t' if it is not otherwise available. */
/* #undef error_t */

/* Define to `int' if <sys/types.h> doesn't define. */
/* #undef gid_t */

/* Define to the type of a signed integer type of width exactly 16 bits if
   such a type exists and the standard includes do not define it. */
/* #undef int16_t */

/* Define to the type of a signed integer type of width exactly 32 bits if
   such a type exists and the standard includes do not define it. */
/* #undef int32_t */

/* Define to the type of a signed integer type of width exactly 64 bits if
   such a type exists and the standard includes do not define it. */
/* #undef int64_t */

/* Define to the type of a signed integer type of width exactly 8 bits if such
   a type exists and the standard includes do not define it. */
/* #undef int8_t */

/* Leave undefined if nullptr is supported */
/* #undef nullptr */

/* Define to `long int' if <sys/types.h> does not define. */
/* #undef off_t */

/* Define to `int' if <sys/types.h> does not define. */
/* #undef pid_t */

/* Define to `unsigned int' if <sys/types.h> does not define. */
/* #undef size_t */

/* Define to `int' if <sys/types.h> does not define. */
/* #undef ssize_t */

/* Define to `int' if <sys/types.h> doesn't define. */
/* #undef uid_t */

/* Define to the type of an unsigned integer type of width exactly 16 bits if
   such a type exists and the standard includes do not define it. */
/* #undef uint16_t */

/* Define to the type of an unsigned integer type of width exactly 32 bits if
   such a type exists and the standard includes do not define it. */
/* #undef uint32_t */

/* Define to the type of an unsigned integer type of width exactly 64 bits if
   such a type exists and the standard includes do not define it. */
/* #undef uint64_t */

/* Define to the type of an unsigned integer type of width exactly 8 bits if
   such a type exists and the standard includes do not define it. */
/* #undef uint8_t */

/* Leave undefined if std::unique_ptr<T> is supported */
/* #undef unique_ptr */
