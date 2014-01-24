cmake_minimum_required(VERSION 2.8)
#-----------------------------------------------------------
project (qudt4dt_lib)

#------------------------------------------------------------
set (libqudt4dt_sparql_src sparql.cpp)
set (current ${CMAKE_CURRENT_SOURCE_DIR})
set (inc_dir ${current}/../../include)
#MESSAGE(STATUS "This dir is" ${inc_dir})
#--------------------------------------------------------------
include_directories(${inc_dir})

add_library(libqudt4dt_sparql STATIC ${libqudt4dt_sparql_src})
#---------------------------------------------------------------
link_directories(/usr/lib/x86_64-linux-gnu/ /usr/lib/)
target_link_libraries(libqudt4dt_sparql libcurl.so)
target_link_libraries(libqudt4dt_sparql libjsoncpp.so)