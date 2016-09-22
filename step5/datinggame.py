import json, urllib2, time
from datetime import timedelta
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

data = {
    'token': '68aa6c44c4ca59529c1676cdbab9b875',
}

# Initial request to the API to get the JSON object
req = urllib2.Request('http://challenge.code2040.org/api/dating')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))

# Load the object into a variable
time_dict = json.loads(response.read())

# Assigning the values of each key to its own variable
date_stamp = time_dict['datestamp']
interval = time_dict['interval']

# parsing the date_stamp string into a datetime object
parsed_stamp = parse(date_stamp)

# adds the seconds to the datetime object.
parsed_stamp += relativedelta(seconds=interval)

# Adding the Z to the str to indicate that its in UTC time.
parsed_stamp = parsed_stamp.isoformat()[:19] + 'Z'

# Adding the key/value pair to the data dictionary
data['datestamp'] = parsed_stamp

# Final Post request to push new json to the API
req = urllib2.Request('http://challenge.code2040.org/api/dating/validate')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
