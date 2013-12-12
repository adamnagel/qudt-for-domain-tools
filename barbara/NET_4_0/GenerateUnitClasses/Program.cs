using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Newtonsoft.Json.Linq;

namespace GenerateUnitClasses
{
    class Program
    {
        static void Main(string[] args)
        {
            // Assume the database is running
            // Access the database and query all classes inheriting from (and including) Qudt4dtUnit
            // For each of these, build a partial class
            // For each of these, add a statement to Barbara allowing "getting" of an instance of that class

            var result = qudt4dt.Query.RunQuery(query_GetAllClasses, new Uri("http://localhost:3030"));
            JObject o = JObject.Parse(result);
            JToken results = o["results"];
            JToken bindings = results["bindings"];

            List<UnitClass> classes = new List<UnitClass>();
            foreach (var b in bindings)
            {
                var classURI = b["class"]["value"].ToString();

                classes.Add(new UnitClass() { 
                    ClassURI = classURI, 
                    ClassName = classURI.Split('#')[1],
                    Namespace = classURI.Split('/')[2]
                });
            }

            foreach (var c in classes)
            {
                // Get more data and populate
            }

            var uc = new UnitClass();
            uc.ClassName = "SomeClass";
            uc.ClassURI = "SomeURI";
            uc.BaseClass = "SomeBaseClass";
            uc.Namespace = "SomeNamespace";
            uc.Properties = new List<string>() { "Prop1", "Prop2" };

            Console.Out.WriteLine(uc.GenerateCode());
        }

        private static String query_GetAllClasses = @"PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT
?class
WHERE
{ 
  <http://qudt4dt.org/ontology#Unit> ^rdfs:subClassOf+ ?class
}";
    }
}
