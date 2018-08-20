# Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
# Reassembler program.
# Also integrated with storing to database

from cassandra.cluster import Cluster
from cassandra.io.libevreactor import LibevConnection
from cassandra.auth import PlainTextAuthProvider
import dbconfig as cfg

import sys
import nids
import os
import traceback

import socket # ip address parsing, and setsockopt (increase pcap buffer)
import struct, os, array, pwd

import sys
import re   # regular expression for parsing multispeak message type
from re import *
from datetime import datetime
import calendar
import logging

import time     # for the support timer code
from multiprocessing import Process, Queue
from parse import MultispeakParser      #class for MS parameter parsing and DB storage

import pdb

class Timer:
    def __enter__(self):
        self.start = time.clock()
        return self
    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start
        #print("Timer: %.07f sec" % t.interval)

class Reassembler(Process):
    def initCluster(self):
        auth_provider = PlainTextAuthProvider(username=cfg.cassandraConfig["user"], password=cfg.cassandraConfig["password"])
        self.session = Cluster([cfg.cassandraConfig["host"]], auth_provider=auth_provider).connect(cfg.cassandraConfig["db"])
        self.preparedQuery = self.session.prepare("""INSERT into packet (source_addr, dest_addr, time_stamp, content, text_values)
                                                        VALUES (?,?,?,?,?)""")

    def insertIntoDatabase(self, sourceAddr, destAddr, timeStamp, content, textValues):
        args = [sourceAddr, destAddr, timeStamp, content, textValues]
        self.session.execute(self.preparedQuery, args)

    def __init__(self, ports):
        self.ports = []
        list = ports.split(',')     # split CSV port list arguments
        self.ports = map(int,list)  # convert ports to int (from string)
        self.initCluster()
        nids.register_tcp(self.handleTcpStream)                     # set up call back
        
    def __call__(self):     # make a singleton clas
        return self
    
    def printableHex(self, buf):
        return ' '.join(x.encode('hex') for x in buf)
        
    def handleTcpStream(self, tcp):
        end_states = (nids.NIDS_CLOSE, nids.NIDS_TIMEOUT, nids.NIDS_RESET)
        logging.debug('tcps - {0} state: {1} timestamp: {2}'.format(str(tcp.addr),tcp.nids_state,nids.get_pkt_ts() * 1000))
        if tcp.nids_state == nids.NIDS_JUST_EST:
            # new to us, but do we care?
            ((src, sport), (dst, dport)) = tcp.addr
            #if dport in self.ports:
            logging.info('collecting: {}'.format(str(tcp.addr)))
            tcp.client.collect = 1
            tcp.server.collect = 1
        elif tcp.nids_state == nids.NIDS_DATA:
            tcp.discard(0)
            # keep all of the stream's new data
            #informs nids how many bytes in the stream to discard
            #((src, sport), (dst, dport)) = tcp.addr
            #serverData = tcp.server.data[:tcp.server.count]
            #clientData = tcp.client.data[:tcp.client.count]
            #envelopeRegex = '<soap.*:envelope.*<.*MultiSpeakMsgHeader.*<soap.*:envelope>'
            #envelopeRegex2 = '</.+:[Ee]nvelope'
            #if serverData is None or clientData is None:
            #   tcp.discard(0)
            #else:
            #   if "Expect: 100-continue" not in serverData:
            #       tcp.discard(0)
            #   else:
            #       if (re.search(envelopeRegex,serverData,re.S | re.IGNORECASE) and re.search(envelopeRegex2,serverData,re.S | re.IGNORECASE) and re.search(envelopeRegex,clientData,re.S | re.IGNORECASE) and re.search(envelopeRegex2,clientData,re.S | re.IGNORECASE)):
            #           tcpaddr = ((dst,dport),(src,sport))
            #           logging.debug( "count_new: {}".format(tcp.server.count_new))
            #           logging.debug( "offset server: {}".format(tcp.server.offset))
            #           self.process_ipframe(serverData,tcp.addr,self.timestamp)
