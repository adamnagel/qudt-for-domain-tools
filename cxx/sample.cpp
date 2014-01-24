#include <iostream>

#include <qudt4dt.hpp>
using namespace qudt4dt;
int main(int argc, char *argv[])
{
    
    init_qudt_server("http://127.0.0.1:3030");
    QudtUnit inch("http://qudt.org/vocab/unit#Inch" );
    QudtUnit meter("http://qudt.org/vocab/unit#Meter");
    auto a = Quantity<QudtUnit>(2*meter);
    auto b = quantity_cast(inch,a);

    // //qudt4dt::ModelicaQuantity m(b);
    // //auto n = qudt4dt::ModelicaQuantity(3,"sample unit url");
    std::cout<<a<<std::endl;
    std::cout<<b<<std::endl;

    return 0;
}

/*
  0.05 m
  2 inch
*/

