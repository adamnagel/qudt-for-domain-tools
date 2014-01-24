#ifndef MODELICAUNIT_HPP
#define MODELICAUNIT_HPP
#include "utils.hpp"
#include "qudtUnit.hpp"
#include <string>

#include <boost/format.hpp>

namespace qudt4dt
{
namespace modelica
{

class ModelicaUnit
{
public:
    typedef ModelicaUnit unit_type;
    
    ModelicaUnit(const std::string& url);
    QudtUnit operator QudtUnit() const;

    std::string getUrl()const;
    double getMax()const;
    double getMin()const;
    double getStart()const;
    std::string getDisplayUnit()const;
    std::string getUnit()const;
    std::string getClassPath()const;
priveate:
    bool queryClassPath();
    bool queryUnit();
    bool queryMax();
    bool queryMin();
    bool queryStart();
    bool queryDisplayUnit();
    template<class T>
    bool query_attr(const std::string&, T&);
    maybe<std::string> Quantity;
    maybe<std::string> Unit;
    std::string ClassPath;
    maybe<double> Min;
    maybe<double> Max;
    maybe<double> Start;
    maybe<string> DisplayUnit;
    std::string url;
};
    
template<class T>
bool ModelicaUnit::query_attr(const std::string& attr_name, T& attr)
{
    std::string querycontext_template = "PREFIX qudt: <http://qudt.org/schema/qudt#>\nPREFIX modelica: <http://modelica.org/msl/SIUnits/vocabulary#>\nSELECT\n?x\nWHERE\n{\n    <%1%> modelica:%2% ?x\n}";
    std::string _q = str(boost::format(querycontext_template) % url % attr_name);
    if(false == query_get_attr(_q, attr))
        return false;
    return true;

}

};//namespace modelica
};//namespace qudt4dt














#endif //MODELICAUNIT_HPP
