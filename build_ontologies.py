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

def LaunchFuseki():
    fuseki_dir = os.getcwd() + "/jena-fuseki-0.2.7"
    fuseki_executable = fuseki_dir + "/fuseki-server"
    f_log = open("fuseki.log","w")
    fuseki = Popen( args=shlex.split("-q --update --loc=../fuseki-data /qudt4dt"),
                    executable=fuseki_executable,
                    cwd=fuseki_dir,
                    stdout=f_log)
    f_log.close()

    PollFusekiLaunch()

    return fuseki

def PollFusekiLaunch():
    while True:
        try:
            urllib.urlopen(fuseki_url)
            return
        except IOError:
            print "polling..."
            time.sleep(1)

print "Launching fuseki..."
fuseki = LaunchFuseki()
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


print "Loading ontologies into Fuseki..."
LoadDirectoryOfOWLFiles('qudt-owl')
LoadDirectoryOfOWLFiles('modelica')
print "done"

print ""

fuseki.terminate()
print "finished"