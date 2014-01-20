#ifndef QUDT4DT_HPP
#define QUDT4DT_HPP
#include <string>
#include <length.h>
#include <boost/format.hpp>
#include <boost/lexical_cast.hpp>
#include <sparql/sparql.h>
namespace qudt4dt
{
    template <class T>
    class QudtUnit
    {
    public:
        QudtUnit(const std::string& url);
        std::string getUrl()const;
        double getFactor()const;
        double getOffset()const;
        std::string getUnitName()const;
        virtual ~QudtUnit(){};
    private:
        bool queryFactor();
        bool queryOffset();
        const std::string url;
        std::string unitName;
        double factor;
        double offset;
    };

    

    //TODO: failure processing
    template <class T>
    QudtUnit<T>::QudtUnit(const std::string& url):url(url)
    {
        queryFactor();
        queryOffset();
    };

    template <class T>
    std::string QudtUnit<T>::getUrl()const
    {
        return url;
    }

    template <class T>
    std::string QudtUnit<T>::getUnitName()const
    {
        return unitName;
    }
    
    template <class T>
    double QudtUnit<T>::getFactor()const
    {
        return factor;
    }
    
    template <class T>
    double QudtUnit<T>::getOffset()const
    {
        return offset;
    }

    template <class T>
    bool QudtUnit<T>::queryOffset()
    {
        std::string temp_q = "PREFIX qudt: <http://qudt.org/schema/qudt#>\n        SELECT\n        ?x\n        WHERE\n        {\n        <%1%> qudt:conversionOffset ?x.\n        }\n";
        std::string _q = str(boost::format(temp_q) % url);
        std::vector<std::string> ret;
        if(!query(_q, ret))
           return false;
        
        offset = boost::lexical_cast<double>(ret.at(0));
        //std::cout<<offset<<std::endl;
        return true;
    }

    template <class T>
    bool QudtUnit<T>::queryFactor()
    {
        std::string temp_q = "PREFIX qudt: <http://qudt.org/schema/qudt#>\n        SELECT\n        ?x\n        WHERE\n        {\n        <%1%> qudt:conversionMultiplier ?x.\n        }\n";
        std::string _q = str(boost::format(temp_q) % url);
        std::vector<std::string> ret;
        if(!query(_q, ret))
            return false;

        factor = boost::lexical_cast<double>(ret.at(0));
        return true;
    }
    
    template <class T>
    std::ostream& operator<<(std::ostream& os,const QudtUnit<T>& u)
    {
        os<<u.getUrl();
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

#endif //QUDT4DT_HPP
