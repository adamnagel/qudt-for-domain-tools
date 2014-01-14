#include "sparql.h"
#include <cstdlib>
#include <jsoncpp/json/json.h>
using namespace std;
namespace qudt4dt{

    struct Server_url
    {
        std::string url_base;
        std::string url_query;
        std::string url_update;
        std::string url_upload;
    };

    static Server_url _su;
    static string* _buf;


    static size_t write_data(void *ptr, size_t size, size_t nmemb, void *userp)
    {
        _buf->append((char*)ptr, size*nmemb);
        return size*nmemb;
    }

    bool query(const Query& _q, vector<string>& _v)
    {
        CURL *curl;
        string encode_query, result, opt_url;
        _buf = &result;
        curl = curl_easy_init();
        if (!curl)
            return false;

        encode_query = string(curl_easy_escape(curl, _q.query_context.c_str(), 0));
        opt_url = _su.url_query + "query=" + encode_query;
        curl_easy_setopt(curl, CURLOPT_URL, opt_url.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_data);
        curl_easy_perform(curl);
        curl_easy_cleanup(curl);
        //get the json_str result

        Json::Reader reader;
        Json::Value value;

        if(!reader.parse(result,value))
            return false;
        Json::Value bindings = value["results"]["bindings"];

        for(Json::Value::iterator i = bindings.begin(); i != bindings.end(); ++i)
            _v.push_back((*i)[_q.field_names]["value"].asString());
        
        return true;
    }
    
    void init_qudt_server(const string& server_url)
    {
        _su.url_base = server_url;
        _su.url_upload = _su.url_base + "/qudt4dt/upload";
        _su.url_query = _su.url_base + "/qudt4dt/query?";
        _su.url_update = _su.url_base + "/qudt4dt/update?";
    };

};

