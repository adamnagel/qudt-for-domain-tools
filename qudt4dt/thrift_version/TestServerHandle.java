import org.junit.Assert;
import org.junit.BeforeClass;
import org.junit.Test;
import qudt4dt.ServerHandler;
import qudt4dt.factory.UnitFactory;
import qudt4dt.thrift.InvalidOperation;
import qudt4dt.thrift.Quantity;
import qudt4dt.thrift.Unit;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by yli on 6/3/14.
 */
public class TestServerHandle {
    static ServerHandler handler;
    @BeforeClass
    public static void serverHandleInit(){
        handler = new ServerHandler("http://localhost:3030/qudt4dt/query?");
    }

    @Test
    public void quantity_convert(){
        UnitFactory qudtFactory = new UnitFactory("http://qudt.org/vocab/unit#Millimeter");
        Unit qudt_millimeter = qudtFactory.create_ins();
        Quantity thousand_millimeter = new Quantity(qudt_millimeter, 1000d);

        try{
            Quantity converted_q = handler.quantity_convert(thousand_millimeter,
                    "http://qudt.org/vocab/unit#Meter");
            Assert.assertEquals(converted_q.value, 1d, 0.001);
            Assert.assertEquals(converted_q.unit.url,
                    "http://qudt.org/vocab/unit#Meter");
        }catch (InvalidOperation err){
            err.printStackTrace();
        }

    }

    @Test
    public void domain_unitset_millimeter(){
        UnitFactory qudtFactory = new UnitFactory("http://qudt.org/vocab/unit#Millimeter");
        Quantity one_meter = new Quantity(qudtFactory.create_ins(), 1000d);

        try{
            Map<String, Quantity> result = handler.list_domain_unitset(one_meter);
            Assert.assertEquals(1d, result.get("modelica").getValue(), 0.001);
            Assert.assertEquals(1d, result.get("mdao").getValue(), 0.001);
            Assert.assertEquals("http://openmdao.org/units/individuals#m",
                    result.get("mdao").getUnit().getUrl());
            Assert.assertEquals("http://modelica.org/msl/SIUnits/individuals#Length",
                    result.get("modelica").getUnit().getUrl());

        }catch (Exception err){
            err.printStackTrace();
        }
    }
}
