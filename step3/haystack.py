import json
import urllib2

data = {
    'token': '68aa6c44c4ca59529c1676cdbab9b875',
}

req = urllib2.Request('http://challenge.code2040.org/api/haystack')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))

dictionary = json.loads(response.read())
needle = dictionary['needle']
list_of_words = dictionary['haystack']
for i in range(len(list_of_words)):
    if needle == list_of_words[i]:
        data['needle'] = i

req = urllib2.Request('http://challenge.code2040.org/api/haystack/validate')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
