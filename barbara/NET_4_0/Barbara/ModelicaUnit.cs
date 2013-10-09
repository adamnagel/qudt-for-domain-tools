using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using qudt4dt;

namespace qudt4dt.modelica
{
    [ClassUri(@"http://modelica.org/msl/SIUnits/vocabulary#ModelicaUnitClass")]
    public class ModelicaUnitClass : DomainToolUnit
    {
        public ModelicaUnitClass(Uri identity,Uri endpoint) : base(identity,endpoint)
        {
        }

        public string ClassPath;
        public string UnitDataType;
        public string UnitDisplayUnit;
        public string UnitMin;
        public string UnitQuantity;
        public string UnitStart;
        public string UnitUnit;
    }
}
