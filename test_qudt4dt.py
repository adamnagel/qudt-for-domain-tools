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
    uc = barb.get_unit_class("http://qudt.org/vocab/unit#Inch")[0]
    print uc
    print ""

    print "Units in Class:"
    units_in_class = barb.get_units_in_class(uc)
    for uic in units_in_class:
        print uic
    print ""

    print "Units in Same Class:"
    units_in_same_class = barb.get_units_in_same_class("http://qudt.org/vocab/unit#Inch")
    for uisc in units_in_same_class:
        print uisc
    print ""

    print "Convert Value"
    print barb.convert_value("http://qudt.org/vocab/unit#Inch","http://qudt.org/vocab/unit#Meter",3.4)

finally:
    print ""
    print "Terminating fuseki..."
    fuseki.terminate()
    print "done"
    print ""
