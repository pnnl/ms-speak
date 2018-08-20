# Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
from multiprocessing import Process, Queue
import os
from cassandra.cluster import Cluster
from cassandra.io.libevreactor import LibevConnection
import re
import logging
import time

class Timer:
	def __enter__(self):
		self.start = time.clock()
		return self
	def __exit__(self, *args):
		self.end = time.clock()
		self.interval = self.end - self.start

class MultispeakParser(Process):
	
	def __init__(self, queue):
		print "Multispeak Parser Initialized"
		self.queue = queue
		logging.basicConfig(level=logging.DEBUG)
		Process.__init__(self)
		
	def initCluster(self):	# initialize cassandra cluster, prepared queries
		os.system('ping 127.0.0.1 -c 1')
		os.system('ping 10.21.1.24 -c 1') 
		cluster = Cluster(['127.0.0.1','10.21.1.24']) # must use connection class libevConnection (rather than default AsyncoreConnection)
		self.session = cluster.connect('demo')
		self.preparedQuery = self.session.prepare("INSERT into packet (source_addr, dest_addr, time_stamp,content,text_values) VALUES (?,?,?,?,?)")
		self.namespace  = {'a':'http://schemas.xmlsoap.org/soap/envelope/'}
		
	def run(self):
		self.initCluster()
		
		while True:
		
			logging.debug('Waiting for item in queue...')
			(((src, sport),(dst,dport)), frame, timestamp) = self.queue.get()
			logging.debug('Retreived item from queue')
			with Timer() as q:
				#try to find the endpoint type from POST Request
				endpointRegex = '(?<=POST\s).*(?=\sHTTP)'	# looks for POST and HTTP, and matches the URL
				match = re.search(endpointRegex,frame)
				# Example: POST /foo/QA_server HTTP1.1\r\n
				# regex matches [/foo/QA_SERVER]
				if match is not None:
					URLsplit = frame[match.start():match.end()].split('/')	# [foo,QA_SERVER]
					endpointCodeSplit = URLsplit[-1].split('_') # [QA,SERVER]
					endpointCode = endpointCodeSplit[0] # QA
					logging.debug("parsed MS endpoint code: {}".format(endpointCode))
				else:
					endpointCode = 'NULL'
					logging.warning("Unable to parse endpoint code from header")
				#get the version from the SOAPAction http header
				versionRegex = '(?<=SOAPAction:\s"http:\/\/www.multispeak.org\/Version_).' # uses lookbehind to extract only version num
				match = re.search(versionRegex,frame, re.IGNORECASE)
				if match is not None:
					mspVersion = frame[match.start()]
					logging.debug("parsed MS version = {}".format(mspVersion))
					if (mspVersion != '3' and mspVersion != '5'):	#incorrect/unsupported version parsed, set field to Null
						mspVersion = 'NULL'
						logging.warning("incorrect version string found")
				else:												# didn't find a version at all
					versionRegex2 = '(?<=SOAPAction:\shttp:\/\/www.multispeak.org\/Version_).' # uses lookbehind to extract only version num
					match2 = re.search(versionRegex2, fram, re.IGNORECASE)
					if match2 is not None:
						mspVersion = frame[match2.start()]
						logging.debug("parsed MS version = {}".format(mspVersion))
						if (mspVersion != '3' and mspVersion != '5'):	#incorrect/unsupported version parsed, set field to Null
							mspVersion = 'NULL'
							logging.warning("incorrect version string found")
					else:
						mspVersion = 'NULL'
						logging.warning("no version string found")
				
				# find the start of the XML.
				with Timer() as t :
					with Timer() as f:
						messageNameRegex = '(<[\w:]*[Bb]ody>)(\s*)(<)(?P<MsgName>[\w|:]+)'
						match = re.search(messageNameRegex,frame)
						messageName = match.group('MsgName').split(':')[-1]		# look at the message name group, and remove the namespace (if there is one)
						text_values = {'endpoint':endpointCode,'messagetype':messageName,'mspVersion':mspVersion}
					print("xml parsing before insertion Timer: %.07f sec" % f.interval)
					logging.debug( "text values: {}".format(text_values))
					args = [src,dst,timestamp,frame,text_values]
					self.session.execute(self.preparedQuery, args)
				print("Envelope xml parsing and insertion Timer: %.07f sec" % t.interval)
			print("Full callback, all parsing and insertion: %.07f sec" % q.interval)
			logging.info("inserted packet")
if __name__ == '__main__':
	print ("Do not run this file directly")
	sys.exit(3)
	