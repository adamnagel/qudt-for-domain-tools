#ifndef SPARQL_H
#define SPARQL_H
#include <string>
#include <vector>
namespace qudt4dt{

void init_qudt_server(const std::string&);
bool query(const std::string&, std::vector<std::string>&);
void init_qudt_server(const std::string& server_url);

};
#endif












