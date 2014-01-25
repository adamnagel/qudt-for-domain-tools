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
};//namespace qudt4dt
};//namespace modelica
