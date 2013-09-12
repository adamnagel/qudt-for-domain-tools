__author__ = 'adam'

import time
from subprocess import Popen
import shlex
import os
import urllib

def LaunchFuseki():
    fuseki_url = "http://localhost:3030"

    fuseki_dir = os.getcwd() + "/jena-fuseki-0.2.7"
    fuseki_executable = fuseki_dir + "/fuseki-server"
    f_log = open("fuseki.log","w")
    fuseki = Popen( args=shlex.split("-q --update --loc=../fuseki-data /qudt4dt"),
                    executable=fuseki_executable,
                    cwd=fuseki_dir,
                    stdout=f_log)
    f_log.close()

    PollFusekiLaunch("http://localhost:3030")

    return fuseki

def PollFusekiLaunch(fuseki_url):
    while True:
        if IsFusekiRunning(fuseki_url):
            return
        else:
            print "polling..."
            time.sleep(1)

def IsFusekiRunning(fuseki_url):
        try:
            urllib.urlopen(fuseki_url)
            return True
        except IOError:
            return False