#
            #           logging.debug( "count_new: {}".format(tcp.server.count_new))
            #           logging.debug( "offset client: {}".format(tcp.client.offset))
            #           tcpaddr = ((dst,dport),(src,sport)) #flip it around to match our point of view (since this is the client
            #           self.process_ipframe(clientData,tcpaddr,self.timestamp)
            #           tcp.discard(tcp.server.count + tcp.client.count)
            #       else:
            #           tcp.discard(0)
        elif tcp.nids_state in end_states:
            ((src,sport),(dst,dport)) = tcp.addr
            serverData = tcp.server.data[:tcp.server.count]
            clientData = tcp.client.data[:tcp.client.count]
            #logging.debug("serverData: {0}".format(    serverData))
            #logging.debug("clientData: {0}".format(clientData))
            self.timestamp = nids.get_pkt_ts() * 1000
            #Add the MultiSpeakMsgHeader since we observed way too many false positives during
            #the virtual field test
            envelopeRegex = '<soap.*:envelope.*<.*MultiSpeakMsgHeader.*<soap.*:envelope>'
            logging.info("Serv Count: {0} Client Count {1} newc: {2} news: {3}".format(tcp.server.count,tcp.client.count,tcp.client.count_new,tcp.server.count_new))
            #Match even if there is a newline since we've observed some payloads with the newline
            #print("server is ", tcp.server.data[:tcp.server.count], "client is ", tcp.client.data[:tcp.client.count], "count new is ", tcp.server.count_new)
            if serverData is not None:
                serverData = serverData.replace("\n","")
                if (re.search(envelopeRegex,serverData,re.S | re.IGNORECASE)): #and tcp.server.count_new > 0):
                    logging.info('full message found in tcp server data')
                    payload = tcp.server.data[:tcp.server.count]
                    #tcpaddr = ((dst,dport),(src,sport))
                    logging.debug( "count_new: {}".format(tcp.server.count_new))
                    logging.debug( "offset server: {}".format(tcp.server.offset))
                    self.process_ipframe(payload,tcp.addr,self.timestamp)
                    tcp.discard(tcp.server.count)
                elif "multispeak" in serverData.lower():
                    logging.warning("multispeak serverData but envelope failed: {}".format(serverData))
            if clientData is not None:
                clientData = clientData.replace("\n","")
                if (re.search(envelopeRegex,clientData, re.S | re.IGNORECASE)):
                    logging.info('full message found in tcp client data')
                    tcpaddr = ((dst,dport),(src,sport)) #flip it around to match our point of view (since this is the client
                    payload = tcp.client.data[:tcp.client.count]
                    logging.debug("count_new client: {}".format(tcp.client.count_new))
                    logging.debug( "offset client: {}".format(tcp.client.offset))
                    self.process_ipframe(payload,tcpaddr,self.timestamp) #modified tcpaddr
                    tcp.discard(tcp.client.count)
                elif "multispeak" in clientData.lower():
                    logging.warning("multispeak clientData but envelope failed: {}".format(clientData))
            logging.debug( "addr: {}".format(tcp.addr))
            logging.debug( "To server:")
            logging.debug( "bytes {}".format(str(tcp.server.count)))
            logging.debug( "To client:")
            logging.debug( "bytes: {}".format(str(tcp.client.count)))

    def process_ipframe(self,frame,tcpaddr, timestamp):
        # note that we are no longer checking source IP addresses
        # so we could be processing frames from other ips if not filtered
        # before this point
        cleansedFrame = frame.replace("\n","").replace("\r","").replace("\t","")
        envelopeRegex = '</.+:[Ee]nvelope'
        match = re.search(envelopeRegex,cleansedFrame)
        if match:
            ((src, sport),(dst,dport)) = tcpaddr
            #try to find the endpoint type from POST Request
            endpointRegex = '(?<=POST\s).*(?=\sHTTP)'   # looks for POST and HTTP, and matches the URL
            match = re.search(endpointRegex,cleansedFrame, re.IGNORECASE)
            if match is not None:
                URLsplit = cleansedFrame[match.start():match.end()].split('/')  # [foo,QA_SERVER]
                endpointCodeSplit = URLsplit[-1].split('_') # [QA,SERVER]
                endpointCode = endpointCodeSplit[0] # QA
                logging.debug("parsed MS endpoint code: {}".format(endpointCode))
            else:
                endpointCode = 'NULL'
                logging.warning("Unable to parse endpoint code from header")
                #get the version from the SOAPAction http header
            versionRegex = '(?<=SOAPAction:\s"http:\/\/www.multispeak.org\/Version_).'
            match = re.search(versionRegex,cleansedFrame, re.IGNORECASE)
            mspVersion = 'NULL'
            if match is not None:
                mspVersion = cleansedFrame[match.start()]
                if (mspVersion != '3' and mspVersion != '5'):
                    mspVersion = 'NULL'
            else:
                versionRegex2 = '(?<=SOAPAction:\shttp:\/\/www.multispeak.org\/Version_).' # uses lookbehind to extract only version num
                match2 = re.search(versionRegex2, cleansedFrame, re.IGNORECASE)
                if match2 is not None:
                    mspVersion = cleansedFrame[match2.start()]
                    if (mspVersion != '3' and mspVersion != '5'):
                        mspVersion = 'NULL'
                else:
                    versionRegex3 = '<MultiSpeakMsgHeader[^>]* Version="(\d)\.'
                    match3 = re.search(versionRegex3, cleansedFrame, re.IGNORECASE)
                    if match3 is not None:
                        mspVersion = match3.group(1)
                        if (mspVersion != '3' and mspVersion != '5'):
                            mspVersion = 'NULL'
                    

