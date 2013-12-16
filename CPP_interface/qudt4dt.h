#ifndef QUDT4DT_H
#define QUDT4DT_H

namespace qudt4dt
{
    template <class T>
    class quantity
    {
    public:
        quantity();
        quantity(const quantity&);
        ~quantity();
        get_factor();
        get_offset();
    private:
        double factor;
        double offset;
    }
    
    
    void Init(std::string);
    template<S,D>
    D quantity_cast(S&);
    
    template<U,T>
    U unit_cast(quantity<T>&);
    
}

#endif //QUDT4DT_H