__author__ = 'adam'

import urllib
import time
from subprocess import Popen
import shlex
import os
import fusekiutils
import qudt4dt


fuseki = fusekiutils.LaunchFuseki()

try:
    fuseki_url = "http://localhost:3030"
    fuseki_upload_url = fuseki_url + '/qudt4dt/upload'

    barb = qudt4dt.Barbara("http://localhost:3030")
    print barb.get_server_status()
    print ""


    print "Get Unit Class"
    print barb.get_unit_class("Unit1")
    print ""

    print "Get Units in Class"
    print barb.get_units_in_class("Unit1")
    print ""

    print "Get Units in Same Class"
    print barb.get_units_in_same_class("Unit1")
    print ""

    print "Convert Value"
    print barb.convert_value("Unit1","Unit2",3.4)

finally:
    print ""
    print "Terminating fuseki..."
    fuseki.terminate()
    print "done"
    print ""