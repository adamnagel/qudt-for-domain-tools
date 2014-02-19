#ifndef QUDT4DT_MODELICA_MODELICAUNIT_HPP
#define QUDT4DT_MODELICA_MODELICAUNIT_HPP

#include <string>
#include <boost/format.hpp>
#include <stdexcept>

#include <unit/qudtUnit.hpp>
namespace qudt4dt
{

namespace modelica
{

class ModelicaUnit
{
public:
    typedef ModelicaUnit unit_type;
    
    ModelicaUnit(const std::string& url);

    std::string getUrl()const;
    double getMax()const;
    double getMin()const;
    double getStart()const;
    std::string getDisplayUnit()const;
    std::string getUnit()const;
    std::string getClassPath()const;
private:
    bool queryClassPath();
    bool queryUnit();
    bool queryMax();
    bool queryMin();
    bool queryStart();
    bool queryDisplayUnit();
    template<class T>
    bool query_attr(const std::string&, T&);
    detail::maybe<std::string> Quantity;
    detail::maybe<std::string> Unit;
    std::string ClassPath;
    detail::maybe<double> Min;
    detail::maybe<double> Max;
    detail::maybe<double> Start;
    detail::maybe<std::string> DisplayUnit;
    std::string url;
};
    

};//namespace modelica


template <>
inline QudtUnit unit_cast(const modelica::ModelicaUnit& _s)
{
    std::string querycontext_template = "PREFIX ontology: <http://qudt4dt.org/ontology#>\nSELECT\n?x\nWHERE\n{ \n    <%1%> ontology:equivalentOf ?x\n}";
    std::string ret_url, _q = str(boost::format(querycontext_template) % _s.getUrl());
    if(false == query_get_attr(_q, ret_url))
        throw std::runtime_error("can not find corresponding qudt unit with the url:" + _s.getUrl());
    //TODO : adding log
    return QudtUnit(ret_url);
}

template <>
inline modelica::ModelicaUnit unit_cast(const QudtUnit& _s)
{
    std::string querycontext_template = "PREFIX ontology: <http://qudt4dt.org/ontology#>\nSELECT\n?x\nWHERE\n{ \n    ?x ontology:equivalentOf <%1%>.\n    ?x a <http://modelica.org/msl/SIUnits/vocabulary#ModelicaUnitClass>\n}";
    std::string ret_url, _q = str(boost::format(querycontext_template) % _s.getUrl());
    if(false == query_get_attr(_q, ret_url))
        throw std::runtime_error("can not find corresponding qudt unit with the url:" + _s.getUrl());
    //TODO : adding log
    return modelica::ModelicaUnit(ret_url);
}
};//namespace qudt4dt

#endif// QUDT4DT_MODELICA_MODELICAUNIT_HPP













