using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

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

            var uc = new UnitClass();
            uc.ClassName = "SomeClass";
            uc.ClassURI = "SomeURI";
            uc.BaseClass = "SomeBaseClass";
            uc.Namespace = "SomeNamespace";
            uc.Properties = new List<string>() { "Prop1", "Prop2" };

            Console.Out.WriteLine(uc.GenerateCode());
        }
    }
}
