# Write a Python program to get a string which is n (non-negative integer) copies of a given string.

# common solution
def larger_string(str, n):
   result = ""
   for i in range(n):
      result = result + str
   return result

print(larger_string('abc', 2))
print(larger_string('.py', 3))

# my solution
my_str = str(input("Enter Any Keyword : " ))
num_copies = int(input("Enter Number Of Copies : " ))
print(num_copies * my_str)

'''
output = 
abcabc
.py.py.py
Enter Any Keyword : avi
Enter Number Of Copies : 5
aviaviaviaviavi
'''