package qudt4dt.factory;

import com.hp.hpl.jena.query.QuerySolution;
import com.hp.hpl.jena.query.ResultSet;
import com.hp.hpl.jena.rdf.model.RDFNode;
import qudt4dt.thrift.QudtAttr;

/**
 * Created by yli on 5/8/14.
 */
public class QudtAttrFactory{
    private String self_url;
    public QudtAttrFactory(String _url){
        self_url = _url;
        init();
    }

    @Deprecated
    private RDFNode query_attr(String attribute){
        String query_template = "PREFIX qudt: <http://qudt.org/schema/qudt#>\n" +
                "        SELECT\n" +
                "        ?key\n" +
                "        WHERE\n" +
                "        {\n" +
                "        <%s> qudt:%s ?key.\n" +
                "        }\n";
        //System.out.print(String.format(query_template, self_url, attribute));
        ResultSet rs = FactoryUtils.ontology.query(String.format(query_template, self_url, attribute));
        if(false == rs.hasNext())
            return null;
        return rs.next().get("key");
    }

    @Deprecated
    public Double getFactor(){
        RDFNode rs = query_attr("conversionMultiplier");
        if(null == rs)
            return null;
        return rs.asLiteral().getDouble();
    }

    @Deprecated
    public Double getOffset(){
        RDFNode rs = query_attr("conversionOffset");
        if(null == rs)
            return null;
        return rs.asLiteral().getDouble();

    }

    @Deprecated
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
        ResultSet rs = FactoryUtils.ontology.query(String.format(query_template, self_url));
        if(false == rs.hasNext())
            return null;
        return rs.next().get("key").toString();
    }


    private void init(){
        ;//TODO:: checking the invalid self_url
    }

    //TODO:: symbol, abbreviation

    public ResultSet getAll(){
        String query_template = "PREFIX qudt: <http://qudt.org/schema/qudt#>\n" +
                "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n" +
                "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n" +
                "SELECT\n" +
                "?factor ?offset ?class\n" +
                "WHERE\n" +
                "{\n" +
                "BIND (<%s> AS ?unit).\n" +
                "?unit qudt:conversionMultiplier ?factor.\n" +
                "?unit qudt:conversionOffset     ?offset.\n" +
                "?unit rdf:type ?class. \n" +
                "FILTER NOT EXISTS{?class rdf:type owl:DeprecatedClass}\n" +
                "}\n";
        ResultSet rs = FactoryUtils.ontology.query(String.format(query_template, self_url));
        return rs;
    }

    // public QudtAttr create_ins(){
    //     QudtAttr result = new QudtAttr();
    //     Object tmp;
    //     tmp = getOffset();
    //     if(null != tmp)
    //         result.setOffset((Double)tmp);

    //     tmp = getFactor();
    //     if(null != tmp)
    //         result.setFactor((Double)tmp);

    //     tmp = getUnitClass();
    //     if(null != tmp)
    //         result.setUnitClass((String)tmp);
    //     return result;
    // }

    public QudtAttr create_ins(){
        QudtAttr result = new QudtAttr();
        ResultSet r = getAll();
        if(false == r.hasNext())
            return null;
        QuerySolution s = r.next();
        result.setOffset(s.get("offset").asLiteral().getDouble());
        result.setFactor(s.get("factor").asLiteral().getDouble());
        result.setUnitClass(s.get("class").toString());
        return result;
    }
}
