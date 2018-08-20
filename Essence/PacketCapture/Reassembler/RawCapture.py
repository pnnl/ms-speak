#!/usr/bin/python -xv
# Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc

# The page at http://7h3ram.github.io/2013/6/18/libnids-pynids/ was used
# as a starter guide

import sys
import nids
import time
from cassandra.cluster import Cluster
from cassandra.io.libevreactor import LibevConnection
from cassandra.auth import PlainTextAuthProvider
import dbconfig as cfg

end_states = (nids.NIDS_CLOSE, nids.NIDS_TIMEOUT, nids.NIDS_RESET)

class TCPPacketCapturer:
    def __call__(self):
        return self

    def __init__(self):
        self.initCluster()
        nids.register_tcp(self.nidsCallback)

    def initCluster(self):  # initialize cassandra cluster, prepared queries
        auth_provider = PlainTextAuthProvider(username=cfg.cassandraConfig["user"], password=cfg.cassandraConfig["password"])
        cluster = Cluster([cfg.cassandraConfig["host"]], auth_provider=auth_provider)
        self.session = cluster.connect(cfg.cassandraConfig["db"])
        self.preparedQuery = self.session.prepare("""INSERT into generic_packet 
                                                    (source_addr, 
                                                     source_port,
                                                     source_content,
                                                     destination_addr, 
                                                     destination_port,
                                                     destination_content,
                                                     protocol,
                                                     time_stamp,
                                                     claimed) 
                                                 VALUES (?,?,?,?,?,?,?,?,?)""")

    def insertPacketIntoDatabase(self, sourceAddr, sourcePort, sourceData, destinationAddr, destinationPort, destinationData, protocol, timeStamp): 
        args = [sourceAddr, sourcePort, sourceData, destinationAddr, destinationPort, destinationData, protocol, timeStamp, False]
        try:
            self.session.execute(self.preparedQuery, args)
        except:
            print "Cassandra error: ", sys.exc_info()[0]

    def nidsCallback(self, tcp):
        if tcp.nids_state == nids.NIDS_JUST_EST:
            ((src, sport), (dst, dport)) = tcp.addr
            if src == "127.0.0.1":
                return
            
            print tcp.addr
            tcp.client.collect = 1
            tcp.server.collect = 1

        elif tcp.nids_state == nids.NIDS_DATA:
            tcp.discard(0)

        elif tcp.nids_state in end_states:
            ((src, sport), (dst, dport)) = tcp.addr
            if (len(tcp.server.data[:tcp.server.count]) > 0 and len(tcp.client.data[:tcp.client.count]) > 0):
                self.insertPacketIntoDatabase(src, sport, tcp.client.data[:tcp.client.count], dst, dport, tcp.server.data[:tcp.server.count], 'tcp',  nids.get_pkt_ts() * 1000)
            elif (len(tcp.server.data[:tcp.server.count]) > 0 and len(tcp.client.data[:tcp.client.count])) == 0:
                self.insertPacketIntoDatabase(src, sport, None, dst, dport, tcp.server.data[:tcp.server.count], 'tcp',  nids.get_pkt_ts() * 1000)
            elif (len(tcp.server.data[:tcp.server.count]) == 0 and  len(tcp.client.data[:tcp.client.count]) > 0):
                 self.insertPacketIntoDatabase(src, sport, tcp.client.data[:tcp.client.count], dst, dport, None, 'tcp',  nids.get_pkt_ts() * 1000)
            else:
                 self.insertPacketIntoDatabase(src, sport, None, dst, dport, None, 'tcp',  nids.get_pkt_ts() * 1000)

def main():
    if len(sys.argv) == 2:
        nids.param("filename", sys.argv[1])

    nids.param("device", "all")
    nids.param("tcp_workarounds", True)
    nids.param("pcap_timeout", 128)
    nids.param("scan_num_hosts",0)  # disable portscan detection
    nids.chksum_ctl([('0.0.0.0/0', False)]) # disable checksumming

    nids.init()

    tcpCapturer = TCPPacketCapturer()

    try:
        nids.run()
    except nids.error, e:
        print "[-] Error: %s" % (e)
    except Exception, e:
        print "[-] Exception: %s" % (e)

if __name__ == '__main__':
    main()
