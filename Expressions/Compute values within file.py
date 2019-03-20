

""" Suming up all 'X-DSPAM-Confidence' values from 'mbox.txt' file """

import re

file_name = input('Enter file name: ')

try:
    file = open(file_name)
except:
    print('No such file found! Try again!')
    quit()

list_num = list()

for line in file:
    num = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)

    # skip lists if we have null or more then 1 element (number)
    if len(num) != 1: continue

    # extracting that number from list, converting to float and adding to list
    list_num.append(float(num[0]))

# suming up all confidence value in the list
print(sum(list_num))

# THE END