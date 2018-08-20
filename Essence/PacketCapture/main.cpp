/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/

/*
  demo file for cassandra drivers
  modified to perform test insertions for essense project
  18 feb 2014
  David Cleckley
*/
/* includes from packet capture */
#include <pcap.h>
#include <string>
#include <sstream>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <iomanip> // for printing hex bytes
#include <errno.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netinet/if_ether.h> 
#include <net/ethernet.h>
#include <netinet/ether.h> 
#include <netinet/ip.h> 
/* includes from cassandra */
#include <cassert>

#include <boost/bind.hpp>
#include <boost/asio.hpp>
#include <boost/asio/ssl.hpp>
#include <boost/foreach.hpp>
#include <boost/lexical_cast.hpp>
#include <boost/thread.hpp>
#include <boost/format.hpp>
#include <boost/algorithm/string.hpp>
#include <boost/program_options/option.hpp>
#include <boost/program_options/variables_map.hpp>
#include <boost/program_options/parsers.hpp>
#include <boost/date_time/posix_time/posix_time.hpp>

#include <cql/cql.hpp>
#include <cql/cql_error.hpp>
#include <cql/cql_event.hpp>
#include <cql/cql_connection.hpp>
#include <cql/cql_session.hpp>
#include <cql/cql_cluster.hpp>
#include <cql/cql_builder.hpp>
#include <cql/cql_execute.hpp>
#include <cql/cql_result.hpp>



/* tcpdump header (ether.h) defines ETHER_HDRLEN) */
#ifndef ETHER_HDRLEN 
#define ETHER_HDRLEN 14
#endif

#ifndef TCP_HDRLEN
#define TCP_HDRLEN 20
#endif



boost::shared_ptr<cql::cql_cluster_t> cluster;
boost::shared_ptr<cql::cql_session_t> session;
std::vector<cql::cql_byte_t> queryid;
 boost::shared_future<cql::cql_future_result_t> future;
 
int unknownPackets=0;
int insertedPackets=0;
int ipPacketsHandled=0;
int callbackHit=0;

u_int16_t handle_ethernet(u_char *args,const struct pcap_pkthdr* pkthdr,const u_char* packet);
u_char* handle_IP(u_char *args,const struct pcap_pkthdr* pkthdr,const u_char* packet);
int database_insert(std::string sourceIP, std::string destIP, std::string protocol, int length,const u_char* payload );
std::string decode_protocol(int protocol);
void log_callback(const cql::cql_short_t,const std::string& message);
void insertPacket(std::string sourceIP, std::string destIP, std::string protocol, int length, std::string packet);
void demo(const std::string& host,bool use_ssl);
void setup(void);
void teardown (void);


// This function is called asynchronously every time an event is logged

void
log_callback(
    const cql::cql_short_t,
    const std::string& message)
{
    //std::cout << "LOG: " << message << std::endl;
}
void insertPacket(std::string sourceIP, std::string destIP, std::string protocol, int length, std::string packet){
	using namespace boost::posix_time;
	int voltage = 0;
	
	boost::shared_ptr<cql::cql_execute_t> bound ( new cql::cql_execute_t(queryid, cql::CQL_CONSISTENCY_ONE));
	ptime time_t_epoch(boost::gregorian::date(1970,1,1));
	ptime now = microsec_clock::universal_time();
	time_duration diff = now - time_t_epoch;
	long time = diff.total_milliseconds();	//this will be the time of insertion, not necessarily capture.
	voltage = std::rand() % 100 + 1;

	
	bound->push_back(sourceIP); 	// source IP
	bound->push_back(destIP);		// dest IP
	bound->push_back(time); 		// 8 byte (long) time since epoch
	bound->push_back(protocol);		//protocol
	bound->push_back(packet);
	bound->push_back(voltage);

	//send sample bound query
	future = session->execute(bound);
	future.wait();

	
	if(!future.get().error.is_err()) {
		 insertedPackets++;
	
	}
	else {
		std::cout << "Error inserting packet #" << insertedPackets << std::endl;
	}
		
}
void
demo(
    const std::string& host,
    bool               use_ssl)
{

    try
    {
		boost::shared_ptr<cql::cql_builder_t> builder = cql::cql_cluster_t::builder();
		builder->with_log_callback(&log_callback);
        builder->add_contact_point(boost::asio::ip::address::from_string(host));


		cluster = (builder->build());
		session = (cluster->connect());

		if (session) {

            // write a query that switches current keyspace to "demo"
            boost::shared_ptr<cql::cql_query_t> use_demo(
                new cql::cql_query_t("USE demo;", cql::CQL_CONSISTENCY_ONE));

            // send the query to Cassandra
           future = session->query(use_demo);

            // wait for the query to execute
            future.wait();

            // check whether the query succeeded
            std::cout << "switch to demo successful? " << (!future.get().error.is_err() ? "true" : "false") << std::endl;

   			//Prepared statement for inserting new records
			std::string preparedInsertString = "INSERT into packet(source_addr,dest_addr,time_stamp,protocol,content,voltage) values (?,?,?,?,?,?);";
			boost::shared_ptr<cql::cql_query_t> preparedInsert(new cql::cql_query_t(preparedInsertString, cql::CQL_CONSISTENCY_ONE));
			//compile query
			future = session->prepare(preparedInsert);
			future.wait();
			std::cout << "prepare successful?" << (!future.get().error.is_err() ?"true": "false") << std::endl;

			// read ID returned for the prepared query
			queryid = future.get().result->query_id();            
		}// if session

		
        
    }// end try
    catch (std::exception& e)
    {
        std::cout<<"Exception: " << e.what() << std::endl;
    }
}
void setup(){
	cql::cql_initialize();
    demo("192.168.2.103", false);
}

