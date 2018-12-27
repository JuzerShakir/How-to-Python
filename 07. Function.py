# Exercise 7

""" Rewrite your pay computation (Ex 5) with time-and-a-half for overtime 
    and create a function called computepay which takes two parameters (hours and rate) """

try:
    # ask hours worked
    hours = float(input('Enter Hours: '))
    # ask rate per hour
    rate = float(input('Enter Rate: '))
except:
    # if not numeric, quit program
    print('Error, please enter numeric input')
    quit()

# function computing pay
def computepay(hours, rate):
    # pay for who worked more than 40 hours
    if hours > 40:
        # pay for 40 hours they worked
        pay = rate * 40
        # calc payment for 40+ hrs
        extra_time = hours - 40
        extra_pay = ((rate * 1.5) * extra_time)
        # total
        total_pay = pay + extra_pay
        print('Pay:', total_pay)

    # pay for less than 40 hours
    else:
        total_pay = hours * rate
        print('Pay:', total_pay)

    return total_pay

# compute pay of users
computepay(hours, rate)

# THE END