the squid.conf file goes in /usr/local/squid/etc

it allows port 8080:
	acl Safe_ports port 8080	# http
	
and enables IPv4 addresses:
	http_port 0.0.0.0:3128