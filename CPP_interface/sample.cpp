#include <qudt4dt.hpp>
#include <modelica.h>
#include <iostream>
int main(int argc, char *argv[])
{
    
    qudt4dt::init_qudt_server("http://127.0.0.1:3030");
    qudt4dt::QudtUnit<qudt4dt::Length> inch("http://qudt.org/vocab/unit#Inch" );
    qudt4dt::QudtUnit<qudt4dt::Length> meter("http://qudt.org/vocab/unit#Meter");
    auto a = qudt4dt::QudtQuantity<qudt4dt::Length>(2*meter);
    auto b = qudt4dt::quantity_cast(inch,a);

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

