using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net;
using System.IO;

namespace qudt4dt
{
    class Query
    {
        /// <summary>
        /// Perform a SPARQL query on the given endpoint
        /// </summary>
        /// <param name="query"></param>
        /// <param name="endpoint"></param>
        /// <returns>String formatted JSON result</returns>
        public static String RunQuery(String query, Uri endpoint)
        {
            Uri uri_query;
            Uri.TryCreate(endpoint, "/qudt4dt/query?", out uri_query);

            String safeQuery = query.Replace("#", "%23");
            String UrlRequest = uri_query + String.Format("query={0}&should-sponge=soft&debug=on&format=application/json&save=display&output=json", safeQuery);
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
    }
}
