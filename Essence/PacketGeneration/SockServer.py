# Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
import SocketServer
import getopt
import sys
from lxml import etree		# xml parsing
import re
import socket #ip address parsing only

class MyTCPHandler(SocketServer.BaseRequestHandler):
	"""
	The RequestHandler class for our server.

	It is instantiated once per connection to the server, and must
	override the handle() method to implement communication to the
	client.
	"""

	def handle(self):		
		# self.request is the TCP socket connected to the client
		buffer = ''
		envelopeRegex = '</.+:[Ee]nvelope'
		while 1:
			self.data = self.request.recv(1024).strip()
			if not self.data: break
			print "{} wrote:".format(self.client_address[0])
			print self.data
			buffer += self.data
		# send back the appropriate reply for the particular message
			print "buffer {}".format(buffer)
			if (re.search(envelopeRegex,  buffer)):
				print "found end of message"
				endpoint,messageName = self.parseMessageTuple(buffer)
				if not self.server.directory.endswith('/'):		#properly format directory
					self.server.directory = self.server.directory + "/"
				responseMessagePath = self.server.directory + endpoint + "/" + messageName + "Response.xml"
				responseMessage = self.genHTTP(responseMessagePath)
				self.request.sendall(responseMessage)
				print "Server Replied With: "
				print responseMessage
				buffer = ''	# clear recv buffer
			else:
				print "did not find end of envelope"
	
	def parseMessageTuple(self,data):
		#try to find the endpoint type from POST Request
		endpointRegex = '(?<=\/).{2,3}(?i)(?=_SERVER)'	# looks for (case-insensitive) _SERVER to be present in a URL. Parses 2 or 3 characters preceeding that
		match = re.search(endpointRegex,data)
		if match is not None:
			endpointCode = data[match.start():match.end()]
			print("parsed MS endpoint code: " + endpointCode)
		else:
			endpointCode = 'NULL'
		
		envelopeRegex = '<([^/])+:[Ee]nvelope'
		match = re.search(envelopeRegex,data)
		index = match.start()
		tree = etree.fromstring(data[index:] )	# parse the incoming packet
		body = [] 
		body = tree.xpath("//*[local-name() = 'Body']")	# get body attribute, doesn't require namespace
		messageText = body[0].getchildren()[0].tag	# select the immediate child of the body tag, which is "always" the multispeak message
						# tag is the text value
		stripDomainNameRegex = '\{([^\}]+)\/'		# filter the domain name
		messageStripped = re.sub (stripDomainNameRegex,'',messageText)		# remove the namespace from the tag
		endpoint, messageName = messageText.split('}')
		print "Server Parsed Message Name: ", messageName
		return endpointCode, messageName
	def genHTTP(self, multispeak_message_ID):
		multispeak = self.genMultiSpeak(multispeak_message_ID)
		# HTTP part of msg
		version = "HTTP/1.1 200 OK\r\n"
		# todo: need to change header to be compatible with v3. right now hardcoded for v5 messages
		headers = "Accept-Encoding: gzip,deflate\r\nContent-Type: text/xml;charset=UTF-8\r\nSOAPAction: \"http://www.multispeak.org/Version_3.0/"+str(multispeak_message_ID).split('/')[-1]+"\"\r\n" #remove filepath if messagename is a whole file instead of hardcoded
		conlen = "Content-Length: "+str(len(multispeak))+"\r\n"
		hostIP = "Host: " + socket.gethostbyname(socket.gethostname())
		hostPort =  ":80\r\n"
		conn = "Connection: Keep-Alive\r\n"
		uagent = "Apache-HttpClient/4.1.1 (java 1.5)\r\n\r\n"
		
		return version + headers + conlen + hostIP + hostPort + conn + uagent + multispeak
		
	def genMultiSpeak(self, multispeak_message_ID):
		# input parameter is xml name of response message to the particular request
		x = open(multispeak_message_ID,'r').read()
		return x
		
if __name__ == "__main__":
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hi:p:d:")
	except getopt.GetoptError:
		print 'TcpServer.py -i <serverIP> -p <serverPort> -d <root directory of xml messages>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'TcpServer.py -i <serverIP> -p <serverPort> -d <root directory of xml messages>'
			sys.exit(2)
		elif opt == '-i':
			ServerIP = arg
		elif opt == '-p':
			ServerPort = int(arg)
		elif opt == '-d':
			directory = str(arg)
		
	if (ServerIP == '') or (ServerPort == '') or (directory == ''):
		print 'required arguments missing, try again. see -h for help'
		sys.exit(2)
	HOST, PORT = ServerIP, ServerPort
	
	# Create the server, binding to localhost on port 9999
	server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
	server.directory = directory	# pass the XML directory to the server instance
	# Activate the server; this will keep running until you
	# interrupt the program with Ctrl-C
	server.serve_forever()
