import re
class _Unit(object):
    pass
class UnitPrefix(object):
    without_comment = re.compile(r'^(.+?): (.+)$')
    with_comment = re.compile(r'^(.+?): (.+?)[, ]*?(\(.+)')
    def __init__(self, line):
        if re.search(r'\,',line):
            r = UnitPrefix.with_comment.match(line)
            self.set_obj(r.group(1),r.group(2),r.group(3))
        else:
            r = UnitPrefix.without_comment.match(line)
            self.set_obj(r.group(1),r.group(2))
            
    def set_obj (self, prefix_string, float_multiplier, comment = None):
        self.prefix_string = prefix_string
        self.float_multiplier = float_multiplier
        self.comment = comment
        
class BaseUnit(_Unit):
    regex = re.compile(r'(.+?): (.+)$')
    def __init__(self, line):
        r = BaseUnit.regex.match(line)
        self.set_obj(r.group(1), r.group(2))
        
    def set_obj(self, quantity_name, unit_name):
        self.quantity_name = quantity_name
        self.unit_name = unit_name
        
    def __repr__(self):
        return "%s,%s" % (self.quantity_name,self.unit_name)

    def to_OWl_xml(self):
        result = '''<!-- http://openmdao.org/units/individuals#{unit_name} -->

    <owl:NamedIndividual rdf:about="http://openmdao.org/units/individuals#{unit_name}">
        <rdf:type rdf:resource="&units;BaseUnit"/>
        <units:UnitName>{unit_name}</units:UnitName>
        <units:QuantityName>{quantity_name}</units:QuantityName>
    </owl:NamedIndividual>
        '''
        return result.format(unit_name = self.unit_name, quantity_name = self.quantity_name)
        
class DerivedUnit(_Unit):
    with_base_unit = re.compile(r'^(.+?): (.+?)\, (.+?)\, (.+?)\, (.+?)$')
    without_base = re.compile(r'^(.+?): (.+?)\, (.+?)$')
    def __init__(self, line):
        if len(re.findall(r'\,', line)) == 3:
            r = DerivedUnit.with_base_unit.match(line)
            self.set_obj(unit_name = r.group(1),
                         factor = r.group(2),
                         base_unit = r.group(3),
                         offset = r.group(4),
                         comment = r.group(5))
        else:
            r = DerivedUnit.without_base.match(line)
            self.set_obj(unit_name = r.group(1),
                         unit_exp = r.group(2),
                         comment = r.group(3))

    def to_OWl_xml(self):
        if self.base_unit == None:
            result = '''<!-- http://openmdao.org/units/individuals#{unit_name} -->

    <owl:NamedIndividual rdf:about="http://openmdao.org/units/individuals#{unit_name}">
        <rdf:type rdf:resource="&units;DerivedUnit"/>
        <units:UnitExpression>{unit_exp}</units:UnitExpression>
        <units:UnitName>{unit_name}</units:UnitName>
        <units:Comment>{comment}</units:Comment>
    </owl:NamedIndividual>
            '''
            return result.format(unit_name = self.unit_name, unit_exp = self.unit_exp,
                                 comment = self.comment)
        else:
            result = '''<owl:NamedIndividual rdf:about="http://openmdao.org/units/individuals#{unit_name}">
        <rdf:type rdf:resource="&units;DerivedUnit"/>
        <units:Comment>{comment}</units:Comment>
        <units:Offset>{offset}</units:Offset>
        <units:Factor>{factor}</units:Factor>
        <units:BaseUnit rdf:resource="http://openmdao.org/units/individuals#{base_unit}"/>
    </owl:NamedIndividual>
            '''
            return result.format(unit_name = self.unit_name, comment = self.comment, offset = self.offset,
                                 factor =  self.factor, base_unit = self.base_unit)
            
    def set_obj(self, unit_name, comment, unit_exp = None, factor = None,
                base_unit = None, offset = None):
        self.unit_name = unit_name
        self.comment = comment
        self.unit_exp = unit_exp
        self.factor = factor
        self.base_unit = base_unit
        self.offset = offset
        
def read_unit_file(filename):
    result = []
    with open(filename) as f:
        for i in f:
            if i[0] == '#':
                continue
            result.append(i)
    return result


    
def find_units(content):
    point = 0
    #print result
    for l in content:
        if l == '[prefixes]\n':
            prefix_start = point
        elif l == '[base_units]\n':
            base_start = point
        elif l == '[units]\n':
            unit_start = point
        point += 1

    result = []
    
    for  t in content[base_start+1:unit_start]:
        if t == '\n': continue
        result.append(BaseUnit(t))
    for t in content[unit_start+1:]:
        if t == '\n': continue
        result.append(DerivedUnit(t))
    return result
    
def xml_generator(source,obj):

    xml_head = '''<?xml version="1.0"?>


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
        <owl:versionIRI rdf:resource="http://openmdao.org/units/1.0.0/individuals"/>
    </owl:Ontology>
    
'''
    xml_tail = '</rdf:RDF>'
    content = read_unit_file(source)
    units = find_units(content)
    result = xml_head
    for b in units:
        result += b.to_OWl_xml()
        result +='\n'
    result += xml_tail
    with open(obj,'w') as f:
        f.write(result)

if __name__ == '__main__':
    xml_generator('unit.txt','openMDAO-individuals.xml')
