.. _settings:

=========================
Settings
=========================


AUTOTHROTTLE
------------
This is a setting for automatically throttling crawling speed based on
load of both the Scrapy server and the website you are crawling.

by default 

    AUTOTHROTTLE = False

TIMEOUT
-------
The amount of the time the spider waits for yielding its next Request.
by default 

    TIMEOUT = 5

MIN_DELAY
---------
by default

    MIN_DELAY = 0.5

MAX_DELAY
---------
by default

    MAX_DELAY = 60

PROXIES
-------
This setting enables us to use proxies in case of blocking by the target websites.This is a list and
it can be initialized with many no of working proxies.

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




