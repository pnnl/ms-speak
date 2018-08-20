#!/usr/bin/env python3

import urllib.parse, urllib.request
import sys

file = open(sys.argv[1], 'r')
request = file.read()
response = sys.argv[2]
params = bytes(request, 'utf-8')
url = 'http://10.0.0.2:8080/'
result = urllib.request.urlopen(url + response, params)
# print(f.read())
