# Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
# Sends long multispeak message payloads with real TCP headers using layer 3 sockets (rather than layer 2)
import socket
import sys, getopt
import random
import select
import time

import re

def genHTTP(multispeak_message_ID):
	multispeak = genMultiSpeak(multispeak_message_ID)
	# HTTP part of msg
	method = "POST"
	space = " "
	url = "/Optimum_Test_Service/Multispeak/30/" + str(multispeak_message_ID).split('/')[-2] + "_Server"
	space = " "
	version = "HTTP/1.1\r\n"
	# todo: need to change header to be compatible with v3. right now hardcoded for v5 messages
	headers = "Accept-Encoding: gzip,deflate\r\nContent-Type: text/xml;charset=UTF-8\r\nSOAPAction: \"http://www.multispeak.org/Version_3.0/"+str(multispeak_message_ID).split('/')[-1]+"\"\r\n" #remove filepath if messagename is a whole file instead of hardcoded
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
			"SetDisconnectedStatus" : SetDisconnectedStatus,
			"MRInterval" : GetMeterReadingsByDateIntervalDataResponse
			}
	if(multispeak_message_ID in messages):
		x =  messages[multispeak_message_ID]()	#execute the corresponding function to generate the correct multispeak message
	if('.xml' in multispeak_message_ID):
		# try to open it as file and use that as the message
		x =  open(multispeak_message_ID,'r').read()
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
#long v3 message from ping
#removed

#from ping v5
def GetMeterReadingsByDateIntervalDataResponse():
	x = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:res="http://www.multispeak.org/V5.0/ws/response" xmlns:com="http://www.multispeak.org/V5.0/commonTypes" xmlns:v5="http://www.multispeak.org/V5.0" xmlns:mr="http://www.multispeak.org/V5.0/wsdl/MR_Server" xmlns:com1="http://www.multispeak.org/V5.0/commonArrays">
   <soapenv:Header>
      <res:MultiSpeakResponseMsgHeader DefaultRegisteredName="?" DefaultSystemName="?" DefaultUtility="?" DefaultCurrencyCode="?" MessageID="?" TimeStamp="?" MessageCreatedTimeStamp="?" Context="?">
         <res:MultiSpeakVersion>
            <com:MajorVersion>?</com:MajorVersion>
            <com:MinorVersion>?</com:MinorVersion>
            <com:Build>?</com:Build>
            <!--Optional:-->
            <com:Branch>?</com:Branch>
            <com:BuildString>?</com:BuildString>
         </res:MultiSpeakVersion>
         <res:Caller>
            <com:AppName>?</com:AppName>
            <!--Optional:-->
            <com:AppVersion>?</com:AppVersion>
            <com:Company>?</com:Company>
            <!--Optional:-->
            <com:AuditID>?</com:AuditID>
            <!--Optional:-->
            <com:AuditPassword>?</com:AuditPassword>
            <com:SystemID>?</com:SystemID>
            <!--Optional:-->
            <com:Password>?</com:Password>
         </res:Caller>
         <!--Optional:-->
         <res:CodedNames>
            <!--1 or more repetitions:-->
            <com:codedName nameType="?">
               <com:codedValue>?</com:codedValue>
               <com:namePart>?</com:namePart>
               <!--Optional:-->
               <com:description>?</com:description>
            </com:codedName>
         </res:CodedNames>
         <!--Optional:-->
         <res:CoordinateSystemInformation>
            <com:CSUnits otherKind="?">?</com:CSUnits>
            <com:CSAuthorities>
               <!--1 or more repetitions:-->
               <com:CSAuthority>
                  <com:CSAuthorityName otherKind="?">?</com:CSAuthorityName>
                  <com:CoordinateSystemAuthorityCode>?</com:CoordinateSystemAuthorityCode>
                  <com:Datum>?</com:Datum>
               </com:CSAuthority>
            </com:CSAuthorities>
         </res:CoordinateSystemInformation>
         <res:Result>
            <v5:resultIdentifier>
               <com:replyCodeCategory otherKind="?">?</com:replyCodeCategory>
               <com:index>?</com:index>
            </v5:resultIdentifier>
            <!--Optional:-->
            <v5:resultDescription>?</v5:resultDescription>
            <!--Optional:-->
            <v5:level otherKind="?">?</v5:level>
            <!--Optional:-->
            <v5:errorObjects>
               <!--1 or more repetitions:-->
               <com:errorObject referenceID="?" nounType="?">
                  <!--Optional:-->
                  <com:extensions>
                     <!--You may enter ANY elements at this point-->
                  </com:extensions>
                  <!--Optional:-->
                  <com:extensionsList>
                     <!--1 or more repetitions:-->
                     <com:extensionsItem>
                        <com:extName>?</com:extName>
                        <com:extValue units="?">?</com:extValue>
                        <!--Optional:-->
                        <com:extType>?</com:extType>
                     </com:extensionsItem>
                  </com:extensionsList>
                  <!--Optional:-->
                  <com:errorCode>
                     <com:replyCodeCategory otherKind="?">?</com:replyCodeCategory>
                     <com:index>?</com:index>
                  </com:errorCode>
                  <com:eventTime>?</com:eventTime>
                  <!--Optional:-->
                  <com:displayString>?</com:displayString>
                  <!--Optional:-->
                  <com:detailedString>?</com:detailedString>
               </com:errorObject>
            </v5:errorObjects>
            <!--Optional:-->
            <v5:lastSent>?</v5:lastSent>
            <!--Optional:-->
            <v5:objectsRemaining>?</v5:objectsRemaining>
         </res:Result>
      </res:MultiSpeakResponseMsgHeader>
   </soapenv:Header>
   <soapenv:Body>
      <mr:GetMeterReadingsByDateIntervalDataResponse>
         <!--Optional:-->
         <mr:ArrayOfIntervalData>
            <!--Zero or more repetitions:-->
            <com1:intervalData>
               <v5:statusDelimiter>?</v5:statusDelimiter>
               <v5:intervalDelimiter>?</v5:intervalDelimiter>
               <!--Optional:-->
               <v5:comment>?</v5:comment>
               <!--Optional:-->
               <v5:profiles>
                  <!--Zero or more repetitions:-->
                  <v5:profile profileID="?">
                     <!--Optional:-->
                     <v5:name>?</v5:name>
                     <!--Optional:-->
                     <v5:intervalLength units="?">?</v5:intervalLength>
                     <!--Optional:-->
                     <v5:channels>
                        <!--1 or more repetitions:-->
                        <v5:channel>
                           <!--Optional:-->
                           <com:extensions>
                              <!--You may enter ANY elements at this point-->
                           </com:extensions>
                           <!--Optional:-->
                           <com:extensionsList>
                              <!--1 or more repetitions:-->
                              <com:extensionsItem>
                                 <com:extName>?</com:extName>
                                 <com:extValue units="?">?</com:extValue>
                                 <!--Optional:-->
                                 <com:extType>?</com:extType>
                              </com:extensionsItem>
                           </com:extensionsList>
                           <!--Optional:-->
                           <v5:index>?</v5:index>
                           <!--Optional:-->
                           <v5:fieldName>?</v5:fieldName>
                           <!--Optional:-->
                           <v5:fieldDescription>?</v5:fieldDescription>
                           <!--Optional:-->
                           <v5:units otherKind="?">?</v5:units>
                        </v5:channel>
                     </v5:channels>
                  </v5:profile>
               </v5:profiles>
               <!--Optional:-->
               <v5:blocks>
                  <!--Zero or more repetitions:-->
                  <v5:block>
                     <!--Optional:-->
                     <v5:profileID>?</v5:profileID>
                     <!--Optional:-->
                     <v5:meterID meterName="?" serviceType="?" otherServiceType="?" objectGUID="?" communicationAddress="?" communicationsPort="?" utility="?" registeredName="?" systemName="?">?</v5:meterID>
                     <!--Optional:-->
                     <v5:endReadings>
                        <!--1 or more repetitions:-->
                        <v5:endReading>
                           <!--Optional:-->
                           <v5:channelIndex>?</v5:channelIndex>
                           <!--Optional:-->
                           <v5:reading>1001</v5:reading>
                           <!--Optional:-->
                           <v5:readingDate>?</v5:readingDate>
                        </v5:endReading>
                     </v5:endReadings>
                     <!--Optional:-->
                     <v5:logTime>?</v5:logTime>
                     <!--Optional:-->
                     <v5:intervalStart>?</v5:intervalStart>
                     <v5:dB>
                        <v5:chs>
                           <!--1 or more repetitions:-->
                           <v5:ch>
                              <v5:idx>9</v5:idx>
                              <v5:d>?</v5:d>
                           </v5:ch>
                        </v5:chs>
                        <!--Optional:-->
                        <v5:cS>?</v5:cS>
                     </v5:dB>
                  </v5:block>
               </v5:blocks>
            </com1:intervalData>
         </mr:ArrayOfIntervalData>
      </mr:GetMeterReadingsByDateIntervalDataResponse>
   </soapenv:Body>
