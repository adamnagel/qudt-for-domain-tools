#ifndef SPARQL_H
#define SPARQL_H
#include <curl/curl.h>
#include <string>
#include <vector>
#include <boost/lexical_cast.hpp>
namespace qudt4dt{

void init_qudt_server(const std::string&);
bool query(const std::string&, std::vector<std::string>&);

template<class T>
bool query_get_attr(const std::string& query_context, T& ret)
{
    std::vector<std::string> _v;
    if(false == query(query_context, _v))
        return false;
         
    ret = boost::lexical_cast<T>(_v.at(0));
    return true;
}
};
#endif












