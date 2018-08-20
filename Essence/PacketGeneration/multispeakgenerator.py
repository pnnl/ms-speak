# Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
import time
import struct
import sys
import random
import socket
## Arguments:

if(len(sys.argv) < 7):
	print 'Usage: multispeakgenerator.py <interface> <#packets> <delay> <sourceIP> <destIP> <multispeakMessageID>'
	sys.exit(1)


source_ip = sys.argv[4] 
dest_ip = sys.argv[5]
multispeak_message_ID = sys.argv[6] # need to validate thise number / string / whatever

# pseudo header fields
source_address = socket.inet_aton( source_ip )
#print bin(struct.unpack('!I',source_address)[0])
dest_address = socket.inet_aton(dest_ip)
#print bin(struct.unpack('!I',dest_address)[0])

def ip_checksum(ip_header, size):
    cksum = 0
    pointer = 0
    #The main loop adds up each set of 2 bytes. They are first converted to strings and then concatenated
    #together, converted to integers, and then added to the sum.
    while size > 1:
        cksum += int((str("%02x" % (ip_header[pointer],)) + 
                      str("%02x" % (ip_header[pointer+1],))), 16)
        size -= 2
        pointer += 2
    if size: #This accounts for a situation where the header is odd
        cksum += ip_header[pointer]
    cksum = (cksum >> 16) + (cksum & 0xffff)
    cksum += (cksum >>16)
    return (~cksum) & 0xFFFF
	
# checksum functions needed for calculation checksum
def checksum(msg):
    s = 0
    # loop taking 2 characters at a time
    for i in range(0, len(msg), 2):
        w = (ord(msg[i]) << 8) + (ord(msg[i+1]) )
       # sys.exit()
        s = s + w   
    s = (s>>16) + (s & 0xffff);
    s = 0xFFFF - s
    return s


def genEther():
	# options for ether
	dest_mac = "6a:1e:f0:57:ea:98"
	src_mac = "ca:17:8f:f5:98:a6"
	type = 0x0800
	
	dest_mac = dest_mac.split(':')
	dest_mac = map(lambda x: int(x,16), dest_mac)
	dest = struct.pack("%dB" % len(dest_mac), *dest_mac)
	src_mac = src_mac.split(':')
	src_mac = map(lambda x: int(x,16), src_mac)
	src = struct.pack("%dB" % len(src_mac), *src_mac)
	return dest + src + struct.pack("!H",type)

def genIP(TCPLength,i):
	version = 4
	length = 5 #4 bit field, size of tcp header, 5 * 4 = 20 bytes
	field = length + (version << 4)
	tos = 0
	totlength = TCPLength+(length*4)
	global count
	
	ident = i
	
	#reserve = 1
	#dontfrag = 0
	#morefrag = 0
	#flags = morefrag + (dontfrag << 1) + (reserve << 2)
	flags = 64
	fragoff = 0
	ttl = 81
	proto = 6
	check = 0
	global source_address
	global dest_address
	out = struct.pack("!BBHHBBBBH4s4s",field,tos,totlength,ident,flags,fragoff,ttl,proto,check,source_address,dest_address)
	header = []
	for i in range(0, len(out)):
		header.append(ord(out[i]))
	check = ip_checksum(header, len(header))
	out = struct.pack("!BBHHBBBBH4s4s",field,tos,totlength,ident,flags,fragoff,ttl,proto,check,source_address,dest_address)
	return out
	#header = []
	#for i in range(0, len(out)):
	#	header.append(ord(out[i]))
	#print("Checksum is: %x" % (ip_checksum(header, len(header)),))

def genTCP(tcp_content):
	source = 48883  # source port
	dest = 80   # destination port
	seq = 750484050
	ack_seq = 2141153
	doff = 5    #4 bit field, size of tcp header, 5 * 4 = 20 bytes
	reserved = 0
	#tcp flags
	fin = 0
	syn = 0
	rst = 0
	psh = 1
	ack = 1
	urg = 0
	window = 120
	check = 0
	urg_ptr = 0
	offset_res = (doff << 4) + 0
	tcp_flags = fin + (syn << 1) + (rst << 2) + (psh <<3) + (ack << 4) + (urg << 5)
	# the ! in the pack format string means network order
	tcp_header = struct.pack('!HHLLBBHHH' , source, dest, seq, ack_seq, offset_res, tcp_flags,  window, check, urg_ptr)
	pseudo = genPsuedoHeader(len (tcp_header + tcp_content))
	pseudo =  pseudo + tcp_header + tcp_content;
	check = checksum(pseudo)
	tcp_header = struct.pack('!HHLLBBHHH' , source, dest, seq, ack_seq, offset_res, tcp_flags,  window, check, urg_ptr)
	return tcp_header
 
