__author__ = 'adam'

import sparqlcommands as sparql
import re
from unit_mapping import createMapping

class Barbara:
    def __init__(self,server_url):
        self.__set_server_urls(server_url)

    def __set_server_urls(self,server_url):
        self.__url_base = server_url
        self.__url_upload = server_url + '/qudt4dt/upload'
        self.__url_query = server_url + '/qudt4dt/query?'
        self.__url_update = server_url + '/qudt4dt/update?'

    def __get_num_triples_in_database(self):
        query = """
        SELECT (COUNT(*) AS ?no) { ?s ?p ?o  }
        """
        result = sparql.query(query,self.__url_query)
        numResults = result["results"]["bindings"][0]["no"]["value"]
        return numResults

    def get_server_status(self):
        numTriples = self.__get_num_triples_in_database()
        numUnits = len(self.list_all_units())

        rtn =  "Connection to database OK\n"
        rtn += str(numTriples) + " triples in database\n"
        rtn += str(numUnits) + " units in database\n"
        return rtn

    def list_all_units(self):
        query = """ PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    SELECT
                    ?unit
                    WHERE
                    { <http://qudt.org/schema/qudt#Unit> ^rdfs:subClassOf+ ?class .
                        ?unit a ?class
                    }"""
        result = sparql.query(query,self.__url_query)
        units = []
        for item in result["results"]["bindings"]:
            unitURI = item["unit"]["value"]
            units.append( unitURI )
        return units

    def list_all_unit_classes(self):
        query = """ PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    SELECT
                    ?class
                    WHERE
                    { <http://qudt.org/schema/qudt#Unit> ^rdfs:subClassOf+ ?class
                    }"""
        result = sparql.query(query,self.__url_query)
        unitClasses = []
        for item in result["results"]["bindings"]:
            classURI = item["class"]["value"]
            unitClasses.append( classURI )
        return unitClasses
        
    def list_domain_tool_unit_classes(self):
        query = """PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                   PREFIX qudt4dt: <http://qudt4dt.org/ontology#>
                   SELECT
                   ?class
                   WHERE
                   { 
                     qudt4dt:DomainToolUnit ^rdfs:subClassOf+ ?class
                   }"""
        result = sparql.query(query, self.__url_query)
        unitClasses = []
        for item in result["results"]["bindings"]:
            classURI = item["class"]["value"]
            unitClasses.append( classURI )
        return unitClasses

    def _jsonGetUri(name):
        def decorate(func):
            def ret(*arg,**karg):
                t = func(*arg,**karg)
                result = []
                for i in t['results']['bindings']:
                    result.append(i[name]['value'])
                return result
            return ret
        return decorate
  
    @_jsonGetUri('class')
    def get_unit_class(self,UnitURL):
        query = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                   PREFIX owl: <http://www.w3.org/2002/07/owl#>
                   SELECT
                   ?class 
                   WHERE
                   {
                     <%s> rdf:type ?class. 
                     FILTER NOT EXISTS{?class rdf:type owl:DeprecatedClass}
                   }"""
        query = query %UnitURL
        result = sparql.query(query,self.__url_query)
        return result
      
    @_jsonGetUri('unit')
    def get_units_in_class(self,ClassURL):
        query = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                   SELECT
                   ?unit 
                   WHERE 
                   {
                     ?unit rdf:type <%s> 
                   }"""
        query = query % ClassURL
        result = sparql.query(query, self.__url_query)
        return result
  
    def get_units_in_same_class(self,UnitURL):
        result = []
        for i in self.get_unit_class(UnitURL):
            result = result + self.get_units_in_class(i)
        return result

    @_jsonGetUri('symbol')
    def __get_sym(self, UnitURL):
        query = '''
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX qudt: <http://qudt.org/schema/qudt#>
        SELECT ?symbol
        WHERE
        {{ 
        <{unitURL}> qudt:quantityKind ?kind.
        ?symbol qudt:referenceQuantity ?kind
        }}
        '''
        return sparql.query(query.format(unitURL = UnitURL),self.__url_query)
        
    def get_SI_symbol(self, UnitURL):
        r = self.__get_sym(UnitURL)
        for i in r:
            if re.search(r'http://qudt.org/vocab/dimension#Dimension_SI_.+',i):
                return i

    @_jsonGetUri('vec')
    def get_SI_vector(self, si_sym):
        query = '''
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX qudt:<http://qudt.org/schema/qudt#>
        SELECT ?vec
        WHERE
        {{ 
        
        <{si_sym}> qudt:dimensionVector ?vecs.
        ?vecs qudt:basisElement ?vec.
        }}
        '''
        return sparql.query(query.format(si_sym = si_sym),self.__url_query)

    def is_baseunit(self, unit):
        offset = self.get_offset(unit)
        mult = self.get_mult_factor(unit)
        if offset == [u'0.0']  and (mult in [[u'1'],[u'1.0e0'],[u'1.0E6'],[u'1.0']]):
            return True
        else:
            return False
        
    @_jsonGetUri('offset')
    def get_offset(self, unit):
        query = '''
        PREFIX qudt: <http://qudt.org/schema/qudt#>
        SELECT
        ?offset
        WHERE
        {{
        <{unit}> qudt:conversionOffset ?offset.
        }}
        '''
        return sparql.query(query.format(unit = unit),self.__url_query)

    @_jsonGetUri('mult')
    def get_mult_factor(self, unit):
        query = '''
        PREFIX qudt: <http://qudt.org/schema/qudt#>
        SELECT
        ?mult
        WHERE
        {{
        <{unit}> qudt:conversionMultiplier ?mult
        }}
        '''
        return sparql.query(query.format(unit = unit),self.__url_query)
            


            
    def convert_value(self,source_unit_url,destination_unit_url,source_value):
        if not self.get_unit_class(source_unit_url) == self.get_unit_class(destination_unit_url):
            raise ValueError
            
        query = '''
        PREFIX qudt: <http://qudt.org/schema/qudt#>
        SELECT
        ?sou_offset ?sou_mult ?des_offset ?des_mult
        WHERE
        {{
        <{source}> qudt:conversionOffset ?sou_offset.
        <{source}> qudt:conversionMultiplier ?sou_mult.
        <{destin}> qudt:conversionOffset ?des_offset.
        <{destin}> qudt:conversionMultiplier ?des_mult.
        }}'''
        take = lambda x: (float(x["results"]["bindings"][0]["sou_offset"]["value"]),
                          float(x["results"]["bindings"][0]["sou_mult"]["value"]),
                          float(x["results"]["bindings"][0]["des_offset"]["value"]),
                          float(x["results"]["bindings"][0]["des_mult"]["value"]))
        result = sparql.query(query.format(source = source_unit_url,
                                           destin = destination_unit_url),self.__url_query)
    
        if result["results"]["bindings"] == []: raise ValueError
        
        sou_offset,sou_mult,des_offset,des_mult = take(result)

        des_value = ((sou_offset - des_offset) + float(source_value)) * sou_mult / float(des_mult)
        return des_value
