package qudt4dt;
import com.hp.hpl.jena.query.ResultSet;
import com.hp.hpl.jena.rdf.model.Literal;

/**
 * Created by yli on 5/9/14.
 */
public class test {
    public static void main(String[] args){
        Sparql q = new Sparql();
        String query =
                "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n" +
                        "                    SELECT\n" +
                        "                    ?class\n" +
                        "                    WHERE\n" +
                        "                    { <http://qudt.org/schema/qudt#Unit> ^rdfs:subClassOf+ ?class\n" +
                        "                    }\n";

        String query2 = "PREFIX qudt: <http://qudt.org/schema/qudt#>\n" +
                "        SELECT\n" +
                "        ?key\n" +
                "        WHERE\n" +
                "        {\n" +
                "        <http://qudt.org/schema/qudt#ResourceUnit> qudt:conversionMultiplier ?key.\n" +
                "       }\n";
        String query3 = "PREFIX qudt: <http://qudt.org/schema/qudt#>\n" +
                "        SELECT\n" +
                "        ?key\n" +
                "        WHERE\n" +
                "        {\n" +
                "        <http://qudt.org/vocab/unit#DegreeCelsius> qudt:conversionMultiplier ?key.\n" +
                "        }";
        ResultSet rs = q.query(query3);

        //if(null == rs.next())
            System.out.print(rs.next().get("key").asLiteral().getDouble());
    }
}
