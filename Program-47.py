# Write a Python program to check whether lowercase letters exist in a string.

s = input('Type a word : ' )

for c in s:
    if c.islower():
         print(c)


'''
output = 
Type a word : SHSBXhbs
h
b
s
'''