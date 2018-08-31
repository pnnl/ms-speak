#!/usr/bin/env python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
# import os, time
import socket
import sys
import gevent
import ansi as ans
import ssl

BIND_IP = '0.0.0.0'  # The default IP address to bind to
BIND_PORT_V5S = 8888 #7777  # The default port to listen on if the v5 server( pnl only permits 21/22/443/80/8080)
LOOP_HOST = '127.0.0.1'  # The IP address to connect to the translator at
RESP_FILE = 'v5_mr_PingURLResponse.xml'
gWait = False


class MyServer(HTTPServer):

	def __init__(
			self, server_address, requesthandlerclass, v5respfile, verboseness,
			usessl, certfile, keyfile, ssl_version=ssl.PROTOCOL_TLSv1,  # PROTOCOL_SSLv23 PROTOCOL_TLSv1
			bind_and_activate=True):
		HTTPServer.__init__(self, server_address, requesthandlerclass)

		self.addr = server_address
		self._v5RespFile = v5respfile
		self._resp_msg = None

		if self._v5RespFile:
			try:
				self._resp_msg = open(self._v5RespFile).read()
			# print "Using {} as a response file...".format(self._v5RespFile)
			except IOError as exc:
				print "Response file I/O error({0}): {1}".format(exc.errno, exc.strerror)
				gevent.sleep(4)
			except:  # handle other exceptions such as attribute errors
				print "Response file Unexpected error:", sys.exc_info()[0]
				gevent.sleep(4)
		else:
			print "NOT using a response file..."

		self.verbosity = verboseness
		self.useSSL = usessl
		self.certfile = certfile
		self.keyfile = keyfile
		self.ssl_version = ssl_version


class MyHTTPHandler(BaseHTTPRequestHandler):  # MyServer's requesthandlerclass
	protocol_version = 'HTTP/1.1'
	"""
	RequestHandler class for TCP server.

	Instantiated once per connection to the server
	and must override the handle() method to
	implement communication to the client. 
	"""
	_response_msg = None
	_verbosity = 0
	_useSSL = False

	def __init__(self, request, client_address, srvr):
		# BaseRequestHandler.__init__(self, request, client_address, srvr)
		BaseHTTPRequestHandler.__init__(self, request, client_address, srvr)

		self._addr = None
		self._v5ResponseFile = None
		self._response_msg = None
		self._verbosity = None
		self._useSSL = None
		self._host = None
		self._port = None
		self.requestline = None
		self.command = None
		self.path = None
		self.request_version = None
		self.headers = None
		self.close_connection = None

	def setup(self):  # called AFTER a connection is made
		self._addr = self.server.addr
		self._v5ResponseFile = self.server._v5RespFile
		self._response_msg = self.server._resp_msg
		self._verbosity = self.server.verbosity
		self._useSSL = self.server.useSSL
		self._host, self._port = self._addr
		print "Connected on {}:{} from {}".format(self._host, self._port, self.client_address)
		print "Waiting for a V5 Request..."
		BaseHTTPRequestHandler.setup(self)

	# handle GET command
	def do_GET(self):
		try:
			self._set_headers()
			self.wfile.write("<html><body><h1>GETs not handled.</h1></body></html>")

		except IOError:
			self.send_error(404, 'file not found')

	#  This method serves the 'HEAD' request type: it sends the headers it would send for the equivalent GET request.
	def do_HEAD(self, length):
		self.send_response(200)
		#self.send_response(400)
		self.send_header("content-type", "text/html")
		self.send_header("content-length", int(length))
		self.end_headers()

	def do_POST(self):  # this used to be 'do_post' in Phase1, but now when sending directly to v5Server from MultiSpeaker,
						# i wasn't getting called here until renamed it 'do_POST'
		global gWait
		# ans.clear()
		content_len = int(self.headers.getheader('content-length', 0))
		post_body = self.rfile.read(content_len)
		# print "a V5 Request of length %d has Arrived from the Pipeline: %s"  % (content_len, post_body)
		print "\nGot a V5 Request of length %d from the Pipeline." % content_len
		print "%s" % post_body
		if self._v5ResponseFile:
			print "Using response XML from {}.".format(self._v5ResponseFile)
			# Doesn't do anything with posted data
			#print "doing head..."
			self.do_HEAD(len(self._response_msg))
			#print "done head."
			if gWait:
				print("Press Any Key to Return a V5 Response to Pipeline, '*' to run continuously")
				key = ans.wait_key()
				if key == '*':
					gWait = False
			# self.wfile.write("<html><body><h1>POST BACK TO YA!</h1></body></html>")
			# print "Returning V5 Response..."#, self._response_msg
			self.wfile.write(self._response_msg)
			# ans.clear()
			# print "Returned V5 Response." #, self._response_msg
		else:
			print "NOT using a response file."
			#print "doing head..."
			#  reply = "<html><body><h1>POST BACK TO YA!</h1></body></html>"
			reply = "<html><body><h1>OK</h1></body></html>"
			self.do_HEAD(len(reply))
			self.wfile.write(reply)

		print "Waiting for Next Request..."

	#  reset;sudo tcpdump -i lo -v	# capture loopback traffic
	#  show all data, in hex:  sudo tcpdump -i lo tcp and port 7777 -s0 -vv -X -c 1000
	def my_parse_request(self):  # over-ride by renaming to parse_request
		"""Parse a request (internal)."""

		requestline = self.raw_requestline
		if requestline[-2:] == '\r\n':
			requestline = requestline[:-2]
		elif requestline[-1:] == '\n':
			requestline = requestline[:-1]
		self.requestline = requestline
		print("requestline:{}".format(requestline))
		words = requestline.split()
		version = None
		if len(words) == 3:
			[command, path, version] = words
			print("command:{}, path:{}, version:{}".format(command, path, version))
			if version[:5] != 'HTTP/':
				self.send_error(400, "Bad request version (%r)" % version)
				return False
			try:
				base_version_number = version.split('/', 1)[1]
				version_number = base_version_number.split(".")
				# RFC 2145 section 3.1 says there can be only one "." and
				#   - major and minor numbers MUST be treated as
				#	  separate integers;
				#   - HTTP/2.4 is a lower version than HTTP/2.13, which in
				#	  turn is lower than HTTP/12.3;
				#   - Leading zeros MUST be ignored by recipients.
				if len(version_number) != 2:
					raise ValueError
				version_number = int(version_number[0]), int(version_number[1])
			except (ValueError, IndexError):
				self.send_error(400, "Bad request version (%r)" % version)
				return False
			if version_number >= (1, 1) and self.protocol_version >= "HTTP/1.1":
				self.close_connection = 0
			if version_number >= (2, 0):
				self.send_error(505, "Invalid HTTP Version (%s)" % base_version_number)
				return False
		elif len(words) == 2:
			[command, path] = words
			self.close_connection = 1
			if command != 'GET':
				self.send_error(400, "Bad HTTP/0.9 request type (%r)" % command)
				return False
		elif not words:
			return False
		else:
			self.send_error(400, "Bad request syntax (%r)" % requestline)
			return False
		if version is None:
			version = "0.0.0"
		self.command, self.path, self.request_version = command, path, version

		# Examine the headers and look for a Connection directive
		self.headers = self.MessageClass(self.rfile, 0)

		conntype = self.headers.get('Connection', "")
		if conntype.lower() == 'close':
			self.close_connection = 1
		elif conntype.lower() == 'keep-alive' and self.protocol_version >= "HTTP/1.1":
			self.close_connection = 0
		return True

	#  this is unreachable.... BaseHTTPRequestHandler.parse_request(self)


