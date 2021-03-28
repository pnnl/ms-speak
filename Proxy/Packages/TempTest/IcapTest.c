#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sqlite3.h> 
#include <stdbool.h>
#include <libxml/xmlmemory.h>   // libxml2-dev,  /usr/include/libxml2/libxml
#include <libxml/parser.h>
#include <curl/curl.h>

#define MAX_DB_NAMELEN  50
#define MAX_DB_ZIPLEN    5

#define WILDCARD_STR "-1"
#define WILDCARD -1

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

typedef signed long gint64;
typedef char   gchar;

// strncpy() Warning: If there is no null byte among the first n bytes of src, 
//		the string placed in dest will not be null-terminated.
typedef struct _tester {
	gchar  m_Tester[MAX_DB_NAMELEN+1];
	gchar  m_AppId[MAX_DB_NAMELEN+1];
	gchar  m_Zipcode[MAX_DB_ZIPLEN+1];
} TESTER_DATA;
typedef struct _bizrule {
	gint64 m_numReq;
	gint64 m_numRPH;
	gint64 m_minTemp;
	gint64 m_maxTemp;
	gint64 m_minHour;
	gint64 m_maxHour;
	gint64 m_ValidRequestNum;
	gint64 m_TotalRequestNum;
	gchar  m_Function[MAX_DB_NAMELEN+1];
	gchar  m_EndPoint[MAX_DB_NAMELEN+1];
	gchar  m_Method[MAX_DB_NAMELEN+1];
	gchar  m_Email[MAX_DB_NAMELEN+1];
} BIZ_RULE;
TESTER_DATA	*pTester;
BIZ_RULE	*pBizRules;
int NumBizRules;
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
	if( RowCnt < NumBizRules ){
		BIZ_RULE *pBizRecs = (BIZ_RULE *)data;
		BIZ_RULE *pBzd = &pBizRecs[RowCnt++];
		pBzd->m_ValidRequestNum = 0;
		pBzd->m_TotalRequestNum = 0;		
		for(i = 0; i<colcount; i++){
			if( !values[i] )
				continue;
			gchar *curr_key = columns[i];
			// Note, any non-existant keys will have already been preset to WILDCARD
			if( !strcmp(curr_key, DB_COLNAME_NUMREQ) ){
				pBzd->m_numReq = atoll(values[i]);
			}
			else if( !strcmp(curr_key, DB_COLNAME_NUMRPH) ){
				pBzd->m_numRPH = atoll(values[i]);
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
				if( RowCnt == 1 ){ // we only need store Tester name once
					strncpy( pTester->m_Tester, values[i], MAX_DB_NAMELEN );
				}				
			}
			else if( !strcmp(curr_key, DB_COLNAME_APPID) ){
				if( RowCnt == 1 ){
					strncpy( pTester->m_AppId, values[i], MAX_DB_NAMELEN );
				}				
			}
			else if( !strcmp(curr_key, DB_COLNAME_ZIPCODE) ){
				if( RowCnt == 1 ){
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
#define APIBUFFLEN     250
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
const static char *api_endpoint = "http://api.openweathermap.org/data/2.5/weather?appid=%s&zip=%s&units=imperial&mode=xml";
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

#define SQL_FROM_QUERY " FROM rules"\
		" INNER JOIN functions ON functions.id = rules.function"\
		" INNER JOIN endpoints ON endpoints.id = rules.endpoint"\
		" INNER JOIN methods ON methods.id = rules.method"\
		" INNER JOIN testers ON testers.id = rules.tester"\
		" WHERE( rules.Tester =(SELECT Tester FROM ActiveTester));"\

// sudo apt-get install libsqlite3-dev
// make -f icapMakefile		./IcapTest
// gcc IcapTest.c -o IcapTest -lsqlite3 -lcurl -lxml2
int main(int argc, char* argv[]) {
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
		
	sql = "SELECT Count(*)" SQL_FROM_QUERY;  // get coount of rules for active counter

	sqlite3_stmt *stmt;
	rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
	if (rc != SQLITE_OK) {
		fprintf(stderr, "PREPARE failed: %s\n", sqlite3_errmsg(db));
		fprintf(stderr, "QUERY: %s\n", sql);
		return(iRet);
	}
	bool bOnce = false;
	while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
		if( !bOnce ){
			NumBizRules = sqlite3_column_int(stmt, 0); // sqlite3_column_text
			//printf("NumBizRules = %d\n", NumBizRules);
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

	if( NumBizRules == 0 ){
		fprintf(stderr, "SANITY FAILURE: %s\n", "No Active Tester Rules Found");
		return(iRet);
	}else{
		printf( "%d Active Tester Rules Found\n", NumBizRules);
	}
	
	size_t size = NumBizRules * sizeof(BIZ_RULE);
	RowCnt = 0;
	
	pTester = (TESTER_DATA *)calloc(1,sizeof(TESTER_DATA)); // assure all string buffs will be null-termed
	pBizRules = (BIZ_RULE *)calloc(1,size);
	for( int i=0; i<NumBizRules; i++ ){
		pBizRules[i].m_numReq = WILDCARD; // preset for any missing fields in DB
		pBizRules[i].m_numRPH = WILDCARD;
		pBizRules[i].m_minTemp = WILDCARD;
		pBizRules[i].m_maxTemp = WILDCARD;
		pBizRules[i].m_minHour = WILDCARD;
		pBizRules[i].m_maxHour = WILDCARD;
	}
	
	/* Execute SQL statement 
	The fourth parameter of sqlite3_exec can be used to pass information to the callback.
	A pointer to a struct to fill would be useful.	
	, functions.Name
	*/
	sql = "SELECT testers.Name as Tester, testers.AppId, testers.Zipcode, functions.Name as Function, endpoints.name as Endpoint, methods.name as Method,"
		"rules.maxTemp,rules.minTemp,rules.maxHour,rules.minHour,rules.numReq,rules.numRPH,rules.email"
		 SQL_FROM_QUERY;	
	rc = sqlite3_exec(db, sql, callback, (void*)pBizRules, &zErrMsg);
	if( rc != SQLITE_OK ) {
		fprintf(stderr, "SQL error getting Active Rules: %s\n", zErrMsg);
		sqlite3_free(zErrMsg);
		return(iRet);
	} else {
		;//fprintf(stdout, "Operation done successfully\n");
	}
	sqlite3_close(db);

	if( RowCnt > NumBizRules ){
		fprintf(stderr, "SANITY FAILURE: %s\n", "excess rows for query");
	}
	else{
		iRet = 0;
		printf("Tester: %s, AppId: %s, Zip: %s\n", pTester->m_Tester, pTester->m_AppId, pTester-> m_Zipcode);
		BIZ_RULE *pBizRecs = pBizRules;
		for( int i=0; i<NumBizRules; i++ ){
			printf("          Function: %s, Endpoint: %s, Method: %s\n",
				   pBizRecs->m_Function,pBizRecs->m_EndPoint,pBizRecs->m_Method);
			printf("          numReq: %ld, numRPH: %ld, maxTemp: %ld, minTemp: %ld, maxHour: %ld, minHour: %ld\n",
				pBizRecs->m_numReq,pBizRecs->m_numRPH,pBizRecs->m_maxTemp,pBizRecs->m_minTemp,pBizRecs->m_maxHour,pBizRecs->m_minHour);
			printf("          Email: %s\n\n",pBizRecs->m_Email);
			pBizRecs++;
		}
	}
#ifdef _WEATHER	
	if( iRet == 0 && pTester->m_AppId)
	{
		CURL *curl;
		CURLcode res;
		curl = curl_easy_init();
		if(curl)
		{
			struct string xmlStr;
			init_string(&xmlStr);
			// appid=85cd2a23af95429c1dbbc7b308463346  is valid
			strncpy( pTester->m_AppId, "85cd2a23af95429c1dbbc7b308463346", MAX_DB_NAMELEN );
			snprintf(api_buffer, APIBUFFLEN, api_endpoint, pTester->m_AppId, pTester->m_Zipcode );
			
			curl_easy_setopt(curl, CURLOPT_URL, api_buffer);
			curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, writefunc);
			curl_easy_setopt(curl, CURLOPT_WRITEDATA, &xmlStr);
			curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0); // Verify the SSL certificate, 0 (zero) means it doesn't.
			//curl_easy_setopt(curl, CURLOPT_CAPATH , getenv("SSL_CERT_DIR"));

			//puts("*** curl_easy_perform(curl) ***");
			res = curl_easy_perform(curl);
			if(res != CURLE_OK) {
				fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
			} else {
				//printf("string len: %ld\n",xmlStr.len);
				//printf("%s\n",xmlStr.ptr);
				xmlNodePtr cur;
				xmlDocPtr xmlDoc;
				xmlDoc = xmlParseMemory(xmlStr.ptr, xmlStr.len);
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
				while (cur != NULL)
				{
					if ((!xmlStrcmp(cur->name, (const xmlChar *)"temperature")))
					{
						xmlChar *key;
						if(cur->xmlChildrenNode == NULL){
							key = xmlGetProp(cur, (const unsigned char *)"value");
							printf("Current Temp: %s\n", key);
							xmlFree(key);
							/*key = xmlGetProp(cur, (const unsigned char *)"min");
							printf("Min Temp: %s\n", key);
							xmlFree(key);
							key = xmlGetProp(cur, (const unsigned char *)"max");
							printf("Max Temp: %s\n", key);
							xmlFree(key);
							key = xmlGetProp(cur, (const unsigned char *)"unit");
							printf("Temp Units: %s\n", key);
							xmlFree(key);*/
						}	
					}
					cur = cur->next;
				}			
				xmlFreeDoc(xmlDoc);
				free(xmlStr.ptr);
			}
			curl_easy_cleanup(curl); 
		}
	}
#endif	
	
	return iRet;
}

