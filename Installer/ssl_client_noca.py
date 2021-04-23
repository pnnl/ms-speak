#!/usr/bin/python3

import socket
import ssl,time

# https://127.0.0.1:8443
# https://130.20.113.7:8443
# https://multispeaker.server.org:8443
host_addr = '130.20.113.7' # '130.20.209.42'
host_addr = '127.0.0.1'
host_port = 8443
server_sni_hostname = 'multispeaker.server.org'
server_cert = 'mss.crt'

print("Connecting to {} via {}, using {}".format(server_sni_hostname, host_addr, server_cert))

try:
	sslCtx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=server_cert)
	#sslCtx = ssl.create_default_context()
	#sslCtx.load_default_certs(ssl.Purpose.SERVER_AUTH)

	cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	secSock = sslCtx.wrap_socket(cliSock, server_side=False, server_hostname=server_sni_hostname)
	# Original socket no longer needed
	cliSock.close();
	try:
		secSock.connect((host_addr, host_port))
	except:
		secSock = None
		raise Exception("Failed to Connect to Server.")
	print("SSL Session Established.\nPeer: {}".format(secSock.getpeercert()))
	print("\n")
	if( True ):
		# Print the cipher used
		cipher = secSock.cipher()
		print("Name of the cipher:%s"%cipher[0]);
		print("TLS/SSL version:%s"%cipher[1]);
		print("Number of secret bits:%s\n"%cipher[2]);
		# Print the shared ciphers
		shared = secSock.shared_ciphers();
		print("Shared ciphers: {}\n".format(shared))
		# Print compression
		compression = secSock.compression();
		print("Compression cipher: {}\n".format(compression))
	time.sleep(1)
	sendStr = b'Hello From the Client Side'
	print("Sending: '{}'".format(sendStr.decode('utf-8')))
	secSock.send(sendStr)
#
# shutdown is a flexible way to block communication in one or both directions.
# When the second parameter is SHUT_RDWR, it will block both sending and
# receiving (like close). However, close is the way to actually destroy a socket.
#
# With shutdown, you will still be able to receive pending data the peer 
# already sent
#
	print("Waiting For Server Response...")
	time.sleep(1)
	data = b''
	while True:
		buf = secSock.recv(1024)
		if not buf:
			break
		data += buf
		break
	print("Received: '{}'".format(data.decode('utf-8')))
except Exception as ex :
   print('Exception : %s' % ex)
finally:
	print("\nClosing Secure connection")
	#secSock.unwrap()
	if secSock:
		secSock.shutdown(socket.SHUT_RDWR)
		secSock.close()
