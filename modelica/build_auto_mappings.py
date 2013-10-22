import json

__author__ = 'adam'
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import qudt4dt
from qudt4dt import sparqlcommands as sparql




barb = qudt4dt.Barbara("http://localhost:3030")

query_GetQUDTUnitsAndSymbols = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX qudt: <http://qudt.org/schema/qudt#>
SELECT DISTINCT
?unit ?symbol
WHERE
{ qudt:Unit ^rdfs:subClassOf+ ?class .
  ?unit a ?class .
  ?unit qudt:symbol ?symbol
}"""
json_QUDTUnits = barb.perform_query(query_GetQUDTUnitsAndSymbols)

qudtUnits = []
for item in json_QUDTUnits["results"]["bindings"]:
    unitURI = item["unit"]["value"]
    symbol = item["symbol"]["value"]
    unit = {'uri' : unitURI, 'symbol' : symbol}
    qudtUnits.append( unit )
print qudtUnits

query_GetModelicaUnitsAndSymbols = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX mv: <http://modelica.org/msl/SIUnits/vocabulary#>
PREFIX mi: <http://modelica.org/msl/SIUnits/individuals#>
SELECT DISTINCT
?unit ?symbol
WHERE
{ ?unit a mv:ModelicaUnitClass .
  ?unit mv:UnitUnit ?symbol
}"""
json_ModelicaUnits = barb.perform_query(query_GetModelicaUnitsAndSymbols)

modelicaUnits = []
for item in json_ModelicaUnits["results"]["bindings"]:
    unitURI = item["unit"]["value"]
    symbol = item["symbol"]["value"]
    unit = {'uri' : unitURI, 'symbol' : symbol}
    modelicaUnits.append( unit )
print modelicaUnits

# Okay, now we have both unit families.
# Let's do some brute-forcing
pairs = []
i_direct = 0
i_method1 = 0
i_method2 = 0
for qudtUnit in qudtUnits:
    for modelicaUnit in modelicaUnits:
        qudtSymbol = qudtUnit["symbol"]
        moSymbol = modelicaUnit["symbol"]
        if qudtSymbol == moSymbol:
            pairs.append( {"qudt": qudtUnit["uri"], "mo" : modelicaUnit["uri"]} )
            i_direct += 1
        elif qudtSymbol == moSymbol.replace("."," "):
            pairs.append( {"qudt": qudtUnit["uri"], "mo" : modelicaUnit["uri"]} )
            i_method1 += 1
        elif moSymbol == qudtSymbol.replace("^",""):
            pairs.append( {"qudt": qudtUnit["uri"], "mo" : modelicaUnit["uri"]} )
            i_method2 += 1

for pair in pairs:
    print pair["mo"].replace("http://modelica.org/msl/SIUnits/individuals#","") + "," + pair["qudt"].replace("http://qudt.org/vocab/unit#","")

