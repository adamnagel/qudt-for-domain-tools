package qudt4dt;

/**
 * Created by yli on 5/9/14.
 */
import org.apache.thrift.TException;
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TProtocol;

import qudt4dt.thrift.Qudt4dt_base;
import qudt4dt.thrift.Unit;

public class client {
    public static void main(String [] args) {


        try {
            TTransport transport;

            transport = new TSocket("localhost", 9090);
            transport.open();



            TProtocol protocol = new  TBinaryProtocol(transport);
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
        Unit rs = client.query("http://qudt.org/vocab/unit#Meter");
        System.out.println(rs.toString());
    }
}
