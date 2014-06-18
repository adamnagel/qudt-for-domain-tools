package qudt4dt;
import org.apache.thrift.TException;
import org.apache.thrift.protocol.TJSONProtocol;
import org.apache.thrift.protocol.TProtocol;
import org.apache.thrift.transport.THttpClient;

import qudt4dt.thrift.Qudt4dt_base;
import qudt4dt.thrift.Unit;
import qudt4dt.thrift.Quantity;
public class ServletTest {

	public static void main(String[] args) {
		String serveltUrl = "http://127.0.0.1:8081/test/MyTest";
		try {
			THttpClient thc = new THttpClient(serveltUrl);
			TProtocol lopFactory = new TJSONProtocol(thc);
			Qudt4dt_base.Client client = new Qudt4dt_base.Client(lopFactory);
			System.out.println("quering ...\n");
	        Unit rs = client.query("http://qudt.org/vocab/unit#Millimeter");
	        Quantity src = new Quantity(rs, 1000d);
	        Quantity dst = client.quantity_convert(src, "http://qudt.org/vocab/unit#Meter");
	        System.out.println(dst);
		} catch (TException ex) {
			ex.printStackTrace();
		}

	}

}
