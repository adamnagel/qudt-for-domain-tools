__author__ = 'adam'

import json
import os
import sparqlcommands as sparql

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


    def get_unit_class(self,UnitURI):
        # Stub
        return self.list_all_units()[0]

    def get_units_in_class(self,ClassURI):
        # Stub
        return self.list_all_unit_classes()[0]

    def get_units_in_same_class(self,UnitURI):
        # Stub
        return self.list_all_units()[1:5]

    def convert_value(self,source_unit_uri,destination_unit_uri,source_value):
        # Stub
        return 5.5