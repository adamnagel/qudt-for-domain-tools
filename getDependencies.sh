echo "===== Downloading QUDT OWL files ====="

mkdir -p qudt-owl
curl 'http://www.linkedmodel.org/1.0/schema/dtype' > qudt-owl/dtype.xml
curl 'http://qudt.org/1.1/schema/dimension' > qudt-owl/dimension.xml
curl 'http://qudt.org/1.1/schema/quantity' > qudt-owl/quantity.xml
curl 'http://qudt.org/1.1/schema/qudt' > qudt-owl/qudt.xml
curl 'http://www.linkedmodel.org/1.2/schema/vaem' > qudt-owl/vaem.xml
curl 'http://voag.linkedmodel.org/1.0/schema/voag' > qudt-owl/voag.xml
curl 'http://qudt.org/1.1/vocab/dimensionalunit' > qudt-owl/dimensionalunit.xml
curl 'http://qudt.org/1.1/vocab/dimension' > qudt-owl/dimension.xml
curl 'http://qudt.org/1.1/vocab/quantity' > qudt-owl/quantity.xml
curl 'http://qudt.org/1.1/vocab/unit' > qudt-owl/unit.xml
curl 'https://github.com/OpenMDAO/OpenMDAO-Framework/raw/master/openmdao.units/openmdao/units/unitLibdefault.ini' > openMDAO/unitLibdefault.ini

echo "===== Downloading Jena Fuseki server ====="
curl 'http://www.apache.org/dist/jena/binaries/jena-fuseki-0.2.7-distribution.tar.gz' > jena-fuseki.tar.gz
tar -xvf jena-fuseki.tar.gz
rm jena-fuseki.tar.gz
