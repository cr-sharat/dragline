=======================
Dragline shell Tutorial
=======================

For decreasing the testing effort,a shell is designed for dragline to view the content of a dragline request object,response and viewing the response in browser.The Dragline shell is an interactive shell where you can try and debug your scraping code very quickly, without having to run the spider. It’s meant to be used for testing data extraction code, but you can actually use it for testing any kind of code as it is also a regular Python shell.It avoids creating the spider each time for very simple scraping tasks.

Launch the shell
================

You can launch the dragline shell by typing the following command.An URL is supplied in the command upon which testing proceeds::

        $ dragline-shell <url>
        
where url is the url required to scrape


Implementing the shell
======================

The Dragline shell is just a regular Python console which provides some additional shortcut functions for convenience

Shortcuts
=========

* ``shelp()``: print a list of available shortcuts.
* ``fetch(url)``: Fetches a fresh response from given URL
* ``view(response)``: Opens a webbrowser and makes response visible for inspection

Dragline objects
================
* ``parser``: It is the crawling object that has methods for scraping

* ``request``: Request object of the last fetched page

* ``response``: Response objects with body content to test


Being familiar through an example
=================================
Here’s an example of a typical shell session where we start by scraping the http://www.python.org page, and then proceed to scrape the page https://archive.org. 
First we launch dragline-shell by following command::
    
    $ dragline-shell http://www.python.org
    
Then, the shell fetches the URL (using the Dragline downloader) and prints the list of available objects and useful shortcuts::

    [d] Available Dragline objects:
    [d]   parser    <Element html at 0xb406c8c4>
    [d]   request    <GET http://www.python.org>
    [d]   response   <200 http://www.python.org>
    [d] Useful shortcuts: ## Override methods in Cmd object ##
    [d]   shelp()           Shell help (print this help)
    [d]   fetch(url)  Fetch from given URL and update local objects
    [d]   view(response)    open response in a browser and saves the view as a static file
    
we can then start using the objects::

    [In]> parser.xpath('//title/text()')[0]
    'Welcome to Python.org'
    [In]> fetch('http://archive.org')
    <Element html at 0x9277f54>
    [d] Available Dragline objects:
    [d]   parser    <Element html at 0xb406c8c4>
    [d]   request    <GET http://archive.org>
    [d]   response   <200 http://archive.org>
    [d] Useful shortcuts: ## Override methods in Cmd object ##
    [d]   shelp()           Shell help (print this help)
    [d]   fetch(url)  Fetch from given URL and update local objects
    [d]   view(response)    open response in a browser and saves the view as a static file

    [In]> parser.xpath('//title/text()')[0]
    Internet Archive: Digital Library of Free Books, Movies, Music & Wayback Machine
    [In]> response
    <200:https://archive.org>
    
You can also open the response in your web browser and see if it’s the response you were expecting::

    [In]> view(response)
    True

Quitting the shell
==================
just hit the CTRL+D to quit the dragline shell if testing was completed. 






    