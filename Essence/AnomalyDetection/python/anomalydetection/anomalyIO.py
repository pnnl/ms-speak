from histograms import Histograms

import datetime
import json
import random
import requests

class AnomalyIO():
    """
    Python is a little goofy with timezones so for now we assume +0000
    """

    def __init__(self, hostname="localhost"):
        self.causeCache = None
        self.statesCache = None
        self.host = hostname

    def getCause(self, id):
        if id < 0:
            return None

        if self.causeCache is None:
            self.causeCache = dict()
            resp = requests.get('http://' + self.host +
                                '/essence-services/anomaly/causes/')
            if resp.status_code != 200:
                # This means something went wrong.
                raise ApiError('GET /tasks/ {}'.format(resp.status_code))

            for i in resp.json():
                self.causeCache[i['id']] = i['cause']

        if id in self.causeCache:
            return self.causeCache[id]

        return None


    def getStates(self, id):
        if id < 0:
            return None

        if self.statesCache is None:
            self.statesCache = dict()
            resp = requests.get('http://' + self.host + 
                                '/essence-services/anomaly/states/')
            if resp.status_code != 200:
                # This means something went wrong.
                raise ApiError('GET /tasks/ {}'.format(resp.status_code))

            for i in resp.json():
                self.statesCache[i['id']] = i['state']

        if id in self.statesCache:
            return self.statesCache[id]

        return None

    @staticmethod
    def getFakeAnomalies():
        ret = dict()
        ret[(0,0)] = Histograms(2, 1)
        for t in range(500):
            ret[(0,0)].insert_one("10.0.0.1", t, 
                                  value = 210 + random.randint(0,200), 
                                  use_internal_time = True)
            ret[(0,0)].insert_one("10.0.0.2", t, 
                                  value = 810 + random.randint(0,200), 
                                  use_internal_time = True)
            ret[(0,0)].insert_one("10.0.0.3", t, 
                                  value = 210 + random.randint(0,200), 
                                  use_internal_time = True)
            ret[(0,0)].next_row()

        ret[(1,1)] = Histograms(2, 1)
        for t in range(500):
            ret[(1,1)].insert_one("10.0.0.1", t, 
                                  value = 0 + random.randint(0,200), 
                                  use_internal_time = True)
            ret[(1,1)].insert_one("10.0.0.2", t, 
                                  value = 900 + random.randint(0,200), 
                                  use_internal_time = True)
            ret[(1,1)].insert_one("10.0.0.3", t, 
                                  value = 0 + random.randint(0,200), 
                                  use_internal_time = True)
            ret[(1,1)].next_row()

        ret[(2,2)] = Histograms(2, 1)
        for t in range(500):
            ret[(2,2)].insert_one("10.0.0.1", t, 
                                  value = 0 + random.randint(0,100), 
                                  use_internal_time = True)
            ret[(2,2)].insert_one("10.0.0.2", t, 
                                  value = 0 + random.randint(0,100), 
                                  use_internal_time = True)
            ret[(2,2)].insert_one("10.0.0.3", t, 
                                  value = 0 + random.randint(0,100), 
                                  use_internal_time = True)
            ret[(2,2)].next_row()
        ret[(3,3)] = Histograms(2, 1)
        for t in range(500):
            ret[(3,3)].insert_one("10.0.0.1", t, 
                                  value = 1000 + random.randint(0,200), 
                                  use_internal_time = True)
            ret[(3,3)].insert_one("10.0.0.2", t, 
                                  value = 11200 + random.randint(0,200), 
                                  use_internal_time = True)
            ret[(3,3)].insert_one("10.0.0.3", t, 
                                  value = 1000 + random.randint(0,200), 
                                  use_internal_time = True)
            ret[(3,3)].next_row()
        return ret

    def getAnomalies(self, testStart = None, testEnd = None, 
                     trainStart = None, trainEnd = None,
                     filterValue = None, targetType = None, 
                     algorithm = None, userState = None, 
                     userCause = None):
        """
        Returns a dictionary where each key is a tuple of (cause, state)
        and each value is a Histogram() of observed anomalous data
        tagged by a user as having that cause/state
        """

        arg = ""
        if testStart is not None:
	    arg += "&detectionTimeWindowStart=" + str(testStart)
	if testEnd is not None:
	    arg += "&detectionTimeWindowEnd=" + str(testEnd)
	if trainStart is not None:
	    arg += "&trainingTimeWindowStart=" + str(trainStart)
	if trainEnd is not None:
	    arg += "&trainingTimeWindowEnd=" + str(trainEnd)
	if filterValue is not None:
	    arg += "&sourceValue=" + sourceValue
	if targetType is not None:
	    arg += "&targetType=" + targetType
	if algorithm is not None:
	    arg += "&algorithm=" + algorithm
	if userCause is not None:
	    arg += "&userCause=" + userCause
	if userState is not None:
	    arg += "&userState=" + userState
        print "arg is ",arg
        resp = requests.get('http://' + self.host + 
                                '/essence-services/anomaly/query/?' + arg)
        if resp.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))


        cause = -1
        state = -1

        ret = dict()
        for i in resp.json():

            if 'userCause' in i and 'id' in i['userCause']:
                cause = i['userCause']['id']
            if 'userState' in i and 'id' in i['userCause']:
                state = i['userCause']['id']

            if (cause, state) not in ret:
                # for why we init Histogram this way, see __init__ where it
                # takes in a matrix as an argument and converts it into
                # internal format. We're basically doing the same thing here
                # but skipping the step of making the matrix to pass into init
                ret[(cause, state)] = Histograms(-1, -1)

            hist = ret[(cause, state)]
            if 'anomalyEntries' not in i:
                continue
            for entries in i['anomalyEntries']:
                hist.insert_one(entries['sequenceNumber'], -1, 
                                use_internal_time = True)
            hist.next_row()
                    
        return ret


