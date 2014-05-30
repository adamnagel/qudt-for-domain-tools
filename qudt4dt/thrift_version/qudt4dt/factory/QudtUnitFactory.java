package qudt4dt.factory;

import com.hp.hpl.jena.query.ResultSet;
import com.hp.hpl.jena.rdf.model.RDFNode;
import qudt4dt.thrift.QudtUnit;

/**
 * Created by yli on 5/8/14.
 */
public class QudtUnitFactory extends Factory {

    public QudtUnitFactory(String _url, String _ontology_server_address){
        super(_ontology_server_address);
        self_url = _url;
        init();
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

    public Double getFactor(){
        RDFNode rs = query_attr("conversionMultiplier");
        if(null == rs)
            return null;
        return rs.asLiteral().getDouble();
    }

    public Double getOffset(){
        RDFNode rs = query_attr("conversionOffset");
        if(null == rs)
            return null;
        return rs.asLiteral().getDouble();

    }

    public String getUnitClass(){
        String query_template = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n" +
                "        PREFIX owl: <http://www.w3.org/2002/07/owl#>\n" +
                "        SELECT\n" +
                "        ?key\n" +
                "        WHERE\n" +
                "        {\n" +
                "        <%s> rdf:type ?key. \n" +
                "        FILTER NOT EXISTS{?key rdf:type owl:DeprecatedClass}\n" +
                "        }\n";
        //System.out.print(String.format(query_template, self_url));
        ResultSet rs = ontology.query(String.format(query_template, self_url));
        if(false == rs.hasNext())
            return null;
        return rs.next().get("key").toString();
    }


    private void init(){
        ;//TODO:: checking the invalid self_url
    }

    //TODO:: symbol, abbreviation

    @Override
    public QudtUnit create_ins(){
        QudtUnit result = new QudtUnit();
        result.setUrl(self_url);
        Object tmp;
        tmp = getOffset();
        if(null != tmp)
            result.setOffset((Double)tmp);

        tmp = getFactor();
        if(null != tmp)
            result.setFactor((Double)tmp);

        tmp = getUnitClass();
        if(null != tmp)
            result.setUnitClass((String)tmp);
        return result;
    }
}
