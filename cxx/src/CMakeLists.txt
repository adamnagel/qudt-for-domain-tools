cmake_minimum_required(VERSION 2.8)
#--------------------------------------------------------
#add_subdirectory(unit)
#add_subdirectory(sparql)
#---------------------------------------------------------
set (inc_dir ${PROJECT_SOURCE_DIR}/include/)
include_directories(${inc_dir})
#---------------------------------------------------------
add_library(libqudt4dt STATIC "qudt4dt.cpp" "sparql.cpp" "qudtUnit.cpp")
target_link_libraries(libqudt4dt jsoncpp curl.lib)
#------------------------cache-----------------------------


find_package(Boost)
if(Boost_FOUND)
    include_directories("${Boost_INCLUDE_DIRS}/")
  endif()

  link_directories(${PROJECT_SOURCE_DIR}/lib/win/)
