rm -rf fuseki-data
mkdir fuseki-data
pushd jena-fuseki-0.2.7
./fuseki-server -q --update --loc=../fuseki-data /ds
