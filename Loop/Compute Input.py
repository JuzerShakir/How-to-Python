
""" Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, 
    and average of the numbers. If the user enters anything other than a number,  detect their mistake using try and 
    except and print an error message and skip to the next number."""
   

num = input('Enter a number: ')

# if users inputs done, quit program
if num == 'done':
    quit()

# initializing values to be calculated
count = 0
sum = 0
avg = 0

# asking user for a number until you type done
while num != 'done':
    # checking if its numeric input
    try:
        sum = sum + float(num)
        count = count + 1
    #if not, then invalid
    except:
        print('Invalid input')

    # asking for next number
    num = input('Enter a number: ')

# calc all inputs avg
avg = sum / count
print(sum, count, avg)

# THE END