void teardown(){
	session->close();
	cluster->shutdown();
	cql::cql_terminate();
}

/* looking at ethernet headers */
void my_callback(u_char *args,const struct pcap_pkthdr* pkthdr,const u_char* packet){
    callbackHit++;
	u_int16_t type = handle_ethernet(args,pkthdr,packet);
    if(type == ETHERTYPE_IP)
    {/* handle IP packet */
		ipPacketsHandled++;
        handle_IP(args,pkthdr,packet);
    }
	else{
		unknownPackets++;
		}
	// else if(type == ETHERTYPE_ARP)
    // {/* handle arp packet */
    // }
    // else if(type == ETHERTYPE_REVARP)
    // {/* handle reverse arp packet */
    // }else{
	//	printf("unknown packet type");
		
	// }
}

u_char* handle_IP(u_char *args,const struct pcap_pkthdr* pkthdr,const u_char* packet){
    const struct ip* ippkt;
    u_int length = pkthdr->len;
    u_int hlen,off,version;
    int i;
    int len;
    #define IP_V(ip)	(((ip)->ip_vhl & 0xf0) >> 4)
    #define IP_HL(ip)	((ip)->ip_vhl & 0x0f)
	unsigned char *payload; /* Packet payload */
	using namespace boost::posix_time;
    /* jump pass the ethernet header */
    ippkt = (struct ip*)(packet + sizeof(struct ether_header));
    length -= sizeof(struct ether_header); 
	
    /* check to see we have a packet of valid length */
    // if (length < sizeof(struct ip))
    // {
        // printf("truncated ip %d",length);
        // return NULL;
    // }

    len     = ntohs(ippkt->ip_len);
    hlen    = ippkt->ip_hl; /* header length */
    version = ippkt->ip_v;/* ip version */

    /* check version */
    if(version != 4)
    {
      fprintf(stdout,"Unknown version %d\n",version);
      return NULL;
    }

    /* check header length */
    if(hlen < 5 )
    {
        fprintf(stdout,"bad-hlen %d \n",hlen);
    }

    /* see if we have as much packet as we should */
    //if(length < len)
     //   printf("\ntruncated IP - %d bytes missing\n",len - length);

    /* Check to see if we have the first fragment */
    // off = ntohs(ippkt->ip_off);
    // if((off & 0x1fff) == 0 )/* aka no 1's in first 13 bits */
    // {
        // fprintf(stdout,"IP: ");
        // fprintf(stdout,"%s ",
                // inet_ntoa(ippkt->ip_src));
        // fprintf(stdout,"%s %d %d %d %d\n",
                // inet_ntoa(ippkt->ip_dst),
                // hlen,version,len,off);
    // }
	//Debugging print out code only!
	
	
	
	payload = (unsigned char *) (packet + ETHER_HDRLEN + (hlen*4) ); // skip the ethernet header and the IP header. *4 since we need to count # of bytes
	
	std::string payload_string(payload, payload +  (len-(hlen*4)));
	
	//Parse the fields to send to database
	std::string sourceip(inet_ntoa(ippkt->ip_src));
	std::string destip(inet_ntoa(ippkt->ip_dst));
	std::string protocol(decode_protocol(ippkt->ip_p));

	
	// length used is total length (which includes ip header), then subtract the header length.
	// we are left with the length of the rest of the payload (TCP/http//whatever else)
	//multiply by 4 since we are counting num of bytes
	//std::cout << "inserting packet: " << sourceip << " " << destip << " " << protocol << " " << (len-(hlen*4)) << std::endl;
	ptime before = microsec_clock::universal_time();
	
	
	insertPacket(sourceip,destip,protocol,(len-(hlen*4)),payload_string);
	ptime after = microsec_clock::universal_time();
	time_duration diff = after - before;
	long time = diff.total_microseconds();
	std::cout  << "# " << ntohs(ippkt->ip_id) << " insert in " << time << " us" << std::endl;
	//for(int i =0; i< (len-(hlen*4));i++){
	//	printf(" %02x",payload[i]);
	//}
	//printf("\n");

    return NULL; // return
}
/*
	"modular" function that inserts each captured packet into a database.
	right now it is written for Cassandra
*/

