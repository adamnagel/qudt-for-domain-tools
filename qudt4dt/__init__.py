__author__ = 'adam'

import json
import os
import sparqlcommands as sparql

class Barbara:
    def __init__(self,server_url):
        self.set_server_urls(server_url)
        self.test_server()

    def set_server_urls(self,server_url):
        self.url_base = server_url
        self.url_upload = server_url + '/ds/upload'
        self.url_query = server_url + '/ds/query?'
        self.url_update = server_url + '/ds/update?'

    def num_triples_in_database(self):
        query = """
        SELECT (COUNT(*) AS ?no) { ?s ?p ?o  }
        """
        result = sparql.query(query,self.url_query)
        numResults = result["results"]["bindings"][0]["no"]["value"]
        return numResults

    def test_server(self):
        numTriples = self.num_triples_in_database()
        numUnits = len(self.list_all_units())
        print "Connection to database OK"
        print str(numTriples) + " triples in database"
        print str(numUnits) + " units in database"

    def list_all_units(self):
        query = """ PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    SELECT
                    ?unit
                    WHERE
                    { <http://qudt.org/schema/qudt#Unit> ^rdfs:subClassOf+ ?class .
                        ?unit a ?class
                    }"""
        result = sparql.query(query,self.url_query)
        units = []
        for item in result["results"]["bindings"]:
            unitURI = item["unit"]["value"]
            units.append( unitURI )
        return units