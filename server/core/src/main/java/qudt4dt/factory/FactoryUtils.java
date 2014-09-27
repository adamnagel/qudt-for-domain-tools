package qudt4dt.factory;

import com.hp.hpl.jena.query.ResultSet;
import qudt4dt.Sparql;
import qudt4dt.thrift.Unit;

/**
 * Created by yli on 6/3/14.
 */
public final class FactoryUtils {
    static public String ontology_server_address;
    static public Sparql ontology;
    
    //TODO:: use annotation to sign domain function
    static public final String domain[] = {"modelica", "mdao"};

    @Deprecated
    static public Unit getunit_modelica(Unit input){
        String query_text = "PREFIX ontology: <http://qudt4dt.org/ontology#>\n" +
                "SELECT\n" +
                "?key\n" +
                "WHERE\n" +
                "{ \n" +
                "?key ontology:equivalentOf <%s>.\n" +
                "?key a <http://modelica.org/msl/SIUnits/vocabulary#ModelicaUnitClass>\n" +
                "}\n";
        return get_domain_unit(input, query_text);

    }

    @Deprecated
    static public Unit getunit_mdao(Unit input){
        String query_text = "PREFIX ontology: <http://qudt4dt.org/ontology#>\n" +
                "SELECT\n" +
                "?key\n" +
                "WHERE\n" +
                "{ \n" +
                "?key ontology:equivalentOf <%s>.\n" +
                "?key a <http://openmdao.org/units#BaseUnit>\n" +
                "}\n";
        return get_domain_unit(input, query_text);
    }

    @Deprecated
    static public Unit get_SI_unit(Unit input){
        String query_text = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n" +
                "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n" +
                "PREFIX qudt: <http://qudt.org/schema/qudt#>\n" +
                "SELECT\n" +
                "?key\n" +
                "WHERE\n" +
                "{\n" +
                "<%s> rdf:type ?class.\n" +
                "FILTER NOT EXISTS{?class rdf:type owl:DeprecatedClass}.\n" +
                "?key rdf:type ?class.\n" +
                "{?key rdf:type qudt:SIDerivedUnit}\n" +
                "UNION\n" +
                "{?key rdf:type qudt:SIBaseUnit}\n" +
                "}";
        ResultSet rs = FactoryUtils.ontology.query(String.format(query_text, input.qudt_url));

        if(false == rs.hasNext())
            return null;
        else{
            UnitFactory _f = new UnitFactory(rs.next().get("key").toString());
            return _f.create_ins();
        }
    }

    static public ResultSet get_SI_domain_unit(Unit input){
        String query_text = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n" +
                "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n" +
                "PREFIX qudt: <http://qudt.org/schema/qudt#>\n" +
                "PREFIX ontology: <http://qudt4dt.org/ontology#>\n" +
                "SELECT\n" +
                "?si ?mdao ?modelica\n" +
                "WHERE\n" +
                "{\n" +
                "    BIND (<%s> AS ?unit).\n" +
                "    ?unit rdf:type ?class.\n" +
                "    FILTER NOT EXISTS{?class rdf:type owl:DeprecatedClass}.\n" +
                "    ?si rdf:type ?class.\n" +
                "    {?si rdf:type qudt:SIDerivedUnit}\n" +
                "    UNION\n" +
                "    {?si rdf:type qudt:SIBaseUnit}.\n" +
                "    ?mdao ontology:equivalentOf ?si.\n" +
                "    ?mdao a <http://openmdao.org/units#BaseUnit>.\n" +
                "    ?modelica ontology:equivalentOf ?si.\n" +
                "    ?modelica a <http://modelica.org/msl/SIUnits/vocabulary#ModelicaUnitClass>. \n" +
                "}";
        return FactoryUtils.ontology.query(String.format(query_text, input.qudt_url));
    }

    static private Unit get_domain_unit(Unit input, String query_text){
        ResultSet rs = FactoryUtils.ontology.query(String.format(query_text, input.qudt_url));

        if(false == rs.hasNext())
            return null;
        else{
            Unit result = new Unit();
            result.setUrl(rs.next().get("key").toString());
            result.setQudt_url(input.getQudt_url());
            result.setQudt_attr(input.getQudt_attr());
            return result;
        }
    }


}
