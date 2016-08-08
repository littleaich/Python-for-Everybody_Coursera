# Use the file name mbox-short.txt as the file name
delim = ' '
fname = raw_input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print 'Cannot open the file: %s' % fname

count = 0
for line in fhand :
    if line.startswith('From ') :
        words = line.split(delim)
        print(words[1])
        count += 1

print 'There were', count, 'lines in the file with From as the first word'

