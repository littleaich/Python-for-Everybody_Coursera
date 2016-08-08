# Use words.txt as the file name
fname = raw_input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print 'Cannot open the file: %s' % fname
    exit()

for line in fhand :
    line = line.rstrip().upper()
    print line
    
#fcontent = fhand.read().upper()
#print fcontent 
