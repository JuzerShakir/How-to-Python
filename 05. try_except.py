# Exercise 5

""" Rewrite your pay program (Ex 4) using try and except so that your program handles non-numeric input gracefully by printing a message and 
    exiting the program. The following shows two executions of the program: """

try:
    # ask hours worked
    hours = float(input('Enter Hours: '))
    # ask rate per hour
    rate = float(input('Enter Rate: '))
except:
    print('Error, please enter numeric input')
    quit()

# pay for who worked more than 40 hours
if hours > 40:
    # pay for 40 hours they worked
    pay = rate * 40
    # calc payment for 40+ hrs
    extra_time = hours - 40
    extra_pay = ((rate * 1.5) * extra_time)
    print('Pay:', pay + extra_pay)

# pay for less than 40 hours
else:
    pay = hours * rate
    print('Pay:', pay)

# THE END