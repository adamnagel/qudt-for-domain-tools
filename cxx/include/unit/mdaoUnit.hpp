#ifndef QUDT4DT_MDAO_MDAOUNIT_HPP
#define QUDT4DT_MDAO_MDAOUNIT_HPP

#include <string>
#include <boost/format.hpp>
#include <stdexcept>

#include <unit/qudtUnit.hpp>
namespace qudt4dt
{

namespace mdao
{

class MdaoUnit
{
public:
	typedef MdaoUnit unit_type;

    MdaoUnit(const std::string& url);

    std::string getUrl()const;
    std::string getComment()const;
    double getFactor()const;
    double getOffset()const;
    std::string getQuantityName()const;
    std::string getUnitName()const;
    std::string getUnitExpression()const;
private:
    bool queryComment();
    bool queryFactor();
    bool queryOffset();
    bool queryQuantityName();
    bool queryUnitName();
    bool queryUnitExpression();
    template<class T>
    bool query_attr(const std::string&, T&);
    std::string url;
    detail::maybe<std::string> Comment;
    detail::maybe<std::string> UnitExpression;
    std::string UnitName;
    detail::maybe<double> Offset;
    detail::maybe<double> Factor;
    std::string QuantityName;
};


};//namespace mdao


template <>
inline QudtUnit unit_cast(const mdao::MdaoUnit& _s)
{
    std::string querycontext_template = "PREFIX ontology: <http://qudt4dt.org/ontology#>\nSELECT\n?x\nWHERE\n{ \n    <%1%> ontology:equivalentOf ?x\n}";
    std::string ret_url, _q = str(boost::format(querycontext_template) % _s.getUrl());
    if(false == query_get_attr(_q, ret_url))
        throw std::runtime_error("can not find corresponding qudt unit with the url:" + _s.getUrl());
    //TODO : adding log
    return QudtUnit(ret_url);
}

template <>
inline mdao::MdaoUnit unit_cast(const QudtUnit& _s)
{
    std::string querycontext_template = "PREFIX ontology: <http://qudt4dt.org/ontology#>\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\nSELECT\n?x\nWHERE\n{ \n    ?x ontology:equivalentOf <%1%>.\n    <http://openmdao.org/units#OpenMdaoUnit> ^rdfs:subClassOf+ ?class .\n    ?x a ?class\n}";
    std::string ret_url, _q = str(boost::format(querycontext_template) % _s.getUrl());
    if(false == query_get_attr(_q, ret_url))
        throw std::runtime_error("can not find corresponding qudt unit with the url:" + _s.getUrl());
    //TODO : adding log
    return mdao::MdaoUnit(ret_url);
}
};//namespace qudt4dt

#endif// QUDT4DT_MDAO_MDAOUNIT_HPP
