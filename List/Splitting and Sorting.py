# Exercise 14

"""     Write a program to open the file romeo.txt and read it line by line. For each line, 
        split the line into a list of words using the split function. For each word, check to see if the word is already in a list. 
        If the word is not in the list, add it to the list. When the program completes, 
        sort and print the resulting words in alphabetical order.       """

file = input('Enter file name: ')

# quit program if file not available
try:
    r_file = open(file)
except:
    print(file,'doesnt exist!')
    quit()

# empty list
list_of_words = list()

# looping through lines
for line in r_file:
    # each word of a line as an element in a list
    words = line.split()
    # lopping through each word in a list
    for word in words:
        # dont add that element which is already in the list
        if word not in list_of_words:
            list_of_words.append(word)


# sorting list alphabetically
list_of_words.sort()
print(list_of_words)

# THE END