#include<string>
#include<sparql/sparql.hpp>
namespace qudt4dt
{
double LIB_VERSION = 0.1;

void init_qudt4dt_server(const std::string& server_url)
{
    sparql::init_server(server_url);
}

}
