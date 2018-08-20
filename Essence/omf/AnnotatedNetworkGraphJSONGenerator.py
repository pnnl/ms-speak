#!/usr/bin/python
# Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from json import *
from sets import *
import time
import datetime
import pickle
import json
import sys
import urllib2
import mysql.connector
import dbconfig as cfg

class SavedNode:
    def __init__(self, ipAddress, color, displayWithMultiSpeak):
        self.ipAddress = ipAddress
        self.color = color
        self.displayWithMultiSpeak = displayWithMultiSpeak

class ANGNode(dict):
    index = 0
    def __init__(self, name, color, displayWithMultiSpeak):
        self.__dict__ = self
        self.index = ANGNode.index
        ANGNode.index += 1
        self.name = name  
        self.tcpServerPorts = set()
        self.protocols = set()
        self.ipAddress = name
        self.tcpConnectionCount = 0
        self.udpConnectionCount = 0
        self.udpPorts = set()
        self.displayWithMultiSpeak = displayWithMultiSpeak

        #src nodes are yellow
        #dst nodes are blue
        #nodes that are both src and dst nodes are purple
        #nodes for protocols we track are are green (protocol entry must be in the database)
        #violations are red
        self.color = color
        
        # Nodes have default radius of 4. Alert nodes have radius of 8
        self.radius = 4
    def addTcpServerPort(self, port):
        self.tcpServerPorts.add(port)
    def addUdpPort(self, port):
        self.udpPorts.add(port)
    def addProtocol(self, protocol):
        self.protocols.add(protocol)
    def incrementTcpConnectionCount(self):
        self.tcpConnectionCount += 1
    def incrementUdpConnectionCount(self):
        self.udpConnectionCount += 1
    def jsonify(self):
        jsonDict = dict(self.__dict__)
        jsonDict.pop("tcpServerPorts")
        jsonDict.pop("protocols")
        jsonDict.pop("tcpConnectionCount")
        jsonDict.pop("udpConnectionCount")
        jsonDict.pop("udpPorts")
        return jsonDict
    def __eq__(self, other):
        return self.name == other.name
    def __hash__(self):
        return hash(self.name)

class ANGLink(dict):
    def __init__(self, source, target, displayWithMultiSpeak):
        self.__dict__ = self
        self.source = source
        self.target = target
        self.displayWithMultiSpeak = displayWithMultiSpeak
        #self.bothNodesMultiSpeak
        self.id = source + "to" + target
    def __eq__(self, other):
        return self.source == other.source and self.target == other.target
    def __hash__(self):
        return hash(self.source + self.target)

class ANGNodeEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ANGNode):
            return obj.__dict__

class ANGCompleteGraph:
    def __init__(self):
        self.links = set()
        self.nodes = dict()
        savedNodes = getNodesFromDatabase()
        savedLinks = getLinksFromDatabase()
        for sn in savedNodes:
            self.addNode(sn.ipAddress, sn.color, sn.displayWithMultiSpeak)
        for sl in savedLinks:
            self.links.add(ANGLink(sl[0], sl[1], sl[2]))

    def saveGraph(self):
        saveNodesToDatabase(self.nodes)
        saveLinksToDatabase(self.links)

    def addNode(self, name, color, displayWithMultiSpeak):
        if name in self.nodes:
            return self.nodes[name]
        newNode = ANGNode(name, color, displayWithMultiSpeak)
        self.nodes[name] = newNode
        return newNode

    def getNode(self, name):
        if name in self.nodes:
            return self.nodes[name]
        return None

    def addLink(self, srcName, srcPort, dstName, dstPort, displayWithMultiSpeak):
        if srcName not in self.nodes or dstName not in self.nodes:
            raise Exception("The src " + srcName + " or destination " + dstName + " did not exist in the graph")

        #if self.nodes[srcName] is already a destination, then we have to make it purple
        srcNode = self.nodes[srcName]
        if srcNode.color != "green" and srcNode.color != "red" and srcNode.color == "orange":
            srcNode.color = "purple"

        #if self.nodes[dstName] is already a source, then we have to make it purple
        dstNode = self.nodes[dstName]
        if dstNode.color != "green" and dstNode.color != "red" and dstNode.color == "blue":
            dstNode.color = "purple"

        newLink = ANGLink(self.nodes[srcName].name, self.nodes[dstName].name, displayWithMultiSpeak)
        if newLink not in self.links:
            self.links.add(newLink)

