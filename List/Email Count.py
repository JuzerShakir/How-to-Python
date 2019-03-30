name = input("Enter file name: ")

# opens file
try:
        file = open(name)
except:
        print(name, "file doesn't exist")
        quit()

count = 0

# looping through each line in file
for line in file:
    # interested in lines that start with From
    if line.startswith('From '):
        # splits each words into key elements by spaces
        split_line = line.split()
        # increamenting count
        count = count + 1
        print(split_line[1])

# if undesired file was input
if count != 0:
    print("There were", count, "lines in the file with 'From' as the first word")
else:
    print('Please input desired file name for computation.')

# THE END