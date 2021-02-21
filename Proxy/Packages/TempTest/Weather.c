#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <libxml/xmlmemory.h>   // libxml2-dev,  /usr/include/libxml2/libxml
#include <libxml/parser.h>
#include <curl/curl.h>

#define _XOPEN_SOURCE       /* See feature_test_macros(7) */
#include <time.h>

char *strptime(const char *s, const char *format, struct tm *tm);
time_t timelocal(struct tm *tm);

struct string {
    char *ptr;
    size_t len;
};

void init_string(struct string *);
size_t writefunc(void *, size_t, size_t, struct string *);

const static char *api_endpoint = "http://api.openweathermap.org/data/2.5/weather?zip=99352&appid=85cd2a23af95429c1dbbc7b308463346&units=imperial&mode=xml";

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


/*
	<?xml version="1.0"?>
	<story>
	<storyinfo>
		<author>John Fleck</author>
		<datewritten>June 2, 2002</datewritten>
		<keyword>example keyword</keyword>
	</storyinfo>
	<body>
		<headline>This is the headline</headline>
		<para>This is the body text.</para>
	</body>
	</story>
*/

//  https://openweathermap.org/current
// sudo apt-get install libsqlite3-dev -lcurl -DDEBUG
// gcc Weather.c -o Weather -lcurl -lxml2
int main(int argc, char* argv[]) {
	
	// get weather
    CURL *curl;
    CURLcode res;

    curl = curl_easy_init();
    if(curl)
    {
        struct string s;
        init_string(&s);

        curl_easy_setopt(curl, CURLOPT_URL, api_endpoint);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, writefunc);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &s);
        curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0); // Verify the SSL certificate, 0 (zero) means it doesn't.
        res = curl_easy_perform(curl);
        if(res != CURLE_OK) {
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
        } else {
            //printf("string len: %ld\n",s.len);
			//printf("%s\n",s.ptr);
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
			
			xmlNodePtr child;
			xmlChar *key, *key2;
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
				}
				else if( (!xmlStrcmp(cur->name, (const xmlChar *)"lastupdate")) ){
					// 2021-02-20T18:44:07
					key = xmlGetProp(cur, (const xmlChar *)"value");
					struct tm result;
					if (strptime( (const char *)key, "%Y-%m-%dT%H:%M:%S",&result) == NULL)
						printf("\nstrptime failed\n");					
					else{
						//time_t local = timelocal(&result);
						time_t local = timegm(&result);
						struct tm *info;
						info = localtime( &local );
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
						key2 = xmlGetProp(child, (const xmlChar *)"value");
						printf("  direction: %s (%s degrees) )\n", key, key2);
						xmlFree(key);
						xmlFree(key2);
					}
					else{
						printf("ERROR: Failed to locate '%s'\n", key );
					}
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

