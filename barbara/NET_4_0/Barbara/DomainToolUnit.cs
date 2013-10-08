using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace qudt4dt
{
    public abstract class DomainToolUnit : qudt4dt.Unit
    {
        public DomainToolUnit(Uri identity,Uri endpoint) : base(identity,endpoint)
        {
        }
    }
}
