#include <qudt4dt.h>
#include <modelica.h>
#include <iostream>
int main(int argc, char *argv[])
{
    //qudt4dt::Init("http://192.168.1.12:3030/");

    auto a = qudt4dt::QudtQuantity<qudt4dt::Length>(2*qudt4dt::meter);
    auto b = qudt4dt::quantity_cast(qudt4dt::inch,a);

    qudt4dt::ModelicaQuantity m(b);
    auto n = qudt4dt::ModelicaQuantity(3,"sample unit url");
    std::cout<<a<<std::endl;
    std::cout<<b<<std::endl;

    return 0;
}

/*
0.05 m
2 inch
*/
