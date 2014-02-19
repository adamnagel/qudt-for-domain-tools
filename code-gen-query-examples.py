import qudt4dt


barb = qudt4dt.Barbara('http://localhost:3030')

derived_classes = barb.list_domain_tool_unit_classes()

for c in derived_classes:
    print c
    for dp in barb.get_data_properties_for_class(c):
        print dp

    print ""


# This query begins with ModelicaUnitClass, and recursively finds all of its baseclasses.
# For each baseclass, it finds any "anonymous classes" that provide "Restrictions".
# For each of those, it finds all triples that have that class as the subject.
# From these, we should be able to figure out if there are attributes that are *required*.
# If none of these anonymouse baseclasses require an attribute, then it considered to be optional.
"""PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
SELECT
?baseclass ?predicate ?object
WHERE
{
<http://modelica.org/msl/SIUnits/vocabulary#ModelicaUnitClass> rdfs:subClassOf+ ?baseclass .
?baseclass <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> owl:Restriction .
?baseclass ?predicate ?object
}"""

json_result = {
    "head": {
        "vars": [
            "baseclass",
            "predicate",
            "object"
        ]
    },
    "results": {
        "bindings": [
            {
                baseclass: {
                    type: "bnode",
                    value: "b0"
                },
                predicate: {
                    type: "uri",
                    value: "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
                },
                object: {
                    type: "uri",
                    value: "http://www.w3.org/2002/07/owl#Restriction"
                }
            },
            {
                baseclass: {
                    type: "bnode",
                    value: "b0"
                },
                predicate: {
                    type: "uri",
                    value: "http://www.w3.org/2002/07/owl#onProperty"
                },
                object: {
                    type: "uri",
                    value: "http://modelica.org/msl/SIUnits/vocabulary#ClassPath"
                }
            },
            {
                baseclass: {
                    type: "bnode",
                    value: "b0"
                },
                predicate: {
                    type: "uri",
                    value: "http://www.w3.org/2002/07/owl#onDataRange"
                },
                object: {
                    type: "uri",
                    value: "http://www.w3.org/2001/XMLSchema#anyURI"
                }
            },
            {
                baseclass: {
                    type: "bnode",
                    value: "b0"
                },
                predicate: {
                    type: "uri",
                    value: "http://www.w3.org/2002/07/owl#qualifiedCardinality"
                },
                object: {
                    datatype: "http://www.w3.org/2001/XMLSchema#integer",
                    type: "typed-literal",
                    value: "1"
                }
            }
        ]
    }
}