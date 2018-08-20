import errno
import getopt
import sys
import time
import os
from ConfigParser import ConfigParser
from collections import defaultdict
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.util import dumpNodeConnections	# DEBUG INFO
from subprocess import call
from functools import partial
from mininet.node import RemoteController
from mininet.node import Node
import threading
# TODO:
#
#	1) Use network id from argv
class myThread (threading.Thread):
	def __init__(self,netObject,hostIndex,args,name):
		threading.Thread.__init__(self)
		self.simulationNet = netObject
		self.args = args
		self.index = hostIndex
		self.name = name
	def run(self):
		print "Starting thread: " + self.name + " args:"
		print self.args
		p = self.simulationNet.hosts[self.index].popen(self.args)
		for line in iter (p.stdout.readline,''):
			sys.stdout.write("["+self.name+"] ")
			sys.stdout.write(line)

class SingleSwitchTopo(Topo):
	"Single switch connected to n hosts."
	def __init__(self, n=2, **opts):
		# Initialize topology and default options
		Topo.__init__(self, **opts)
		switch = self.addSwitch('s1')
		# Python's 'range(n)' generates 0..n-1
		for h in range(n):
			host = self.addHost("h%s" % (h + 1))
			self.addLink(host, switch)
			
def startNAT(root, inetIntf='eth0', subnet='172.16.0.0/12' ):
        """Start NAT/forwarding between Mininet and external network
        root: node to access iptables from
        inetIntf: interface for internet access
        subnet: Mininet subnet (default 10.0/8)="""
   
        # Identify the interface connecting to the mininet network
        localIntf =  root.defaultIntf()

    # Flush any currently active rules
        root.cmd( 'iptables -F' )
        root.cmd( 'iptables -t nat -F' )

    # Create default entries for unmatched traffic
        root.cmd( 'iptables -P INPUT ACCEPT' )
        root.cmd( 'iptables -P OUTPUT ACCEPT' )
        root.cmd( 'iptables -P FORWARD DROP' )

    # Configure NAT
        root.cmd( 'iptables -I FORWARD -i', localIntf, '-d', subnet, '-j DROP' )
        root.cmd( 'iptables -A FORWARD -i', localIntf, '-s', subnet, '-j ACCEPT' )
        root.cmd( 'iptables -A FORWARD -i', inetIntf, '-d', subnet, '-j ACCEPT' )
        root.cmd( 'iptables -t nat -A POSTROUTING -o ', inetIntf, '-j MASQUERADE' )

    # Instruct the kernel to perform forwarding
        root.cmd( 'sysctl net.ipv4.ip_forward=1' )
		
def stopNAT(root ):
        """Stop NAT/forwarding between Mininet and external network"""
        # Flush any currently active rules
        root.cmd( 'iptables -F' )
        root.cmd( 'iptables -t nat -F' )

    # Instruct the kernel to stop forwarding
        root.cmd( 'sysctl net.ipv4.ip_forward=0' )
def fixNetworkManager( root, intf ):
        """Prevent network-manager from messing with our interface,
           by specifying manual configuration in /etc/network/interfaces
           root: a node in the root namespace (for running commands)
           intf: interface name"""
        cfile = '/etc/network/interfaces'
        line = '\niface %s inet manual\n' % intf
        config = open( cfile ).read()
        if line not in config:
            print '*** Adding', line.strip(), 'to', cfile
        with open( cfile, 'a' ) as f:
            f.write( line )
        # Probably need to restart network-manager to be safe -
        # hopefully this won't disconnect you
     #   root.cmd( 'service network-manager restart' )
def connectToInternet(network, switch='s1', rootip='172.30.0.0', subnet='172.16.0.0/12'):
        """Connect the network to the internet
           switch: switch to connect to root namespace
           rootip: address for interface in root namespace
           subnet: Mininet subnet"""
        switch = network.get( switch )
        prefixLen = subnet.split( '/' )[ 1 ]

    # Create a node in root namespace
        root = Node( 'root', inNamespace=False )

    # Prevent network-manager from interfering with our interface
        fixNetworkManager( root, 'root-eth0' )

    # Create link between root NS and switch
        link = network.addLink( root, switch )
        link.intf1.setIP( rootip, prefixLen )

    # Start network that now includes link to root namespace
        network.start()

    # Start NAT and establish forwarding
        startNAT( root )

    # Establish routes from end hosts
        for host in network.hosts:
            host.cmd( 'ip route flush root 0/0' )
            host.cmd( 'route add -net', subnet, 'dev', host.defaultIntf() )
            host.cmd( 'route add default gw', rootip )

        return root
		
