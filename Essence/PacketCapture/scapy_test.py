# Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc

import socket, struct, os, array
from scapy.all import *
import sys
import happybase
import time
from decimal import *

class IPSniff:

    def callback(self,pkt):
	print (pkt.summary())
	print ("source ip {0}".format(pkt[IP].src))
	print ("dest ip {0} ".format(pkt[IP].dst))
	if(pkt.haslayer(Raw) and len(pkt) > 499): # 499 - needs at least that many bytes to include a multispeak header (not even a complete header)
		proto = str(pkt[Raw])[435:445]	#extract the word Multispeak after the soap envelope header
	else:
		proto = pkt[IP].proto
	print str(proto).lower()
	if(str(proto).lower() == "multispeak"):
		print 'storing MS pkt'
		self.dbwrite(sourceIP=pkt[IP].src,destIP=pkt[IP].dst,protocol=proto.lower(),data=str(pkt).encode('hex'))

    def __del__(self):
	self.connection.close()

    def __init__(self, interface_name, filter, count=0):
	getcontext().prec = 19	#set precision for timestamp calculation (truncation not considered here)
        self.interface_name = interface_name
        self.count = count
	self.build_filter = filter
	self.connection = happybase.Connection('localhost', compat='0.90')
	self.connection.open()
	self.table = self.connection.table('test')        
	# TODO: maybe we should check to make sure our table exits here, if not, create it
	sniff(count=self.count,iface=self.interface_name,prn=self.callback,filter=self.build_filter)

	                           
    def dbwrite(self,sourceIP,destIP,protocol,data):
	#rowkey calculation
	reverse_timestamp = Decimal(sys.maxint) - Decimal(time.time()) # generating current timestamp, not necessarily packet 'capture' timestamp
	rowkey = sourceIP + "-" + str(reverse_timestamp)
	self.table.put(rowkey, {'hdr:sip' : sourceIP,
                                'hdr:dip' : destIP,
                                'pkt:protocol' : protocol,
                                'pkt:data' : data} )
	print 'DB Insertion Completed'

if __name__ == "__main__":
	if (len(sys.argv) < 3):
		print 'Usage: capture.py <interface> <BPF> [count]'
		sys.exit(1)
	else:
		print 'Capturing on interface %s, filter: '% sys.argv[1],sys.argv[2]
	if len(sys.argv) < 4 :
		print 'unlimited'
		ip_sniff = IPSniff(interface_name =sys.argv[1], filter=sys.argv[2])
	else:
		print 'count =%d' % int(sys.argv[3])
		ip_sniff = IPSniff(interface_name =sys.argv[1], filter=sys.argv[2], count = int(sys.argv[3]))

