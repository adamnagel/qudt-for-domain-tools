cmake_minimum_required(VERSION 2.8)
#--------------------------------------------------------
project (qudt4dt_lib)

add_subdirectory(sparql)
#---------------------------------------------------------
set (current ${CMAKE_CURRENT_SOURCE_DIR})
set (inc_dir ${current}/../include)
set (libqudt4dt_src qudtUnit.cpp)
#---------------------------------------------------------
include_directories(${inc_dir})
add_library(libqudt4dt STATIC ${libqudt4dt_src})
target_link_libraries(libqudt4dt libqudt4dt_sparql)