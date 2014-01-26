#ifndef QUDT4DT_DETAIL_UTILS_HPP
#define QUDT4DT_DETAIL_UTILS_HPP
#include <iostream>
#include <string>
#include <cstdlib>
#include <boost/static_assert.hpp>

namespace qudt4dt
{
namespace detail
{

#define ASSERT_WITH_MSG(cond, msg) do                                   \
    { if (!(cond))                                                      \
        {                                                               \
            std::ostringstream str;                                     \
            str << msg;                                                 \
            std::cerr << str.str()<<"at"<<__FILE__<<' '<<__LINE__;      \
            std::abort();                                               \
        }                                                               \
} while(0)

template <class T>
struct always_false
{
    enum{value = false };
};


template<class T>
class maybe
{
    bool is_initialized;
    T value;
public:
    maybe(bool _e = false) : is_initialized(_e){};
    maybe(const T& _v, bool _e = true) : value(_v), is_initialized(_e){};
    maybe(const maybe<T>& rhs) : is_initialized(rhs.is_initialized), value(rhs.value){};
    bool is_existed()const {return is_initialized;};
    operator T() const{return value;};
    operator T&() {return value;};
    //operator T() const{return value;};
    ~maybe(){};
};
// template<class T>
// friend std::istream& operator>>(std::istream& ins, maybe<T>& _m)
// {
//     std::string input;
//     ins>>input;
//     if(0 == input.length())
//     {
//         _m.is_initialized = false;
//     }
//     else
//     {
        
//     }
// }

};//namespace detail
};//namespace qudt4dt


#endif //QUDT4DT_UTILS_HPP













