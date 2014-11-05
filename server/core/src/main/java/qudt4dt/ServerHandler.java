package qudt4dt;

import com.hp.hpl.jena.query.QuerySolution;
import com.hp.hpl.jena.query.ResultSet;
import qudt4dt.factory.FactoryUtils;
import qudt4dt.factory.UnitFactory;
import qudt4dt.thrift.InvalidOperation;
import qudt4dt.thrift.Quantity;
import qudt4dt.thrift.Qudt4dt_base;
import qudt4dt.thrift.Unit;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.reflect.Method;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Created by yli on 5/8/14.
 */
public class ServerHandler implements Qudt4dt_base.Iface{

    public ServerHandler(String _ontology_server_address){
        FactoryUtils.ontology_server_address = _ontology_server_address;
        FactoryUtils.ontology = new Sparql(_ontology_server_address);
    }

    @Override
    public Unit query(String url) throws InvalidOperation{
        UnitFactory rs = new UnitFactory(url);
        return rs.create_ins();
    }

    @Override
    public Quantity quantity_convert(Quantity src, String dst_url) throws InvalidOperation{
        UnitFactory dst_factory = new UnitFactory(dst_url);
        Unit dst_unit = dst_factory.create_ins();
        if(!src.unit.qudt_attr.unitClass.equals(dst_unit.qudt_attr.unitClass)){
            InvalidOperation err = new InvalidOperation("attempting to convert to a incompatible unit");
            throw err;
        }

        double dst_value = ((src.unit.qudt_attr.offset - dst_unit.qudt_attr.offset) + src.value) *
                src.unit.qudt_attr.factor / dst_unit.qudt_attr.factor;

        return new Quantity(dst_unit,dst_value);
    }

    @Override
    public Map<String, Quantity> list_domain_unitset(Quantity input) throws InvalidOperation{
        if(null == input.unit.qudt_url || "".equals(input.unit.qudt_url))
            throw new InvalidOperation("Invalid input unit (empty qudt_url field)");

        Map<String, Quantity> result = new HashMap<String, Quantity>();
        Unit _q = new Unit(input.unit.qudt_url, input.unit.qudt_url, input.unit.qudt_attr);
        result.put("qudt", new Quantity(_q, input.value));
        ResultSet domain_SI = FactoryUtils.get_SI_domain_unit(input.unit);

        if(false == domain_SI.hasNext())
            return null;

        QuerySolution q = domain_SI.next();
        Unit modelica = new Unit();
        modelica.setUrl(q.get("modelica").toString());
        modelica.setQudt_url(input.unit.getQudt_url());
        modelica.setQudt_attr(input.unit.getQudt_attr());

        Unit mdao     = new Unit();
        mdao.setUrl(q.get("mdao").toString());
        mdao.setQudt_url(input.unit.getQudt_url());
        mdao.setQudt_attr(input.unit.getQudt_attr());

        Quantity tmp = quantity_convert(input, modelica.qudt_url);
        result.put("modelica", new Quantity(modelica, tmp.value));
        tmp = quantity_convert(input, mdao.qudt_url);
        result.put("mdao", new Quantity(mdao, tmp.value));
        return result;
    }
    @Override
    public String unitExp(String exp, String dstUnit) throws InvalidOperation{
        ProcessBuilder pb = new ProcessBuilder("units", "\"" + exp + "\"", dstUnit);
        String result = "";
        try{
            Process p = pb.start();
            BufferedReader is = new BufferedReader(new InputStreamReader(p.getInputStream()));

            String line;
            while ((line = is.readLine()) != null)
                result += line;
        } catch (Exception x) {
            x.printStackTrace();
        }
        Pattern p = Pattern.compile("[\\d\\.]+");
        Matcher m = p.matcher(result);
        m.find();
        return m.group();

    }


}
