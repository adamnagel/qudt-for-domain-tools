using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using qudt4dt;
using qudt4dt.modelica;
using qudt4dt.owl;


namespace qudt4dt_example
{
    class Program
    {
        static void Main(string[] args)
        {
            Uri uri_endpoint = new Uri(@"http://192.168.1.12:3030/");

            var inch = new qudt4dt.qudt.Unit(new Uri(@"http://qudt.org/vocab/unit#Inch"),uri_endpoint);
            var millimeter = new qudt4dt.qudt.Unit(new Uri(@"http://qudt.org/vocab/unit#Millimeter"), uri_endpoint);
            var meter = new qudt4dt.qudt.Unit(new Uri(@"http://qudt.org/vocab/unit#Meter"), uri_endpoint);
            var mile = new qudt4dt.qudt.Unit(new Uri(@"http://qudt.org/vocab/unit#MileUSStatute"), uri_endpoint);

            double val_inch = 1;
            Console.Out.WriteLine("{0} {1}", val_inch, inch.symbol);

            double val_mile = Converter.ConvertValue(inch,mile,val_inch);
            Console.Out.WriteLine("{0} {1}", val_mile, mile.symbol);
            
            double val_mm = millimeter.ConvertValueFrom(inch, val_inch);
            Console.Out.WriteLine("{0} {1}", val_mm, millimeter.symbol);
            
            double val_m = inch.ConvertValueTo(meter, val_inch);
            Console.Out.WriteLine("{0} {1}", val_m, meter.symbol);

            ModelicaUnitClass m_ModelicaEquiv = meter.GetEquivalents()
                                                     .Where(t => t.GetType() == typeof(ModelicaUnitClass))
                                                     .Cast<ModelicaUnitClass>()
                                                     .FirstOrDefault();
            if (m_ModelicaEquiv != null)
            {
                Console.Out.WriteLine("== Modelica Equivalent Class ==");
                foreach (var field in m_ModelicaEquiv.GetType().GetFields())
                {
                    String msg = String.Format("  {0}: {1}", field.Name, field.GetValue(m_ModelicaEquiv));
                    Console.Out.WriteLine(msg);
                }
            }
           
        }
    }
}
