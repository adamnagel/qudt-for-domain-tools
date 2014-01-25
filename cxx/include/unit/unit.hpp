#ifndef QUDT4DT_UNIT_HPP
#define QUDT4DT_UNIT_HPP
#include <sparql/sparql.hpp>
namespace qudt4dt
{

template <class _to, class _from>
_to unit_cast(_from _s);

template<class T>
bool query_get_attr(const std::string& query_context, T& ret)
{
    std::vector<std::string> _v;
    if(false == query(query_context, _v))
        return false;
         
    ret = boost::lexical_cast<T>(_v.at(0));
    return true;
}
};//namespace qudt4dt
#endif //QUDT4DT_UNIT_HPP
