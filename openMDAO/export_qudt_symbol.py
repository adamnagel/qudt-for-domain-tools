# -*- coding:utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath('../'))
reload(sys) 
sys.setdefaultencoding( "utf-8" ) 


import re
import qudt4dt
bara = qudt4dt.Barbara("http://localhost:3030")
baseUnit = {u'L':u'm', u'M':u'kg',
            u'T':u's', u'I':u'A',
            u'N':u'mol',u'J':u'cd',
            u'\u0398': u'K', u'U':u'rad'}

def symbol_lex_token(symbolString):
    if symbolString == '':
        return []
    else:
        token = re.compile(ur'^([LMNJTIU\u0398])-?\d*',re.UNICODE)
        result = re.match(token,symbolString)
        point = len(result.group(0))
        power = result.group(0)[len(result.group(1)):]
        pair = (result.group(1), power)
        return symbol_lex_token(symbolString[point:]) + [pair]
        
def tokens_to_unit(tokens):
    r = ''
    for (i,j) in tokens:
        if j == '':
            r += '*{sym}'.format(sym = baseUnit[i])
        else:
            r += '*{sym}**{pow}'.format( sym = baseUnit[i], pow =j)
    return r[1:]

def get_all_unit_symbol():
    unitList = bara.list_all_units()
    result = {}
    for u in unitList:
        symbol = bara.get_SI_symbol(u)

        if not symbol == None:
            print u
            si = re.match(r'http://qudt.org/vocab/dimension#Dimension_SI_(.+)$',symbol).group(1)
            print si
            print tokens_to_unit(symbol_lex_token(si))
            print ('\n')

class OpenMdaoDynamicUnit(object):
    """
    to create the owl file from QUDT to OpenMdao Dynamic Units
    """
    
    def __init__(self, qudtUrl):
        self.qudtUrl = qudtUrl
        self.unitName = re.match(r'^http://qudt.org/vocab/unit#(.+)$',qudtUrl).group(1)
        factor = bara.get_mult_factor(qudtUrl)
        if factor == []:
            factor = ''
        else:
            factor = factor[0]
        symbol = bara.get_SI_symbol(qudtUrl)
        if not symbol == None:
             si = re.match(r'http://qudt.org/vocab/dimension#Dimension_SI_(.+)$',symbol).group(1)
             SI_symbol = tokens_to_unit(symbol_lex_token(si))
        self.unitExp = '{factor}*{SI}'.format(factor = factor, SI = SI_symbol)
        offset = bara.get_offset(qudtUrl)
        if offset == []:
            self.offset = ''
        else:
            self.offset = offset[0]
    def xml_str(self):
        template = ''' <!-- http://openmdao.org/units/individuals#{unitName} -->

    <owl:NamedIndividual rdf:about="http://openmdao.org/units/individuals#{unitName}">
        <rdf:type rdf:resource="&units;DynamicUnitDefinition"/>
        <units:UnitName rdf:datatype="&xsd;string">{unitName}</units:UnitName>
        <units:UnitExpression rdf:datatype="&xsd;string">{unitExp}</units:UnitExpression>
        <units:Offset>{offset}</units:Offset>
        <units:Comment>dynamic-unit</units:Comment>
    </owl:NamedIndividual>
        '''
        return template.format(unitName = self.unitName, unitExp = self.unitExp, offset = self.offset)
    def csv_str(self):
        template = '{name},{name}\n'
        return template.format(name = self.unitName)

def xml_generator(xmlFile,csvFile):
    # print u'\u0398'
    head = '''<?xml version="1.0"?>


<!DOCTYPE rdf:RDF [
    <!ENTITY units "http://openmdao.org/units#" >
    <!ENTITY owl "http://www.w3.org/2002/07/owl#" >
    <!ENTITY xsd "http://www.w3.org/2001/XMLSchema#" >
    <!ENTITY rdfs "http://www.w3.org/2000/01/rdf-schema#" >
    <!ENTITY rdf "http://www.w3.org/1999/02/22-rdf-syntax-ns#" >
]>


<rdf:RDF xmlns="http://openmdao.org/units/individuals#"
     xml:base="http://openmdao.org/units/individuals"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
     xmlns:owl="http://www.w3.org/2002/07/owl#"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:units="http://openmdao.org/units#">
    <owl:Ontology rdf:about="http://openmdao.org/units/individuals">
        <owl:imports rdf:resource="http://openmdao.org/units#"/>
        <owl:imports rdf:resource="http://openmdao.org/units/individuals"/>
    </owl:Ontology>
    

'''
    xml = open(xmlFile,'w')
    csv = open(csvFile,'w')
    xml.write(head)
    unitList = bara.list_all_units()
    # unit = OpenMdaoDynamicUnit('http://qudt.org/vocab/unit#SquareCentimeterMinute')
    # xml.write(unit.xml_str())
    for u in unitList:
        if not bara.get_SI_symbol(u) == None:
            unit = OpenMdaoDynamicUnit(u)
            xml.write(unit.xml_str())
            csv.write(unit.csv_str())

    xml.write('</rdf:RDF>')
if __name__ == '__main__':
    xml_generator('openMDAO-dynamic-individuals.xml','test.csv')
    #print bara.get_mult_factor('http://qudt.org/vocab/unit#SquareFootDegreeFahrenheit')
    #print tokens_to_unit(symbol_lex_token(u'ϴ-1'))
   # print bara.get_unit_class('http://qudt.org/vocab/unit#SquareCentimeterMinute')
   # print bara.get_units_in_same_class('http://qudt.org/vocab/unit#SquareCentimeterMinute')
