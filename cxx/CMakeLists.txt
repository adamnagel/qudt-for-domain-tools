cmake_minimum_required(VERSION 2.8)
#--------------------------------------------------------
project (qudt4dt_lib)

add_subdirectory (src lib)
#---------------------------------------------------------
set (current ${CMAKE_CURRENT_SOURCE_DIR})
set (inc_dir ${current}/include)
set (sample_src sample.cpp)
#---------------------------------------------------------
include_directories(${inc_dir})
add_executable(sample ${sample_src})
target_link_libraries(sample libqudt4dt)
#target_link_libraries(sample libqudt4dt_sparql)
#---------------------------------------------------------
if(CMAKE_COMPILER_IS_GNUCXX)
    set(CMAKE_CXX_FLAGS "-std=c++0x")  
endif()
