# Write a Python program to input a number, if it is not a number generates an error message.

while True:
    try:
        a = int(input("Input a number: "))
        print("This Is A Number")
        break
    except ValueError:
        print("This is not a number. Try again...")

'''
output =
Input a number: xyz
This is not a number. Try again...
Input a number: 32
This Is A Number

'''
