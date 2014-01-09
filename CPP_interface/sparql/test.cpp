#include <curl/curl.h>
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include "sparql.h"


std::string buffer;

size_t write_data(void *ptr, size_t size, size_t nmemb, void *userp)
{
    buffer.append((char*)ptr, size*nmemb);
    return size*nmemb;
}

int main()
{
    qudt4dt::init_qudt_server("http://127.0.0.1:3030");
    std::string _q = "\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n                   PREFIX qudt4dt: <http://qudt4dt.org/ontology#>\n                   SELECT\n                   ?class\n                   WHERE\n                   { \n                     qudt4dt:DomainToolUnit ^rdfs:subClassOf+ ?class\n                   }";
    std::string b = qudt4dt::query(_q);
    std::cout<<b;
    return 0;
//CURL *curl = curl_easy_init();

    //curl_easy_setopt(curl, CURLOPT_URL, "http://127.0.0.1:3030/qudt4dt/query?query=PREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0A++++++++++++++++++++SELECT%0D%0A++++++++++++++++++++%3Funit%0D%0A++++++++++++++++++++WHERE%0D%0A++++++++++++++++++++%7B+%3Chttp%3A%2F%2Fqudt.org%2Fschema%2Fqudt%23Unit%3E+%5Erdfs%3AsubClassOf%2B+%3Fclass+.%0D%0A++++++++++++++++++++++++%3Funit+a+%3Fclass%0D%0A++++++++++++++++++++%7D&output=json&stylesheet=&force-accept=text%2Fplain"); 
    //curl_easy_setopt(curl, CURLOPT_TIMEOUT, 20);
    //curl_easy_setopt(curl, CURLOPT_NOSIGNAL, 1);   
    //curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_data);
    //curl_easy_setopt(curl, CURLOPT_HEADER, 1);     
    //curl_easy_setopt(curl, CURLOPT_RANGE, "0-500");   
    //char buffer[MAXHEADLEN] = {0x0};
//    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, callback_get_head); 
    //  curl_easy_setopt(curl, CURLOPT_WRITEDATA, buffer);
    
    //curl_easy_perform(curl);
    //curl_easy_cleanup(curl);
    //std::cout<<buffer;
 //   fwrite( buffer.c_str(), buffer.length(), sizeof(char), stdout);
}
