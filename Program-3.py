# Write a Python program to display the current date and time.

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

'''
date.strftime(format) returns a string representing the date, 
controlled by an explicit format string. 
Format codes referring to hours, minutes or seconds will see 0 values.
'''

'''
output = 
now = 2022-12-25 07:06:59.508301
date and time = 25/12/2022 07:06:59
'''