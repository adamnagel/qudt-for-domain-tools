__author__ = 'adam'
import urllib
import json

### Define query function ###
def query(query, queryURL, format="application/json"):
    params={
        "should-sponge": "soft",
        "debug": "on",
        "timeout": "",
        "format": format,
        "save": "display",
        "fname": "",
        "output":"json",
        "query":query
    }
    querypart=urllib.urlencode(params)
    response = urllib.urlopen(queryURL,querypart).read()
    return json.loads(response)

### Define update function ###
def update(update, baseURL):
    params={
        "update":update
    }
    querypart=urllib.urlencode(params)
    response = urllib.urlopen(baseURL,querypart).read()