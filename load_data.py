__author__ = 'adam'
import json
import requests
import os
import urllib
import glob


# Establish key URLS for SPARQL database
url_base = 'http://localhost:3030'
url_upload = url_base + '/ds/upload'
url_query = url_base + '/ds/query?'
url_update = url_base + '/ds/update?'

def LoadDirectoryOfOWLFiles(path):
    # Load QUDT data
    ap_XMLFiles = glob.glob(path + '/*.xml')
    for filename in ap_XMLFiles:
        path_File = filename
        print 'Loading', filename
        file_AsDict = {'file': open(path_File,'rb')}
        r = requests.post(url_upload, files=file_AsDict)

        if r.status_code != 200:
            print "EXCEPTION loading DB: ", r.status_code

LoadDirectoryOfOWLFiles('qudt-owl')
LoadDirectoryOfOWLFiles('modelica')

