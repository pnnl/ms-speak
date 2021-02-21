#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sqlite3.h> 
#include <stdbool.h>
#include <libxml/xmlmemory.h>   // libxml2-dev,  /usr/include/libxml2/libxml
#include <libxml/parser.h>
#include <curl/curl.h>

#define MAX_DB_NAMELEN  50
#define MAX_DB_HOSTLEN  15
#define MAX_DB_ZIPLEN    5
#define APIBUFFLEN     250

#define WILDCARD_STR "-1"
#define WILDCARD -1

#define DB_COLNAME_TESTER	"Tester"
#define DB_COLNAME_HOST		"Host"
#define DB_COLNAME_APPID	"AppId"
#define DB_COLNAME_ZIPCODE	"Zipcode"
#define DB_COLNAME_ENDPOINT "Endpoint"
#define DB_COLNAME_METHOD	"Method"
#define DB_COLNAME_MAXTEMP	"maxTemp"
#define DB_COLNAME_MINTEMP	"minTemp"
#define DB_COLNAME_MAXHOUR	"maxHour"
#define DB_COLNAME_MINHOUR	"minHour"
#define DB_COLNAME_NUMREQ	"numReq"
#define DB_COLNAME_EMAIL	"email"

typedef signed long gint64;
typedef char   gchar;

// strncpy() Warning: If there is no null byte among the first n bytes of src, 
//		the string placed in dest will not be null-terminated.
typedef struct _bizdata {
	gint64 m_numReq;
	gint64 m_minTemp;
	gint64 m_maxTemp;
	gint64 m_minHour;
	gint64 m_maxHour;
	gint64 m_ValidRequestNum;
	gint64 m_TotalRequestNum;
	gchar  m_Tester[MAX_DB_NAMELEN+1];
	gchar  m_Host[MAX_DB_HOSTLEN+1];
	gchar  m_AppId[MAX_DB_NAMELEN+1];
	gchar  m_Zipcode[MAX_DB_ZIPLEN+1];
	gchar  m_EndPoint[MAX_DB_NAMELEN+1];
	gchar  m_Method[MAX_DB_NAMELEN+1];
	gchar  m_Email[MAX_DB_NAMELEN+1];
} BIZ_DATA;
BIZ_DATA *pBizRecords;
int NumBizRecs;
int RowCnt;

struct string {
    char *ptr;
    size_t len;
};

void init_string(struct string *);
size_t writefunc(void *, size_t, size_t, struct string *);

/*
typedef int (*sqlite3_callback)(
   void*,    // Data provided in the 4th argument of sqlite3_exec() 
   int,      // The number of columns in row 
   char**,   // An array of strings representing fields in the row 
   char**    // An array of strings representing column names 
);
*/

static int callback(void *data, int colcount, char **values, char **columns){
	int i;
	if( RowCnt < NumBizRecs ){
		BIZ_DATA *pBizRecs = (BIZ_DATA *)data;
		BIZ_DATA *pBzd = &pBizRecs[RowCnt++];
		pBzd->m_ValidRequestNum = 0;
		pBzd->m_TotalRequestNum = 0;		
		for(i = 0; i<colcount; i++){
			gchar *curr_key = columns[i];
			// Note, any non-existant keys will have already been preset to WILDCARD
			if( !strcmp(curr_key, DB_COLNAME_NUMREQ) ){
				pBzd->m_numReq = atoll(values[i]);
			}
			else if( !strcmp(curr_key, DB_COLNAME_MINTEMP) ){
				pBzd->m_minTemp = atoll(values[i]);
			}
			else if( !strcmp(curr_key, DB_COLNAME_MAXTEMP) ){
				pBzd->m_maxTemp = atoll(values[i]);
			}
			else if( !strcmp(curr_key, DB_COLNAME_MINHOUR) ){
				pBzd->m_minHour = atoll(values[i]);
			}
			else if( !strcmp(curr_key, DB_COLNAME_MAXHOUR) ){
				pBzd->m_maxHour = atoll(values[i]);
			}
			else if( !strcmp(curr_key, DB_COLNAME_TESTER) ){
				strncpy( pBzd->m_Tester, values[i], MAX_DB_NAMELEN );
			}
			else if( !strcmp(curr_key, DB_COLNAME_HOST) ){
				strncpy( pBzd->m_Host, values[i], MAX_DB_HOSTLEN );
			}
			else if( !strcmp(curr_key, DB_COLNAME_APPID) ){
				if( values[i] )
					strncpy( pBzd->m_AppId, values[i], MAX_DB_NAMELEN );
			}
			else if( !strcmp(curr_key, DB_COLNAME_ZIPCODE) ){
				if( values[i] )
					strncpy( pBzd->m_Zipcode, values[i], MAX_DB_ZIPLEN );
			}
			else if( !strcmp(curr_key, DB_COLNAME_ENDPOINT) ){
				strncpy( pBzd->m_EndPoint, values[i], MAX_DB_NAMELEN );
			}
			else if( !strcmp(curr_key, DB_COLNAME_METHOD) ){
				strncpy( pBzd->m_Method, values[i], MAX_DB_NAMELEN );
			}
			else if( !strcmp(curr_key, DB_COLNAME_EMAIL) ){
				if( values[i] )
					strncpy( pBzd->m_Email, values[i], MAX_DB_NAMELEN );
			}
			else{
				fprintf(stderr, "Key Lookup Sanity Failure: %s\n", curr_key);
			}
		}
	}
	else{
		fprintf(stderr, "Row Count Sanity Failure: %d\n", RowCnt);
	}
   /*
	* If callback returns non-zero, the sqlite3_exec() routine returns 
	* SQLITE_ABORT without invoking the callback again and without running
	*  any subsequent SQL statements.
	*/
   return 0;
}

