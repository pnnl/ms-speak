import numpy as np
import time

from constants import *
from generic_calc import GenericCalc
from histograms import Histograms
from sklearn import cross_validation
from sklearn import preprocessing
from sklearn.metrics.pairwise import chi2_kernel
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import OneClassSVM
from sklearn.svm import SVC

class SVMCalc(GenericCalc):

    @staticmethod
    def test(train_h, test_h, train_start_sec=None, train_end_sec=None,
             train_from_start_min=None, train_from_end_min=None,
             train_drop_start_min=None, train_drop_end_min=None,
             test_start_sec=None, test_end_sec=None,
             test_drop_start_min=None, test_drop_end_min=None,
             test_from_start_min=None, test_from_end_min=None):
        """
        Run a test. Takes in a training dataset and a test dataset and
        optional arguments to set a time window to work with

        TODO: the edges of the dataspace should be dropped
        train_h and test_h are the Histogram() for training
        data and test data

        for start_sec, end_sec, from_start_min, from_end_min see
        histograms.get_histograms()
        """
        assert(isinstance(train_h, Histograms))
        assert(isinstance(test_h, Histograms))

        # These histograms might have different features or they're in 
        # different orders. Generate a union of them
        train_feat = train_h.get_features()
        test_feat = test_h.get_features()
        feat_uniq = dict()
        for f in train_feat + test_feat:
            feat_uniq[f] = 0
        sort_feat = sorted(feat_uniq.keys())

        train_m = train_h.get_histograms(features=sort_feat,
                                         start_sec = train_start_sec,
                                         end_sec = train_end_sec,
                                         from_start_min = train_from_start_min,
                                         from_end_min = train_from_end_min,
                                         drop_start_min = train_drop_start_min,
                                         drop_end_min = train_drop_end_min)
        test_m = test_h.get_histograms(features=sort_feat,
                                       start_sec = test_start_sec,
                                       end_sec = test_end_sec,
                                       from_start_min = test_from_start_min,
                                       from_end_min = test_from_end_min,
                                       drop_start_min = test_drop_start_min,
                                       drop_end_min = test_drop_end_min)

        # scale the data
        scaler = preprocessing.MaxAbsScaler().fit(train_m)
        train_m_s = scaler.transform(train_m)
        test_m_s = scaler.transform(test_m)

        train_k = chi2_kernel(train_m_s)
        test_k = chi2_kernel(test_m_s, train_m_s)

        if train_h._nu == -1:
            best_nu = SVMCalc._cross_validate(train_k)
            assert best_nu > 0
            assert best_nu <= 1
            train_h._nu = best_nu

        clf = OneClassSVM(kernel="precomputed", nu=train_h._nu)

        clf.fit(train_k)

        #positive = normal, negative = anomaly
        res = clf.decision_function(test_k)
        return res

    @staticmethod
    def _generate_nu_list(nu_dict, nu_start_pow_low, nu_start_pow_high):
        """
        nu is a configuration parameter for our classifier. The ideal nu
        depends on the dataset, so we generate a list of possibilities
        and do cross-validation on them to see which produces the best
        results. If the best nu is on the edge of the range of values,
        we expand the range and try again
        """

        for nu_base in NU_BASE_LIST:
            for nu_pow in range(nu_start_pow_low, nu_start_pow_high):
                new_nu = nu_base * pow(10, nu_pow)
                if new_nu not in nu_dict and \
                        new_nu > 0 and new_nu <=1:
                    nu_dict[new_nu] = -1
        return nu_dict

    @staticmethod
    def _cross_validate(train_k):
        """
        if using precomputed kernel, k_train is the precomputed output
        not the orignal data
        """
        target = np.zeros(train_k.shape[0])

        # mark all of these as normal data
        target.fill(1)

        best_nu = -1
        best_pct = -1

        nu_dict = dict()
        nu_start_pow_high = NU_START_POW_HIGH
        nu_start_pow_low = NU_START_POW_LOW

        # If the nu we select is on the edge of the list of possible nu values
        # we grow the list of nu values and try again. Since nu values are
        # bounded by (0,1] we can only grow so much. We break out if we run
        # out of useful nu so we don't get stuck in a loop
        while len(nu_dict.keys()) == 0 or best_nu == min(nu_dict.keys()) or \
                best_nu == max(nu_dict.keys()):

            nu_count = len(nu_dict.keys())
            nu_dict = SVMCalc._generate_nu_list(nu_dict, nu_start_pow_low,
                                            nu_start_pow_high)
            assert(len(nu_dict.keys()) > 0)
            # so future loops will expand generate_nu_list
            nu_start_pow_high += NU_EXPAND_INCREMENT
            nu_start_pow_low -= NU_EXPAND_INCREMENT

            if nu_count == len(nu_dict.keys()):
                # this means generate_nu_list did now grow the list any
                # more, probably because we hit the (0, 1] bound
                break
            for nu_try in nu_dict:
                if nu_dict[nu_try] != -1:
                    continue

                clf = OneClassSVM(kernel="precomputed", nu=nu_try)
                kfold = cross_validation.KFold(train_k.shape[1], n_folds=4)

                # this scoring param was arbitrarily selected
