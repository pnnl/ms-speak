from anomalydetection.anomalyIO import AnomalyIO
from anomalydetection.constants import *
from anomalydetection.histograms import Histograms
from anomalydetection.cassandraIO import CassandraIO
from random import randint
from anomalydetection.svm_calc import SVMCalc
import time
from sklearn.datasets import load_iris
import numpy as np
import json
import datetime

class TestHistograms:
    def setUp(self):
        # these are only used for one test so they should either be named
        # better or moved somewhere 
        self.item_count = 10000
        self.values_count = 10

    def test_svm(self):
        """
        Use a built-in dataset to generate a consistent test case. We'll
        test the data against itself and expect few anomalies then test
        against some bogus data and expect a large number of anomalies
        """
        i = load_iris()
        assert i.data.shape[0] == 150 #detect if data changes in future version

        print "Using same data for training and testing (low anomaly rate)"
        h1 = Histograms(0, 0, matrix = i.data)
        res = SVMCalc.test(h1, h1)

        count = 0
        anom = 0
        for r in res:
            score = r[0]
            if score < -0.001:
                raise Exception("Same data for training and testing got",
                                "unexpectedly high anomaly score", score)
            count += 1
            if score < 0:
                anom += 1
        pct = anom/float(count)
        print "Anomaly percentage %0.3f" % (pct)
        if (pct > 0.05):
            raise Exception("Same data for training and testing got",
                            "unexpectedly high anomaly ratio", (pct))

        print "Using same data but verify padding on size mismatches works"
        (r,c) = i.data.shape
        wide_m = np.zeros((r,c+3), np.float64)
        wide_m[0:r, 0:c] = i.data.copy()
        h2 = Histograms(0, 0, matrix = wide_m)
        res = SVMCalc.test(h1, h2)

        count = 0
        anom = 0
        for r in res:
            score = r[0]
            if score < -0.001:
                raise Exception("Padded same data for training and testing got",
                                "unexpectedly high anomaly score", score)
            count += 1
            if score < 0:
                anom += 1
        pct = anom/float(count)
        print "Anomaly percentage %0.3f" % (pct)
        if (pct > 0.05):
            raise Exception("Padded same data for training and testing got",
                            "unexpectedly high anomaly ratio", (pct))

        # make some very anomalous data
        anom_m = i.data.copy()
        for r in anom_m:
            for c in range(len(r)):
                r[c] *= 10

        print "Testing with anomalous data (high anomaly rate)"
        h3 = Histograms(0, 0, matrix = anom_m)
        res = SVMCalc.test(h1, h3)
        count = 0
        anom = 0
        for r in res:
            score = r[0]
            if score > -0.04:
                raise Exception("With highly anomalous data, got unexpectedly",
                                "low anomaly score", score)
            count += 1
            if score < 0:
                anom += 1
        pct = anom/float(count)
        print "Anomaly percentage %0.3f" % (pct)
        if (pct < 0.99):
            raise Exception("With highly anomalous data, got unexpectedly",
                            "low anomaly ratio", (pct))

        print "Anomalous data with padding"
        (r,c) = i.data.shape
        wide_m = np.ones((r,c+3), np.float64)
        wide_m[0:r, 0:c] = i.data.copy()
        h4 = Histograms(0, 0, matrix = wide_m)
        res = SVMCalc.test(h1, h4)

        count = 0
        anom = 0
        for r in res:
            score = r[0]
            if score > -0.04:
                raise Exception("Padded anomalous data, got unexpectedly",
                                "low anomaly score", score)
            count += 1
            if score < 0:
                anom += 1
        pct = anom/float(count)
        print "Anomaly percentage %0.3f" % (pct)
        if (pct < 0.99):
            raise Exception("Padded anomalous data got unexpectedly",
                            "low anomaly ratio", (pct))

        print "Testing bounds splitting"
        time_diff = h1._end_sec - h1._start_sec
        # the iris dataset only has 150 points in it so this split has big
        # implications especially since it is in 1 minute granularity
        # and we import the data into a 5 minute period
        split_pct = .75
        train_time = int(round(time_diff * split_pct / 60))
        test_time = int(round(time_diff * (1.0-split_pct) / 60))

        res = SVMCalc.test(h1, h1, train_from_start_min = train_time,
                           test_from_end_min = test_time)

        count = 0
        anom = 0
        # we know the worst score that using the same data for training and test
        # got us. Now we're using a subset of the training data so our test 
        # should give us a slightly worse score
        worse_score_than_same_data = 0
        for r in res:
            score = r[0]
            # score tolerance is loosened because we have less training data
            if score < 0.0:
                raise Exception("Split data for training and testing got",
                                "unexpectedly high anomaly score", score)
            count += 1
            if score < 0:
                anom += 1
        pct = anom/float(count)
        print "Anomaly percentage %0.3f" % (pct)
        if (pct > 0.05):
            raise Exception("Split data for training and testing got",
                            "unexpectedly high anomaly ratio", (pct))

        print "Using same data for training and testing (low anomaly rate)"
        h1 = Histograms(0, 0, matrix = i.data)
        res = SVMCalc.test(h1, h1, train_start_sec = 6, test_start_sec = 6,
                           train_end_sec = h1._end_sec - 6,
                           test_end_sec = h1._end_sec - 6)

        count = 0
        anom = 0
        worst_score_same_data = 9999
        for r in res:
            score = r[0]
            if score < -0.001:
                raise Exception("Same data for training and testing got",
                                "unexpectedly high anomaly score", score)
            if score < worst_score_same_data:
                worst_score_same_data = score
            count += 1
            if score < 0:
                anom += 1
        pct = anom/float(count)
        print "Anomaly percentage %0.3f" % (pct)
        if (pct > 0.05):
            raise Exception("Same data for training and testing got",
                            "unexpectedly high anomaly ratio", (pct))

    def test_histogram(self):
        debug_override = 1

        # slide is aligned with sample
        sample_window_sec = 1800
        slide_window_sec = 300
        highest_time_sec = 5000
        self.exercise_histogram(sample_window_sec, slide_window_sec,
                           highest_time_sec, debug_override)

        sample_window_sec = 300
        slide_window_sec = 300
        highest_time_sec = 1000
        self.exercise_histogram(sample_window_sec, slide_window_sec,
                           highest_time_sec, debug_override)

        # slide is not aligned with sample
        sample_window_sec = 1800
        slide_window_sec = 456
        highest_time_sec = 5000
        self.exercise_histogram(sample_window_sec, slide_window_sec,
                           highest_time_sec, debug_override)

        # slide > sample isn't a useful configuration because there
        # will be gaps in the data
        sample_window_sec = 300
        slide_window_sec = 600
        highest_time_sec = 1000
        try:
            self.exercise_histogram(sample_window_sec, slide_window_sec,
                                    highest_time_sec, debug_override)
            raise
        except:
            pass

    def exercise_histogram(self, sample_window_sec, slide_window_sec,
                           highest_time_sec, debug_override):

        new_hist = Histograms(sample_window_sec, slide_window_sec, 
                              debug_override)

        print "Inserting boundary values"
        new_hist.insert_one(0, 0)
        new_hist.insert_one(1, slide_window_sec)
        new_hist.insert_one(2, sample_window_sec)
        new_hist.insert_one(3, slide_window_sec)
        new_hist.insert_one(4, sample_window_sec)
        new_hist.insert_one(5, slide_window_sec * 2)
        new_hist.insert_one(6, sample_window_sec * 2)
        new_hist.insert_one(7, highest_time_sec)

        print "Inserting random values"
        for i in range(self.item_count):
            new_hist.insert_one(randint(0, self.values_count),
                                randint(0, highest_time_sec))

        print "Displaying result (timestamp: histogram)"
        new_hist.print_histograms()
        print "Validating results"
        new_hist.get_histograms()

    def test_anomalies(self):
        anom = AnomalyIO()

        testStart = 1234
        testEnd = 4321
        trainStart = 34567
        trainEnd = 76543
        filterType = "source_address"
        filterValue = "10.0.0.1"
        featureType = "dest_address"
        algorithm = "chi_squared"
        score = 1.23
        trainingFeatureValue = ["10.0.0.2", "10.0.0.3", "10.0.0.4"]
        trainingMinCount = [0, 1, 2]
        trainingMaxCount = [300, 400, 500]
        trainingMeanCount = [150, 250, 350]
        trainingStandardDeviation = [22, 33, 44]
        anomalyFeatureValue = ["10.0.0.2", "10.0.0.3", "10.0.0.4"]
        anomalyCount = [150, 999, 10]
        patternIndex = [3, 1, 2]
        predictedCauses = [2, 3]
        predictedStates = [4, 5]
        predictedScoreString = ["low", "high"]

        ret_json = anom.prepareJson(testStart, testEnd, trainStart, trainEnd,
                         filterType, filterValue, featureType,
                         algorithm, score,
                         trainingFeatureValue, trainingMinCount,
                         trainingMaxCount, trainingMeanCount,
                         trainingStandardDeviation, anomalyFeatureValue,
                         anomalyCount, patternIndex=patternIndex, 
                         predictedCauses=predictedCauses,
                         predictedStates=predictedStates, 
                         predictedScoreString=predictedScoreString)

        ret = json.loads(ret_json)

        temp = datetime.datetime.strptime(ret['detectionTimeWindowStart'],
                                          "%a, %d %b %Y  %H:%M:%S +0000")     
        assert int(time.mktime(temp.timetuple())) == testStart

        temp = datetime.datetime.strptime(ret['detectionTimeWindowEnd'],
                                          "%a, %d %b %Y  %H:%M:%S +0000")     
        assert int(time.mktime(temp.timetuple())) == testEnd

        temp = datetime.datetime.strptime(ret['trainingTimeWindowStart'],
                                          "%a, %d %b %Y  %H:%M:%S +0000")     
        assert int(time.mktime(temp.timetuple())) == trainStart

        temp = datetime.datetime.strptime(ret['trainingTimeWindowEnd'],
                                          "%a, %d %b %Y  %H:%M:%S +0000")     
        assert int(time.mktime(temp.timetuple())) == trainEnd

        # the essence REST API uses outdated terminology
        # see anomalyIO.prepareJson
        assert filterType == ret['sourceType']
        assert filterValue == ret['sourceValue']
        assert featureType == ret['targetType']
        assert algorithm == ret['algorithm']
        assert score == ret['score']
        assert sorted(patternIndex) == sorted(ret['patternIndex'])

        for i in range(len(ret['normalEntries'])):
            temp = ret['normalEntries'][i]
            assert temp['sequenceNumber'] == i
            #do these necessarily retain their ordering? not sure
            assert temp['targetValue'] == trainingFeatureValue[i]
            assert temp['minCount'] == trainingMinCount[i]
            assert temp['maxCount'] == trainingMaxCount[i]
            assert temp['meanCount'] == trainingMeanCount[i]
            assert temp['standardDeviation'] == trainingStandardDeviation[i]
            
        for i in range(len(ret['anomalyEntries'])):
            temp = ret['anomalyEntries'][i]
            assert temp['sequenceNumber'] == i
            assert temp['targetValue'] == anomalyFeatureValue[i]
            assert temp['count'] == anomalyCount[i]

        for i in range(len(ret['predictions'])):
            temp = ret['predictions'][i]
            assert len(temp['cause']) == 1

            assert temp['cause']['id'] == predictedCauses[i]

            assert len(temp['state']) == 1
            assert temp['state']['id'] == predictedStates[i]

            assert temp['score'] == predictedScoreString[i]
            
            
