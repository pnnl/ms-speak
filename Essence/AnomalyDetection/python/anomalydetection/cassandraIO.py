from cassandra.cluster import Cluster
from constants import *
from histograms import Histograms

import datetime
import time

class CassandraIO():
    """
    This module reads the packet info from the Cassandra database and returns
    a histogram of the data. As of this writing, Cassandra is not suitable
    for our needs and the plan is to move to a relational database so not a lot
    of care is being put into this module
    """

    def __init__(self, keyspace, table, hostname="127.0.0.1"):
        self._cluster = Cluster([hostname])
        self._session = self._cluster.connect(keyspace)
        self._table = table

    def get_histogram(self, sample_window_sec, slide_window_sec, 
                      filter_name, filter_value, features_keep):
        """
        filter_name and filter_value is to define one thing that we're making
        histograms for. For example, source_addr = 10.0.0.1 would build
        histograms for all packets originating from 10.0.0.1 and with whatever
        desired features
        
        features_keep is a tuple of strings representing field names in the 
        database. If the feature is
        inside the text_values map, just pass in the key for the map and this
        code will automatically try the various maps looking for it. We 
        assume the same key name doesn't appear in multiple maps

        As a result the ret dict contains a flat keyspace
        """
        ret = Histograms(sample_window_sec, slide_window_sec)

        self._result = self._session.execute("SELECT * FROM " + self._table)

        temp_data = dict()

        count = 0
        for res in self._result:
            count += 1

            features = ()
            res_dict = res._asdict()

            if res_dict[filter_name] != filter_value:
                continue

            if res.source_addr in temp_data:
                temp_data[res_dict["dest_addr"]] += 1
            else:
                temp_data[res_dict["dest_addr"]] = 0

            for f in features_keep.split(","):
                f = f.strip()
                if f in res_dict:
                    features = features + (res_dict[f],)
                elif f in res_dict["text_values"]:
                    features = features + (res_dict["text_values"][f],)
                else:
                    raise Exception("Could not find field " + f)

            sec = time.mktime(res.time_stamp.timetuple())
            
            ret.insert_one(','.join(map(str, features)), sec)
        return ret
        

    def close(self):
        self._session = None
        self._cluster.shutdown()
        self._cluster = None