def usage(name=None):
	return '''i.e., python %(prog)s v5_mr_PingURLResponse.xml -v'''


def dohelp(name=None):
	msg = "sends V5 Responses to the translator (defaults to Ip:{}, Port: {})".format(LOOP_HOST, BIND_PORT_V5S)
	return msg


############
##  Main  ##
############
try:

	import os.path
	import argparse

	# DebugTest()

	v3XsltOrResp = None

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('8.8.8.8', 0))  # connecting to a UDP address doesn't send packets
	local_ip_address = s.getsockname()[0]  # 130.20.185.0
	s.close()
	'''
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-v", "--verbose", action="store_true")
	group.add_argument("-q", "--quiet", action="store_true")
	'''
	parser = argparse.ArgumentParser(description='sends V5 Responses to the translator.', add_help=False
	                                 , epilog="i.e., python %(prog)s -v"
	                                 , usage=usage())
	parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help=dohelp())
	parser.add_argument('-i', '--v5Resp', help="V5 Response File to use")
	parser.add_argument('-ip', '--host', dest='BindIp', default=BIND_IP, help="IP Address to Bind to.")
	parser.add_argument("-L", "--LoopBack", dest='Loopback', action='store_true', help="Use Loopback mode")
	parser.add_argument('-nr','--no-resp', dest='no_resp', action='store_true', help="Do Not Send Response.")
	parser.add_argument('-p', '--port', dest='BindPort', default=None, help="TCP Port to Bind.")
	parser.add_argument('-r', '--revision', action='version', version='%(prog)s 1.0')
	parser.add_argument('-s', '--ssl', dest='UseSSL', action='store_true', help="Use SSL Encryption")
	parser.add_argument('-v', '--verbosity', action="count", default=1, help="increase output verbosity")  # -vvv
	parser.add_argument('-w', '--wait', dest='Wait', action='store_true',
	                    help="Pause and Display Messages as Received.")
	parser._positionals.title = 'Required arguments'
	args = parser.parse_args()
	v5ResponseFile = args.v5Resp
	verbosity = args.verbosity
	useSSL = args.UseSSL
	BindIp = args.BindIp
	BindPort = args.BindPort
	gWait = args.Wait
	loopback = args.Loopback
	no_response =  args.no_resp

	if not no_response:
		if v5ResponseFile is None and not no_response:
			v5ResponseFile = RESP_FILE
		if not os.path.isfile(v5ResponseFile):
			raise IOError('File does not exist: %s' % v5ResponseFile)

	if loopback:
		if BindIp != BIND_IP:
			raise RuntimeError("Cannot Specify both Loopback mode and an IP address!")
		BindIp = LOOP_HOST

	if BindPort is None:
		BindPort = BIND_PORT_V5S
	else:
		BindPort = int(BindPort)
