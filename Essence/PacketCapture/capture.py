# Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc

import socket, struct, os, array
from scapy.all import ETH_P_ALL
from scapy.all import select
from scapy.all import MTU
from cassandra.cluster import Cluster
from cassandra.io.libevreactor import LibevConnection
from lxml import etree		# xml parsing
import sys
import time	# for timestamp
import re	# regular expression for parsing multispeak message type

#author: askldjd
#see: http
class IPSniff:

    def __init__(self, interface_name, on_ip_incoming, on_ip_outgoing):

        self.interface_name = interface_name
        self.on_ip_incoming = on_ip_incoming
        self.on_ip_outgoing = on_ip_outgoing
        
        # The raw in (listen) socket is a L2 raw socket that listens 
        # for all packets going through a specific interface.
        self.ins = socket.socket(
            socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))
        self.ins.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 2**30)
        self.ins.bind((self.interface_name, ETH_P_ALL))	
	self.captureCount = 0
	self.numPackets = int(sys.argv[3])
	cluster = Cluster(['127.0.0.1','192.168.2.103']) # must use connection class libevConnection (rather than default AsyncoreConnection)
	self.session = cluster.connect('demo')
	self.preparedQuery = self.session.prepare("INSERT into packet (source_addr, dest_addr, time_stamp,content,text_values) VALUES (?,?,?,?,?)")
	self.namespace  = {'a':'http://schemas.xmlsoap.org/soap/envelope/'}
    def __process_ipframe(self, pkt_type, ip_header, payload, frame):
    
        # Extract the 20 bytes IP header, ignoring the IP options
        fields = struct.unpack("!BBHHHBBHII", ip_header)
        
        dummy_hdrlen = fields[0] & 0xf    
        iplen = fields[2]

        ip_src = payload[12:16]
        ip_dst = payload[16:20]
        ip_frame = payload[0:iplen]

        #if pkt_type == socket.PACKET_OUTGOING:
           # if self.on_ip_outgoing is not None:
           #     self.on_ip_outgoing(ip_src, ip_dst, ip_frame)
          # pass	#skip, don't worry about this case     
        #else:

	#check to make sure the IP matches the filter
	ip_src_string = socket.inet_ntoa(ip_src)
	index = frame.find('<soapenv:Envelope')
	if self.on_ip_incoming is not None and ip_src_string == sys.argv[2] and index != -1:
            self.on_ip_incoming(self, ip_src, ip_dst, ip_frame, frame)
	    self.captureCount += 1
		
    def recv(self):
        condition = self.captureCount < self.numPackets # initial setting
	while condition:
	    pkt, sa_ll = self.ins.recvfrom(MTU)
            self.timestamp = time.time()
            
	    if type == socket.PACKET_OUTGOING and self.on_ip_outgoing is None:
                continue
            elif self.on_ip_outgoing is None:
                continue
            
            if len(pkt) <= 0:
                break
                
            eth_header = struct.unpack("!6s6sH", pkt[0:14])
            
            dummy_eth_protocol = socket.ntohs(eth_header[2])
            
            if eth_header[2] != 0x800 :
                continue
                
            ip_header = pkt[14:34]
	    ip_id = pkt[18:19]
            payload = pkt[14:]      

            self.__process_ipframe(sa_ll[2], ip_header, payload,pkt)
	    condition = self.captureCount < self.numPackets
	print('Capture complete %s packets captured' % self.captureCount)	
	sys.stdout.flush()
def test_incoming_callback(self, src, dst, payload,frame):
    num = struct.unpack('!H',frame[18:20])
    # find the start of the XML.
    index = frame.find('<soapenv:Envelope')
    
    tree = etree.fromstring(frame[index:] )	# parse the incoming packet
    body = [] 
    body = tree.xpath('//a:Body',namespaces={'a':'http://schemas.xmlsoap.org/soap/envelope/'})	# get to the body attribute
    messageText = body[0].getchildren()[0].tag	# select the immediate child of the body tag, which is "always" the multispeak message
					# tag is the text value
    stripDomainNameRegex = '\{([^\}]+)\/'		# filter the domain name
    messageStripped = re.sub (stripDomainNameRegex,'',messageText)		# remove the namespace from the tag
    endpoint, messageName = messageStripped.split('}')			# separate into endpoint type and message name
    text_values = {'endpoint':endpoint,'messagetype':messageName}
    args = [socket.inet_ntoa(src),socket.inet_ntoa(dst),self.timestamp,frame,text_values]

    self.session.execute(self.preparedQuery, args)

    print ("inserted packet #%s" % num)
    sys.stdout.flush()

def test_outgoing_callback(src, dst, frame):
	pass
#    print("outgoing - src=%s, dst=%s, frame len = %d" 
#        %(socket.inet_ntoa(src), socket.inet_ntoa(dst), len(frame)))    
#    sys.stdout.flush()

#if __name__ == "__main__":
if (len(sys.argv) != 4):
	print 'Usage: capture.py <interface> <src.ip> <#packets>'
	sys.stdout.flush()
	sys.exit(1)
else:
	print 'Capturing %s packets on interface %s, filter: %s '% (sys.argv[3],sys.argv[1],sys.argv[2])
	sys.stdout.flush()
# test statement is below, it worked during testing
#session.execute("insert into packet (dest_addr, time_stamp, source_addr) VALUES ('172.16.0.12',12345,'172.2.2.2')")
	ip_sniff = IPSniff(sys.argv[1], test_incoming_callback, test_outgoing_callback)
	ip_sniff.recv()
	sys.stdout.flush()
