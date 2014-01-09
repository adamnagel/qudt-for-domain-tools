#include "sparql.h" 
using namespace std;
namespace qudt4dt{
    
    Server_url Barbara::_su;
    string* _buf;


    size_t write_data(void *ptr, size_t size, size_t nmemb, void *userp)
    {
        _buf->append((char*)ptr, size*nmemb);
        return size*nmemb;
    }

    void Barbara::init(const string& server_url)
    {
        _su.url_base = server_url;
        _su.url_upload = _su.url_base + "/qudt4dt/upload";
        _su.url_query = _su.url_base + "/qudt4dt/query?";
        _su.url_update = _su.url_base + "/qudt4dt/update?";
    }



    string Barbara::query(const string& query_str)
    {
        CURL *curl;
        string encode_query, result, opt_url;
        _buf = &result;
        curl = curl_easy_init();
        if (curl)
        {
            encode_query = std::string(curl_easy_escape(curl, query_str.c_str(), 0));
        }
        //TODO failure process
        opt_url = _su.url_query + "query=" + encode_query;
        curl_easy_setopt(curl, CURLOPT_URL, opt_url.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_data);
        curl_easy_perform(curl);
        curl_easy_cleanup(curl);

        return result;
    }

    string query(const string& query_str)
    {
        return Barbara::query(query_str);
    }
    
    void init_qudt_server(const string& server_url)
    {
        Barbara::init(server_url);
    };

};