class ANGJSON(dict):
    def __init__(self, ang, alerts):
        self.__dict__ = self
        #self.nodes = [None] * len(ang.nodes)
        self.nodes = dict()
        for key in ang.nodes:
            self.nodes[ang.nodes[key].name] = ang.nodes[key].jsonify()
            self.nodes[ang.nodes[key].name]["IP address"] = ang.nodes[key].name
            
            strTcpPortList = ""
            for port in ang.nodes[key].tcpServerPorts:
                if (strTcpPortList != ""):
                    strTcpPortList += " "
                strTcpPortList += str(port)
                
            if (strTcpPortList != ""):
                self.nodes[ang.nodes[key].name]["Open TCP ports"] = strTcpPortList

            strUdpPortList = ""
            for port in ang.nodes[key].udpPorts:
                if (strUdpPortList != ""):
                    strUdpPortList += " "
                strUdpPortList += str(port)

            if (strUdpPortList != ""):
                self.nodes[ang.nodes[key].name]["Open UDP ports"] = strUdpPortList

            strProtocolList = ""
            for protocol in ang.nodes[key].protocols:
                if (strProtocolList != ""):
                    strProtocolList += " "
                strProtocolList += protocol

            if strProtocolList != "":
                self.nodes[ang.nodes[key].name]["Protocols Analyzed"] = strProtocolList

            if ang.nodes[key].tcpConnectionCount > 0:
                self.nodes[ang.nodes[key].name]["TCP connections made"] = ang.nodes[key].tcpConnectionCount
            if ang.nodes[key].udpConnectionCount > 0:
                self.nodes[ang.nodes[key].name]["UDP connections made"] = ang.nodes[key].udpConnectionCount

            annotations = getAnnotationsFromDatabase(ang.nodes[key].name)
            if annotations != None:
                for akey in annotations:
                    self.nodes[ang.nodes[key].name][akey] = annotations[akey]

            if "hostname" not in self.nodes[ang.nodes[key].name]:
                self.nodes[ang.nodes[key].name]["hostname"] = ang.nodes[key].name

        self.links = list(ang.links)
        self.alerts = alerts

class AlertJSON(dict):
    def __init__(self, alerts):
        self.__dict__ = self
        self.alerts = alerts
        
class ANGCompleteGraphEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ANGCompleteGraph):
            ret = list(obj.nodes)
            print ret
            
