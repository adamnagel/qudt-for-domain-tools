__author__ = 'adam'
import os
import shutil
import urllib
import zipfile
import tarfile

## Delete and create 'qudt-owl' fresh
shutil.rmtree('qudt-owl')
os.makedirs('qudt-owl')

l_owlfiles = ['http://www.linkedmodel.org/1.0/schema/dtype',
              'http://qudt.org/1.1/schema/dimension',
              'http://qudt.org/1.1/schema/quantity',
              'http://qudt.org/1.1/schema/qudt',
              'http://www.linkedmodel.org/1.2/schema/vaem',
              'http://voag.linkedmodel.org/1.0/schema/voag',
              'http://qudt.org/1.1/vocab/dimensionalunit',
              'http://qudt.org/1.1/vocab/dimension',
              'http://qudt.org/1.1/vocab/quantity',
              'http://qudt.org/1.1/vocab/unit']

print "===== Downloading QUDT OWL files ====="
for url in l_owlfiles:
    localfilename = url.rsplit('/', 1)[1] + '.xml'
    localfilepath = os.path.join('qudt-owl', localfilename)
    print url + ": " + localfilepath
    urllib.urlretrieve(url, localfilepath)
print ""

print "===== Downloading OpenMDAO Unit INI file ====="
path_mdaoINI = 'openMDAO/unitLibdefault.ini'
print "downloading..."
urllib.urlretrieve(
    'https://raw.github.com/OpenMDAO/OpenMDAO-Framework/master/openmdao.units/openmdao/units/unitLibdefault.ini',
    path_mdaoINI)

# Our scripts expect no system-specific line endings
file_mdaoINI = open(path_mdaoINI)
content_mdaoINI = file_mdaoINI.readlines()
file_mdaoINI.close()

file_mdaoINI = open(path_mdaoINI, "w")
file_mdaoINI.writelines(content_mdaoINI)
file_mdaoINI.close()
print ""


print "===== Downloading Requests v1.2.3 ====="
if os.path.exists('requests'):
    shutil.rmtree('requests')
print "downloading..."
urllib.urlretrieve('https://github.com/kennethreitz/requests/archive/v1.2.3.zip',
                   'requests-1.2.3.zip')
print "extracting..."
with zipfile.ZipFile('requests-1.2.3.zip', 'r') as zip_requests:
    zip_requests.extractall()
    os.rename('requests-1.2.3', 'requests')
os.remove('requests-1.2.3.zip')
print ""


print "===== Downloading Jena Fuseki server ====="
path_jena_fuseki = 'jena-fuseki'
shutil.rmtree(path_jena_fuseki)

print "downloading..."
path_fuseki_tar_gz = 'jena-fuseki.tar.gz'
urllib.urlretrieve('http://www.apache.org/dist/jena/binaries/jena-fuseki-1.0.0-distribution.tar.gz', path_fuseki_tar_gz)

print "extracting..."
with tarfile.open(path_fuseki_tar_gz, 'r:gz') as targz_fuseki:
    targz_fuseki.extractall()
    os.rename('jena-fuseki-1.0.0','jena-fuseki')
os.remove(path_fuseki_tar_gz)