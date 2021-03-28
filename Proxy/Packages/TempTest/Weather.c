#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <libxml/xmlmemory.h>   // libxml2-dev,  /usr/include/libxml2/libxml
#include <libxml/parser.h>
#include <curl/curl.h>

#define _XOPEN_SOURCE       /* See feature_test_macros(7) */
#include <time.h>

#define APIBUFFLEN     250

char *strptime(const char *s, const char *format, struct tm *tm);
time_t timelocal(struct tm *tm);

struct string {
    char *ptr;
    size_t len;
};

void init_string(struct string *);
size_t writefunc(void *, size_t, size_t, struct string *);

// appid=85cd2a23af95429c1dbbc7b308463346
const static char *api_endpoint = "http://api.openweathermap.org/data/2.5/weather?appid=%s&zip=%s&units=imperial&mode=xml";
char api_buffer[APIBUFFLEN+1];

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

// http://www.xmlsoft.org/tutorial/ar01s04.html
xmlNodePtr parseNode (xmlNodePtr cur, const xmlChar *subchild)
{
	xmlNodePtr child = NULL;
    xmlNodePtr nxt = cur->xmlChildrenNode;
    while (nxt != NULL)
    {
        if ((!xmlStrcmp(nxt->name, subchild)))
        {
			child = nxt;
			break;
        }
        nxt = nxt->next;
    }
    return child;
}

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

