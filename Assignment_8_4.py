# Use the file name romeo.txt as the file name
fname = raw_input("Enter file name: ")
delim = ' '
try:
    fhand = open(fname)
except:
    print 'Cannot open the file: %s' % fname 

words = list()
for line in fhand :
    line = line.rstrip()
    tmpList = line.split(delim)
    for word in tmpList :
        if not words.__contains__(word) :
            words.append(word)

words.sort()
print words
