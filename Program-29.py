'''
Write a Python program to compute the future value of a specified principal amount,
rate of interest, and a number of years.

The formula for future value with compound interest is FV = P(1 + r/n)^nt.
'''

amt = 10000
int = 3.5
years = 7
future_value = amt*((1+(0.01*int)) ** years)
print(round(future_value,2))

# output = 12722.79