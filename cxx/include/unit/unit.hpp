#ifndef QUDT4DT_UNIT_HPP
#define QUDT4DT_UNIT_HPP
#include <sparql/sparql.hpp>
#include <boost/lexical_cast.hpp>
#include <utils.hpp>
namespace qudt4dt
{

template <class _to, class _from>
_to unit_cast(_from _s)
{
    BOOST_STATIC_ASSERT_MSG(detail::always_false<_to>::value, "no corresponding unit casting");
};


namespace detail{
inline bool query_get_str(const std::string& query_context, std::string& ret)
{
    std::vector<std::string> _v;
    if(false == sparql::query(query_context, _v))
        return false;

    if(true == _v.empty())
        ret = "";
    else
        ret = _v.at(0);
    return true;
}
};//namespace detail
template<class T>
bool query_get_attr(const std::string& query_context, T& ret)
{
    std::string _s;
    if(false == detail::query_get_str(query_context, _s))
        return false;
    ASSERT_WITH_MSG("" != _s, "can not get the arrtibute with\n-----------------------------------------------\n" + query_context);
    ret = boost::lexical_cast<T>(_s);
    return true;
}

template<class T>
bool query_get_attr(const std::string& query_context, detail::maybe<T>& ret)
{
    std::string _s;
    if(false == detail::query_get_str(query_context, _s))
        return false;
    if("" != _s)
        ret = detail::maybe<T>(boost::lexical_cast<T>(_s));
    else
        ret = detail::maybe<T>();
    return true;
}

};//namespace qudt4dt
#endif //QUDT4DT_UNIT_HPP