def getGraph():
    completeGraph = ANGCompleteGraph()
    
    alertDict = dict()

    # capture the alert data
    # do this first so that nodes with alerts can be flagged to be displayed
    # with multispeak nodes, in case node isn't already flagged as multispeak
    try:
        response = urllib2.urlopen(cfg.serviceUrl + '/alertcount')
        html = response.read()
        alerts = json.loads(html)
        for alert in alerts:
            if 'ipAddress' in alert:
                alertDict[alert['ipAddress']] = list()
                
    except Exception as e:
        print "Unable to obtain alerts", e

    auth_provider = PlainTextAuthProvider(username=cfg.cassandraConfig["user"], password=cfg.cassandraConfig["password"])
    cluster = Cluster([cfg.cassandraConfig["host"]], auth_provider=auth_provider)
    session = cluster.connect(cfg.cassandraConfig["db"])

    #first we find all of the multispeak nodes since thats a relatively easy task
    multispeakNodes = set()
    testNodes = set()
    lastTimestamp = getTimestampFromDatabase()
    nowMinusOneDay = datetime.datetime.now() - datetime.timedelta(1)
    if lastTimestamp is None or lastTimestamp < nowMinusOneDay:
        lastTimestamp = nowMinusOneDay;
    
    for currentRow in session.execute('select source_addr, dest_addr from packet where time_stamp > %s allow filtering', (lastTimestamp,)):
        multispeakNodes.add(currentRow[0])
        multispeakNodes.add(currentRow[1])

    lastRawPacketTimestamp = datetime.datetime(1, 1, 1)
    for currentRow in session.execute('select source_addr, source_port, destination_addr, destination_port, protocol, time_stamp from generic_packet where time_stamp > %s allow filtering', (lastTimestamp,)):
        srcName = currentRow[0]
        srcPort = currentRow[1]
        dstName = currentRow[2]
        dstPort = currentRow[3]
        protocol = currentRow[4]
        time_stamp = currentRow[5]
        if time_stamp > lastRawPacketTimestamp:
            lastRawPacketTimestamp = time_stamp;

        isMultiSpeakLink = False # true if at least one node is multispeak
        
        srcNode = completeGraph.addNode(srcName, "blue", False)
        dstNode = completeGraph.addNode(dstName, "orange", False)

        if srcName in multispeakNodes:
            isMultiSpeakLink = True
            if srcNode.color != "red":
                srcNode.color = "green"
            srcNode.addProtocol("Multispeak")
            # If only displaying multispeak, this node and any connected nodes should be displayed
            srcNode.displayWithMultiSpeak = True
            dstNode.displayWithMultiSpeak = True
        if dstName in multispeakNodes:
            isMultiSpeakLink = True
            if dstNode.color != "red":
                dstNode.color = "green"
            dstNode.addProtocol("Multispeak")
            # If only displaying multispeak, this node and any connected nodes should be displayed
            srcNode.displayWithMultiSpeak = True
            dstNode.displayWithMultiSpeak = True
        if srcName in alertDict:
        
            srcNode.color = "red"
            srcNode.radius = 8
            # If only displaying multispeak, display this node if it has alerts even if it isn't multispeak
            isMultiSpeakLink = True
            srcNode.displayWithMultiSpeak = True
            dstNode.displayWithMultiSpeak = True
        if dstName in alertDict and dstNode.color != "red":
            dstNode.color = "red"
            dstNode.radius = 8
            # If only displaying multispeak, display this node if it has alerts even if it isn't multispeak
            isMultiSpeakLink = True
            srcNode.displayWithMultiSpeak = True
            dstNode.displayWithMultiSpeak = True
        
        completeGraph.addLink(srcName, srcPort, dstName, dstPort, isMultiSpeakLink)

        if (protocol == "tcp"):
            dstNode.addTcpServerPort(dstPort)
            srcNode.incrementTcpConnectionCount()
            dstNode.incrementTcpConnectionCount()
        else:
            srcNode.addUdpPort(srcPort)
            srcNode.incrementUdpConnectionCount()
            dstNode.addUdpPort(dstPort)
            dstNode.incrementUdpConnectionCount()

    cluster.shutdown()
    completeGraph.saveGraph()

    if lastRawPacketTimestamp.year >= 1900:
        saveTimestampToDatabase(lastRawPacketTimestamp.strftime('%Y-%m-%d %H:%M:%S.%f'))
    return dumps(ANGJSON(completeGraph, alertDict), sort_keys=True, indent=2)

def getEndpointTypes(version):
    if version != "3" and version != "5":
        version = "3"

    url = cfg.serviceUrl + "/endpointconfigurationtype/" + version;
    return getJSONFromEssenceServices(url)
    
def getAlerts(ip):
    response = urllib2.urlopen(cfg.serviceUrl + '/alert/ip/' + ip)
    html = response.read()
    allAlertInfo = json.loads(html)
    alerts = list()
    for alertInfo in allAlertInfo:
        alerts.append(alertInfo)
        
    return dumps(AlertJSON(alerts), sort_keys=True, indent=2)

def getDetectionRuleTypes():
    url = cfg.serviceUrl + "/detectionruletype"
    return getJSONFromEssenceServices(url)

def getDetectionRulesForNode(ip):
    url = cfg.serviceUrl + "/detectionrule/ip/" + ip;
    return getJSONFromEssenceServices(url)

def getJSONFromEssenceServices(url):
    try:
        response = urllib2.urlopen(url)
        return dumps(json.loads(response.read()))
    except Exception as e:
        print "Unable to get JSON from essence services at ", url, e 
        
def getMysqlConnection():
    cnx = mysql.connector.connect(user=cfg.mysqlConfig["user"], password=cfg.mysqlConfig["password"], database=cfg.mysqlConfig["db"])
    return cnx

def getTimestampFromDatabase():
    cnx = getMysqlConnection()
    cursor = cnx.cursor()

    query = ("SELECT timestamp FROM timestamps ORDER BY timestamp desc limit 1")
    cursor.execute(query)
    row = cursor.fetchone()
    ret = None
    if row is not None:
        ret = row[0]

    cursor.close()
    cnx.close()

    return ret
    
def saveTimestampToDatabase(timestamp):
    cnx = getMysqlConnection()
    cursor = cnx.cursor()

    try:
        cursor.execute("INSERT INTO timestamps (timestamp) VALUES (%s) ON DUPLICATE KEY UPDATE timestamp=timestamp", (timestamp,))
    except:
        print "Error inserting timestamp: ", sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2]

    cnx.commit()
    cursor.close()
    cnx.close()
    return "success"
    
