package qudt4dt.factory;


import qudt4dt.thrift.Unit;

/**
 * Created by yli on 5/8/14.
 */
public class UnitFactory extends Factory{
    private String qudt_url;

    public UnitFactory(String _url, String _ontology_server_address){
        super(_ontology_server_address);
        self_url = _url;
        init();
    }
    public void init(){
        qudt_url = self_url;
        //TODO:: acception for non qudt unit
    }
    public Unit create_ins(){
        Unit result = new Unit();

        result.setUrl(self_url);

        QudtUnitFactory q = new QudtUnitFactory(qudt_url, ontology_server_address);
        result.setQudt_u(q.create_ins());

        ModelicaUnitFactory m = new ModelicaUnitFactory(qudt_url, ontology_server_address);
        result.setModelica_u(m.create_ins());

        MdaoUnitFactory md = new MdaoUnitFactory(qudt_url, ontology_server_address);
        result.setMdao_u(md.create_ins());

        return result;
    }
}
