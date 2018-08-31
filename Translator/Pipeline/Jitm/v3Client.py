#!/usr/bin/env python

from struct import *
from xml.etree import ElementTree
import xml.dom.minidom
import socket
import sys, os, errno, time
import ansi as AN
import ssl
import gevent
import httplib # , urllib  # The httplib module has been renamed to http.client in Python 3
#from OpenSSL.SSL import SENT_SHUTDOWN

# Constants
#XL8_HOST = '192.168.88.24'
XL8_HOST = '64.184.186.24'	# The IP address to connect to the translator at
XL8_PORT = 8080				# The port	   to connect to the translator at
LOOP_HOST = '127.0.0.1'		# The IP address to connect to the translator at
LOOP_PORT = XL8_PORT #7776	# The port	   to connect to the translator at
REQ_FILE = 'v3_mr_PingURL.xml'
MSGLEN = 8192

class ClientHandler:
	_verbosity = 0
	_usessl = False
	_sock = None
	_ssl_sock = None
	_httpconn = None
	_usehttp = None

	def __init__(self, verboseness, usessl, cert, http, sock=None):
		self._usehttp = http
		if( self._usehttp ):
			return

		try:
			if sock is None:
				self._sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
				#elf._sock.setblocking(0) NOTE: IF THIS IS ENABLE, THAN THE TMO DOES NOT THROW AN EXCEPTION
				self._sock.settimeout( 2 )
			else:
				self._sock = sock
			self._verbosity = verboseness
			self._usessl = usessl
			if self._usessl:
				self._ssl_sock = ssl.wrap_socket(self._sock,
						   ca_certs=cert,
						   cert_reqs=ssl.CERT_REQUIRED, ssl_version=ssl.PROTOCOL_TLSv1 )# PROTOCOL_TLSv1 PROTOCOL_SSLv23
		except ssl.SSLError as e:
			print "** SSLError: %s" % e
			raise

		except:
			e = sys.exc_info()[0]
			print "** exception: %s" % e
			raise

	def connect(self, host, port):
		try:
			if( self._usehttp ):
				self._httpconn = httplib.HTTPConnection(host, port) #, 10)
			else:
				if self._usessl:
					self._ssl_sock.connect((host, port))
				else:
					self._sock.connect((host, port))
		except:
			e = sys.exc_info()[0]
			print "** Error Connecting to Host {}, Port {}: {}".format(host, port, e)
			raise

	def send(self, msg):
		# None is returned on success. On error, an exception is raised, and
		# there is no way to determine how much data, if any, was successfully sent.
		try:
			if( self._usehttp ):
				'''
				this is from MultiSpeaker:
					POST HTTP/1.1
					Host: 127.0.0.1:8888
					Content-Length: 1214
					Content-Type: text/xml;charset=utf-8
					SOAPAction: http://www.multispeak.org/Version_3.0/PingURL
				this is from cUrl:
					POST HTTP/1.1
					Host: 127.0.0.1:8080
					User-Agent: curl/7.52.1
					Content-Length: 1205
					Content-Type: application/x-www-form-urlencoded
					Expect: 100-continue
				this is from Wake Forest pcap:
					HTTP/1.1
					Host: 10.7.14.184:50080
					User-Agent: gSOAP/2.8
					Content-Type: text/xml; charset=utf-8
					Content-Length: 603
					Connection: close
					Accept-Encoding: gzip, deflate
					SOAPAction: ""			'''
				#params = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
				# if i use "Connection" : "close", the response.read doesn't return until the server closes
				headers = {  "User-Agent" : "gSOAP/2.8"
						   , "Content-type" : "text/xml; charset=utf-8"
						   , "Connection" : "keep-alive"
						   , "Accept-Encoding" : "gzip, deflate"
						   , "SOAPAction" : "http://www.multispeak.org/Version_3.0/PingURL"
						   }
				#conn = httplib.HTTPConnection("bugs.python.org")
				self._httpconn.request("POST", "", msg, headers)
				sent = None
			else:
				if self._usessl:
					#sent = self._ssl_sock.send(msg[totalsent:])
					sent = AN.send_msg( self._ssl_sock, msg )
				else:
					#sent = self._sock.send(msg[totalsent:])
					sent = AN.send_msg( self._sock, msg )

		except KeyboardInterrupt:
			print 'KeyboardInterrupted in send.'
			raise
		except:
			e = sys.exc_info()[0]
			print "** send:exception: %s" % e
			return 0

		return sent

	def receive(self):
		if( self._usehttp ):
			try:
				# Returns an HTTPResponse instance.
				response = self._httpconn.getresponse()
				if( response.status != 200 ):
					print('Response not OK: %d, %s' % (response.status, response.reason))
				#	return None
				data = response.read() # returns the response body
				data.strip()
				return data
			except httplib.HTTPException:
				print "** HTTPException."
				raise httplib.HTTPException('*** HTTPException. ***')
			except IOError as exc:
				print "** IOError: %s" % exc
			except ValueError as exc:
				print "** ValueError: %s" % exc
			return None
		else:
			try:
				if self._usessl:
					r = AN.recv_msg( self._ssl_sock )
					return r
				else:
					r = AN.recv_msg( self._sock )
					return r
			except socket.timeout: # this appears to have to come before except socket.error else socket.error is caught
					return None
			except ssl.SSLError, why:
				if why.message == 'The read operation timed out':
					return None
				if why.args[0] in (errno.EAGAIN, errno.EWOULDBLOCK, errno.ECONNRESET, errno.ECONNABORTED):
					if why.args[0] == errno.EAGAIN:
						if self._verbosity >= 2:
							print "** EAGAIN **"
					elif why.args[0] == errno.EWOULDBLOCK:
						if self._verbosity >= 2:
							print "** EWOULDBLOCK **"
					elif why.args[0] == errno.ECONNRESET:
						if self._verbosity >= 2:
							print "** ECONNRESET **"
					elif why.args[0] == errno.ECONNABORTED:
						if self._verbosity >= 2:
							print "** ECONNABORTED **"
				elif why.args[0] == errno.ETIMEDOUT:
					print "** socket.error: ETIMEDOUT"
				else:
					e = sys.exc_info()[0]
					print "** socket.error: %s" % e
					raise
			except socket.error, why:
				if why.args[0] in (errno.EAGAIN, errno.EWOULDBLOCK, errno.ECONNRESET, errno.ECONNABORTED):
					if why.args[0] == errno.EAGAIN:
						if self._verbosity >= 2:
							print "** EAGAIN **"
					elif why.args[0] == errno.EWOULDBLOCK:
						if self._verbosity >= 2:
							print "** EWOULDBLOCK **"
					elif why.args[0] == errno.ECONNRESET:
						if self._verbosity >= 2:
							print "** ECONNRESET **"
						raise
					elif why.args[0] == errno.ECONNABORTED:
						if self._verbosity >= 2:
							print "** ECONNABORTED **"
						raise
					else:
						print "** socket.error: EAGAIN, EWOULDBLOCK, ECONNRESET or ECONNABORTED"
				elif why.args[0] == errno.ETIMEDOUT:
					print "** socket.error: ETIMEDOUT"
				else:
					e = sys.exc_info()[0]
					print "** socket.error: %s" % e
					raise
			except KeyboardInterrupt:
				print 'KeyboardInterrupted in receive.'
				raise
			except:
				e = sys.exc_info()[0]
				print "** exception: %s" % e

	def shutdown(self):
		print 'Closing socket...'
		if( self._usehttp ):
			self._httpconn.close()
		else:
			if self._usessl:
				self._ssl_sock.close()
			else:
				self._sock.close()

