using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Newtonsoft.Json.Linq;
using System.Reflection;

namespace qudt4dt
{
    public class Mapping
    {
        /// <summary>
        /// Recursively find all base classes of the given class
        /// </summary>
        /// <param name="clazz"></param>
        /// <param name="endpoint"></param>
        /// <returns></returns>
        private static List<String> RecursivelyGetBaseClasses(String clazz,Uri endpoint)
        {
            /* This query, in English:
             * Given the input class, get its base classes.
             * Filter out those base classes that are marked as owl:DeprecatedClass
             */ 
            String queryTemplate = @"PREFIX qudt4dt: <http://qudt4dt.org/ontology#>
                                     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                                     PREFIX owl: <http://www.w3.org/2002/07/owl#>
                                     SELECT ?class
                                     WHERE {{
                                       <{0}> rdfs:subClassOf ?class .
                                       FILTER NOT EXISTS{{?class a owl:DeprecatedClass}}
                                     }}";
            String query = String.Format(queryTemplate,clazz);
            String response = Query.RunQuery(query, endpoint);

            JObject o = JObject.Parse(response);
            JToken results = o["results"];
            JToken bindings = results["bindings"];

            List<String> rtn = new List<String>();
            
            /* For each base class found, add it to the return list.
             * Add all of its base classes too.
             */
            foreach (var binding in bindings)
            {
                var superClass = binding["class"]["value"].ToString();
                rtn.Add(superClass);
                rtn.AddRange(RecursivelyGetBaseClasses(superClass,endpoint));
            }
            return rtn;
        }

        /// <summary>
        /// Get C# classes that have "ClassUri" attribute matching the input
        /// </summary>
        /// <param name="assembly"></param>
        /// <param name="classUri"></param>
        /// <returns>Collection of conforming C# classes</returns>
        private static IEnumerable<Type> GetTypesWithMatchingClassUri(Assembly assembly, String classUri)
        {
            foreach (Type type in assembly.GetTypes())
            {
                if (type.GetCustomAttributes(typeof(ClassUri), true)
                        .Where(ca => ((ClassUri)ca).uri == classUri).Count() > 0)
                    yield return type;
            }
        }

        /// <summary>
        /// Get qudt4dt.Unit objects marked as equivalent to "unit".
        /// </summary>
        /// <param name="unit">URI of the initial unit</param>
        /// <param name="endpoint">SPARQL endpoint to search</param>
        /// <returns>A list of equivalent objects</returns>
        public static IEnumerable<Unit> GetEquivalents(Unit unit,Uri endpoint)
        {
            /* 
             * This query, in English:
             * For the given unit URI, find other individuals (?unit) that are related
             * via the qudt4dt:equivalentOf owl:ObjectProperty. Search this relation in
             * both directions, and take the UNION.
             * For each resulting ?unit, get the ?class of that unit.
             * Filter out ?class values that are marked as owl:DeprecatedClass.
             */
            String queryTemplate = @"PREFIX qudt4dt: <http://qudt4dt.org/ontology#>
                                     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                                     PREFIX owl: <http://www.w3.org/2002/07/owl#>
                                     SELECT ?unit ?class
                                     WHERE {{
                                       {{ {{<{0}> qudt4dt:equivalentOf ?unit}}
                                          UNION
                                          {{?unit qudt4dt:equivalentOf <{0}>}}
                                       }} .
                                       ?unit a ?class .
                                       FILTER NOT EXISTS{{?class a owl:DeprecatedClass}}
                                     }}";
            String query = String.Format(queryTemplate, unit.uri);
            String response = Query.RunQuery(query, endpoint);

            JObject o = JObject.Parse(response);
            JToken results = o["results"];
            JToken bindings = results["bindings"];

            // For each equivalent individual unit found
            foreach (var binding in bindings)
            {
                var equivalentUnitIndividual = binding["unit"]["value"].ToString();
                var equivalentUnitClass = binding["class"]["value"].ToString();
                
                // Get the all of the baseclasses of the equivalent unit's direct class
                List<String> classes = new List<String>();
                classes.Add(equivalentUnitClass);
                classes.AddRange(RecursivelyGetBaseClasses(equivalentUnitClass, endpoint));

                /* Iterate over the individual's baseclasses, which are ordered by ancestry (immediates first),
                 * and when if/when we find a C# class that has a matching "classUri",
                 * then create an instance of that class, corresponding to the individual unit,
                 * and add it to the return using "yield"
                 */
                foreach (var clazz in classes)
                {
                    Assembly asm = typeof(Mapping).Assembly;
                    var validTypes = GetTypesWithMatchingClassUri(asm, clazz);
                    if (validTypes.Count() > 0)
                    {
                        var targetClass = validTypes.FirstOrDefault();
                        ConstructorInfo ctor = targetClass.GetConstructor(new[] { typeof(Uri), typeof(Uri) });
                        yield return ctor.Invoke(new object[] { new Uri(equivalentUnitIndividual), endpoint }) as qudt4dt.Unit;
                        
                    }
                }
            }
        }
    }

    public partial class Unit
    {
        /// <summary>
        /// Get qudt4dt.Unit objects marked as equivalent to this one.
        /// Uses the same SPARQL endpoint as this individual.
        /// </summary>
        /// <returns>A list of equivalent objects</returns>
        public IEnumerable<Unit> GetEquivalents()
        {
            return Mapping.GetEquivalents(this, myEndpoint);
        }
    }
}
