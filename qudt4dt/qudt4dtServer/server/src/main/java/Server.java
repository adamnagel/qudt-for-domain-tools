/**
 * Created by yli on 5/8/14.
 */
package qudt4dt;

import org.apache.thrift.TProcessor;
import org.apache.thrift.server.*;
import org.apache.thrift.transport.TServerSocket;
import org.apache.thrift.transport.TServerTransport;
import org.apache.thrift.protocol.TJSONProtocol;

import qudt4dt.thrift.Qudt4dt_base;


import qudt4dt.ServerHandler;
import qudt4dt.factory.UnitFactory;
import qudt4dt.thrift.InvalidOperation;
import qudt4dt.thrift.Quantity;
import qudt4dt.thrift.Unit;

import java.util.HashMap;
import java.util.Map;

public class Server {

    public static ServerHandler handler;
    public static TProcessor processor;
    public static void main(String[] args){
      //  try{
            handler = new ServerHandler("http://localhost:3030/qudt4dt/query?");
            processor = new Qudt4dt_base.Processor<ServerHandler>(handler);
            //System.out.print(handler.query("http://qudt.org/vocab/unit#DegreeCelsius").qudt_u);
            performance();
            //simple(processor);
//            Runnable t1 = new Runnable(){
//                public void run(){
//                    simple(processor);
//                }
//            };
//            new Thread(t1).start();
       // } catch (org.apache.thrift.transport.TTransportException x) {
         //   x.printStackTrace();
       // }
    }

    public static void performance(){
        ServerHandler handler = new ServerHandler("http://localhost:3030/qudt4dt/query?");
        UnitFactory qudtFactory = new UnitFactory("http://qudt.org/vocab/unit#Millimeter");
        Quantity one_meter = new Quantity(qudtFactory.create_ins(), 1000d);

        try{
            for(int i = 0; i < 20; ++i){
                long start_list = System.currentTimeMillis();
                Map<String, Quantity> result = handler.list_domain_unitset(one_meter);
                long end_list = System.currentTimeMillis();
                long start_convert = System.currentTimeMillis();
                Quantity converted_q = handler.quantity_convert(one_meter,
                        "http://qudt.org/vocab/unit#Meter");
                long end_convert = System.currentTimeMillis();
                System.out.print("list:" + (end_list - start_list) +"ms," +
                    "convert:" + (end_convert - start_convert) + "ms," +
                    "node:" + (end_list + end_convert - start_list - start_convert) + "ms\n");
            }
        }catch (Exception err){
            err.printStackTrace();
        }
    }

    public static void simple(TProcessor processor) {
        try {
            TServerTransport serverTransport = new TServerSocket(9090);
            
            TServer server = new TSimpleServer(new TServer.Args(serverTransport).processor(processor).protocolFactory(new TJSONProtocol.Factory()));


            // Use this for a multithreaded server
            //TServer server = new TThreadPoolServer(new TThreadPoolServer.Args(serverTransport).processor(processor));

            System.out.println("Starting the simple server...");
            server.serve();
        } catch (org.apache.thrift.transport.TTransportException e) {
            e.printStackTrace();
        }
    }
}
