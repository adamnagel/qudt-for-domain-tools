#ifndef SPARQL_H
#define SPARQL_H
#include <string>
#include <vector>
namespace qudt4dt{
namespace sparql{
void init_server(const std::string&);
bool query(const std::string&, std::vector<std::string>&);
};//namespace sparql
};//namespace qudt4dt
#endif












