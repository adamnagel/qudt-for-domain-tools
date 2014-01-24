#include "qudtUnit.hpp"

namespace qudt4dt{

//TODO: failure processing
QudtUnit::QudtUnit(const std::string& url):url(url)
{
    queryFactor();
    queryOffset();
};

std::string QudtUnit::getUrl()const
{
    return url;
}

// std::string QudtUnit::getUnitName()const
// {
//     return unitName;
// }
    
double QudtUnit::getFactor()const
{
    return factor;
}
    
double QudtUnit::getOffset()const
{
    return offset;
}

bool QudtUnit::queryOffset()
{    
    if(false == query_attr<double>("conversionOffset", offset))
        return false;
    return true;
}

bool QudtUnit::queryFactor()
{
    if(false == query_attr<double>("conversionMultiplier", factor))
        return false;
    return true;
}


std::ostream& operator<<(std::ostream& os,const QudtUnit& u)
{
    os<<u.getUrl();
    return os;
}

}//namespace qudt4dt
