import csv
import sys
import re
class UnitMapping(object):
    """
    Create a UnitMapping from 3rd part unit lib to QUDT
    """
    
    def __init__(self, sourceFile, objFile, libName = None):
        """
        init XML template
        """
        self.reader = csv.reader(file(sourceFile,'rU'))
        if libName == None: self.libName = re.search("([^/]+?)\.xml", objFile).group(1)
        print self.libName
        self.objFile = objFile
        self.sourceClassURI = '' 
        self.objClassURI = ''
        self.head = '''<?xml version="1.0"?>

<!DOCTYPE rdf:RDF [
    <!ENTITY ontology "http://qudt4dt.org/ontology#" >
    <!ENTITY owl "http://www.w3.org/2002/07/owl#" >
    <!ENTITY xsd "http://www.w3.org/2001/XMLSchema#" >
    <!ENTITY rdfs "http://www.w3.org/2000/01/rdf-schema#" >
    <!ENTITY rdf "http://www.w3.org/1999/02/22-rdf-syntax-ns#" >
    <!ENTITY modelica "http://modelica.org/msl/SIUnits/vocabulary#" >
]>


<rdf:RDF xmlns="http://www.qudt4dt.org/ontology/{libName}#"
     xml:base="http://www.qudt4dt.org/ontology/{libName}"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
     xmlns:owl="http://www.w3.org/2002/07/owl#"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:ontology="http://qudt4dt.org/ontology#">
    <owl:Ontology rdf:about="http://www.qudt4dt.org/ontology/{libName}">
        <owl:imports rdf:resource="{sourceClassURI}"/>
	<owl:imports rdf:resource="{objClassURI}"/>
        <owl:imports rdf:resource="http://qudt4dt.org/ontology"/>
    </owl:Ontology>
    
'''
        self.body='''
    <!-- {sourceUnitURI} -->

    <rdf:Description rdf:about="{sourceUnitURI}">
        <ontology:equivalentOf rdf:resource="{objUnitURI}"/>
    </rdf:Description>

'''
        
    def __getClassURI(self):
        firstLn = self.reader.next()
        self.sourceClassURI = firstLn[0]
        self.objClassURI = firstLn[1]

    def __createOWL(self):
        filename = self.objFile
        classname = self.libName
        s_uri = self.sourceClassURI
        o_uri = self.objClassURI
        with open(filename,'w') as f:
            f.write(self.head.format(libName = self.libName,sourceClassURI = s_uri,objClassURI = o_uri))
            for line in self.reader:
                s_unit = s_uri + line[0]
                o_unit = o_uri + line[1]
                f.write(self.body.format(sourceUnitURI = s_unit, objUnitURI = o_unit))
            f.write("</rdf:RDF>")
            
    def run(self):
        self.__getClassURI()
        self.__createOWL()


def createMapping(sourceFile, objFile, libName = None):
    mapping = UnitMapping(sourceFile, objFile, libName)
    mapping.run()

