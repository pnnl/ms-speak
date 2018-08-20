#!/usr/bin/python
# Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc

from cassandra.cluster import Cluster

session = Cluster(['127.0.0.1']).connect('demo')
for currentRow in session.execute('select content from packet'):
        print currentRow[0], '\n'
