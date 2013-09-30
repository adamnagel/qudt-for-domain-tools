#!/usr/bin/env python
import re
import sys
import os
sys.path.append(os.path.abspath('modelica'))
import MSL2OWL
from subprocess import Popen
import shlex
import urllib
import shutil
import time
import glob
import requests
import fusekiutils
import qudt4dt

p_ScriptPathRoot = os.path.dirname(__file__)

### Generate Modelica Unit Ontology
p_SIUnits = os.path.join(p_ScriptPathRoot,'modelica/SIunits.mo')
p_ModelicaUnitOntology = os.path.join(p_ScriptPathRoot,'modelica/modelica-individuals.xml')
print "Generating Modelica Unit ontology"
MSL2OWL.GenerateOWLIndividualFile(p_SIUnits,p_ModelicaUnitOntology)
print "complete"

print ""

### start jena-fuseki and seed database ###
print "Cleaning fuseki database"
fuseki_data_path = os.getcwd() + '/fuseki-data'
shutil.rmtree(fuseki_data_path)
os.makedirs(fuseki_data_path)
print "done"

print ""

fuseki_url = "http://localhost:3030"
fuseki_upload_url = fuseki_url + '/qudt4dt/upload'

print "Launching fuseki..."
fuseki = fusekiutils.LaunchFuseki()
print "done"

print ""

def LoadDirectoryOfOWLFiles(path):
    # Load QUDT data
    ap_XMLFiles = glob.glob(path + '/*.xml')
    for filename in ap_XMLFiles:
        # Skip Protege's "catalog" files
        if filename.find('catalog-') != -1:
            continue

        path_File = filename
        print 'Loading', filename
        file_AsDict = {'file': open(path_File,'rb')}
        r = requests.post(fuseki_upload_url, files=file_AsDict)

        if r.status_code != 200:
            print "EXCEPTION loading DB: ", r.status_code

def CreateOWLFilesFromCSV(sourceFilePath ,objFilePath):
    s_file = re.search('[^/]+?\.csv',sourceFilePath).group()
    o_file = re.search('[^/]+?\.xml',objFilePath).group()
    print 'coverting %s to %s' %(s_file, o_file)
    qudt4dt.unit_mapping.createMapping(sourceFilePath, objFilePath)
            
try:
    print "Creating ontologies from CSV file..."
    CreateOWLFilesFromCSV('modelica/mapping-to-qudt.csv','modelica/modelica-qudt.xml')
    print "Loading ontologies into Fuseki..."
    LoadDirectoryOfOWLFiles('qudt-owl')
    LoadDirectoryOfOWLFiles('modelica')
    LoadDirectoryOfOWLFiles('ontologies')
    print "done"

finally:
    print ""
    print "Terminating fuseki..."
    fuseki.terminate()
    print "done"
    print ""

print "finished"