#           messageNameRegex = '(<[\w:]*[Bb]ody>)(\s*)(<)(?P<MsgName>[\w|:]+)'
            messageNameRegex = '(<([\w-]+:)?body>)(\s*)(<)(([\w-]+:)?)(?P<MsgName>\w*)'
            match = re.search(messageNameRegex,cleansedFrame, re.IGNORECASE)
            if match is not None:
                    messageName = match.group('MsgName').split(':')[-1]
                    text_values = {'endpoint':endpointCode,'messagetype':messageName,'mspVersion':mspVersion}
                    logging.debug( "text values: {}".format(text_values))
                    self.insertIntoDatabase(src, dst, timestamp, frame, text_values)
                    print("inserted packet")
            else:
                    print("MsgName not found")
                    logging.debug("frame with no MsgName: {}".format(cleansedFrame))
        else:
            logging.debug("end of envelope not found: {}".format(cleansedFrame))
            print("end of envelope not found")
            

def main():
    logging.basicConfig(filename="mspCapturer.log",level=logging.DEBUG)
    if (len(sys.argv) != 2):
        logging.error( 'Invalid arguments. Usage: main.py <monitor port(s)>\n monitor ports should be specified in a comma seperated list ')
        sys.exit(1)
    logging.info( 'Set up Reassembler')
    nids.param("scan_num_hosts",0)  # disable portscan detection
    nids.chksum_ctl([('0.0.0.0/0', False)]) # disable checksumming
    nids.param("pcap_timeout", 128)
    nids.param("tcp_workarounds", True)
    nids.param("sk_buff_size", 256) #default 168
    nids.param("n_tcp_streams", 2048) #default 1024
    nids.param("device", "all")

    nids.init()

    assm = Reassembler(ports=sys.argv[1])
    try:
        nids.run()
    except KeyboardInterrupt:
        logging.error( "Reassembler Terminated: Quitting")
        sys.exit(2)

if __name__ == '__main__':
    main()

