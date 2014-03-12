import barbara as bar
from qudt import Unit
class ModelicaUnit(Unit):
    def __init__(self, _server, _url):
        super(ModelicaUnit ,self).__init__(_server, _url)
    
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
    