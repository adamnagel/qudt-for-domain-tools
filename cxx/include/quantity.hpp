#ifndef QUDT4DT_QUANTITY_HPP
#define QUDT4DT_QUANTITY_HPP

#include <stdexcept>

#include <unit/qudtUnit.hpp>
namespace qudt4dt
{
template <class _unit>
class Quantity
{
public:
    typedef typename _unit::unit_type unit_type;
    
    Quantity(const _unit&, double num = 1);
    Quantity(const Quantity<_unit>&);
    const _unit& getUnit()const;
    const double& getNum()const;
    virtual ~Quantity(){};
private:
    const _unit u;
    double num;
};


template <class _unit>
Quantity<_unit>::Quantity(const _unit& u, double num):u(u), num(num){};

template <class _unit>
Quantity<_unit>::Quantity(const Quantity<_unit>& rhs):u(rhs.u), num(rhs.num){};

template <class _unit>
const _unit& Quantity<_unit>::getUnit()const
{
    return u;
};

template <class _unit>
Quantity<_unit> operator*(double num, const _unit& u)
{
    return Quantity<_unit>(u, num);
};

template <class _unit>
const double& Quantity<_unit>::getNum()const
{
    return num;
};


template <class _unit>
std::ostream& operator<<(std::ostream& os,const Quantity<_unit>& _q)
{
    os<<_q.getNum()<<" ";
    os<<_q.getUnit();
    return os;
};
    
template <class _unit>
Quantity<_unit> quantity_cast(const _unit& obj, const Quantity<_unit>& src){
    const _unit& srcu = src.getUnit();
    if(srcu.getUnitClass() != obj.getUnitClass())
        throw std::domain_error("convertion happened in the units with different unit classes");
    double src_factor = srcu.getFactor();
    double src_offset = srcu.getOffset();
    double obj_factor = obj.getFactor();
    double obj_offset = obj.getOffset();
    double num = ((src_offset - obj_offset) + src.getNum()) * src_factor / obj_factor;
    return Quantity<_unit>(obj, num);
}
    
template<class _to, class _from>
typename qudt4dt::Quantity<_to> unit_cast(const Quantity<_from>& _qs)
{
	return Quantity<_to>(
			unit_cast<_to>(_qs.getUnit()),
			_qs.getNum());

}

}; //namespace qudt4dt
#endif //QUDT4DT_QUANTITY_HPP










