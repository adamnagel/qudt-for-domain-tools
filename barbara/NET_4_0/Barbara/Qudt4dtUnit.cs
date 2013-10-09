using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net;
using System.IO;

namespace qudt4dt
{
    [ClassUri(@"http://qudt4dt.org/ontology#Unit")]
    public partial class Unit : owl.Thing
    {
        public Unit(Uri identity,Uri endpoint) : base(identity,endpoint)
        {
        }
    }
}
