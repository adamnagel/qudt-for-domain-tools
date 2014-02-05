#include "unit/mdaoUnit.hpp"

namespace qudt4dt
{
namespace mdao
{
//TODO::error processing.
MdaoUnit::MdaoUnit(const std::string& url)
	:url(url)
{
	queryUnitName();
}

bool MdaoUnit::queryUnitName()
{
	return query_attr("UnitName", UnitName);
}

bool MdaoUnit::queryComment()
{
	return query_attr<std::string>("Comment", Comment);
}

std::string MdaoUnit::getUrl()const
{
	return url;
}
template<class T>
bool MdaoUnit::query_attr(const std::string& attr_name, T& attr)
{
    std::string querycontext_template = "PREFIX mdao: <http://openmdao.org/units#>\nSELECT ?x\nWHERE\n{\n    <%1%> mdao:%2% ?x\n}";
    std::string _q = str(boost::format(querycontext_template) % url % attr_name);
    if(false == query_get_attr(_q, attr))
        return false;
    return true;

}
}
}
