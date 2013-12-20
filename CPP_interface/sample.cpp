#include <qudt4dt.h>
#include <iostream>
int main(int argc, char *argv[])
{
    //qudt4dt::ModelicaUnitClass n = qudt4dt::ModelicaUnitClass(ModelicaUnitName,value);
    //qudt4dt::Init("http://192.168.1.12:3030/");

    auto a = qudt4dt::quantity<qudt4dt::Length>(2*qudt4dt::meter);
    auto b = qudt4dt::quantity_cast(qudt4dt::inch,a);

    //qudt4dt::ModelicaUnitClass m = qudt4dt::unit_cast<Modelica>(b);
    std::cout<<a<<std::endl;
    std::cout<<b<<std::endl;

    return 0;
}

/*
0.05 m
2 inch
*/
