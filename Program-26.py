# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

num1 = int(input("Enter First Number : " ))
num2 = int(input("Enter Second Number : " ))
num3 = int(input("Enter Third Number : " ))

if num1 == num2 or num2 == num3 or num3 == num1:
    print(0)
else:
    print(num1 + num2 + num3)

'''
output = 
Enter First Number : 1
Enter Second Number : 2
Enter Third Number : 2
0

Enter First Number : 2
Enter Second Number : 3
Enter Third Number : 6
11

'''