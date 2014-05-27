using System;
using Thrift;
using Thrift.Protocol;
using Thrift.Server;
using Thrift.Transport;
using qudt4dt.thrift;
namespace qudt4dt
{
    namespace CSClient
    {
        public class Client
        {
            private Qudt4dt.Client _client;
            private const String defaultAddress = "localhost";

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

            public Client() : this(defaultAddress) { }

            private void init(String address)
            {
                TTransport transport = new TSocket(address, 9090);
                transport.Open();

                TProtocol protocol = new TBinaryProtocol(transport);
                _client = new Qudt4dt.Client(protocol);
            }


            //client sample
            public static void Main()
            {
                try
                {
                    TTransport transport = new TSocket("10.67.29.212", 9090);
                    transport.Open();


                    TProtocol protocol = new TBinaryProtocol(transport);
                    Qudt4dt.Client client = new Qudt4dt.Client(protocol);


                    perform(client);
                    Console.ReadLine();
                    transport.Close();
                }
                catch (TApplicationException x)
                {
                    Console.WriteLine(x.StackTrace);
                }
            }


            private static void perform(Qudt4dt.Client client)
            {

                Console.WriteLine("quering ...");
                Unit rs = client.query("http://qudt.org/vocab/unit#DegreeCelsius");
                QudtUnit rs1 = rs.Qudt_u;
                Console.WriteLine(rs1.ToString());
            }
        }
    }
}
