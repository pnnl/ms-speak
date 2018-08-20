#!/usr/bin/python2.7

from anomalyIO import AnomalyIO
from cassandraIO import CassandraIO
from flask import Flask
from flask import request
from flask import Response
from flask_restful import reqparse
from histograms import Histograms
from pattern import AnomalyPattern
from svm_calc import SVMCalc

import argparse
import numpy as np
import re
import sys

##
# To run this, make sure the permissions are right:
# chmod a+x daemon_service.py 
#
# Then run it:
# ./daemon_service.py
##

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--docker_mode', default=False, action='store_true',
                    help='Configure server to operate inside Docker container')
args = parser.parse_args()

app = Flask(__name__)

next_id = 0
hist_dict = dict()
anom = None

@app.route('/getdb')
def getdb():
    """
    Retrieve a dataset from the packet database and store it. An ID number
    is returned which can be used to reference this dataset in the future

    Assumes that the packet and anomaly databases are on the same machine
    """
    global next_id
    global hist_dict
    global anom

    parser = reqparse.RequestParser()
    parser.add_argument('hostname', help="default = localhost")
    parser.add_argument('keyspace', required=True)
    parser.add_argument('table', required=True)
    parser.add_argument('filter', required=True)
    parser.add_argument('filter_val', required=True)
    parser.add_argument('featuresCSV', required=True)
    parser.add_argument('sample_window_sec', required=True, type=int)
    parser.add_argument('slide_window_sec', required=True, type=int)
    args = parser.parse_args()

    c = CassandraIO(args['keyspace'], args['table'], hostname=args['hostname'])

    hist = c.get_histogram(args['sample_window_sec'], args['slide_window_sec'],
                           args['filter'], args['filter_val'],
                           args['featuresCSV'])
    c.close()

    hist_dict[next_id] = hist

    output = "Dataset ID: " + str(next_id) + "\nFeatures (" + \
        args['featuresCSV'] + "):\n"
    for f in hist.get_features():
        output += f + "\n"

    next_id += 1

    if anom is None:
        anom = AnomalyIO(hostname=args['hostname'])

    return Response(output, mimetype='text/plain')

@app.route('/getfakedata')
def getfakedata():
    global next_id
    global hist_dict
    train_h = Histograms.get_fake_histogram_train()
    test_h = Histograms.get_fake_histogram_test()
    hist_dict[next_id] = train_h

    output = "Dataset ID: " + str(next_id) + "\n"
    for f in train_h.get_features():
        output += f + "\n"

    next_id += 1
    train_h.print_histograms()
    hist_dict[next_id] = test_h

    output += "Dataset ID: " + str(next_id) + "\n"
    for f in test_h.get_features():
        output += f + "\n"

    next_id += 1
    test_h.print_histograms()
    return Response(output, mimetype='text/plain')

@app.route('/getcause')
def getcause():
    """
    Translate an ID to a string from the anomaly causes table. If a hostname
    is passed, use that hostname from now on (and reset the caches)

    If getDB is called first, we will use that hostname
    """
    global anom
    parser = reqparse.RequestParser()
    parser.add_argument('id', required=True, type=int)
    parser.add_argument('hostname', help="not required if getDB called first")
    args = parser.parse_args()
    if args['hostname'] is not None:
        anom = AnomalyIO(hostname=args['hostname'])

    if anom == None:
        return Response("hostname undefined. See docs", mimetype='text/plain')

    ret = anom.getCause(args['id'])
    if ret is None:
        ret = "ID not found"
    return Response(ret, mimetype='text/plain')

@app.route('/getstates')
def getstates():
    """
    Translate an ID to a string from the anomaly states table. If a hostname
    is passed, use that hostname from now on (and reset the caches)

    If getDB is called first, we will use that hostname
    """
    global anom

    parser = reqparse.RequestParser()
    parser.add_argument('id', required=True, type=int)
    parser.add_argument('hostname', help="not required if getDB called first")
    args = parser.parse_args()
    if args['hostname'] is not None:
        anom = AnomalyIO(hostname=args['hostname'])

    if anom == None:
        return Response("hostname undefined. See docs", mimetype='text/plain')

    ret = anom.getStates(args['id'])
    if ret is None:
        ret = "ID not found"

    return Response(ret, mimetype='text/plain')

@app.route('/getanomalies')
def getanomalies():
    """
    Retrieve the user-labeled anomaly data
    """
    global anom

    parser = reqparse.RequestParser()
    parser.add_argument('testStart', type=int)
    parser.add_argument('testEnd', type=int)
    parser.add_argument('trainStart', type=int)
    parser.add_argument('trainEnd', type=int)
    parser.add_argument('filterValue')
    parser.add_argument('targetType')
    parser.add_argument('algorithm')
    parser.add_argument('userState')
    parser.add_argument('userCause')
    args = parser.parse_args()

    ret = anom.getAnomalies(testStart=args['testStart'],
                            testEnd=args['testEnd'],
                            trainStart=args['trainStart'],
                            trainEnd=args['trainEnd'],
                            filterValue=args['filterValue'],
                            targetType=args['targetType'],
                            algorithm=args['algorithm'],
                            userState=args['userState'],
                            userCause=args['userCause'])
    output = ""
    for k in ret:
        output += str(k[0]) + "," +str(k[1]) + \
            str(len(ret[k].get_histograms())) + "\n"

    return Response(output, mimetype='text/plain')

