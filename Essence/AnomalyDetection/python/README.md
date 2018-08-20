AnomalyDetection python
=======================

For more about Anomaly Detection, see the [parent doc](..)

As of this writing, this code is tested internally under both supervised and
unsupervised learning. It has also been run against an existing
dataset but the anomaly reporting to Essence has not.

## Running the current release with Docker (easiest way)
To run the most recent release with the REST service exported
to port 5000, install Docker, then simply run:
 * docker run -p 5000:5000 autonlab/anomalydetection-powergrid

## Building a new Docker container 
To build and run the Docker container:
 * cd AnomalyDetection/docs
 * docker build --force-rm -t anom-detect .   <--note the trailing period
 * docker run -p 5000:5000 anom-detect

## Running without Docker
To run the code without Docker, install the dependencies listed
in docs/Dockerfile and python/setup.py
 * use your package manager to install the dependencies listed in Dockerfile
 * sudo python python/setup.py install
 * cd AnomalyDetection/python/anomalydetection
 * ./daemon_service.py

## Exercising the code
To exercise the API once the code is running:
* http://127.0.0.1:5000/getfakedata
* http://127.0.0.1:5000/test?train_id=0&test_id=1

## Running tests
 * cd AnomalyDetection/python/anomalydetection
 * nosetests-2.7 (nose is one of the dependencies in setup.py so this should be installed)



