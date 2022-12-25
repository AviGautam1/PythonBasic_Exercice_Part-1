'''
Write a Python program which accepts a sequence of comma-separated numbers
from user and generate a list and a tuple with those numbers.
'''

num = input("Enter some comma seprated numbers : ")
list = num.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

'''
output = 
Enter some comma seprated numbers : 2,3,4,4
List :  ['2', '3', '4', '4']
Tuple :  ('2', '3', '4', '4')
'''