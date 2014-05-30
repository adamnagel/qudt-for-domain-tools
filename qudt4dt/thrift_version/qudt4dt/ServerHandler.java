package qudt4dt;

import qudt4dt.factory.UnitFactory;
import qudt4dt.thrift.Qudt4dt;
import qudt4dt.thrift.Unit;

/**
 * Created by yli on 5/8/14.
 */
public class ServerHandler implements Qudt4dt.Iface{

    private String ontology_server_address;

    public ServerHandler(String _ontology_server_address){
        ontology_server_address = _ontology_server_address;
    }

    @Override
    public Unit query(String url){
        UnitFactory rs = new UnitFactory(url, ontology_server_address);
        return rs.create_ins();
    }


}
