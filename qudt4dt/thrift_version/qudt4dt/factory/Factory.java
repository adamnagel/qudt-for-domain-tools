package qudt4dt.factory;

import qudt4dt.Sparql;

/**
 * Created by yli on 5/8/14.
 */
public abstract class Factory {
    protected String self_url;
    protected String ontology_server_address;
    protected Sparql ontology;


    public Factory(String _ontology_server_address){
        ontology_server_address = _ontology_server_address;
        ontology = new Sparql(ontology_server_address);
    }

    public abstract Object create_ins();
}
