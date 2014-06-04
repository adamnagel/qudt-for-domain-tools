import org.junit.BeforeClass;
import org.junit.Test;
import org.junit.Assert;
import qudt4dt.ServerHandler;
import qudt4dt.Sparql;
import qudt4dt.factory.FactoryUtils;
import qudt4dt.factory.UnitFactory;
import qudt4dt.thrift.Quantity;
import qudt4dt.thrift.Qudt4dt_base;
import qudt4dt.thrift.Unit;

/**
 * Created by yli on 6/3/14.
 */

public class TestFactoryUlits {
    @BeforeClass
    public static void ontologyInit(){
        FactoryUtils.ontology_server_address =
                "http://localhost:3030/qudt4dt/query?";
        FactoryUtils.ontology = new Sparql(FactoryUtils.ontology_server_address);
    }

    @Test
    public void qudt_to_modelica(){
        UnitFactory qudtFactory = new UnitFactory("http://qudt.org/vocab/unit#Meter");
        Unit qudt_meter = qudtFactory.create_ins();
        Unit modelica_meter = FactoryUtils.getunit_modelica(qudt_meter);
        Assert.assertEquals("http://modelica.org/msl/SIUnits/individuals#Length", modelica_meter.getUrl());
        Assert.assertEquals("http://qudt.org/vocab/unit#Meter", modelica_meter.getQudt_url());
    }

    @Test
    public void qudt_to_mdao(){
        UnitFactory qudtFactory = new UnitFactory("http://qudt.org/vocab/unit#Meter");
        Unit qudt_meter = qudtFactory.create_ins();
        Unit mdao_meter = FactoryUtils.getunit_mdao(qudt_meter);
        Assert.assertEquals("http://openmdao.org/units/individuals#m", mdao_meter.getUrl());
        Assert.assertEquals("http://qudt.org/vocab/unit#Meter", mdao_meter.getQudt_url());
    }

    @Test
    public void find_qudt_SI(){
        UnitFactory qudtFactory = new UnitFactory("http://qudt.org/vocab/unit#Millimeter");
        Unit qudt_millimeter = qudtFactory.create_ins();
        Unit qudt_length_si = FactoryUtils.get_SI_unit(qudt_millimeter);
        Assert.assertEquals("http://qudt.org/vocab/unit#Meter", qudt_length_si.getUrl());
    }


}
