#ifndef SPARQL_H
#define SPARQL_H
#include <curl/curl.h>
#include <string>
#include <vector>
namespace qudt4dt{

void init_qudt_server(const std::string&);
bool query(const std::string&, std::vector<std::string>&);
bool query_get_attr(const std::string&, std::string&);
        
};
#endif












