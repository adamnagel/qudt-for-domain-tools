using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net;
using System.IO;

namespace qudt4dt
{
    public class Unit : owl.Thing
    {
        public Unit(Uri identity,Uri endpoint) : base(identity,endpoint)
        {
        }
    }
}
