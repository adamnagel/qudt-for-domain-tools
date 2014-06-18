package qudt4dt;

import qudt4dt.factory.FactoryUtils;
import qudt4dt.factory.UnitFactory;
import qudt4dt.thrift.InvalidOperation;
import qudt4dt.thrift.Quantity;
import qudt4dt.thrift.Qudt4dt_base;
import qudt4dt.thrift.Unit;

import java.lang.reflect.Method;
import java.util.HashMap;
import java.util.Map;

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

        for(String _d : FactoryUtils.domain){
            Class<FactoryUtils> _c = FactoryUtils.class;
            Method get_domain_unit;
            Unit _u;

            try{
                get_domain_unit = _c.getDeclaredMethod("getunit_" + _d, new Class[] {Unit.class});
                Object _r = get_domain_unit.invoke(null, input.unit);
                if(null == _r){
                    Unit SI = FactoryUtils.get_SI_unit(input.unit);

                    if(null == SI)
                        throw new InvalidOperation("fail to get SI unit");

                    _r = get_domain_unit.invoke(null, SI);
                }
                _u = (Unit) _r;

            }catch (Exception e){
                throw new InvalidOperation("Invalid domain name");
            }

            Quantity _tmp = quantity_convert(new Quantity(input), _u.qudt_url);
            result.put(_d,
                    new Quantity(_u, _tmp.value));

        }
        return result;
    }


}
