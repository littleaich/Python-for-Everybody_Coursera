# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

# example urls used in this program
# http://python-data.dr-chuck.net/comments_42.html
# http://python-data.dr-chuck.net/comments_296181.html

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
count_total = 0
for tag in tags:
    # Look at the parts of a tag
    #print 'TAG:',tag
    #print 'URL:',tag.get('href', None)
    #print 'Contents:',tag.contents[0]
    #print int(tag.contents[0])
    #print 'Attrs:',tag.attrs
    count_total += int(tag.contents[0])

print count_total
