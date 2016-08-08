# example urls used in this program
# http://python-data.dr-chuck.net/comments_42.xml
# http://python-data.dr-chuck.net/comments_296178.xml

import urllib
import xml.etree.ElementTree as ET

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

tree = ET.fromstring(data)

elem_list = tree.findall('comments/comment/count')
#elem_list = tree.findall('..//count')
#print len(elem_list)

print sum( [ int(elem.text) for elem in elem_list ] )
