__author__ = 'adam'

import time
from subprocess import Popen
import shlex
import os
import urllib
import sys

def LaunchFuseki():
    if IsFusekiRunning('http://localhost:3030'):
        print "Jena-Fuseki is already running"
        return

    fuseki_dir = os.path.join(os.path.abspath(os.getcwd()), 'jena-fuseki')
    fuseki_data = os.path.join('..', 'fuseki-data')
    f_log = open("fuseki.log", "w")

    if sys.platform == 'win32':
        fuseki_executable = os.path.join(fuseki_dir, 'fuseki-server.bat')
        args = '%(exec)s -q --update --loc=%(data)s /qudt4dt' % {'exec': fuseki_executable, 'data': fuseki_data}
        fuseki = Popen(args=args,
                       cwd=fuseki_dir,
                       stdout=f_log)
    else:
        fuseki_executable = os.path.join(fuseki_dir, 'fuseki-server')
        args = '%(exec)s -q --update --loc=%(data)s /qudt4dt' % {'exec': fuseki_executable, 'data': fuseki_data}
        fuseki = Popen(args=shlex.split(args), cwd=fuseki_dir, stdout=f_log)


    f_log.close()
    PollFusekiLaunch("http://localhost:3030")

    print "Jena-Fuseki now running (pid %(pid)s)" % {'pid': fuseki.pid}
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