from anomalydetection.anomalyIO import AnomalyIO
from anomalydetection.constants import *
from anomalydetection.histograms import Histograms
from anomalydetection.svm_calc import SVMCalc
from anomalydetection.pattern import AnomalyPattern
import numpy as np
class TestSupervisedLearning:
        
    def test_pattern(self):
        train_h = Histograms.get_fake_histogram_train()
        test_h = Histograms.get_fake_histogram_test()
        ret = SVMCalc.test(train_h, test_h);

        train_feat = train_h.get_features()
        test_feat = test_h.get_features()
        feat_uniq = dict()
        for f in train_feat + test_feat:
            feat_uniq[f] = 0

        sort_feat = sorted(feat_uniq.keys())
        test_h_get = test_h.get_histograms(
            features=sort_feat)
        train_h_get = train_h.get_histograms(
            features=sort_feat)

        anom_count = 0
        for r,h in zip(ret,test_h_get):
            ret = []
            if r < -0.02:
                print "ANOMALY\n"
                anom_count += 1
                ret = AnomalyPattern.anomaly_pattern(h, 
                                                     np.mean(train_h_get, axis=0),
                                                     np.std(train_h_get, axis=0))
        print "total ", anom_count

        # These bounds are mostly made up. I think as long as it isn't none
        # or all, it is ok. The randomness of the data generation and the 
        # cross validation affects the results
        assert anom_count >= 10
        assert anom_count <= 23
        
