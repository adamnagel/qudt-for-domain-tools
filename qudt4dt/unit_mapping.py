import csv
import sys

class UnitMapping(object):
    """
    Create a UnitMapping from 3rd part Unit lib to QUDT
    """
    
    def __init__(self, fileName, sourceClassName):
        """
        Default XML template
        """
        self.reader = csv.reader(file(fileName,'rU'))
        self.sourceClassName = sourceClassName
        self.sourceClassURI = '' 
        self.destClassURI = ''
        self.head = '''
<?xml version="1.0"?>


<!DOCTYPE rdf:RDF [
    <!ENTITY ontology "http://qudt4dt.org/ontology#" >
    <!ENTITY owl "http://www.w3.org/2002/07/owl#" >
    <!ENTITY xsd "http://www.w3.org/2001/XMLSchema#" >
    <!ENTITY rdfs "http://www.w3.org/2000/01/rdf-schema#" >
    <!ENTITY rdf "http://www.w3.org/1999/02/22-rdf-syntax-ns#" >
]>


<rdf:RDF xmlns="http://www.qudt4dt.org/ontology/{sourceClassName}-to-qudt#"
     xml:base="http://www.qudt4dt.org/ontology/{sourceClassName}-to-qudt"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
     xmlns:owl="http://www.w3.org/2002/07/owl#"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:ontology="http://qudt4dt.org/ontology#">
    <owl:Ontology rdf:about="http://www.qudt4dt.org/ontology/{sourceClassName}-to-qudt">
        <owl:imports rdf:resource="{sourceClassURI}"/>
        <owl:imports rdf:resource="http://qudt4dt.org/ontology"/>
    </owl:Ontology>
    
'''
        self.body='''
    <!-- {sourceUnitURI} -->

    <rdf:Description rdf:about="{sourceUnitURI}">
        <ontology:equivalentOf rdf:resource="{destUnitURI}"/>
    </rdf:Description>

'''
        
    def __getClassURI(self):
        firstLn = self.reader.next()
        self.sourceClassURI = firstLn[0]
        self.destClassURI = firstLn[1]

    def __createOWL(self):
        filename = self.sourceClassName + " to qudt.xml"
        classname = self.sourceClassName
        s_uri = self.sourceClassURI
        d_uri = self.destClassURI
        with open(filename,'w') as f:
            f.write(self.head.format(sourceClassName = classname,sourceClassURI = s_uri))
            for line in self.reader:
                s_unit = s_uri + line[0]
                d_unit = d_uri + line[1]
                f.write(self.body.format(sourceUnitURI = s_unit, destUnitURI = d_unit))
            f.write("</rdf:RDF>")
            
    def run(self):
        self.__getClassURI()
        self.__createOWL()


def createMapping(filename, classname):
    mapping = UnitMapping(filename, classname)
    mapping.run()

    
if __name__ == '__main__':
    #filename = sys.argv[1]
    createMapping("mapping-to-qudt.csv","modelica")
