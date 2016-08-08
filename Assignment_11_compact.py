import re

#fname = 'regex_sum_42.txt'
fname = 'regex_sum_296176.txt'

try:
    fhand = open(fname)
except:
    print 'Cannot open the file: %s' % fname

print sum( [ int(num) for num in re.findall('[0-9]+', fhand.read() ) ] )
