# Exercise 16

""" This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the "From" line by 
    finding the time string and then splitting that string into parts using the colon character. 
    Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.  """

name = input("Enter file name: ")

# opens file
file = open(name)

# empty dictionary for counting
counts = dict()

# looping through each line in file
for line in file:
    # interested in lines that start with From
    if line.startswith('From'):
        words = line.split()
        # two 'From's for single message, so just considering which has time
        if len(words) > 2:
            # selecting the time
            time = words[5]
            # splitting time
            time_split = time.split(':')
            # first element is hour
            hour = time_split[0]
            # increases count by 1 if the hour exists or intializes with value 0 if not and then adds 1 
            counts[hour] = counts.get(hour, 0) + 1

# sorting dictionary with respect to hours (key) in ascedning order
sorted_counts = sorted(counts.items())

print(sorted_counts)

# THE END