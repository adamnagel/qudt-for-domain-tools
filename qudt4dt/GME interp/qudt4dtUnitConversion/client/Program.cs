using System;
using Thrift;
using Thrift.Protocol;
using Thrift.Server;
using Thrift.Transport;
using qudt4dt.thrift;

using System.Collections.Generic;
namespace qudt4dt
{
    namespace CSClient
    {
        public class Client
        {
            private Qudt4dt_base.Client _client;
            private const String defaultAddress = "localhost";
            private TTransport _transport;

            public Client(String address)
            {
                try
                {
                    init(address);
                }
                catch (TApplicationException x)
                {
                    Console.WriteLine(x.StackTrace);
                }
            }

            ~Client()
            {
                _transport.Close();
            }

            public Client() : this(defaultAddress) { }

            private void init(String address)
            {
                _transport = new TSocket(address, 9090);
                _transport.Open();

                TProtocol protocol = new TBinaryProtocol(_transport);
                _client = new Qudt4dt_base.Client(protocol);
            }

            public qudt4dt.thrift.Unit query(string url)
            {
                return _client.query(url);
            }

            public qudt4dt.thrift.Quantity quantity_convert(qudt4dt.thrift.Quantity src, string dst_url)
            {
                return _client.quantity_convert(src, dst_url);
            }

            public Dictionary<String, Quantity> list_domain_unitset(Quantity input)
            {
                return _client.list_domain_unitset(input);
            }

            //client sample
            public static void Main()
            {
                try
                {
                    TTransport transport = new TSocket("10.67.68.239", 9090);
                    transport.Open();


                    TProtocol protocol = new TBinaryProtocol(transport);
                    Qudt4dt_base.Client client = new Qudt4dt_base.Client(protocol);


                    perform(client);
                    Console.ReadLine();
                    transport.Close();
                }
                catch (TApplicationException x)
                {
                    Console.WriteLine(x.StackTrace);
                }
            }


            private static void perform(Qudt4dt_base.Client client)
            {

                Console.WriteLine("quering ...");
                Unit rs = client.query("http://qudt.org/vocab/unit#DegreeCelsius");
                Console.WriteLine(rs.ToString());
            }
        }
    }
}
