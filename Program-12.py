# Write a Python program to calculate number of days between two dates.

from datetime import date

first_date = date(2022, 12, 25)
last_date = date(2023, 1, 1)

result = last_date - first_date
print(result.days)
print(f'Hurrah !! New Year Coming In {result.days} Days')

'''
output = 
7
Hurrah !! New Year Coming In 7 Days
'''

