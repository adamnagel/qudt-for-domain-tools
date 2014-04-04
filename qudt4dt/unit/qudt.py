import sys sys.path.append("..")
import qudt_pb2 
import barbara as bar
class Unit(object):
    def __init__(self, _server, _url):
        self.url = _url
        self.query = bar.Barbara(_server)

    
class QudtUnit(Unit):
    def __init__(self,_server, _url):
        super(QudtUnit, self).__init__(_server, _url)
        
    def query_attr(self, attribute):
        query_template = '''
        PREFIX qudt: <http://qudt.org/schema/qudt#>
        SELECT
        ?key
        WHERE
        {{
        <{_url}> qudt:{_attribute} ?key.
        }}'''
        query = query_template.format(_url = self.url, _attribute = attribute)
        return self.query.make_query(query)
    
    def getFactor(self):
        return self.query_attr('conversionMultiplier')
    
    def getOffset(self):
        return self.query_attr('conversionOffset')
    
    def getUnitClass(self):
        query_template = '''
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        SELECT
        ?key
        WHERE
        {{
        <{_url}> rdf:type ?key. 
        FILTER NOT EXISTS{{?key rdf:type owl:DeprecatedClass}}
        }}'''
        #print query_template.format(_url = self.url)
        return self.query.make_query(query_template.format(_url = self.url))
    
    def createInstance(self, result):
        #result = qudt_pb2.QudtUnit()
        result.url = self.url
        result.unitClass = self.getUnitClass()[0]
        if not len(self.getOffset()) == 0:
            result.offset = self.getOffset()[0]
        if not len(self.getFactor()) == 0:
            result.factor = self.getFactor()[0] 
        
        
