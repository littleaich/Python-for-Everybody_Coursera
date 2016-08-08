# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
str_check = 'X-DSPAM-Confidence:'
delim = ' '
try:
    fhand = open(fname)
except:
    print 'Cannot open the file: %s' % fname 

total = 0.0
count = 0
for line in fhand:
    if line.startswith(str_check) :
        pos_space = line.find(delim)
        num = float(line[pos_space+1:])
        total += num
        count += 1
        
print 'Average spam confidence:', total/count
