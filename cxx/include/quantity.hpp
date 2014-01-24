#ifndef QUDT4DT_QUANTITY_HPP
#define QUDT4DT_QUANTITY_HPP


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
    double num;
    const _unit u;
};


template <class _unit>
Quantity<_unit>::Quantity(const _unit& u, double num):u(u), num(num){};

template <class _unit>
Quantity<_unit>::Quantity(const Quantity<_unit>& rhs):num(rhs.num), u(rhs.u){};

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
    double src_factor = srcu.getFactor();
    double src_offset = srcu.getOffset();
    double obj_factor = obj.getFactor();
    double obj_offset = obj.getOffset();
    double num = ((src_offset - obj_offset) + src.getNum()) * src_factor / obj_factor;
    return Quantity<_unit>(obj, num);
}
    

#endif //QUDT4DT_QUANTITY_HPP