//  https://openweathermap.org/current
// sudo apt-get install libsqlite3-dev
// gcc Weather.c -o Weather -lcurl -lxml2
int main(int argc, char* argv[])
{
	bool bShowAll = false;
	
	if( argc < 2 ){
		printf("\n You Must Provide a Zipcode.\n"); // 10502: Ardsley, ./Weather 97429: DC
		return -1;	
	}
	if( argc == 3 )
		bShowAll = true;
	
	// get weather
    CURL *curl;
    CURLcode res;
	int tmz_off = 0;
	char *Zipcode = argv[1];
	char *appid = "85cd2a23af95429c1dbbc7b308463346";
	if( !strcmp(Zipcode, "10502") ){
		tmz_off = 3;
	}
	
	curl = curl_easy_init();
    if(curl)
    {
        struct string s;
        init_string(&s);
		printf("\n Getting Weather for area %s\n", Zipcode);		
		printf("      using AppID: %s\n", appid);		
		//snprintf(api_buffer, APIBUFFLEN, api_endpoint, Zipcode );
		snprintf(api_buffer, APIBUFFLEN, api_endpoint, appid, Zipcode );
        curl_easy_setopt(curl, CURLOPT_URL, api_buffer);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, writefunc);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &s);
        curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0); // Verify the SSL certificate, 0 (zero) means it doesn't.
        res = curl_easy_perform(curl);
        if(res != CURLE_OK) {
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
        } else {
			if( bShowAll ){
				//printf("string len: %ld\n",s.len);
				printf("\n%s\n\n",s.ptr);
			}
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
			
			xmlNodePtr child;
			xmlChar *key, *key2;
			struct tm result;
			struct tm *info;
			time_t local;
			while (cur != NULL)
			{
				//printf("Current Name: '%s'\n", cur->name);
				if( (!xmlStrcmp(cur->name, (const xmlChar *)"temperature")) )
				{
					if(cur->xmlChildrenNode == NULL){
						key = xmlGetProp(cur, (const xmlChar *)"value");
						printf("Current Temp: %s\n", key);
						xmlFree(key);
						key = xmlGetProp(cur, (const xmlChar *)"min");
						printf("Min Temp: %s\n", key);
						xmlFree(key);
						key = xmlGetProp(cur, (const xmlChar *)"max");
						printf("Max Temp: %s\n", key);
						xmlFree(key);
						key = xmlGetProp(cur, (const xmlChar *)"unit");
						printf("Temp Units: %s\n", key);
						xmlFree(key);
					}	
				}
				else if( (!xmlStrcmp(cur->name, (const xmlChar *)"feels_like")) ){
					key = xmlGetProp(cur, (const xmlChar *)"value");
					printf("Feels like: %s\n", key);
					xmlFree(key);
				}				
				else if( (!xmlStrcmp(cur->name, (const xmlChar *)"humidity")) ){
					key = xmlGetProp(cur, (const xmlChar *)"value");
					printf("Humidity: %s%%\n", key);
					xmlFree(key);
				}				
				else if( (!xmlStrcmp(cur->name, (const xmlChar *)"city")) ){
					key = xmlGetProp(cur, (const xmlChar *)"name");
					printf("City: %s\n", key);
					xmlFree(key);
					key = (xmlChar *)"coord";
					child = parseNode( cur, key);
					if( child ){
						key = xmlGetProp(child, (const xmlChar *)"lat");
						printf("Lat: %s\n", key);
						xmlFree(key);
						key = xmlGetProp(child, (const xmlChar *)"lon");
						printf("Lon: %s\n", key);
						xmlFree(key);
					}
					else{
						printf("ERROR: Failed to locate '%s'\n", key );
					}
					key = (xmlChar *)"sun";
					child = parseNode( cur, key);
					if( child ){
						key = xmlGetProp(child, (const xmlChar *)"rise");
						if (strptime( (const char *)key, "%Y-%m-%dT%H:%M:%S",&result) == NULL)
							printf("\nstrptime failed\n");					
						else{
							local = timegm(&result);
							info = localtime( &local );
							info->tm_hour+=tmz_off;
							printf("Sunrise: %d:%d:%d\n", info->tm_hour,info->tm_min,info->tm_sec );
						}
						xmlFree(key);
						key = xmlGetProp(child, (const xmlChar *)"set");
						if (strptime( (const char *)key, "%Y-%m-%dT%H:%M:%S",&result) == NULL)
							printf("\nstrptime failed\n");					
						else{
							local = timegm(&result);
							info = localtime( &local );
							info->tm_hour+=tmz_off;
							printf("Sunset: %d:%d:%d\n", info->tm_hour,info->tm_min,info->tm_sec );
						}
						xmlFree(key);
					}
					else{
						printf("ERROR: Failed to locate '%s'\n", key );
					}
				}
				else if( (!xmlStrcmp(cur->name, (const xmlChar *)"lastupdate")) ){
					// 2021-02-20T18:44:07
					key = xmlGetProp(cur, (const xmlChar *)"value");
					if (strptime( (const char *)key, "%Y-%m-%dT%H:%M:%S",&result) == NULL)
						printf("\nstrptime failed\n");					
					else{
						//time_t local = timelocal(&result);
						local = timegm(&result);
						info = localtime( &local );
						info->tm_hour+=tmz_off;
						//printf("Current local time and date: %s", asctime(info));
						printf("Last Update: %s\n", asctime(info));
					}
					xmlFree(key);
				}
				else if( (!xmlStrcmp(cur->name, (const xmlChar *)"wind")) ){
					key = (xmlChar *)"speed";
					child = parseNode( cur, key);
					if( child ){
						key = xmlGetProp(child, (const xmlChar *)"value");
						key2 = xmlGetProp(child, (const xmlChar *)"unit");
						printf("Wind Speed: %s %s\n", key, key2);
						xmlFree(key);
						xmlFree(key2);
						key = xmlGetProp(child, (const xmlChar *)"name");
						printf(" ( %s )\n", key);
						xmlFree(key);
					}
					else{
						printf("ERROR: Failed to locate '%s'\n", key );
					}
					//<direction value="210" code="SSW" name="South-southwest"/>
					key = (xmlChar *)"direction";
					child = parseNode( cur, key);
					if( child ){
						key = xmlGetProp(child, (const xmlChar *)"name");
						if( key ){
							key2 = xmlGetProp(child, (const xmlChar *)"value");
							printf("  direction: %s (%s degrees)\n", key, key2);
							xmlFree(key2);
						}
						xmlFree(key);
					}
					else{
						printf("ERROR: Failed to locate '%s'\n", key );
					}
					key = (xmlChar *)"gusts";
					child = parseNode( cur, key);
					if( child ){
						key = xmlGetProp(child, (const xmlChar *)"value");
						if( key ){
							printf("  gusts: %s\n", key);
							xmlFree(key);
						}
					}
					else{
						printf("ERROR: Failed to locate '%s'\n", key );
					}					
				}				
				else if( (!xmlStrcmp(cur->name, (const xmlChar *)"clouds")) ){
					key = xmlGetProp(cur, (const xmlChar *)"name");
					printf("%s\n", key);
					xmlFree(key);
				}
				//.mode Possible values are 'no", name of weather phenomena as 'rain', 'snow'				
				else if( (!xmlStrcmp(cur->name, (const xmlChar *)"precipitation")) ){
					key = xmlGetProp(cur, (const xmlChar *)"value");
					if( key ){
						key2 = xmlGetProp(cur, (const xmlChar *)"mode");
						printf("precipitation: %smm, %s\n", key,key2);
						xmlFree(key2);
					}
					else{
						printf("precipitation: %s\n", "none");
					}
					xmlFree(key);
				}
				cur = cur->next;
			}			
			xmlFreeDoc(xmlDoc);
            free(s.ptr);
        }
        curl_easy_cleanup(curl); 
    }	
	printf("\n\n");
	return 0;
}