def usage( name=None):
	return '''i.e., python %(prog)s v3_mr_PingURL.xml -v '''

def dohelp( name=None):
	msg = "sends a V3 Request to the translator (defaults to sending '{} to'Ip:{}, Port: {})".format(REQ_FILE, XL8_HOST, LOOP_PORT)
	return msg

#
#-- main -----------------------------------------------------------------------------------------
#
def main():
	try:
		import os.path
		import argparse # https://docs.python.org/3/library/argparse.html
		verbosity = 0
		inputXml = None
		outputXml = None
		useSSL = None
		typeData = None
		client = None
		HostIp  = None
		Port  = None

		import commands
		#XL8_HOST = commands.getoutput("hostname -I") # 64.184.186.24 192.168.88.24
		#XL8_HOST = commands.getoutput("hostname -i") # 64.184.186.24

		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(('8.8.8.8', 0))  # connecting to a UDP address doesn't send packets
		local_ip_address = s.getsockname()[0] # 130.20.185.0
		s.close()
		#
		#local_ip_address = socket.gethostbyname(socket.gethostname()) # 127.0.1.1
		# XL8_HOST = socket.gethostname()  #getfqdn() gethostname

		parser = argparse.ArgumentParser(description='Sends MultiSpeak V3 Messages, Reads back the corresponding V5 Response Messages',
										 add_help=False, epilog="i.e., python %(prog)s -v"
										 , usage=usage())

		parser.add_argument('-c', '--count', dest='Count', help="Number of messages to send in burst.", type=int, default=1)
		parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help=dohelp())
		parser.add_argument('-i', "--inputXml",  help="Input XML File to use for V3 Packet")
		parser.add_argument('-ip', '--host', dest='HostIp', default=XL8_HOST, help="IP Address of pipeline.")
		parser.add_argument('-L', "--LoopBack", dest='Loopback', action='store_true', help="Use Loopback mode")
		parser.add_argument('-o', "--outputXml", help="File to save V5 Message to")
		parser.add_argument('-p', '--port', dest='Port', help="TCP Port of pipeline.", type=int)
		parser.add_argument('-r', '--revision', action='version', version='%(prog)s 1.0')
		parser.add_argument('-s', '--ssl', dest='UseSSL', action='store_true', help="Use SSL Encryption")
		parser.add_argument('-t', '--type', dest='Type', action='store_true', help="Type data instead of using a file")
		parser.add_argument('-v', "--verbosity", action="count", default=1, help="increase output verbosity") # -vvv
		parser.add_argument('-w', '--wait', dest='Wait', action='store_true', help="Pause and Display Messages as Received.")
		parser._positionals.title = 'Required arguments'
		args = parser.parse_args()

		verbosity = args.verbosity
		inputXml  = args.inputXml
		outputXml = args.outputXml
		useSSL = args.UseSSL
		typeData = args.Type
		wait = args.Wait
		loopback = args.Loopback

		Count = args.Count
		Port = args.Port
		if( loopback ):
			HostIp = LOOP_HOST
			if( Port is None ):
				Port = LOOP_PORT
			else:
				Port = int(Port)
		else:
			HostIp = args.HostIp
			if( Port is None ):
				Port = XL8_PORT
			else:
				Port = int(Port)

		if( not typeData ):
			if( inputXml is None ):
				inputXml = REQ_FILE
			if( not os.path.isfile(inputXml) ):
				raise IOError('File does not exist: %s' % inputXml)

		if( useSSL ):
			if( not os.path.isfile("server.crt") ):
				raise IOError('Certificate File does not exist: %s' % "server.crt")
		useHttp = True # True False
		client = ClientHandler( verbosity, useSSL, "server.crt", useHttp )

	except IOError as ex:
		print('Error: {}'.format(ex))
	except KeyboardInterrupt:
		exit()
	except argparse.ArgumentError:
		print "ArgumentError."
	except argparse.ArgumentTypeError:
		print "Wrong type."
	except SystemExit:
		if inputXml is None:
			#print "	you need to specify an input xml file"
			#parser.print_help()
			pass
		pass
	except NameError as e:
		print "** NameError caught: {}".format(e)
	except:
		e = sys.exc_info()[0]
		print "** Exception caught: {}".format(e)
		raise
	else:
		try:
			AN.clear()
			print "V3 Client @ {} Connecting to Pipeline @ {}, on Port {}".format(local_ip_address, HostIp, Port)
			client.connect(HostIp, Port)

			key = '0'
			#print AN.BOLD + AN.GREEN + AN.WHITEBG + 'this is bold green on white' + AN.RESET
			print "Connected."
			if( not wait ): # if not waiting, send packets continuously
				typeData = False
				verbosity = 0
				gevent.sleep(3)
			else:
				strg = "send a v3 request pkt"

			if( not typeData ):
				#strg = "send a v3 request pkt"
				msg = open(inputXml).read()
			else:
				strg = "Enter Some Data To Send"
				msg = None

			modder = 0
			key = '1'
			while key != '0':
				if( key == '1' ):
					if( wait ): # if not waiting, send packets continuously
						print("Press '1' to {},'0' to exit or '*' to run continuously: ".format(strg))
						key = AN.wait_key()
						if( key == '*' ):
							wait = False
							if( msg is None ):
								msg = open(inputXml).read()
						elif( key <> '1' ):
							continue
					AN.clear()
					if( typeData ):
						msg = raw_input("Enter something to send: ")
					#CountList = [1] * Count
					CountList = [x for x in range(Count)]
					for i in CountList:
						print( "sending msg {}".format(i) )
						sent = client.send( msg )
						if( i < Count-1 ):
							print "checking for response..."
							client.receive() # you can't send multiple msgs without doing a receive in between.
					if( not sent is None ):
						raise RuntimeError( "Sanity Failure({}) on send_msg, assure IP:Port are correct.".format(sent) )
					else:
						if verbosity >= 1:
							print "\nSent the V3 Message..."
						key = '2'
				elif( key == '2' ):
					AN.clear()
					if( modder ):
						print "checking for pipeline response pkt..."
					else:
						print "   checking for pipeline response pkt"

					modder = (modder+1) % 2
					v5Msg = client.receive()
					if( v5Msg is not None ):
						if( wait ):
							if outputXml is not None:
								with open( outputXml, 'w') as ofile:
									ofile.write( v5Msg )
						if( len(v5Msg) > 0 ):
							print("\nReceived a V3 Response Message from Pipeline:\n{}".format(v5Msg) )
						else:
							print("\nReceived a NULL V3 Response Message from Pipeline:\n" )
						if( not wait ): # 'wait' means wait for user to press a key....
							gevent.sleep(2)
						key = '1'
					else: # must been a non-200 response
						key = '1'
						#gevent.sleep(2.50) #don't need this, recv socket has tmo
				else:
					key = '1'
					continue
			# while
			if verbosity >= 1:
				print "\n"
		except KeyboardInterrupt:
			print 'KeyboardInterrupt Caught.'
		except RuntimeError as e:
			print "\n***** RuntimeError Caught: {}".format(e)
			print "*****       Attempted Connection to {}:{}\n".format(HostIp, Port)
		except AttributeError as e:
			print "\n***** AttributeError Caught: {}".format(e)
		except NameError as e:
			print "\n***** NameError Caught: {}".format(e)
		except:
			e = sys.exc_info()[0]
			print "** Exception caught: {}".format(e)
			raise
	finally:
		if( client ):
			print 'Shutting Down Client...'
			client.shutdown()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print 'KeyboardInterrupted.'
	finally:
		print 'Exiting...'
		sys.exit()

'''
cat sample.xml | netcat localhost 8888
alias v3c='python v3Client.py -v' -i someother.xml --port

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
	
	
python v3Client.py -w -L -p 8080
'''
