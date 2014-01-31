#ifndef QUDT4DT_QUDTUNIT_HPP
#define QUDT4DT_QUDTUNIT_HPP
#include <string>
#include <boost/format.hpp>

#include <unit/unit.hpp>

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
    std::string getUnitClass()const;
    //std::string getUnitName()const;
    virtual ~QudtUnit(){};
private:
    bool queryFactor();
    bool queryOffset();
    bool queryUnitClass();
    template<class T>
    bool query_attr(const std::string&,T&);
    const std::string url;
    std::string symbol;
    std::string unitClass;
    std::string abbreviation;
    //std::string unitName;
    detail::maybe<double> factor;
    detail::maybe<double> offset;
};

std::ostream& operator<<(std::ostream&,const QudtUnit&);



};//namespace qudt4dt   

    
    
#endif //QUDT4DT_QUDTUNIT_HPP














