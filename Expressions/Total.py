""" Finding numbers in a Haysack """

# needed for extratcing texts from strings
import re

file_name = input('Enter file name: ')

try:
    file = open(file_name)
except:
    print('No such file found! Try again!')
    quit()

total = 0

for line in file:
    # will extract any integer and will return list of them for each line
    num_list = re.findall('[0-9]+', line)

    # if no numbers found in a line, skip
    if len(num_list) == 0: continue
    #print(num)

    # coverting elements in a list to int format for calculation
    for num in num_list:
        total = total + int(num)

# outputs total of all integers found in a file
print(total)

# THE END