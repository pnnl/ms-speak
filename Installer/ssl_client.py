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

print("Connecting to CA SSL Store {} on {}".format(server_sni_hostname, host_addr))

try:
	sslCtx = ssl.create_default_context()
	sslCtx.load_default_certs(ssl.Purpose.SERVER_AUTH)

	cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	secSock = sslCtx.wrap_socket(cliSock, server_side=False, server_hostname=server_sni_hostname)
	# Original socket no longer needed
	cliSock.close();
	try:
		secSock.connect((host_addr, host_port))
	except:
		secSock = None
		raise Exception("Failed to Connect to Server.")
	print("CA Store SSL  established.\nPeer: {}".format(secSock.getpeercert()))
	print("\n")
	if( False ):
		# Print the cipher used
		cipher = secSock.cipher()
		print("Name of the cipher:%s"%cipher[0]);
		print("TLS/SSL version:%s"%cipher[1]);
		print("Number of secret bits:%s\n"%cipher[2]);

		time.sleep(1)
		# Print the shared ciphers
		shared = secSock.shared_ciphers();
		print("Shared ciphers: {}\n".format(shared))
		time.sleep(1)
		# Print compression
		compression = secSock.compression();
		print("Compression cipher: {}\n".format(compression))
	time.sleep(1)
	print("Sending: 'Hello From the Client Side'")
	secSock.send(b"Hello From the Client Side\n")
#
# shutdown is a flexible way to block communication in one or both directions.
# When the second parameter is SHUT_RDWR, it will block both sending and
# receiving (like close). However, close is the way to actually destroy a socket.
#
# With shutdown, you will still be able to receive pending data the peer 
# already sent
#
	#secSock.shutdown(socket.SHUT_WR) # SHUT_RDWR
	print("Waiting For Server Response...")
	time.sleep(1)
	data = b''
	while True:
		buf = secSock.recv(1024)
		if not buf:
			break
		data += buf
		data += b", "
		print('Received', repr(buf))
		secSock.sendall(b'done')
		buf = secSock.recv(1024)
		data += buf
		break
	print('Received', repr(data))
except Exception as ex :
   print('Exception : %s' % ex)
finally:
	print("\nClosing Secure connection")
	#secSock.unwrap()
	if secSock:
		secSock.shutdown(socket.SHUT_RDWR)
		secSock.close()
