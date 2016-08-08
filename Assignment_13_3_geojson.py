import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
# serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    try :
        url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
        print 'Retrieving', url
        uh = urllib.urlopen(url)
        data = uh.read()
        print 'Retrieved',len(data),'characters'
    except :
        print 'Invalid URL: %s' % url
        exit()

    try :
        js = json.loads(str(data))
    except :
        js = None

    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    # print json.dumps(js, indent=4) # shows data in json format

    #lat = js["results"][0]["geometry"]["location"]["lat"]
    #lng = js["results"][0]["geometry"]["location"]["lng"]
    #print 'lat',lat,'lng',lng
    #location = js['results'][0]['formatted_address']
    #print location
    print js['results'][0]['place_id']
