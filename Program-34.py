# Write a Python program to calculate sum of digits of a number.

n = int(input("Enter The Numbers : " ))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)

'''
output = 
Enter The Numbers : 2345
The total sum of digits is: 14
'''