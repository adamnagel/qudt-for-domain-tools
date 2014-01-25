#include <cassert>
#include <iostream>
#include <curl/curl.h>
#include <jsoncpp/json/json.h>
#include "sparql/sparql.hpp"
using namespace std;
namespace qudt4dt{

static struct
{
    string url_base;
    string url_query;
    string url_update;
    string url_upload;
}_su;

// Server_url;
static string* _buf;


static size_t write_data(void *ptr, size_t size, size_t nmemb, void *userp)
{
    qudt4dt::_buf->append((char*)ptr, size*nmemb);
    return size*nmemb;
}

static bool query_raw(const string& query_str, string& ret_value)
{
    CURL *curl;
    string encode_query, result, opt_url;
    //connect callback func to query func
    //'_buf' should be null at this time 
    assert(!_buf);
    qudt4dt::_buf = &result;
        
    curl = curl_easy_init();
    if (!curl)
        return false;

    encode_query = string(curl_easy_escape(curl, query_str.c_str(), 0));
    opt_url = ::qudt4dt::_su.url_query + "query=" + encode_query;
    curl_easy_setopt(curl, CURLOPT_URL, opt_url.c_str());
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_data);
    curl_easy_perform(curl);
    curl_easy_cleanup(curl);
    ret_value = result;
    qudt4dt::_buf = static_cast<std::string*>(0);
    //TODO: add log action here
    return true;
}

bool query(const string& query_context, vector<string>& ret_value)
{
    string raw_result;
    if(false == query_raw(query_context, raw_result))
        return false;
    //get the json_str result
        
    Json::Reader reader;
    Json::Value value;

    if(!reader.parse(raw_result,value))
        return false;
    Json::Value bindings = value["results"]["bindings"];

    for(Json::Value::iterator i = bindings.begin(); i != bindings.end(); ++i)
        ret_value.push_back((*i)["x"]["value"].asString());
        
    return true;
}

void init_qudt_server(const string& server_url)
{
    ::qudt4dt::_su.url_base = server_url;
    ::qudt4dt::_su.url_upload = server_url + "/qudt4dt/upload";
    ::qudt4dt::_su.url_query = server_url + "/qudt4dt/query?";
    ::qudt4dt::_su.url_update = server_url + "/qudt4dt/update?";
};
    

};

