#include "unit/qudtUnit.hpp"

namespace qudt4dt{

//TODO: failure processing
QudtUnit::QudtUnit(const std::string& url):url(url)
{
    queryFactor();
    queryOffset();
    queryUnitClass();
};

std::string QudtUnit::getUnitClass()const
{
    return unitClass;
}
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
bool QudtUnit::queryUnitClass()
{
    std::string querycontext_template = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\nPREFIX owl: <http://www.w3.org/2002/07/owl#>\nSELECT\n?x \nWHERE\n{\n    <%1%> rdf:type ?x. \n    FILTER NOT EXISTS{?x rdf:type owl:DeprecatedClass}\n}";
    std::string _q = str(boost::format(querycontext_template) % url);
    if(false == query_get_attr(_q, unitClass))
        return false;
    return true;
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


template<class T>
bool QudtUnit::query_attr(const std::string& attr_name, T& attr)
{
    std::string querycontext_template = "PREFIX qudt: <http://qudt.org/schema/qudt#>\nSELECT\n?x\nWHERE\n{\n    <%1%> qudt:%2% ?x.\n}\n";
    std::string _q = str(boost::format(querycontext_template) % url % attr_name);
    if(false == query_get_attr(_q, attr))
        return false;
    return true;
}

}//namespace qudt4dt