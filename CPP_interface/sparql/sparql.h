#ifndef SQARQL_H
#define SQARQL_H
#include <curl/curl.h>
#include <string>
#include <vector>
namespace qudt4dt{
    
        struct Query
        {
            std::string query_context;
            std::string field_names;
        };
        
       

        void init_qudt_server(const std::string&);
        bool query(const Query&, std::vector<std::string>&);

        
}
#endif










