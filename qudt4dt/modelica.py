import barbara as bar
from qudt import Unit
class ModelicaUnit(Unit):
    def __init__(self, _server, _url):
        super(ModelicaUnit ,self).__init__(_server, _url)
        querycontext_template = '''
        PREFIX ontology: <http://qudt4dt.org/ontology#>
        SELECT
        ?key
        WHERE
        {{ 
        ?key ontology:equivalentOf <{url}>.
        ?key a <http://modelica.org/msl/SIUnits/vocabulary#ModelicaUnitClass>
        }}'''
        print querycontext_template.format(url = _url)
        self.url = self.query.make_query(querycontext_template.format(url = _url))[0]
    def query_attr(self, attribute):
        query_template = '''
        PREFIX modelica: <http://modelica.org/msl/SIUnits/vocabulary#>
        SELECT
        ?key
        WHERE
        {{
        <{_url}> modelica:{_attribute} ?key.
        }}'''
        query = query_template.format(_url = self.url, _attribute = attribute)
        print query
        return self.query.make_query(query)
    
    def queryClassPath(self):
        return self.query_attr('ClassPath')
    
    def queryMax(self):
        return self.query_attr('Max')
    
    def queryMin(self):
        return self.query_attr('Min')
    
    def queryStart(self):
        return self.query_attr('Start')
    
    def queryDisplayUnit(self):
        return self.query_attr('DisplayUnit')
    
    def queryQuantity(self):
        return self.query_attr('Quantity')
    
    def createInstance(self, result):
        #result = qudt_pb2.ModelicaUnit()
        result.classPath = self.queryClassPath()[0]
        result.max = float(self.queryMax()[0])
        result.min = float(self.queryMin()[0])
        result.start = float(self.queryStart()[0])
        result.displayUnit = self.queryDisplayUnit()[0]
        result.quantity = self.queryQuantity()[0]
        return result