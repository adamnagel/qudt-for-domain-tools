/**
 * Created by yli on 5/8/14.
 */
package qudt4dt;

import org.apache.thrift.server.TServer;
import org.apache.thrift.server.TThreadPoolServer;
import org.apache.thrift.transport.TServerSocket;
import org.apache.thrift.transport.TServerTransport;

import qudt4dt.thrift.Qudt4dt_base;

public class Server {

    public static ServerHandler handler;
    public static Qudt4dt_base.Processor processor;
    public static void main(String[] args){
        try{
            handler = new ServerHandler("http://localhost:3030/qudt4dt/query?");
            processor = new Qudt4dt_base.Processor(handler);
            //System.out.print(handler.query("http://qudt.org/vocab/unit#DegreeCelsius").qudt_u);
            Runnable t1 = new Runnable(){
                public void run(){
                    simple(processor);
                }
            };
            new Thread(t1).start();
        } catch (Exception x) {
            x.printStackTrace();
        }
    }

    public static void simple(Qudt4dt_base.Processor processor) {
        try {
            TServerTransport serverTransport = new TServerSocket(9090);
            //TServer server = new TSimpleServer(new TServer.Args(serverTransport).processor(processor));


            // Use this for a multithreaded server
            TServer server = new TThreadPoolServer(new TThreadPoolServer.Args(serverTransport).processor(processor));

            System.out.println("Starting the simple server...");
            server.serve();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
