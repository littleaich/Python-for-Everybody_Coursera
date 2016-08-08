# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

# example urls used in this program
# http://python-data.dr-chuck.net/known_by_Fikret.html
# http://python-data.dr-chuck.net/known_by_Jakob.html

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL - ')
count = int(raw_input('Enter count - '))
pos = int(raw_input('Enter position - '))

n = 1 # 1 is for the given page
name_last = ''
while n <= count :
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    # Retrieve all of the anchor tags
    tag = soup('a')[pos-1]
    url = tag.get('href', None)
    name_last = tag.contents[0]
    print name_last
    n += 1
