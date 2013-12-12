using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace GenerateUnitClasses
{
    public class UnitClass
    {
        public String Namespace;
        public String ClassName;
        public String ClassURI;
        public String BaseClass;
        public List<String> Properties;

        public String GenerateCode()
        {
            String properties = "";
            foreach (var field in Properties)
            {
                properties += Environment.NewLine;
                properties += String.Format(propertyFormat, field);
            }

            return String.Format(codeFormat, Namespace, ClassURI, ClassName, BaseClass, properties);
        }

        #region Templates
        private String codeFormat = @"using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using qudt4dt;

namespace {0}
{{
    [ClassUri(@""{1}"")]
    public class {2} : {3}
    {{
        public {2}(Uri identity, Uri endpoint) : base(identity, endpoint)
        {{
        }}

        {4}
    }}
}}";
        private String propertyFormat = @"        public String {0};";
        #endregion
    }
}