except IOError as ex:
	print('Error: {}'.format(ex))
except argparse.ArgumentError:
	print "ArgumentError."
except argparse.ArgumentTypeError:
	print "Wrong type."
except SystemExit:
	pass
else:
	server = None
	try:
		# Create the server, bind it to host on port
		server = MyServer((BindIp, BindPort), MyHTTPHandler, v5ResponseFile, verbosity,
		                  useSSL, "server.crt", "server.key")

		# server_address = ('127.0.0.1', 80)
		# httpd = HTTPServer(server_address, KodeFunHTTPRequestHandler)
		# httpd.serve_forever()

		ans.clear()
		print "V5 HTTP Server @ {} Listening on {}:{}".format(local_ip_address, BindIp, BindPort)
		if not gWait:
			gevent.sleep(3)
		server.serve_forever(poll_interval=0.5)
	except KeyboardInterrupt:
		'''
		causes server to shut down but this only works in multiple threads application since the 
		shutdown needs to be called from different thread than the thread where serve_forever() is running
		or it will deadlock.
		So, just add the following in your request handler:
			self.server._BaseServer__shutdown_request = True
		The server will shutdown. This does the same thing as calling server.shutdown(), 
		just without waiting (and deadlocking the main thread) until it's shutdown

		'''
		print '\n\nServer Interrupted, Shutting Down Server of ', BindIp, ':', BindPort
		if server is not None:
			server._BaseServer__shutdown_request = True
		# server.shutdown()
		print 'Exiting...'
		sys.exit()

	except TypeError as e:
		print "** TypeError caught: {}".format(e)
	except:
		e = sys.exc_info()[0]
		print "** Exception caught: {}".format(e)
		raise
finally:
	# print 'Exiting...'
	pass

'''
determine the key length:
openssl rsa -in private.key -text -noout
The top line of the output will display the key size.

For example:

Private-Key: (2048 bit)
To view the key size from a certificate:

$ openssl x509 -in public.pem -text -noout | grep "RSA Public Key"
RSA Public Key: (2048 bit)


http://stackoverflow.com/questions/8582766/adding-ssl-support-to-socketserver
cat sample.xml | netcat localhost 8888

generate a 2048-bit RSA key pair:
	openssl genrsa -des3 -out private.pem 2048
						or
	openssl genrsa -des3 -out key.pem 2048

extract the public key (certificate) (Export the RSA Public Key to a File):
	openssl rsa -in private.pem -outform PEM -pubout -out public.pem
								or 
	openssl rsa -in key.pem -outform PEM -pubout -out server.pem
								or 
	openssl rsa -in key.pem -outform PEM -pubout -out cert.pem

( The -pubout flag is really important, Be sure to include it since
  without it the the meaning of the command changes from that of exporting the 
  public key to exporting the private key outside of its encrypted wrapper. )
  
	OR
	openssl genrsa -des3 -out server.orig.key 2048
	openssl rsa -in server.orig.key -out server.key
	openssl req -new -key server.key -out server.csr
	openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt	

NOTE: 
	wrap_socket(self._sock, ca_certs="cert.pem", cert_reqs=ssl.CERT_REQUIRED) failed
								but
	wrap_socket(self._sock, ca_certs="server.crt", cert_reqs=ssl.CERT_REQUIRED) worked...


start the v5 Server:
	python v5Server.py -v --host 64.184.186.24  
	python v5Server.py -v --host 130.20.185.0 
	python v5Server.py -v
start the v3 Client (server.crt):
	python v3Client.py -v --host 64.184.186.24  
	python v3Client.py -v --host 130.20.185.0 
	python v3Client.py -v

'''
