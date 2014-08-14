.. _parser:

=========================
Settings
=========================

This is the basic module for performing settings options.It allows us to alter the behavior of the workflows
and even entire spider.According to the situation one should set the Request settings ,Log settings and Crawl settings.
There are three main settings classes in defaultsettings module.We can discuss each of them here.

-----------------
RequestSettings 
-----------------
The main settings under Requestsettings are:

    * `AUTOTHROTTLE`_
    * `CACHE`_
    * `TIMEOUT`_
    * `DELAY`_
    * `MIN_DELAY`_
    * `MAX_DELAY`_
    * `PROXIES`_
    * `COOKIE`_
    * `MAX_REDIRECTS`_


AUTOTHROTTLE
------------
This is a setting for automatically throttling crawling speed based on
load of both the Scrapy server and the website you are crawling.

by default 

    AUTOTHROTTLE = False

Enable AutoThrottle debug mode which will display stats on every response received,
so you can see how the throttling parameters are being adjusted in real time.

CACHE
-----
If this setting is set True then all the urls the spider process will be cached and used
if running the same spider nexttime

by default

   CACHE = False
   
TIMEOUT
-------
The amount of the time the spider waits for yielding its next Request.
by default 

    TIMEOUT = 5

DELAY
-----
If enabled, spider will wait for a random amount of time (between 0.5 and 1.5 * DELAY)
while fetching requests from the same website.
by default

    DELAY = 0.5
    
MIN_DELAY
---------
It is similar to delay but it specifies minimum time to wait is specified.
by default    
    
    MIN_DELAY = 0.5
    
MAX_DELAY
---------
It is the maximum time needed to wait for a connection.If MAX_DELAY is crossed then connection will be reset.
by default

    MAX_DELAY = 60

PROXIES
-------
This setting enables us to use proxies in case of blocking by the target websites.This is a list and
it can be initialized with many no of working proxies.


COOKIE
------
cookie enables us to store the cookies of server in the system that running the spider.
by default

    COOKIE = True
    
MAX_REDIRECTS
-------------
Defines the maximum times a request can be redirected. After this maximum the request’s response is returned as is. 
We used Firefox default value for the same task.
by default

    MAX_REDIRECTS = 1
    
---------------
Crawlsettings
---------------
The main settings under Crawlsettings are:
    
    * `TIME_ZONE`_ 
    * `RESUME`_ 
    * `MAX_RETRY`_ 
    * `REDIS_URL`_
    * `REDIS_PORT`_ 
    * `REDIS_DB`_
    
TIME_ZONE
---------
It sets the time zone in which the current system is working.Generally it fetch information from the 
host system and interprets time according to timezone.
by default

    TIME_ZONE = 'UTC'
    
RESUME
------
This option sets the spider resuming property.If after the session loss whether spider restarts or it should
be continued deapending on this setting.
by default

    RESUME = FALSE
    
MAX_RETRY
---------

If connection is been timed out,then this option specifies how many no of times the spider process
the URL.
by default

    MAX_RETRY = 3
    
REDIS_URL
---------
This specifies the location address of the redis queue on which spider is activated.It is local host if spider and queue 
are on same machine.IP address if redis queue is located on remote system
by default

    REDIS_URL = 'localhost'
    
REDIS_PORT
----------
port no of the redis server used by spider for storing URL.
by default 

    REDIS_PORT = 6379
    
REDIS_DB
--------
It is the ID of the database which is used
by default 

    REDIS_DB = 1

----------------
Spidersettings
----------------
The settings in this are:
DB
---
This controlls the database selection whether db is maintained on localhost or remote server.
by default 

    DB = None



