#include <curl/curl.h>
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include "sparql.h"
#include <jsoncpp/json/json.h>
#include <typeinfo>

int main()
{
    
    qudt4dt::init_qudt_server("http://127.0.0.1:3030");
    std::string _q = "\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n                   PREFIX qudt4dt: <http://qudt4dt.org/ontology#>\n                   SELECT\n                   ?class\n                   WHERE\n                   { \n                     qudt4dt:DomainToolUnit ^rdfs:subClassOf+ ?class\n                   }";
    std::vector<std::string> result;
    qudt4dt::Query a = {
        .query_context = _q,
        .field_names = "class",
    };

    if(!qudt4dt::query(a, result))
        std::cout<<"fail"<<std::endl;
    for(auto& i : result)
        std::cout<<i<<std::endl;
    return 0;

}
















