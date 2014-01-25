cmake_minimum_required(VERSION 2.8)
#-----------------------------------------------------------

#------------------------------------------------------------
set (sparql_src sparql.cpp)
set (inc_dir ${PROJECT_SOURCE_DIR}/include/)

#--------------------------------------------------------------
include_directories(${inc_dir})

add_library(sparql STATIC ${sparql_src})
#---------------------------------------------------------------
link_directories(/usr/lib/x86_64-linux-gnu/ /usr/lib/)

find_package(Boost)
if(Boost_FOUND)
    include_directories("${Boost_INCLUDE_DIRS}/")
    MESSAGE(STATUS "====${Boost_INCLUDE_DIRS}")
    target_link_libraries(sparql curl jsoncpp)
endif()

#-----------------------------------------------------------------




