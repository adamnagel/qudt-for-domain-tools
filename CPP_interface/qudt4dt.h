#ifndef QUDT4DT_H
#define QUDT4DT_H
#include <string>
#include <length.h>
namespace qudt4dt
{
    //TODO: database accessing
    template <class T>
    class QudtUnit
    {
    public:
        QudtUnit(std::string name, double factor, double offset):name(name),factor(factor),offset(offset){};
        std::string getName()const{return name;};
        double getFactor()const{return factor;};
        double getOffset()const{return offset;};
        virtual ~QudtUnit(){};
    private:
        const std::string name;
        const double factor;
        const double offset;
    };
    
    static QudtUnit<Length> inch("inch", 0.0254, 0 );
    static QudtUnit<Length> meter("meter", 1, 0);
    
    template <class T>
    std::ostream& operator<<(std::ostream& os,const QudtUnit<T>& u)
    {
        os<<u.getName();
        return os;
    }
    
    template <class T>
    class QudtQuantity
    {
    public:
        QudtQuantity(const QudtUnit<T>& u):num(1),u(u){};
        QudtQuantity(const QudtQuantity<T>& rhs):num(rhs.num), u(rhs.u){};
        QudtQuantity(double num, const QudtUnit<T>& u):num(num),u(u){};
        const QudtUnit<T>& getUnit()const {return u;};
        double getNum()const {return num;};
        virtual ~QudtQuantity(){};
    private:
        double num;
        const QudtUnit<T>& u;
    };
    template <class T>
    QudtQuantity<T> operator*(double num, const QudtUnit<T>& u){return QudtQuantity<T>(num, u);};
    
    template <class T>
    std::ostream& operator<<(std::ostream& os,const QudtQuantity<T>& qudt_q)
    {
        os<<qudt_q.getNum()<<' '<<qudt_q.getUnit();
        return os;
    };
    
    template <class T>
    QudtQuantity<T> quantity_cast(const QudtUnit<T>& obj, const QudtQuantity<T>& src){
        const QudtUnit<T>& srcu = src.getUnit();
        double src_factor = srcu.getFactor();
        double src_offset = srcu.getOffset();
        double obj_factor = obj.getFactor();
        double obj_offset = obj.getOffset();
        double num = ((src_offset - obj_offset) + src.getNum()) * src_factor / obj_factor;
        return QudtQuantity<T>(num, obj);
    }
    
    //void Init(std::string);
//    template<S,D>
  //  D quantity_cast(S&);
    
  //  template<U,T>
   // U unit_cast(quantity<T>&);
    
}

#endif //QUDT4DT_H
