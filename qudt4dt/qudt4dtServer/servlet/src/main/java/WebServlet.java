package qudt4dt;
import org.apache.thrift.server.TServlet;
import org.apache.thrift.protocol.TJSONProtocol;

import qudt4dt.thrift.Qudt4dt_base;

public class WebServlet extends TServlet{
	public WebServlet(){
		super(new Qudt4dt_base.Processor<ServerHandler>(
				new ServerHandler("http://localhost:3030/qudt4dt/query?")
				),
				new TJSONProtocol.Factory());
		addCustomHeader("Access-Control-Allow-Origin", "*");
		//addCustomHeader("Access-Control-Allow-Methods", "POST,GET,OPTIONS,PUT,DELETE,HEAD");
		//addCustomHeader("Access-Control-Allow-Headers", "X-PINGOTHER,Origin,X-Requdsted-With,Content-Type,Accept");
		//addCustomHeader("Access-Control-Max-Age","1728000");
	}
}