def genPsuedoHeader(tcp_len):
	reserved = 0
	protocol = socket.IPPROTO_TCP
	global source_address
	global dest_address
	tcp_content = genHTTP(multispeak_message_ID)
	tcp_length = tcp_len
	pseudo = struct.pack('!4s4sBBH' , source_address , dest_address , reserved , protocol , tcp_length);
	return pseudo
 
def genHTTP(multispeak_message_ID):
	multispeak = genMultiSpeak(multispeak_message_ID)
	# HTTP part of msg
	method = "POST"
	space = " "
	url = "/"
	space = " "
	version = "HTTP/1.1\r\n"
	# todo: need to change header to be compatible with v3. right now hardcoded for v5 messages
	headers = "Accept-Encoding: gzip,deflate\r\nContent-Type: text/xml;charset=UTF-8\r\nSOAPAction: \"http://www.multispeak.org/Version_5.0_Release/"+str(multispeak_message_ID)+"\"\r\n"
	conlen = "Content-Length: "+str(len(multispeak))+"\r\n"
	hostIP = "Host: " + socket.gethostbyname(socket.gethostname())
	hostPort =  ":80\r\n"
	conn = "Connection: Keep-Alive\r\n"
	uagent = "Apache-HttpClient/4.1.1 (java 1.5)\r\n\r\n"
	
	return method + space + url + space + version + headers + conlen + hostIP + hostPort + conn + uagent + multispeak

def genMultiSpeak(multispeak_message_ID):
	messages = {"GetCustomerByMeterNumberAndServiceType" : GetCustomerByMeterNumberAndServiceType,
			"InitiateDisconnectedStatus" : InitiateDisconnectedStatus,
			"GetAllStreetLights" : GetAllStreetLights,
			"LongTestMessage" : LongTestMessage,
			"SetDisconnectedStatus" : SetDisconnectedStatus
			}
	if(multispeak_message_ID in messages):
		x =  messages[multispeak_message_ID]()	#execute the corresponding function to generate the correct multispeak message
	else:
		print 'multispeak_message_id ' + multispeak_message_ID + ' not found in message dictionary!'
		sys.exit(2)
	return x

def LongTestMessage():
	x = 'a' * 1100
	return x

def InitiateDisconnectedStatus():
	x = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ver="http://www.multispeak.org/Version_3.0">'
	x += '   <soapenv:Header>'
	x += '      <ver:MultiSpeakMsgHeader Version="3.0" UserID="GreenSuite" Pwd="TechAdv2013" AppName="GreenSuite Applications" AppVersion="1.0" Company="GreenSuite" BuildString="'+str(random.randrange(0,100))+'"/>'
	x += '   </soapenv:Header>'
	x += '   <soapenv:Body>'
	x += '      <ver:InitiateDisconnectedStatus>'
	x += '         <ver:meterNos>'
	x += '            <ver:string>'+str(random.randrange(0, 1000))+'</ver:string>'
	x += '            <ver:string>AB12345</ver:string>'
	x += '            <ver:string>CD00000</ver:string>'
	x += '         </ver:meterNos>'
	x += '      </ver:InitiateDisconnectedStatus>'
	x += '   </soapenv:Body>'
	x += '</soapenv:Envelope>'

	return x
#version 5 message
def SetDisconnectedStatus():
	x = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:req="http://www.multispeak.org/V5.0/ws/request" xmlns:com="http://www.multispeak.org/V5.0/commonTypes" xmlns:mr="http://www.multispeak.org/V5.0/wsdl/MR_Server" xmlns:com1="http://www.multispeak.org/V5.0/commonArrays">'
	x += '   <soapenv:Header>'
	x += '      <req:MultiSpeakRequestMsgHeader DefaultRegisteredName="Milsoft" TimeStamp="20140203" MessageCreatedTimeStamp="20140304" Context="abc">'
	x += '         <req:MultiSpeakVersion>'
	x += '            <com:MajorVersion>5</com:MajorVersion>'
	x += '         </req:MultiSpeakVersion>'
	x += '      </req:MultiSpeakRequestMsgHeader>'
	x += '   </soapenv:Header>'
	x += '   <soapenv:Body>'
	x += '      <mr:SetDisconnectedStatus>'
	x += '         <mr:ArrayOfMeterID>'
	x += '            <com1:meterID meterName="1234123" serviceType="q" otherServiceType="?" objectGUID="3452345" communicationAddress="25" communicationsPort="1" utility="REC" registeredName="name" systemName="name">'+str(random.randrange(0, 1000))+'</com1:meterID>'
	x += '         </mr:ArrayOfMeterID>'
	x += '         <mr:transactionID>av2345</mr:transactionID>'
	x += '      </mr:SetDisconnectedStatus>'
	x += '   </soapenv:Body>'
	x += '</soapenv:Envelope>'
	return x
