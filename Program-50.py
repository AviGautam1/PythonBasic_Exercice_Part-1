# Write A program to Check if variable is tuple or not.

# initialize tuple
test_tup = (4, 5, 6)

# printing original tuple
print("The original tuple : " + str(test_tup))

# Check if variable is tuple
# using type()
res = type(test_tup) is tuple

# printing result
print("Is variable tuple ? : " + str(res))

'''
output = 
The original tuple : (4, 5, 6)
Is variable tuple ? : True
'''
