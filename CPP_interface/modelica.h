#ifndef MODELICA_H
#define MODELICA_H
#include <string>
#include <qudt4dt.h>
namespace qudt4dt
{
    class ModelicaQuantity{
    public:
        //TODO: unit name convertion from qudt to modelica
        template <class T>
        ModelicaQuantity(const QudtQuantity<T> rhs): value(rhs.getNum()),unitUrl(""){};
        ModelicaQuantity(double _v, const std::string& _s): value(_v),unitUrl(_s){};
    private:
        std::string unitUrl;
        double value;
    };
    
}

#endif