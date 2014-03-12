import barbara as bar
from qudt import Unit

class MdaoUnit(Unit):
    def __init__(self, _server, _url):
        super(MdaoUnit, self).__init__(_server, _url)
    
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
        return self.query.make_query(query)
    
    def queryExpression(self):
        return self.query_attr('UnitExpression')
    
    def queryName(self):
        return self.query_attr('UnitName')
    
    def queryComment(self):
        return self.query_attr('Comment')
    
    