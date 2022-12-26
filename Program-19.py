# Write a Python program to check whether a specified value is contained in a group of values.

# my solution
values = int(input("Enter Any Number : " ))
lst = [2, 4, 5, 1, 8]

if values in lst:
    print(True)
else:
    print(False)

# common solution
def is_group_member(group_data, n):
   for value in group_data:
       if n == value:
           return True
   return False
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))


'''
output = 
Case-1
Enter Any Number : 5
True
True
False

Case-2
Enter Any Number : 12
False
True
False

'''