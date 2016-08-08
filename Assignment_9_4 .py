# Use the file name mbox-short.txt as the file name
import string
delim = ' '
#fname = raw_input("Enter file name: ")
fname = 'mbox-short.txt'
try:
        fhand = open(fname)
except:
        print 'Cannot open the file: %s' % fname
        exit()

counts = dict()
max_word = ''
max_val = -1
for line in fhand :
        if line.startswith('From ') :
                words = line.split(delim)
                word = words[1]
                counts[word] = counts.get(word,  0) + 1
                if counts[word] > max_val :
                        max_word = word
                        max_val = counts[word]

print max_word,  max_val

