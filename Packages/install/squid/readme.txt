the squid.conf file goes in /usr/local/squid/etc

I modified mss.config to be like this:
	[ x509_ext ]
		keyUsage               = Certificate Sign, CRL Sign, Digital Signature, Key Agreement
		basicConstraints       = critical, CA:TRUE

I also added
	DNS.8       = 192.168.1.3
	DNS.9       = 192.168.1.14
and (though i'm not sure these did anything useful):
	IP.3 = 192.168.1.1
	IP.4 = 192.168.1.2
	IP.5 = 192.168.1.3
	IP.6 = 192.168.1.4
	IP.7 = 192.168.1.14

# create squid ca cert:
	openssl req -new -newkey rsa:2048 -sha256 -days 365 -nodes -x509 -extensions v3_ca -keyout mspCA.pem -out mspCA.pem	
	sudo mkdir /usr/local/squid/ssl_cert
	sudo chown nobody:nogroup /usr/local/squid/ssl_cert
	sudo chmod 700 /usr/local/squid/ssl_cert
	sudo cp mspCA.pem /usr/local/squid/ssl_cert
	sudo chown nobody:nogroup /usr/local/squid/ssl_cert/mspCA.pem
		1182  cd Packages/squid-4.7/
		1184  ./configure --with-openssl --enable-ssl-crtd
		1186  sudo apt-get install libssl-dev
		1188  ./configure --with-openssl --enable-ssl-crtd
		1201  sudo /usr/local/squid/libexec/security_file_certgen -c -s /var/lib/ssl_db -M 4MB
		1202  sudo chown nobody:nogroup -R /var/lib/ssl_db
			*** might have to first run
			cd /home/carl/msspeak/msspeak/Packages/squid-4.7
			./configure --with-openssl --enable-ssl-crtd
					configure: error: library 'crypto' is required for OpenSSL
				need sudo apt-get install libssl-dev
			still no security_file_certgen even after configure
			try make:
				now security_file_certgen is in /usr/local/squid/libexec
			try this again:
				sudo /usr/local/squid/libexec/security_file_certgen -c -s /var/lib/ssl_db -M 4MB
					Initialization SSL db...
					Done
			try this again:
				sudo chown nobody:nogroup -R /var/lib/ssl_db
				OK

# create mss ca cert:
	openssl req -new -newkey rsa:2048 -sha256 -days 365 -nodes -x509 -keyout mss.key -out mss.crt -config mss.config

# update ca store:	
	sudo ls /usr/local/share/ca-certificates
	sudo rm /usr/local/share/ca-certificates/mssca.crt
	sudo cp mss.crt /usr/local/share/ca-certificates/mssca.crt
	
	# i think i only need do the following since i can't load the .der file into a browser....
	sudo cp /usr/local/squid/ssl_cert/mspCA.pem /usr/local/share/ca-certificates/mspCA.crt
	
	sudo ls -l /etc/ssl/certs/ms*
	sudo update-ca-certificates -f
	
# modify squid.conf
/usr/local/squid/etc/squid.conf
	added acl SSL_ports port  8443

	http_port 3128 ssl-bump \
	cert=/usr/local/squid/ssl_cert/mspCA.pem \
	generate-host-certificates=on dynamic_cert_mem_cache_size=4MB

	# For squid 4.x 
	sslcrtd_program /usr/local/squid/libexec/security_file_certgen -s /var/lib/ssl_db -M 4MB

	acl step1 at_step SslBump1

	ssl_bump peek step1
	ssl_bump bump all 
	
	
THEN I DID:
	curl -v --proxy http://192.168.1.3:3128 --url "https://127.0.0.1:8443" --data @ODEventNotification.xml -A "MultiSpeak Test/1.0" -H "Accept: application / soap + xml, application / dime, multipart / related, text/*" -H "Content-Type: text/xml;charset=utf-8" -H "SOAPAction: http://www.multispeak.org/Version_3.0/ODEventNotification" --referer "http://buster.test.com/"
ALSO TO -url "https://192.168.1.3:8443"
	

MS -> squid - icap bump - MS
	MS:   ssl to 192.168.1.3, proxy at 127.0.0.1
	MSS:  ssl listen on 192.168.1.3


	
