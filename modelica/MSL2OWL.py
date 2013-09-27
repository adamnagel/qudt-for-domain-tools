'''
Created on Aug 13, 2013

@author: adam
'''

import re
import json

def ExtractUnitsFromMSL(p_mslSIUnits):
    # Read contents of SIunits.mo
    f_mslSIUnits = open(p_mslSIUnits,'r')
    as_mslSIUnits_ = f_mslSIUnits.readlines()
    f_mslSIUnits.close()
        
    # Remove comment lines
    s_mslSIUnits = ''
    for s in as_mslSIUnits_:
        if s.find('//') == -1:
            s_mslSIUnits += s
        
    # Strip out whitespace
    s_mslSIUnits = s_mslSIUnits.replace('\n','').replace('\r','').replace('\t','').replace('  ','')
    
    # Divide into lines based on semicolon
    d_TypeStatements = dict()
    as_Statements = s_mslSIUnits.split(';')
    pr_IsTypeStatement = re.compile('type.*')
    for s in as_Statements:
        
        mo_IsTypeStatement = pr_IsTypeStatement.match(s)
        if mo_IsTypeStatement != None:
            mo = re.match(r"type (?P<type_name>\w+)",s)
            key = mo.group(1)
            
            d_TypeStatements[key] = GetUnitPropDict(s)
            d_TypeStatements[key]['ClassPath'] = 'Modelica.SIunits.' + key
                    
    return d_TypeStatements
            
def CombineDict(d1, d2):
    return dict(d1.items() + d2.items())

# RegEXes for unit properties
apr_DataTypeProps = []
apr_DataTypeProps.append( re.compile('.*=\s*(?P<UnitDataType>\w+) ') )
apr_DataTypeProps.append( re.compile('.*final quantity\s*=\s*\"(?P<UnitQuantity>\w+)\"') )
apr_DataTypeProps.append( re.compile('.*final unit\s*=\s*\"(?P<UnitUnit>\w+)\"') )
apr_DataTypeProps.append( re.compile('.*displayUnit\s*=\s*\"(?P<UnitDisplayUnit>\w+)\"') )
apr_DataTypeProps.append( re.compile('.*min\s*=\s*(?P<UnitMin>\w+)') )
apr_DataTypeProps.append( re.compile('.*start\s*=\s*(?P<UnitStart>\w+)') )
pr_EquivalentClass = re.compile('type \S*\s*=\s*(?P<EquivalentClass>\w+)')
def GetUnitPropDict(str):
    d_rtn = dict()
        
    for pr in apr_DataTypeProps:
        if pr.match(str) != None:
            d_rtn = CombineDict(d_rtn,pr.match(str).groupdict())
    
    if str.find('(') == -1:
        # This is just equivalent to something else
        d_rtn = CombineDict(d_rtn, pr_EquivalentClass.match(str).groupdict())
    
    return d_rtn

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
    for key, value in d_Units.iteritems():
        xml_Final += GenerateOWLNode(key,value)
    xml_Final += xml_Footer
    
    return xml_Final

def GenerateOWLIndividualFile(p_SIUnits,p_OutputFile):
    d_TypeStatements = ExtractUnitsFromMSL(p_SIUnits)
    
    xml_IndividualFile = GenerateOWLIndividualFileContent(d_TypeStatements)
    f = open(p_OutputFile,'w')
    f.write(xml_IndividualFile)
    f.close()