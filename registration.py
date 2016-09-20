import json
import urllib2

data = {
    'token': '68aa6c44c4ca59529c1676cdbab9b875',
    'github': 'https://github.com/Dcampb007/Code2040API'
}

req = urllib2.Request('http://challenge.code2040.org/api/register')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))
