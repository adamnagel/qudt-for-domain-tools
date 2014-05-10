package qudt4dt;

import qudt4dt.factory.UnitFactory;
import qudt4dt.thrift.Qudt4dt;
import qudt4dt.thrift.Unit;

/**
 * Created by yli on 5/8/14.
 */
public class ServerHandler implements Qudt4dt.Iface{

    private String ontology_service;

    public ServerHandler(){
        ontology_service = null;
    }

    public ServerHandler(String _ontology_service){
        ontology_service = _ontology_service;
    }

    public Unit query(String url){
        UnitFactory rs;
        if(null == ontology_service)
            rs = new UnitFactory(url);
        else
            rs = new UnitFactory(url, ontology_service);

        return rs.create_ins();
    }


}