/* handle ethernet packets, much of this code gleaned from
 * print-ether.c from tcpdump source
 */
u_int16_t handle_ethernet(u_char *args,const struct pcap_pkthdr* pkthdr,const u_char* packet){
    u_int caplen = pkthdr->caplen;
    u_int length = pkthdr->len;
    struct ether_header *eptr;  /* net/ethernet.h */
    u_short ether_type;

    if (caplen < ETHER_HDRLEN)
    {
        fprintf(stdout,"Packet length less than ethernet header length\n");
        return -1;
    }

    /* lets start with the ether header... */
    eptr = (struct ether_header *) packet;
    ether_type = ntohs(eptr->ether_type);

    /* Lets print SOURCE DEST TYPE LENGTH */
    // fprintf(stdout,"ETH: ");
    // fprintf(stdout,"%s "
            // ,ether_ntoa((struct ether_addr*)eptr->ether_shost));
    // fprintf(stdout,"%s "
            // ,ether_ntoa((struct ether_addr*)eptr->ether_dhost));

    /* check to see if we have an ip packet */
    if (ether_type == ETHERTYPE_IP)
    {
        //fprintf(stdout,"(IP)");
    }else  if (ether_type == ETHERTYPE_ARP)
    {
        //fprintf(stdout,"(ARP)");
    }else  if (eptr->ether_type == ETHERTYPE_REVARP)
    {
        //fprintf(stdout,"(RARP)");
    }else {
        //fprintf(stdout,"(?)");
    }
    //fprintf(stdout," %d\n",length);

    return ether_type;
}
std::string decode_protocol(int protocol){
	std::stringstream ss;
	switch(protocol) {
		case IPPROTO_ICMP:
			return std::string("ICMP");
			break;
		case IPPROTO_TCP:
			return std::string("TCP");
			break;
		case IPPROTO_IGMP:
			return std::string("IGMP");
			break;
		case IPPROTO_EGP:
			return std::string("EGP");
			break;
		case IPPROTO_DCCP:
			return std::string("DCCP");
			break;
		case IPPROTO_IPV6:
			return std::string("IPV6");
			break;
		case IPPROTO_GRE:
			return std::string("GRE");
			break;
		case IPPROTO_UDP:
			return std::string("UDP");
			break;
		default:
			ss << std::string("Unknown protocol #") << protocol << std::endl;
			return ss.str();
	}
}

int main(int argc,char **argv){ 
    char *dev; 
    char errbuf[PCAP_ERRBUF_SIZE];
    pcap_t* descr;
    struct bpf_program fp;      /* hold compiled program     */
    bpf_u_int32 maskp;          /* subnet mask               */
    bpf_u_int32 netp;           /* ip                        */
    u_char* args = NULL;

    /* Options must be passed in as a string  */
    if(argc < 2){ 
        fprintf(stdout,"Usage: %s numpackets \"options\"\n",argv[0]);
        return 0;
    }
	/* open cassandra session */
	setup();	// setup database stuff
	
    /* grab a device to peek into... */
    dev = pcap_lookupdev(errbuf);
    if(dev == NULL)
    { printf("%s\n",errbuf); exit(1); }

    /* ask pcap for the network address and mask of the device */
    pcap_lookupnet(dev,&netp,&maskp,errbuf);

    /* open device for reading. NOTE: defaulting to
     * promiscuous mode*/
    descr = pcap_open_live(dev,BUFSIZ,1,-1,errbuf);
    if(descr == NULL)
    { printf("pcap_open_live(): %s\n",errbuf); exit(1); }


    if(argc > 2)
    {
        /* Lets try and compile the program.. non-optimized */
        if(pcap_compile(descr,&fp,argv[2],0,netp) == -1)
        { fprintf(stderr,"Error calling pcap_compile\n"); exit(1); }

        /* set the compiled program as the filter */
        if(pcap_setfilter(descr,&fp) == -1)
        { fprintf(stderr,"Error setting filter\n"); exit(1); }
    }

    /* ... and loop */ 
	std::cout << "capturing " << argv[1] << " packets" << std::endl;
    pcap_loop(descr,atoi(argv[1]),my_callback,args);
	/* close cassandra session */
	
	teardown(); // teardown database stuff
    fprintf(stdout,"\nfinished\n");
	std::cout << "processed: " << callbackHit << " ip packets handled: " << ipPacketsHandled << " non IP pkts: " << unknownPackets << " inserted pkts: " << insertedPackets << std::endl;
    return 0;
}

