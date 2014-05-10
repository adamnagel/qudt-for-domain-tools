package qudt4dt.factory;


import qudt4dt.Sparql;
import qudt4dt.thrift.QudtUnit;
import qudt4dt.thrift.Unit;

/**
 * Created by yli on 5/8/14.
 */
public class UnitFactory extends Factory{
    private String qudt_url;
    public UnitFactory(String _url){
        super(_url);
        init();
    }
    public UnitFactory(String _url, String _ontology_service){
        super(_url, _ontology_service);
        init();
    }
    public void init(){
        qudt_url = url;
        //TODO:: acception for non qudt unit
    }
    public Unit create_ins(){
        Unit result = new Unit();
        QudtUnitFactory q = new QudtUnitFactory(qudt_url);
        result.url = url;
        result.qudt_u = q.create_ins();
        return result;
    }
}
