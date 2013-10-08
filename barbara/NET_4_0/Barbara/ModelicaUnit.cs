using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace qudt4dt
{
    public class ModelicaUnit : DomainToolUnit
    {
        public ModelicaUnit(Uri identity,Uri endpoint) : base(identity,endpoint)
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
