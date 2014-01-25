cmake_minimum_required(VERSION 2.8)
#--------------------------------------------------------
project (qudt4dt)

add_subdirectory (src)
#---------------------------------------------------------
set (inc_dir ${PROJECT_SOURCE_DIR}/include/)
set (sample_src sample.cpp)
#---------------------------------------------------------
include_directories(${inc_dir})
add_executable(sample ${sample_src})
target_link_libraries(sample libqudt4dt jsoncpp curl.lib)
#---------------------------------------------------------
if(CMAKE_COMPILER_IS_GNUCXX)
    set(CMAKE_CXX_FLAGS "-std=c++0x")  
  endif()

  
find_package(Boost)
if(Boost_FOUND)
    include_directories("${Boost_INCLUDE_DIRS}/")
endif()
set(BOOST_ROOT CACHE PATH "")

link_directories(${PROJECT_SOURCE_DIR}/lib/win/)