#pattern is [0, 2]{"sourceValue":"10.0.0.2","sourceType":1,"predictions":[{"cause":{"id":0},"state":{"id":1},"score":"ok"},{"cause":{"id":1},"state":{"id":2},"score":"bye"}],"normalEntries":[{"meanCount":268.1284403669725,"targetValue":"10.0.0.1","standardDeviation":5.456417679927006,"minCount":256,"maxCount":283,"sequenceNumber":0},{"meanCount":0.0,"targetValue":"10.0.0.2","standardDeviation":0.0,"minCount":0,"maxCount":0,"sequenceNumber":1},{"meanCount":0.0,"targetValue":"10.0.0.3","standardDeviation":0.0,"minCount":0,"maxCount":0,"sequenceNumber":2}],"detectionTimeWindowStart":"Wed, 10 Feb 2016 10:07:41 -0500","patternIndex":[0,2],"score":212.87350824719027,"trainingTimeWindowStart":"Wed, 10 Feb 2016 09:30:30 -0500","trainingTimeWindowEnd":"Wed, 10 Feb 2016 10:06:40 -0500","targetType":1,"detectionTimeWindowEnd":"Wed, 10 Feb 2016 10:44:41 -0500","anomalyEntries":[{"count":213,"targetValue":"10.0.0.1","sequenceNumber":0},{"count":0,"targetValue":"10.0.0.2","sequenceNumber":1},{"count":47,"targetValue":"10.0.0.3","sequenceNumber":2}],"algorithm":"svm_chi_squared_1.0"}

    def prepareJson(self, testStart, testEnd, trainStart, trainEnd,
                       filterType, filterValue, featureType,
                       algorithm, score, 
                       trainingFeatureValue, trainingMinCount,
                       trainingMaxCount, trainingMeanCount,
                       trainingStandardDeviation, anomalyFeatureValue,
                       anomalyCount, patternIndex=None, predictedCauses=None,
                       predictedStates=None, predictedScoreString=None):
        """
        Note: the official terminology is to use the word "feature" to describe
        the histogram data and "filter" to describe where the data comes from.
        However as of this writing the essence side still uses "target" and 
        "source"
        """

        if patternIndex is not None:
            assert isinstance(patternIndex, list)

        if predictedCauses is not None or predictedStates is not None or \
                predictedScoreString is not None:
            assert len(predictedCauses) == len(predictedStates) == \
                len(predictedScoreString)

        if trainingFeatureValue is not None or traniningMinCount is not None or \
                trainingMaxCount is not None or traningMeanCount is not None:
            assert len(trainingFeatureValue) == len(trainingMinCount) == \
                len(trainingMaxCount) == len(trainingStandardDeviation)

        if anomalyFeatureValue is not None and anomalyCount is not None:
            assert len(anomalyFeatureValue) == len(anomalyCount)

        data = dict()

        testStart_s = datetime.datetime.fromtimestamp(testStart).strftime(
            "%a, %d %b %Y  %H:%M:%S") + " +0000"
        data['detectionTimeWindowStart'] = testStart_s

        testEnd_s = datetime.datetime.fromtimestamp(testEnd).strftime(
            "%a, %d %b %Y  %H:%M:%S") + " +0000"
        data['detectionTimeWindowEnd'] = testEnd_s

        trainStart_s = datetime.datetime.fromtimestamp(trainStart).strftime(
            "%a, %d %b %Y  %H:%M:%S") + " +0000"
        data['trainingTimeWindowStart'] = trainStart_s

        trainEnd_s = datetime.datetime.fromtimestamp(trainEnd).strftime(
            "%a, %d %b %Y  %H:%M:%S") + " +0000"
        data['trainingTimeWindowEnd'] = trainEnd_s

        data['sourceType'] = filterType
        data['sourceValue'] = filterValue
        data['targetType'] = featureType
        data['algorithm'] = algorithm
        data['score'] = score
        data['patternIndex'] = patternIndex
        
        normalEntries = list()
        for i in range(len(trainingFeatureValue)):
            temp = dict()
            temp['sequenceNumber'] = i
            temp['targetValue'] = trainingFeatureValue[i]
            temp['minCount'] = trainingMinCount[i]
            temp['maxCount'] = trainingMaxCount[i]
            temp['meanCount'] = trainingMeanCount[i]
            temp['standardDeviation'] = trainingStandardDeviation[i]
            normalEntries.append(temp)
        data['normalEntries'] = normalEntries

        anomalyEntries = list()
        for i in range(len(anomalyFeatureValue)):
            temp = dict()
            temp['sequenceNumber'] = i
            temp['targetValue'] = anomalyFeatureValue[i]
            temp['count'] = anomalyCount[i]
            anomalyEntries.append(temp)
        data['anomalyEntries'] = anomalyEntries

        predictions = list()
        for i in range(len(predictedCauses)):
            temp = dict()
            tempCause = dict()
            tempState = dict()

            tempCause['id'] = predictedCauses[i]
            temp['cause'] = tempCause

            tempState['id'] = predictedStates[i]
            temp['state'] = tempState

            temp['score'] = predictedScoreString[i]
            predictions.append(temp)

        data['predictions'] = predictions

        payload = json.JSONEncoder().encode(data)
        return payload

    def writeAnomalies(payload):
        url = 'http://' + self.host + '/essence-services/anomaly/'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=payload, headers=headers)
