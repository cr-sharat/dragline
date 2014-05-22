import os
import inspect
import zipfile
import sys
from json import dumps
from httplib2 import Http
from urllib import urlencode
import base64
import subprocess
from os.path import normpath, basename
from runner import load_module


h = Http()


def zipdir(path, zip):
    for root, dirs, files in os.walk(path):
        for file in files:
            print file
            zip.write(os.path.join(root, file))


def deploy(url, username, password, foldername, spider_website=None):
    # check whether the folder is a spider
    if not "main.py" in os.listdir(foldername):
        return "Not a valid spider"

    # check if the main.py contain a spider class
    module = load_module(foldername, "main")
    # check if main.py contain a spider class
    try:
        spider = getattr(module, "Spider")
    except Exception as e:
        return "Spider class not found"

    if not inspect.isclass(spider):
        return "Spider class not found"

    # create a spider object and check whether it contain required attributes
    spider_object = spider(None)

    try:
        if spider_object._name and spider_object._start and spider_object._allowed_urls_regex and spider_object.parse:
            spider_name = spider_object._name
        else:
            return "required attributes not found in spider"

    except Exception as e:
        print e
        return "Spider deploying failed"

    # zip the folder
    chfold = os.path.split(os.path.abspath(foldername))[0]
    os.chdir(chfold)
    comm = ["zip", "-r", "/tmp/%s.zip" %
            spider_name, ".", "-i", basename(normpath(foldername)) + "/*.py"]
    subprocess.call(comm)
    zipf = base64.encodestring(open("/tmp/%s.zip" % spider_name, "rb").read())
    post_data = {'username': username, 'password': password, 'name':
                 spider_name, 'zipfile': zipf, 'website': spider_website}
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    resp, content = h.request(
        url, "POST", body=urlencode(post_data), headers=headers)
    # read zip file
    return content


if __name__ == "__main__":
    print deploy("http://192.168.0.20:8000/deploy/", "shimil",
                 "passme", "../../samplespider/NetaPorter/")