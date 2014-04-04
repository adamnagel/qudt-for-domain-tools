import sys sys.path.append("..")
import barbara as bar
from qudt import Unit

class MdaoUnit(Unit):
    def __init__(self, _server, _url):
        super(MdaoUnit, self).__init__(_server, _url)
        querycontext_template = '''
        PREFIX ontology: <http://qudt4dt.org/ontology#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT
        ?key
        WHERE
        {{ 
        ?key ontology:equivalentOf <{url}>.
        <http://openmdao.org/units#OpenMdaoUnit> ^rdfs:subClassOf+ ?class .
        ?key a ?class
        }}'''
        print querycontext_template.format(url = _url)
        self.url = self.query.make_query(querycontext_template.format(url = _url))[0]
        
    def query_attr(self, attribute):
        query_template = '''
        PREFIX mdao: <http://openmdao.org/units#>
        SELECT
        ?key
        WHERE
        {{
        <{_url}> mdao:{_attribute} ?key.
        }}'''
        query = query_template.format(_url = self.url, _attribute = attribute)
        print query
        return self.query.make_query(query)
    
    def queryExpression(self):
        return self.query_attr('UnitExpression')
    
    def queryName(self):
        return self.query_attr('UnitName')
    
    def queryComment(self):
        return self.query_attr('Comment')
    
    def createInstance(self, result):
        #result = qudt_pb2.MdaoUnit()
        result.name = self.queryName()[0]
        if not len(self.queryExpression())== 0:
            result.expression = self.queryExpression()[0]
        if not len(self.queryComment()) == 0:
            result.comment = self.queryComment()[0]
        return result