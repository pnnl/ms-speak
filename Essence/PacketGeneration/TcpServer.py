# Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
# receives messages from tcp client and echos back a success message
# reassembler not imported in this file, use /capture-test/PacketCapture/Reassembler.py

import socket
import sys, getopt
from SocketServer import *
from threading import Thread

def printableHex(buf):
    return ' '.join(x.encode('hex') for x in buf)

def handler(clientsocket, clientaddr):
	total = 0
	print "Accepted conn from: ", clientaddr
	
	while 1:
		try:
			data = clientsocket.recv(1024)
		except:
			print "receive error"
			break
		if not data:
			break
		print "received data len: ", len(data)
		total += len(data)
		msg = str(total) + " "
		try: 
			clientsocket.send(msg)
		except Exception as exc:
			print exc
			print "error sending server response"
			break
	clientsocket.close()
	print "total len: ", total

def main(argv):
	ServerIP = ''
	ServerPort = 0
	count = 1
	BUFFER_SIZE = 1024 # normally 1024
	device = ''
	# import reassembler program
	#sys.path.append('/home/dcleckley/capture-test/PacketCapture')
	#import Reassembler
	try:
		opts, args = getopt.getopt(argv,"hi:p:c:d:")
	except getopt.GetoptError:
		print 'TcpServer.py -i <serverIP> -p <serverPort> -c <receive_count> -d <eth interface>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'TcpServer.py -i <serverIP> -p <serverPort> -c <receive_count> -d <eth interface>'
			sys.exit(2)
		elif opt == '-i':
			ServerIP = arg
		elif opt == '-p':
			ServerPort = int(arg)
		elif opt == '-c':
			count = int(arg)
		elif opt == '-d':
			device = arg
	if (ServerIP == '') or (ServerPort == '') or (device == ''):
		print 'required arguments missing, try again. see -h for help'
		sys.exit(2)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((ServerIP, ServerPort))
	s.listen(count)
	threads = []
	print ' setup on ', (ServerIP,ServerPort)

	while count:
		print "Server listening"
		conn, addr = s.accept()
		t = Thread(target=handler,args= (conn, addr))
		t.start()
		threads.append(t)
		count = count - 1
	
	for x in threads:
		print x
		x.join()
	s.close()
	#nidsThread.join(5)

if __name__ == "__main__":
	main(sys.argv[1:])	
