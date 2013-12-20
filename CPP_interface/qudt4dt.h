#ifndef QUDT4DT_H
#define QUDT4DT_H
#include <string>
#include <length.h>
namespace qudt4dt
{
    template <class T>
    class unit
    {
        friend std::ostream& operator<<(std::ostream& os,const unit<T>& u)
        {
            os<<u.getName();
            return os;
        };
    public:
        unit(std::string name, double factor, double offset):name(name),factor(factor),offset(offset){};
        std::string getName()const{return name;};
        double getFactor()const{return factor;};
        double getOffset()const{return offset;};
        virtual ~unit(){};
    private:
        const std::string name;
        const double factor;
        const double offset;
        unit(){};
    };
    
    static unit<Length> inch("inch", 0.0254, 0 );
    static unit<Length> meter("meter", 1, 0);
    
    
    template <class T>
    class quantity
    {
        friend std::ostream& operator<<(std::ostream& os,const quantity<T>& qu)
        {
            os<<qu.getNum()<<' '<<qu.getUnit();
            return os;
        };
    public:
        quantity(const unit<T>& u):num(1),u(u){};
        quantity(const quantity<T>& rhs):num(rhs.num), u(rhs.u){};
        quantity(double num, const unit<T>& u):num(num),u(u){};
        const unit<T>& getUnit()const {return u;};
        double getNum()const {return num;};
        virtual ~quantity(){};
    private:
        double num;
        const unit<T>& u;
    };
    template <class T>
    quantity<T> operator*(double num, const unit<T>& u){return quantity<T>(num, u);};
    
    template <class T>
    quantity<T> quantity_cast(const unit<T>& obj, const quantity<T>& src){
        const unit<T>& srcu = src.getUnit();
        double src_factor = srcu.getFactor();
        double src_offset = srcu.getOffset();
        double obj_factor = obj.getFactor();
        double obj_offset = obj.getOffset();
        double num = ((src_offset - obj_offset) + src.getNum()) * src_factor / obj_factor;
        return quantity<T>(num, obj);
    }
    
    //void Init(std::string);
//    template<S,D>
  //  D quantity_cast(S&);
    
  //  template<U,T>
   // U unit_cast(quantity<T>&);
    
}

#endif //QUDT4DT_H
