'''
Write a Python program which will return true if the two given
integer values are equal or their sum or difference is 5
'''


# my solution
num1 = int(input("Enter First Number : " ))
num2 = int(input("Enter Second Number : " ))

if num1 == num2:
    print(True)
elif num1 - num2 == 5 or num2 - num1 == 5:
    print(True)
elif num1 + num2 == 5 or num2 + num1 == 5:
    print(True)
else:
    print(False)

# common solution
#def test_number5(x, y):
#   if x == y or abs(x-y) == 5 or (x+y) == 5:
 #      return True
 #  else:
 #      return False
#print(test_number5(7, 2))
#print(test_number5(3, 2))
#print(test_number5(2, 2))
#print(test_number5(7, 3))
#print(test_number5(27, 53))


'''
output =
Case-1
Enter First Number : 5
Enter Second Number : 5
True

Case-2
Enter First Number : 15
Enter Second Number : 10
True

Case-3
Enter First Number : 2
Enter Second Number : 4
False

'''