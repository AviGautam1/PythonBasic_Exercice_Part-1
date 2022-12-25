'''
Write a Python program to print the calendar of a given month and year.

Note: Use 'calendar' module.
'''

import calendar

y = int(input("Enter The Year You Want : " ))
m = int(input("Enter The Month You Want : " ))

print("EXpected Calender Is : ", calendar.month(y, m))

'''
output = 
Enter The Year You Want : 2023
Enter The Month You Want : 1
EXpected Calender Is :      January 2023
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
'''