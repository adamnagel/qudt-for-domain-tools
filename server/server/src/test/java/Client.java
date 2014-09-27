package qudt4dt;

/**
 * Created by yli on 5/9/14.
 */
import org.apache.thrift.TException;
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.protocol.TJSONProtocol;
import org.apache.thrift.protocol.TProtocol;

import qudt4dt.thrift.Quantity;
import qudt4dt.thrift.Qudt4dt_base;
import qudt4dt.thrift.Unit;

public class Client {
    public static void main(String [] args) {


        try {
            TTransport transport;

            transport = new TSocket("localhost", 9090);
            transport.open();



            TProtocol protocol = new  TJSONProtocol(transport);
            Qudt4dt_base.Client client = new Qudt4dt_base.Client(protocol);

            perform(client);

            transport.close();
        } catch (TException x) {
            x.printStackTrace();
        }
    }

    private static void perform(Qudt4dt_base.Client client) throws TException
    {

        System.out.println("quering ...\n");
        Unit rs = client.query("http://qudt.org/vocab/unit#Millimeter");
        Quantity src = new Quantity(rs, 1000d);
        Quantity dst = client.quantity_convert(src, "http://qudt.org/vocab/unit#Meter");
        System.out.println(dst);
    }
}
