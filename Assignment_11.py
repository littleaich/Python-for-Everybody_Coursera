# Use the file name regex_sum_42.txt as the file name OR
# Use the file name regex_sum_296176.txt as the file name
import re

delim_01 = ' '
delim_02 = ':'
#fname = raw_input("Enter file name: ")
#fname = 'regex_sum_42.txt'
fname = 'regex_sum_296176.txt'
try:
    fhand = open(fname)
except:
    print 'Cannot open the file: %s' % fname
    exit()

num_list = list()
for line in fhand :
    num_list_str = re.findall('[0-9]+', line)
    if len(num_list_str) > 0 :
        #print num_list
        for num_str in num_list_str :
            num_list.append(int(num_str))

print sum(num_list)
