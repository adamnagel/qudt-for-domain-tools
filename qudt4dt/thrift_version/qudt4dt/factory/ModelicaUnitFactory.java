package qudt4dt.factory;

import com.hp.hpl.jena.query.ResultSet;
import com.hp.hpl.jena.rdf.model.RDFNode;
import qudt4dt.thrift.ModelicaUnit;

/**
 * Created by yli on 5/8/14.
 */
public class ModelicaUnitFactory extends Factory {
    public ModelicaUnitFactory(String qudt_url, String _ontology_server_address){
        super(_ontology_server_address);
        init(qudt_url);

    }

    //finding corresponding modelica unit
    private void init(String qudt_url){
        String query_text = "PREFIX ontology: <http://qudt4dt.org/ontology#>\n" +
                "SELECT\n" +
                "?key\n" +
                "WHERE\n" +
                "{ \n" +
                "?key ontology:equivalentOf <%s>.\n" +
                "?key a <http://modelica.org/msl/SIUnits/vocabulary#ModelicaUnitClass>\n" +
                "}\n";

        ResultSet rs = ontology.query(String.format(query_text, qudt_url));
        if(false == rs.hasNext())
            self_url = null;
        else
            self_url = rs.next().get("key").toString();

    }

    private RDFNode query_attr(String attribute){
        String query_template = "PREFIX qudt: <http://qudt.org/schema/qudt#>\n" +
                "        SELECT\n" +
                "        ?key\n" +
                "        WHERE\n" +
                "        {\n" +
                "        <%s> qudt:%s ?key.\n" +
                "        }\n";
        //System.out.print(String.format(query_template, self_url, attribute));
        ResultSet rs = ontology.query(String.format(query_template, self_url, attribute));
        if(false == rs.hasNext())
            return null;
        return rs.next().get("key");
    }

    @Override
    public ModelicaUnit create_ins(){
        if(null == self_url)
            self_url = "null";

        ModelicaUnit result = new ModelicaUnit();
        result.setUrl(self_url);

        result.setClassPath("");
        //Object tmp;
        return result;
    }

}
