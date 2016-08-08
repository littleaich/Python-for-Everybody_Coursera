# Use the file name mbox-short.txt as the file name
import string
delim_01 = ' '
delim_02 = ':'
#fname = raw_input("Enter file name: ")
fname = 'mbox-short.txt'
try:
        fhand = open(fname)
except:
        print 'Cannot open the file: %s' % fname
        exit()

counts = dict()
for line in fhand :
        if line.startswith('From ') :
                words = line.split(delim_01)
                word = words[6]
                tmp = word.split(delim_02)
                hour = tmp[0]
                counts[hour] = counts.get(hour,  0) + 1

lst = list()
for key,  val in counts.items() :
        lst.append((key,  val))

lst.sort()

for key,  val in lst :
        print key,  val
