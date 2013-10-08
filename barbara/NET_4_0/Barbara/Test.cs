using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net;

using Xunit;
using System.IO;

namespace qudt4dt
{
    public class Test
    {
        [Fact]
        public void FirstTest()
        {
            Uri uri_endpoint = new Uri(@"http://10.67.211.162:3030/");
            Uri uri_length = new Uri(@"http://modelica.org/msl/SIUnits/individuals#Length");
            ModelicaUnit len = new ModelicaUnit(uri_length,uri_endpoint);

            Uri uri_FermiTemperature = new Uri(@"http://modelica.org/msl/SIUnits/individuals#FermiTemperature");
            ModelicaUnit ft = new ModelicaUnit(uri_FermiTemperature, uri_endpoint);
        }
    }
}
