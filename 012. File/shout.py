# Exercise 12

"""Write a program to read through a file 'mbox-short.txt' and print the contents of the file (line by line) all in upper case."""

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

# loop through each line in the file upper case it
for line in open_file:
    print(line.upper())

# THE END