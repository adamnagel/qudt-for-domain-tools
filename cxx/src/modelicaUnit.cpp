#include "unit/modelicaUnit.hpp"


namespace qudt4dt
{
namespace modelica
{
bool ModelicaUnit::queryClassPath()
{
if(false == query_attr("ClassPath", this->ClassPath))
    return false;
return true;


}
};
};
