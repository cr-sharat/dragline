.. _intro-install:

==================
Installation guide
==================

Pre-requisites
===============

The installation steps assume that you have the following things installed:

* `Python`_ 2.7
* `lxml`_. Most Linux distributions ships prepackaged versions of lxml. Otherwise refer to http://lxml.de/installation.html
* `redis`_.Redis server need to be installed to run the dragline.Please refer to http://redis.io/download

for Ubuntu users::

    sudo apt-get install libxml2-dev libxslt-dev python-dev zlib1g-dev redis-server

Installing Dragline
===================

To install using pip::

    sudo pip install --pre dragline


.. _Python: http://www.python.org
.. _pip: http://www.pip-installer.org/en/latest/installing.html
.. _lxml: http://lxml.de/
.. _redis: http://redis.io/
