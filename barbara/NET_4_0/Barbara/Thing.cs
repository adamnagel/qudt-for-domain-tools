using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net;
using System.IO;
using Newtonsoft.Json.Linq;
using System.Reflection;

namespace owl
{
    public class Thing
    {
        public Thing(Uri identity,Uri endpoint)
        {
            uri = identity;
            String newData = QuerySelf(endpoint);
            SetProperties(newData);
        }
        public Uri uri;

        protected String QuerySelf(Uri endpoint)
        {
            Uri uri_query;
            Uri.TryCreate(endpoint, "/qudt4dt/query?", out uri_query);

            String query = BuildQuery_MoreDataOnThis();
            String UrlRequest = uri_query + String.Format("query={0}&should-sponge=soft&debug=on&format=application/json&save=display&output=json", query);
            HttpWebRequest request = WebRequest.Create(UrlRequest) as HttpWebRequest;
            String s_Response;
            using (HttpWebResponse response = request.GetResponse() as HttpWebResponse)
            {
                if (response.StatusCode != HttpStatusCode.OK)
                    throw new Exception(String.Format("Server error (HTTP {0}: {1}).", response.StatusCode, response.StatusDescription));
                using (Stream stream = response.GetResponseStream())
                {
                    StreamReader reader = new StreamReader(stream, Encoding.UTF8);
                    s_Response = reader.ReadToEnd();
                }
            }

            return s_Response;
        }

        protected String BuildQuery_MoreDataOnThis()
        {
            String template = @"PREFIX owl: <http://www.w3.org/2002/07/owl#> 
SELECT ?predicate ?object 
WHERE {{ 
    <{0}> ?predicate ?object . 
    ?predicate a owl:DatatypeProperty
}}";
            return String.Format(template, uri.ToString()).Replace("#", "%23");
        }

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
