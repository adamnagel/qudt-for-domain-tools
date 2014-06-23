package qudt4dt.factory;


import qudt4dt.thrift.Unit;

/**
 * Created by yli on 5/8/14.
 */
public class UnitFactory{
    private String qudt_url;
    private String self_url;
    public UnitFactory(String _url){
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
        result.setQudt_url(qudt_url);
        QudtAttrFactory q = new QudtAttrFactory(qudt_url);
        result.setQudt_attr(q.create_ins());

        return result;
    }
}
