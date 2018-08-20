from setuptools import setup


setup(
      name='anomalydetection',
      version='0.0.1',
      author = 'Terrence Wong',
      author_email = 'tw@andrew.cmu.edu', 
      packages = ['anomalydetection'],
      package_dir = {'anomalydetection': 'anomalydetection'},
      url="http://www.github.com",
      install_requires = ["cassandra-driver >= 3.0.0", 
                          "Flask-Bootstrap >= 3.3.5.7",
                          "Flask-RESTful >= 0.3.5",
                          "flask-nav >= 0.5",
                          "coverage >= 4.0",
                          "nose >= 1.3.7",
			  "numpy >= 1.10.4",
                          "scipy >= 0.17.0",
                          "scikit-learn >= 0.17",
                          "requests >= 2.9.1"],

      include_package_data = True,
      )
