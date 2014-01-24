PROJECT (qudt4dt_lib)
SET (LIBQUDT4DT_MODELICA_SRC qudtUnit.cpp)

ADD_LIBRARY(libqudt4dt_modelica STATIC ${LIBQUDT4DT_MODELICA_SRC})
target_link_libraries()