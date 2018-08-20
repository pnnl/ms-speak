import datetime
import errno
import os
import random
import SocketServer
import sys
import time
import uuid
from collections import defaultdict
from ConfigParser import ConfigParser
from functools import partial
from random import randint
from mininet.topo import Topo
# from mininet.util import dumpNodeConnections    # DEBUG INFO
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.node import OVSController
# from mininet.node import RemoteController
from mininet.node import Node
from struct import *
from subprocess import call
from mininet.node import RemoteController
from mininet.cli import CLI




class CustomTopo(Topo):
    def __init__(self, **opts):

       self.finalHostCount=0
       Topo.__init__(self, **opts)
       self.switchHostMapping = []
       hostCount=1
       switchMain=self.addSwitch('s1')
       x=randint(minHost,maxHost)
       for i in range(0,x):
         host=self.addHost("h%s" %hostCount)
         self.addLink(host,switchMain)
         hostCount+=1
       self.switchHostMapping.append(x)

       switch7_1=self.addSwitch('s2')
       x=randint(minHost,maxHost)
       for i in range(0,x):
         host=self.addHost("h%s" %hostCount)
         self.addLink(host,switch7_1)
         hostCount+=1
       self.switchHostMapping.append(x)

       switch7_2=self.addSwitch('s3')
       x=randint(minHost,maxHost)
       for i in range(0,x):
         host=self.addHost("h%s" %hostCount)
         self.addLink(host,switch7_2)
         hostCount+=1
       self.switchHostMapping.append(x)

       switch5_1=self.addSwitch('s4')
       x=randint(minHost,maxHost)
       for i in range(0,x):
         host=self.addHost("h%s" %hostCount)
         self.addLink(host,switch5_1)
         hostCount+=1
       self.switchHostMapping.append(x)

       switch5_2=self.addSwitch('s5')
       x=randint(minHost,maxHost)
       for i in range(0,x):
         host=self.addHost("h%s" %hostCount)
         self.addLink(host,switch5_2)
         hostCount+=1
       self.switchHostMapping.append(x)

       switch2_1=self.addSwitch('s6')
       x=randint(minHost,maxHost)
       for i in range(0,x):
         host=self.addHost("h%s" %hostCount)
         self.addLink(host,switch2_1)
         hostCount+=1
       self.switchHostMapping.append(x)

       switch2_2=self.addSwitch('s7')
       x=randint(minHost,maxHost)
       for i in range(0,x):
         host=self.addHost("h%s" %hostCount)
         self.addLink(host,switch2_2)
         hostCount+=1
       self.switchHostMapping.append(x)


       self.addLink(switchMain, switch7_1)
       self.addLink(switchMain, switch7_2)
       self.addLink(switch7_1, switch7_2)
       self.addLink(switch7_1, switch5_1)
       self.addLink(switch7_1, switch5_2)
       self.addLink(switch7_2, switch5_1)
       self.addLink(switch7_2, switch5_2)
       self.addLink(switch5_1, switch5_2)
       self.addLink(switch5_1,switch2_1)
       self.addLink(switch5_1,switch2_2)
       self.addLink(switch5_2,switch2_1)
       self.addLink(switch5_2,switch2_2)



if __name__ == "__main__":
    #setLogLevel('debug')
    strNetworkID = "10.0.0.0/24"
    i = 1
    while i < len(sys.argv):
        currentArg = sys.argv[i]
        if currentArg == '-h':
            lstNumberOfHost = sys.argv[i+1].split(",")
            minHost=int(lstNumberOfHost[0])
            maxHost=int(lstNumberOfHost[1])
        i=i+1;
    topo=CustomTopo()
    net = Mininet(topo, controller=partial( RemoteController, ip='127.0.0.1', port=6633 ))
    net.start()
    cmdName = "python PacketGeneration/SockServer.py"
    for host in net.hosts:
        host.cmd(cmdName + " -i " + host.IP() + " -p 5555 -d PacketGeneration/v3 &>mininetlog/server" + host.name + ".out &")
    CLI(net)
    for host in net.hosts:
        host.cmd("kill %'" + cmdName + "'") 
    net.stop()
    
