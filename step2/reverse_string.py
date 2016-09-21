import json
import urllib2

data = {
    'token': '68aa6c44c4ca59529c1676cdbab9b875',
}

req = urllib2.Request('http://challenge.code2040.org/api/reverse')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))

string = response.read()
response = string[::-1]
data['string'] = response

req = urllib2.Request('http://challenge.code2040.org/api/reverse/validate')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
