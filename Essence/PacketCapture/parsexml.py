# Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc

import random
from lxml import etree as ET

#sample XML Payload

#x =  '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ver="http://www.multispeak.org/Version_3.0">'
#x += '   <soapenv:Header>'
#x += '      <ver:MultiSpeakMsgHeader Version="'+str(random.randrange(0, 1000))+'" UserID="'+str(random.randrange(0, 1000))+'" Pwd="?" AppName="?" AppVersion="'+str(random.randrange(0, 1000))+'" Company="?" CSUnits="feet" CoordinateSystem="?" Datum="?" SessionID="?" PreviousSessionID="?" ObjectsRemaining="?" LastSent="?" RegistrationID="'+str(random.randrange(0, 1000))+'" AuditID="'+str(random.randrange(0, 1000))+'" MessageID="'+str(random.randrange(0, 1000))+'" TimeStamp="?" BuildString="?"/>'
#x += '   </soapenv:Header>'
#x += '   <soapenv:Body>'
#x += '      <ver:GetCustomerByMeterNumberAndServiceType>'
#x += '         <ver:meterNo>23151</ver:meterNo>'
#x += '         <ver:serviceType>Meter</ver:serviceType>'
#x += '      </ver:GetCustomerByMeterNumberAndServiceType>'
#x += '   </soapenv:Body>'
#x += '</soapenv:Envelope>'
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
root = ET.fromstring(x[0:])
ns = {'a':'http://schemas.xmlsoap.org/soap/envelope/'}
print ns
list = []
list =  root.xpath('//a:Body',namespaces=ns)
print list
children = list[0].getchildren()
print children[0].tag
#for child in root:
#	print child.tag, child.text 
#	for x in child.getchildren():
#		print x.tag,x.text
#print(ET.tostring(root, pretty_print=True))
