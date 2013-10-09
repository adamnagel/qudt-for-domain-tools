using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace qudt4dt
{
    [AttributeUsage(AttributeTargets.Class, Inherited = false)]
    class ClassUri : System.Attribute
    {
        public String uri;
        public ClassUri(String classUri)
        {
            uri = classUri;
        }
    }
}
