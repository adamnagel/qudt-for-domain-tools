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

echo "===== Downloading OpenMDAO Unit INI file"
curl 'https://raw.github.com/OpenMDAO/OpenMDAO-Framework/master/openmdao.units/openmdao/units/unitLibdefault.ini' > openMDAO/unitLibdefault.ini
sed -i.bak 's/\r//' openMDAO/unitLibdefault.ini

echo "===== Downloading Requests v1.2.3"
git clone https://github.com/kennethreitz/requests.git --depth 0 -b v1.2.3


echo "===== Downloading Jena Fuseki server ====="
curl 'http://www.apache.org/dist/jena/binaries/jena-fuseki-1.0.0-distribution.tar.gz' > jena-fuseki.tar.gz
rm -rf jena-fuseki
tar -xvf jena-fuseki.tar.gz
rm jena-fuseki.tar.gz
mv jena-fuseki-1.0.0 jena-fuseki