#ifdef _WEATHER	
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
const static char *api_endpoint = "http://api.openweathermap.org/data/2.5/weather?zip=%s&appid=%s&units=imperial&mode=xml";
char api_buffer[APIBUFFLEN+1];
#endif

void init_string(struct string *s) {
    s->len = 0;
    s->ptr = malloc(s->len+1);
    if (s->ptr == NULL) {
      fprintf(stderr, "in init_string(), malloc() failed\n");
      exit(EXIT_FAILURE);
    }
    s->ptr[0] = '\0';
}

size_t writefunc(void *ptr, size_t size, size_t nmemb, struct string *s)
{
    size_t new_len = s->len + size*nmemb;
    s->ptr = realloc(s->ptr, new_len+1);
    if (s->ptr == NULL) {
      fprintf(stderr, "realloc() failed\n");
      exit(EXIT_FAILURE);
    }
    memcpy(s->ptr+s->len, ptr, size*nmemb);
    s->ptr[new_len] = '\0';
    s->len = new_len;

    return size*nmemb;
}

typedef struct _hostrecs{
	BIZ_DATA *m_first;
	int		  m_num;
} HOST_RECS;

// GetHostRecs
bool GetHostRecs( BIZ_DATA *pBizRecs, int numRecs, 
				  const char *pHost, HOST_RECS *pHRecs ){
	bool bRet = false;
	if( pBizRecs && pHost && pHRecs ){
		pHRecs->m_first = NULL;
		pHRecs->m_num = 0;
		for( int i=0; i<numRecs; i++ ){
			if( !strcmp(pBizRecs->m_Host, pHost) ){ //  found host, find the rest now
				if( !bRet ){
					pHRecs->m_first = pBizRecs;
					bRet = true;
				}
				pHRecs->m_num++;
			}
			else if( bRet )
				break;
			pBizRecs++;
		}
	}
	return bRet;
}

