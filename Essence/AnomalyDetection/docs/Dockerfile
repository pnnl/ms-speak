FROM ubuntu:15.10

RUN apt-get -y update 
# Later when we install from setup.py it doesn't handle dependencies well
# so we install some modules now and later we upgrade them to the needed versions
RUN apt-get -y install git python python-setuptools libblas-dev liblapack-dev libatlas-base-dev gfortran python-dev python-numpy python-scipy python-flask

RUN cd /tmp && /usr/bin/git clone https://github.com/dpinney/essence.git

#RUN cd /tmp/AnomalyDetection && /usr/bin/git checkout twong/python
RUN cd /tmp/essence/AnomalyDetection/python/ && python setup.py install

WORKDIR /tmp/essence/AnomalyDetection/python/anomalydetection
CMD ./daemon_service.py --docker_mode

