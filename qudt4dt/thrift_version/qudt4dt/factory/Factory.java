package qudt4dt.factory;

import qudt4dt.Sparql;

/**
 * Created by yli on 5/8/14.
 */
public abstract class Factory {
    protected String url;
    protected String ontology_service;
    protected Sparql ontology;
    public Factory(String _url, String _ontology_service){
        url = _url;
        ontology_service = _ontology_service;
        ontology = new Sparql(ontology_service);
    }

    public Factory(String _url){ //local sparql service
        url = _url;
        ontology_service = null;
        ontology = new Sparql();
    }
    public abstract Object create_ins();
}
