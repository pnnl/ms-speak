#!/usr/bin/python3

import socket
from socket import AF_INET, SOCK_STREAM, SO_REUSEADDR, SOL_SOCKET, SHUT_RDWR
import ssl, time

# build with:
#  openssl req -config mss.config -new -x509 -sha256 -newkey rsa:2048 -nodes -keyout mss.key -days 365 -out mss.crt

# openssl x509 -text -in mss.crt > mss.crt.info

listen_addr = '0.0.0.0'
listen_port = 8443
server_cert = 'mss.crt'
server_key = 'mss.key'

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=server_cert, keyfile=server_key)

bindsocket = socket.socket()
bindsocket.bind((listen_addr, listen_port))
bindsocket.listen(5)

#while True:
print("\nListening on {} for CA Store SSL Client secSockection...\n".format(listen_addr))
cliSock, fromaddr = bindsocket.accept()
print("Client secSockected from {} on:{}".format(fromaddr[0], fromaddr[1]))
secSock = None
try:
	secSock = context.wrap_socket(cliSock, server_side=True)
	# Original socket no longer needed
	cliSock.close()
	print("CA Store SSL established.\nPeer: {}".format(secSock.getpeercert()))
	if( False ):
		used = secSock.cipher()
		print("Used cipher: {}\n".format(used))
		time.sleep(1)
		# Print the shared ciphers
		shared = secSock.shared_ciphers()
		print("Shared ciphers: {}\n".format(shared))
		time.sleep(1)
		# Print compression
		compression = secSock.compression()
		print("Compression cipher: {}\n".format(compression))

	buf = b''  # Buffer to hold received client data
	print("\nWaiting {}".format('for data'))
	while True:
		data = secSock.recv(1024)
		if data:
			# Client sent us data. Append to buffer
			print("got: {}".format(data))
			buf += data
			buf += b", "
			secSock.sendall(b'ok')
		else:
			# No more data from client. Show buffer and close secSockection.
			print("Received:{}".format(buf))
			#secSock.shutdown(socket.SHUT_RD)
			break
except Exception as ex :
   print('Exception : %s' % ex)
finally:
	if( secSock ):
		secSock.sendall(b'Done With You')
		print("\nClosing Secure connection")
		secSock.shutdown(socket.SHUT_RDWR) # SHUT_RDWR
		secSock.close()