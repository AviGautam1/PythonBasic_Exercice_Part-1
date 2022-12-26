# Write a Python program to convert the distance (in feet) to inches, yards, and miles.

d_ft = int(input("Input distance in feet: "))
d_inches = d_ft * 12
d_yards = d_ft / 3.0
d_miles = d_ft / 5280.0

print("The distance in inches is %i inches." % d_inches)        # %i used for integer value
print("The distance in yards is %.2f yards." % d_yards)         # %f used for float value
print("The distance in miles is %.2f miles." % d_miles)


'''
output = 
Input distance in feet: 5
The distance in inches is 60 inches.
The distance in yards is 1.67 yards.
The distance in miles is 0.00 miles.
'''