@app.route('/writeanomalies')
def writeanomalies():
    """
    Write a new anomaly to the anomaly database. As of this writing, this code 
    not been tested against the Essence API so this function is a placeholder
    """
    global anom

    anom.writeAnomalies(1,10,2,20,
                        "okay", "okay2", "foo",
                        "chi2",1.2, 
                        ["a","b","c"], [3,4,5], 
                        [100,200,300], [150,151,152], 
                        [2,3,4], ['7','8','9'],
                        [11,12,13], patternIndex=[1,2,3], predictedCauses=[1,2],
                        predictedStates=[1,2],predictedScoreString="good")
    return Response("ok", mimetype='text/plain')

@app.route('/test')
def test():
    """
    Run a test and look for anomalies

    The inputs are two dataset IDs and optional
    parameters to define the time windows being
    considered
    """
    global hist_dict

    # see svm_calc.py:test()
    parser = reqparse.RequestParser()
    parser.add_argument('train_start_sec', type=int)
    parser.add_argument('train_end_sec', type=int)
    parser.add_argument('train_from_start_min', type=int)
    parser.add_argument('train_from_end_min', type=int)
    parser.add_argument('train_drop_start_min', type=int)
    parser.add_argument('train_drop_end_min', type=int)
    parser.add_argument('test_start_sec', type=int)
    parser.add_argument('test_end_sec', type=int)
    parser.add_argument('test_from_start_min', type=int)
    parser.add_argument('test_from_end_min', type=int)
    parser.add_argument('test_drop_start_min', type=int)
    parser.add_argument('test_drop_end_min', type=int)

    parser.add_argument('train_id', required=True, type=int)
    parser.add_argument('test_id', required=True, type=int)
    args = parser.parse_args()

    output = ""
    error = 0
    if args['train_id'] not in hist_dict:
        output += "Error: training ID not found: " + str(args['train_id'])
        error += 1
    if args['test_id'] not in hist_dict:
        output += "Error: test ID not found: " + str(args['test_id'])
        error += 1
    if error == 0:
        ret = SVMCalc.test(hist_dict[args['train_id']], 
                           hist_dict[args['test_id']],
                           train_start_sec=args['train_start_sec'],
                           train_end_sec=args['train_end_sec'],
                           train_from_start_min=args['train_from_start_min'],
                           train_from_end_min=args['train_from_end_min'],
                           train_drop_start_min=args['train_drop_start_min'],
                           train_drop_end_min=args['train_drop_end_min'],
                           test_start_sec=args['test_start_sec'],
                           test_end_sec=args['test_end_sec'],
                           test_from_start_min=args['test_from_start_min'],
                           test_from_end_min=args['test_from_end_min'],
                           test_drop_start_min=args['test_drop_start_min'],
                           test_drop_end_min=args['test_drop_end_min'])

        # These histograms might have different features or they're in 
        # different orders. Generate a union of them
        train_feat = hist_dict[args['train_id']].get_features()
        test_feat = hist_dict[args['test_id']].get_features()
        feat_uniq = dict()
        for f in train_feat + test_feat:
            feat_uniq[f] = 0
        sort_feat = sorted(feat_uniq.keys())

        test_h_get = hist_dict[args['test_id']].get_histograms(
            features=sort_feat,
            start_sec=args['test_start_sec'],
            end_sec=args['test_end_sec'],
            from_start_min=args['test_from_start_min'],
            from_end_min=args['test_from_end_min'],
            drop_start_min=args['test_drop_start_min'],
            drop_end_min=args['test_drop_end_min'])

        train_h_get = hist_dict[args['train_id']].get_histograms(
            features=sort_feat,
            start_sec=args['train_start_sec'],
            end_sec=args['train_end_sec'],
            from_start_min=args['train_from_start_min'],
            from_end_min=args['train_from_end_min'],
            drop_start_min=args['train_drop_start_min'],
            drop_end_min=args['train_drop_end_min'])
        
        count = 0

        anomalies = AnomalyIO.getFakeAnomalies()
        for r,h in zip(ret,test_h_get):
            output += str(count) + ":" + str(h) + " score " + str(r) + "\n"
            count += 1
            if r < -0.02:
                output += "ANOMALY\n"
                #output += np.array_str(SVMCalc.onevsall(anomalies, [h]))+"\n"
                output += SVMCalc.onevsall2(anomalies, [h])
                #ret = AnomalyPattern.anomaly_pattern(h, 
                #                     np.mean(train_h_get, axis=0),
                #                     np.std(train_h_get, axis=0))
                #if len(ret) > 0:
                #    output += "pattern: " + str(ret) + "\n"

    return Response(output,  mimetype='text/plain')

if __name__ == '__main__':
    if args.docker_mode == True:
        app.run(host='0.0.0.0', debug=False)
    else:
        app.run(debug=True)
