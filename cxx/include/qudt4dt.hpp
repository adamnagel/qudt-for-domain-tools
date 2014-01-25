#ifndef QUDT4DT_HPP
#define QUDT4DT_HPP
#include <string>
namespace qudt4dt
{
extern double LIB_VERSION;
void init_qudt_server(const std::string& server_url);
};

#include "quantity.hpp"

//-----------------------unit-----------------------------------
#include "unit/qudtUnit.hpp"
#include "unit/modelicaUnit.hpp"


#endif// QUDT4DT_HPP

















