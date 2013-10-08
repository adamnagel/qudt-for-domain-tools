using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using qudt4dt;
using qudt;


namespace qudt4dt_example
{
    class Program
    {
        static void Main(string[] args)
        {
            Uri uri_endpoint = new Uri(@"http://10.67.211.162:3030/");
            Uri uri_length = new Uri(@"http://modelica.org/msl/SIUnits/individuals#Length");
            ModelicaUnit len = new ModelicaUnit(uri_length, uri_endpoint);

            Uri uri_FermiTemperature = new Uri(@"http://modelica.org/msl/SIUnits/individuals#FermiTemperature");
            ModelicaUnit ft = new ModelicaUnit(uri_FermiTemperature, uri_endpoint);

            foreach (var field in ft.GetType().GetFields())
            {
                String msg = String.Format("{0}: {1}",field.Name,field.GetValue(ft));
                Console.Out.WriteLine(msg);
            }
        }
    }
}