def PrintUsage():
	print("Usage: python decouple.py -h numberOfHosts (E.G. 2) -n networkID (E.G. 192.168.0.0) -c configFile (E.G. /etc/apache2/msp.conf) -a x,y,z (Run Apache on hosts x, y, and z) -f x,y,z (Run Firefox on hosts x, y, and z) -w x,y,z (Run WireShark on hosts x, y, and z) -x x,y,z (Run Xterm on hosts x, y, and z) -r host,interface,port,ip")
	sys.exit()


if __name__ == "__main__":
	# Variables (and some sane default values)
	strConfigFileLocation = "/usr/local/decouple/decouple.cfg"
	intNumberOfHosts = 2
	strNetworkID = "172.16.0.1"
	lstHostsApache = list()
	lstHostsFirefox = list()
	lstHostsWireshark = list()
	lstHostsXterm = list()
	lstEndPoints = list()	# From configuration file
	reassemblerOptions = list()

	# Parse command line arguments
	try:
		options, args = getopt.getopt(sys.argv[1:], "a:f:w:x:h:n:c:r:?")

		for o, a in options:
			if o == "-a":
				lstHostsApache = a.split(",")
			if o == "-f":
				lstHostsFirefox = a.split(",")
			if o == "-w":
				lstHostsWireshark = a.split(",")
			if o == "-x":
				lstHostsXterm = a.split(",")
			if o == "-h":
				intNumberOfHosts = int(a)
			if o == "-n":
				strNetworkID = a			
			if o == "-c":
				strConfigFileLocation = a
			if o == "-r":
				reassemblerOptions = a.split(",")
				if len(reassemblerOptions) != 4:
					print 'invalid options for reassembler'
					PrintUsage()
			if o == "-?":
				PrintUsage()
	except getopt.GetoptError as error:
		PrintUsage()

	# Parse configuration file
	#
	# NOTE: Not sure how we will use this yet, but it might be useful to know
	#       what role each host plays (although each Apache instance shares
	#       a common 'HTDOCS' file system and can fulfil any role).
	#
	config = ConfigParser()
        lstRoles = list()                       # A list of roles seen in the configuration file
        dictHostRoles = defaultdict(list)       # A dictionary of host names by role

	# Open config file
	config.read(strConfigFileLocation)

	# Populate lstRoles
	for role in config._sections['EndPoints']:
        	# Ignore built-in '__name__'
        	if (role != "__name__"):
                	# Append all others 
                	lstRoles.append(role)

	# Populate dictHostRoles
	for role in lstRoles:
        	hosts = config.get('HostRoles', role)
	        # Handle a range of hosts
	        if ("-" in hosts):
        	        lowerBound, upperBound = hosts.split("-")
                	for i in range(int(lowerBound),int(upperBound)+1):
                        	try:
                                	# Append the current host to the 'role' key in the dictionary
	                                dictHostRoles[role].append("h"+str(i))
        	                except KeyError, e:
                	                # Create the 'role' key if it does not exist
                        	        dictHostRoles[role] = { }
                                	# Add the current host to the 'role' key in the dictionary
	                                dictHostRoles[role] = "h"+str(i)

	        # Handle a single host
        	else:
                	try:
	                	# Append the current host to the 'role' key in the dictionary
        	                dictHostRoles[role].append("h" + hosts)
        	        except KeyError, e:
                	        # Create the 'role' key if it does not exist
                        	dictHostRoles[role] = { }
	                        # Add the current host to the 'role' key in the dictionary
        	                dictHostRoles[role] = "h" + hosts

	# EXAMPLE: The next four lines of code show how to get a list of hosts by a given role.
	#
	# lstMRHosts = dictHostRoles.get('mr', { })	# 1
	# print("Available MR hosts: \n")		# 2
	# for host in lstMRHosts:			# 3
	#	print(host + "\n")			# 4

	# Make mininet topology
	setLogLevel("info")

	# SimpleTest()
        "Create and test a simple network."
        topo = SingleSwitchTopo(n=intNumberOfHosts)
	# TODO: IP/Port could be parameterized.
	net = Mininet(topo=topo, controller=partial(RemoteController, ip='192.168.2.103', port=6633),ipBase='172.16.0.0/12')
	rootnode = connectToInternet(net)
    # start call is taken care of in connectToInternet function
	#net.start()

	# DEBUG INFO
	# dumpNodeConnections(net.hosts)

	# Create and modify the necessary Apache configuration files for each Mininet host
	#
	for h in range(intNumberOfHosts):
		# Copy the various apache config files
		call(["cp", "/etc/apache2/default.conf.template", "/etc/apache2/" + str(h+1) + ".conf"])					#1
		call(["cp", "/etc/apache2/envvars.template", "/etc/apache2/envvars"])								#2
		call(["cp", "/etc/apache2/ports.conf.template", "/etc/apache2/ports" + str(h+1) + ".conf"])					#3
		call(["cp", "/etc/apache2/sites-available/000-default.conf.template", "/etc/apache2/sites-available/" + str(h+1) + ".conf"])	#4

		# Link the sites-available/conf file to ../sites-enabled
		try:
			# Creat the symbolic link
			os.symlink("/etc/apache2/sites-available/" + str(h+1) + ".conf", "/etc/apache2/sites-enabled/" + str(h+1) + ".conf")	#5
		except OSError, e:
			# Unless the link already exists, then...
			if e.errno == errno.EEXIST:
				# Delete the link
				os.remove("/etc/apache2/sites-enabled/" + str(h+1) + ".conf")
				# and recreate it (This is necessary because the host IP may have changed.)
				os.symlink("/etc/apache2/sites-available/" + str(h+1) + ".conf", "/etc/apache2/sites-enabled/" + str(h+1) + ".conf")


		# Edit '/etc/apache2/X.conf' (#1) to include ServerName, PID file, portsX.conf, and site-enabled/X.conf
		apache = ""
		f = open("/etc/apache2/" + str(h+1) + ".conf", "r")
		while(True):
			line = f.readline()
			if not line:
				break
			else:
				# Store the first part of 'X.conf'
				apache = apache + line
				# Seek to the appropriate line in 'X.conf' to add PID file, portsX.conf, and site-enabled/X.conf
				if "E.G. ServerName a.b.c.d" in line:
                                        host = net.get("h" + str(h+1))
                                        apache = apache + "ServerName " + host.IP() + "\n"
				elif "E.G. PidFile ${APACHE_PID_FILEX}" in line:
					# Add PID file
					apache = apache + "PIDFile ${APACHE_PID_FILE" + str(h+1) + "}\n"
				elif "E.G. Include portsX.conf" in line:
					# Add portsX.conf
					apache = apache + "Include ports" + str(h+1) + ".conf\n"
				elif "E.G. IncludeOptional sites-enabled/X.conf" in line:
					# Add sites-enabled/X.conf
					apache = apache + "IncludeOptional sites-enabled/" + str(h+1) + ".conf\n"
		# Store the rest of 'X.conf'
		f.close()

		# Write the new version of 'X.conf'
		f = open("/etc/apache2/" + str(h+1) + ".conf", "w")
		f.write(apache)
		f.close()


		# Edit '/etc/apache2/portsX.conf' (#3) to include Listen
		ports=""
		f = open("/etc/apache2/ports" + str(h+1) + ".conf", "r")
		while(True):
			line = f.readline()
			if not line:
				break
			else:
				# Store the first part of 'portsX.conf'
				ports = ports + line
				# Seek to the appropriate line in 'portsX.conf' to add Listen
				if "E.G. Listen a.b.c.d:p" in line:
					# Add Listen
					host = net.get("h" + str(h+1))
					ports = ports + "Listen " + host.IP() + ":80\n"
		# Store the rest of 'portsX.conf'
		f.close()

		# Write the new version of 'portsX.conf'
		f = open("/etc/apache2/ports" + str(h+1) + ".conf", "w")
		f.write(ports)
		f.close()

		# Edit '/etc/apache2/sites-available/X.conf' (#4) to add ServerName
		sitesAvailable = ""
		f = open("/etc/apache2/sites-available/" + str(h+1) + ".conf", "r")
		while(True):
			line = f.readline()
			if not line:
				break
			else:
				# Store the first part of 'sites-available/X.conf'
				sitesAvailable = sitesAvailable + line
				if "E.G. ServerName a.b.c.d" in line:
					# Add ServerName
					host = net.get("h" + str(h+1))
					sitesAvailable = sitesAvailable + "\tServerName " + host.IP() + "\n"
		# Store the rest of 'sites-available/X.conf'
		f.close()

		# Write the new version of 'sites-available/X.conf'
		f = open("/etc/apache2/sites-available/" + str(h+1) + ".conf", "w")
		f.write(sitesAvailable)
		f.close()

	# Edit '/etc/apache2/envvars' (#2) to include a PID environment variable for each host
	#
	# Create a new version of 'envvars' in memory
	envvars = ""
	f = open("/etc/apache2/envvars", "r")
	while(True):
		line = f.readline()
		if not line:
			break
		else:
			# Store the first part of 'envvars'
			envvars = envvars + line
			# Seek to the appropriate line in 'envvars' to add the PID variables
			if "List PID variables here..." in line:
				# Add a PID environment variable for each host
				for h in range(intNumberOfHosts):
					envvars = envvars + "export APACHE_PID_FILE" + str(h+1) + "=/var/run/apache2/" + str(h+1) + "$SUFFIX.pid\n"
		# Store the rest of 'envvars'
	f.close()

	# Write the new version of 'envvars'
	f = open("/etc/apache2/envvars", "w")
	f.write(envvars)
	f.close()

	# TODO: Use a for-loop to start apache on each host
	for h in range(intNumberOfHosts):
		host = net.get("h" + str(h+1))

	# Parse command-line arguments to determine what to start on each host
	#
	# Apache
        for h in lstHostsApache:
		hostNumber = str(h)
                hostName = "h" + hostNumber
                host = net.get(hostName)
                host.cmd("/usr/sbin/apachectl -f /etc/apache2/" + hostNumber + ".conf")
		print("/usr/sbin/apachectl -f /etc/apache2/"+hostNumber+".conf")
	#
	# Firefox
        for h in lstHostsFirefox:
		hostNumber = str(h)
                hostName = "h" + hostNumber
                host = net.get(hostName)
                host.cmd("firefox &")
	#
	# Wireshark
        for h in lstHostsWireshark:
		hostNumber = str(h)
                hostName = "h" + hostNumber
                host = net.get(hostName)
                host.cmd("wireshark &")
	#
	# Xterm
	for h in lstHostsXterm:
		hostNumber = str(h)
		hostName = "h" + hostNumber
		host = net.get(hostName)
		host.cmd("xterm &")
	#	
	# Reassembler program (may need to run using popen?)
	if (len(reassemblerOptions) > 0):
    		hostNumber = str(reassemblerOptions[0])
		hostName = "h" + hostNumber
		host = net.get(hostName)
	# TODO: validate arguments, # device, port, IP
		
		device = reassemblerOptions[1]
		port = reassemblerOptions[2]
		IP = reassemblerOptions[3]
		path = '/home/dcleckley/capture-test/PacketCapture/Reassembler.py'
		args = ['/usr/bin/python',path,device,port,IP]
		reassemblerThread = myThread(net,int(hostNumber)-1,args,"reassembler")
		reassemblerThread.start()

	# Run forever until the 'decouple.run' control file contains a '0' (false).
	f = open("decouple.run", "r")
	run = f.read(1)
	f.close()

	print("You asked for " + str(intNumberOfHosts) + " hosts on a network ID of " + strNetworkID + " using a config file at " + strConfigFileLocation);

	print("Change the contents of 'decouple.run' from '1' to '0' to end...") 

	while(bool(int(run))):
		time.sleep(5)	# seconds

		f = open('decouple.run', 'r')
		run = f.read(1)
		f.close()
		
	# Clean up resources
	stopNAT(rootnode)
	net.stop()
	call(["mn","-c"])

	call(["killall", "/usr/sbin/apache2"])
	reassemblerThread.join(3)
	# TECHNICAL DEBT: Convert intNumberOfHosts to a string, then get the string length to determine how many '?' to pad to these to delete all the config files
	#		  Use a reverese for loop to delete ???.conf, then ??.conf, and finally ?.conf.
	# LOGIC BUG: 'File not found'
	# call(["rm", "/etc/apache2/?.conf"])
	# call(["rm", "/etc/apache2/ports*.conf"])
	# call(["rm", "/etc/apache2/envvars"])
	# call(["rm", "/etc/apache2/sites-available/?.conf"])
	# call(["rm", "/etc/apache2/sites-enabled/?.conf"])
