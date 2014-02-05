#include <iostream>
#include <cassert>
#include <qudt4dt.hpp>
using namespace qudt4dt;


bool AreDoubleSame(double dFirstVal, double dSecondVal)
{
    return std::fabs(dFirstVal - dSecondVal) < 1E-3;
}

int main(int argc, char *argv[])
{
    
    init_qudt4dt_server("http://127.0.0.1:3030");

    //---------------------qudt unit and quantity caculation-----------------------
    QudtUnit inch("http://qudt.org/vocab/unit#Inch" );
    QudtUnit meter("http://qudt.org/vocab/unit#Meter");
    assert("http://qudt.org/vocab/unit#Inch" == inch.getUrl());
    assert("http://qudt.org/vocab/unit#Meter" == meter.getUrl());
    
    Quantity<QudtUnit> two_meters = Quantity<QudtUnit>(2* meter);
    assert(2 == two_meters.getNum() && "http://qudt.org/vocab/unit#Meter" == two_meters.getUnit().getUrl());

    auto two_meters_to_inch = quantity_cast(inch,two_meters);
    assert(AreDoubleSame(78.7402, two_meters_to_inch.getNum()) );
    assert("http://qudt.org/vocab/unit#Inch" == two_meters_to_inch.getUnit().getUrl());
    
    //---------------------modelica unit---------------------------------------------
    modelica::ModelicaUnit mass("http://modelica.org/msl/SIUnits/individuals#Mass");
    assert("http://modelica.org/msl/SIUnits/individuals#Mass" == mass.getUrl());
    assert("Modelica.SIunits.Mass" == mass.getClassPath());


    //---------------------convert to qudt unit from modelica unit-------------------
    auto qudt_mass = unit_cast<QudtUnit>(mass);
    assert("http://qudt.org/vocab/unit#Kilogram" == qudt_mass.getUrl());

    auto modelica_meter = unit_cast<modelica::ModelicaUnit>(meter);
    assert("http://modelica.org/msl/SIUnits/individuals#Length" == modelica_meter.getUrl());

    auto modelica_two_meters = unit_cast<modelica::ModelicaUnit>(two_meters);
    assert("http://modelica.org/msl/SIUnits/individuals#Length" == modelica_two_meters.getUnit().getUrl());
    //---------------------mdao unit--------------------------------------------------
    mdao::MdaoUnit m("http://openmdao.org/units/individuals#m");
    auto qudt_m = unit_cast<QudtUnit>(m);
    auto mdao_meter = unit_cast<mdao::MdaoUnit>(meter);
    assert(meter.getUrl() == qudt_m.getUrl());
    assert(m.getUrl() == mdao_meter.getUrl());

    //--------------------between mdao and modelica ----------------------------------
    auto modelica_m = unit_cast<modelica::ModelicaUnit>(m);
    auto mdao_mass = unit_cast<mdao::MdaoUnit>(mass);
    assert("http://modelica.org/msl/SIUnits/individuals#Length" == modelica_m.getUrl());
    assert("http://openmdao.org/units/individuals#kg" == mdao_mass.getUrl());
    //---
    std::cout<<"all green\n";
    return 0;
}

/*
  0.05 m
  2 inch
*/

