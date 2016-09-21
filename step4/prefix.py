import json
import urllib2

data = {
    'token': '68aa6c44c4ca59529c1676cdbab9b875',
}

req = urllib2.Request('http://challenge.code2040.org/api/prefix')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))

dictionary = json.loads(response.read())
prefix = dictionary['prefix']
list_of_words = dictionary['array']
array = []
for i in range(len(list_of_words)):
    try:
        word = (list_of_words[i])
        if prefix != str(word[:len(prefix)]):
            array.append(word)
    except IndexError:
        pass
data['array'] = array
req = urllib2.Request('http://challenge.code2040.org/api/prefix/validate')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
