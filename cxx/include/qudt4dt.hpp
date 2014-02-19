#ifndef QUDT4DT_HPP
#define QUDT4DT_HPP
#include <string>
namespace qudt4dt
{
extern double LIB_VERSION;
void init_qudt4dt_server(const std::string& server_url);
};

#include "quantity.hpp"

//-----------------------unit-----------------------------------
#include "unit/qudtUnit.hpp"
#include "unit/modelicaUnit.hpp"
#include "unit/mdaoUnit.hpp"


//
//namespace qudt4dt
//{
//template <class _from>
//inline QudtUnit unit_cast(const _from& _s)
//{
//	//should not come to here
//	BOOST_STATIC_ASSERT_MSG(detail::always_false<_from>::value, "no corresponding unit casting");
//}
//
//template <class _to>
//inline _to unit_cast(const QudtUnit& _s)
//{
//	//should not come to here
//	BOOST_STATIC_ASSERT_MSG(detail::always_false<_to>::value, "no corresponding unit casting");
//}
//
//}


#endif// QUDT4DT_HPP

















