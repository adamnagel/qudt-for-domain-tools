#include <curl/curl.h>
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include "sparql.h"
#include <jsoncpp/json/json.h>
#include <typeinfo>
#include <boost/format.hpp>
int main()
{
    
    qudt4dt::init_qudt_server("http://127.0.0.1:3030");
    std::string _q = "PREFIX qudt: <http://qudt.org/schema/qudt#>\n        SELECT\n        ?x\n        WHERE\n        {\n        <%1%> qudt:conversionMultiplier ?x.\n        }\n";
    std::vector<std::string> result;
    

    if(!qudt4dt::query((boost::format(_q) % "http://qudt.org/vocab/unit#kelvin").str(), result))
        std::cout<<"fail"<<std::endl;
    for(auto& i : result)
        std::cout<<i<<std::endl;
    return 0;

}
