</soapenv:Envelope>'''

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


def main(argv):
	serverIP = ''
	serverPort = ''
	messageName = ''
	count = 1
	BUFFER_SIZE = 1024
		
	try:
		opts, args = getopt.getopt(argv,"hi:p:c:m:")
	except getopt.GetoptError:
		print 'TcpClient.py -i <ServerIP> -p <ServerPort> -c <tcp conn count> -m <message name>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'TcpClient.py -i <serverIP> -p <serverport> -c <tcp connection count> -m <message name>'
			sys.exit(2)
		elif opt == '-i':
			serverIP = arg
		elif opt == '-p':
			serverPort = int(arg)	
		elif opt == '-c':
			count = int(arg)
		elif opt == '-m':
			messageName = arg
	if (serverIP == '') or (serverPort == '') or (messageName == ''):
		print "Server IP or port or message not specified, exiting... "
		sys.exit(2)
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	
	message = genHTTP(messageName)
	
	#for y in range (0,count):	# tcp connection 'count' times
	s.connect((serverIP,serverPort))
	#try:
	s.sendall(message + "\n")

	#except Exception as exc:
	#	print exc
	#	print "client error sending message"
	print ("Response data: ")
	envelopeRegex = '</.+:[Ee]nvelope'
	while True:
		data = s.recv(BUFFER_SIZE)
		print(data)
		if (re.search(envelopeRegex,data)):
			s.close()
			sys.exit(1)

if __name__ == "__main__":
	main(sys.argv[1:])


