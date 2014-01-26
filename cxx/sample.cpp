#include <iostream>

#include <qudt4dt.hpp>
using namespace qudt4dt;
int main(int argc, char *argv[])
{
    
    init_qudt_server("http://127.0.0.1:3030");

    std::cout<<"---------------------qudt unit and quantity caculation------------------"<<std::endl;
    QudtUnit inch("http://qudt.org/vocab/unit#Inch" );
    QudtUnit meter("http://qudt.org/vocab/unit#Meter");
    std::cout<<inch<<std::endl;
    std::cout<<meter<<std::endl;
    
    auto a = Quantity<QudtUnit>(2*meter);
    std::cout<<a<<std::endl;
    
    auto b = quantity_cast(inch,a);
    std::cout<<"2*meter = "<<b<<std::endl;
    
    std::cout<<"---------------------modelica unit--------------------------------------"<<std::endl;
    modelica::ModelicaUnit mass("http://modelica.org/msl/SIUnits/individuals#Mass");
    std::cout<<"modelica unit url: "<<mass.getUrl()<<std::endl;
    std::cout<<"modelica unit classPath: "<<mass.getClassPath()<<std::endl;

    std::cout<<"---------------------convert to qudt unit from modelica unit------------"<<std::endl;
    auto m2q_unit = unit_cast<QudtUnit>(mass);
    std::cout<<"corresponding qudt url:"<<m2q_unit.getUrl()<<std::endl;

    return 0;
}

/*
  0.05 m
  2 inch
*/

