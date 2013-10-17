import re

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
        
class BaseUnit(object):
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
        
class DerivedUnit(object):
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
            return result.format(unit_name = self.unit_name, comment = self.comment, offset = self.offset, factor =  self.factor, base_unit = self.base_unit)
            
    def set_obj(self, unit_name, comment, unit_exp = None, factor = None,
                base_unit = None, offset = None):
        self.unit_name = unit_name
        self.comment = comment
        self.unit_exp = unit_exp
        self.factor = factor
        self.base_unit = base_unit
        self.offset = offset
        
def prefix_parser(data):
    for l in data:
        if l == '\n': continue
        yield UnitPrefix(l)

def base_unit_parser(data):
    for l in data:
        if l == '\n': continue
        yield BaseUnit(l)

def derived_unit_parser(data):
    for l in data:
        if l == '\n': continue
        yield DerivedUnit(l)
        
def read_unit_file(filename):
    f = open(filename)
    result = []
    for i in f:
        if i[0] == '#':
            continue
        result.append(i)
    point = 0
    #print result
    for l in result:
        if l == '[prefixes]\n':
            prefix_start = point
        elif l == '[base_units]\n':
            base_start = point
        elif l == '[units]\n':
            unit_start = point
        point += 1

    for t in prefix_parser(result[prefix_start+1:base_start]):
        print repr(t)
    for  t in base_unit_parser(result[base_start+1:unit_start]):
        print t.to_OWl_xml()
    for t in derived_unit_parser(result[unit_start+1:]):
        print t.to_OWl_xml()
read_unit_file('unit.txt')