// sudo apt-get install libsqlite3-dev -lcurl -DDEBUG
// make -f icapMakefile
// gcc IcapTest.c -o IcapTest -lsqlite3
int main(int argc, char* argv[]) {
	HOST_RECS hRecs; // host records should be consecutive by tester due to 'ORDER BY Tester' query
	const char *clientip;
	sqlite3 *db;
	char *zErrMsg = 0;
	int rc;
	int iRet = -1;
	char *sql;

	/* Open database */
	rc = sqlite3_open_v2("BizRules.db", &db, SQLITE_OPEN_READONLY, NULL);  
	if( rc ) {
		fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(db));
		return(iRet);
	} else {
		;//fprintf(stderr, "Opened database successfully\n");
	}
	sql = "SELECT Count(*)"
		" FROM rules"
		" INNER JOIN endpoints ON endpoints.id = rules.endpoint"
		" INNER JOIN methods ON methods.id = rules.method"
		" INNER JOIN testers ON testers.id = rules.tester;";
	sqlite3_stmt *stmt;
	rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
	if (rc != SQLITE_OK) {
		fprintf(stderr, "PREPARE failed: %s\n", sqlite3_errmsg(db));
		return(iRet);
	}
	bool bOnce = false;
	while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
		if( !bOnce ){
			NumBizRecs = sqlite3_column_int(stmt, 0); // sqlite3_column_text
			//printf("NumBizRecs = %d\n", NumBizRecs);
			bOnce = true;
		}
		else{
			fprintf(stderr, "SANITY FAILURE: %s\n", "mutliple rows for Count(*)");
			sqlite3_finalize(stmt);	
			return(iRet);
		}
	}
	if (rc != SQLITE_DONE) {
		fprintf(stderr, "SELECT failed: %s\n", sqlite3_errmsg(db));
		sqlite3_finalize(stmt);	
		return(iRet);
	}
	sqlite3_finalize(stmt);	

	size_t size = NumBizRecs * sizeof(BIZ_DATA);
	RowCnt = 0;
	pBizRecords = (BIZ_DATA *)calloc(1,size); // assure all string buffs will be null-termed
	for( int i=0; i<NumBizRecs; i++ ){
		pBizRecords[i].m_numReq = WILDCARD; // preset for any missing fields in DB
		pBizRecords[i].m_minTemp = WILDCARD;
		pBizRecords[i].m_maxTemp = WILDCARD;
		pBizRecords[i].m_minHour = WILDCARD;
		pBizRecords[i].m_maxHour = WILDCARD;
	}
	
	sql = "SELECT testers.Name as Tester, testers.Host, testers.AppId, testers.Zipcode, endpoints.name as Endpoint, methods.name as Method,"
		"rules.maxTemp,rules.minTemp,rules.maxHour,rules.minHour,rules.numReq,rules.email"
		" FROM rules"
		" INNER JOIN endpoints ON endpoints.id = rules.endpoint"
		" INNER JOIN methods ON methods.id = rules.method"
		" INNER JOIN testers ON testers.id = rules.tester"
		" ORDER BY Tester;";

	/* Execute SQL statement 
		The fourth parameter of sqlite3_exec can be used to pass information to the callback.
		A pointer to a struct to fill would be useful.	 
		*/
	rc = sqlite3_exec(db, sql, callback, (void*)pBizRecords, &zErrMsg);
	if( rc != SQLITE_OK ) {
		fprintf(stderr, "SQL error: %s\n", zErrMsg);
		sqlite3_free(zErrMsg);
	} else {
		;//fprintf(stdout, "Operation done successfully\n");
	}
	sqlite3_close(db);

	if( RowCnt > NumBizRecs ){
		fprintf(stderr, "SANITY FAILURE: %s\n", "excess rows for query");
	}
	else{
		//fprintf(stdout, "Rules Read Successfully\n");
		clientip = "172.31.153.24"; // should be extracted by icap from msp packet
		if( GetHostRecs( pBizRecords, NumBizRecs, clientip, &hRecs ) )
		{
			iRet = 0;
			BIZ_DATA *pBizRecs = hRecs.m_first;
			for( int i=0; i<hRecs.m_num; i++ ){
				printf("Record %d:\n  Tester: %s, Host: %s, AppId: %s, Zip: %s\n",
					i,pBizRecs->m_Tester,pBizRecs->m_Host,pBizRecs->m_AppId, pBizRecs-> m_Zipcode);
				printf("          Endpoint: %s, Method: %s\n",pBizRecs->m_EndPoint,pBizRecs->m_Method);
				printf("          numReq: %ld, maxTemp: %ld, minTemp: %ld, maxHour: %ld, minHour: %ld\n",
					pBizRecs->m_numReq,pBizRecs->m_maxTemp,pBizRecs->m_minTemp,pBizRecs->m_maxHour,pBizRecs->m_minHour);
				printf("          Email: %s\n",pBizRecs->m_Email);
				pBizRecs++;
			}
		}else{
			fprintf(stderr, "No Host Records Found For Host '%s'\n", clientip);
		}
	}
#ifdef _WEATHER	
	if( iRet == 0 )
	{
		CURL *curl;
		CURLcode res;
		curl = curl_easy_init();
		if(curl)
		{
			struct string s;
			init_string(&s);
			snprintf(api_buffer, APIBUFFLEN, api_endpoint, hRecs.m_first->m_Zipcode, hRecs.m_first->m_AppId );

			curl_easy_setopt(curl, CURLOPT_URL, api_buffer);
			curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, writefunc);
			curl_easy_setopt(curl, CURLOPT_WRITEDATA, &s);
			curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0); // Verify the SSL certificate, 0 (zero) means it doesn't.
			//curl_easy_setopt(curl, CURLOPT_CAPATH , getenv("SSL_CERT_DIR"));

			puts("*** curl_easy_perform(curl) ***");
			res = curl_easy_perform(curl);
			if(res != CURLE_OK) {
				fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
			} else {
				printf("string len: %ld\n",s.len);
				printf("%s\n",s.ptr);
				xmlNodePtr cur;
				xmlDocPtr xmlDoc;
				xmlDoc = xmlParseMemory(s.ptr, s.len);
				if (xmlDoc == NULL) {
					printf("XML Document not parsed successfully.\n");
					return 0;
				}
				cur = xmlDocGetRootElement(xmlDoc);
				if (cur == NULL) {
					printf("Failed to get XML ROOT\n");
					xmlFreeDoc(xmlDoc);
					return 0;
				}
				cur = cur->xmlChildrenNode;
				printf("\n\n");
				while (cur != NULL)
				{
					if ((!xmlStrcmp(cur->name, (const xmlChar *)"temperature")))
					{
						xmlChar *key;
						if(cur->xmlChildrenNode == NULL){
							key = xmlGetProp(cur, (const unsigned char *)"value");
							printf("Current Temp: %s\n", key);
							xmlFree(key);
							key = xmlGetProp(cur, (const unsigned char *)"min");
							printf("Min Temp: %s\n", key);
							xmlFree(key);
							key = xmlGetProp(cur, (const unsigned char *)"max");
							printf("Max Temp: %s\n", key);
							xmlFree(key);
							key = xmlGetProp(cur, (const unsigned char *)"unit");
							printf("Temp Units: %s\n", key);
							xmlFree(key);
						}	
					}
					cur = cur->next;
				}			
				xmlFreeDoc(xmlDoc);
				free(s.ptr);
			}
			curl_easy_cleanup(curl); 
		}
	}
#endif	
	
	return iRet;
}

