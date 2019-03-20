
""" Write a program to prompt the user for hours and rate per hour to compute gross pay. """

# asking no. of hours worked
hours = input('Enter Hours:')

# asking rate per hour
rate = input('Emter Rate:')

# converting inputs to floats & calculating pay
pay = float(hours) * float(rate)

# Total Pay
print('Pay: ', pay)

# THE END