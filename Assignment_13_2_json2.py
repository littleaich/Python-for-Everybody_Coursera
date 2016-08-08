# http://python-data.dr-chuck.net/comments_42.json
# http://python-data.dr-chuck.net/comments_296182.json

import urllib
import json

url = raw_input('Enter location: ')
if len(url) < 1 :
    print 'Blank URL'
    exit()

try :
    print 'Retrieving', url
    uhand = urllib.urlopen(url)
    data = uhand.read()
    print 'Retrieved',len(data),'characters'
except :
    print 'Invalid URL: %s' % url
    exit()

#print data

json_list = json.loads(data)
# here json.loads() returns a dictionary with two keys 'notes' and 'comments'
#print type(json_list)
json_list = json.loads(data)['comments']
# print type(json_list)

print 'User count:', len(json_list)

print sum( [ int(item['count']) for item in json_list ] )
