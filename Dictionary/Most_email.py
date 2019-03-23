
""" Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address. 
    Look through the dictionary using a maximum loop to find who has the most messages and print how many messages the person has."""

name = input("Enter file name: ")

# opens file
try:
        file = open(name)
except:
        print(name, "file doesn't exist")
        quit()

# empty dictionary for counting
counts = dict()

# looping through each line in file
for line in file:
    # interested in lines that start with From
    if line.startswith('From'):
        words = line.split()
        # two 'From's for single message, ignoring duplicate counts
        if len(words) > 2:
            counts[words[1]] = counts.get(words[1], 0) + 1


email = None
count = None

# looping through each key, value in dictionary
for key, value in counts.items():
    # email of the person with most messages and its count
    if count is None or value > count:
        email = key
        count = value

if email != None:
        print(email, 'has most messages of',count)
else:
        print('Inappropraite file to compute.')

# THE END