/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/

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



/* tcpdump header (ether.h) defines ETHER_HDRLEN) */
#ifndef ETHER_HDRLEN 
#define ETHER_HDRLEN 14
#endif

#ifndef TCP_HDRLEN
#define TCP_HDRLEN 20
#endif


u_int16_t handle_ethernet(u_char *args,const struct pcap_pkthdr* pkthdr,const u_char* packet);
u_char* handle_IP(u_char *args,const struct pcap_pkthdr* pkthdr,const u_char* packet);
int database_insert(std::string sourceIP,O std::string destIP, std::string protocol, int length,const u_char* payload );
std::string decode_protocol(int protocol);

/* looking at ethernet headers */
void my_callback(u_char *args,const struct pcap_pkthdr* pkthdr,const u_char* packet){
    u_int16_t type = handle_ethernet(args,pkthdr,packet);
    if(type == ETHERTYPE_IP)
    {/* handle IP packet */
        handle_IP(args,pkthdr,packet);
    }else if(type == ETHERTYPE_ARP)
    {/* handle arp packet */
    }
    else if(type == ETHERTYPE_REVARP)
    {/* handle reverse arp packet */
    }else{
		printf("unknown packet type");
	}
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
	
    /* jump pass the ethernet header */
    ippkt = (struct ip*)(packet + sizeof(struct ether_header));
    length -= sizeof(struct ether_header); 
	
    /* check to see we have a packet of valid length */
    if (length < sizeof(struct ip))
    {
       // printf("truncated ip %d",length);
        //return NULL;
    }

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
    //    printf("\ntruncated IP - %d bytes missing\n",len - length);

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
	
	//Parse the fields to send to database
	std::string sourceip(inet_ntoa(ippkt->ip_src));
	std::string destip(inet_ntoa(ippkt->ip_dst));
	std::string protocol(decode_protocol(ippkt->ip_p));

	
	// length used is total length (which includes ip header), then subtract the header length.
	// we are left with the length of the rest of the payload (TCP/http//whatever else)
	//multiply by 4 since we are counting num of bytes
	database_insert(sourceip,destip,protocol,(len-(hlen*4)),payload);

    return NULL; // return
}
/*
	"modular" function that inserts each captured packet into a database.
	right now it is written for Cassandra
*/
int database_insert(std::string sourceIP, std::string destIP, std::string protocol, int length,const u_char* payload ){
	//std::cout << "database insert: " << sourceIP << " " << destIP << " " << protocol << " "  << length << std::endl;
	// print the payload (debug only)
	// for (int i = 0; i < length; i++){
		// printf(" %02x", payload[i] &0xff);
	// }
	// printf("\n");
	return 0;
}
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
    fprintf(stdout,"ETH: ");
    fprintf(stdout,"%s "
            ,ether_ntoa((struct ether_addr*)eptr->ether_shost));
    fprintf(stdout,"%s "
            ,ether_ntoa((struct ether_addr*)eptr->ether_dhost));

    /* check to see if we have an ip packet */
    if (ether_type == ETHERTYPE_IP)
    {
        fprintf(stdout,"(IP)");
    }else  if (ether_type == ETHERTYPE_ARP)
    {
        fprintf(stdout,"(ARP)");
    }else  if (eptr->ether_type == ETHERTYPE_REVARP)
    {
        fprintf(stdout,"(RARP)");
    }else {
        fprintf(stdout,"(?)");
    }
    fprintf(stdout," %d\n",length);

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
	
    /* grab a device to peak into... */
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
    pcap_loop(descr,atoi(argv[1]),my_callback,args);

    fprintf(stdout,"\nfinished\n");
    return 0;
}

