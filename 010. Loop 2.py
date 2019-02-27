# Exercise 10

""" Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the minimum and maximum 
    of the numbers. If the user enters anything other than a number, detect their mistake using try and  except and print an error message 
    and skip to the next number."""

# initialize min and max to nonetype
min = None
max = None

# looping through inputs of user
while True:
    num = input('Enter a number: ')

    # quiting program with reuslts
    if num == 'done':
        print('Minimum =', min, 'Maximum =', max)
        quit()

    # checking for numeric input
    try:
        # converting input to float
        num = float(num)
        # setting first input to both min and max
        if max is None and min is None:
            max = num
            min = num
            continue

        # storing highest number
        elif max < num:
            max = num
            continue

        # storing lowest
        elif min > num:
            min = num
            continue
    # warning for input other than number or done
    except:
        print('Invald input.')
        continue

# THE END