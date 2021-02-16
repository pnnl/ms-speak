#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sqlite3.h> 
#include <stdbool.h>

#define MAX_DB_NAMELEN  50
#define WILDCARD_STR "-1"
#define WILDCARD -1

#define DB_COLNAME_TESTER	"Tester"
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
	gchar  m_EndPoint[MAX_DB_NAMELEN+1];
	gchar  m_Method[MAX_DB_NAMELEN+1];
	gchar  m_Email[MAX_DB_NAMELEN+1];
} BIZ_DATA;
BIZ_DATA *pBizRecords;
int NumBizRecs;
int RowCnt;

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
			if( !strcmp(curr_key, DB_COLNAME_NUMREQ)){
				pBzd->m_numReq = atoll(values[i]);
			}
			else if( !strcmp(curr_key, DB_COLNAME_MINTEMP)){
				pBzd->m_minTemp = atoll(values[i]);
			}
			else if( !strcmp(curr_key, DB_COLNAME_MAXTEMP)){
				pBzd->m_maxTemp = atoll(values[i]);
			}
			else if( !strcmp(curr_key, DB_COLNAME_MINHOUR)){
				pBzd->m_minHour = atoll(values[i]);
			}
			else if( !strcmp(curr_key, DB_COLNAME_MAXHOUR)){
				pBzd->m_maxHour = atoll(values[i]);
			}
			else if( !strcmp(curr_key, DB_COLNAME_TESTER)){
				strncpy( pBzd->m_Tester, values[i], MAX_DB_NAMELEN );
			}
			else if( !strcmp(curr_key, DB_COLNAME_ENDPOINT)){
				strncpy( pBzd->m_EndPoint, values[i], MAX_DB_NAMELEN );
			}
			else if( !strcmp(curr_key, DB_COLNAME_METHOD)){
				strncpy( pBzd->m_Method, values[i], MAX_DB_NAMELEN );
			}
			else if( !strcmp(curr_key, DB_COLNAME_EMAIL)){
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

// sudo apt-get install libsqlite3-dev
// gcc IcapTest.c -o IcapTest -lsqlite3
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
		fprintf(stderr, "Opened database successfully\n");
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
	
	sql = "SELECT testers.Name as Tester, endpoints.name as Endpoint, methods.name as Method,"
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
		fprintf(stdout, "Operation done successfully\n");
	}
	sqlite3_close(db);

	if( RowCnt > NumBizRecs ){
		fprintf(stderr, "SANITY FAILURE: %s\n", "excess rows for query");
	}
	else{
		iRet = 0;
		fprintf(stdout, "Rules Read Successfully\n");
		BIZ_DATA *pBizRecs = pBizRecords;
		for( int i=0; i<NumBizRecs; i++ ){
			printf("Record %d:\n  Tester: %s, Endpoint: %s, Method: %s\n",
				   i,pBizRecs->m_Tester,pBizRecs->m_EndPoint,pBizRecs->m_Method);
			printf("          numReq: %d, maxTemp: %d, minTemp: %d, maxHour: %d, minHour: %d\n",
				   pBizRecs->m_numReq,pBizRecs->m_maxTemp,pBizRecs->m_minTemp,pBizRecs->m_maxHour,pBizRecs->m_minHour);
			printf("          Email: %s\n",pBizRecs->m_Email);
			pBizRecs++;
		}		
	}
	return iRet;
}

