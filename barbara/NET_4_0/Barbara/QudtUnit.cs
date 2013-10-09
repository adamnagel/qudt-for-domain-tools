using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace qudt4dt.qudt
{
    [ClassUri(@"http://qudt.org/schema/qudt#Unit")]
    public partial class Unit : qudt4dt.Unit
    {
        public Unit(Uri identity,Uri endpoint) : base(identity,endpoint)
        {

        }

        public String abbreviation;
        public Double conversionMultiplier;
        public Double conversionOffset;
        public String description;
        public String symbol;
        public String uneceCommonCode;
    }
}