#http://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter
                s = cross_validation.cross_val_score(clf, train_k,
                                                     target,
                                                     scoring="f1",
                                                     cv=kfold, n_jobs=-1)
                mean = s.mean()
                print "nu %0.5f %0.8f (+/- %0.2f)" % (nu_try, s.mean(),s.std()*2)
                if mean > best_pct:
                    best_pct  = mean
                    best_nu = nu_try

                nu_dict[nu_try] = mean


        # we don't want to ruin the user experience by asserting 
        # inappropriately but if cross validation returns 0% correct
        # then something is broken
        assert(nu_dict[best_nu] > 0.01) #cross validate returned 0% correct
        return best_nu

    @staticmethod
    def onevsall2(anomalies, observed):
        """
        This takes an observed data and tests them against each
        set of anomalies and sees which one has the best score.
        This is not a onevsall impelementation but more of a
        one class classifier used against each class. I don't know
        if it is any better or worse, but it is much faster than
        onevsall, so I'll leave it here for now.

        The Java code used this method.
        """
        observed_h = None
        output = " "

        #somehow this is generating the same scores for training data.. weird
        for k in sorted(anomalies.keys()):
            if observed_h is None:
                observed_h = Histograms(0,0)
                features = anomalies[k].get_features()
                for i in range(len(features)):
                    observed_h.insert_one(features[i], 0, value=observed[0][i], 
                                          use_internal_time = True)

            #print anomalies[k].get_histograms()
            #import IPython
            #IPython.embed()
            output += str(k) + " : " + np.array_str(SVMCalc.test(anomalies[k], observed_h)) + "\n"

        return output

    @staticmethod
    def onevsall(anomalies, observed):
        """
        Test the observed data against the labeled anomalies
        observed MUST be a list of data points (each point is also
        a list) so passing in a single piece of observed data for
        testing still requires an array inside an array

        anomalies is a dict of Histograms where each key is
        
        This function implements a one-vs-all for each call. In my demo
        where this is called multiple times, this is actually a bit slow.
        See onevsall2
        """
        assert(isinstance(anomalies, dict))
        assert(isinstance(observed, list))

        dims = (0,0);
        all_h = None
        labels = None
        next_label = 0;
        # build a giant matrix of all anomaly data and make the labels
        # The labels matrix is samples x n_classes with a 1 if that sample
        # is in that class and a 0 if not. It is currently not sparse but
        # should eventually be
        label_count = len(anomalies.keys())

        for k in sorted(anomalies.keys()):
            if all_h is None:
                all_h = anomalies[k].get_histograms()
                for r in range(all_h.shape[0]):
                    row_label = np.zeros(label_count)
                    row_label[next_label] = 1
                    if labels is None:
                        labels = row_label
                    else:
                        labels = np.vstack((labels,row_label))
                next_label = 1
            else:
                new_h = anomalies[k].get_histograms()
                all_h = np.vstack([all_h, new_h])
                for r in range(new_h.shape[0]):
                    row_label = np.zeros(label_count)
                    row_label[next_label] = 1
                    labels = np.vstack((labels,row_label))
                next_label += 1

        # From the documentation:
        #SVC is quadratic with the number of samples and a dataset of 10k+ is hard
        #I used this because an example I found did. We should find out if there is
                # a better one
        clf = OneVsRestClassifier(SVC(probability=True), n_jobs = -1)
        scaler = preprocessing.MaxAbsScaler().fit(all_h)
        all_m_s = scaler.transform(all_h)

        observed_m_s = scaler.transform(observed)

        clf.fit(all_m_s, labels)

        # now test the new anomaly against the classifier
        # this seems to work but with this quirk: if two training classes have similar data
        # and is tested with an observed data that is similar to both, this reports neither as being matches
        # so the different classes influence each other  in that they split the 
        # vote if they're the same training data rather than simply maching both
        # as independent comparisons

        #return clf.predict_proba(observed_m_s)
        return clf.predict(observed_m_s)

