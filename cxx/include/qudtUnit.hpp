#ifndef QUDT4DT_QUDTUNIT_HPP
#define QUDT4DT_QUDTUNIT_HPP
#include <string>
#include <boost/format.hpp>
#include <sparql/sparql.hpp>

#include "utils.hpp"
namespace qudt4dt
{
class QudtUnit
{
public:
    typedef QudtUnit unit_type;
    
    QudtUnit(const std::string& url);
    std::string getUrl()const;
    double getFactor()const;
    double getOffset()const;
    //std::string getUnitName()const;
    virtual ~QudtUnit(){};
private:
    bool queryFactor();
    bool queryOffset();
    template<class T>
    bool query_attr(const std::string&,T&);
    const std::string url;
    std::string symbol;
    std::string abbreviation;
    //std::string unitName;
    detail::maybe<double> factor;
    detail::maybe<double> offset;
};

std::ostream& operator<<(std::ostream&,const QudtUnit&);

template<class T>
bool QudtUnit::query_attr(const std::string& attr_name, T& attr)
{
    std::string querycontext_template = "PREFIX qudt: <http://qudt.org/schema/qudt#>\n SELECT\n ?x\n WHERE\n {\n        <%1%> qudt:%2% ?x.\n        }\n";
    std::string _q = str(boost::format(querycontext_template) % url % attr_name);
    if(false == query_get_attr(_q, attr))
        return false;
    return true;
}

};//namespace qudt4dt   

    
    
#endif //QUDT4DT_QUDTUNIT_HPP