def saveAnnotationsToDatabase(ip, keysToSave):

    if len(keysToSave) <= 0:
        return "success"

    cnx = getMysqlConnection()
    cursor = cnx.cursor()

    query = ("DELETE FROM annotations WHERE ip_address = %s")
    cursor.execute(query, (ip,))
    cnx.commit()

    query = ("INSERT INTO annotations (ip_address, keyname, keyvalue) VALUES (%s, %s, %s)")
    for key in keysToSave:
        cursor.execute(query, (ip, key, keysToSave[key]))

    cnx.commit()
    cursor.close()
    cnx.close()
    return "success"
    
def getNodesFromDatabase():
    cnx = getMysqlConnection()
    cursor = cnx.cursor()

    query = ("SELECT ipAddress, color, displayWithMultiSpeak FROM nodes")
    cursor.execute(query)

    ret = list()
    for (ipAddress, color, displayWithMultiSpeak) in cursor:
        node = SavedNode(ipAddress, color, displayWithMultiSpeak)
        ret.append(node)

    cursor.close()
    cnx.close()

    return ret
    
def saveNodesToDatabase(nodes):
    if len(nodes) <= 0:
        return "no nodes"

    cnx = getMysqlConnection()
    cursor = cnx.cursor()

    query = ("INSERT INTO nodes (ipAddress, color, displayWithMultiSpeak) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE color = values(color), displayWithMultiSpeak = values(displayWithMultiSpeak)")
    for key in nodes:
        cursor.execute(query, (nodes[key].ipAddress, nodes[key].color, nodes[key].displayWithMultiSpeak))

    cnx.commit()
    cursor.close()
    cnx.close()
    return "success"
    
def getLinksFromDatabase():
    cnx = getMysqlConnection()
    cursor = cnx.cursor()

    query = ("SELECT source, target, displayWithMultiSpeak FROM links")
    cursor.execute(query)

    ret = list()
    for row in cursor:
        ret.append(row)

    cursor.close()
    cnx.close()

    return ret
    
def saveLinksToDatabase(links):
    if len(links) <= 0:
        return "no links"

    cnx = getMysqlConnection()
    cursor = cnx.cursor()

    query = ("INSERT INTO links (source, target, displayWithMultiSpeak) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE displayWithMultiSpeak = values(displayWithMultiSpeak)")
    for link in links:
        cursor.execute(query, (link.source, link.target, link.displayWithMultiSpeak))

    cnx.commit()
    cursor.close()
    cnx.close()
    return "success"
    
def saveAnnotationsToDatabase(ip, keysToSave):

    if len(keysToSave) <= 0:
        return "success"

    cnx = getMysqlConnection()
    cursor = cnx.cursor()

    query = ("DELETE FROM annotations WHERE ip_address = %s")
    cursor.execute(query, (ip,))
    cnx.commit()

    query = ("INSERT INTO annotations (ip_address, keyname, keyvalue) VALUES (%s, %s, %s)")
    for key in keysToSave:
        cursor.execute(query, (ip, key, keysToSave[key]))

    cnx.commit()
    cursor.close()
    cnx.close()
    return "success"

def getAnnotationsFromDatabase(ip):
    cnx = getMysqlConnection()
    cursor = cnx.cursor()

    query = ("SELECT keyname, keyvalue FROM annotations WHERE ip_address = %s")
    cursor.execute(query, (ip,))

    ret = dict()
    for (keyname, keyvalue) in cursor:
        ret[keyname] = keyvalue

    cursor.close()
    cnx.close()
    return ret
    
def getSetting(setting):
    cnx = getMysqlConnection()
    cursor = cnx.cursor()

    query = ("SELECT value FROM setting WHERE name = %s")
    cursor.execute(query, (setting,))

    ret = cursor.fetchone()
    if ret is not None and len(ret) > 0:
        ret = ret[0]

    cursor.close()
    cnx.close()

    return ret
    
def saveSetting(name, value):
    cnx = getMysqlConnection()
    cursor = cnx.cursor()

    query = ("INSERT INTO setting (name, value) VALUES (%s, %s) ON DUPLICATE KEY UPDATE value = values(value)")
    cursor.execute(query, (name, value))

    cnx.commit()
    cursor.close()
    cnx.close()
    return "success"
