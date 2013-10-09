using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net;
using System.IO;
using Newtonsoft.Json.Linq;
using System.Reflection;
using qudt4dt;

namespace qudt4dt.owl
{
    [ClassUri(@"http://www.w3.org/2002/07/owl#Thing")]
    public class Thing
    {        
        /// <summary>
        /// Constructor for the owl.Thing class
        /// </summary>
        /// <param name="identity">The URI identity of the individual being instantiated</param>
        /// <param name="endpoint">The URI of the SPARQL endpoint to be used to populate the instance</param>
        public Thing(Uri identity,Uri endpoint)
        {
            myEndpoint = endpoint;
            myUri = identity;

            String newData = Query.RunQuery(this.query_GetDataOnThis, myEndpoint);
            SetProperties(newData);
        }
        
        protected Uri myUri;
        /// <summary>
        /// The URI of the individual (instance)
        /// </summary>
        public Uri uri { get { return myUri; } }

        /// <summary>
        /// The SPARQL endpoint from which this individual was instantiated
        /// </summary>
        protected Uri myEndpoint;
        
        /// <summary>
        /// This string is a SPARQL query that gets all DatatypeProperties, with their values, of the individual
        /// </summary>
        protected string query_GetDataOnThis
        {
            get
            {
                String template = @"PREFIX owl: <http://www.w3.org/2002/07/owl#> 
                                    SELECT ?predicate ?object 
                                    WHERE {{ 
                                        <{0}> ?predicate ?object . 
                                        ?predicate a owl:DatatypeProperty
                                    }}";
                return String.Format(template, this.uri.ToString());
            }
        }

        /// <summary>
        /// The URI of the ontology class corresponding to this class
        /// </summary>
        public string classUri
        {
            get
            {
                Type t = this.GetType();
                ClassUri cu = (ClassUri)Attribute.GetCustomAttribute(t, typeof(ClassUri));
                return cu.uri;
            }
        }
        
        /// <summary>
        /// Given the results of "query_GetDataOnThis", set the individual's Fields
        /// </summary>
        /// <param name="query_result">JSON result of the "query_GetDataOnThis"</param>
        protected void SetProperties(String query_result)
        {
            JObject o = JObject.Parse(query_result);

            JToken results = o["results"];
            JToken bindings = results["bindings"];
            foreach (var thing in bindings)
            {
                var predicate = thing["predicate"]["value"].ToString();
                var val = thing["object"]["value"].ToString();

                var propName = predicate.Split('#')[1];

                // Reflect through our properties to see if there are any name matches
                var myField = this.GetType()
                                  .GetFields(BindingFlags.FlattenHierarchy | BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic)
                                  .Where(f => f.Name == propName)
                                  .FirstOrDefault();
                if (myField != null)
                    myField.SetValue(this, Convert.ChangeType(val, myField.FieldType));
            }
        }
    }
}
