using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace qudt4dt
{
    [ClassUri(@"http://qudt.org/schema/qudt#DomainToolUnit")]
    public abstract class DomainToolUnit : Unit
    {
        public DomainToolUnit(Uri identity,Uri endpoint) : base(identity,endpoint)
        {
        }
    }
}
