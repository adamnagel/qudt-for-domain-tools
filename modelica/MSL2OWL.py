#!/usr/bin/env python
import re
import json

def ExtractUnitsFromJson(jsonSIUnitsFile):
    ''' Read contents of SIunits json file '''
    f = open(jsonSIUnitsFile,'r')
    jsonSIUnits = json.load(f)
    
    mapping = {'quantity':'UnitQuantity', 'unit':'UnitUnit',
               'displayUnit':'UnitDisplayUnit', 'min':'UnitMin', 
               'start':'UnitStart'}
    for unit in jsonSIUnits:
       # print unit
        if not unit['class'] == 'type': continue
        result = {}
        result['ClassPath'] = unit['name']
        unitName = re.match('.*?([^\.]+)$',result['ClassPath']).group(1)
        if unit['modifiers']:
            for k,v in unit['modifiers'].iteritems():
                m = mapping.get(k,None)
                if not m == None:
                    value = v
                    value = re.compile('["= ]').sub('', value)
                    value = re.compile('"').sub('', value)
                    result[m] = value
                    
        yield (unitName,result)
    
    f.close()
        
     

def GenerateOWLNode(s_Name, d_Unit):
    xml_OWLNode = '\n  <NamedIndividual rdf:about="http://modelica.org/msl/SIUnits/individuals#' + s_Name + '">\n'
    xml_OWLNode += '    <rdf:type rdf:resource="&modelica;ModelicaUnitClass"/>\n'
    for key,value in d_Unit.iteritems():
        xml_OWLNode += '    <modelica:' + key + ' rdf:datatype="&xsd;string">' + value + "</modelica:" + key + ">\n"
    xml_OWLNode += '  </NamedIndividual>\n'
    
    return xml_OWLNode

def GenerateOWLIndividualFileContent(d_Units):
    xml_Header = '''<?xml version="1.0"?>

<!DOCTYPE rdf:RDF [
    <!ENTITY owl "http://www.w3.org/2002/07/owl#" >
    <!ENTITY xsd "http://www.w3.org/2001/XMLSchema#" >
    <!ENTITY rdfs "http://www.w3.org/2000/01/rdf-schema#" >
    <!ENTITY modelica "http://modelica.org/msl/SIUnits/vocabulary#" >
    <!ENTITY rdf "http://www.w3.org/1999/02/22-rdf-syntax-ns#" >
]>
    <rdf:RDF xmlns="http://www.w3.org/2002/07/owl#"
     xml:base="http://www.w3.org/2002/07/owl"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
     xmlns:modelica="http://modelica.org/msl/SIUnits/vocabulary#"
     xmlns:owl="http://www.w3.org/2002/07/owl#"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
    <Ontology rdf:about="http://modelica.org/msl/SIUnits/individuals">
        <imports rdf:resource="http://modelica.org/msl/SIUnits/vocabulary#"/>
    </Ontology>'''
    
    xml_Footer = '''
</rdf:RDF>'''
    
    xml_Final = xml_Header
    for key, value in d_Units:
        xml_Final += GenerateOWLNode(key,value)
    xml_Final += xml_Footer
    
    return xml_Final

def GenerateOWLIndividualFile(jsonSIUnitsFile,OutputFile):
    d_TypeStatements = ExtractUnitsFromJson(jsonSIUnitsFile)
    xml_IndividualFile = GenerateOWLIndividualFileContent(d_TypeStatements)
    with open(OutputFile,'w') as f:
        f.write(xml_IndividualFile)


if __name__ == '__main__':
    GenerateOWLIndividualFile('modelica_units.json','example.xml')
