

""" Extracting emails from 'mbox.txt' file starting line with 'From' """

# needed for extratcing texts from strings
import re

file_name = input('Enter file name: ')

try:
    file = open(file_name)
except:
    print('No such file found! Try again!')
    quit()

# empty list for all email ids
emails = list()

# looping through each line and finding line starting from 'From ', extracting email
for line in file:
    id = re.findall('^From (\S+@\S+)', line)
    # just making sure we have 1 email
    if len(id) != 1: continue
    # adding to our list
    emails.extend(id)

print('Numeber of email id\'s: ', len(emails))

# empty dictionary for number of mails done by each email ids
email_count = dict()


for email in emails:
    # adding items to dictionary or if it exists increamenting by 1
    email_count[email] = email_count.get(email, 0) + 1

highest_count = 0

# gives count and email id of the user which has done highest mails
for key, value in email_count.items():
    if highest_count < value: 
        highest_count = value
        highest_mail = key

print(highest_count, 'is highest number of mails done by', highest_mail, 'email id.')

# THE END