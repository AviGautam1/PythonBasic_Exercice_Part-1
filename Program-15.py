# Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.

num1 = int(input("Enter First Number : " ))
num2 = int(input("Enter Second Number : " ))
num3 = int(input("Enter Third Number : " ))

if num1 == num2 == num3:
    print(3*(num1+num2+num3))
elif num1 != num2 != num3:
    print(num1+num2+num3)
else:
    print("Oops No Number Found !")

'''
output = 
Case 1 -
Enter First Number : 5
Enter Second Number : 5
Enter Third Number : 5
45

Case 2 -
Enter First Number : 1
Enter Second Number : 5
Enter Third Number : 6
12

'''