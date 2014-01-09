#ifndef SQARQL_H
#define SQARQL_H
#include <curl/curl.h>
#include <string>

namespace qudt4dt{

    struct Server_url
    {
        std::string url_base;
        std::string url_query;
        std::string url_update;
        std::string url_upload;
    };

    void init_qudt_server(const std::string&);
    std::string query(const std::string&);

    class Barbara
    {
    public:
        static void init(const std::string&);
        static std::string query(const std::string&);
    private:
        Barbara(){};
        Barbara(const Barbara&){};
        Barbara& operator=(const Barbara&){};
        ~Barbara(){};
        static Server_url _su;
    };

}
#endif
