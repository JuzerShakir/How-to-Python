# Exercise 13

"""Write a program to read through the file 'mbox-short.txt' and look for lines of the form:

    X-DSPAM-Confidence: 0.8475

    When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line to extract the floating-point number on the line. 
    Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, 
    print out the average spam confidence.

"""

# user will enter name of the file
file_name = input('Enter a file name: ')

# will check if the file exists with that name
try:
    # reads file
    open_file = open(file_name, 'r')
# quits the program if no file found
except:
    print('No such file exists in this directory with this file name:', file_name)
    quit()

total = 0
count = 0

# loop through each line in the file
for line in open_file:
    # count total spam confidence value 
    if line.startswith('X-DSPAM-Confidence:'):
        total = total + float(line[19:])
        count = count + 1

# show average
print('Average spam confidence:', total/count)


# THE END