def GetAllStreetLights():
	x  = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:req="http://www.multispeak.org/V5.0/ws/request" xmlns:com="http://www.multispeak.org/V5.0/commonTypes" xmlns:am="http://www.multispeak.org/V5.0/wsdl/AM_Server">'
	x += '   <soapenv:Header>'
	x += '      <req:MultiSpeakRequestMsgHeader DefaultRegisteredName="Milsoft" DefaultSystemName="Milsoft" DefaultUtility="RCE" DefaultCurrencyCode="USD" RegistrationID="24" MessageID="35" TimeStamp="20140203" MessageCreatedTimeStamp="20140304" Context="ABC">'
	x += '         <req:MultiSpeakVersion>'
	x += '            <com:MajorVersion>2</com:MajorVersion>'
	x += '            <com:MinorVersion>3</com:MinorVersion>'
	x += '            <com:Build>24</com:Build>'
	x += '            <com:BuildString>AC</com:BuildString>'
	x += '         </req:MultiSpeakVersion>'
	x += '         <req:Caller>'
	x += '            <com:AppName>MilsoftApp</com:AppName>'
	x += '            <com:Company>Milsoft</com:Company>'
	x += '            <com:SystemID>ABQ10</com:SystemID>'
	x += '         </req:Caller>'
	x += '      </req:MultiSpeakRequestMsgHeader>'
	x += '   </soapenv:Header>'
	x += '   <soapenv:Body>'
	x += '      <am:GetAllStreetLights>'
	x += '         <am:lastReceived>'+str(random.randrange(0,10000))+'</am:lastReceived>'
	x += '      </am:GetAllStreetLights>'
	x += '   </soapenv:Body>'
	x += '</soapenv:Envelope>'
	
	return x

def GetCustomerByMeterNumberAndServiceType():
	x = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ver="http://www.multispeak.org/Version_3.0">'
	x += '   <soapenv:Header>'
	x += '      <ver:MultiSpeakMsgHeader Version="'+str(random.randrange(0, 1000))+'" UserID="'+str(random.randrange(0, 1000))+'" Pwd="?" AppName="?" AppVersion="'+str(random.randrange(0, 1000))+'" Company="?" CSUnits="feet" CoordinateSystem="?" Datum="?" SessionID="?" PreviousSessionID="?" ObjectsRemaining="?" LastSent="?" RegistrationID="'+str(random.randrange(0, 1000))+'" AuditID="'+str(random.randrange(0, 1000))+'" MessageID="'+str(random.randrange(0, 1000))+'" TimeStamp="?" BuildString="?"/>'
	x += '   </soapenv:Header>'
	x += '   <soapenv:Body>'
	x += '      <ver:GetCustomerByMeterNumberAndServiceType>'
	x += '         <ver:meterNo>'+str(random.randrange(0, 1000))+'</ver:meterNo>'
	x += '         <ver:serviceType>'+str(random.randrange(0, 1000))+'</ver:serviceType>'
	x += '      </ver:GetCustomerByMeterNumberAndServiceType>'
	x += '   </soapenv:Body>'
	x += '</soapenv:Envelope>'
	
	return x


def genpacket(i):
	HTTP = genHTTP(multispeak_message_ID)
	# check to see if we need padding to calculate checksum
	 # add count for fun.
	if len(HTTP)%2 == 1:
		HTTP += " "
	TCP = genTCP(HTTP)
	IP = genIP(len(TCP+HTTP),i)
	ETHER = genEther()
#	global TCP,ETHER
	return ETHER+IP+TCP+HTTP



#buff = genEther()+genIP()+genTCP()+genPsuedoHeader(genTCP())[1]
# Use a raw socket - requires root privs
s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW,socket.getprotobyname('ip')) 
# Bind to interface rather then address
s.bind((sys.argv[1], 2048))
# get time that we start
start = time.time()

for i in range(0,int(sys.argv[2])):
	global count
	count = i
	buff= genpacket(i)
	s.send(buff)
	print "sent packet " + str(i)
	sys.stdout.flush()
	time.sleep(float(sys.argv[3]))
print (len(buff))
# We could receive data back by using data = s.receive(1024)
# Get time that we end
stop = time.time()
# Subtract the two to see how long we took
runtime=stop-start
print str(runtime) + " seconds"
