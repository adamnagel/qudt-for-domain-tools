__author__ = 'adam'
import json
import requests
import os
import urllib

# Establish key URLS for SPARQL database
url_base = 'http://localhost:3030'
url_upload = url_base + '/ds/upload'
url_query = url_base + '/ds/query?'
url_update = url_base + '/ds/update?'

### Define query function ###
def sparqlQuery(query, baseURL, format="application/json"):
    params={
        "should-sponge": "soft",
        "debug": "on",
        "timeout": "",
        "format": format,
        "save": "display",
        "fname": "",
        "output":"json",
        "query":query
    }
    querypart=urllib.urlencode(params)
    response = urllib.urlopen(baseURL,querypart).read()
    return json.loads(response)

### Define update function ###
def sparqlUpdate(update, baseURL):
    params={
        "update":update
    }
    querypart=urllib.urlencode(params)
    response = urllib.urlopen(baseURL,querypart).read()
    
# SELECT -- return unit and modelica class
# WHERE -- ?unit has "modelicaClass" DataProperty of ?moClass
query_GetAllModelicaUnitClasses="""PREFIX avm: <http://avm.org/unitLib#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX qudt: <http://qudt.org/schema/qudt#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX unit: <http://qudt.org/vocab/unit#>
PREFIX modelica: <http://metamorphinc.com/ontology/modelica#>
SELECT
?s
WHERE {
?s a modelica:ModelicaUnitClass
}
ORDER BY ASC(?s)"""
json_Response = sparqlQuery(query_GetAllModelicaUnitClasses,url_query)
print json.dumps(json_Response, indent=4, sort_keys=True)

# QUERIES BELOW THIS LINE DON'T WORK -- NEED TO BE UPDATED
'''
# Create extension to define "ModelicaClass" DataProperty for Units
update_CreateModelicaClass_DataProperty = """PREFIX avm: <http://avm.org/unitLib#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX qudt: <http://qudt.org/schema/qudt#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
INSERT DATA
{ avm:modelicaClass a owl:DatatypeProperty .
  avm:modelicaClass rdfs:domain qudt:Unit .
  avm:modelicaClass rdfs:range xsd:string
}"""


# Create ModelicaClass property for one unit
update_SetModelicaClass_Mass = """PREFIX avm: <http://avm.org/unitLib#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX qudt: <http://qudt.org/schema/qudt#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX unit: <http://qudt.org/vocab/unit#>
INSERT DATA
{
  unit:Kilogram avm:modelicaClass "Modelica.SIUnits.Mass"^^xsd:string
}"""


#### Here are some sample queries ####

# SELECT -- return subclasses of Unit
# WHERE -- Get all subclasses of "Unit" (specific unit classes)
query_GetAllSubclassesOfUnit="""PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT
?object
WHERE
{ <http://qudt.org/schema/qudt#Unit> ^rdfs:subClassOf+ ?object}"""

# SELECT -- return class and unit
# WHERE -- First, get all subclasses of "Unit" (specific unit classes)
#          Finally, get all individuals that are members of those classes (specific units)
query_GetAllIndividualsThatBelongToThe_Unit_Class="""PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT
?class ?unit
WHERE
{ <http://qudt.org/schema/qudt#Unit> ^rdfs:subClassOf+ ?class .
  ?unit a ?class }"""

# SELECT -- return class, unit, and symbol
# WHERE -- First, get all subclasses of "Unit" (specific unit classes)
#          Next, get all individuals that are members of those classes (specific units)
#          Finally, get the symbols for each unit
query_GetAllUnitIndividualsPlusSymbols="""PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT
?class ?unit ?symbol
WHERE
{ <http://qudt.org/schema/qudt#Unit> ^rdfs:subClassOf+ ?class .
  ?unit a ?class .
  ?unit <http://qudt.org/schema/qudt#symbol> ?symbol
}"""




# SELECT -- return unit
# WHERE -- ?unit has "modelicaClass" DataProperty of "Modelica.SIUnits.Mass"
query_GetQUDTUnitForModelicaKilogram="""PREFIX avm: <http://avm.org/unitLib#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX qudt: <http://qudt.org/schema/qudt#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX unit: <http://qudt.org/vocab/unit#>
SELECT
?unit
WHERE {
?unit avm:modelicaClass "Modelica.SIUnits.Mass"^^xsd:string
}"""

# SELECT -- return Modelica class
# WHERE -- unit:Kilogram has "modelicaClass" DataProperty ?moClass
query_GetModelicaClassForKilogram="""PREFIX avm: <http://avm.org/unitLib#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX qudt: <http://qudt.org/schema/qudt#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX unit: <http://qudt.org/vocab/unit#>
SELECT
?moClass
WHERE {
unit:Kilogram avm:modelicaClass ?moClass
}"""

'''