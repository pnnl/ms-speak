from constants import *
import numpy as np
import random
import sys

class Histograms():
    """ 
    Histograms is a class that stores a series of histograms. Each histogram
    represents the number of times a certain feature has been seen within a 
    window of time. The feature identifiers are strings like the IP address or
    a message type but internally that is abstracted away into an integer index
    to save space.

    The histograms are organized by time. Each histogram is sample_window 
    seconds long and each subsequent histogram starts slide_window seconds 
    after the previous. Therefore, the times represented within one histogram 
    may overlapwith adjacent histograms.

    When a datapoint is stored via insert_one, it will be counted in all of the 
    appropriate histograms for that timestamp. The bounds on a histogram's time
    window are inclusive.

    Converting the dict structure to a numpy matrix 
    appears to be pretty expensive. We're kind of stuck while we are using 
    Cassandra. Maybe we can justloop over the data twice and  get the high and 
    low timestamps and count how many features there are. Also we can take as 
    input any user-desirebounds on the timestamps

    An optional argument to __init__ is a matrix. I think this will
    be primarily used for tests but it might be useful for other things in
    the future. If this option is used, the sample_window_sec and 
    slide_window_sec arguments are ignored

    It might seem silly to use this class to store a matrix and then return it
    but generic_calc requires a histogram so we can store misc data like the
    scaling factor or in the case of svm_calc, the precomputed nu parameter

    The matrix is recomputed every time get_histograms is called. We could do
    some caching here but the dimensions of the matrix depends on the other data
    it is being tested with
    """


    def __init__(self, sample_window_sec, slide_window_sec, debug_override=-1,
                 matrix = None):
        
        # slide > sample isn't a useful configuration because there
        # will be gaps in the data
        if sample_window_sec < slide_window_sec:
            raise Exception("Sample window cannot be less than slide window")

        self._sample_window = sample_window_sec
        self._scaling_factor = 0.0
        self._slide_window = slide_window_sec
        self._start_sec = sys.maxint
        self._end_sec = -1

        # sometimes we build a histogram using data that doesn't have a time
        # sequence so we have internal support for faking it to get a useful
        # result. See below where the matrix argument is converted into 
        # internal format.
        self._internal_timestamp = 1

        self._histograms = dict()

        # to save space, store the feature name as an id. This table
        # translates between the name and the id
        self._index_feature_to_id = dict()
        self._next_feature_index = 0

        self._histograms_debug = HISTOGRAMS_DEBUG
        if debug_override >= 0:
            self._histograms_debug = debug_override

        # for debug, track all timestamps saved in a given histogram
        self._histograms_timestamps = dict()

        if matrix is not None:
            # items on a window boundary get counted in both windows
            # so we make the window span 3 numbers and insert in the 
            # middle one
            self._sample_window = 2
            self._slide_window = 2
            self._internal_timestamp = 1
            for r in matrix:
                index_list = range(len(r))
                # in debug mode, randomize the feature insert order to verify
                # that we build the final matrix from the dict correctly
                if self._histograms_debug > 0:
                    random.shuffle(index_list)
                for c in index_list:
                    self.insert_one(c, self._internal_timestamp, value=r[c])
                self._internal_timestamp += 2

        # used by svm_calc. If more classes store things here
        # we'll want to use a dict and provide more generic support
        self._nu = -1

    def next_row(self):
        self._internal_timestamp += 2

    def insert_one(self, feature_value, timestamp, value = 1.0, 
                   use_internal_time = False):
        """
        Save one datapoint into all of the appropriate histograms
        An optional 'value' param allows us to insert a different quantity

        Call this multiple times, one for each feature.

        If using internal time, call next_row to move onto the next timestamp
        """
        if use_internal_time == True:
            timestamp = self._internal_timestamp
            self._sample_window = 2
            self._slide_window = 2

        assert timestamp >= 0
        assert self._sample_window > 0
        assert self._slide_window > 0

        try:
            feature_index_id = self._index_feature_to_id[feature_value]
        except KeyError:
            feature_index_id = self._next_feature_index
            self._index_feature_to_id[feature_value] = feature_index_id
            self._next_feature_index += 1

        # get the index of the most recent window this timestamp is in
        list_offset = int(timestamp / self._slide_window)
        list_offset_end_time = (list_offset * self._slide_window) \
            + self._sample_window

        # if the windows overlap, this entry can be in multiple windows
        # list_back is the number of additional windows it is in, not including
        # the initial one that list_offset describes
        list_back = int((list_offset_end_time - timestamp) / self._slide_window)

        if timestamp < self._start_sec:
            self._start_sec = timestamp
        if timestamp > self._end_sec:
            self._end_sec = timestamp

        while list_back >= 0:
            histogram_index = list_offset - list_back
            list_back -= 1
            if histogram_index < 0:
                continue

            try:
                one_histogram = self._histograms[histogram_index]
            except KeyError:
                one_histogram = dict()
                self._histograms[histogram_index] = one_histogram

            try:
                one_histogram[feature_index_id] += value
            except KeyError:
                one_histogram[feature_index_id] = value

            # store the timestamp at the index where it is being counted. 
            # Later we will verify that everything was stored in the expected 
            # place
            if self._histograms_debug > 0:
                try:
                    one_histogram_timestamps = \
                        self._histograms_timestamps[histogram_index]
                except KeyError:
                    one_histogram_timestamps = dict()
                    self._histograms_timestamps[histogram_index] \
                        = one_histogram_timestamps
                one_histogram_timestamps[timestamp] = 0

    def get_features(self):
        """
        Returns a list of feature names in sorted order
        """
        return sorted(self._index_feature_to_id.keys())

    def print_histograms(self):
        assert self._histograms_debug > 0

        print "Feature Names"
        for k in self._index_feature_to_id.keys():
            print k,":",self._index_feature_to_id[k]

        print "\nHistograms"
        for index in sorted(self._histograms.keys()):
            current_time = index * self._slide_window
            sys.stdout.write(str(current_time) + ":")
            one_histogram = self._histograms[index]

            for i in range(self._next_feature_index):
                try:
                    val = one_histogram[i]
                    sys.stdout.write(str(val) + " ")
                except:
                    sys.stdout.write('x ')
                    continue

            sys.stdout.write('\n')


    def get_histograms(self, features=None, start_sec=None, end_sec=None,
                       from_start_min=None, from_end_min=None,
                       drop_end_min=None, drop_start_min=None):
        """
        Return the histogram datastructure. If debugging is enabled
        it will first verify that all of the timestamps are in the correct
        histograms. 

        If an array of features is provided, the returned matrix will have
        its columns ordered as per the array. Any columns in the array that
        that don't exist in histogram will have zeros placed in

        start_sec = do not include data earlier than this
        end_sec = do not include data after this
        from_start_min = only include data from oldest histogram to this many
            minutes after that. Use for ignoring recent data. This operates on
            the original histogram start time, not the start_sec argument
        to_end_min = only include data from the most recent time to this many
            minutes back. Use for ignorning old data. This operates on the
            original histogram end time, not the end_sec argument
        drop_start_min = do not include data this many minutes from the start
        drop_end_min = do not include data this many minutes from the end

        The timestamps are lost during this conversion. The first row in the
        matrix will correspond to the window beginning at the lowest valid 
        timestamp in the histogram data. Each subsequent row will correspond
        to the next window after time is slid forward.
        """
        if features is not None:
            # this situation may be valid but offhand I can't think one.
            # I'd rather have this to detect bugs and remove it
            # later if we find out it is too restrictive
            assert(len(features) >= len(self._index_feature_to_id))

        # verify that the timestamps are all in the right places
        if self._histograms_debug > 0:
            # make sure every stored timestamp is in a valid slot
            all_timestamps = dict()
            for index in sorted(self._histograms.keys()):
                current_start = index * self._slide_window
                current_end = current_start + self._sample_window
                one_histogram_timestamps = self._histograms_timestamps[index]

                for one_timestamp in one_histogram_timestamps.keys():
                    if one_timestamp < current_start or \
                            one_timestamp > current_end:
                        raise Exception("Timestamp",one_timestamp,
                                        "at histogram index",index,
                                        "outside of window",current_start,
                                        "to",current_end)
                    all_timestamps[one_timestamp] = 0

            # make sure every slot has only valid timestamps
            for index in sorted(self._histograms.keys()):
                current_start = index * self._slide_window
                current_end = current_start + self._sample_window
                for one_timestamp_in_all in all_timestamps.keys():
                    if one_timestamp_in_all >= current_start and \
                            one_timestamp_in_all <= current_end:
                        try:
                            one_histograms_timestamps = \
                                self._histograms_timestamps[index]
                            one_histograms_timestamps[one_timestamp_in_all]
                        except KeyError:
                            raise Exception("Did not see timestamp",
                                            one_timestamp_in_all,
                                            "at histogram index",index,
                                            "window",current_start,
                                            "to",current_end)

        # these are indices starting from 0
        low = sorted(self._histograms.keys())[0]
        high = sorted(self._histograms.keys())[-1]
        feature_count =  self._next_feature_index
        if features is not None:
            feature_count = len(features)

        ret = np.zeros((high - low + 1, feature_count), np.float64)

        # self._histograms is keyed by timestamp relative to time=0
        # but when we put it in the return matrix we remap the lowest
        # index in self._histograms with data to ret[0]
        row = 0

        for i in range(low, high + 1):
            cur_time = self._sample_window + (i * self._slide_window)
            if start_sec is not None and cur_time < start_sec:
                continue
            if end_sec is not None and cur_time > end_sec:
                continue
            if from_start_min is not None and \
                    cur_time > self._start_sec + (from_start_min * 60):
                continue
            if from_end_min is not None and \
                    cur_time < self._end_sec - (from_end_min * 60):
                continue
            if drop_start_min is not None and \
                    cur_time < self._start_sec + (drop_start_min * 60):
                continue
            if drop_end_min is not None and \
                    cur_time > self._end_sec - (drop_end_min * 60):
                continue

            if i in self._histograms:
                one_histogram = self._histograms[i]
            else:
                row += 1
                continue

            if features == None:
                index = 0
                for feat in sorted(self._index_feature_to_id.keys()):
                    f_offset = self._index_feature_to_id[feat]
                    if f_offset in one_histogram:
                        ret[row][index] = one_histogram[f_offset]
            else:
                count = 0
                for f in sorted(features):
                    if f in self._index_feature_to_id:
                        feature_offset = self._index_feature_to_id[f]
                        if feature_offset >= len(one_histogram):
                            # this happens if we had to grow the matrix
                            # dimensions to match another histogram we're
                            # testing against, so just set the value to zero
                            ret[row][count] = 0
                        else:
                            ret[row][count] = one_histogram[feature_offset]
                    else:
                        ret[row][count] = 0
                    count += 1
                
            row += 1

        ### adjust the ret to account for any rows we discarded
        return ret[:row]

    @staticmethod
    def get_fake_histogram_train():
        """
        For testing purposes
        Generate a dataset where a lot of data is sent to 10.0.0.2
        using a window size of 60 seconds and a slide window of 10 seconds
        """
        ret = Histograms(60, 10)

        for t in range(1200):
            for i in range(20 + random.randint(0,10)):
                ret.insert_one("10.0.0.2", t)

        return ret

    @staticmethod
    def get_fake_histogram_test():
        """
        For testing purposes
        Generate a dataset that stats to look like get_fake_histogram_train
        then changes to traffic sent to 3 IP addresses then returns to
        normal traffic again
        """
        ret = Histograms(60, 10)

        for t in range(2000,2060):
            for i in range(20):
                ret.insert_one("10.0.0.2", t)
        for t in range(2060,2110):
            for i in range(10):
                ret.insert_one("10.0.0.2", t)
                ret.insert_one("10.0.0.1", t)
                ret.insert_one("10.0.0.3", t)
        for t in range(2110,2200):
            for i in range(20):
                ret.insert_one("10.0.0.2", t)

        return ret
