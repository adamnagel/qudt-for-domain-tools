#include "unit/modelicaUnit.hpp"


namespace qudt4dt
{
namespace modelica
{
//TODO: failure processing
ModelicaUnit::ModelicaUnit(const std::string& url):url(url)
{
    queryClassPath();
}

bool ModelicaUnit::queryClassPath()
{
if(false == query_attr("ClassPath", ClassPath))
    return false;
return true;

}

std::string ModelicaUnit::getClassPath()const
{
    return ClassPath;
}

std::string ModelicaUnit::getUrl()const
{
    return url;
}

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
